import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'scripts' / 'budget.py'


class BudgetTests(unittest.TestCase):
    def setUp(self):
        artifacts = ROOT / '.test-artifacts'
        artifacts.mkdir(exist_ok=True)
        self.folder = tempfile.TemporaryDirectory(dir=artifacts)
        self.addCleanup(self.folder.cleanup)
        self.path = Path(self.folder.name) / 'settings' / 'budget.json'

    def run_cli(self, *args, expected=0):
        result = subprocess.run([sys.executable, '-B', str(SCRIPT), '--config', str(self.path), *args],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, expected, result.stderr + result.stdout)
        return json.loads(result.stdout) if result.stdout else None

    def test_missing_prompts_without_writing_even_with_override(self):
        for args in [('get',), ('resolve',), ('resolve', '--task-budget', 'none')]:
            data = self.run_cli(*args)
            self.assertEqual(data['status'], 'needs_setup')
            self.assertEqual(data['choices_tokens'], [1000000, 5000000, 10000000])
        self.assertFalse(self.path.parent.exists())

    def test_presets_custom_and_default_changes_persist(self):
        for amount in [1000000, 5000000, 10000000, 2345678]:
            self.run_cli('set-default', str(amount))
            data = self.run_cli('resolve')
            self.assertEqual(data['effective_budget_tokens'], amount)
            self.assertEqual(data['source'], 'saved_default')

    def test_overrides_never_mutate_saved_default(self):
        self.run_cli('set-default', '5000000')
        before = self.path.read_bytes()
        for value, expected in [('2000000', 2000000), ('none', None)]:
            data = self.run_cli('resolve', '--task-budget', value)
            self.assertEqual(data['effective_budget_tokens'], expected)
            self.assertEqual(data['source'], 'task_override')
            self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(self.run_cli('resolve')['effective_budget_tokens'], 5000000)

    def test_explicit_no_budget_default_and_numeric_override(self):
        self.run_cli('set-default', 'none')
        self.assertEqual(self.run_cli('resolve')['mode'], 'no_budget')
        self.assertEqual(self.run_cli('resolve', '--task-budget', '100')['effective_budget_tokens'], 100)
        self.assertIsNone(self.run_cli('get')['default_budget_tokens'])

    def test_resolution_does_not_claim_native_configuration_or_measurement(self):
        self.run_cli('set-default', '10000000')
        for args in [('resolve',), ('resolve', '--task-budget', 'none')]:
            data = self.run_cli(*args)
            self.assertEqual(data['native_budget_state'], 'unchecked')
            self.assertIsNone(data['usage_tokens'])
        self.assertEqual(self.run_cli('get')['default_budget_tokens'], 10000000)

    def test_invalid_values_preserve_existing_settings(self):
        self.run_cli('set-default', '1000000')
        before = self.path.read_bytes()
        for value in ['0', '-1', '1.5', 'abc', 'true']:
            self.run_cli('set-default', value, expected=2)
            self.assertEqual(self.path.read_bytes(), before)

    def test_bad_settings_report_error_without_overwrite(self):
        self.path.parent.mkdir()
        for text in ['{bad', '{}', '{"schema_version":1,"default_budget_tokens":true}',
                     '{"schema_version":1,"default_budget_tokens":0}']:
            self.path.write_text(text)
            self.assertEqual(self.run_cli('resolve', expected=1)['status'], 'error')
            self.assertEqual(self.path.read_text(), text)

    def test_codex_home_storage_survives_task_processes(self):
        env = dict(os.environ, CODEX_HOME=self.folder.name)
        for args in [('set-default', '5000000'), ('resolve',)]:
            run = subprocess.run([sys.executable, '-B', str(SCRIPT), *args], env=env,
                                 capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)
        saved = Path(self.folder.name) / 'skill-settings/goblin-mini-astra/budget.json'
        self.assertEqual(json.loads(saved.read_text())['default_budget_tokens'], 5000000)


if __name__ == '__main__':
    unittest.main()
