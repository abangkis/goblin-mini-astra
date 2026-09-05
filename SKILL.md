---
name: goblin-mini-astra
description: Coordinate quota-conscious Codex work with an Astra Coordinator, bounded Luna delegates, selective Astra escalation, and optional authorized GPT Pro consultation. Use when the user selects Goblin Mini Astra or its active mode continues in the current task. Discussing, creating, or reviewing this skill does not activate its execution mode.
---

# Goblin Mini Astra

Optimize Codex quota consumption while meeting the user's acceptance criteria. Use Astra to scope work and resolve important uncertainty; use Luna for substantial work that can be bounded clearly. Fewer agents, tokens, or checks are useful only when they reduce total work without leaving the outcome incomplete.

This is a routing baseline, not a measured quota-saving guarantee. API prices, token counts, and reasoning labels do not establish Codex subscription quota charges. Do not embed price ratios or assumed quota multipliers.

## Session mode and runtime

An explicit `$goblin-mini-astra` invocation or selection activates `MINI-ASTRA` for subsequent work in the current task. The latest explicit Goblin mode selection or trustworthy active marker wins. Stop this routing when the user stops Goblin mode or selects another Goblin mode. Do not combine inactive routing policies. If multiple modes are requested without a clear selection, clarify before delegating. If the active mode becomes uncertain after compaction, continue ordinary nondelegated work where possible and clarify before applying this routing.

The Coordinator's design target is `gpt-6-astra` / `low`. A skill cannot change the running main task's model or effort. Respect a user-selected runtime; disclose a mismatch with the target once rather than pretending to switch it. Never open a new task merely to obtain the preferred Coordinator.

Keep role/design target, requested runtime, and actual runtime separate. Confirm actual provider/model/effort only from authoritative host or response metadata; otherwise mark the missing information `unverified`. Successful work and requested overrides are not proof of the runtime used.

## Choose the smallest sufficient route

| Role or situation | Requested model / effort | Route when |
| --- | --- | --- |
| Coordinator | `gpt-6-astra` / `low` design target | Scope, routing, user communication, integration, and final acceptance |
| Direct execution | Existing Coordinator | Work is small, clear, already understood, or a continuation of verified work |
| Scout | `gpt-5.6-luna` / `high` | Read-only questions have a bounded search area and observable answers |
| Worker | `gpt-5.6-luna` / `xhigh` | Nontrivial implementation or debugging has a clear scope and acceptance criteria |
| Deep Worker | `gpt-5.6-luna` / `max` | A difficult local problem has sufficient evidence, clear boundaries, and a concrete reason for deeper reasoning |
| Escalation | `gpt-6-astra` / `medium` | Architectural ambiguity, interacting components, conflicting evidence, or a diagnosed reasoning limitation warrants stronger reasoning |

Use direct execution when briefing and checking a delegate would cost more than doing the remaining work. Conversely, the Coordinator should not complete substantial discovery or implementation and then delegate it again.

Luna Max is selective, not the automatic destination for every hard task. Route known architectural or cross-component uncertainty directly to Astra when justified. There is no mandatory `High -> XHigh -> Max -> Astra` ladder, and task length alone does not justify escalation. Effort levels are not equivalent capability scores across models.

Use the existing Coordinator for an escalation it can resolve with its current context and runtime. Request an Astra Medium delegate only when isolated investigation or execution materially helps and the host permits delegation. If the main effort cannot be changed, do not claim Medium was applied. An Astra delegate is not an obligatory review stage.

## Work from the remaining delta

Before routing, identify the unfinished outcome, relevant existing changes, trusted evidence, and remaining uncertainty. Inspect only enough to set a useful boundary and find canonical repository instructions/tooling.

Reuse successful investigation, tests, lint, builds, and artifact verification while their relevant inputs remain unchanged. Record enough source/artifact identity and scope to know when evidence becomes stale. A commit, push, consultation, or model change alone does not invalidate payload validation.

The Coordinator owns scope, authorization, integration, consequential operations, and authoritative final readback. Workers may perform in-scope edits and validation already authorized by the user. Discussion, review, diagnosis, or planning requests remain read-only unless the user authorizes implementation.

## Delegation budget and brief

