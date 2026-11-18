# Brand voice rules for a company Page

Canonical voice reference. Every writing skill in this bundle reads it. Skill
specific rules (character ranges, threading, format constraints) are local;
everything else defers here.

## A Page has two voice problems, not one

A personal post can sound like AI. A Page post can sound like AI **and** like a
press release, and the two failure modes reinforce each other because they
share most of their tells: abstraction, hedging, the passive voice, the absent
narrator, and enthusiasm with nothing underneath it. This matters more than
style preference now that generic AI-written content is actively discounted
(`page-algorithm-heuristics.md`) — corporate Pages are the most likely thing in
the feed to trip that filter.

Diagnosing which one you have:

- **Press-release voice** says *who the company is* ("a leading provider of
  end-to-end solutions"). The giveaway is that the sentence would survive if
  you swapped in a competitor's name.
- **AI voice** says *what is generally true* ("In today's rapidly evolving
  landscape, data is the new currency"). The giveaway is that the sentence
  would survive if you swapped in a different industry.

Both are fixed the same way: put a named human, a specific number, and a dated
event into the first three lines. A sentence that could not have been written
by anyone else is, by construction, neither.

## The attribution rule

**This is the highest-leverage move in the whole bundle.** A Page cannot say
"I", and the reflex fix is the corporate "we", which is what makes Page posts
unreadable. The actual fix is to name a person and let them carry the first
person inside the Page's voice.

> Weak: "Our team worked tirelessly to improve deployment reliability."
>
> Strong: "Rahul rewrote our deploy script three times in a week. The third
> version is the one that stopped the 2am pages. Here is what the first two got
> wrong."

Rules for it:

- Name real people, with permission, and capitalise their names properly.
  Lowercasing a person's name reads as carelessness about the person.
- "We" is fine for a decision the company made ("we stopped taking projects
  under ten seats"). It is not fine as the subject of feelings ("we are
  thrilled", "we are passionate about").
- A customer's name is a claim, not a flourish. It needs an entry in
  `proof-library.md` and clearance under `claims-and-compliance.md`.
- If nobody can be named, use the artefact instead of the abstraction: "the
  migration runbook", "the Tuesday invoice", "the 40-page RFP". Concrete
  objects do the work a named person would have done.

## Banned vocabulary, by density

These are banned because they carry no information, not because they are
ugly. One of them in a 1,200-character post is a word choice; four is a tell.
The working threshold is **no more than one word from this list per 300
characters, and zero in the first 210**.

**Consultancy filler:** leverage, synergy, holistic, robust, seamless,
scalable (as an adjective with no number), best-in-class, world-class,
industry-leading, cutting-edge, state-of-the-art, end-to-end, turnkey,
bespoke, mission-critical, value-add, solutioning, ecosystem (unless literal).

**AI register:** fundamentally, delve, unlock, harness, streamline, foster,
navigate (figurative), landscape (figurative), realm, tapestry, testament,
pivotal, transformative, game-changer, deep dive, paradigm, underscore,
elevate, empower, meticulous, crucial, vital, intricate.

**Enthusiasm with nothing under it:** excited to announce, thrilled to share,
proud to announce, humbled to, honoured to, delighted to, passionate about,
committed to excellence, stay tuned, watch this space, exciting times ahead.

**Dead openers:** "In today's fast-paced world", "In an era where", "As we all
know", "Let's talk about", "Here's what / Here's how", "Stop X, start Y",
"It's not X, it's Y", "The future of X is Y".

**Dead bridges:** "The result?", "Plot twist:", "But here's the thing", "And
that's when it hit me", "The best part?".

**Dead closers:** "Reach out to learn more", "DM us to discuss", "What are your
thoughts?", "Tag someone who needs this", "Drop a comment below", "comment X
and we'll send you Y" (this last one is the named target of LinkedIn's March
2026 authenticity update, not merely tired).

Replacing one of these with a synonym is not a fix. "Utilise" for "leverage"
is the same empty slot with a different word in it. The fix is a fact.

## Structural rules

1. **Line one is a statement, a number, or a named event. Never a question.**
   A question as the opening line measures as a material drag on reach across
   every follower band (MagicPost, 1.2M posts, vendor data). Move the question
   to the close, where it earns comments.
2. **Hook inside 210 characters desktop, 140 mobile.** Verify with
   `python -m scripts.fit --surface page_post --file draft.md` rather than
   counting by eye. A hook whose payoff sits behind "...see more" has lost the
   readers who would have engaged.
3. **One contrast and one triple per post.** The contrast ("not X, but Y") and
   the rule of three are legitimate devices that human writers use constantly.
   The tell is repetition plus emptiness, not the device itself. One of each,
   both carrying a fact.
4. **Em dashes capped at about one per 100 words.** Replace the excess with a
   comma, colon or parentheses, never a full stop — breaking the sentence
   changes the rhythm, which is what the reader notices. No en dashes between
   clauses, no double hyphens.
5. **`..` is available as a soft mid-sentence pause** where the rhythm wants
   one. Used sparingly it reads as a person thinking.
6. **One idea per paragraph, blank line between.** One- and two-sentence
   paragraphs. This is the recommended layout, not an AI tell.
7. **Natural rhythm, not manufactured variance.** One genuinely long sentence
   beside a short one is how people write. Alternating long/short across a
   whole post is a tic, and stacked fragments ("Fast. Reliable. Cheap.") read
   as a slide, not a sentence. At most two standalone fragments per post.
8. **0-2 hashtags, at the end.** Hashtag stacking stopped working and now
   looks like a Page that learned LinkedIn in 2019.
9. **No external link in the body.** First comment for a post, caption for a
   document post.
10. **Emoji: zero or one, never as bullets.** A 🚀✅💡 column is the single most
    recognisable AI-content signature on the platform. If the Page's own
    `company-profile.md` records an emoji habit, follow that instead.
11. **Specific numbers beat adjectives.** "Cut invoice processing from 40
    minutes to 6" beats "significantly improved efficiency". Every number needs
    a `proof-library.md` entry.
12. **Capitalise all personal, company and product names**, including inside an
    otherwise lowercase sentence.

## Worked rewrites

**Announcement**

> Before: "We are thrilled to announce the launch of our new AI-powered
> automation platform, designed to help businesses streamline operations and
> unlock new efficiencies. Stay tuned for more updates!"
>
> After: "We shipped the thing that replaced our own ops spreadsheet. It
> started as a 600-row Google Sheet that three people were editing at once
> and breaking twice a week. Priya rebuilt it as a proper workflow in
> February. We have run our own invoice approvals through it since, 180 a
> month, and the spreadsheet is archived. Now it is available to clients."

Why: the before could be any company. The after has a named person, a month, a
count, and a reason to believe, and it says what the product is by saying what
it replaced.

**Hiring**

> Before: "We're growing! We are passionate about finding talented individuals
> to join our dynamic team. If you're interested in making an impact, reach out
> to learn more."
>
> After: "We are hiring a second backend engineer, and the honest pitch is that
> you would spend your first month in other people's ERP systems, which most
> engineers hate. The person who does well here is the one who finds that
> interesting. Full scope and salary band in the comments."

Why: it filters instead of flattering, and the awkward truth is the credibility.

**Thought leadership**

> Before: "In today's rapidly evolving business landscape, leveraging AI is no
> longer optional. Organisations must fundamentally rethink their approach to
> digital transformation to remain competitive."
>
> After: "Four of the last six mid-size manufacturers who asked us for an AI
> roadmap did not need one. They needed their three systems to agree on a part
> number. We said so, and two of them hired us anyway for the smaller job."

Why: the before asserts a trend; the after reports a count and gives something
away that costs the company something to admit.

## The limit, stated plainly

None of this reliably beats a trained AI-text classifier, and no skill in this
bundle claims otherwise. Detector scores move on surface statistics that shift
between model generations, so an edit that lowers a score this month may raise
it next month. What these rules do is make the writing specific, attributable
and checkable, which is what a human reader responds to and what the 2026
ranker's credibility signals are built to reward. Optimise for the reader.

See also: `page-formats.md` for the post structures, `claims-and-compliance.md`
for what the business may assert, `precedence.md` for what wins in a conflict.
