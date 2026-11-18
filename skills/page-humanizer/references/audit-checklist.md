# Audit checklist and tier rationale

## The six gates, in order

Order matters: a voice pass on a draft whose central claim has no evidence is
wasted work, and a user who gets style notes on a post that cannot legally ship
has been failed.

### Gate 1 — Claims

Extract every assertion of fact from the draft, then resolve each against
`../../../references/proof-library.md`.

What counts as a claim, including the ones that get missed:

- Any number: results, counts, durations, percentages, prices, headcount, years
- Any customer, named or identifiable by description
- Any credential, certification, partner tier, registration or award
- Any superlative: leading, best, first, largest, only, fastest, most trusted
- Any comparative: faster than, cheaper than, unlike other
- Any statement about what the company has done, for whom, or how often
- **Implied claims.** "Our clients see results in weeks" is a performance
  claim with the number removed, and it needs the same evidence a number would.

Status per claim:

| Status | Meaning | Action |
|---|---|---|
| **cleared** | Current row, in date, matching wording | Pass |
| **pending** | Row exists, not cleared for public use | Blocker until cleared |
| **expired** | Past its Expires date | Blocker until re-verified. Not publishable with a caveat |
| **absent** | No row | **Blocker.** Remove, evidence, or change format |
| **drifted** | Row exists but the draft states it differently | Blocker. Use the cleared wording verbatim |

**Drift is the one most often waved through.** A cleared row saying "46
migrations since 2019" becomes "nearly 50 migrations" in a draft because it
reads better. That is a new, unevidenced claim.

### Gate 2 — Compliance

Against `../../../references/claims-and-compliance.md`:

- [ ] Named competitor anywhere? → blocker, default position is no
- [ ] Superlative without held substantiation? → blocker
- [ ] Regulated category touched (§4)? → apply that rule, name the approver
- [ ] Confidential client, unreleased work, NDA material? → blocker
- [ ] A subject §6 says the Page stays out of? → blocker
- [ ] Forward-looking statement presented as fact? → relabel as intention
- [ ] Price stated — does it match what sales is quoting this week?
- [ ] Employee named or photographed with consent on file (§7)?
- [ ] Second approver required for this content type (§1)? → name it and the
      expected turnaround

### Gate 3 — Surface fit

Run it, do not estimate it:

```bash
python -m scripts.fit --surface page_post --file draft.md
python -m scripts.fit --surface about --text "..."
```

- [ ] Within the hard limit (over = silently truncated in public)
- [ ] Hook complete and paying off inside 210 desktop / 140 mobile
- [ ] Document post: 5-12 pages, under 10 MB, PDF, link in caption not in PDF
- [ ] Article: headline within 100 characters, subheads every 200-300 words
- [ ] Poll question within 140 characters

### Gate 4 — Voice

- [ ] Banned-word density: max one per 300 characters,
      **zero in the first 210** (`../../../references/brand-voice-rules.md`)
- [ ] Em dashes: about one per 100 words maximum
- [ ] No emoji used as bullets
- [ ] Hashtags: 0-2, at the end
- [ ] One contrast, one triple maximum
- [ ] At most two standalone fragments
- [ ] **Competitor-swap test** on the first three lines: would they survive a
      competitor's name? → press-release voice
- [ ] **Industry-swap test** on the first three lines: would they survive a
      different industry? → AI voice
- [ ] A named person, a specific number, or a dated event present in the
      opening three lines
- [ ] §5 rules observed: banned words, emoji policy, spelling convention

### Gate 5 — Platform rules

- [ ] First line is not a question
- [ ] No comment-gating ("comment X and we'll send Y")
- [ ] No external link in the body
- [ ] No all-caps opening line
- [ ] No recycled engagement-bait closer
- [ ] LinkedIn not framed as inferior
- [ ] Not an anti-format (`../../../references/page-formats.md` §Anti-formats)

### Gate 6 — Job and distribution

- [ ] Which job is this doing (`page-formats.md` §Pick by job)?
- [ ] Is there an amplification plan — 3-6 named people, distinct angles?
- [ ] Is this the post worth the week's single Notify-employees slot?
- [ ] Does the KPI exist, and is it something other than impressions?

A draft that passes gates 1-5 and fails gate 6 is clean copy that will reach
almost nobody. Say so; it is a more useful finding than an approval.

## Tier rationale

### T1 — Surface

The copy is structurally sound and reads stiff. Swap banned vocabulary for
facts, cap the em dashes, remove emoji bullets, cut dead bridges, trim
hashtags. Fifteen minutes, meaning unchanged.

### T2 — Structural

The hook fails, the question is in the wrong place, the paragraphs are
sequenced for the writer rather than the reader, or triads are stacked. Rebuild
the shape; keep the content. The commonest T2 is a draft whose third paragraph
is the actual hook.

### T3 — Substantive

Every sentence survives the competitor swap. There is nothing specific in the
copy, so there is nothing to rewrite *toward*.

**This is where an agent fails badly if it tries to be helpful.** Thin copy
cannot be edited into specific copy; a fact has to arrive from outside. The
correct moves, in order:

1. Name the missing fact and ask for it. "This needs one number. What was the
   before-state?"
2. If no fact is available, propose a format that needs none — several in
   `page-formats.md` run on process or position rather than on figures.
3. If neither, say the post should not ship, and why.

Inventing the fact is the one unacceptable option
(`../../../references/precedence.md` rule 2).

## Worked diagnoses

**Draft:** "We are excited to announce our new partnership with a leading
technology provider. This collaboration will enable us to deliver even more
value to our clients through cutting-edge innovation."

- Gate 1: "leading technology provider" is an unsubstantiated superlative about
  a third party. "More value" is an implied claim with no number. Both absent.
- Gate 4: survives both swap tests entirely. Four banned terms in 230
  characters.
- Gate 6: no job. It is an anti-format announcement.
- **Verdict: do not ship. T3.** The post needs the partner's name (cleared),
  what the partnership actually lets a client do, and when. Without those it is
  an announcement that the company has news.

---

**Draft:** "Rahul rewrote our deployment script three times last month. The
third version is the one that stopped the 2am alerts. Here's what the first two
got wrong — and why we almost shipped version two."

- Gate 1: no figures beyond "three times" and "last month", both internally
  verifiable. Rahul needs §7 consent.
- Gate 4: passes both swaps. Named person, dated, specific. One em dash, within
  cap.
- Gate 5: "Here's what" appears mid-sentence rather than as the opener, which
  is acceptable, though "what the first two got wrong" is tighter.
- Gate 6: job is P2 Build Log, trust and talent. Needs an amplification plan.
- **Verdict: ship after confirming Rahul's consent and naming amplifiers. T1
  at most.**

---

**Draft (tagline):** "Empowering businesses to achieve digital excellence
through innovative solutions."

- Gate 3: 76 characters, within 120.
- Gate 4: four banned terms in nine words. Survives both swap tests.
- **Verdict: T3.** Not a rewrite. The business has to say what it does and for
  whom (`../../page-optimizer/references/page-copy-templates.md` §T1).
