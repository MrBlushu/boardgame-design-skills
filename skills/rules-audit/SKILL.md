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
- find and state the strongest source-supported resolution before assigning severity, including specific procedures, component text, diagrams, and examples; if it fully determines play, omit the finding or classify only the obstructive wording as editorial;
- when the candidate concerns a shared concept such as targeting, immunity, discarding, or elimination, inspect every rule, component, and exception that uses that concept before scoping or merging the finding;
- for every `BLOCKER` or `MAJOR`, give a concrete legal witness state or reproducible sequence that reaches the disputed decision using only rules shared by all interpretations; never assume the contested action or state is already legal;
- if reachability cannot be established without that circular assumption, omit the candidate or record it as a scope limitation;
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
- strongest source-supported resolution considered and why it does not settle the finding;
- plausible interpretations when relevant;
- concrete legal witness state or sequence for `BLOCKER` and `MAJOR` findings;
- concrete gameplay consequence;
- whether clarification is required and from whom (`source owner`, or `designer` for a draft).

Use `BLOCKER` only when no coherent source-supported interpretation lets players continue through a reachable state or complete the core game loop. Different outcomes alone do not make an ambiguity a blocker. Use `MAJOR` when at least one coherent procedure exists but the issue can change legal actions, outcomes, or repeated play. Use `MINOR` for localized comprehension or editorial problems.

## Output

Begin with:

- sources audited and their authority;
- scope limitations;
- readiness: `READY`, `READY WITH CLARIFICATIONS`, or `NOT READY FOR BLIND PLAYTEST`.

Assign readiness consistently:

- `READY`: no unresolved `BLOCKER` or `MAJOR` findings;
- `READY WITH CLARIFICATIONS`: no blocker, and remaining major issues are localized enough that the core lifecycle is executable once clarified;
- `NOT READY FOR BLIND PLAYTEST`: a blocker or unresolved issue prevents reliable execution of the core lifecycle.

Scope readiness to the affected rules. A problem confined to an optional mode or variant must not lower core-game readiness; report that mode or variant separately.

Then provide the findings in priority order, followed by:

- unresolved authority clarifications, or designer decisions when auditing a draft;
- editorial-only corrections, if any;
- a short coverage summary.

Use the full finding record for `BLOCKER` and `MAJOR` issues. Group `MINOR` and editorial issues compactly. Do not narrate checks that passed unless they materially bound the scope or readiness conclusion.

Do not report an issue merely because the design is unusual. Do not claim the game is balanced, fun, fair, or clear from a rules audit.