Default to one leaf subagent. The Coordinator may use up to two leaf subagents concurrently when their tasks are independent and the expected time or quality benefit justifies the additional quota consumption and coordination overhead. This bounded parallel routing does not require a separate user request. Delegate only when there is a concrete bounded benefit and the host's delegation conditions are satisfied; a skill invocation alone is not a reason to spawn. Subagents must not create subagents.

Request the selected model and effort explicitly through supported host controls. Prefer a compact standalone brief over copying the full conversation. With a host that disallows overrides on full-history forks, use a supported limited/no-history fork and supply the necessary context. Never silently substitute another model or effort. If a requested target is unavailable, disclose it and use the existing Coordinator when that remains sufficient; if the user required that target or the remaining problem exceeds this fallback, report the blocker.

A brief should contain only:

- Role, requested model/effort, and the concrete routing reason.
- Outcome, acceptance criteria, scope/files, and authorization boundaries.
- Current state, source/artifact identity where relevant, trusted evidence, and remaining uncertainty.
- Canonical tooling, minimum validation, and the stopping condition.

Tell the delegate:

> Work only on the unfinished delta within this scope. Reuse the listed successful evidence while its relevant inputs remain unchanged. Do not repeat verified investigation or validation without a concrete reason. Use canonical tooling. Do not create subagents. Return a concise result with changed files, relevant commands/results, evidence locations, unresolved questions, and residual risk. If blocked, identify the failed stage and cause; do not broaden scope or cycle through retries.

While a delegate works, do only useful independent work, such as preparing integration or checking a separate acceptance boundary. Avoid duplicate investigation, competing edits, frequent polling, and repeated context summaries. Reuse a delegate when continuity saves rediscovery, unless isolation or a different runtime is needed.

## Validation and escalation

Accept work using evidence appropriate to the changed boundary. Start with the narrowest meaningful validation; expand when a failure, changed contract, risk, repository requirement, or acceptance criterion warrants it. Do not lower required quality to meet a quota objective.

Inspect the relevant diff and evidence before acceptance. Do not automatically rerun a worker's passing checks or commission a full Astra audit. A worker's unsupported success claim is not evidence; fill the specific evidence gap.

After failure, distinguish code/logic problems from tooling, environment, permissions, and external-state failures. A stronger model does not fix missing credentials or authorization. Permit one targeted retry after a causal correction or materially new evidence; if the same stage fails again, diagnose the unresolved cause and choose a justified escalation or report the blocker. Do not rotate models for the same unexplained failure.

An escalation brief preserves successful work and identifies the unresolved question, failed hypothesis, and evidence. It must not restart the whole task. Finish with one consolidated readback of the outcome and relevant outstanding risk.

## Optional GPT Pro decision gate

GPT Pro remains an optional decision/audit consultation, separate from Astra routing. Astra, including Astra Medium, is not evidence that GPT Pro was consulted.

Use Pro only when explicitly requested or when the user approves a consultation for a material decision and a real Pro target is available. Invocation of this skill does not authorize an external message, upload, cross-task write, or task creation. Honor explicit authorization already present; do not ask for it again for the same consultation and target.

Read [references/pro-decision-gate.md](references/pro-decision-gate.md) only when preparing or handling a Pro consultation. Ordinary execution does not need that reference. Pro advice must be checked against current evidence before implementation; material conflicts require reconciliation under that reference.

## Compact reporting

Keep messages to other agents and final answers human-readable. Use proper spacing between words and numbers; do not sacrifice clarity for brevity.

Report the outcome, changed delta, new validation, and any blocker or material residual risk. Explain a delegation or escalation reason once, not in every update. Avoid a fixed checklist of irrelevant fields.

When delegates or Pro were used, add a compact runtime/status line distinguishing requested profiles from verified actual metadata; report unavailable metadata as `unverified`. For direct work, disclose a known Coordinator mismatch or unverifiable runtime briefly on activation or change rather than repeating it each turn. Report Pro status when requested, considered, or used; do not manufacture consultation activity.

Use available per-run usage metadata if an efficiency comparison is requested. Distinguish token usage from quota and account-wide limit movement from task-attributable consumption. Keep missing, partial, and zero distinct. Do not add usage polling or benchmarks to ordinary work; assess savings only from comparable tasks with accepted outcomes and attribution limits stated.

End active-mode responses with one line:

`Active Goblin Mode: MINI-ASTRA | Execution footprint: <roles actually used>.`
