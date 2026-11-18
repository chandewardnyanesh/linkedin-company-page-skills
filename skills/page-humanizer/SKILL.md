---
name: page-humanizer
description: "Strip AI tells and corporate press-release voice out of company Page content, and run a pre-publish audit against brand voice, surface limits, claims clearance and platform rules. Use when the user says 'this sounds like AI', 'make this sound human', 'too corporate', 'rewrite this in our voice', 'check this before we post', 'audit this draft', or pastes any brand copy that reads stiff. Use --mode audit for a pre-publish review that also checks every figure against the proof library. Works on Page posts, articles, newsletters, taglines, About sections and comments. Not for drafting from scratch (use page-post-writer or authority-article-writer)."
---

# Page Humanizer

Two modes. `--mode rewrite` (default) fixes the copy. `--mode audit` reviews a
draft before it goes out and reports rather than rewrites.

## The two voices, and why a Page gets both

A personal post can sound like AI. Brand copy sounds like AI **and** like a
press release, and the two reinforce each other because they share most of
their tells: abstraction, hedging, the passive voice, the absent narrator, and
enthusiasm with nothing underneath it.

Diagnose before editing — the fix differs:

- **Press-release voice** says *who the company is*. Test: swap in a
  competitor's name. If the sentence survives, it says nothing.
- **AI voice** says *what is generally true*. Test: swap in a different
  industry. If the sentence survives, cut it.

Both resolve the same way, and it is not word substitution. **Replace the empty
slot with a fact**: a named person, a specific number, a dated event. "Utilise"
for "leverage" is the same hole with a different word in it.

This also has a distribution consequence, not just an aesthetic one. Generic
AI-written content is actively discounted by the 2026 ranker, and corporate
Pages are the most likely thing in the feed to trip it
(`../../references/page-algorithm-heuristics.md`).

## When to use

- "This sounds like AI" / "too corporate" / "make it sound human"
- "Rewrite this in our voice"
- `--mode audit`: "check this before we post", "review this draft"
- Automatically as the last pass in `page-post-writer` and
  `authority-article-writer`

## Mode: rewrite

### 1. Load the voice

Read `../../references/company-profile.md` §5 (voice fingerprint, banned words,
emoji, hashtags, spelling) and §6 (the customer's own vocabulary — the richest
source of non-generic phrasing available, because nobody can invent it).

If the profile is unfilled, work from `../../references/brand-voice-rules.md`
and mention once that `page-profile-builder` can learn the business's voice from
its website and real copy.

### 2. Diagnose, then pick a tier

Report what is actually wrong before changing anything, so the user can see
whether you understood the problem. Then choose the lightest tier that fixes
it — detail in `references/audit-checklist.md`:

| Tier | What it touches | When |
|---|---|---|
| **T1 Surface** | Banned vocabulary, em dash cap, emoji bullets, hashtag stacking, dead bridges | The copy is structurally fine and reads stiff |
| **T2 Structural** | Rebuild the hook, break stacked triads, resequence paragraphs, move the question to the close | The hook fails or the shape is wrong |
| **T3 Substantive** | The copy has no facts in it. Needs the business to supply one, or a format change | Every sentence survives the competitor swap |

**T3 is a conversation, not an edit.** Copy with nothing specific in it cannot
be rewritten into specificity; something has to be added. Say which fact is
missing and ask for it, or propose a format from
`../../references/page-formats.md` that the available evidence supports. An
agent that fabricates the missing fact at this step is the exact failure this
bundle is built to prevent.

### 3. Rewrite, within the limits

Apply `../../references/brand-voice-rules.md` §Structural rules. Keep the
author's meaning; change the execution. Preserve anything that is genuinely
theirs — an odd phrasing a founder actually uses is the opposite of a tell.

Check the result fits: `python -m scripts.fit --surface <name> --file draft.md`.

### 4. Show the work

Present **before and after with the diagnosis per change**, not just the new
version. Three reasons: the user learns the pattern and writes better
unassisted, they can reject a change that lost something you did not know
mattered, and a silent rewrite is indistinguishable from a different draft.

Flag separately anything you changed that touches a **claim**. Rewording a
figure or a credential is not a style edit; route it through the audit rules
below.

