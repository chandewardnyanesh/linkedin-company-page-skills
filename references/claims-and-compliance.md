# Claims and compliance

What this business may assert in public, who decides, and the categories where
a sentence that reads as ordinary marketing is a regulated statement.

This file is the gate that `page-humanizer --mode audit` checks a draft
against. It is not legal advice and this bundle does not provide any — it is a
record of decisions the business has already made, so that a draft does not
quietly re-litigate them at 9pm before a post goes out.

> Filled, this is a confidential document. Same handling as the other
> templates: gitignore it or keep the filled copy outside the repo.

## Status

- filled: no
- source: template
- reviewed by: --
- updated: --

---

## 1. Who approves what

The most useful section in the file, because an unclear approval path is why
posts sit in drafts for three weeks or go out unchecked.

| Content type | Drafter | Approver | Second approver needed when |
|---|---|---|---|
| Routine Page post |  |  |  |
| Post naming a customer |  |  |  |
| Post with a performance figure |  |  |  |
| Article / newsletter |  |  |  |
| Incident or post-mortem |  |  |  |
| Hiring post |  |  |  |
| Comment replying to a complaint |  |  |  |
| Anything touching a regulated claim |  |  |  |

**Turnaround expected:** ___ . A plan that assumes same-day approval when the
real path is four days produces a calendar nobody can hold.

## 2. Claim types and their requirements

Default positions, to be overridden per business.

| Claim type | Requirement |
|---|---|
| Performance / outcome figure | Entry in `proof-library.md` §1, dated, with a measured baseline |
| Aggregate or scale figure | `proof-library.md` §2, re-verified within the quarter |
| Named customer | `proof-library.md` §4, written permission, correct permitted form |
| Quote | `proof-library.md` §5, written approval, verbatim |
| Credential or partner status | `proof-library.md` §6, in-date, **exact permitted wording** |
| Comparative claim vs a competitor | See §3 — default is no |
| Superlative ("leading", "best", "largest") | Substantiation or do not say it. See §3 |
| Forward-looking statement | Flag as intention, never as fact |
| Price or fee | Must match what sales is quoting this week |
| Third-party research | Cited with source and date; never restated as your own finding |
| Employee photograph or name | `proof-library.md` §7 consent |

## 3. Comparative and superlative claims

Two categories that cause most of the real trouble, so the defaults here are
restrictive.

**Naming a competitor: default no.** A Page that tears down a named competitor
converts a credibility post into a legal and reputational liability, and it
reads as insecurity to the buyer you were trying to impress. `page-formats.md`
P3 and `article-architectures.md` A4 therefore tear down *artefacts and
practices* — a pricing model, an RFP template, a widely-shared claim — never a
company. Describing a *category* of alternative ("the in-house build route",
"the big-four approach") is fine and is usually more useful anyway.

**Superlatives need substantiation that survives a challenge.** "Leading",
"best", "number one", "fastest", "largest", "most trusted" are advertising
claims in most jurisdictions, and India's CCPA guidelines on misleading
advertisements, the UK's CAP Code and the US FTC's substantiation standard all
expect evidence held *before* publication. If the business cannot produce a
cited, dated, independent source, the honest version is a specific fact
instead: "the only firm in Nagpur doing X" needs evidence; "we have run 46 of
these migrations since 2019" needs a row in the proof library.

Record the ones this business has cleared:

| Superlative | Substantiation held | Dated | Cleared by |
|---|---|---|---|
|  |  |  |  |

## 4. Regulated categories

Tick what applies and record the rule, because these are the cases where
ordinary-sounding marketing copy is a regulated statement.

- [ ] **Financial services / investment** — performance figures, return
  expectations, risk disclosures, licensing disclosure. Rule: ___
- [ ] **Real estate** — in India, RERA registration numbers are required in
  advertising, and claims about possession dates, approvals and amenities are
  constrained. Rule: ___
- [ ] **Health / medical / wellness** — efficacy and outcome claims. Rule: ___
- [ ] **Legal services** — jurisdiction-specific advertising restrictions,
  which in India are unusually tight. Rule: ___
- [ ] **Education** — placement, salary and outcome statistics. Rule: ___
- [ ] **Recruitment / employment** — non-discrimination in job content, salary
  transparency where mandated. Rule: ___
- [ ] **Data and AI** — accuracy, automation and security claims; what the
  system does versus what it is marketed as doing. Rule: ___
- [ ] **Government or public-sector contracting** — what may be disclosed
  about an engagement at all. Rule: ___
- [ ] **Other:** ___

## 5. Confidentiality

- Clients under NDA: (list, or point at where the list lives)
- Default assumption for a new client: (named / descriptive / silent)
- Unreleased work, products and partnerships: ___
- What may be said about an engagement before it is signed: ___
- Internal figures that are never public: ___

## 6. Subjects the Page stays out of

Positions the business has decided not to take publicly. Recording them stops
the question being reopened by whoever is drafting.

-
-

## 7. Incident and complaint handling

The case where the clock matters and improvisation is most expensive.

- Who is told first when a complaint appears in the comments: ___
- Response window the business commits to: ___
- What may be said publicly before the facts are established: ___
  (default: acknowledge, do not diagnose, move it to a channel)
- Who may approve a public post-mortem: ___
- Complaints that must never be handled in public: ___

Comment-level handling and escalation routes: `skills/page-engagement-desk/`.

## 8. Platform rules worth knowing

Not legal compliance, but they carry real cost.

- **Comment-gating** ("comment X and we'll send Y") is the named target of
  LinkedIn's March 2026 authenticity update. Do not use it.
- **Paid partnership disclosure** is required when a sponsored post's author is
  not an employee. Employee Thought Leader Ads need no label; an outside
  creator's post does (`amplification-mechanics.md`).
- **Generic AI-generated content is actively discounted**, and a reported "AI
  slop" report button cuts flagged posts' views substantially
  (`page-algorithm-heuristics.md`). This is a distribution risk attached to
  lazy copy, not a policy violation.
- **Engagement pods** are detected at high accuracy and the penalty is borne by
  the participants.

## 9. When a draft hits a limit

The resolution order, so a skill under pressure does not improvise one:

1. **The claim comes out.** A post without the number is still a post.
2. **Or the claim gets evidence** — someone produces it, and it goes into
   `proof-library.md` before the draft is approved, not after.
3. **Or the format changes.** `page-formats.md` has sixteen; several need no
   figure at all.
4. **Never soften and publish.** "Up to", "as much as", "helped clients
   achieve" around an unevidenced number is the same claim with deniability
   attached, and it reads as a weaker version of a thing you could not prove.

Full ordering: `precedence.md`.
