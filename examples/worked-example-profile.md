# Worked example: `page-profile-builder` output

What the research step produces, and — more importantly — **what it leaves
empty**. About half the fields below are blank. That is the skill working
correctly, not failing.

> **Meridian Systems is an invented company**, composed from the kind of
> material a real services website actually carries. Every figure here is
> illustrative. The point of the example is the *shape* of the output: which
> fields get filled from a website crawl, which cannot be, how inference is
> labelled, and how claims enter the proof library.
>
> A real filled profile is a confidential business document. See the handling
> note at the top of [`../references/company-profile.md`](../references/company-profile.md).

---

## Part 1 — `company-profile.md`, as the research fills it

### Status

- filled: partial
- source: website crawl (11 pages) + public LinkedIn Page, read 2026-11-19
- website crawled: yes — sitemap.xml, then case studies, services, pricing,
  about, 3 recent posts, careers, footer
- page audited: yes — tagline, About, last 14 posts
- updated: 2026-11-19

### 1. What the business actually does

- **One sentence:** Makes a company's existing systems agree with each other —
  typically an ERP, a CRM and a set of spreadsheets that each hold a different
  version of the same customer.
- **The work, concretely:** Two weeks of reading (the data, the process, and
  the places people have built workarounds), then the integration and
  reconciliation, documented, with handover training.
- **What they do not do, though people ask:** *(empty — ask. This single line
  prevents more bad drafts than any other field in the file.)*
- **Legal entity:** Meridian Systems Ltd
- **Founded:** 2019 *(About page; also in the footer, consistent)*
- **Headcount:** 14 *(careers page lists 14 team members by name)* — note the
  LinkedIn Page shows 22 employees, which is a **drift flag**, see Part 3
- **Markets:** UK and Ireland *(services page)*

### 2. Who it is for

- **Primary buyer:** `inferred:` operations or finance lead — the case studies
  are written to someone who owns a process, not to IT. Confirm the actual
  title.
- **Who else is in the room:** *(empty — ask)*
- **Company profile that fits best:** 100-500 people, manufacturing and
  distribution *(every case study sits in this band)*
- **Who is a bad fit:** `inferred:` companies wanting a platform licence; the
  services page says twice that they build with what you already own
- **The trigger:** `inferred:` a failed or stalled migration — two of five case
  studies open with one. Worth confirming, because it is the most useful
  single fact for `trend-radar`.

### 3. Offers and pricing posture

- **Offers:** integration audit (2 weeks, fixed fee) · integration build
  (project) · reconciliation and handover · ongoing support retainer
- **Entry point:** the integration audit
- **What is public about pricing:** nothing — no figures anywhere on the site
- **What is never stated publicly:** *(empty — ask, because a draft cannot
  mention cost at all until this is answered)*

### 4. Position

- **Category the market puts them in:** systems integration
- **The category they would rather be in:** `inferred:` the services copy
  pushes toward "data reconciliation" rather than "integration". Worth asking
  whether that is deliberate.
- **The honest trade-off of choosing them:** *(empty — ask. Every real position
  has one, and naming it is what makes the rest believable)*
- **The status quo they lose to:** `inferred:` an internal hire, or living with
  the spreadsheets. Usually the real competitor, and never on a competitor list.

### 5. Voice

- **Three words for the voice:** plain, specific, unhurried *(drawn from the
  blog, which is written in short declarative sentences with no adjectives)*
- **Three it must never be:** salesy, breathless, jargon-heavy
- **People who may be named:** *(empty — the careers page names 14 people, but
  naming someone in a post needs their consent, not a public page listing)*
- **Who signs off:** *(empty — ask)*
- **Regional spelling:** en-GB *(consistent across the site)*
- **Emoji:** none observed in 14 LinkedIn posts
- **Hashtags:** none observed

#### Signature samples

Three passages lifted verbatim from the blog and one proposal excerpt on the
site. The writing skills mirror the rhythm of these rather than a generic
brand voice:

- "The migration did not fail because of the software. It failed because
  nobody owned the part number."
- "We spent the first week reading. That is usually the week clients want to
  skip."
- "If your finance team is reconciling against yesterday's numbers, nightly
  sync is the problem, not the fix."

### 6. The customer's own words

Lifted verbatim from case-study quotes and the FAQ page. **Worth more than
everything above it**, and nobody can invent these:

- How they describe the problem: "the two systems don't talk", "we're
  double-entering everything", "nobody trusts the report"
- Their words for the category: "integration", occasionally "middleware" —
  never "data fabric"
- Objections, verbatim: "we tried this before and it broke", "our IT team says
  they can do it"
- What they say when it works: "we stopped checking it"

### 7. Content pillars

