# Tabletop Design Lab

An open-source, skill-based workflow for turning tabletop rulebooks into traceable design evidence.

The first release does one thing: it audits written rules without inventing missing answers.

## Why it exists

Rulebook reviews often mix three different activities: identifying what the rules say, guessing what the designer intended, and proposing a fix. `rules-audit` keeps them separate so a designer can resolve the right problem before a blind playtest.

It can find contradictions, ambiguity, missing rules, terminology drift, and unresolved timing. It cannot determine whether a game is fun, balanced, fair, or understandable to real players.

## Quick start

1. Copy [`skills/rules-audit`](skills/rules-audit) into your Codex skills directory.
2. Start a new task with your rulebook available.
3. Ask: `Use $rules-audit to audit this rulebook for blind-playtest readiness.`

To inspect the repository without installing anything, compare the deliberately flawed [Lantern Line rulebook](examples/lantern-line/rulebook.md) with its [example audit](examples/lantern-line/audit.md).

## v0.1 scope

- One Codex skill: `rules-audit`.
- One original, redistributable example game.
- One deterministic repository check using the Python standard library.
- No automated balancing, simulated players, or claims about human experience.

## Principles

- Source text outranks assumptions.
- Diagnosis is separate from solution design.
- Uncertainty stays visible until the designer resolves it.
- AI-generated analysis is a lead for investigation, not playtest evidence.

## Check the repository

```bash
python -m unittest discover -s tests
```

The check rejects unfinished skill scaffolding and common document formats that could accidentally introduce private or third-party source material.

## Status

Experimental. The current skill has been exercised on the included example; broader game coverage is not yet established.

## License

MIT. See [LICENSE](LICENSE).