## Mode: audit

A pre-publish review. Reports, does not rewrite. Full checklist:
`references/audit-checklist.md`.

Six gates, in this order, because a later pass is wasted if an earlier one
fails:

**1. Claims.** Every figure, customer name, credential, superlative and result
against `../../references/proof-library.md`. Report each as **cleared**,
**pending**, **expired** or **absent**. Absent is a blocker. This gate comes
first because it is the only one whose failure is expensive after publication.

**2. Compliance.** Against `../../references/claims-and-compliance.md`: named
competitor, unsubstantiated superlative, regulated-category claim, confidential
material, a subject §6 says the Page stays out of. Name the required second
approver if the content type needs one.

**3. Surface fit.** Character count against the limit, hook inside the fold,
document specs if applicable. Run `scripts.fit`; do not count by eye.

**4. Voice.** Banned-word density (max one per 300 characters, zero in the
first 210), em dash cap, emoji-as-bullets, hashtag count, the competitor-swap
test and the industry-swap test on the opening three lines.

**5. Platform rules.** Question as first line, comment-gating, link in body,
all-caps opener, engagement-bait closer, LinkedIn framed as inferior.

**6. Job.** Which `page-formats.md` job is this post doing, and is there an
amplification plan? A post with neither is a post that will reach nobody, and
saying so is more useful than approving it.

### Audit output

```
## Audit — [asset], [date]

VERDICT: ship / fix first / do not ship

BLOCKERS
  [claim with no proof row, compliance breach, over the limit]

FIX BEFORE SHIPPING
  [voice density, hook behind the fold, missing amplification]

WORTH CONSIDERING
  [softer notes]

CLAIMS LEDGER
  [each claim → status → source]
```

**Give a verdict.** An audit that lists observations without a recommendation
pushes the decision back to someone who asked precisely because they wanted
one.

## Hard rules

- **Never invent a fact to fix thin copy.** T3 asks; it does not fill.
  (`../../references/precedence.md` rule 2.)
- **Never change a number, date, name or credential** while rewriting for
  voice. Flag it and leave it.
- **Never relax a claim into deniability.** "Up to", "as much as", "helped
  clients achieve" around an unevidenced figure is the same claim wearing a
  hedge, and it reads weaker than dropping it.
- **A blocker is a blocker.** An absent proof row is not a "consider".
- **Preserve the client's own oddities.** A founder's actual phrasing is
  evidence of a human, not a defect. Only touch it if it breaks a stated rule
  in §5.
- **Claim no detector result.** See below.

## On AI detectors

No edit reliably beats a trained classifier, and this skill does not claim one.
Detector scores move on surface statistics that shift between model
generations, so an edit that lowers a score this month may raise it next. A
detector score is also not what anyone is actually optimising for.

What these rules do is make copy specific, attributable and checkable — which
is what a human reader responds to and what the ranker's credibility signals
are built to reward. If a user asks for a detector score, say this, and offer
the audit instead.

## Anti-patterns

- Rewriting a draft into a different, better draft about something else.
- Synonym substitution presented as humanising.
- Adding a fabricated specific to satisfy the "needs a number" rule.
- Stripping every contrast and every triple. One of each, carrying a fact, is
  how people write; the tell is repetition plus emptiness, not the device.
- Manufactured variance — alternating long and short sentences across a whole
  post, or stacking fragments ("Fast. Reliable. Scalable.").
- Auditing without a verdict.
- Flagging the em dash as the problem when the problem is that the paragraph
  says nothing.

## Resources

- `references/audit-checklist.md` — the six gates in full, the tier rationale, worked diagnoses
- `../../references/brand-voice-rules.md` — banned vocabulary, structural rules, worked rewrites
- `../../references/proof-library.md` — claim statuses
- `../../references/claims-and-compliance.md` — compliance gates
- `../../references/page-surfaces.md` — every limit

## Related skills

- `page-post-writer` / `authority-article-writer` — call this as their last pass
- `page-profile-builder` — builds the §5 voice fingerprint this reads
- `page-repurposer` — runs this over repurposed copy, which arrives in the source's voice
