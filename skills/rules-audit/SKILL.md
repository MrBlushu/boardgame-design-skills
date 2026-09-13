---
name: rules-audit
description: Audit tabletop-game rules for contradictions, ambiguity, missing rules, terminology drift, and timing problems. Use when reviewing a rulebook or preparing it for blind playtesting; do not use to judge fun, balance, or player experience without playtest evidence.
---

# Rules Audit

Produce a traceable diagnosis of the supplied rules without silently completing the design.

## Source discipline

1. Identify the files the user treats as authoritative. If authority is unclear, report the conflict instead of choosing silently.
2. Treat only explicit source text as a current rule.
3. Label conclusions as `CURRENT RULE`, `INFERENCE`, `UNCERTAINTY`, or `PROBLEM`.
4. Never turn an inference, common convention, or proposed fix into a rule.
5. Do not edit source files unless the user separately asks for an approved rewrite.
6. For visual rules, inspect every relevant page, panel, diagram, caption, and worked example. Reconcile them with the prose, and treat extraction or encoding artifacts as tooling limitations rather than rulebook defects.

## Audit

Read the complete authoritative rules before reporting findings. Check only issues supported by the material:

- contradiction: two instructions cannot both be followed;
- ambiguity: multiple readings remain plausible;
- missing rule: a reachable state has no defined resolution;
- terminology: one concept has inconsistent names or one name has conflicting meanings;
- timing: order, priority, duration, or simultaneous effects are unresolved;
- editorial: wording obstructs comprehension without changing the design.

Before recording a finding:

- confirm that the gap or competing readings are supported by the source, not merely imaginable;
- check whether another section, diagram, caption, component label, or worked example resolves it;
- for every `BLOCKER` or `MAJOR`, give a concrete legal witness state or reproducible sequence; if reachability cannot be established, omit it or record it as a scope limitation;
- ignore harmless social conventions and hypothetical pathologies with no demonstrated gameplay consequence unless the user requests an exhaustive audit;
- merge findings that share one root cause.

Before finalizing, run one lifecycle coverage pass:

- trace setup, a normal turn, success, failure, timeout, cleanup, and the next round when those states exist;
- for each component, deck, pile, and resource, check initialization, ownership, visibility, legal transitions, cleanup, and exhaustion;
- verify that every reachable turn has at least one legal action or an explicit stop rule;
- order resolution checks, triggered effects, recovery, discards, and state changes when their results can interact;
- distinguish an action being illegal from it being legal but causing a failed objective.

For each finding, record:

- stable ID (`RA-001`, `RA-002`, ...);
- category and severity (`BLOCKER`, `MAJOR`, or `MINOR`);
- exact source section and a short quotation or faithful paraphrase;
- observed issue, kept separate from its possible consequence;
- plausible interpretations when relevant;
- concrete legal witness state or sequence for `BLOCKER` and `MAJOR` findings;
- concrete gameplay consequence;
- whether a designer decision is required.

Use `BLOCKER` only when play cannot continue or different readings produce materially incompatible states. Use `MAJOR` when the issue can change legal actions, outcomes, or repeated play. Use `MINOR` for localized comprehension or editorial problems.

## Output

Begin with:

- sources audited and their authority;
- scope limitations;
- readiness: `READY`, `READY WITH CLARIFICATIONS`, or `NOT READY FOR BLIND PLAYTEST`.

Then provide the findings in priority order, followed by:

- unresolved designer decisions;
- editorial-only corrections, if any;
- a short coverage summary.

Use the full finding record for `BLOCKER` and `MAJOR` issues. Group `MINOR` and editorial issues compactly. Do not narrate checks that passed unless they materially bound the scope or readiness conclusion.

Do not report an issue merely because the design is unusual. Do not claim the game is balanced, fun, fair, or clear from a rules audit.
