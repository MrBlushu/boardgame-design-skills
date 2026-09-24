# Boardgame Design Skills

![A paladin, a wizard, and a dragon playing cards around a tavern table in pixel art](assets/readme-banner.png)

An open-source lab of Codex skills for tabletop-game design. The first release focuses on one narrow job: finding rulebook defects before a blind playtest without inventing missing rules.

## What `rules-audit` does

The skill checks a supplied rulebook for contradictions, ambiguity, missing rules, terminology drift, and unresolved timing. Each serious finding includes its source, the strongest counter-reading, a legal example that reaches the problem, and its gameplay consequence.

It produces one of three scoped readiness outcomes:

- `READY`
- `READY WITH CLARIFICATIONS`
- `NOT READY FOR BLIND PLAYTEST`

It does not judge balance, fun, fairness, or player comprehension. Those require playtest evidence.

## Try it

1. Copy [`skills/rules-audit`](skills/rules-audit) into your Codex skills directory as `rules-audit`.
2. Start a new Codex task and attach or reference your rulebook.
3. Use this prompt:

   ```text
   Use $rules-audit to audit the attached rulebook. Treat only the supplied document as authoritative. Do not browse or rely on remembered rules.
   ```

For a result you can inspect immediately, compare the original [Lantern Line rulebook](examples/lantern-line/rulebook.md) with its [example audit](examples/lantern-line/audit.md).

## How the method works

The skill keeps five things separate: written rules, reasonable inferences, unresolved uncertainty, demonstrated problems, and proposed fixes. A `BLOCKER` or `MAJOR` finding needs a legal sequence supported by every plausible reading. Optional modes are assessed separately from the core game.

This is a human-in-the-loop review method, not a deterministic validator. Model output can vary, severity still needs editorial judgment, and a clean audit does not prove that a rulebook will succeed with players. See [Evaluation notes](BENCHMARK.md) for the current evidence and known failure modes.

## In development

[`playtest-planner`](skills/playtest-planner) turns an executable rulebook and optional audit into a small set of traceable scenario cards. It prepares mechanical checks for human or agent-assisted testing without claiming evidence about fun or balance. See the [Lantern Line example plan](examples/lantern-line/playtest-plan.md).

## Verify the repository

Run the standard-library checks:

```bash
python -m unittest discover -s tests -v
```

They verify the public example and reject common document formats that could accidentally add private or third-party source material.

## Project boundaries

- Public content is written in English.
- Examples are original and redistributable.
- Third-party rulebooks and private game files are never committed.
- New skills are added only after an end-to-end example demonstrates a real need.

## Roadmap

- [x] Release `rules-audit` with an original fixture and an anonymous evaluation record.
- [x] Add a skill that turns audit findings into a focused blind-playtest checklist.
- [ ] Add a skill that structures playtest observations without presenting them as rules.
- [ ] Expand the anonymous benchmark with repeated runs to track consistency.

Development happens on `develop`. Each skill starts with an original, redistributable fixture, is tested locally against more complex rulebooks that are never committed, and reaches `main` only after its example, documentation, and repository checks agree.

Release history is in [CHANGELOG.md](CHANGELOG.md). Contributions should follow [AGENTS.md](AGENTS.md).

## License

MIT. See [LICENSE](LICENSE).
