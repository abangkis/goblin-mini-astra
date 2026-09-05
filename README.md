# Goblin Mini Astra

A Codex skill focused on conserving Codex quota while meeting task acceptance criteria. Astra scopes work and resolves important uncertainty; Luna handles substantial work with clear boundaries.

Derived from [Goblin Mini Pro](https://github.com/abangkis/goblin-mini-pro), with quota-conscious routing and an optional authorized GPT Pro decision gate.

## Roles

| Role | Model / reasoning design target | Purpose |
| --- | --- | --- |
| Coordinator | GPT-6 Astra / Medium | Scope, routing, integration, and final acceptance |
| Scout | GPT-5.6 Luna / High | Bounded read-only investigation |
| Worker | GPT-5.6 Luna / XHigh | Implementation and debugging with clear acceptance criteria |
| Deep Worker | GPT-5.6 Luna / Max | Selectively address difficult, well-defined local problems |
| Escalation | GPT-6 Astra / XHigh | Resolve architectural ambiguity or interacting components |

Small tasks stay with the Coordinator when delegation would add more work. There is no mandatory escalation ladder. Delegation depends on the host's available tools and conditions; a skill cannot change the main task's model or reasoning effort. Select the intended Coordinator runtime in your host. Actual runtime is reported only when authoritative metadata establishes it.

## Quota-conscious workflow

- Inspect only enough to give a delegate a useful boundary.
- Carry relevant context and trusted evidence instead of full conversation history.
- Default to one leaf delegate; the Coordinator may use up to two concurrently for independent tasks when the expected benefit justifies additional quota and coordination overhead. Subagents cannot create subagents.
- Reuse successful investigation and validation while their relevant inputs remain unchanged.
- Escalate based on diagnosed uncertainty, not task length or an unexplained failure.
- Verify the changed boundary without an automatic full Astra audit or redundant tests.

This is a routing baseline, not a measured savings guarantee. API pricing and token counts do not establish Codex subscription quota charges. Quota savings have not been benchmarked.

## Install

Ask Codex:

```text
Use $skill-installer to install goblin-mini-astra from
https://github.com/abangkis/goblin-mini-astra
```

Alternatively, copy the skill folder to `~/.codex/skills/goblin-mini-astra/` (or the `skills` directory under your configured `CODEX_HOME`). The required package files are `SKILL.md`, `agents/openai.yaml`, and `references/pro-decision-gate.md`.

## Use

```text
$goblin-mini-astra

Complete the following task, conserving Codex quota while meeting these acceptance criteria:
[task, constraints, and desired outcome]
```

The active mode is `MINI-ASTRA`. A later explicit Goblin mode selection replaces it; asking to stop Goblin mode disables this routing. Discussing or editing the skill does not activate execution mode.

## Optional GPT Pro consultation

Pro is a separate decision or audit consultation, never an implied Astra capability or an execution worker. A consultation requires a real Pro target and explicit authorization for the handoff. Required but unavailable Pro consultation pauses dependent execution; optional consultation does not block routine work.

Pro recommendations are checked against current evidence before implementation. Material conflicts require a revised aligned decision or an explicitly approved documented resolution. The detailed procedure is loaded only when needed from [the Pro gate reference](references/pro-decision-gate.md).

## Validation status

The initial skill passed restricted YAML structure, metadata, local-reference, and unfinished-scaffold checks. The official `quick_validate.py` could not run because PyYAML was unavailable. Routing was reviewed against representative cases but has not been independently runtime-tested or quota-benchmarked.

## License

[MIT](LICENSE), copyright (c) 2026 abangkis.
