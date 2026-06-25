---
name: goal
description: "Use when the user invokes /goal, asks for goal mode, designs an agent loop, or starts long-horizon autonomous work that should be clarified into a concrete, verifiable objective before execution."
argument-hint: "<goal draft or request>"
---

# Goal Mode (/goal)

`/goal` is for durable autonomous work: the goal text becomes the **exit criteria** the agent is
re-checked against after every turn, so it keeps working until the goal holds. So the rule is simple —
**the agent must know what "done" means, and how it will be proven, before it starts.** The preflight
below makes sure of that: a fuzzy goal gets a real **discovery conversation** first (so you shape it
together), then a tight structured confirmation; a genuinely crisp goal can fast-path straight to the
contract. Never start on "I'll know it when I see it."

## The bar: a runnable, self-evident done-check

A goal is ready when its done-condition is **observable, ideally numeric, and provable from what the
agent itself surfaces** — not asserted. The turn-by-turn completion check judges the agent's own
output and does **not** run your tools, so write the done-check as something the agent *demonstrates in
the transcript* (show the passing test / the metric / the diff), never "trust me, it passes." Pick the
strongest **available** check, in this order:

1. **Rules / commands** — `npm test` exits 0, build succeeds, lint clean, a benchmark number. (Best.)
2. **Visual** — a screenshot or visual diff, for UI. (Specs/checklists are the real criterion — never a raw image alone.)
3. **LLM judgement** — last resort; not robust, high latency.

Good goals carry a number: *"Reduce build+deploy time 30%."* · *"Migrate this feature TS→Rust at 100%
test parity."* · *"Get production LCP < 2.5s."* If you can't yet name a runnable check, that is the ONE
thing to resolve before starting — propose a check and confirm it; don't start on a feeling.

## Preflight: discovery → decide → start

A goal should be **bigger than one prompt but smaller than an open-ended backlog.** If the request is a
loose list of unrelated work, it's not a goal — ask to split it; do not interview.

1. **Classify intent.** Only answering a question about goal mode → answer normally. Starting
   autonomous work → continue.
2. **Read local context first.** Inspect the relevant files / failing tests / logs / docs / plan
   BEFORE asking anything — most fields are inferable straight from the repo.
