# Goblin Mini Astra

Current skill version: **v2**. This release adds persistent per-user budget defaults, first-use selection, task-only overrides, and `no budget`. Version numbering began at v1; increment the integer for subsequent published skill updates, keeping the README, skill declaration, and footer aligned.

A Codex skill focused on conserving Codex quota while meeting task acceptance criteria. Astra scopes work and resolves important uncertainty; Luna handles substantial work with clear boundaries.

Derived from [Goblin Mini Pro](https://github.com/abangkis/goblin-mini-pro), with quota-conscious routing and an optional authorized GPT Pro decision gate.

## Roles

| Role | Model / reasoning design target | Purpose |
| --- | --- | --- |
| Coordinator | GPT-6 Astra / Low | Scope, routing, integration, and final acceptance |
| Scout | GPT-5.6 Luna / High | Bounded read-only investigation |
| Worker | GPT-5.6 Luna / XHigh | Implementation and debugging with clear acceptance criteria |
| Deep Worker | GPT-5.6 Luna / Max | Selectively address difficult, well-defined local problems |
| Escalation | GPT-6 Astra / Medium | Resolve architectural ambiguity or interacting components |

Small tasks stay with the Coordinator when delegation would add more work. There is no mandatory escalation ladder. Delegation depends on the host's available tools and conditions; a skill cannot change the main task's model or reasoning effort. Select the intended Coordinator runtime in your host. Actual runtime is reported only when authoritative metadata establishes it.

## Quota-conscious workflow

- Inspect only enough to give a delegate a useful boundary.
- Carry relevant context and trusted evidence instead of full conversation history.
- Default to one leaf delegate; the Coordinator may use up to two concurrently for independent tasks when the expected benefit justifies additional quota and coordination overhead. Subagents cannot create subagents.
- Reuse successful investigation and validation while their relevant inputs remain unchanged.
- Escalate based on diagnosed uncertainty, not task length or an unexplained failure.
- Verify the changed boundary without an automatic full Astra audit or redundant tests.

This is a routing baseline, not a measured savings guarantee. API pricing and token counts do not establish Codex subscription quota charges. Quota savings have not been benchmarked.

## Budget defaults and options

On first use, Codex asks for a default: **1 million**, **5 million**, **10 million tokens**, or **your own positive amount**. No number is selected automatically. This one-time setup also applies to simple tasks. Python 3 is required for the bundled standard-library helper, which returns the setup status; Codex asks the question in conversation rather than opening a terminal prompt.

The choice applies to each new task until explicitly changed:

| Example request | This task | Saved default |
| --- | --- | --- |
| No budget instruction | Uses saved default | Unchanged |
| `Use a budget of 2 million tokens for this task` | 2 million tokens | Unchanged |
| `No budget for this task` | No task token ceiling | Unchanged |
| `Change the default budget to 10 million tokens` | Existing task retains its budget unless asked otherwise | 10 million for future tasks |
| `Change the default to no budget` | Existing task retains its budget unless asked otherwise | No ceiling for future tasks |

Follow-up messages and repeated skill invocations retain the current task budget and accumulated usage. A numeric override changes the task's total ceiling, not an additional allowance. Explicitly request use of the saved default again to clear a task override. `No budget` does not disable efficient routing, validation, or actual-usage reporting.

Preferences live in `$CODEX_HOME/skill-settings/goblin-mini-astra/budget.json` (fallback `~/.codex/skill-settings/goblin-mini-astra/budget.json`). They are local to the user/host, survive skill-folder upgrades, and are not included in this repository. Only an explicit default selection/change writes this file. Task overrides are resolved without modifying it.

See [budget setup and helper commands](references/budget-options.md) for first-use behavior, custom values, errors, and precedence. The helper resolves policy; it does not count tokens or enforce a host-level hard stop. Installing or editing the skill does not start setup or choose your default.

### Usage checks and reporting

For nontrivial tasks, the Coordinator keeps a small task-local checkpoint of the initial budget, measured usage, verified progress, and remaining work. It reuses available metadata and checks fresh usage only when that could change a costly delegation, escalation, investigation, or phase decision. There is no dedicated monitoring agent or periodic polling, and checking costs are part of the tradeoff.

Reserve enough room for integration, validation, and handoff. Low account quota discourages optional work with marginal value, while required validation remains mandatory. A budget is not a spending target. Native goals are created only on explicit request, not automatically from the saved preference.

The final report for nontrivial work includes initial effective budget and its source, measured actual tokens, and accounting coverage. Explicitly disabled ceilings are `no budget`; missing usage is `unavailable`; incomplete Coordinator/delegate coverage is `partial`. If the ceiling changes mid-task, retain the initial value and report the current ceiling too. Task usage is not inferred from account-wide quota changes. Simple tasks skip ongoing bookkeeping and budget reporting unless requested, while still inheriting the default. Savings remain unmeasured until comparable outcomes and full overhead can be assessed.

## Install

Ask Codex:

```text
Use $skill-installer to install goblin-mini-astra from
https://github.com/abangkis/goblin-mini-astra
```

Alternatively, copy the skill folder to `~/.codex/skills/goblin-mini-astra/` (or the `skills` directory under your configured `CODEX_HOME`). Include `SKILL.md`, `agents/openai.yaml`, both files in `references/`, and `scripts/budget.py`. Preserve the separate user-settings directory when updating the skill.

## Use

```text
$goblin-mini-astra

Complete the following task, conserving Codex quota while meeting these acceptance criteria:
[task, constraints, and desired outcome]
```

The active mode is `MINI-ASTRA`. A later explicit Goblin mode selection replaces it; asking to stop Goblin mode disables this routing. Discussing or editing the skill does not activate execution mode.

Active task responses end with the loaded skill version, for example:

```text
Active Goblin Mode: MINI-ASTRA v2 | Execution footprint: Coordinator.
```

This identifies the skill instructions in use, not the model version. Existing tasks must load updated instructions before reporting a newer skill version.

## Optional GPT Pro consultation

Pro is a separate decision or audit consultation, never an implied Astra capability or an execution worker. A consultation requires a real Pro target and explicit authorization for the handoff. Required but unavailable Pro consultation pauses dependent execution; optional consultation does not block routine work.

Pro recommendations are checked against current evidence before implementation. Material conflicts require a revised aligned decision or an explicitly approved documented resolution. The detailed procedure is loaded only when needed from [the Pro gate reference](references/pro-decision-gate.md).

## Validation status

Run helper behavior tests with `python -B -m unittest discover -s tests -v`. Tests use project-local isolated settings, covering first-use setup, saved presets/custom defaults, task overrides, no-budget behavior, invalid data, and persistence across processes. They do not alter personal preferences. The initial skill passed restricted structural checks; the official `quick_validate.py` was unavailable due to missing PyYAML. Routing has not been independently runtime-tested or quota-benchmarked.

## License

[MIT](LICENSE), copyright (c) 2026 abangkis.
