---
name: page-optimizer
description: "Audit and rewrite a LinkedIn company Page end-to-end for 2026: tagline, About section, specialties and keywords, custom button, Products and Services tabs, Featured, cover image, Life tab and Page completeness. Use when the user says 'review our company page', 'rewrite our About section', 'fix our tagline', 'our page looks dead', 'optimise our LinkedIn page', 'page audit', or asks why their Page gets no followers or traffic. Also use before any content push, because the Page is the credibility check a buyer runs after seeing a post. Not for writing feed posts (use page-post-writer)."
---

# Page Optimizer

Fix the Page itself. This is static-asset work, and on a company Page it is
worth more than the feed.

## Why this outranks posting

A company Page reaches roughly 1-2% of its followers organically
(`../../references/page-algorithm-heuristics.md`). The Page's *fields*, by
contrast, are read by every buyer who met the founder, clicked an ad, got a
cold email, or saw an employee's post and wanted to know whether the company is
real. That audience is small, late-funnel, and the most valuable traffic the
account gets.

The common inversion is a Page posting four times a week with a tagline written
when the company did something else. Fix the asset, then feed it. LinkedIn also
reports that complete Pages draw around 30% more weekly page views and unlock
features like content suggestions, so completeness is prerequisite work rather
than polish.

## When to use

- "Review / audit / optimise our company page"
- "Rewrite our About section" or "fix our tagline"
- The Page gets views but no follows, or follows but no enquiries
- Before a content push, a launch, a funding announcement or a hiring drive
- Positioning changed and the Page has not caught up

## Steps

### 1. Load the profile

Read `../../references/company-profile.md`. If it is not `filled: yes`, run
`page-profile-builder` first — rewriting a Page without knowing the positioning
produces fluent copy that says the wrong thing, which is harder to spot than
bad copy.

Also read `../../references/competitor-set.md` §5 if filled, so the new tagline
does not echo a phrase four competitors already use.

### 2. Capture the current state

Fetch the Page. Record every field verbatim before changing anything, and
character-count each one with
`python -m scripts.fit --surface <name> --text "..."`. Truncation is invisible
in the admin editor and obvious in public.

If the Page is not publicly fetchable, ask for the text of each field. Do not
audit from memory of what such Pages usually say.

### 3. Audit against the inventory

Work through `../../references/page-surfaces.md` §Static surfaces. For each
field record: present or missing, over or under its limit, and — the question
that matters — **would this survive having a competitor's name substituted into
it?** A sentence that survives the swap is saying nothing.

Score the Page on the four jobs it actually does
(`../../references/page-algorithm-heuristics.md` §What follows from that):
credibility check, asset library, owned distribution, conversion. Most Pages
score on none of them, and naming which one is weakest sets the priority order
for everything below.

### 4. Rewrite, field by field

Templates and worked examples: `references/page-copy-templates.md`.

Priority order, because attention is finite:

1. **Tagline (120 chars).** The highest-leverage string on the Page. It appears
   beside the Page in search and in follow prompts, and it has no fold — it fits
   or it is cut. Specific over clever: what you do, for whom.
2. **About (2,000 chars).** Note the limit: a Page gets 2,000, not the 2,600 a
   personal profile gets, so templates written for a personal About overflow.
   The first ~300 characters carry the whole pitch. Structure in the templates
   file.
3. **Specialties / keywords (up to 20).** The closest thing a Page has to SEO.
   Use the customer's words from `company-profile.md` §6, not internal names
   for things.
4. **Custom button.** Pick the one whose clicks you will actually read as a
   signal. Its click count is a reported metric and one of very few unambiguous
   intent signals a Page produces (`../../references/metrics-taxonomy.md`).
5. **Services (up to 10)** and **Products.** Both surface the Page in search.
   Products get their own followers.
6. **Featured.** Where the newsletter and the best heavy asset go. An empty
   Featured section on a Page with good assets is a wasted shelf.
7. **Cover image.** Brief it; do not describe it as done. Say what it must
   communicate and what text must be legible at mobile size.
8. **Life tab.** Only when actively hiring. Half-filled, it reads worse than
   absent.

Draft **two or three options for the tagline and the About opener**, with the
trade-off of each stated in a line. These are the two fields people argue
about, and a single option invites a rewrite rather than a decision.

### 5. Flag the newsletter question

If the Page has no newsletter, check eligibility against
`../../references/page-surfaces.md` §Newsletter eligibility — Super Admin, 150+
followers, active posting, recent original content.

If they qualify and have not started one, say so prominently. It is the only
Page surface whose delivery does not depend on the ranker, and a qualifying
Page without one is leaving its most defensible channel unused. If they do not
qualify yet, say what is missing and what it would take.

### 6. Approval card

Use `lib.render_approval_card()` per field group, or one card listing every
field with its before, after and character count. Every field is manual to
apply — no API touches Page fields — so the deliverable is clean paste-ready
text plus the admin path: **Page admin view → Edit page**.

## Hard rules

- **Count characters with the tool.** `about` is 2,000 on a Page. Getting this
  wrong silently drops the last paragraph, which is usually the CTA.
- **No superlatives without substantiation.** "Leading", "best", "number one"
  are advertising claims and need evidence held before publication
  (`../../references/claims-and-compliance.md` §3). On a Page field, which sits
  up permanently, this matters more than in a post.
- **No credential stated without a current entry** in
  `../../references/proof-library.md` §6, in the issuer's exact permitted
  wording. Lapsed certifications on About sections are extremely common.
- **Never name a competitor** in a Page field.
- **The first 300 characters of About are the whole pitch.** Write them to be
  read alone. Company history belongs below the fold, if anywhere.
- **Show before and after together.** A rewrite presented without the original
  cannot be judged, and the owner needs to see what they are giving up.

## Anti-patterns

- An About section that opens with the founding year. Nobody who clicked is
  asking when you started.
- "We are a leading provider of end-to-end solutions" in any form. Survives the
  competitor-name swap, therefore says nothing.
- Keyword stuffing the About. It reads as desperate and the search benefit sits
  in Specialties anyway.
- A tagline that is the company's internal mission statement.
- Filling the Life tab when not hiring.
- Recommending a Showcase page without a genuinely separate audience. It splits
  followers across two Pages that both then underperform.
- Rewriting everything at once for a Page whose real problem is that it has no
  assets worth featuring. Say that instead.

## Resources

- `references/page-copy-templates.md` — tagline formulas, About structures, worked rewrites
- `../../references/page-surfaces.md` — every field, its limit, what gates it
- `../../references/brand-voice-rules.md` — banned vocabulary, the attribution rule
- `../../references/claims-and-compliance.md` — superlatives and credentials
- `../../references/page-algorithm-heuristics.md` — why static beats feed here

## Related skills

- `page-profile-builder` — run first if the profile is empty
- `competitor-page-analyzer` — which positioning words are already taken
- `authority-article-writer` — makes the assets that fill Featured
- `page-performance-report` — whether the rewrite moved button clicks and visitors
