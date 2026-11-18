# Amplification mechanics

How a Page borrows the reach it cannot earn. Given the economics in
`page-algorithm-heuristics.md`, this is not a supplementary tactic — it is the
distribution layer, and a content plan without it is a plan to publish into a
room with five people in it.

## The arithmetic

Ten employees averaging 1,500 connections each expose a post to roughly 15,000
first-degree connections before anyone reshares further. For most Pages that is
several times the follower count, from people the algorithm favours over the
Page by a wide margin. Supporting figures from the 2026 literature:

- Employee posts carry around **561% more reach per post** than Page content
  (SocialPilot, Sept 2026).
- People are reported to be around **24x more likely to reshare** content
  posted by employees than by brands, and leads sourced through employees
  convert several times more often (Social Media Examiner, citing LinkedIn's
  own advocacy material).

Treat the multipliers as directional. The mechanism — individual accounts get
distribution that Page accounts do not — is the part that is settled.

## The thing that ruins it

**A plain reshare with nothing added is worse than not resharing.** It carries
no new information, barely circulates, and reduces the sharer's own future
distribution. 360Brew was built specifically to discount low-credibility
content signals, and a dozen identical reshares of the same corporate post is
the cleanest such signal available.

This kills the standard advocacy playbook. "Here is the post, everyone please
share" produces a dozen clones, each reaching almost nobody, and quietly
damages the reach of the twelve people who helped. The 2026 shift is from
**message relay to content contribution**: employees share as authors with a
point of view, not as relays.

So every amplification kit this bundle produces gives each person **their own
angle and their own words**, never one caption to paste. The Page post is the
raw material; the employee post is a different post about the same thing.

## The amplification ladder

Ordered by effort and by value. Rungs 3 and 4 are where the reach actually is.

**Rung 1 — React.** Lowest value, near zero cost. Worth asking for only in the
first hour, where early engagement helps the Page post clear its initial
distribution test.

**Rung 2 — Comment with substance.** Underrated. A comment from an employee who
actually did the work adds information the post did not have, is visible to
that employee's network, and feeds the comment-depth signal the 2026 ranker
weighs most heavily. Cheaper than a post and disproportionately effective.

> Weak: "Great insights!"
>
> Strong: "The part we cut from this post: the first version of the mapping
> ran nightly and we had to move it to real time, because finance was
> reconciling against yesterday's numbers."

**Rung 3 — Reshare with a personal take.** The person's own first 2-3 lines
before the reshared post. Their angle, their stake, their disagreement if they
have one. Minimum ~40 words of original framing, or it reads as a relay.

**Rung 4 — An original post on the same subject.** Highest value by a distance.
Same topic, that person's experience, no link to the Page post at all. Two
posts about one thing from two accounts beat one post shared twice.

## The "Notify employees" button

LinkedIn's native tool, in the post's "..." menu in the Page admin view.

- **Rate limit: once every seven days per Page.** LinkedIn states admins can
  notify employees every seven days and shows the next eligible date. (Some
  guidance says daily; the seven-day figure is what LinkedIn's own interface
  reports, so plan on seven.)
- Notifications go to members who list the company as their current employer,
  delivered on a relevance model rather than to everyone, and employees can
  opt out.
- **Therefore it is a once-a-week budget, and it should be spent on the one
  post of the week that is worth a dozen people's credibility.** Spending it on
  a routine update is the most common way Pages waste the lever: employees
  learn the notification is noise and stop opening it.
- It is desktop-only in practice, and it has no personalisation — no suggested
  captions, no variants. That gap is exactly what rungs 2-4 above fill.

## Picking who to ask

Not everyone, and not by seniority.

- **Relevance beats rank.** The engineer who built the thing is a better
  amplifier than the CEO who did not. Consistency beats title: an engaged
  mid-level person who posts regularly is worth more than an executive who
  needs chasing for every post.
- **Match the post to the person's actual stake.** A P1 proof post goes to
  whoever delivered the work; a P9 hiring post goes to the team that will
  interview; a P4 data drop goes to whoever ran the numbers.
- **Three to six people per post, with different angles.** More than that and
  the angles start repeating, which is the clone problem again.
- **Never make it mandatory.** Compliance-driven programmes produce robotic
  posts and low participation, and the robotic posts are the ones the ranker
  discounts. Ask, make it easy, accept no.
- **Protect the volunteers.** Someone resharing twice a week turns their feed
  into a company channel and loses the audience that made them useful. One
  company-adjacent post a week per person is a reasonable ceiling.

## Thought Leader Ads, honestly

TLAs sponsor an **individual's** organic post rather than a Page post, which is
how a brand buys around the Page reach problem. Mechanics worth knowing before
a plan assumes them:

- The **member must approve** the sponsorship request.
- **Only posts from the last 30 days** are eligible, so the organic pipeline
  has to run continuously.
- **Eligible formats:** text, single image, video, article and newsletter
  posts. **Not eligible:** document posts, polls, multi-image posts. This is a
  real planning constraint, because document posts are the best organic format
  and the worst TLA candidate.
- Objectives are limited (brand awareness, engagement, video views); LinkedIn
  lists no lead-gen or website-visits objective for TLAs.
- Employee TLAs need no partnership label; a non-employee author does.

**On the performance claims, be careful.** LinkedIn reports around 252% higher
CTR and 62% lower CPC versus single-image ads. Independent benchmarks across
119 TLAs and $300K+ of spend put median TLA CTR at 2.68% against roughly 0.42%
for single-image ads — but the same dataset puts **click-through to landing page
at around 0.29-0.43%**, and a Sept 2026 paired within-account comparison found
landing-page CTR of 0.449% for TLAs against 0.441% for Page sponsored content:
effectively identical.

The resolution: TLA "clicks" include expanding the post, viewing the profile
and other in-feed interactions. So TLAs genuinely win on **attention and
cost per engagement**, and the evidence that they win on **traffic** is weak.
Plan them as a credibility and awareness instrument. Do not promise a pipeline
number from a CTR benchmark, and when reporting, separate in-feed clicks from
landing-page clicks or the report will flatter the format.

## What to measure

From the Page's **Employee Advocacy** analytics tab plus the posts themselves:

- Number of employees who posted, not the number asked. Participation rate is
  the health metric.
- Reach of employee posts versus the Page post on the same subject. This is the
  number that justifies the programme internally.
- Comments carrying new information, counted by hand. The quality signal.
- Rung distribution. A programme stuck at rungs 1-2 is a programme that has not
  started.

Definitions in `metrics-taxonomy.md`. Programme design, governance and the
launch sequence live in `skills/employee-amplification/`.
