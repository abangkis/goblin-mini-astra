# Model profiles

Use this table for Coordinator selection and all worker assignments. Choose the action in [SKILL.md](../SKILL.md), then match the remaining work to an eligible profile. A requested model and effort describe the intended runtime. Verify them against host metadata when available.

| Work | Model / effort | When to choose it |
| --- | --- | --- |
| Coordinate | `gpt-6.2-sol` / `high` by default | Own scope, communication, routing, integration, and acceptance. Execute directly when existing context is sufficient and the Coordinator is eligible for the work. |
| Coordinate by explicit selection | `gpt-6.2-sol` / `medium` or `gpt-6.1-terra` / `xhigh` | Same responsibilities. A Terra Coordinator delegates the FE portion to Sol or Astra. |
| Objective non-FE work | `gpt-6-luna` / `high`, `xhigh`, or `max` | High for bounded read-only scouting, XHigh for routine implementation or debugging, Max for a difficult local problem with objective checks. |
| Bounded delivery | `gpt-6.2-sol` / `medium` | A separable change needs limited cross-component judgment, or a UI change follows established design decisions and known states. |
| Design or investigation | `gpt-6.2-sol` / `high` or `xhigh` | High for open design decisions, complex implementation, or an independent investigation. Choose XHigh for specific competing hypotheses, interactions, or edge cases. |
| Bounded capability gap | `gpt-6.2-astra` / `low` | Answer one unresolved technical question or correct one observed visual or interaction defect. |
| Escalation | `gpt-6.2-astra` / `medium` or selectively `high` | Medium for interacting uncertainties, consequential architecture, original visual direction, or experience-wide tradeoffs. Use High only when the conditions below hold. |

Use only Sol or Astra for **all FE execution**, including scouting and UI testing. Apply [frontend routing](frontend-routing.md) for FE ownership and acceptance. A Sol Coordinator can handle bounded work at its current effort. A same-profile handoff needs a concrete benefit. Sol Low and Sol Max require an explicit user request and host support.

## Selecting Astra effort

Apply the capability escalation criteria in [SKILL.md](../SKILL.md) to every Astra assignment. Select the effort directly from the evidence.

Choose High when the wrong decision would cause material harm or rework, credible explanations or constraints conflict, and an available check can distinguish the options. Before assigning it, state which decision Medium is unlikely to settle and why, what evidence the worker can inspect, and what result ends the assignment. Keep room in the shared task budget for integration and validation.

For example, a migration rehearsal may pass on each schema separately while a rollback trace shows both old and new writers active. High can resolve which write order preserves acknowledged updates by checking the competing orders against that trace. Medium can handle a cross-service migration when the contracts and acceptance test already settle that question. Missing traces call for evidence collection. Task size, a request for a premium look, or a failed tool call alone gives no reason to select High.

High is an effort choice within the escalation assignment. A prior Medium attempt is optional. Use bounded judgment for a decision alone. When authorized, one worker can own diagnosis, the closely coupled fix, and its targeted test. Stop when the agreed check settles the decision or the necessary evidence is unavailable.

[GPT Pro consultation](pro-decision-gate.md) requires separate authorization and an available Pro target. Model labels alone establish neither runtime nor measured quota savings.
