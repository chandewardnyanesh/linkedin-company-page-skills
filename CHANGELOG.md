# Changelog

All notable changes to this project are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/); this project uses
[semantic versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] — 2026-11-19

First public release. 13 skills, 14 shared reference files, no dependencies.

### Skills

- `page-profile-builder` — website and Page research into the canonical brand
  profile, proof library, ICP and competitor set
- `page-optimizer` — audit and rewrite of tagline, About, specialties, custom
  button, Products, Services, Featured and Life tab
- `trend-radar` — ranked content opportunities with graded evidence; uses
  Search Console, Ahrefs or Semrush connectors when present
- `competitor-page-analyzer` — competitor cadence, formats, newsletters,
  employees posting, and white-space mapping
- `page-content-calendar` — 30-day multi-surface plan built on stated capacity
- `page-post-writer` — page posts across 16 brand formats
- `authority-article-writer` — Articles and newsletter issues across 8
  authority architectures, with eligibility checking
- `page-humanizer` — de-AI and de-corporate rewriting, plus a six-gate
  `--mode audit` pre-publish review
- `page-repurposer` — one source into several native assets across surfaces
- `page-asset-extractor` — `--mode pattern` post deconstruction and
  `--mode proof` document mining
- `employee-amplification` — per-person reshare kits, notify budget, Thought
  Leader Ad selection
- `page-engagement-desk` — comment replies, complaint triage, escalation
- `page-performance-report` — monthly reporting against the Page's own baseline

### Library

- `lib/surfaces.py` — every Page surface limit with its provenance, plus a
  draft checker and fold preview
- `lib/url_parser.py` — Page URLs to slug, numeric id and organization URN.
  Refuses to derive a URN from a vanity slug rather than guess
- `lib/approval.py` — approval card with a claims-and-sources block that warns
  when a draft carries figures and no claim list
- `lib/backend_selector.py` — manual publish path with a shell-only extension
  point, and an explicit record of which surfaces no API can reach

### Tooling

- `scripts/fit` — surface limit checker, usable as a CLI gate
- `scripts/selftest` — 19 offline checks
- `scripts/check_frontmatter`, `check_markdown_references`, `check_no_secrets`
- `tests/test_instruction_integrity` — 57 checks on cross-skill handoff
  contracts, reference consistency and the no-detector-claims rule
- `evals/` — three test cases in `claude plugin eval` layout

### Notes

- Platform limits and benchmarks were observed in 2026 and carry their sources
  in `references/page-algorithm-heuristics.md`
- Articles and newsletters have no LinkedIn publishing API; those skills are
  draft-and-paste by design rather than by omission
