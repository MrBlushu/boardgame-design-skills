# Lantern Line rules audit

## Scope and readiness

- **Authoritative source:** `rulebook.md`, entire draft.
- **Limitations:** no component images, designer notes, or playtest observations were supplied.
- **Readiness:** `NOT READY FOR BLIND PLAYTEST`.

## Findings

### RA-001 — Contradiction — BLOCKER

- **Source:** Setup limits hands to three cards, while Turn step 1 requires drawing to four.
- **Observed issue:** A player cannot obey the draw instruction without violating the absolute hand limit.
- **Possible interpretations:** The maximum hand size should be four; or the turn should not begin by drawing to four.
- **Concrete witness:** Every player starts with three cards; on that player's first turn, step 1 requires drawing to four while the stated maximum remains three.
- **Gameplay consequence:** Players cannot determine the intended hand cycle or when the deck is consumed.
- **Clarification required:** Yes — designer.

### RA-002 — Missing rule — BLOCKER

- **Source:** Setup and Turn define draws, but no section defines what happens when the Lantern deck is empty.
- **Observed issue:** A reachable draw step has no resolution.
- **Concrete witness:** With four players, setup deals twelve of eighteen cards. If six draw steps occur without an end condition, the next turn still requires a draw from the empty deck.
- **Gameplay consequence:** Play may stop before either win or loss condition occurs.
- **Clarification required:** Yes — designer.

### RA-003 — Ambiguity — MAJOR

- **Source:** Turn, step 3: “If you cannot play a card...”
- **Observed issue:** The rules do not say whether playing is mandatory when a legal card exists.
- **Possible interpretations:** A player must play when able; or a player may decline and take the storm penalty.
- **Concrete witness:** A player who holds a legally playable card still reaches the conditional wording “If you cannot play,” without a rule saying whether declining is legal.
- **Gameplay consequence:** Players may gain or lose control over hand management and storm timing.
- **Clarification required:** Yes — designer.

### RA-004 — Missing rule — MAJOR

- **Source:** Components include six Storm cards, but Setup and Turn never instruct players to place, draw, or resolve them.
- **Observed issue:** A listed component has no defined function.
- **Concrete witness:** Immediately after following setup, all six Storm cards remain outside the defined game state, and no later phase references them.
- **Gameplay consequence:** Players cannot know whether the storm marker should advance only after a failed play or also through an omitted Storm-card procedure.
- **Clarification required:** Yes — designer.

### RA-005 — Ambiguity — MAJOR

- **Source:** Players may discuss cards, but hands must remain secret.
- **Observed issue:** “Secret” may prohibit showing cards, naming exact cards, or both.
- **Possible interpretations:** Verbal disclosure is allowed; only physical cards are hidden; or exact card information is prohibited.
- **Concrete witness:** A player can propose naming an exact card while keeping it physically hidden; the permission to discuss cards and the secrecy rule do not determine whether that communication is legal.
- **Gameplay consequence:** The available cooperation and memory burden vary materially.
- **Clarification required:** Yes — designer.

## Unresolved authority clarifications

1. Define the hand and draw cycle.
2. Define deck exhaustion.
3. Decide whether a legal play is mandatory.
4. Define the role of Storm cards or remove them from the component list.
5. Define what information players may communicate.

## Coverage summary

The audit found two blockers and three major issues. It does not evaluate balance, enjoyment, fairness, or real-player comprehension.
