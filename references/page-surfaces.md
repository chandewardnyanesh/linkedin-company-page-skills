# Page surface inventory

Every place a company Page can put words, what it costs to fill, what gates it,
and whether anything can publish it for you. Limits observed in 2026; LinkedIn
moves them without notice.

**Check a draft with code, not by eye:**
`python -m scripts.fit --surface <name> --file draft.md`, or `--list` for the
whole table. Counting characters by hand is the most reliable way to ship a
truncated tagline.

## Static surfaces — the credibility check

These are filled once and revisited quarterly. Given the reach economics in
`page-algorithm-heuristics.md`, **this group is worth more than the feed**: it
is what a buyer reads after a founder's post, an ad or a cold email. A Page
posting four times a week with a 2019 About section has its priorities
inverted.

| Surface | `--surface` | Limit | Notes |
|---|---|---|---|
| Page name | `page_name` | 100 | Appears on every post from the Page |
| Tagline | `tagline` | 120 | Under the logo, and beside the Page in search and follow prompts. No fold — it fits or it is cut |
| About / description | `about` | **2,000** | Not the 2,600 a personal profile gets. First ~300 characters carry the pitch; the rest sits behind the section's own "see more" |
| Specialties / keywords | — | up to 20 entries | Feeds Page search. The closest thing a Page has to SEO |
| Custom button | — | fixed label set | Visit website / Contact us / Learn more / Register / Sign up. Its clicks are a reported metric, which makes it the cheapest conversion signal on the Page |
| Location(s) | — | — | Affects local search surfacing |
| Products tab | — | — | Each product gets its own page, with its own followers |
| Services | — | 10 services | Surfaces the Page in service-based search |
| Featured | — | — | Pins posts, newsletters, links. Where the newsletter and the best P4 go |
| Life tab | — | — | Employer brand. Only worth filling when actively hiring |
| Career pages | — | paid add-on | Separate metrics under Employer Brand |
| Showcase pages | — | — | A sub-Page for a product line or audience. Splits followers; only worth it with a genuinely separate audience |

LinkedIn reports that complete Pages generate around 30% more page views per
week than incomplete ones, and completeness also unlocks features like content
suggestions. Treat Page completion as prerequisite work, not optimisation.

## Feed surfaces — the borrowed-reach layer

| Surface | `--surface` | Limit | Notes |
|---|---|---|---|
| Page post | `page_post` | 3,000 | Fold at ~210 desktop, ~140 mobile. Default range 900-1,300 when nobody has asked for a length |
| Document post (PDF carousel) | — | see below | Strongest organic format |
| Poll | `poll_question` | 140 | Options are short; the value is the follow-up post |
| Comment as the Page | `comment` | 1,250 | Switch identity in the comment box. 200-400 is the working range |
| Multi-image post | — | 2-20 images | LinkedIn deprecated the native carousel creator, so this is not a carousel |
| Video | — | — | Native upload only; a YouTube link is an external link and is deprioritised |

### Document post specs

The one format where the numbers matter as much as the writing.

- **Accepted:** PDF, PPTX, DOC, DOCX. **Max:** 100 MB, 300 pages.
- **Practical:** under 10 MB so it renders fast; **5-12 pages** is the retention
  sweet spot, with measurable drop-off past 20.
- **Caption:** 100-200 words (`page_post` surface, same fold rules).
- **Link goes in the caption.** A link inside the PDF is not tappable.
- **Slide 1 carries the hook**, because a large share of viewers see only it.
- **Document title** is a separate field and shows as the carousel's label in
  the feed. It is not the file name; set it deliberately.

## Owned-distribution surfaces — the only reach the feed cannot throttle

| Surface | `--surface` | Limit | Gate |
|---|---|---|---|
| Article (Articles for Pages) | `article_title` / `article_body` | 100 / ~110,000 | Super or Content admin view → "Write article" |
| Newsletter | `newsletter_title` | 100 | See below |
| Event | — | — | Page admin view → Events |

### Newsletter eligibility

A Page newsletter needs all of:

- **Super Admin** permission on the Page,
- **at least 150 followers**,
- an **active Page with recent posts**, and
- a **history of original content on LinkedIn**, ideally within the past 30 days.

Once launched, subscribers are **notified by email** for each issue. This is
the reason the newsletter matters strategically: it is the only Page surface
whose delivery does not depend on the ranker. A Page that qualifies and has not
started one is leaving its single most defensible channel unused.

Mechanically: start an article as the Page, then **Manage → Create newsletter**
for the first issue. Add the newsletter to Featured once it exists.

## What can be published by an API, and what cannot

This distinction is the platform's, not this bundle's, and a skill should state
it plainly rather than imply that configuration would fix it.

**An API could reach these**, given the `w_organization_social` scope, an
eligible admin role, and the organization URN as the post author
(`urn:li:organization:{id}` — see `lib/url_parser.py`, which refuses to
convert a vanity slug into a URN rather than guess):

- Page posts, document posts, comments as the Page.

**Nothing can reach these. There is no publishing API:**

- **Articles for Pages** — manual for everyone.
- **Newsletters** — an extension of articles, so no API either.
- **Polls, Events**, and every static Page field (tagline, About, specialties,
  tabs, Featured, Life).

So for articles and newsletters, "here is the draft, paste it into the editor"
is the complete and correct answer. Do not apologise for it, and do not suggest
a key or a connector would change it.

This bundle ships draft-only on every surface by default. `lib.publish()`
returns a paste block plus the exact UI path. To automate the API-reachable
surfaces, export `LINKEDIN_PAGE_CUSTOM_POSTER` in a trusted shell before
starting the agent; the variable is deliberately ignored inside `.env` files,
because a file on disk choosing which executable runs is a code-execution hole
dressed as configuration.

## Paid surfaces, in one paragraph

Not this bundle's job, but the planning skills need to know they exist.
**Thought Leader Ads** sponsor an employee's or founder's organic personal post
rather than a Page post, which is how a brand buys its way around the Page
reach problem — see `amplification-mechanics.md` for the mechanics, the
eligibility rules and an honest reading of the benchmark claims.
**Document Ads** and **Sponsored Articles** promote the Page's own long-form
assets. A reported figure worth knowing when choosing where a gated asset
lives: native lead-gen forms convert far better than sending traffic to a
landing page (one 2026 benchmark across 1,240 campaigns put it at 11.9% versus
3.0%).

See also: `page-formats.md`, `article-architectures.md`, `metrics-taxonomy.md`.
