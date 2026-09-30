---
name: goblin-mini-astra
description: Coordinate quota-conscious Codex work with a Sol 6.1 Medium Coordinator, bounded Luna workers, selective Sol 6.1 investigation, justified Astra execution, and optional authorized GPT Pro consultation. Use when the user selects Goblin Mini Astra or its active mode continues in the current task. Discussing, creating, or reviewing this skill does not activate its execution mode.
---

# Goblin Mini Astra

Skill version: **v8**. Report the version actually loaded; read updated instructions before adopting them mid-task. Increment this integer and the footer for behavior changes, not documentation-only edits.

Optimize Codex quota per accepted outcome, including handoffs, review, and retries. Sol 6.1 Medium coordinates and handles investigation when efficient; Luna handles predictable bounded work; selective Sol or Astra workers resolve harder uncertainty. Do not trade away acceptance criteria for fewer tokens or agents.

This is a routing baseline, not a measured quota-saving guarantee. API prices, token counts, and reasoning labels do not establish Codex subscription quota charges. Do not embed price ratios or assumed quota multipliers.

## Session mode and runtime

An explicit `$goblin-mini-astra` invocation or selection activates `MINI-ASTRA` for subsequent work in the current task. The latest explicit Goblin mode selection or trustworthy active marker wins. Stop this routing when the user stops Goblin mode or selects another Goblin mode. Do not combine inactive routing policies. If multiple modes are requested without a clear selection, clarify before delegating. If the active mode becomes uncertain after compaction, continue ordinary nondelegated work where possible and clarify before applying this routing.

The Coordinator targets `gpt-6.1-sol` / `medium`. A skill cannot switch the main task's runtime; respect the user's choice and disclose a mismatch once. Do not create a task to obtain the target. Sol 6.1 Light means `low` in host controls; it does not support `none` or `minimal`.

Distinguish design target, requested runtime, and actual runtime. Verify actual model/effort from authoritative metadata or mark it `unverified`.

## Choose the smallest sufficient route

| Role or situation | Requested model / effort | Route when |
| --- | --- | --- |
| Coordinator | `gpt-6.1-sol` / `medium` design target | Scope, routing, user communication, integration, and final acceptance |
| Direct execution | Existing Coordinator | Small work, verified continuations, or bounded investigation the Coordinator can resolve efficiently with its existing context |
| Scout | `gpt-6-luna` / `high` | Read-only questions have a bounded search area and observable answers |
| Routine Worker | `gpt-6-luna` / `xhigh` | Implement a clear solution with explicit acceptance criteria |
| Deep Worker | `gpt-6-luna` / `max` by default; `gpt-6.1-sol` / `low` selectively | Difficult bounded work with sufficient evidence; use Sol Low when cross-component understanding or judgment justifies its cost |
| Investigative Worker | `gpt-6.1-sol` / `high` or `xhigh`; `gpt-6-astra` / `low` for a justified capability gap | Resolve bounded uncertainty and own the resulting fix and targeted validation when efficient |
| Escalation Worker | `gpt-6-astra` / `medium` | Resolve interacting uncertainty, conflicting evidence, consequential architecture, or an ambitious visual direction |

Execute directly when delegation overhead exceeds the remaining work. Do not repeat substantial Coordinator work through a delegate.

Keep Scout and Routine work on Luna when sufficient. Luna Max remains the Deep default for difficult local problems with objective checks. Sol 6.1 Low is a selective alternative, not a wholesale replacement: lower effort does not establish a lower task cost than Luna Max. Compare accepted outcomes, retries, handoffs, Coordinator work, and attributable usage before claiming savings.

For a delegated investigation, choose Sol 6.1 High when evidence, boundaries, and a validation path are clear; choose XHigh when plausible hypotheses, interactions, or edge cases require deeper analysis. Sol 6.1 Max is an exceptional Deep or Investigative profile for very dense, well-defined reasoning with sufficient evidence and objective checks. Name the reason for Max; it is neither a permanent role nor a required step before Astra.

Before requesting Astra, name the unresolved question, why the available Sol or Luna route cannot resolve it efficiently, the evidence needed, and a stopping condition. Astra Low fits a bounded capability gap, such as hypotheses that do not explain the evidence. Use Astra Medium directly for interacting uncertainty, conflicting evidence, consequential architecture, or experience-wide visual tradeoffs when a lighter route would likely repeat work. A long task, vague difficulty, or a failed tool call is not enough. There is no mandatory model ladder or required failed Sol attempt; effort labels are not equivalent capability scores across models.

Keep small questions with the Coordinator. An investigative assignment ends when its question and bounded outcome are verified, or when progress requires new evidence, access, or scope. Let its worker finish a closely coupled fix; hand off a large mechanical remainder to Luna only when saved execution outweighs briefing and review. Pass only unresolved questions and reusable evidence to an escalation, including a separable decision-only consultation. Sol reviews relevant changes without repeating discovery; Astra review is not obligatory. Do not describe Sol Medium as Astra Medium.

