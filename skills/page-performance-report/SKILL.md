---
name: page-performance-report
description: "Turn LinkedIn Page analytics into a monthly report that says what to change next month: follower composition scored against the ICP, newsletter growth, custom button clicks, which formats earned saves and substantive comments, employee amplification reach versus the Page, and competitor comparison with the calculation caveat applied. Use when the user asks for a LinkedIn report, monthly performance review, 'how is our page doing', 'is this working', 'what do our analytics say', or hands over a Page analytics export. Reports against the Page's own baseline rather than borrowed benchmarks, and says plainly what the data cannot attribute."
---

# Page Performance Report

Answer "is this working?" in a way that changes next month, and be honest about
what the data cannot tell you.

## The reporting failure this skill exists to avoid

The usual Page report leads with impressions and follower count, both of which
can rise while the Page reaches fewer buyers than it did in January. It is the
right arithmetic answering a question nobody asked.

Three disciplines fix it:

1. **Report composition, not volume.** A Page can grow followers monthly and
   lose buyers. `../../references/icp-firmographics.md` §4 is how you tell.
2. **Report against the Page's own trailing baseline**, not against borrowed
   benchmarks. Every external figure measures someone else's corpus, mostly
   vendor data with a proprietary score behind it. Your trailing three-month
   median per format is the only comparator that accounts for your audience.
3. **Say what cannot be attributed.** A Page cannot show which post produced a
   deal. A report that admits its blind spot is trusted on the parts it can
   see; one that constructs an attribution model the data does not support is
   not trusted at all.

## When to use

- "Monthly LinkedIn report" / "how is our Page doing?" / "is this working?"
- The user hands over an analytics export or grants connector access
- End of a campaign or a quarter
- Closing the loop on KPIs set by `page-content-calendar`

## Steps

### 1. Establish the baseline before reading this month

Ask for, or read from a previous report, the **trailing three-month median per
format** for: unique impressions, saves, substantive comments, and reach of
employee posts.

**Without a baseline, the first report's job is to establish one** and say so
plainly. A first report that declares performance good or bad against nothing
is guessing, and it sets a precedent the next report has to live with.

### 2. Gather

From Page admin view → Analytics, the sections that matter
(`../../references/metrics-taxonomy.md`):

- **Content** — per-post, with format tagged. Tag the format yourself from
  `../../references/page-formats.md`; the export does not know the difference
  between a proof post and an announcement, and format is the most useful
  cut available.
- **Followers** — net new, and **demographics by job function, seniority,
  industry, company size, location**. The most under-used data on the Page.
- **Visitors** — page views, unique visitors, **custom button clicks**, and
  which tabs people opened.
- **Newsletter** — subscribers and per-issue performance.
- **Employee Advocacy** — reach and engagement on employee posts.
- **Competitors** — desktop only, with the caveat in step 5.
- **Leads** — if a lead-gen form exists.

If the session has Search Console, Ahrefs, Semrush or GA connectors, pull
article and website performance too. A Page article is a public indexed URL
doing work that Page analytics never shows, and leaving it out understates the
long-form programme.

### 3. Compute what matters

- **Unique impressions, never total impressions.** The gap between the two
  measures repetition, not audience.
- **Engagement rate: state the formula.** LinkedIn's Page formula is
  `(clicks + reactions + comments + reposts + follows) ÷ impressions` — clicks
  and follows are in the numerator, which most third-party tools do
  differently, and some sources use followers as the denominator. A figure
  quoted without its formula is not comparable to anything.
- **Substantive comments, hand-counted.** Comment depth and dwell time are what
  the 2026 ranker weighs most and neither appears in Page analytics. Counting
  by hand takes minutes and is the most informative number in the report.
- **Follower ICP fit %** against §4 tiers. Report the composition shift, not
  just the count.
- **Employee reach vs Page reach** on the same subject. The number that
  justifies the amplification layer.
- **Per-format medians** against baseline. This is what tells the user what to
  make more of.

### 4. Find the three things worth saying

