# Contributing

Corrections are the most valuable contribution here. LinkedIn changes its
limits, gates and ranking behaviour without notice, and a reference file that
is six months stale produces confidently wrong drafts.

## Most useful contributions, in order

1. **A platform limit that changed.** A character count, a gating rule (the
   newsletter follower threshold, the notify-employees interval), an eligible
   ad format. Put the number in `lib/surfaces.py` or the relevant reference
   file, and say where you verified it.
2. **A benchmark with a better source.** Every figure in
   `references/page-algorithm-heuristics.md` carries its provenance. If you
   have a primary source where we cite a vendor roundup, that is a direct
   upgrade.
3. **Banned-vocabulary lists for other languages.** The lists in
   `references/brand-voice-rules.md` are English. Corporate filler and AI
   register exist in every language and the structure transfers; the words do
   not.
4. **A format that works and is not in the sixteen.** Open an issue with two
   real examples and what job it does. Formats earn their place by being
   fillable from evidence a company actually has.
5. **Bug fixes in `lib/` or `scripts/`.**

## Before opening a pull request

```bash
python -m scripts.selftest                    # 19 checks
python -m tests.test_instruction_integrity    # handoff contracts
python -m scripts.check_markdown_references   # every pointer resolves
python -m scripts.check_no_secrets            # no filled template, no token
```

All four must pass. `check_markdown_references` matters more than it looks: a
broken reference pointer does not error, it just makes a skill quietly thinner.

## Conventions

- **Cite, do not assert.** Any number added to a reference file carries its
  source and the date it was read. A figure with no provenance will be asked
  for one in review.
- **Keep `SKILL.md` under ~250 lines.** Detail goes in `references/` with a
  pointer. Progressive disclosure is the reason the bundle is usable at all.
- **One rule, one home.** If a rule needs to apply in two skills, it goes in
  `references/` and both cite it. Two copies is how two paths quietly stop
  agreeing — see `references/precedence.md` §Handoffs.
- **No new runtime dependencies.** `lib/` is standard library only and the
  default path makes no network call. That is a feature, not an accident.
- **Do not weaken the claim gate.** The rule that no figure publishes without a
  cleared proof row is the core of the project. A PR that adds a convenience
  path around it will be declined.
- **Do not add detector claims.** `tests/test_instruction_integrity.py` fails
  the build on any affirmative claim about beating AI detectors.
- **Templates ship blank.** Never commit a filled `company-profile.md`,
  `proof-library.md`, `claims-and-compliance.md`, `icp-firmographics.md` or
  `competitor-set.md`.

## Testing a skill change

The repo ships three eval cases under `evals/`, in the layout
`claude plugin eval` reads. They test judgement under pressure rather than
output formatting:

- `refuses-unevidenced-number` — the user invites a fabricated statistic
- `audits-corporate-draft` — a press-release draft needing a verdict
- `plans-within-capacity` — a request that contradicts its own constraints

If your change touches a writing or planning skill, run them and say what
happened in the PR.

## Reporting a problem

Open an issue with the skill name, what you asked for, and what you got. For a
platform-limit correction, include where you verified the new value — that is
the part that makes the fix mergeable.
