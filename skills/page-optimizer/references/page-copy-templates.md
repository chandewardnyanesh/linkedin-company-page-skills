# Page copy templates

Structures and worked rewrites for the Page's static fields. Check every draft
with `python -m scripts.fit --surface <name>`.

## Tagline — 120 characters

No fold. It fits or it is cut. It appears beside the Page in search results and
in follow prompts, which means it is often the only thing a stranger reads
about the company.

The test for every option: **substitute a competitor's name. If the sentence
survives, it says nothing.**

### Five structures that work

**T1 — What, for whom.** The default, and hard to beat.
> `[What you do, in plain words] for [specific buyer or company type]`
>
> "ERP and systems integration for mid-size Indian manufacturers"

**T2 — The outcome, concretely.**
> `[The result the buyer gets] — [the mechanism, briefly]`
>
> "Your three systems agreeing on one part number. Integration and data work."

**T3 — The narrow claim.** Strongest when true and checkable.
> `[The specific thing you are the obvious choice for]`
>
> "The people you call when the migration has already failed once"

**T4 — Who you are not for.** Filters, and filtering reads as confidence.
> `[What you do]. [Who it is not for.]`
>
> "Fractional data engineering for 50-500 person companies. Not for startups."

**T5 — The named category plus the qualifier.** For a crowded category where
the qualifier is the whole differentiator.
> `[Category] for [constraint that rules out most providers]`
>
> "AI consulting for companies with no data team"

### Taglines to refuse

- "Empowering businesses to achieve their full potential" — survives any swap.
- "Innovation. Excellence. Integrity." — three nouns, no claim.
- "Your trusted partner in digital transformation" — four dead words.
- Anything with "solutions" unless naming a literal product.
- The mission statement. A mission is internal; a tagline is for strangers.

## About — 2,000 characters

**A Page gets 2,000, not the 2,600 a personal profile gets.** Templates written
for a personal About overflow and lose their closing paragraph, which is
usually the CTA.

The first **~300 characters** show before the section's own "see more". Write
them so they work alone, because for most readers they are the whole thing.

### Structure

```
[1] The first 300 characters: what the company does, for whom, and the one
    thing that makes it the obvious choice. No history, no founding year, no
    "we are a leading". A reader who stops here should still know whether to
    keep reading.

[2] The work, concretely. What arrives, what you do to it, what the client
    gets back. This is where a services business wins or loses — vagueness
    here reads as inexperience.

[3] Proof. One or two specific results, or the shape of the client base.
    Every figure needs a cleared row in proof-library.md.

[4] Who it is for, and who it is not for. The exclusion is load-bearing.

[5] How to start. One step, named plainly, matching the custom button.
```

### Worked rewrite

> **Before** (1,180 chars, and it survives the competitor swap entirely):
>
> "Founded in 2019, Meridian Systems is a leading provider of end-to-end IT
> enabled services and AI consulting solutions. We are passionate about
> empowering businesses to leverage cutting-edge technology to streamline
> their operations and unlock new efficiencies. Our team of dedicated
> professionals works closely with clients across industries to deliver
> world-class, scalable solutions tailored to their unique needs. We believe
> in innovation, excellence and building long-term partnerships. Whether you
> are looking to digitally transform your business or optimise existing
> processes, Meridian Systems is your trusted partner on the journey. Reach
> out to learn more about how we can help you succeed."
>
> **After** (first 300 chars doing the work):
>
> "We make a company's existing systems agree with each other. Usually that
> means an ERP, a CRM and a pile of spreadsheets that each hold a different
> version of the same customer. We map it, fix it, and hand back something
> your team can run without us.
>
> A typical engagement starts with two weeks of reading: your data, your
> process, and the three places people have built workarounds. Then we build
> the integration and the reconciliation, document it, and train whoever will
> own it.
>
> We have run 46 of these since 2019, mostly for manufacturers between 100 and
> 500 people. The last one cut invoice approval from 40 minutes to 6.
>
> We are a good fit if you have systems that do not talk and no internal data
> team. We are a poor fit if you want a platform licence — we build with what
> you already own.
>
> Start with the integration audit. Button above, or hello@meridiansystems.example."

What changed: the founding year moved out of position one, every adjective was
replaced by a fact, the exclusion paragraph was added, and the CTA names one
step. Figures shown are illustrative — real ones need cleared proof rows.

## Specialties — up to 20 entries

The closest thing a Page has to SEO. Rules:

- Use **the customer's words** (`company-profile.md` §6), not internal names.
  Buyers search "ERP integration", not "unified data fabric".
- One concept per entry. No stuffing two into a slot with a slash.
- Include the long-tail phrases a buyer would actually type, including
  misspellings of the category if they are common.
- Skip the aspirational ones. A specialty you cannot evidence is a lead you
  cannot convert.

## Custom button

Five fixed labels: Visit website · Contact us · Learn more · Register ·
Sign up.

Pick by what the click would tell you. "Visit website" is the default and
tells you almost nothing; "Contact us" is a narrower, more informative signal.
Its clicks are a reported metric and one of the very few unambiguous intent
signals a Page produces, so choose the one whose count you would act on.

## Services — up to 10

Each one surfaces the Page in service-based search. Name them as a buyer would
ask for them, not as the proposal names them. "Data migration" over
"Data Lifecycle Modernisation Engagement".

## Featured

The shelf. In priority order:

1. The newsletter, once it exists.
2. The month's heavy asset — the data report or process manual
   (`../../../references/article-architectures.md` A2, A7).
3. The one case study that most resembles the buyer you want more of.

An empty Featured section on a Page with good assets is the cheapest fix
available.

## Cover image brief

Do not describe this as finished work. Brief it:

- **Must communicate:** one thing, named.
- **Text on it:** at most six words, legible at mobile width.
- **Safe area:** the lower-left is covered by the logo on desktop and the
  crop differs on mobile. Keep text centred and high.
- **Must not be:** a stock photo of a handshake, a skyline, a diverse team
  pointing at a monitor, or an abstract blue network mesh.
