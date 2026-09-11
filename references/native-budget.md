# Native budget integration (v5)

Use native tools exposed by the current host, not shell access to internal databases or an invented API. The preference helper cannot install a native budget, count tokens, or establish enforcement. Keep configuration, measurement, and stopping guarantees separate.

## Establish native state before substantial execution

1. Resolve the preference/task override and retain its source and original task baseline.
2. Call `get_goal` (or the host's documented equivalent) once, unless fresh authoritative goal metadata is already available. Confirm the objective, status, configured token budget, measured usage, and remaining budget where exposed. Missing values are unknown, never zero.
3. Reuse a matching active goal. If its objective, scope, or budget differs, report the mismatch before further substantial work. Never replace an unfinished goal or reset its counter to match a default. A mid-task increase changes the total ceiling, not a fresh allowance.
4. The user's bundled-budget instruction requests native goal setup whenever this workflow runs with a saved numeric default or an explicit numeric task budget. Do not ask a separate confirmation to create that native goal. If no goal exists, or the previous goal is complete, use `create_goal` with the current authorized task objective and resolved token budget. Reuse the user's standing instruction; do not treat each new task as requiring renewed budget consent. Do not replace an unfinished/inactive goal merely to restart its counter: use supported continuation controls or report the concrete conflict. A workflow without a numeric budget does not request goal creation, and ordinary tasks outside this selected workflow do not inherit this request.
5. After authorized creation, read back with `get_goal` unless the creation result already authoritatively verifies the objective and budget. Only then report `native configured`. A requested value without successful readback is `unverified`, not configured.

For goal changes, budget removal, pause, or resume, use only supported host controls and explicit user authorization. The current `update_goal` tool controls completion/blockage, not budgets or pausing. Never use false completion/blockage to simulate a budget stop, clear an active goal, or bypass a cap. Do not manipulate app state files as a fallback.

With `no budget`, do not create a native goal or set a native token budget, including merely to obtain accounting. The override requests removal of the task cap if one is already active; use supported controls without a redundant permission question while preserving the objective and usage history. If removal is unsupported, report that the existing cap remains and the exact user action needed. Never claim the helper removed a native cap or clear the goal/counter as a workaround.

If native tools are absent, fail, or cannot configure the requested state, disclose `preference only; native enforcement inactive/unverified` and the specific reason. Ask whether to proceed under that limitation or wait for native setup; this is a real capability decision, not renewed permission for already-requested native setup. Retain progress and evidence. A numeric budget requests setup even for a simple task; simple tasks may still omit ongoing bookkeeping and the final budget line.

## Measure only when it changes a decision

Read `get_goal` before additional costly delegation, escalation, extended investigation, or a major phase when the last snapshot is no longer sufficient. Reuse returned usage/remaining-budget metadata instead of fetching again. Do not poll each tool call or introduce a monitoring worker. Account-quota reads are separate and cannot substitute for task-token counters.

Retain goal identity/objective, measurement cutoff, counter scope, and baseline. If attaching a goal after work has started, its counter excludes earlier work unless documented otherwise: report post-activation usage with partial task coverage. Preserve cumulative usage across turns; do not subtract the same baseline repeatedly. A counter decrease or goal replacement invalidates continuity until reconciled.

Native `tokensUsed`/`remainingTokens` values are useful measurements, but do not assume parent counters include all workers. Use verified host semantics/metadata before claiming aggregate coverage or adding child totals. Do not count a worker twice. Report an available parent/goal measurement even if worker coverage is unknown, e.g. `actual: 820,000 goal tokens; worker coverage unknown`. Do not replace a known scoped measurement with a blanket `unavailable`.

Before delegation, state the shared task budget, latest remaining amount if known, and stopping condition in the brief. Two workers share the same remaining budget; neither gets the full allowance independently. Prefer one worker if uncertain aggregate usage makes parallel spending unsafe. Per-worker allocations are behavioral unless the host exposes verified enforcement for them.

Reserve room for integration, validation, and reporting. When measured remaining budget cannot cover the next substantial step plus that reserve, do not launch it. Prepare a checkpoint and request a scope/budget decision; at an exhausted budget, stop further execution as permitted by host controls. Do not raise the cap or mark the goal complete unless the work is actually complete. Native configuration alone does not prove exact hard-stop timing or coverage of in-flight worker calls.

## Final readback and report

Use one final native usage read, or the authoritative completion budget report when legitimately completing a goal, without a duplicate fetch. Report any final-response/in-flight usage excluded by that snapshot.

For nontrivial work include:

`Budget: <initial amount/source; current cap if changed> | Native: <configured / preference only / unverified / no budget> | Actual: <measured tokens and scope, or unavailable with reason> | Coverage: <complete / partial / unavailable, with cutoff>.`

`Complete` requires confirmed task and delegate coverage. No usable measurement means `unavailable`, not a vague `partial`. Unknown runtime provenance remains separate from token accounting. Do not claim exact quota savings or hard-cap guarantees based solely on a configured goal.

Reference: [Codex App Server goal state](https://learn.chatgpt.com/docs/app-server#manage-a-thread-goal) exposes `tokenBudget` and `tokensUsed`. Tool capabilities and authoritative runtime metadata remain the authority for the current host.
