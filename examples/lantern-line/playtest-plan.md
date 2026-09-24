# Lantern Line mechanical playtest plan

## Scope and status

- **Authoritative source:** `revised-rulebook.md`, entire document.
- **Test fixture authority:** fixed hands and deck order below replace random setup only for the named scenario.
- **Limitations:** no component usability, strategy, balance, accessibility, enjoyment, or group communication quality is evaluated.
- **Planning status:** `PLAN READY`.

## Coverage map

| Risk | Card |
| --- | --- |
| Setup at two, three, and four players; hand limit; hidden information | PT-001 |
| Legal and illegal path placement | PT-002 |
| No legal card and storm advancement | PT-003 |
| Empty draw deck while cards remain | PT-004 |
| Empty hand after a skipped draw | PT-005 |
| Immediate victory | PT-006 |
| Immediate storm defeat | PT-007 |

Timing effects, cleanup, and a next round are excluded because this game defines none.

## Scenario cards

### PT-001 — Setup and hidden information

- **Target risk:** setup produces the correct hand size without exposing private cards.
- **Sources:** Components, Setup, Communication.
- **TEST FIXTURE:** run one setup with each supported player count and deal three fixed cards to each player instead of shuffling.
- **Players and roles:** Players A–D as required; A is the youngest and therefore first.
- **Initial public state:** three empty paths, storm at 0, and a face-down draw deck.
- **Private information:** each player sees only their own three-card hand.
- **Action prompt:** complete setup, verify the deck count, let A perform the draw step, then ask each player to describe what information may be communicated.
- **Expected behavior:** every player starts with three cards; the deck contains 12, 9, or 6 cards for two, three, or four players; A draws one card and reaches a hand of four; no hand identity is exposed by color or value.
- **Invariant:** no player holds more than four cards and no private card identity becomes public.
- **Stop condition:** A has drawn and every player has stated the communication boundary.
- **Record:** player count, initial hand counts, initial and post-draw deck count, A's post-draw hand count, any exposed card, any hand-identity statement, and any facilitator intervention.
- **Can establish:** whether setup quantities, the first draw, and the written communication boundary were followed at each supported player count.
- **Cannot establish:** whether the communication restriction is enjoyable or strategically desirable.

### PT-002 — Placement boundary

- **Target risk:** players distinguish a legal higher card from lower and invalid opening cards.
- **Sources:** Turn; legal-card conditions.
- **TEST FIXTURE:** fixed deals and draws produce the legal play history blue 1, gold 1, blue 3, gold 6; stop at the next action step with red empty.
- **Players and roles:** one active player.
- **Initial public state:** paths as described; storm below 6.
- **Private information:** active hand contains red 1, red 2, blue 2, and blue 5.
- **Action prompt:** identify every legal play, then make one.
- **Expected behavior:** red 1 and blue 5 are legal; red 2 and blue 2 are illegal; no card may be added to gold.
- **Invariant:** the selected card matches its path and satisfies the path boundary.
- **Stop condition:** one card is played or the player attempts an illegal card.
- **Record:** chosen card, rejected alternatives, rule lookup, and intervention.
- **Can establish:** whether the placement boundary was executed correctly.
- **Cannot establish:** whether the available choice is interesting or balanced.

### PT-003 — No legal card

- **Target risk:** a player with no legal play discards exactly one card and advances the storm once.
- **Sources:** Turn steps 3–4.
- **TEST FIXTURE:** fixed deals and draws produce the legal play history red 1, blue 1, gold 1, red 4, blue 5, gold 6; stop at the next action step.
- **Players and roles:** one active player.
- **Initial public state:** storm at 4.
- **Private information:** active hand contains red 2, blue 3, and gold 4.
- **Action prompt:** resolve the action step.
- **Expected behavior:** the player places one card face up in the shared discard pile, advances the storm from 4 to 5, and does not play a card.
- **Invariant:** one card leaves the hand, remains publicly visible, and the storm advances exactly one space.
- **Stop condition:** the next player would begin a turn.
- **Record:** discarded card, storm position, illegal play attempt, and intervention.
- **Can establish:** whether forced recovery and non-terminal storm advancement were executed.
- **Cannot establish:** whether the penalty feels fair.

### PT-004 — Continue after deck exhaustion

