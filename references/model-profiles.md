# Model profiles

This is the authoritative model/effort mapping for Goblin Mini Astra. Load it on activation or profile selection, and reuse it for delegation while unchanged. A profile is a requested runtime, not evidence of what the host actually ran. Worker controls and available models must be verified in the current host; never silently substitute.

| Role | Model / effort | Selection reason |
| --- | --- | --- |
| Default Coordinator | `gpt-6.1-sol` / `high` | Scope, communication, direct investigation, routing, integration, and final acceptance |
| Alternative Coordinator | `gpt-6.1-sol` / `medium`; `gpt-6.1-terra` / `xhigh` | Explicit user choice; same responsibilities and safeguards |
| Scout | `gpt-6-luna` / `high` | Bounded read-only search with observable answers |
| Routine Worker | `gpt-6-luna` / `xhigh` | Clear implementation/debugging with explicit acceptance criteria |
| Deep Worker | `gpt-6-luna` / `max`; selectively `gpt-6.1-sol` / `medium` | Luna for difficult local problems with objective checks; Sol Medium for bounded cross-component judgment with clear questions and validation |
| Investigative Worker | `gpt-6.1-sol` / `high` or `xhigh` | High for a separable investigation or specific independent assessment; XHigh for unresolved hypotheses, interactions, or edge cases requiring deeper analysis |
| Capability-gap investigation | `gpt-6-astra` / `low` | A bounded question the Coordinator or available workers cannot resolve efficiently; own the closely coupled fix and validation when authorized |
| Escalation Worker | `gpt-6-astra` / `medium` | Interacting uncertainty, conflicting evidence, consequential architecture, or experience-wide visual tradeoffs |

Sol Low and Sol Max are excluded from standard routing. Use them only on explicit user request, subject to host availability; do not select them as automatic fallbacks. Luna Max and Astra Low remain standard options.

## Frontend domain override

Frontend work uses only Sol and Astra. These profiles override general worker rows for FE investigation, design, implementation, debugging, and visual/interaction validation. Load [frontend routing](frontend-routing.md) for ownership and selection criteria. General Luna roles apply only to non-FE work.

| Frontend profile | Model / effort | Selection reason |
| --- | --- | --- |
| Frontend bounded | `gpt-6.1-sol` / `medium` | Defined design system, bounded FE investigation, mechanical edits, responsive fixes, or known states |
| Frontend design and implementation | `gpt-6.1-sol` / `high`; selectively `xhigh` | Open design/UX decisions or complex implementation; XHigh for concrete unresolved interactions or hypotheses |
| Frontend visual correction | `gpt-6-astra` / `low` | Specific unresolved visual or interaction gap with rendered evidence |
| Frontend original direction | `gpt-6-astra` / `medium` | Original direction, taste-led deliverables, or experience-wide visual tradeoffs |

An existing Sol Coordinator can execute directly at its current effort; the bounded profile does not require downgrading a Sol High thread or spawning a worker. Alternative Coordinator selection does not waive the frontend family restriction.

Coordinator High does not require every worker to use High or higher. Use the action criteria in SKILL.md first: a worker needs a concrete benefit, even if it uses the same model/effort. Keep already-understood, closely coupled investigation with the Coordinator. Sol Medium is selective, not a blanket replacement for Luna.

Apply the escalation gate in SKILL.md before either Astra profile; no failed Sol attempt is required. Effort labels are not equivalent capability scores across models. These are routing hypotheses, not measured quality, latency, or quota guarantees.

GPT Pro remains a separate, explicitly authorized consultation through a real available target; it is not an execution worker or an alias for Astra. Load the [Pro procedure](pro-decision-gate.md) only when considering or preparing that consultation.