### Frontend routing

Frontend work alone does not justify Astra. Sol 6.1 Medium owns design direction and visual judgment by default; Luna implements clear designs, components, responsive behavior, and states. Judge rendered desktop/mobile screens and the primary interaction, not code or build output alone.

Use Astra Low for a specific unresolved visual or interaction problem after a focused Sol revision still misses the stated quality bar. Give it the brief, rendered evidence, the observed gap, and a bounded question; accept a targeted correction rather than restarting the whole frontend. Use Astra Medium directly for a consequential, original visual direction or complex interaction whose requirements and tradeoffs span the experience. This is a routing hypothesis, not proof that Sol or Luna matches Astra's frontend quality. Compare accepted results and attributable usage on representative frontend tasks before claiming savings or retiring Astra from this category.

## Work from the remaining delta

Before routing, identify the unfinished outcome, existing changes, trusted evidence, and uncertainty. Inspect enough to set the boundary and find canonical tooling.

Reuse successful evidence while its inputs remain unchanged; retain source/artifact identity and scope. A commit, push, consultation, or model change alone does not invalidate payload validation.

The Coordinator owns scope, authorization, integration, consequential operations, and final readback. Workers may edit and validate within authorization. Discussion, review, diagnosis, and planning remain read-only without implementation authorization.

## Delegation budget and brief

Default to one leaf subagent. Use at most two concurrently for independent work when time or quality gains justify quota and coordination overhead. Delegate only for a concrete benefit under host rules; invocation alone is insufficient. Workers cannot create subagents.

Request model/effort through host controls. Brief compactly; use a limited/no-history fork when required for overrides. Never silently substitute. If unavailable, disclose and work directly when sufficient; report a blocker if the target was required or direct work is insufficient.

A brief should contain only:

- Role, requested model/effort, and the concrete routing reason.
- Outcome, acceptance criteria, scope/files, and authorization boundaries.
- Current state, source/artifact identity where relevant, trusted evidence, and remaining uncertainty.
- Canonical tooling, minimum validation, and the stopping condition.

Tell the delegate:

> Work only on the unfinished delta within this scope. Reuse the listed successful evidence while its relevant inputs remain unchanged. Do not repeat verified investigation or validation without a concrete reason. Use canonical tooling. Do not create subagents. Return a concise result with changed files, relevant commands/results, evidence locations, unresolved questions, and residual risk. If blocked, identify the failed stage and cause; do not broaden scope or cycle through retries.

While a delegate works, avoid duplicate investigation, competing edits, and frequent polling. Reuse it when continuity saves rediscovery.

## Validation and escalation

Accept work using evidence appropriate to the changed boundary. Start with the narrowest meaningful validation; expand when a failure, changed contract, risk, repository requirement, or acceptance criterion warrants it. Do not lower required quality to meet a quota objective.

Inspect the relevant diff and evidence before acceptance. Do not automatically rerun a worker's passing checks or commission a full Astra audit. A worker's unsupported success claim is not evidence; fill the specific evidence gap.

After failure, distinguish reasoning/code problems from tooling, environment, permissions, and external state. A stronger model does not fix missing access. Retry once only after a causal correction or material new evidence; if the stage fails again, diagnose and escalate a specific reasoning gap or report the blocker. Do not rotate models for an unexplained failure.

An escalation brief preserves successful work and identifies the unresolved question, failed hypothesis, and evidence. It must not restart the whole task. Finish with one consolidated readback of the outcome and relevant outstanding risk.

## Budget default and task overrides

On first activation for each task, read [references/budget-options.md](references/budget-options.md) and run `scripts/budget.py resolve` from the loaded skill directory using Python 3. The helper reads per-user settings outside the skill folder. If no default exists, ask the user to choose 1 million, 5 million, 10 million tokens, or a custom positive amount, then save their actual selection with `set-default`. Wait for selection before task execution; do not invent a default. This setup applies even to simple tasks. The helper returns JSON; the Coordinator presents the question through conversation/input tools.

Use the saved default unless the user supplies a task budget or says `no budget`. Those overrides apply only to this task and must not change the saved preference. Change the persistent default only when the user explicitly asks to change it; an explicit no-budget default is also supported. Preserve the effective budget and accumulated usage across follow-ups/reinvocations; default changes affect future tasks unless the user asks to apply them here. Read the reference for helper commands, errors, storage, and accounting semantics. Editing this skill does not activate budget setup.

## Budget-aware decisions

