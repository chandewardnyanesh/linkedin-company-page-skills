# Company Profile

The keystone file. Every writing, planning and auditing skill in this bundle
reads it before producing anything, so that you stop re-explaining the business
on every request and so that two skills never describe the company differently.

Fill it once — or let `page-profile-builder` build it from the company website
and the existing LinkedIn Page — then correct it as things change.

> **This file lives in the repository, so git can carry it.** A filled profile
> holds positioning, pricing posture, customer names and the things you have
> decided not to say in public. If you cloned or forked this bundle, either add
> `references/company-profile.md` to `.gitignore` or keep the filled copy
> outside the repo and paste it in when you need it. `scripts/check_no_secrets.py`
> fails the build when this file is marked `filled: yes`, as a reminder.

Skills load this profile **only when `filled: yes`**. An untouched template is
ignored, and drafts fall back to the generic rules in `brand-voice-rules.md`.

## Status

- filled: no
- source: template
- website crawled: --
- page audited: --
- updated: --

---

## 1. What the business actually does

Write it the way you would say it to a peer who is not in your industry. If the
answer needs the word "solutions", it is not specific enough yet.

- One sentence:
- The work, concretely: (what arrives, what you do to it, what the client gets back)
- What you do **not** do, though people ask: (this line prevents more bad drafts than any other in the file)
- Legal entity / entities, and which one the Page belongs to:
- Founded:
- Headcount, roughly:
- Where you operate / which markets:

## 2. Who it is for

Summary only — the scoring detail lives in `icp-firmographics.md`.

- Primary buyer (role, not department):
- Who else is in the room on a decision:
- Company profile that fits best: (size, sector, situation)
- Who is a bad fit, and why:
- The trigger that makes someone start looking:
- What they were doing before they found you:

## 3. Offers and pricing posture

Pricing posture decides whether a post can mention cost at all, which is why it
belongs here rather than in a sales doc.

- Offers, with the shape of each: (fixed fee / retainer / per seat / project)
- Entry point:
- Typical engagement value and length:
- What is public about pricing: (published / ranges only / on request / never)
- What is never stated publicly:

## 4. Position

- The category the market puts you in:
- The category you would rather be in, if different:
- What a buyer gets from you that they cannot get from the obvious alternative:
- The honest trade-off of choosing you: (every real position has one; naming it
  is what makes the rest believable — see `page-formats.md` P13)
- Competitors, in the buyer's mind rather than yours: (detail in `competitor-set.md`)
- The status quo you most often lose to: (usually "nothing", "a spreadsheet", or
  "an internal hire" — and that is the real competitor)

## 5. Voice

How the Page should sound. Examples beat adjectives, and a sample of real
copy beats both.

- Three words for the voice, and three it must never be:
- People who may be named in posts, with role: (and whether each has agreed)
- Who signs off on a post before it goes out:
- Reading level / jargon tolerance: (who the audience is decides this)
- Words and phrases this business uses that outsiders would not:
- Words and phrases banned beyond the global list in `brand-voice-rules.md`:
- Emoji: (none / one occasionally / which)
- Hashtags: (none / which, consistently)
- Regional spelling: (en-GB / en-US / other)
- Language(s) the Page publishes in:

### Signature samples

Paste 2-4 passages of real copy that sound most like the business — from the
website, a proposal, an email a founder actually sent. The writing skills mirror
the rhythm and word choice of these rather than a generic brand voice. A
founder's own writing is usually the best source.

-
-
-

## 6. The customer's own words

Lift phrases verbatim from sales calls, support tickets, review sites, RFPs and
inbound emails. **This section is worth more than everything above it.** Copy
written in the customer's words outperforms copy written in the company's, and
nobody can invent these.

- How they describe the problem, in their words:
- The words they use for your category:
- Objections, verbatim:
- What they say when it works:

## 7. Content pillars

Three or four recurring subjects the Page has standing to own. A pillar needs
evidence behind it, not just interest — if there is nothing in
`proof-library.md` under a pillar, it is an aspiration.

| Pillar | Why this business has standing | Evidence available | Primary audience |
|---|---|---|---|
|  |  |  |  |

## 8. Page facts

- Page URL:
- Page numeric id: (admin view → read it from the URL. Needed for any API or
  ad work. `lib.organization_urn()` refuses to guess this from a vanity slug,
  because a wrong id publishes somewhere nobody is watching.)
- Super Admins:
- Follower count, and date checked:
- Newsletter: (none / name + subscriber count. Eligibility rules in `page-surfaces.md`)
- Showcase pages:
- Website:
- Analytics access available: (Page analytics / Search Console / Ahrefs /
  Semrush / GA — which, and under which account)

## 9. Cadence the business can actually hold

Set this to the worst month, not the best one. Over-committing here is what
produces the filler the Page will be judged on.

- Page posts per week:
- Articles per month:
- Newsletter frequency: (and whether it can survive a busy quarter)
- Who writes:
- Who approves:
- Realistic time budget per week:

## 10. Hard limits

Standing instructions. These outrank every other consideration in this bundle,
including a stronger draft — see `precedence.md`.

- Clients who may never be named:
- Numbers that may never be published:
- Subjects the Page stays out of:
- Regulatory or contractual constraints: (detail in `claims-and-compliance.md`)
- Anything a previous post got wrong that must not recur:

## 11. Brand assets

- Logo file / location:
- Brand colours (hex):
- Fonts:
- Cover image: (current file, and when it was last changed)
- Document carousel template: (if one exists)
- Image style: (and what to avoid — most businesses have a stock-photo
  allergy worth recording)
