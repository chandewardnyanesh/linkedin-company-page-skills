---
name: page-content-calendar
description: "Build a 30-day multi-surface LinkedIn content plan for a company Page: page posts, document carousels, articles, newsletter issues, polls and events, each with its pillar, format, proof asset, publish window, employee amplification assignment and the KPI it is for. Use when the user asks to 'plan our LinkedIn content', wants a content calendar, monthly or weekly plan, editorial calendar, posting schedule, or says 'what should we post this month'. Builds the plan around the company's real capacity rather than a posting target. Not for drafting the posts themselves (use page-post-writer) and not for finding the topics (use trend-radar)."
---

# Page Content Calendar

Turn opportunities into a month the business can actually execute.

## The planning premise

A company Page reaches roughly 1-2% of its followers organically, while
individual accounts take the large majority of feed distribution
(`../../references/page-algorithm-heuristics.md`). So a calendar that is only a
list of Page posts is a plan to publish into an empty room, however good the
posts are.

A working Page calendar has three layers, and the second two are where the
reach is:

1. **The Page's own posts** — the asset library and the credibility signal.
2. **The amplification layer** — who carries each post, with their own angle.
   Not optional, not a nice-to-have.
3. **The owned-distribution layer** — the newsletter, which notifies
   subscribers by email and is the only Page surface the ranker cannot
   throttle.

A plan missing layer 2 or 3 should be flagged as incomplete when you present
it, with the reason.

## When to use

- "Plan our LinkedIn content" / "content calendar" / "editorial calendar"
- Monthly or quarterly planning
- After `trend-radar` has produced opportunities
- When the user wants a posting schedule they can hand to someone

## Steps

### 1. Capacity first, volume second

Read `../../references/company-profile.md` §9 — posts per week, articles per
month, newsletter frequency, who writes, who approves, hours available.

**Plan to that, and if the user asks for more, say what would have to give.**
This is the most consequential step in the skill. Over-planning is the standard
failure of content calendars: it produces three good weeks and a month of
filler, and the Page is judged on the filler. `page-formats.md` is explicit
that a quiet week costs less follower trust than a filled one with nothing in
it.

Also read §7 pillars, §10 hard limits, and
`../../references/claims-and-compliance.md` §1 for the approval path and its
real turnaround. A plan assuming same-day approval when legal takes four days
is a plan that misses every launch date.

### 2. Get the raw material

Either take the ranked opportunities from `trend-radar`, or build a short list
with the user. Each slot in the calendar needs a **subject the business has
standing on** and a **proof entry or named experience behind it**. A slot with
neither is a slot that will be filled with an adjective in three weeks.

### 3. Anchor the month on one heavy asset

Decide this before anything else: the **one P4 data drop or P7 process reveal**
(`../../references/page-formats.md`) that the month is built around.

That single asset becomes:

- the document carousel (the strongest organic format),
- the article or newsletter issue (`../../references/article-architectures.md`
  A2 or A7),
- two or three Page posts pulling different findings out of it,
- the thing employees actually reshare,
- and, if there is paid budget, the sponsorable asset.

One properly made asset produces a month. Four thin ones produce four days.
**A month with no heavy asset in it is a month of filler** — say so plainly if
the capacity will not support one, and plan a lighter month honestly rather
than a busy one that pretends.

### 4. Lay out the month

Working mix for a Page posting 2-4 times a week:

| Frequency | Slot | Formats |
|---|---|---|
| 1 × month | Heavy asset + its carousel + its article | P4 / P7 → A2 / A7 |
| 2 × month | Proof or honesty | P1, P12 |
| Weekly | Customer question answered | P11 |
| 1 × month | Position-taking, for comments | P5, P6, P13 |
| As needed | Hiring, events, milestones | P9, P16, P14, P10 |
| Per frequency in §9 | Newsletter issue | A8 |

Sequence rules that matter more than the slots:

- **The carousel follows the article by 3-7 days**, not the same day. The post
  is the trailer; releasing both at once wastes one.
- **Space position-taking posts.** Two contrarian posts in a week reads as a
  Page with a grievance.
- **Put the heavy asset mid-month**, so there is room to pull follow-up posts
  from the response to it.