- **Target risk:** an empty draw deck does not end the game while the active player still has cards.
- **Sources:** Turn steps 1–4; Empty draw deck.
- **TEST FIXTURE:** with two players, use initial hands `A: gold 6, red 6, blue 5` and `B: blue 6, red 1, gold 1`; draw order `gold 2, blue 2, blue 1, red 3, red 2, gold 3, blue 3, blue 4, red 4, red 5, gold 4, gold 5`; execute `discard gold 6, play red 1, blue 1, gold 1, red 2, blue 2, gold 2, red 3, blue 3, gold 3, red 4, blue 4, gold 4, red 5, blue 5, gold 5`.
- **Players and roles:** Player A is active; Player B follows.
- **Initial public state:** draw deck empty; every path is topped by 5; storm at 1; gold 6 is face up in the discard pile.
- **Private information:** A holds red 6; B holds blue 6.
- **Action prompt:** let A and B each take one complete turn, then stop before A resolves the next draw step.
- **Expected behavior:** both players skip drawing; A plays red 6, B plays blue 6, and play continues because gold remains incomplete.
- **Invariant:** no card is drawn or reshuffled.
- **Stop condition:** A becomes active again with an empty hand.
- **Record:** draw attempts, played cards, hand counts, path tops, and next player.
- **Can establish:** whether play continues correctly after deck exhaustion.
- **Cannot establish:** whether deck exhaustion occurs at an appropriate frequency.

### PT-005 — Empty-hand defeat

- **Target risk:** the game stops before an empty-handed player attempts an action.
- **Sources:** Turn step 2; Empty draw deck; End conditions.
- **Reachability:** continue from PT-004 after B plays blue 6 and A becomes active again.
- **Players and roles:** one active player.
- **Initial public state:** draw deck empty, storm below 6, and at least one path incomplete.
- **Private information:** active hand is empty.
- **Action prompt:** begin the turn.
- **Expected behavior:** skip drawing and lose immediately; no play or discard occurs.
- **Invariant:** the state does not advance after the loss is declared.
- **Stop condition:** defeat is declared.
- **Record:** any attempted action after the skipped draw and the moment defeat is declared.
- **Can establish:** whether the empty-hand stop rule is applied at the correct time.
- **Cannot establish:** whether players consider this ending satisfying.

### PT-006 — Immediate victory

- **Target risk:** completing the third path ends play immediately.
- **Sources:** Turn step 4; End conditions.
- **TEST FIXTURE:** fixed deals and draws produce the legal play history red 1, red 6, blue 1, blue 6, gold 1, gold 5; stop at the next action step.
- **Players and roles:** one active player.
- **Initial public state:** storm at 0; draw step already complete.
- **Private information:** active hand contains gold 6.
- **Action prompt:** resolve the legal play.
- **Expected behavior:** play gold 6 and declare victory immediately.
- **Invariant:** no later turn begins and the storm does not advance.
- **Stop condition:** victory is declared.
- **Record:** played card, declared result, and any action attempted afterward.
- **Can establish:** whether the victory check stops the game.
- **Cannot establish:** whether the victory condition is too easy or difficult.

### PT-007 — Immediate storm defeat

- **Target risk:** the sixth storm advance ends play immediately.
- **Sources:** Turn steps 3–4; End conditions.
- **TEST FIXTURE:** with two players, use initial hands `A: red 6, gold 6, gold 4` and `B: blue 6, blue 4, red 3`; draw order `red 4, red 2, blue 3, blue 2, gold 3, red 1, red 5, blue 1, blue 5, gold 1, gold 5, gold 2`; execute `discard red 6, blue 6, gold 6, blue 4, gold 4, then play red 1, red 5, blue 1, blue 5, gold 1, gold 5`. Player B then draws gold 2.
- **Players and roles:** one active player.
- **Initial public state:** storm at 5 and at least one path incomplete.
- **Private information:** Player B holds red 2, red 3, blue 2, and gold 2; none is legal above the three path values of 5.
- **Action prompt:** resolve the action step.
- **Expected behavior:** place one card face up in the shared discard pile, advance the storm to 6, and declare defeat immediately.
- **Invariant:** no next turn begins after the storm reaches 6.
- **Stop condition:** defeat is declared.
- **Record:** discarded card, storm movement, declared result, and any later action.
- **Can establish:** whether storm defeat is resolved at the correct time.
- **Cannot establish:** whether the storm track creates good tension.

## Run sheet

Run the cards in order. The facilitator sets fixtures but does not explain the expected behavior. Record exact actions, rule lookups, questions, and interventions before discussing causes. Stop a card after an illegal state transition or a disputed expectation; do not repair the rules during the run. Treat deviations as observations for review, not automatic proof of a rulebook defect.
