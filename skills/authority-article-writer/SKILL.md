---
name: authority-article-writer
description: "Write long-form LinkedIn Articles and Newsletter issues published as a company Page — original data reports, category arguments, buyer's guides, process manuals, teardowns and post-mortems — using eight authority architectures. Use when the user wants an article, newsletter, whitepaper, thought leadership piece, long-form content, 'something more substantial than a post', or asks how to start a LinkedIn newsletter for their company. This is the authority-building core of the bundle: the asset that posts point at and employees reshare. Also checks newsletter eligibility. Not for short feed posts (use page-post-writer)."
---

# Authority Article Writer

Write the asset. Everything else in this bundle points at it.

## Why articles, when articles get less engagement than posts

They do, and it is mostly irrelevant, because an article is not competing for
feed engagement. It is doing four jobs a post cannot
(`../../references/article-architectures.md` §Why articles):

1. **It is the thing everything points at.** A data-drop post is content for a
   day; the article behind it works for a year. The post is the trailer.
2. **It carries the newsletter** — and a newsletter notifies subscribers by
   **email**, which makes it the only Page surface whose delivery does not
   depend on the ranker. Given that Page posts reach roughly 1-2% of followers
   (`../../references/page-algorithm-heuristics.md`), this is the single most
   defensible channel a Page can own.
3. **It is a public, indexed URL.** For a business whose buyers search before
   they ask, this is work happening in a channel Page analytics never shows.
4. **It is sponsorable**, via Sponsored Articles or a Thought Leader Ad on an
   article post.

So judge an article by whether it is the best thing on the internet about one
narrow question. Not by its reaction count.

## When to use

- "Write an article / newsletter / whitepaper / thought leadership piece"
- "Something more substantial than a post"
- "How do we start a LinkedIn newsletter?"
- The heavy asset in a `page-content-calendar` month
- A `trend-radar` opportunity that needs more than 3,000 characters

## Steps

### 0. Profile and proof, before structure

Read `../../references/company-profile.md` (§5 voice, §6 customer language, §7
pillars, §10 limits) and `../../references/proof-library.md`.

**The bar is higher here than for a post.** An article is linkable, quotable
and screenshot-able for years. A wrong figure in a post is embarrassing; a
wrong figure in an article becomes a citation. Every claim needs a cleared row,
and claims that are `pending` either get cleared before publication or come out
of the draft.

### 1. Pick the architecture by what the company actually has

Eight structures in `../../references/article-architectures.md`. The common
failure is choosing a structure the company cannot fill, then filling it with
assertion.

| Architecture | Needs | Half-life |
|---|---|---|
| **A1 Reference** | Deep operational knowledge of a narrow question | Years |
| **A2 Data Report** | Proprietary data — the strongest asset a Page can own | A year, and citable |
| **A3 Category Argument** | A real position, held publicly | As long as it holds |
| **A4 Teardown** | Judgement and a specific artefact | Months |
| **A5 Post-mortem** | An incident, and the nerve to publish it | Permanent trust |
| **A6 Buyer's Guide** | Honesty about where you lose | A year |
| **A7 Process Manual** | A process that genuinely exists | Years |
| **A8 Newsletter Issue** | A cadence the business can hold | A week, compounding |

Ask the diagnostic question for the architecture before drafting:

- **A2:** what is n, over what date range, and what can the data not tell you?
- **A3:** can you state the prevailing view so fairly that its believers
  recognise it?
- **A6:** is there a paragraph that sends a reader to a competitor? Without
  one, nobody believes the rest.
- **A7 / A1:** could a competent reader do this without hiring you? If not, it
  is a brochure.

If the answer is no, the architecture is wrong, not the question.

### 2. Outline first, and show it

Draft the structure with one line per section and the evidence each section
needs. **Show the outline before writing the body.** Two thousand words in the
wrong shape is an expensive thing to discover at the end, and the outline is
where a subject-matter expert can correct you cheaply.

Build in stages after approval: outline → section by section → full pass.

### 3. Draft

- **Target 1,200-2,500 words** (~7,000-15,000 characters). Below 1,200 it
  should have been a post. Above 2,500 make it a series — completion rate falls
  away and an unfinished article converts nobody.
- **Headline: 100 characters**, declarative, with a number or a named thing in
  it. No question headlines, same reason as post hooks. Check with
  `python -m scripts.fit --surface article_title --text "..."`.
- **Subheads every 200-300 words.** Most readers scan subheads first and decide
  from them whether to read anything, so the subheads have to carry the
  argument on their own.
