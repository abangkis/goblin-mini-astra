# How Goblin Mini Astra budgeting works

This guide explains the budget in simple terms. It describes both the Goblin Mini Astra policy and the native Codex Goal system it uses.

## The short version

A numeric budget is a ceiling for one task. It is not a spending target.

The budget is not an account quota, an API bill, or a price limit. It does not promise a particular amount of finished work.

Goblin Mini Astra uses the native Codex Goal system to store the task objective, `tokenBudget`, and measured `tokensUsed`. The Goblin helper stores the user's preferred default, but it does not count tokens or enforce the limit by itself.

## Starting a task

On first use, Goblin Mini Astra asks the user to choose a default budget. The available suggestions are 1 million, 5 million, or 10 million tokens. A custom positive amount is also allowed.

The default is stored locally for future tasks. It is not synchronized between devices.

A user can override the default for one task. The override does not change the saved default.

When the effective budget is numeric, Goblin Mini Astra asks the native Codex Goal system to create or reuse a matching goal with that total token budget. It verifies the result before claiming that native budgeting is configured.

If the user selects `no budget`, Goblin Mini Astra does not create a new native token budget. Quota-conscious routing and normal validation rules still apply.

## While the task is running

The budget belongs to the whole task. It is shared by the Coordinator and any delegates.

Two workers do not each receive the full task budget. They consume from the same overall allowance when the host's accounting covers them.

Goblin Mini Astra does not check the counter after every sentence or tool call. It reads the native goal at decision points where the result could change what happens next. Examples include starting another delegate, escalating reasoning, or beginning a large new phase.

The Coordinator tries to leave enough room for integration, validation, and the final report. It does not spend the entire remaining amount on execution and leave no room to verify the result.

## When the budget is getting close

The Coordinator compares the measured remaining budget with the next substantial step.

If the next step and the necessary validation can fit, work may continue.

If they cannot fit, the Coordinator does not start that step. It prepares a checkpoint that records:

- What is complete.
- What has been verified.
- What remains unfinished.
- What decision is needed from the user.

The Coordinator then asks the user to reduce the scope, increase the total budget, or stop with the current partial result.

Goblin Mini Astra does not weaken required validation merely to stay under budget.

## When the budget is reached

Goblin Mini Astra stops launching further work.

It does not automatically increase the budget. It does not reset the counter. It does not mark incomplete work as complete.

Completed files and evidence remain in the workspace. Reaching the budget does not roll back earlier work.

The task waits for a user decision. The user can:

- Increase the total budget.
- Reduce the remaining scope.
- Accept the current partial result.
- Stop or clear the goal.

If the budget is increased, work continues from the existing checkpoint. It should not repeat successful investigation or validation without a concrete reason.

## Increasing a budget does not reset usage

Suppose the original budget is 1,000,000 tokens and 900,000 tokens have been used.

If the user increases the budget to 2,000,000 tokens, the new total ceiling is 2,000,000. The remaining amount is about 1,100,000 tokens, subject to the native counter's coverage and timing.

The increase is not an additional 2,000,000 tokens.

Updating the budget for the same unfinished goal preserves its usage history. Goblin Mini Astra must not replace the objective or clear the goal merely to reset the counter.

## The native stop may not land on the exact token

Native goal state provides a budget and a usage counter. Current OpenAI documentation does not promise interruption at the exact individual-token boundary.

An already-running response or tool operation may finish before the latest usage is recorded. The final measured count can therefore reach or slightly exceed the configured amount.

For this reason, Goblin Mini Astra tries to stop proactively. It avoids starting work that does not appear to fit inside the remaining allowance.

The exact hard-stop timing and delegate coverage depend on the current Codex host. Missing coverage is reported as unknown or partial, never as zero.

## Budget and account quota are different

The task budget measures one goal. Account quota applies more broadly to the user's Codex account.

A task can have budget remaining while the account quota is low. Account quota movement is not treated as exact usage attributable to this task.

Goblin Mini Astra never converts task tokens into a claimed subscription-quota percentage unless authoritative product metadata provides that relationship.

## Native Goal controls

Codex Goal mode lets the user pause, resume, edit, or clear a goal. These controls do not grant new filesystem, network, or approval permissions.

Changing the budget of the same unfinished goal preserves its usage history. Supplying a genuinely new objective replaces the goal and resets its usage accounting. Goblin Mini Astra does not use objective replacement as a budget workaround.

## Official OpenAI references

- [Codex App Server: manage a thread goal](https://learn.chatgpt.com/docs/app-server#manage-a-thread-goal)
- [Long-running work with Codex goals](https://learn.chatgpt.com/docs/long-running-work)
