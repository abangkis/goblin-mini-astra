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

Coordinator High does not require every worker to use High or higher. Use the action criteria in SKILL.md first: a worker needs a concrete benefit, even if it uses the same model/effort. Keep already-understood, closely coupled investigation with the Coordinator. Sol Medium is selective, not a blanket replacement for Luna.

Apply the escalation gate in SKILL.md before either Astra profile; no failed Sol attempt is required. Effort labels are not equivalent capability scores across models. These are routing hypotheses, not measured quality, latency, or quota guarantees.

GPT Pro remains a separate, explicitly authorized consultation through a real available target; it is not an execution worker or an alias for Astra. Load the [Pro procedure](pro-decision-gate.md) only when considering or preparing that consultation.