| Pillar | Standing | Evidence available | Primary audience |
|---|---|---|---|
| Why migrations fail | 5 case studies, 2 opening with a prior failure | strong | Economic buyer |
| The reconciliation nobody budgets for | Named in 4 of 5 case studies | strong | Technical evaluator |
| Build vs buy vs internal hire | Services copy takes a position | **partial** — no comparative data | Economic buyer |
| What two weeks of reading finds | The audit offer exists | **unverified** | Both |

### 8. Page facts

- Page URL: `linkedin.com/company/meridian-systems-example`
- **Page numeric id:** *(empty — must come from Page admin view. Deliberately
  not guessed: `lib.organization_urn()` refuses to derive one from a vanity
  slug, because a wrong id publishes somewhere nobody is watching.)*
- Follower count: 1,840 *(checked 2026-11-19)*
- Newsletter: none — **eligible**, see Part 3
- Website: meridiansystems.example
- Analytics access: unknown — ask

### 9. Cadence the business can actually hold

*(empty — and the field most worth getting right. Set it to the worst month,
not the best. The Page's own history shows 14 posts in 11 months, which is a
better guide than any stated intention.)*

---

## Part 2 — `proof-library.md`, as the research fills it

Every row **pending**. Nothing is cleared by research; only a human clears a
claim. The value of this table is that it converts "what does our website say"
into "which of these is still true" — a question someone can answer in ten
minutes.

| Claim | Evidence | Measured | Status |
|---|---|---|---|
| "cut invoice approval from 40 minutes to 6" | Case study 3 | undated | **pending** — is the 40 minutes measured or recalled? |
| "46 integrations since 2019" | Homepage counter | undated | **pending** — counters drift; confirm today's number |
| "most projects live in 8 weeks" | Services page | undated | **pending** — median, or best case? |
| Founded 2019 | About page + footer, consistent | — | **pending** (low risk) |
| 14 people | Careers page | 2026-11 | **pending — conflicts with the Page.** See Part 3 |
| Named customer: Rathi Industries | Case study 3, logo + name | — | **pending** — logo on a site is not permission for a LinkedIn results claim |
| "ISO 27001 certified" | Footer badge | no date shown | **pending — check validity.** Lapsed certifications on footers are common |

**Measured baselines found: one of five case studies.** That is the most
consequential finding in this table, because it decides how many P1 Proof
Ledger posts are available: one.

---

## Part 3 — the gap report

The deliverable the user actually acts on.

### What the research established

A clear offer, a genuinely distinctive voice with three usable samples, strong
customer vocabulary, and two pillars with real evidence behind them. Enough to
start writing. Not enough to publish a performance figure.

### Two things being claimed in public that need a decision

1. **Headcount disagrees across surfaces.** The careers page names 14 people;
   the LinkedIn Page shows 22 employees. Both are public, both are read by
   buyers, and a procurement check notices. Decide the accurate number and make
   every surface agree.
2. **The ISO 27001 badge carries no date.** For a business handling customer
   data this is the highest-risk claim on the site: it is material, it is
   checkable against the certification register, and a lapsed certification
   stated as current is a different category of problem from a stale statistic.
   Confirm validity and record the issuer's exact permitted wording.

Neither is a finding about the business. Both are findings about **what the
public record currently asserts** — which is what a proof library is for.

### The newsletter opportunity

The Page has 1,840 followers, posts regularly enough to count as active, and
has original content within the last 30 days. **It qualifies for a LinkedIn
newsletter and has not started one.** That is the only Page surface whose
delivery does not depend on the feed algorithm, and it is the single largest
unused asset in this account.

### The five questions worth asking, ranked

Each one changes what later drafts can say. Nothing else is asked.

1. **What do you refuse?** The "what we don't do" line.
2. **Is the 40-minutes baseline measured or remembered?** It decides whether
   the strongest format is available at all.
3. **What is your pricing posture?** Until this is answered no draft may
   mention cost.
4. **Who may be named in a post, and have they agreed?** Fourteen names on a
   careers page is not consent.
5. **What cadence survives a busy month?** The Page's own history suggests
   roughly one post a fortnight; plan to that, not to an intention.

---

## What this example demonstrates

1. **Gaps stay visible.** Roughly half the fields are empty, each with the
   question that would fill it.
2. **Inference is labelled.** `inferred:` marks every field where the research
   reasoned rather than read, because downstream skills treat this file as
   fact.
3. **Nothing is cleared.** Seven pending claims, zero cleared.
4. **The drift flags are the real output.** Two contradictions in the public
   record, found by reading eleven pages — the kind of thing nobody inside a
   business notices, because the careers page and the LinkedIn Page are
   maintained by different people in different years.
5. **The Page's own history beats stated intention.** 14 posts in 11 months is
   the honest capacity signal, whatever the plan says.
6. **Five questions, not thirty.**
