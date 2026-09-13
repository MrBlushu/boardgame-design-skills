# Lantern Line rules audit

## Scope and readiness

- **Authoritative source:** `rulebook.md`, entire draft.
- **Limitations:** no component images, designer notes, or playtest observations were supplied.
- **Readiness:** `NOT READY FOR BLIND PLAYTEST`.

## Findings

### RA-001 — Contradiction — BLOCKER

- **Source:** Setup limits hands to three cards, while Turn step 1 requires drawing to four.
- **Observed issue:** A player cannot obey the draw instruction without violating the absolute hand limit.
- **Strongest source-supported resolution:** Treating the turn procedure as more specific still requires drawing a fourth card while the absolute limit remains three, so the instructions cannot be reconciled without changing one of them.
- **Possible interpretations:** The maximum hand size should be four; or the turn should not begin by drawing to four.
- **Concrete witness:** Every player starts with three cards; on that player's first turn, step 1 requires drawing to four while the stated maximum remains three.
- **Gameplay consequence:** Players cannot determine the intended hand cycle or when the deck is consumed.
- **Clarification required:** Yes — designer.

### RA-002 — Missing rule — BLOCKER

- **Source:** Setup and Turn define draws, but no section defines what happens when the Lantern deck is empty.
- **Observed issue:** A reachable draw step has no resolution.
- **Strongest source-supported resolution:** Neither the end conditions nor the turn procedure supplies a stop, reshuffle, or failed-draw rule, so no source-supported resolution exists.
- **Concrete witness:** With four players, setup deals twelve of eighteen cards. If six draw steps occur without an end condition, the next turn still requires a draw from the empty deck.
- **Gameplay consequence:** Play may stop before either win or loss condition occurs.
- **Clarification required:** Yes — designer.

### RA-003 — Missing rule — MAJOR

- **Source:** Components include six Storm cards, but Setup and Turn never instruct players to place, draw, or resolve them.
- **Observed issue:** A listed component has no defined function.
- **Strongest source-supported resolution:** The storm marker can advance without the cards, but that does not determine whether the listed cards are extraneous or an omitted subsystem.
- **Concrete witness:** Immediately after following setup, all six Storm cards remain outside the defined game state, and no later phase references them.
- **Gameplay consequence:** Players cannot know whether the storm marker should advance only after a failed play or also through an omitted Storm-card procedure.
- **Clarification required:** Yes — designer.

### RA-004 — Ambiguity — MAJOR

- **Source:** Players may discuss cards, but hands must remain secret.
- **Observed issue:** “Secret” may prohibit showing cards, naming exact cards, or both.
- **Strongest source-supported resolution:** Reading “secret” as a ban on physical display is compatible with discussion, but the source does not say whether exact verbal disclosure is included in the permission to discuss.
- **Possible interpretations:** Verbal disclosure is allowed; only physical cards are hidden; or exact card information is prohibited.
- **Concrete witness:** A player can propose naming an exact card while keeping it physically hidden; the permission to discuss cards and the secrecy rule do not determine whether that communication is legal.
- **Gameplay consequence:** The available cooperation and memory burden vary materially.
- **Clarification required:** Yes — designer.

## Unresolved authority clarifications

1. Define the hand and draw cycle.
2. Define deck exhaustion.
3. Define the role of Storm cards or remove them from the component list.
4. Define what information players may communicate.

## Coverage summary

The audit found two blockers and two major issues. It does not evaluate balance, enjoyment, fairness, or real-player comprehension.
