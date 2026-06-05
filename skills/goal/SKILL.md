---
name: goal
description: "Use when the user invokes /goal, asks for Codex goal mode, or starts long-horizon autonomous work that should be clarified into a concrete verifiable objective before execution."
argument-hint: "<goal draft or request>"
---

# Codex Goal Mode (/goal)

`/goal` is for durable autonomous work. The goal text is the exit criteria, so do not create
or continue a goal from a rough request until the request has passed the preflight below.

## Anti-Pattern: "I basically know the goal, I'll just start"

This is the failure that wastes the most time. A goal that *sounds* clear in your head
("make it faster", "match this design") is almost never a verifiable exit criterion. If you
skip the preflight, the run goes for hours and either stops early on a fuzzy match or
rabbit-holes on the wrong thing. Every goal passes the preflight — the synthesis can be short,
but it must produce a checkable done-condition.

## Mandatory Preflight

Run this before calling `create_goal`, updating an active goal, or treating a `/goal` message as
the working objective.

1. **Classify intent.** If the user is only asking about goal mode, answer normally. If they are
   invoking `/goal` or asking you to start autonomous work, continue.
2. **Capture the draft.** Restate the likely outcome in one sentence.
3. **Inspect local context first.** When files, repos, docs, tests, URLs, or prior plans are
   relevant and safely inspectable, read them before asking questions.
4. **Run the ambiguity gate.** A goal is not ready until these fields are known or safely inferred:
   outcome, done evidence, scope boundaries, starting point, constraints, anti-cheat criteria,
   progress tracking, and final verification.
5. **Ask clarifying questions.** Ask only questions that change the goal contract. Prefer one
   high-leverage question at a time when answers branch; ask up to three concise questions when
   they are independent. Multiple choice is preferred when it reduces ambiguity.
6. **Synthesize the goal contract.** Write a concise objective with explicit exit criteria and
   verification. Include constraints and exclusions when they prevent drift.
7. **Start execution.** Once the ambiguity gate passes, invoke goal mode by calling `create_goal`
   with the synthesized objective when the tool is available, then begin work immediately. Do not
   ask "should I proceed" unless the next action is destructive, externally side-effectful, or the
   remaining ambiguity materially changes the work.

## Ambiguity Gate

Ask before starting if any required field is missing:

| Field | Question to answer |
| --- | --- |
| Outcome | What concrete artifact, behavior, metric, or state must exist? |
| Done evidence | What command, metric, screenshot, deploy, file, or manual check proves completion? |
| Scope | What is included, and what is explicitly out of bounds? |
| Starting point | Which repo, files, URLs, failing checks, plan, or environment should be inspected first? |
| Constraints | Are new dependencies, network calls, commits, PRs, migrations, destructive actions, or paid services allowed? |
| Anti-cheat | What would be a fake win, such as deleting tests, hiding failures, cropping a screenshot, or weakening requirements? |
| Progress | Should progress be tracked in a status file, commits, PR, dashboard, or concise chat updates? |
| Finalization | What cleanup, review, tests, and handoff are expected after the target is met? |

Stop interviewing as soon as the missing fields are answered or safely inferable. Goal mode should
clarify enough to execute, not become an endless planning conversation.

## Prefer Verifiable, Numeric Exit Criteria

A good done-condition is observable and, where possible, numeric. Examples:

- "Reduce build and deployment time by 30%."
- "Migrate this feature from TypeScript to Rust and reach 100% test parity."
- "Get production largest-contentful-paint below 2.5s."

A number is not mandatory, but it makes every other field sharper. If you cannot frame a
verifiable criterion yet, keep interviewing — do not start the goal on a feeling of "done".

## Make Progress Measurable

If the goal is ambitious or has many possible paths, ensure there is a way to *know it is
getting closer*. Sometimes this is free (build times, test counts). Otherwise build or request
measurement tooling — an eval suite, or a visual-diff tool comparing two screenshots (such a
tool can evolve over the run to add diff modes). Without a measurement method, the goal cannot
self-verify and is not ready to start.

## Create a Realistic Environment

Real progress needs same stack, same flags, similar database, and real deploy/test targets that
mimic production. Watch for environments that diverge from prod — e.g. deploy previews with build
paths disabled versus full production runs; in that case do manual deploys to a prod-like config
instead. Computer-use or even a physical device (e.g. iOS profiling traces) can give the most
accurate signal when the goal is performance- or UI-sensitive.

## Special Case: Visual Goals

"Implement this UI 100% pixel perfect from this image" is tempting but risky — the run may
rabbit-hole on generating SVG icons/images and burn tokens on repeated image comparison.
Instead use images as **context**, and define done via **feature checklists, specs, and
design-system adherence**. Never make the raw image the sole exit criterion.

## Goal Contract Template

Use this shape when creating the objective:

```text
Goal: <single concrete outcome>

Done when:
- <observable proof 1>
- <observable proof 2>

Scope:
- Include: <areas>
- Exclude: <non-goals>

Constraints:
- <allowed tools/dependencies/side effects/budget>

Anti-cheat:
- <ways not to satisfy the goal>

Execution notes:
- Start at <files/docs/tests/URLs>
- Track progress via <artifact or update cadence>

Final verification:
- Run <commands/checks/manual verification>
- Clean up dead ends before reporting completion
```

Keep the final goal prompt short enough to be remembered across a long run, but specific enough
that another agent could decide whether the goal is complete.

## Running the Goal

- Do not ask the user to type `/goal` again after the interview. In Codex agent context,
  `create_goal` is the programmatic `/goal` invocation.
- If no active goal exists and `create_goal` is available, call it with the synthesized objective.
  The objective must include the relevant contract details from the interview: done evidence,
  scope, constraints, anti-cheat criteria, starting point, progress tracking, and final
  verification. Do not pass only the headline goal.
- If the Codex client already created an active goal from the rough `/goal` text, pause
  implementation, finish this preflight, and use the synthesized contract as the current working
  contract unless the user explicitly wants to replace or stop the old goal.
- If `create_goal` is unavailable, provide the synthesized objective as the exact `/goal` payload
  and continue only when the client exposes an active goal or the user explicitly asks for normal
  non-goal execution.
- If the user gives a token budget, pass it to the goal tool. Otherwise do not invent one.
- After major work chunks, check goal status and continue until the contract is met.
- Mark a goal complete only after the final verification evidence exists.
- Mark blocked only when the same blocker has repeated for at least three consecutive goal turns
  and no meaningful alternative remains.

## Tracking Long Runs

When a goal runs for hours or days (possibly on another machine), keep progress visible:

- **Commit at meaningful steps and push to a draft PR** — especially useful with preview
  deployments.
- **Maintain a progress artifact** — an HTML dashboard kept open, a rendered graph image, or a
  plain markdown status file.
- **Post updates** to Slack or wherever progress is tracked, if the user asked for it.
- **Use side chats for status checks** — `/side` forks the current thread (full context, short
  lived) to ask "where are we?" without disturbing the run; a recurring check-in can be scheduled.

## Finalization

Reaching the target is not the end. Because the run continues until the bar is met, it may leave
dead ends and failed experiments behind. Before reporting completion:

- Run `/review` for a local code review.
- Reflect on the attempts made during the run and remove leftover or abandoned changes.
- This matters most for optimization tasks, where many approaches get tried.

## Question Examples

- "Which result should count as done: passing the full CI suite, fixing one failing job, or merging a PR?"
- "Is adding a new dependency allowed, or should the solution stay within the current stack?"
- "What would be an unacceptable shortcut here, even if the headline metric improves?"
- "Where should I start: the failing test output, the last PR, or a specific file?"
