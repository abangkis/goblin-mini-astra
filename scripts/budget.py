"""Persistent per-user budget preferences; task resolution never changes them."""
import argparse
import json
import os
from pathlib import Path
import sys


def budget_value(value):
    if value == 'none':
        return None
    if not value.isascii() or not value.isdecimal() or int(value) <= 0:
        raise argparse.ArgumentTypeError('Use a positive integer token count or none.')
    return int(value)


def config_path():
    home = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    return home / 'skill-settings' / 'goblin-mini-astra' / 'budget.json'


def read_default(path):
    if not path.exists():
        return {'status': 'needs_setup', 'choices_tokens': [1000000, 5000000, 10000000],
                'custom_allowed': True}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != 1 or 'default_budget_tokens' not in data:
        raise ValueError('Invalid budget settings schema; explicit repair is required.')
    value = data['default_budget_tokens']
    if value is not None and (type(value) is not int or value <= 0):
        raise ValueError('Invalid saved budget; expected positive integer or null.')
    return {'status': 'ready', 'default_budget_tokens': value}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, default=None,
                        help='Explicit settings file, primarily for isolated tests.')
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('get')
    setting = sub.add_parser('set-default')
    setting.add_argument('tokens', type=budget_value)
    resolving = sub.add_parser('resolve')
    resolving.add_argument('--task-budget', type=budget_value, default=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    path = args.config if args.config is not None else config_path()
    try:
        if args.command == 'set-default':
            # The caller must obtain explicit user selection/change authorization.
            # Only this command writes; resolve/get do not even create directories.
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps({'schema_version': 1,
                                       'default_budget_tokens': args.tokens}, indent=2) + '\n',
                            encoding='utf-8')
            result = read_default(path)
        else:
            result = read_default(path)
            if args.command == 'resolve' and result['status'] == 'ready':
                override = hasattr(args, 'task_budget')
                value = args.task_budget if override else result['default_budget_tokens']
                result.update(effective_budget_tokens=value,
                              source='task_override' if override else 'saved_default',
                              mode='no_budget' if value is None else 'limited')
        print(json.dumps(result))
        return 0
    except (OSError, ValueError) as exc:
        print(json.dumps({'status': 'error', 'message': str(exc)}))
        return 1


if __name__ == '__main__':
    sys.exit(main())
