---
name: page-post-writer
description: "Draft a LinkedIn post to publish as a company Page, using the 16 brand post formats (proof ledger, build log, teardown, original data drop, honest no, category reframe, process reveal, document carousel caption, hiring with friction, post-mortem, comparison table, customer question and more) picked by the job the post has to do. Use when the user wants a post for their company page, business page, brand account or client's page, says 'write a post for our company', 'post this as the business', 'draft a LinkedIn update for us', or hands over a topic and a company. Runs the brand voice pass, checks every claim against the proof library, and produces an approval card with the amplification plan. Not for personal profile posts and not for long-form articles (use authority-article-writer)."
---

# Page Post Writer

Draft posts that a company can publish, that a buyer believes, and that
employees will carry.

## The constraint that shapes everything here

A Page cannot say "I". The reflex substitute is the corporate "we", which is
what makes Page posts unreadable, and no amount of hook craft fixes it.

What a Page has instead is **access a person does not have**: the aggregate
numbers, the thing that broke in production, the pattern across forty clients,
the real cost of the work. Every format in
`../../references/page-formats.md` is a way of spending that advantage, and the
fix for brand voice is always the same — a named person, a specific number, a
dated event in the first three lines (`../../references/brand-voice-rules.md`
§The attribution rule).

The second constraint: because the Page itself reaches so little, **a Page
post's real first audience is often the company's own employees**, who decide
whether to carry it to networks several times larger. Write for the employee
deciding whether resharing this makes them look sharp or makes them look like a
billboard.

## When to use

- "Write a post for our company page" / "post this as the business"
- Drafting for a client's brand account
- The user has a topic and a company and wants a Page post
- A calendar slot from `page-content-calendar` needs drafting

## Steps

### 0. Load the profile, and stop if the claim is not there

Read `../../references/company-profile.md`. If `filled: yes`, match §5 voice,
§6 customer vocabulary, §7 pillars, §10 hard limits. If it is not filled,
mention once that `page-profile-builder` would learn the business from its
website, then proceed on the generic rules in
`../../references/brand-voice-rules.md`.

