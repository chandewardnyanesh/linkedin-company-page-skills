# Page metrics taxonomy

What each number in Page analytics actually counts, and which ones are worth
reporting. Written because the most common reporting failure on a company Page
is not a wrong number — it is the right number answering a question nobody
asked.

## Where the data lives

Page admin view → Analytics, split into: **Content**, **Visitors**,
**Followers**, **Leads**, **Newsletters**, **Competitors**, and **Employee
Advocacy**. Most sections export to CSV, and Competitor analytics is
desktop-only.

## Definitions, precisely

**Impressions** — times content was served in a feed. Counts repeats to the
same person. Inflates with scroll volume and is the easiest number to grow
without anything improving.

**Unique impressions** — times content was served to *distinct signed-in
members*. The closer thing to reach. Always report this instead of impressions
where both are available; the gap between the two is a measure of repetition,
not of audience.

**Engagement rate (LinkedIn's Page formula)** — `(clicks + reactions +
comments + reposts + follows) ÷ impressions`. Note that **clicks and follows
are in the numerator**, which is not how most third-party tools compute it.
Consequences worth stating in any report:

- A Page engagement rate is **not comparable** to a personal-profile engagement
  rate computed as reactions ÷ followers, and the two get compared constantly.
- Some sources define it as interactions ÷ *followers*. Different denominator,
  different number, same name. Always say which formula a figure uses.
- A post with heavy link clicking can show a strong engagement rate with almost
  no conversation on it.

**Reactions / comments / reposts** — as labelled. **Comment depth and dwell
time are what the 2026 ranker actually rewards**, and neither appears in Page
analytics. So a report built on reactions is measuring the signal the platform
cares least about. Count substantive comments by hand; it is a few minutes and
it is the most informative number available.

**Clicks** — all clicks on the post, including expanding "see more", the
document, the Page name and any link. Not link clicks. Do not report clicks as
traffic.

**Custom button clicks** — clicks on the Page's single CTA button. One of the
few unambiguous intent signals a Page produces, and routinely ignored.

**Page views / unique visitors** — total views of Page tabs versus distinct
people. High views with low unique visitors means a small group returning,
which is usually staff and candidates rather than buyers. Visitor metrics
break down by tab, which tells you what people came to check.

**Followers / follower demographics** — total and net new. Negative when
unfollows exceed gains. Demographics break down by job function, seniority,
industry, company size and location: **this is the most under-used data on the
Page**, because it answers whether you are reaching buyers or peers. Score it
against `icp-firmographics.md`.

**Leads** — downloadable, and only populated if a lead-gen form exists on the
Page.

**Newsletter analytics** — subscribers and per-issue performance. Subscriber
count is the single most important growth number a Page has, because it is the
only audience the ranker cannot throttle (`page-surfaces.md`).

**Employee Advocacy tab** — reach and engagement on employee posts about the
company. The number that justifies the programme in
`amplification-mechanics.md`.

**Competitor analytics** — follower and content comparison against Pages you
nominate. One critical caveat: **competitor engagement is calculated
differently from your own**, so the columns are not directly comparable. The
standard workaround is to add your own Page to the competitor list and compare
your Page against itself inside that view. Without that step the comparison is
noise, and most competitive reports skip it.

## What to report, and what to stop reporting

**Lead with these.** They move for reasons you control and they map to money.

| Metric | Why |
|---|---|
| Newsletter subscribers, net new | The only throttle-proof channel |
| Custom button clicks | Unambiguous intent |
| Unique impressions on the month's heavy asset (P4/P7) | Did the thing worth making land |
| Substantive comments, hand-counted | The signal the ranker weighs most |
| Follower ICP fit % | Reaching buyers or reaching peers |
| Employee posts published, and their reach vs the Page's | The distribution layer's health |
| Saves and reposts on document posts | Whether the asset is being carried |
| Lead-form submissions / DM conversations started | Pipeline |

**Stop leading with these.** Report them if asked, with context.

- **Total impressions.** Compares badly across periods and rewards volume.
- **Follower count as a headline.** A Page can gain followers monthly and reach
  fewer buyers. Composition beats count.
- **Engagement rate without its formula.** See above.
- **Reactions.** The weakest signal on the platform.
- **Anything benchmarked against another industry's Page.**

## Baselines beat benchmarks

Every external figure in `page-algorithm-heuristics.md` measures someone else's
corpus, most of it vendor data with a proprietary score behind it. Your own
trailing three-month median per format is a better comparator than any of them,
and it is the only comparator that accounts for your follower composition.

Practical rule: **report change against your own last three months, and use
external benchmarks only to sanity-check direction.** When the two disagree,
your analytics win.

## Attribution honesty

A Page cannot show you which post produced a deal, and no amount of reporting
rigour changes that. What it can show is whether the right kind of people are
arriving and whether they take an action with intent in it. Say so in the
report rather than constructing an attribution model the data does not support:
a report that admits its blind spot is trusted on the parts it can see.

Reporting workflow and templates: `skills/page-performance-report/`.
