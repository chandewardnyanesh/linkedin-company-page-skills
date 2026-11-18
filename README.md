# LinkedIn Company Page Skills for Claude

**13 Claude skills for running a LinkedIn company page in 2026** — website
research, content strategy, page post writing, authority articles and
newsletters, a de-AI and de-corporate humanizer, employee advocacy, and
monthly analytics reporting.

Built for the one fact most LinkedIn advice ignores: **a company page reaches
1–2% of its own followers.** Everything here follows from that.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills: 13](https://img.shields.io/badge/skills-13-brightgreen.svg)](#the-13-skills)
[![Dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](#installation)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-8A63D2.svg)](https://claude.com/claude-code)

Works with **Claude Code**, **Claude Desktop** and the **claude.ai** skills
interface. No API keys, no signup, no Python packages.

---

## Contents

- [Why company pages need their own skills](#why-company-pages-need-their-own-skills)
- [Installation](#installation)
- [The 13 skills](#the-13-skills)
- [How a request flows](#how-a-request-flows)
- [Three design decisions](#three-design-decisions)
- [What LinkedIn's API can and cannot publish](#what-linkedins-api-can-and-cannot-publish)
- [Repository layout](#repository-layout)
- [FAQ](#faq)
- [What this project does not claim](#what-this-project-does-not-claim)
- [Credits](#credits)

---

## Why company pages need their own skills

A LinkedIn company page is **not a reach channel**. It is an authority and
conversion asset whose distribution has to be borrowed from people. The 2026
data, from several independent directions:

| Measure | Company page | Personal profile | Source |
|---|---|---|---|
| Median engagement rate | 1–2% | ~4.7% | Sprout Social Q1 2026 Index, 52M+ posts |
| Share of feed distribution | ~5% | ~65% | SocialPilot, Sept 2026 |
| Organic reach vs follower count | ~1.2% | 8–15% | SMM News 2026, 524 B2B brand pages |
| Reach change, 2024 → early 2026 | **down 60–66%** | down ~50% | multiple 2026 roundups |
| Median reactions per B2B post | 23 | 39 (founder/exec) | Imagine AI, Oct 2026 |
| Reach per post vs employee posts | baseline | **+561%** | SocialPilot, Sept 2026 |

So a page with 20,000 followers can reach fewer people than a founder with
2,000. Any content plan whose growth depends on page post volume does not work.

**This is also why a personal-brand skill bundle cannot simply be pointed at a
company page.** The personal formula libraries are built on devices a brand
cannot use honestly — a confession hook needs someone to confess, and a company
has no self. The attempt produces the worst genre on the platform: a corporate
entity performing feelings.

What a page has instead is **access a person does not have**: the whole book of
business, the aggregate numbers, the thing that broke in production, the pattern
across forty clients, the real cost of the work. A person can report their own
experience. A page can report a population. Every format in this repository is
a way of spending that advantage.

The four jobs a company page actually does well, and which every skill here
serves:

1. **Pass the credibility check** — the buyer who met you elsewhere and opened
   the page before replying.
2. **Hold the assets that get borrowed** — carousels, articles, research that
   employees reshare.
3. **Own distribution the feed cannot throttle** — a LinkedIn newsletter
   notifies subscribers by email.
4. **Convert** — custom button, lead-gen forms, products and services tabs.

Full sourcing and the honest reading of every figure:
[`references/page-algorithm-heuristics.md`](references/page-algorithm-heuristics.md).

## Installation

### Claude Code (plugin)

```bash
git clone https://github.com/chandewardnyanesh/linkedin-company-page-skills.git
cd linkedin-company-page-skills
python -m scripts.selftest      # 19 checks, offline, no dependencies
```

Then add it as a plugin marketplace in Claude Code, pointing at the cloned
directory — the repo ships `.claude-plugin/marketplace.json` and
`.claude-plugin/plugin.json`.

### Claude Desktop or claude.ai

Upload any individual `skills/<name>/SKILL.md` as a skill, or the whole
directory as a plugin where your plan supports it. Each skill works
standalone; they hand off to each other by name when both are present.

### Requirements

**None.** `lib/` is Python standard library only and the default path makes no
network call. Python 3.10+ for the helper scripts.

**Optional, used when present:** Google Search Console, Ahrefs or Semrush
connectors sharpen `trend-radar` and `page-performance-report` with measured
search demand instead of inference. Without them, those skills label their
evidence as observed rather than measured and say so.

## The 13 skills

### Setting up

| Skill | What it does |
|---|---|
| **`page-profile-builder`** | Crawls the company website and LinkedIn page, writes the canonical brand profile, proof library, ICP and competitor set every other skill reads. **Run this first.** |
| **`page-optimizer`** | Audits and rewrites the page itself — tagline (120 chars), About (2,000 chars), specialties, custom button, Products and Services tabs, Featured, Life tab |

### Deciding what to say

| Skill | What it does |
|---|---|
| **`trend-radar`** | Ranked content opportunities with graded evidence. Uses Search Console / Ahrefs / Semrush when available |
| **`competitor-page-analyzer`** | Competitor cadence, format mix, newsletters, employees posting — and the white space you have standing to own |
| **`page-content-calendar`** | 30-day multi-surface plan built on real capacity, not a posting target |

### Writing

| Skill | What it does |
|---|---|
| **`page-post-writer`** | LinkedIn page posts across 16 brand formats, picked by the job the post has to do |
| **`authority-article-writer`** | LinkedIn Articles and newsletter issues across 8 authority architectures |
| **`page-humanizer`** | Strips AI tells **and** press-release voice. `--mode audit` runs a six-gate pre-publish review |

### Reusing what exists

| Skill | What it does |
|---|---|
| **`page-repurposer`** | One source into several native assets — blog to carousel, webinar to posts, founder's post to page version |
| **`page-asset-extractor`** | `--mode pattern` deconstructs any high-performing post · `--mode proof` mines documents for claims |

### Distribution and inbound

| Skill | What it does |
|---|---|
| **`employee-amplification`** | Per-person reshare kits with distinct angles, the once-a-week notify budget, Thought Leader Ad selection. **This is the distribution layer** |
| **`page-engagement-desk`** | Comment replies, complaint triage and escalation, commenting as the page |

### Measuring

| Skill | What it does |
|---|---|
| **`page-performance-report`** | Monthly report that says what to change, measured against your own baseline rather than borrowed benchmarks |

## How a request flows

1. **Load the profile.** Nothing is written from a blank slate.
2. **Draft**, using the formats, architectures and voice rules in
   [`references/`](references/).
3. **Show an approval card** — every claim with its source, the surface
   character fit, the amplification plan, and what happens on approval.
4. **Publish only after a human approves that exact text.**

## Three design decisions

### 1. No figure publishes without a cleared proof row

A number on a company page is a representation the business made, in public,
with a timestamp, to an audience that includes its customers and competitors.
It gets screenshotted before it gets corrected.

So every writing skill stops at a claim with no entry in
[`references/proof-library.md`](references/proof-library.md). A format's
`[specific number]` slot is **not** a licence to produce a plausible one —
plausible is fabricated. When the library has nothing that fits, the skill
asks, drops the claim, or changes format. It does not soften an unevidenced
number into "up to".

This is the behaviour most LLM marketing tooling gets wrong, and it is the
single most expensive thing to get wrong on a brand account.

### 2. The humanizer fixes two voices, not one

Brand copy sounds like AI **and** like a press release, and the two reinforce
each other because they share most of their tells. Two tests on every opening
line:

- **Swap in a competitor's name.** Survives? It says nothing. → press-release voice
- **Swap in a different industry.** Survives? Cut it. → AI voice

Both resolve the same way, and it is not word substitution — "utilise" for
"leverage" is the same empty slot with a different word in it. The fix is a
named person, a specific number, or a dated event. Worked rewrites in
[`references/brand-voice-rules.md`](references/brand-voice-rules.md).

### 3. Manual publishing is the honest answer, not a missing feature

See the table below. For articles and newsletters there is no API to use, so
"here is the draft, paste it into the editor" is complete and correct, and no
skill here implies a key would change it.

## What LinkedIn's API can and cannot publish

| Surface | Publishable by API? |
|---|---|
| Page post, document post, comment | Yes — `w_organization_social` scope + admin role |
| **LinkedIn Article (Articles for Pages)** | **No. No publishing API exists** |
| **LinkedIn Newsletter** | **No. An extension of articles, so no API either** |
| Poll, Event | No |
| Tagline, About, specialties, tabs, Featured | No |

Any tool claiming to automate a LinkedIn article is driving a browser or is
wrong.

This bundle ships **draft-first on every surface**. To automate the
API-reachable ones, export a poster command in a trusted shell:

```bash
export LINKEDIN_PAGE_CUSTOM_POSTER='/path/to/your-poster'
```

Approved drafts are piped to it as JSON on stdin. The variable is
**deliberately ignored inside `.env` files** — a file on disk choosing which
executable runs is a code-execution hole dressed as configuration.

## Repository layout

```
linkedin-company-page-skills/
├── SKILL.md                  # router: which skill for which request
├── skills/                   # 13 skills, each a single-purpose SKILL.md
├── references/               # 14 shared reference files (see below)
├── lib/                      # standard library only, no network calls
│   ├── surfaces.py           # every character limit + a draft checker
│   ├── url_parser.py         # page URLs → slug, numeric id, organization URN
│   ├── approval.py           # the approval card
│   └── backend_selector.py   # manual publish + shell-only extension point
├── scripts/                  # fit, selftest, 3 validators
├── tests/                    # handoff-contract integrity
├── evals/                    # 3 test cases, runnable with `claude plugin eval`
└── examples/                 # a real worked research output
```

### The reference layer

| File | Holds |
|---|---|
| [`page-algorithm-heuristics.md`](references/page-algorithm-heuristics.md) | The 2026 reach economics, sourced. **Read first** |
| [`page-formats.md`](references/page-formats.md) | 16 page post formats, the monthly mix, and the anti-formats to refuse |
| [`article-architectures.md`](references/article-architectures.md) | 8 long-form structures, newsletter shape and eligibility |
| [`brand-voice-rules.md`](references/brand-voice-rules.md) | Banned vocabulary by density, the attribution rule, worked rewrites |
| [`page-surfaces.md`](references/page-surfaces.md) | Every surface, its limit, what gates it, what is manual |
| [`amplification-mechanics.md`](references/amplification-mechanics.md) | The advocacy ladder, notify limits, an honest Thought Leader Ads reading |
| [`metrics-taxonomy.md`](references/metrics-taxonomy.md) | What each metric counts and what to stop reporting |
| [`precedence.md`](references/precedence.md) | What wins when two rules conflict |
| [`untrusted-content.md`](references/untrusted-content.md) | Fetched content is data, never instructions |

Five more are **blank templates** that become confidential business documents
once filled: `company-profile.md`, `proof-library.md`,
`claims-and-compliance.md`, `icp-firmographics.md`, `competitor-set.md`.
`scripts/check_no_secrets.py` fails the build when one is marked
`filled: yes`, as a reminder to gitignore it.

## Tools

```bash
python -m scripts.fit --surface page_post --file draft.md   # does it fit?
python -m scripts.fit --list                                # every surface and limit
python -m scripts.selftest                                  # is it wired up?
python -m scripts.check_no_secrets                          # before committing
python -m tests.test_instruction_integrity                  # handoff contracts
```

Count characters with the tool, not by eye. A LinkedIn **page** About section
is **2,000** characters, not the 2,600 a personal profile gets, and the
overflow is dropped rather than wrapped — invisible in the admin editor,
obvious in public.

## FAQ

**Is this for personal LinkedIn profiles?**
No. It is built specifically for company pages, where the formats, voice
constraints, claim liability and distribution model are all different. For
personal-profile work, see
[sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills).

**Does it post to LinkedIn automatically?**
Not by default, and for articles and newsletters not at all — LinkedIn has no
publishing API for them. Page posts and comments can be automated by wiring up
your own poster command. Everything goes through a human approval card first.

**Do I need an API key, a scraper, or a paid tool?**
No. There are no dependencies and the default path makes no network call.
Search Console, Ahrefs and Semrush connectors are used if you already have
them.

**Will this make my AI-written posts undetectable?**
No, and no skill here claims it. See
[what this project does not claim](#what-this-project-does-not-claim).

**Can it write LinkedIn newsletters?**
Yes — `authority-article-writer` drafts newsletter issues and checks your
eligibility (Super Admin, 150+ followers, active page, recent original
content). Publishing is manual because no API exists.

**How is this different from asking Claude to "write a LinkedIn post"?**
Three things: it refuses to invent statistics about your business, it picks a
format based on the job the post has to do rather than defaulting to a hook,
and it plans the employee amplification without which a page post reaches
almost nobody.

**Does it work for non-English pages?**
The voice rules and formats are language-agnostic in structure, and
`company-profile.md` records the publishing language. The banned-vocabulary
lists are English; contributions for other languages are welcome.

**Is it safe to point at my company website?**
Yes. Everything fetched is treated as data, never as instructions, and a
figure found on your own website is **not** treated as evidence until a human
clears it — which is how stale claims get republished with fresh timestamps.
See [`references/untrusted-content.md`](references/untrusted-content.md).

## What this project does not claim

- **It does not beat AI detectors.** No edit reliably does, detector scores
  move between model generations, and claiming otherwise would be dishonest.
  What these rules do is make copy specific, attributable and checkable, which
  is what a reader responds to.
- **It does not promise reach.** Every benchmark in the references measures
  someone else's corpus, most of it vendor data with a proprietary score
  behind it. Your own trailing baseline beats all of them.
- **It does not attribute revenue to posts.** A company page cannot show which
  post produced a deal, and `page-performance-report` says so in every report
  rather than modelling what the data will not support.
- **It does not automate LinkedIn articles or newsletters.** Nothing can.

## Contributing

Issues and pull requests welcome — particularly reference-file corrections
when LinkedIn changes a limit or a gate, and banned-vocabulary lists for
languages other than English. See [CONTRIBUTING.md](CONTRIBUTING.md).

Before opening a PR:

```bash
python -m scripts.selftest
python -m tests.test_instruction_integrity
python -m scripts.check_markdown_references
```

## Credits

Structure and conventions follow the pattern established by
[sergebulaev/linkedin-skills](https://github.com/sergebulaev/linkedin-skills)
(MIT) for personal-profile LinkedIn work: single-purpose skills, a shared
reference layer with an explicit precedence order, an untrusted-content rule,
and draft → approval → publish throughout.

The formats, voice rules, claim gating, distribution model and surface
handling in this repository are built for company pages, which behave
differently.

Built by [Dnyanesh Chandewar](https://github.com/chandewardnyanesh).

## Licence

[MIT](LICENSE).

---

<sub>Keywords: LinkedIn company page, LinkedIn business page, Claude skills,
Claude Code plugin, LinkedIn content strategy, B2B LinkedIn marketing,
LinkedIn employee advocacy, LinkedIn newsletter, LinkedIn document carousel,
thought leadership, brand voice, AI content humanizer, LinkedIn analytics,
company page SEO.</sub>