Read `../../references/proof-library.md`. **Every figure, customer name,
credential and result in the draft must have an entry.** A format's `[specific
number]` slot is not a licence to produce a plausible number — plausible is
fabricated, and on a company Page a fabricated number is a representation the
business made in public with a timestamp on it.

When the library has nothing that fits: ask the user, or pick a format that
needs no figure. Several do. Do not soften an unevidenced claim into "up to" or
"helped clients achieve" — that is the same claim with deniability attached and
it reads weaker than the honest version (`../../references/precedence.md` rule 2).

### 1. Establish the job

Before anything else: **what is this post for?** Use the table in
`../../references/page-formats.md` §Pick by job.

| Job | Formats |
|---|---|
| Make a buyer believe you can do the work | P1, P4, P7, P13 |
| Make the Page worth following | P3, P4, P6, P12 |
| Earn substantive comments | P5, P6, P11, P13, P15 |
| Earn saves and reshares | P4, P7, P8, P13 |
| Attract talent | P9, P16 |
| Fill an event or launch | P14, P10 |
| Give employees something to reshare | P1, P2, P4, P8, P16 |

A post that is not doing one of these should not be written, however good the
angle is. If the user's request maps to none of them, say so and ask what the
post is meant to achieve — that question has saved more Page posts than any
rewrite.

### 2. Pick the format

Shortlist two or three from the job, narrow by what the evidence supports, and
let the user choose. Show each with what it needs: *"P1 Proof Ledger needs a
measured before-state — do you have one, or is the 40 minutes a recollection?"*

That question, asked at format-selection time, prevents the most common failure
in this skill, which is discovering mid-draft that the evidence does not exist
and filling the gap.

### 3. Draft

Fill the format skeleton with the business's own material. Non-negotiables from
`../../references/brand-voice-rules.md`:

- **Line one is a statement, a number or a named event. Never a question.** A
  question as the opening line measures as a material drag on reach. The
  question goes at the close, where it earns comments.
- **Hook inside 210 characters desktop, 140 mobile.** Verify with
  `python -m scripts.fit --surface page_post --file draft.md` rather than
  counting by eye.
- **Length: what the user asked for wins.** 900-1,300 characters is the default
  when nobody has said, never a ceiling over an explicit request. Hard limit
  3,000.
- **Name a person** where there is one to name, with their consent recorded in
  `../../references/proof-library.md` §7.
- **One contrast and one triple maximum.** No "The result?" or "Plot twist:"
  bridges.
- **Em dashes capped at about one per 100 words.**
- **One idea per paragraph, blank line between.** 1-2 sentence paragraphs.
- **Close with a specific question** — specific to this post, not "what are
  your thoughts?"
- **0-2 hashtags at the end. No link in the body** (first comment instead; for
  a document post, the caption, where it is tappable).

### 4. Brand voice pass

Run the draft against the two failure modes, which on a Page reinforce each
other:

- **Press-release voice:** would this sentence survive if you swapped in a
  competitor's name? If yes, it says nothing.
- **AI voice:** would this sentence survive if you swapped in a different
  industry? If yes, cut it.

Then check density: no more than one word from the banned list per 300
characters, and **zero in the first 210**. For a full pass, hand to
`page-humanizer`.

### 5. Document post? Switch jobs

If the post is a carousel caption (P8), the caption is setting up a swipe, not
substituting for it. 100-200 words, slide 1 carries the whole hook, link in the
caption. Specs in `../../references/page-surfaces.md` §Document post specs —
5-12 pages, under 10 MB, PDF.

Deliver a **slide-by-slide outline** alongside the caption, because the PDF is
the deliverable and the caption is its label.

### 6. Amplification plan

Every Page post needs one, or it publishes into a room with five people in it.
Name 3-6 people with a genuine stake, their rung, and **a distinct angle each**
— never one caption for everyone, because a dozen identical reshares is the
clone signal 360Brew discounts and it reduces the resharers' own reach.

Say whether this is the post worth spending the week's single
Notify-employees slot on. Detail: `../../references/amplification-mechanics.md`.

### 7. Approval card

```python
from lib import render_approval_card
print(render_approval_card(
    kind="Page post",
    draft=draft,
    page="<Page name>",
    surface="page_post",
    format_choice="P1 Proof Ledger",
    claims=[{"claim": "...", "source": "proof-library.md §1 row 3, cleared 2026-10-02"}],
    amplification=["Priya — rung 3, angle: the reconciliation nobody budgets for"],
    publish_window="Tue-Thu 09:00-10:30 IST",
    on_approval="Returned as a paste block with the admin path.",
))
```

Every claim carries its source. A draft with figures and an empty claims list
is the thing the reviewer most needs to notice, and the card says so.

If `../../references/claims-and-compliance.md` §1 requires a second approver
for this content type — a named customer, a performance figure, an incident —
say which approval is still outstanding. The person in the chat may not be the
person who carries it.

### 8. On approval

```python
from lib import publish
publish(kind="Page post", draft_text=approved, surface="page_post", page=page_name)
```

Returns a paste block plus the admin path. Page posts are API-reachable in
principle, so if a custom poster is configured it is used; otherwise pasting is
a supported way to work, not a degraded one, and it needs no apology.

## Hard rules

- **No figure without a proof row.** The single rule that matters most here.
- **Never name a competitor** (`../../references/claims-and-compliance.md` §3).
- **Never name a customer** without a cleared entry and the correct permitted
  form. Default to descriptive: "a 180-person auto components maker".
- **Never name an employee** without consent in §7. Consent does not survive
  their departure.
- **No superlatives** without held substantiation.
- **No comment-gating** ("comment X and we'll send Y") — the named target of
  LinkedIn's March 2026 authenticity update.
- **Never frame LinkedIn as inferior in a LinkedIn post.**
- **One product mention maximum**, and only where it is the natural conclusion
  rather than the purpose.
- **Include something that costs the company something to say** — a dead end, a
  limit, a case where they are the wrong choice. Pure-assertion Page posts do
  not land, and the admission is what makes the rest credible.

## Anti-patterns

The full list is `../../references/page-formats.md` §Anti-formats. The ones
this skill refuses outright:

- "We are thrilled / excited / proud to announce" in any form
- A question as the first line
- All-caps opening line
- Emoji used as bullets (🚀✅💡) — the most recognisable AI signature on the platform
- Inspirational quote over stock imagery
- Holiday or awareness-day posts with no business connection
- Rebroadcasting industry news with no position taken
- Follower-milestone and anniversary posts
- A post whose entire content is a link to the blog
- Hashtag stacking

## Resources

- `../../references/page-formats.md` — all 16 formats with skeletons, examples and failure modes
- `../../references/brand-voice-rules.md` — banned vocabulary, attribution, structural rules
- `../../references/proof-library.md` — what may be claimed
- `../../references/claims-and-compliance.md` — approval paths, superlatives, regulated categories
- `../../references/page-surfaces.md` — limits and document specs
- `../../references/amplification-mechanics.md` — rungs and the notify budget

## Related skills

- `page-humanizer` — full de-AI and de-corporate pass, plus `--mode audit` pre-publish
- `authority-article-writer` — when the subject deserves long form
- `page-repurposer` — when the source already exists elsewhere
- `employee-amplification` — builds the reshare kits this post's plan names
- `page-asset-extractor --mode pattern` — reverse-engineer a format from a post you admire
