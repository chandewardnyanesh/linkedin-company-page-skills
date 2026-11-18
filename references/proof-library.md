# Proof Library

Every factual claim the Page is allowed to make, with the evidence behind it.

## Why this file is the one that prevents the expensive mistake

A number in a personal post is a person's recollection. A number on a company
Page is a representation made by a business, in public, with a timestamp, to an
audience that includes its customers, its competitors and its regulators. It
gets screenshotted before it gets corrected.

So the rule across this bundle is: **a draft may only state a figure that has an
entry here.** No exceptions, no "approximately", no rounding up to a better
number. If the business cannot produce the evidence, the claim does not go in
the draft — and a weaker post is a far cheaper outcome than a retraction.

This also removes the most common failure mode when an agent writes marketing
copy: filling a template's `[specific number]` slot with something plausible.
A plausible number is a fabricated number. When a format needs a figure and
this library has none that fits, the correct move is to ask, or to pick a
different format (`page-formats.md`).

Every skill that drafts anything surfaces the claims it used, and their sources,
on the approval card (`lib/approval.py`), so the reviewer approves evidence
rather than prose.

> **A filled library is a confidential document.** It contains customer names,
> contract values and internal figures. Same handling as
> `company-profile.md`: gitignore it or keep the filled copy outside the repo.

## Status

- filled: no
- source: template
- updated: --
- next review due: --

---

## How to write an entry

| Field | What goes in it |
|---|---|
| **Claim** | The sentence as it would appear in public, verbatim |
| **Evidence** | Where the number comes from — the system, report or document, named specifically enough that someone else could find it |
| **Measured** | The date or date range. A claim with no date goes stale invisibly |
| **Sample** | n, and what the n is. "3 clients" is honest; "our clients" is not |
| **Clearance** | Who approved public use, and on what date |
| **Named party OK** | Whether the customer may be identified, and in what form |
| **Expires** | When it must be re-verified or retired |

Status values: **cleared** (usable as written) · **anonymised** (usable without
the name) · **pending** (do not publish yet) · **retired** (never publish
again, kept so nobody re-adds it).

---

## 1. Outcome claims

Results delivered for customers. The backbone of P1 Proof Ledger posts and A6
buyer guides.

| Claim | Evidence | Measured | Sample | Clearance | Named party OK | Status | Expires |
|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |

**Before adding a row, check:** is the before-state measured or remembered? An
unmeasured baseline makes the whole claim an estimate, and it has to be
labelled as one.

## 2. Aggregate and scale claims

"X clients", "Y transactions processed", "Z years". The easiest claims to drift
on, because they were true once.

| Claim | Evidence | Measured | Clearance | Status | Expires |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Drift check:** "over 50 clients" written when you had 51 is still being
published at 38. Date every scale claim and review quarterly.

## 3. Proprietary data

Findings from your own book of business. The raw material for P4 posts and A2
reports — the highest-value content a Page can publish, because nobody else
can.

| Finding | Dataset | Date range | n | Method, in one line | Known limits | Status |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

**Limits are not optional.** A finding published without its sample size is
read as marketing by exactly the audience it was meant to convince. State n and
state what the data cannot tell you (`article-architectures.md` A2).

## 4. Named customers and logos

| Customer | Permitted form | What may be said | Clearance doc / date | Expires |
|---|---|---|---|---|
|  |  |  |  |  |

Permitted forms: **full name** · **descriptive** ("a 180-person auto components
maker") · **sector only** · **no mention**. Default to descriptive unless the
contract or a written approval says otherwise. A logo on a website does not
imply permission for a LinkedIn post claiming a result.

## 5. Quotes and testimonials

| Quote | Attributed to | Role | Source | Written approval | Status |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

A quote must be what the person actually said. Tidying grammar is fine;
sharpening the meaning is not, and it is the thing that turns a testimonial
into a liability.

## 6. Credentials

Certifications, partner tiers, registrations, awards, memberships. These are
load-bearing for a services business and the ones most often stated after they
lapse.

| Credential | Issuer | Reference / number | Valid from | Expires | Exact permitted wording |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

**Exact wording matters.** Partner programmes and regulators specify how their
status may be described, and "certified" versus "registered" versus "partner"
are not interchangeable. Record the permitted phrasing and use it verbatim.

## 7. People

Who may be named, photographed, or quoted in Page content.

| Person | Role | May be named | May be photographed | May be quoted | Noted |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Consent is per-person and revocable. A departing employee's consent does not
survive their departure by default, and a post naming them stays up until
someone notices.

## 8. Retired claims

Kept deliberately, so a claim that was pulled once does not come back through a
new draft.

| Claim | Why retired | Date | Replace with |
|---|---|---|---|
|  |  |  |  |

---

## Review cadence

- **Quarterly:** scale claims, credentials, people.
- **On use:** anything past its Expires date is treated as `pending` until
  re-verified, not published with a caveat.
- **Immediately:** when a customer relationship ends, when a credential lapses,
  when a named person leaves.

See also: `claims-and-compliance.md` for what the business may assert at all,
`company-profile.md` §10 for standing limits, `precedence.md` for why truth of
the specifics outranks a stronger draft.
