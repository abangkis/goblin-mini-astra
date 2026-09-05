# Optional GPT Pro decision and audit gate

Read this reference only for a requested or proposed Pro consultation. Keep the handoff proportional to the decision; do not generate large reports for routine work.

## Authority and availability

GPT Pro advises; Codex retains responsibility for repository changes, execution, and verification. A Pro response grants no new authority. Neither the skill name nor an Astra runtime proves Pro use.

Before sending anything, establish a real callable/selectable Pro target and the user's explicit authorization for the consultation, target, and material being transferred. Reuse valid authorization already given. Do not create a task, send a cross-task/external message, or upload source merely because a Pro gate would be helpful. Prefer an authorized existing target or a manual brief. Exclude credentials, secrets, unrelated source, and unnecessary personal data.

If Pro is optional and unavailable or not authorized, continue normal routing with transparent status. If the user requires Pro and no target is available, prepare a manual handoff and pause the dependent execution; do not substitute Astra or Luna. Independent authorized work may continue when it cannot pre-empt the required decision.

## Minimal handoff records

Prepare a compact **Decision Brief** with:

- Objective, non-goals, constraints, and acceptance criteria.
- Current state and source/artifact identity.
- Relevant verified evidence, remaining uncertainty, and credible alternatives.
- The precise decision or audit question, including assumptions to challenge.
- Authorized target/transport and material scope; requested versus verified actual runtime.

Do not ask Pro to repeat discovery already supported by evidence. Keep records in the conversation unless a durable artifact is needed or requested.

On receipt, extract a **Pro Decision Record**: recommendation, assumptions, acceptance implications, risks, unresolved questions, source/target, and runtime provenance. Treat a user-supplied answer as proposed advice with its provenance stated, not independently verified Pro output.

Validate the recommendation against the current repository/schema, user constraints, and evidence. Record `aligned`, `validation-conflict`, or `partial` with the reason. Advice alone is not implementation or test evidence.

## Gate states and reconciliation

| State | Action |
| --- | --- |
| `not-needed` / `not-requested` | Continue normal routing; no consultation is implied |
| `awaiting-authorization` | Prepare the brief; do not transmit it |
| `ready` | Available Pro target and explicit authorization established |
| `consulted` | Response received; validate before dependent execution |
| `unavailable` / `manual-handoff` | Continue if optional; pause dependent execution if required |
| `validation-conflict` | Record the conflicting claim, authoritative evidence, and impact |
| `aligned` / `audited` | Route remaining work using validated evidence |

For a material conflict, set `GPT Pro consultation: validation-conflict` and `Execution status: needs-reconciliation`. Do not select or run an execution route for the disputed decision, including implementing it merely to test the advice. Resolve through a revised Pro decision that aligns with authoritative evidence or an explicitly user-approved documented resolution. A generic instruction to continue does not approve an unspecified resolution. Do not stall unrelated authorized work that cannot pre-empt reconciliation.

After resolution, retain a compact **Evidence Capsule**: artifact/source identity, implemented delta, validation and its scope, decision record, conflict/resolution if any, and residual risk. Reuse existing evidence; only a relevant changed input justifies revalidation.

Post-execution Pro audits use the same authorization and provenance rules and are advisory. Do not automatically request another audit or perform a complete re-review merely because Pro was consulted.
