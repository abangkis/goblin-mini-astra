# Budget setup and options (v2)

The helper uses Python 3's standard library. Run `scripts/budget.py` relative to the loaded skill directory. It returns JSON; the Coordinator asks the user through the available input tool or conversation. It never opens a terminal prompt, monitors usage, changes the model, or creates a native goal.

## First activation

Run `python scripts/budget.py resolve` once when first activating the skill for a task. If the user supplied a task budget, pass `--task-budget <positive-integer>` or `--task-budget none` for `no budget`.

`needs_setup` means no saved preference exists. Ask in the user's language:

> Budget default untuk setiap task Goblin Mini Astra: 1 juta, 5 juta, 10 juta token, atau masukkan angka sendiri?

Use suggested answers 1 juta, 5 juta, 10 juta when the input tool supports them; its free-text field accepts custom values. Do not preselect a policy on the user's behalf. Normalize an unambiguous answer such as `2 juta` to `2000000`; clarify ambiguous or nonpositive values. Wait for the answer before starting task execution. This setup also applies to simple tasks and first-use task overrides; retain the override while collecting the default. Editing/installing the skill does not activate it or request setup.

After selection, run `python scripts/budget.py set-default <integer>`, then resolve the current task again. Persist only the user's actual choice, never an illustrative number. Successful readback confirms saving. If writing is denied, report that the default was not saved, request the required host permission, and retain the selected value only for the current task if needed; never claim persistence succeeded. An unreadable or malformed file is `error`, not `needs_setup` or `no budget`: do not silently replace it or repeatedly retry. Ask for explicit repair/selection or a task-local override.

## Precedence and lifetime

| User request | Effective task budget | Saved default |
| --- | --- | --- |
| No task override | Saved default | Unchanged |
| `Budget task ini 2 juta token` | 2,000,000 | Unchanged |
| `No budget untuk task ini` | No task token ceiling | Unchanged |
| `Ubah default menjadi 10 juta token` | New default for a new task | 10,000,000 |
| `Ubah default menjadi no budget` | No ceiling by default for new tasks | Explicitly disabled (`null`) |
| Change default plus a separate task budget | Explicit task override | New selected default |

Only an explicit default-setting request invokes `set-default`. A plain budget or `no budget` always applies to the current task alone. To re-enable budgeting for a no-budget task, supply a numeric task override; to restore the saved default for that task, explicitly request it and resolve again without an override.

Snapshot effective budget, source, and baseline in the current task checkpoint. Follow-up messages and repeat invocations within the same unfinished task retain that budget and accumulated usage; do not reset accounting on each turn. Changes to the saved default apply to future tasks, not silently to active tasks. Apply to an active task only if the user asks. When a genuinely new task starts, resolve afresh. A numeric mid-task change sets the total task ceiling from the existing baseline, not an additional allowance.

`no budget` disables only the task token ceiling. Keep quota-conscious routing, required validation, account quota checks when decision-useful, authorization rules, and nontrivial-task usage reporting. Never redeem reset credits or change account spending settings as a consequence.

## Storage and accounting

Store only `schema_version` and `default_budget_tokens` in `$CODEX_HOME/skill-settings/goblin-mini-astra/budget.json`, falling back to `~/.codex/skill-settings/goblin-mini-astra/budget.json`. This is local user configuration, not cross-device synchronization or model memory. Keep it outside the installed skill/repository so upgrades preserve it and publication excludes personal preferences. `null` is an explicitly saved no-budget default; an absent file is unconfigured.

`get` reads the preference; `resolve` reads and applies a task override without writing; `set-default` writes and reads back the selected preference. `--config <path>` overrides storage for tests; do not use test paths as production defaults. Concurrent default writes use the last completed write; do not run competing preference updates.

The script resolves policy only. It does not enforce a hard cap or count Coordinator/delegate tokens. Use authoritative usage metadata with verified coverage and no double counting. Create a native goal only when explicitly requested and supported; never create one just because a default exists. If unavailable, report a behavioral budget and partial/unavailable usage honestly.

For nontrivial tasks report, for example:

`Budget: 5,000,000 (saved default) | Actual: 820,000 tokens | Coverage: complete through last measurement.`

Use `task override` as source when appropriate, `no budget` for a disabled ceiling, and `unavailable` for missing usage. Simple tasks omit ongoing bookkeeping and the final budget line unless requested; they still perform first-use preference setup and inherit or override the policy.