- **Tuesday-Thursday mornings in the audience's timezone** as the default
  window. Treat it as a tiebreaker; timing has never rescued a post nobody
  wanted to read.

### 5. Assign amplification per slot

For each Page post, name:

- **Who carries it** — 3-6 people with a genuine stake, chosen by relevance to
  that post rather than by seniority.
- **Which rung** — react / substantive comment / reshare with a take / original
  post (`../../references/amplification-mechanics.md`).
- **Their distinct angle** — one line each. Never one caption for everyone: a
  dozen identical reshares is the clone signal 360Brew discounts, and it
  reduces the resharers' own future reach.

And allocate the **Notify-employees budget: once every seven days per Page.**
Mark the one post each week it is spent on. Spending it on a routine update
teaches employees the notification is noise.

### 6. Attach a KPI per slot

Each slot gets one metric from `../../references/metrics-taxonomy.md`, chosen
from the ones worth reporting — newsletter subscribers, custom button clicks,
substantive comments, saves, employee reach, lead-form fills. **Not
impressions.** A slot whose only possible KPI is impressions is a slot doing no
job.

### 7. Output

```
# [Company] — LinkedIn Page plan, [month]

## The month in one line
[what this month is trying to achieve]

## Capacity this plan assumes
[posts/week, articles, newsletter, who writes, who approves, turnaround]

## The heavy asset
[what it is, what it is built from, what it becomes]

## Calendar
| Date | Surface | Format | Pillar | Working title | Proof needed | KPI | Amplifiers | Notify? |
|---|---|---|---|---|---|---|---|---|

## Amplification per post
[post → people → rung → their angle]

## Proof gaps to close before drafting
[the claims that need clearing, and who clears them]

## What this plan deliberately does not do
[the things skipped, and why]

## Inbound readiness check
[who answers comments and DMs during this month, and the response window]
```

That last check exists because a plan that generates inbound nobody answers is
worse than no plan: an unanswered comment on a company Page is read as the
company's actual service level.

### 8. Hand off

`page-post-writer` drafts the posts, `authority-article-writer` the long form,
`employee-amplification` builds the reshare kits. Name the handoffs and stop —
do not draft here.

## Hard rules

- **Never plan beyond stated capacity.** If asked, show the trade-off and let
  the user choose. Do not quietly pad the month.
- **Every slot names its proof requirement.** A slot with an unfilled proof
  requirement is flagged in the plan, not silently assumed.
- **Every Page post gets an amplification assignment**, or the plan is marked
  incomplete.
- **One Notify-employees slot per week.** It is a hard platform limit.
- **No slot exists only to hit a number.** A thin week stated honestly beats a
  full week of anti-formats (`../../references/page-formats.md` §Anti-formats).
- **Respect §10 and the approval path.** A slot needing a second approver says
  so, with the lead time built in.
- **Protect the amplifiers.** One company-adjacent post per person per week is
  the ceiling; beyond it they lose the audience that made them useful.

## Anti-patterns

- A five-posts-a-week calendar for a company with one person writing part time.
- Daily posting to "stay top of mind". It trains followers to scroll past the
  Page and the penalty compounds.
- Theme days ("Monday Motivation", "Feature Friday"). The theme becomes the
  reason to post and the content arrives second.
- Holiday and awareness-day slots with no connection to the business.
- A plan with no newsletter line when the Page qualifies for one
  (`../../references/page-surfaces.md` §Newsletter eligibility).
- Planning the article and its promotional post for the same day.
- A calendar where every KPI is impressions.

## Resources

- `references/pillar-and-cadence-models.md` — pillar sets by business type, and honest cadence models
- `../../references/page-formats.md` — the 16 formats and the monthly mix
- `../../references/article-architectures.md` — long-form structures
- `../../references/amplification-mechanics.md` — rungs, the notify budget, who to ask
- `../../references/page-surfaces.md` — every surface and its gating
- `../../references/metrics-taxonomy.md` — which KPIs are worth a slot

## Related skills

- `trend-radar` — supplies the opportunities
- `page-post-writer` / `authority-article-writer` — draft the slots
- `employee-amplification` — builds the per-post reshare kits
- `page-performance-report` — closes the loop on the KPIs set here