- **Use the rich text.** Unlike posts, articles support headers, bold, lists,
  blockquotes, images and clickable in-body links. An article is the one
  surface where an external link costs nothing.
- **Attribution over the corporate "we"** — an article can carry a named author
  inside the Page's voice: "Priya, who ran this migration, found…"
  (`../../references/brand-voice-rules.md`).
- **State method and limits early** in a data report, before anyone asks. A
  report that hides its sample size is read as marketing by exactly the people
  it was written to convince.
- **Cover image**: brief it. An article without one looks broken in the feed.

### 4. Newsletter handling

If the request is a newsletter issue, or the user asks about starting one,
check eligibility against `../../references/page-surfaces.md`:

- Super Admin on the Page
- At least 150 followers
- An active Page with recent posts
- A history of original content on LinkedIn, ideally within the past 30 days

**If they qualify and have no newsletter, say so prominently.** It is the most
defensible channel available to a Page and a qualifying Page without one is
leaving it unused. If they do not qualify, say exactly what is missing.

Then settle cadence honestly against `company-profile.md` §9: **monthly held
for two years beats weekly abandoned after six issues.** Pick the frequency the
business can hold in its worst month and record it.

Issue shape (A8): one idea, 800-1,500 words, open with the specific thing that
prompted it this week, one thing the reader can do differently, and a
consistent closing section — recognisable structure is what turns a newsletter
into a habit.

### 5. Plan the promotion before you finish the draft

An article nobody links to is a file. Produce alongside it:

- **The Page post that promotes it** — not a summary with a link. A P4 or P7
  post that stands alone and happens to point at the article
  (`page-post-writer`). Schedule it 3-7 days apart from the carousel.
- **The document carousel version** — the article's spine as 5-12 slides. The
  strongest organic format on the platform.
- **The amplification angles** — one line each for 3-6 people
  (`../../references/amplification-mechanics.md`).
- **The Featured slot** — articles and newsletters belong in the Page's
  Featured section (`page-optimizer`).

### 6. Approval, and the honest publishing answer

Approval card with the full draft, the headline options, the claims and their
sources, and the promotion plan.

Then state the publishing reality plainly: **there is no API for Articles for
Pages or for Newsletters.** Every tool that claims to automate a LinkedIn
article is driving a browser or is wrong. So the deliverable is a clean draft
plus the UI path:

> Page admin view (Super or Content) → **Write article** → paste headline and
> body → add cover image → publish.
> For a first newsletter: start the article, then **Manage → Create
> newsletter**.

This is the complete and correct answer. Do not apologise for it and do not
imply a key or connector would change it (`../../references/page-surfaces.md`).

## Hard rules

- **Every claim cleared, not pending.** The article outlives the quarter.
- **State n and the limits** in anything data-based, unprompted.
- **One article, one job.** Educating, differentiating and converting at once
  achieves none of them.
- **No named competitor**, including in a teardown. Tear down artefacts,
  standards and practices (`../../references/claims-and-compliance.md` §3).
- **A post-mortem needs sign-off.** An incident disclosure can carry
  contractual consequences; `claims-and-compliance.md` §1 names the approver.
- **Third-party research is cited with source and date**, never restated as
  your own finding.
- **Outline approved before body drafted.** Non-negotiable at this length.
- **Never promise a cadence the business cannot hold.** An abandoned newsletter
  is worse than none: it is a dated public record of giving up.

## Anti-patterns

- A 900-word "article" that should have been a post.
- An article that is the blog post with the same title, published again. If it
  is genuinely the same piece, use `page-repurposer` and say that is what it is.
- A buyer's guide where your option wins every row. Readers price it as an ad,
  correctly.
- A data report with no sample size.
- A category argument that misrepresents the view it is arguing against. It
  only persuades people who already agreed.
- Listicles ("7 ways to…") with no evidence under any of the seven.
- A newsletter that is a roundup of links. One idea per issue.
- Gating the article behind a form. It is the public, indexed asset; gate the
  deeper thing it leads to.

## Resources

- `../../references/article-architectures.md` — all eight structures, length and shape rules, repeating rules
- `../../references/page-surfaces.md` — article and newsletter limits, eligibility, why publishing is manual
- `../../references/proof-library.md` — claim clearance
- `../../references/brand-voice-rules.md` — voice and attribution
- `../../references/claims-and-compliance.md` — approval paths and regulated claims

## Related skills

- `page-post-writer` — the post that promotes this, and the carousel caption
- `page-repurposer` — turns the article into the carousel, the posts and the series
- `page-humanizer` — de-AI and de-corporate pass before publishing
- `employee-amplification` — the reshare angles
- `page-optimizer` — puts the finished asset in Featured
