---
name: playtest-planner
description: Turn an executable tabletop rulebook and optional rules audit into a small set of traceable scenario cards for blind or agent-assisted testing. Use to prepare mechanical rule tests before a playtest; do not simulate players or claim evidence about fun, balance, or engagement.
---

# Playtest Planner

Create reproducible tests for rule execution without turning expected behavior into playtest evidence.

## Sources and readiness

1. Identify the authoritative rulebook, optional audit, and any approved clarifications.
2. Treat test fixtures as scenario setup, never as new game rules.
3. Do not silently resolve an audit finding or incomplete rule.
4. Assign one planning status:
   - `PLAN READY`: the tested lifecycle is executable;
   - `PLAN WITH BRANCHES`: localized ambiguity can be tested under named interpretations;
   - `BLOCKED FOR PLANNING`: setup, a required transition, or an end condition cannot be executed without a design decision.
5. When blocked, output only the blocking decisions and the coverage they prevent. Do not manufacture scenario cards.

## Select scenarios

Build the smallest useful set of cards. Prioritize demonstrated audit risks, then cover distinct lifecycle boundaries:

- setup and visibility;
- supported player counts when they change setup quantities or resource exhaustion;
- a normal legal action and a nearby illegal action;
- timing or triggered effects when present;
- a failed action or forced recovery;
- deck, pile, component, or resource exhaustion;
- no-legal-action states;
- success, failure, and cleanup or the next round when present.

Every scenario must begin from a state that setup and legal transitions can reach. State the reachability path or label a deterministic replacement for random setup as a `TEST FIXTURE`. Merge scenarios that test the same rule boundary. Use at most eight cards by default.

Do not enumerate every permutation. Exclude cases whose only difference cannot change legality, state, timing, or termination.

## Scenario card

Give each card a stable ID (`PT-001`, `PT-002`, ...), then record:

- target risk;
- exact rule sources;
- reachability or test fixture;
- players and roles;
- initial public state;
- private information by player, if any;
- action prompt;
- source-supported expected behavior;
- invariant that must remain true;
- stop condition;
- observations to record without interpretation;
- what the scenario can and cannot establish.

If the source supports multiple interpretations, name each branch and its expected result. Never select the most convenient branch.

## Output

Begin with authoritative sources, limitations, and planning status. Then provide:

1. a compact coverage map linking each lifecycle risk to a card or an explicit exclusion;
2. scenario cards in execution order;
3. a short run sheet telling the facilitator when to intervene, stop, and record a rules lookup.

Keep rule expectations separate from observations. An observed deviation may show that the rule was applied differently; it does not by itself prove that the rulebook is unclear.

Do not report the game as fun, balanced, accessible, strategically sound, or validated. Agent execution is a rehearsal of rule application, not a substitute for human playtest evidence.
