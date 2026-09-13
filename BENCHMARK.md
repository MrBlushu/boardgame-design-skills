# Evaluation notes

`rules-audit` was evaluated as a human-reviewed analysis method, not as a deterministic rules engine. The sample is small and qualitative, so it does not support an accuracy percentage.

External rulebooks were reviewed locally and are not included in this repository. The descriptions below are intentionally anonymous and contain no reproduced rules or artwork.

## Cases

| Case | Document profile | What it tested | Observed result |
| --- | --- | --- | --- |
| Original microgame | Short text-only draft with deliberate defects | Baseline detection and traceable witnesses | Found two blockers and two major issues; the public fixture reproduces this case. |
| Abstract strategy game | Polished commercial rulebook with diagrams | Reconciliation of prose, examples, and visual evidence | Core play remained executable; two edge cases needed clarification. |
| Cooperative card game | Long, structured commercial rulebook | Restraint on a mostly complete source | No serious defect was reported; two localized minor issues remained. |
| Deduction card game | Unofficial translated rulebook | Resistance to wording noise and missing reference material | Early runs overclassified ambiguities and varied between passes. This exposed the need for legal witnesses and counter-readings. |
| Bluffing card game | Translated rulebook with an optional mode | Scoped readiness and component exhaustion | A later run stopped optional-mode defects from lowering core readiness and retained a material resource-exhaustion issue. Some severity still required human correction. |

## What improved during evaluation

- Serious findings now require a concrete legal witness that does not assume the disputed rule.
- Every serious finding must state the strongest source-supported resolution before claiming a gap.
- Shared concepts such as targeting, discarding, and protection are checked across the whole source.
- Optional modes receive their own readiness result.
- Findings with one root cause are merged.

## Known failure modes

- **Severity inflation:** a unique, coherent reading may still be reported as a major ambiguity when the source contains a clear typo.
- **Compound findings:** a valid major issue can absorb a weaker edge case that should be minor or omitted.
- **Run-to-run variance:** different passes may find different plausible issues.
- **Source limits:** missing cards, player aids, diagrams, or unreadable pages reduce what can be verified.
- **No experiential evidence:** the method cannot establish fun, balance, accessibility, or real-player comprehension.

## Release criterion

Version 0.1.0 is considered useful when it produces traceable leads, suppresses unsupported major findings through counterevidence checks, and keeps readiness scoped to the affected mode. A human reviewer remains responsible for the final severity and design decision.
