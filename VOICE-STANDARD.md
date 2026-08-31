# MidnightLabs Voice and Authorship Standard

This standard governs public-facing writing produced with AI assistance for MidnightLabs, including GitHub narratives, LinkedIn drafts, project retrospectives, video scripts, portfolio material, and personal statements.

Its purpose is not to disguise AI-generated writing. Its purpose is to keep authorship with the person whose experience, judgment, and name are attached to the work.

> **Augment the voice. Do not replace the mind that produced it.**

## The authorship position

MidnightLabs approaches systems as wholes rather than as collections of isolated tools. The builder's role is to enter an unfamiliar system, study it, learn its relationships, and adapt it toward a deliberate purpose.

The larger purpose is transferable control over technology.

A MidnightLabs project should not end with, “Does this work for us?” It should eventually ask:

- Can another person understand what was built?
- Can the process be reproduced with ordinary or repurposed hardware?
- Can the person operate it without depending on an opaque service?
- Does the work increase their knowledge, protection, confidence, time, access, or independence?
- What must change before the solution can travel beyond its original environment?

The work is not organized around profit as its primary measure. Its value lies in creating systems, knowledge, and methods that remain useful beyond one builder and one moment.

## The Authorship Gate

Before drafting anything that speaks publicly in the builder's name or interprets the builder's experience, stop and request first-person input.

The gate applies to:

- LinkedIn posts
- Portfolio and project narratives
- Retrospectives and lessons learned
- Personal statements
- Video scripts and narration
- Public explanations of motives, values, emotions, or changes in judgment
- Any claim beginning with the equivalent of “I learned,” “I realized,” “I believe,” or “This mattered because”

The gate is usually unnecessary for mechanical changes such as fixing a broken link, correcting a filename, formatting a table, or reproducing already approved factual language.

### Prompt back

Ask one or more focused questions that expose the experience beneath the artifact:

- What actually happened from your perspective?
- What did you believe before the work began?
- What confused, surprised, frustrated, or changed you?
- Which failure altered the design?
- What remains unresolved?
- What language did you naturally use while describing it?
- What do you want another person to gain from this work?
- What would a clean technical summary fail to show?

Do not ask every question by default. Ask the smallest number capable of locating the author's center of gravity.

If the author does not answer, produce an outline or explicitly labeled technical summary—not a fabricated personal narrative.

## Nondelegable material

AI assistance must never invent or infer as fact:

- Personal emotions
- Private motives
- First-person quotations
- Moments of realization
- Moral conclusions
- Confidence levels
- Claims of struggle, excitement, pride, frustration, or transformation
- Intentions that the author has not expressed
- A heroic arc unsupported by the record

When personal meaning is required, mark the gap and prompt the author back.

## Drafting sequence

1. **Collect evidence.** Start with logs, commits, screenshots, notes, commands, results, and dates.
2. **Request authorship.** Pass through the Authorship Gate when the artifact interprets experience.
3. **Find the tension.** Identify the real problem, failed assumption, tradeoff, or design change.
4. **Draft around judgment.** Use the author's reasoning as the center rather than a generic success story.
5. **Verify every claim.** Connect technical statements to inspectable evidence.
6. **Run the slop audit.** Remove generic language, repetition, and artificial significance.
7. **Return for confirmation.** Flag personal claims, selected quotations, unresolved questions, and publication choices.
8. **Publish through review.** Use a branch and draft pull request. Never merge public-facing work automatically.

## Mister Midnight voice characteristics

Preserve these behaviors without reducing them to catchphrases:

- Systems thinking: relationships and downstream effects matter more than isolated tools.
- Directness: say what happened before decorating it.
- Intellectual motion: allow the writing to show when an interpretation changed.
- Technical metaphor: use metaphor to expose structure, not to replace explanation.
- Evidentiary restraint: distinguish what exists, what was tested, what is reconstructed, and what is planned.
- Humor with function: use it when it reveals frustration, scale, absurdity, or personality.
- Uneven rhythm: permit short sentences, longer reasoning, interruptions, and unresolved edges when natural.
- Human stakes: connect control of technology to agency without manufacturing inspiration.
- Transferability: ask whether another person can reproduce, control, or benefit from the work.

Profanity, slang, and signature phrases are not authenticity tokens. Use them only when they originate in the author's supplied language and suit the audience.

## Slop audit

Before requesting publication approval, test the draft.

### Specificity

- Could this passage describe thousands of unrelated student projects?
- Does it contain a concrete system, decision, result, or failure?
- Is the central claim inspectable?

### Authorship

- Did the author supply the personal judgment?
- Does the draft preserve how the author's thinking moved?
- Has the model fabricated emotion or certainty?
- Would the author plausibly say this aloud?

### Language

Challenge phrases such as:

- “I'm excited to share”
- “In today's rapidly evolving landscape”
- “This journey taught me”
- “This project was more than just”
- “This experience reinforced the importance of”
- “I'm thrilled to continue growing”
- “Here are three key takeaways”

These phrases are not automatically forbidden, but they require a specific reason to survive.

Also remove:

- Generic motivational conclusions
- Repeated summaries
- Inflated claims of impact
- Perfectly symmetrical sections created only for presentation
- Abstract nouns standing in for evidence
- Unnecessary transitions
- Corporate enthusiasm the author did not express
- Contrast formulas repeated as a stylistic habit

### Transferability

- Does the artifact explain what another person could reuse?
- Does it identify dependencies, limits, or missing steps?
- Does it increase control over technology rather than merely advertise technical consumption?

## LinkedIn rule

A LinkedIn draft is a translation of verified work for a professional audience. It is not a substitute for the GitHub record and must not become an inspirational costume placed over thin evidence.

Each draft should contain:

- One meaningful outcome, tension, or change in judgment
- A link to the strongest supporting evidence
- Only technical claims verified by the repository
- Personal meaning supplied through the Authorship Gate
- A recommended visual and accurate alt text
- A restrained set of relevant hashtags
- Explicit flags for anything requiring confirmation

AI may prepare the draft. Only the author decides whether it represents them and whether it should be posted.

## Final review questions

Before public-facing writing is approved:

1. What evidence supports it?
2. Which words or judgments came directly from the author?
3. What changed in the author's understanding?
4. What remains uncertain or incomplete?
5. Could another person gain control, knowledge, or a reproducible path from it?
6. Does any sentence sound polished at the expense of being true?
7. Would the author sign their name beneath it without needing to explain what they “really meant”?

If the final question is uncertain, return through the Authorship Gate.