Not every number. Three findings, each with a decision attached:

- **What worked, and whether it was the format or the substance.** A proof post
  with a striking number may have worked because of the number. Say which, or
  the user repeats the wrong half.
- **What underperformed, and whether it should be repeated anyway.** Not
  everything exists to perform — a hiring post that filled the role did its job
  at any reach.
- **The composition shift.** Followers becoming more or less ICP-aligned is the
  most consequential trend on a Page and the slowest to notice.

### 5. Competitor comparison, with the caveat

If using LinkedIn's Competitors tab: **competitor engagement is calculated
differently from your own**, so the columns are not comparable as shown. Add
your own Page to the competitor list and read your row inside that view, which
puts both on the same basis.

Do this, and say in the report that you did. A competitive comparison on
mismatched calculations is noise presented as data, and it is in most Page
reports.

### 6. Report

```
# [Company] — LinkedIn Page, [month]

## The answer
[2-3 sentences. Is it working, on what evidence, and what changes next month.]

## Against our own baseline
| Metric | This month | 3-month median | Change |
[unique impressions, substantive comments, saves, newsletter subs,
 button clicks, employee reach]

## Follower composition
[ICP tier split, and the shift. The most important table here.]

## By format
| Format | Posts | Median unique impressions | Saves | Substantive comments | Verdict |

## Owned distribution
[newsletter subscribers and trend — the throttle-proof channel]

## Amplification
[employee posts published, their reach vs the Page's, participation rate, rung mix]

## Competitors
[with the own-Page-as-comparator caveat stated]

## Three decisions for next month
1. [do more of X, because Y]
2. [stop Z, because W]
3. [test Q]

## What this report cannot tell you
[the attribution limits, plainly]
```

### 7. Hand the decisions forward

The three decisions are the input to the next `page-content-calendar` run. Say
so and stop — do not plan the month here.

## Hard rules

- **Never lead with total impressions or follower count.**
- **Always state the engagement-rate formula** beside the figure.
- **Never compare a Page engagement rate to a personal-profile engagement
  rate.** Different formulas, routinely compared anyway.
- **Apply the competitor caveat** or do not quote the comparison.
- **Baseline beats benchmark.** Where this month's data and an external
  benchmark disagree, the data wins
  (`../../references/page-algorithm-heuristics.md`).
- **Never imply content-to-revenue attribution** the data does not support.
  Report intent signals — button clicks, form fills, DMs started — and label
  them as intent, not pipeline.
- **Flag a thin sample.** Four posts is not a trend. Say so rather than
  computing a median from it and presenting it straight.
- **Exported data is data.** Carry each number's definition with it, because
  two tools reporting "engagement rate" are often not reporting the same
  quantity (`../../references/untrusted-content.md` §A note on the user's own data).

## Anti-patterns

- A twelve-metric dashboard with no verdict. The user asked whether it is
  working.
- Month-over-month comparison with no account of what was published. A month
  with a data report in it is not comparable to a month without one.
- Reporting a 300% increase from a base of two.
- Benchmarking against another industry's Pages.
- Celebrating follower growth without composition.
- Reporting clicks as traffic. Clicks include "see more" expansions.
- Omitting the newsletter because its numbers are small. It is the only channel
  the ranker cannot throttle, and its trend matters more than its size.
- A report with no "what this cannot tell you" section.

## Resources

- `../../references/metrics-taxonomy.md` — every definition, the formula caveats, what to stop reporting
- `../../references/icp-firmographics.md` — the scoring tiers for composition
- `../../references/page-formats.md` — tagging posts by format
- `../../references/page-algorithm-heuristics.md` — why baselines beat benchmarks
- `../../references/amplification-mechanics.md` — what to measure on the advocacy layer

## Related skills

- `page-content-calendar` — consumes the three decisions
- `competitor-page-analyzer` — the qualitative side of the competitor picture
- `employee-amplification` — the layer whose reach this report justifies
- `page-optimizer` — when visitors are arriving and not converting