The user's bundled-budget instruction requests native setup together with every numeric budget in this workflow, whether inherited from the saved default or supplied for this task. Read [references/native-budget.md](references/native-budget.md): resolve the budget, inspect `get_goal`, reuse a matching goal or create the requested native goal when no unfinished goal prevents it, and verify the configured budget. Do not ask a second confirmation for native setup. Apply this numeric-budget setup even to simple tasks. `No budget` requests neither a new native goal nor a native token budget. A saved value or request is not proof of enforcement; verify readback. If native tools are unavailable or an existing unfinished goal conflicts, report the actual limitation rather than asking redundant authorization. Ordinary work outside this selected workflow does not request goal creation.

For a plain-language explanation of what the budget means and what happens near or at the limit, read [references/budget-behavior.md](references/budget-behavior.md). Use it when explaining budgeting to users; keep native configuration and enforcement claims grounded in the current host's verified behavior.

After resolving budget policy, skip ongoing bookkeeping for simple tasks unless requested. For nontrivial work, the Coordinator keeps a compact task-local checkpoint: initial effective budget and source (saved default or task override), measurement baseline/scope, latest measured usage, verified progress, and remaining work. Reuse conversation/checkpoint state; do not create a budget-monitor agent, separate persistent memory system, or periodic polling loop.

Prefer usage metadata already available. Use `get_goal` for task usage at costly decision points and final readback; account quota is a separate signal. Reuse a recent snapshot when still relevant. Account for the read, context replay, reasoning, and reporting overhead; do not spend more measuring than the decision warrants. If metadata is unavailable, record the reason once and follow the agreed fallback rather than repeated retrieval attempts. Include the shared remaining budget and stopping condition in delegate briefs; never allocate the full remainder independently to both workers.

Compare consumption with verified progress. If usage grows without progress, diagnose and change approach; a justified Sol or Astra profile may avoid repeated attempts. Low remaining account quota favors fewer optional investigations and marginal parallel tasks, but never removes required validation. Account-wide quota movement is a caution signal, not usage attributable to this task or a fixed token conversion.

A numeric effective budget is a ceiling, not a spending target. The bundled native setup request does not expand the task objective or authorize unrelated actions. `No budget` skips native setup; if a cap already exists, remove only that cap through supported controls while preserving usage, or disclose the host limitation. Keep quota-conscious routing and required validation. Reserve a task-appropriate portion for integration, validation, and handoff without a fixed percentage. Near the effective limit, prepare a checkpoint and seek a scope/budget decision before further work would exceed it. Do not claim incomplete work is complete or increase/reset a budget to continue. Distinguish a behavioral budget from a verified host-enforced hard cap.

Aim to account for the Coordinator and all delegates from the task baseline, using documented counter semantics. Verify coverage before summing; avoid counting child usage or cached/reasoning components twice. Mark missing coverage as partial, and distinguish measured usage from estimates. Do not infer exact totals from answer length.

## Optional GPT Pro decision gate

GPT Pro remains an optional decision/audit consultation, separate from Astra routing. Astra, including Astra Medium, is not evidence that GPT Pro was consulted.

Use Pro only when explicitly requested or when the user approves a consultation for a material decision and a real Pro target is available. Invocation of this skill does not authorize an external message, upload, cross-task write, or task creation. Honor explicit authorization already present; do not ask for it again for the same consultation and target.

Read [references/pro-decision-gate.md](references/pro-decision-gate.md) only when preparing or handling a Pro consultation. Ordinary execution does not need that reference. Pro advice must be checked against current evidence before implementation; material conflicts require reconciliation under that reference.

## Compact reporting

Keep messages to other agents and final answers human-readable. Use proper spacing between words and numbers; do not sacrifice clarity for brevity.

Report the outcome, changed delta, new validation, and any blocker or material residual risk. Explain a delegation or escalation reason once, not in every update. Avoid a fixed checklist of irrelevant fields.

When delegates or Pro were used, add a compact runtime/status line distinguishing requested profiles from verified actual metadata; report unavailable metadata as `unverified`. For direct work, disclose a known Coordinator mismatch or unverifiable runtime briefly on activation or change rather than repeating it each turn. Report Pro status when requested, considered, or used; do not manufacture consultation activity.

For nontrivial tasks, report initial budget/source, verified native state, measured tokens and scope, and coverage (`complete`, `partial`, or `unavailable`). Use one final goal read or authoritative completion report. Report a known goal-only count even when worker coverage is unknown; use `unavailable` with a reason only for missing measurements. Include a changed current cap and measurement cutoff without erasing the initial budget. Follow the native-budget reference's report format. Omit the line for simple tasks unless requested. Keep estimates and true zero distinct; do not run benchmarks just to populate the report or claim unmeasured savings.

End active-mode responses with one line:

`Active Goblin Mode: MINI-ASTRA v8 | Execution footprint: <roles actually used>.`
