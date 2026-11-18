# Authority article architectures

Eight structures for LinkedIn Articles and Newsletter issues published as the
Page. This is where a company builds the thing a Page post cannot: a reference
that keeps earning attention after the week it shipped.

## Why articles, given that nobody reads articles

The common objection is that LinkedIn articles get less engagement than posts.
That is true and mostly irrelevant, because an article is not competing for
feed engagement. It is doing four jobs a post cannot:

1. **It is the asset everything else points at.** A P4 data drop
   (`page-formats.md`) is a post for one day and an article for a year. The
   post is the trailer.
2. **It carries the newsletter.** A newsletter issue *is* an article, and the
   newsletter is the only Page surface that notifies subscribers by email —
   the one channel the ranker cannot throttle (`page-surfaces.md`).
3. **It is indexed.** Articles are public URLs. For a business whose buyers
   search before they ask, an article that answers a specific buying question
   does work in a channel the Page's feed metrics never show.
4. **It is sponsorable.** Sponsored Articles and Thought Leader Ads on
   article posts give a long-form asset paid distribution.

So judge an article by whether it is the best thing on the internet about one
narrow question, not by its reaction count. A Page that publishes one genuinely
authoritative article a month beats one publishing four thin ones.

## Length and shape

- **Body limit ~110,000 characters.** Effectively unlimited, which is a trap.
- **Target 1,200-2,500 words** (roughly 7,000-15,000 characters). Below 1,200
  it should have been a post. Above 2,500 it needs to be a series, because the
  completion rate falls off a cliff and an unfinished article converts nobody.
- **Headline: 100 characters**, and it is the whole click decision. Sources
  disagree between 100 and 150; `lib/surfaces.py` uses 100 so a headline is
  never silently clipped.
- **Subheads every 200-300 words.** Most readers scan the subheads first and
  decide from them whether to read anything.
- **Cover image** is required in practice — an article without one looks
  broken in the feed.
- **Rich text works here.** Unlike posts, articles support real formatting:
  headers, bold, lists, blockquotes, embedded images, and clickable links in
  the body. Use the links; an article is the one surface where an external
  link costs nothing.

## The architectures

Pick by what the company actually has. The common failure is choosing a
structure the company cannot fill, then filling it with assertion.

---

### A1 — The Reference
**Needs:** deep operational knowledge. **Half-life:** years.

The definitive answer to one narrow question a buyer searches for. Not "a guide
to AI" — "what to do when two ERP systems disagree about a part number".

```
1. The question, stated exactly as a buyer would ask it.
2. Why the obvious answer fails. (This is the part that earns the authority.)
3. The decision tree — the two or three real situations, and what each needs.
4. The procedure for each, in enough detail to follow without you.
5. What it costs and how long it takes, honestly.
6. When to call someone, and what to ask them.
```

**Test:** could a competent reader do the thing without hiring you? If not, it
is a brochure. The credibility comes from the giveaway being real.

---

### A2 — The Data Report
**Needs:** proprietary data. **Half-life:** a year, and it is citable.

The strongest asset a Page can own, because nobody can replicate it. Grows out
of a P4 post.

```
1. The headline finding as a number, in the first two sentences.
2. Method and sample, early and plainly — n, date range, how collected, what
   it cannot tell you.
3. Three to five findings, each with its own subhead and chart.
4. The finding that contradicted your own expectation. (Include it. Its
   presence is what tells a reader you did not write the conclusion first.)
5. What you think it means, labelled as interpretation rather than finding.
6. What you would measure next.
```

**Test:** state n and the limits before anyone asks. A report that hides its
sample size is read as marketing by exactly the people you wanted to convince.

---

### A3 — The Category Argument
**Needs:** a real position. **Half-life:** as long as the position holds.

```
1. The prevailing frame, stated fairly enough that its believers recognise it.
2. The specific decisions that frame produces.
3. Where those decisions fail, with evidence.
4. The alternative frame.
5. What changes under it — concretely, on Monday.
6. The strongest objection, answered rather than dismissed.
```

**Test:** does a smart person who disagrees find their own view represented
accurately in section 1? If not, the article only persuades people who already
agreed, which is nobody worth persuading.

---

### A4 — The Teardown, long form
**Needs:** judgement and a specific artefact. **Half-life:** months.

A P3 post with the full working shown. Tear down an artefact, a standard, a
widely-shared claim or an industry practice — **never a named competitor**
(`claims-and-compliance.md`).

---

### A5 — The Post-mortem, long form
**Needs:** an incident and the nerve to publish it. **Half-life:** permanent trust.

Timeline, cause, blast radius, fix, what remains unknown. The most trusted
genre in technical B2B and the one most companies will not write. Needs
sign-off, because an incident disclosure can carry contractual consequences.

---

### A6 — The Buyer's Guide
**Needs:** honesty about where you lose. **Half-life:** a year.

How to evaluate a category you sell into, written so that it is useful to
someone who will buy from a competitor.

```
1. The three or four real approaches, yours among them.
2. The dimensions that actually decide — total cost including internal time,
   time to value, who maintains it, what breaks at scale, exit cost.
3. A comparison table.
4. "Choose X if..." for each option, including the cases where you are the
   wrong answer.
5. The questions to ask any vendor, including the ones that are awkward for you.
```

**Test:** is there a paragraph that sends a reader to a competitor? If not,
nobody believes the rest of it.

---

### A7 — The Process Manual
**Needs:** a process that actually exists. **Half-life:** years.

The full version of P7. The method, step by step, with the artefacts: the
checklist, the template, the question list. This is the article that gets saved
and sent internally, which is the most valuable thing that can happen to a B2B
asset.

---

### A8 — The Newsletter Issue
**Needs:** a cadence you can actually hold. **Half-life:** one week, compounding.

A newsletter issue is an article with a different contract: it arrives by email
whether or not the ranker cooperates, so the reader has given you permission
and expects consistency.

```
1. One idea per issue. Not a roundup.
2. 800-1,500 words — shorter than a standalone article. It arrives uninvited
   and earns the next one by being finishable.
3. Open with the specific thing that prompted it this week.
4. One thing the reader can do differently.
5. A consistent closing section — a question you are chewing on, a number you
   are watching. Recognisable structure is what makes a newsletter a habit.
```

**Cadence honesty:** monthly held for two years beats weekly abandoned after
six issues. Pick the frequency the business can hold in its worst month, and
record it in `company-profile.md` so the planner does not over-commit.

## Repeating rules

- **Every factual claim needs a `proof-library.md` entry.** An article is
  linkable, quotable and screenshot-able for years. A wrong figure in a post is
  embarrassing; a wrong figure in an article is a citation.
- **Attribution over the corporate "we".** Same rule as everywhere else
  (`brand-voice-rules.md`). An article can carry a named author inside the
  Page's voice: "Priya, who ran this migration, found…".
- **No question as the headline.** Same as a post hook. A declarative headline
  with a number or a named thing in it wins.
- **One article, one job.** An article trying to educate, differentiate and
  convert at once does none of them.
- **Articles are manual to publish.** No API exists for Articles for Pages or
  Newsletters. The deliverable is a clean draft plus the UI path
  (`page-surfaces.md`), and that is the complete answer.

See also: `page-formats.md` for the post that promotes the article,
`page-surfaces.md` for limits and newsletter eligibility.