3. **Discovery — a real, CONVERSATIONAL back-and-forth (do this BEFORE the structured questions).**
   Reflect back what you understand, then have an open exchange — **typically 3–6 short rounds** — to
   genuinely understand: the *why* behind it, what "great" looks like, the approach/options and their
   trade-offs, the constraints, and the landmines/risks. Go one thread at a time, build on each answer,
   and **listen more than you talk** — **plain open questions, NOT multiple-choice**. Don't rush to the
   structured gate; keep exploring until you could explain the goal back *better* than the user first
   did. Stop once it's genuinely well-understood (or sooner if the user signals they're ready). (Per
   OpenAI's own guidance: brainstorm the project first, *then* set the goal.)
4. **Draft the contract stub** — one line, and the forcing artifact: you literally cannot fill it
   without an exit criterion. Emit it from the discovery + context:
   > **Outcome:** _\<one concrete end state\>_ · **Done when:** _\<runnable check + expected result\>_ ·
   > **Guard:** _\<only the must-not-regress / destructive limits\>_ · **Inferred (correct me):**
   > start=_\<files/URLs\>_, between-tries=_\<iteration policy\>_, refresh=_\<signals\>_,
   > track=_\<commits + progress log\>_, on-blocked=_\<what to report + what would unlock\>_
5. **Lock the MANDATORY fields with STRUCTURED questions.** Now switch from open chat to decisions:
   just three things must be user-confirmed *if still unresolved* — **Outcome**, the **Done-check**,
   and any **destructive/irreversible constraint** (paid deps, migrations, force-push, prod deploy,
   real spend). Ask these as **at most 3 multiple-choice questions in ONE batch** (multiple-choice
   because these are decisions, not exploration). Everything else — scope, starting point, iteration
   policy, context-refresh, anti-cheat, tracking, finalization — **infer and put in the stub's
   "Inferred" line** for the user to redline; don't ask. Never run a second batch unless an answer
   revealed a contradiction; tempted to ask a 4th → infer it and state it instead.
6. **Start.** Emit the final stub and invoke goal mode (`create_goal` where the runtime has it); begin
   immediately. Don't ask "should I proceed" unless the next action is destructive or externally
   side-effectful.

> **Fast path:** if the request already makes the outcome AND a runnable check unambiguous (you could
> state the success check in one sentence), **skip discovery and the questions** — emit the stub and
> start. Discovery + rigor are for fuzzy goals, not clear ones.

The rhythm: **listen (discovery) → decide (structured questions) → start.** Discovery is open, human,
and can take several rounds (≈3–6); the structured batch is tight (≤3, one shot). Spend the time
*understanding*, not interrogating.

## Design the loop, not just the first prompt

A durable run needs four live parts — **goal, context, evaluation, action** (gather context → act →
verify → repeat). Name them in the stub:

- **Iteration policy (between tries):** how to choose the next move — default *"re-run the done-check,
  attack the largest remaining gap."* This is what prevents rabbit-holing.
- **Context refresh:** start with the *smallest useful* context, then deliberately fetch more (CI,
  logs, failure traces, analytics, review feedback) as the loop advances — don't dump it all up front.
- **Guidance:** point at where to start and what tools it may use. For ambitious goals, research/plan
  first → write a plan file → have the goal reference it.
- **Verify with the strongest signal, and don't self-grade:** prefer rules over a model's opinion; for
  big runs, use a fresh-context verification subagent so the agent doing the work isn't the one judging
  it.
- **Budget ≠ done:** hitting a turn/time/token budget is NOT completion — stop substantive work,
  summarize progress + blockers, and name the next useful step. Add an explicit *"or stop after N
  turns"* clause when you want a hard ceiling.

## Make progress measurable

If the goal is ambitious or has many paths, the loop must be able to *know it's getting closer*.
Sometimes that's free (build time, test count); otherwise build or request the tool — an eval suite, or
a visual-diff tool (which can evolve diff modes over the run). Guard against fake wins the headline
check would miss — deleting/weakening tests, cropping a screenshot, inlining the design image to look
"pixel perfect." Derive the anti-cheat clause mechanically from the done-check. For visual goals
especially: use images as *context*, but define "done" via feature checklists / specs / design-system
adherence — never make the raw image the sole exit criterion.

## Create a realistic environment

Real progress needs the real stack: same flags, a similar database, deploy/test targets that mimic
production. Watch for environments that diverge from prod (e.g. preview builds with paths disabled) —
do manual prod-like deploys instead. Computer-use or a physical device gives the most accurate signal
for performance/UI goals.

## Track long runs

When a goal runs for hours or days (possibly on another machine), keep progress visible: commit at
meaningful steps + push to a **draft PR** (great with preview deploys); keep a **progress artifact**
(HTML dashboard / rendered graph / markdown); post milestones to **Slack** if asked; and use a short
side-thread or a scheduled check-in to ask "where are we?" without disturbing the run.

## Finalization

Reaching the target isn't the end — the run may have left dead ends and failed experiments behind.
Before reporting done: run a review; reflect on the attempts and remove leftover/abandoned changes
(matters most for optimization tasks). When reviewing, flag only gaps that affect **correctness or the
stated criteria** — a reviewer told to "find gaps" always finds some, and chasing every one causes
over-engineering. Mark complete ONLY when the done-check's evidence exists in the transcript; mark
blocked only after the same blocker has held for ~3 turns with no alternative.

## Full contract — expand ONLY for multi-day / multi-agent runs

The one-line stub is enough to start most goals. For long, multi-agent, or hand-off runs, expand it:

```text
Goal: <single concrete outcome>
Done when: <observable, runnable proof(s) — judgeable from the agent's own output>
Scope: include <areas> · exclude <non-goals>
Iteration policy: <how to pick the next move after each attempt>
Context refresh: re-check <signals> every <cadence / milestone>
Constraints: <allowed deps / side-effects / budget; what must not regress>
Anti-cheat: <ways NOT to satisfy it>
Start at: <files / docs / tests / URLs> · Track via: <commits / PR / artifact>
On blocked: <what to report + what would unlock progress>
Final check: <commands / manual verification>; clean up dead ends before reporting done
```

Keep the live goal prompt short enough to remember across a long run, specific enough that another
agent could decide whether it's complete.

<!-- Modeled on Dominik Kundel's (OpenAI) /goal guidance + OpenAI's "Using Goals in Codex" cookbook and
Anthropic's Claude Code /goal docs, "Building Effective Agents," and best-practices. The balance:
always produce a verifiable, self-evident exit condition before starting — but infer everything
inferable and cap clarifying questions at 3-in-one-batch so a clear goal starts with zero. -->
