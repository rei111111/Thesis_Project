# ADHD annotation review synchronized with the corrected CSVs

Updated 9 September 2026 under the author’s instruction to assess stated wording without inferring intent. This edition supersedes the immediately preceding review with SHA-256 `720ed32e6e08bb47336bf8ceb72bf56e6a6335e2dff4baebbecb5aa34b520591` for the CSV update.

## Scope and preservation

The completed evidence review is carried forward, with a targeted consistency pass over wording-sensitive decisions. This is not a new independent medical re-audit of every unchanged assertion. **21 claim items in 12 videos** have revised verdicts; **12 labels** differ from the immediately preceding reviewed edition. Every change is recorded below and in the accompanying audit.

Both supplied CSVs contain the same 250 records. Their original filenames, nine columns, row order, titles, likes, comments, views and durations are retained. No video is deleted or deduplicated. The six former Devanagari transcripts (108, 115, 133, 177, 187, 198) are replaced with the author-supplied English text. Three CSV transcript fields (72, 77, 78) had an exact title prefix; that prefix is removed to match the reviewed spoken text. The other 241 transcript cells are unchanged. Whitespace is collapsed only when converting the six multiline English replacements to CSV cells.

All 250 Markdown transcript/title/metadata sections below retain the author’s supplied text, with CRLF-to-LF normalization only. CSV metadata is preserved from the CSVs; Markdown metadata is preserved from the Markdown. Those supplied metadata versions are not assumed identical. Transcript wording after whitespace normalization, claim totals, unsupported counts and labels agree between this review and both corrected CSVs. No recording or alternative transcription was retrieved. The three removed CSV prefixes also include their trailing title hashtags (72, 77) or credit (78); the remaining spoken text matches the Markdown.

Compared with the uploaded CSVs there are **59 label/status changes** and **91 rows with an annotation-field change**. These totals include earlier accepted corrections, not just this literal-wording pass. All 250 rows remain present; **7 labels are blank** under the two-claim minimum.

## Coding rules

An eligible item is an externally verifiable clinical assertion concerning ADHD, including associated conditions and treatment. Personal reports and opinions remain outside that denominator unless generalized. Explicitly attributed and rebutted quotations are not treated as the speaker’s endorsement. Explicit qualifiers (for example, may, can, some and a stated hypothesis) are retained. Literal reading does not add a causal assertion to the word correlation or an anatomical claim to an explicit analogy.

No unspoken intention, irony or charitable replacement wording is used to rescue an unsupported clinical assertion. Stated all, always, never, will, cannot and impossible are retained with their actual scope. An implied clinical claim that the transcript does not state is not added. A material unsupported component makes the recorded compound item unsupported; pre-existing claim units are otherwise retained for traceability.

S = supported; U = false, overstated or insufficiently supported as stated; X = excluded from scoring. The existing CSV column `false_claims` counts U, which does not mean that every U assertion has been experimentally disproved. Excluded items are absent from both the total and the unsupported denominator.

At least two eligible claims are required for a label. The exact supported fraction determines Label 1 (at least 80%), Label 2 (at least 60% but under 80%), Label 3 (at least 16% but under 60%) or Label 4 (under 16%). The fraction is not rounded before comparison. Fewer than two claims produce a blank CSV label, including a one-claim video whose claim is supported.

## Label changes from the preceding reviewed Markdown

| Video | Previous reviewed label | Current label | Supported / eligible | Changed claim items |
|---:|---|---|---:|---|
| 53 | Label 1 | Label 3 | 1/3 | 1, 4 |
| 57 | Label 3 | Label 4 | 0/2 | 2 |
| 110 | Label 3 | Label 4 | 1/7 | 2 |
| 112 | Label 1 | Label 2 | 7/11 | 1, 2 |
| 115 | Label 1 | Label 3 | 1/4 | 1, 2, 4, 5 |
| 133 | Label 1 | Label 2 | 6/8 | 2, 4 |
| 134 | Label 1 | Label 3 | 2/5 | 1, 2 |
| 164 | Label 2 | Label 3 | 2/5 | 2 |
| 187 | Label 1 | Label 2 | 2/3 | 1 |
| 202 | Label 2 | Label 3 | 1/3 | 1 |
| 228 | Label 1 | Label 2 | 5/8 | 2, 4, 7 |
| 247 | Label 3 | Label 4 | 0/3 | 2 |

## All label changes from the uploaded CSVs

Video number equals the one-based CSV data-row number. In a spreadsheet that displays the header as row 1, add one to locate the row.

| Video / CSV data row | Title | Uploaded CSV label | Corrected label | Eligible | Unsupported |
|---:|---|---|---|---:|---:|
| 1 | How ADHD & Depression Alter Your Memory | Label 2 | Label 1 | 8 | 0 |
| 10 | How Caffeine Helps People With ADHD | Label 3 | Label 2 | 4 | 1 |
| 13 | How to Get Diagnosed With ADHD | Label 2 | Label 1 | 6 | 1 |
| 14 | Dangers of Untreated ADHD | Label 3 | Label 2 | 8 | 3 |
| 21 | 10 signs of ADHD in women, FULL VIDEO on channel. #adhd #adhdtiktok | Label 2 | Label 1 | 10 | 0 |
| 22 | Symptoms of ADHD in women #adhd #doctor #shorts #mentalhealth #therapy | Label 2 | Label 1 | 8 | 1 |
| 25 | 3 Underrated symptoms of #ADHD | Label 3 | Label 2 | 3 | 1 |
| 37 | “ADHD is Not Real” #wait | Label 2 | Label 1 | 8 | 0 |
| 47 | ADHD isn’t a Superpower, it’s a real struggle. | Label 2 | Label 1 | 7 | 1 |
| 49 | ADHD and Time Blindness | Label 2 | Label 3 | 4 | 2 |
| 52 | ADHD and Time Blindness Explained | Label 2 | Label 1 | 5 | 1 |
| 58 | 5 Signs of ADHD 🤚🧠 \| CBBC #Shorts | Label 1 | Unlabelled | 0 | 0 |
| 59 | Fake ADHD versus real ADHD #adhd #adhdbrain #adhdselfimprovement | Label 3 | Label 2 | 4 | 1 |
| 61 | Rejection sensitivity & ADHD \| Experts answer | Label 3 | Label 1 | 4 | 0 |
| 65 | Can Sugar or Screens Cause ADHD? Here's the Real Answer | Label 1 | Label 3 | 4 | 2 |
| 73 | NEW ADHD Medication: Centanafadine (Simtriyo) Explained | Label 2 | Label 3 | 8 | 5 |
| 79 | ADHD Is Not Just a Superpower (and I Will Not Pretend) | Label 3 | Label 1 | 2 | 0 |
| 81 | 13 Ways ADHD Affects Eating Habits #adhd | Label 2 | Label 3 | 13 | 6 |
| 84 | ADHD and Sleep: Why You Can’t Just “Go to Bed Earlier” | Label 3 | Label 2 | 9 | 3 |
| 90 | ⚠️AWARENESS⚠️ #pov symptoms of ADHD that you probably didn’t know about… #shorts #fyp #tiktok #adhd | Label 3 | Label 1 | 6 | 1 |
| 96 | How does ADHD medication work? \| Experts answer | Label 1 | Label 2 | 3 | 1 |
| 103 | 4 Supplements I Take Everyday For ADHD As A Naturopathic Doctor | Label 3 | Label 4 | 4 | 4 |
| 106 | ADHD treatment options explained | Label 2 | Label 1 | 13 | 0 |
| 108 | Episode 53: ADHD #keepgoing #adhd #adhdawareness #adhdfamily #unconditionyourselfwithnamitathapar | Label 1 | Label 2 | 5 | 2 |
| 111 | ADHD Medication: What You Need to Know #adhd | Label 2 | Label 1 | 3 | 0 |
| 113 | ADHD medication does ✨SO MUCH MORE✨ than just help us focus. | Label 1 | Unlabelled | 1 | 0 |
| 115 | Adult ADHD: How Can It Impact Your Day-To-Day Life? Dr. Samir Parikh Explains #shorts | Label 1 | Label 3 | 4 | 3 |
| 126 | Can Supplements Help ADHD? | Label 3 | Label 4 | 5 | 5 |
| 134 | How to Overcome Executive Dysfunction with ADHD #adhd #executivedysfunction #bodybuilding | Label 2 | Label 3 | 5 | 3 |
| 137 | Links between ADHD and pain #ChronicPain #Pain #ADHD #ADHDAwareness | Label 3 | Label 2 | 5 | 2 |
| 138 | Side Effects of Stimulant Medication Can Worsen ADHD. | Label 2 | Label 1 | 2 | 0 |
| 146 | How do #periods impact #ADHD symptoms? #pms | Label 1 | Label 2 | 3 | 1 |
| 149 | ADHD medication pros and cons | Label 2 | Label 1 | 4 | 0 |
| 151 | Natural Recommendations For Kids With ADHD | Label 3 | Label 2 | 6 | 2 |
| 152 | Long-term use of amphetamines and stimulants can cause side effects. | Label 3 | Label 2 | 6 | 2 |
| 155 | HSP & ADHD #adhd #highlysensitiveperson #healing | Label 4 | Label 3 | 4 | 3 |
| 159 | ADULT ADHD Symptoms Diagnosis Dr Rajiv Psychiatrist हिंदी में #adhd #adultadhd #mentalhealth | Label 2 | Label 1 | 4 | 0 |
| 160 | Can ADHD Be Treated Holistically? 💊 | Label 1 | Label 2 | 5 | 2 |
| 173 | 7 Signs of ADHD in Women No One’s Talking About | Label 3 | Label 2 | 8 | 2 |
| 175 | 5 signs your boyfriend or husband may have adhd #mentalhealth #education #adhd #facts #hope | Label 2 | Label 3 | 3 | 2 |
| 178 | ADHD + Autism = AuDHD. Here's what that can really feel like… | Label 1 | Label 2 | 8 | 2 |
| 181 | How does #perimenopause impact #adhd symptoms?? | Label 1 | Label 2 | 3 | 1 |
| 182 | What it means when people with ADHD masking their symptoms? | Label 2 | Label 1 | 4 | 0 |
| 185 | Signs You Might be AuDHD (ADHD & Autism) #autism #audhd #adhd | Label 1 | Label 2 | 4 | 1 |
| 186 | What are the symptoms of ADHD? \| ABC NEWS | Label 3 | Label 1 | 5 | 1 |
| 187 | ADHD Explained: Key Symptoms, Diagnosis Criteria & Early Signs Before Age 12 #rachnabuxani #adhd | Label 1 | Label 2 | 3 | 1 |
| 191 | The "physical signs" of ADHD #adhd #neurodivergent | Label 4 | Label 3 | 3 | 2 |
| 196 | The Most Common ADHD Symptoms in Women | Label 2 | Label 1 | 4 | 0 |
| 201 | Signs of ADHD in women that no one ever talks about #shorts #ADHD | Label 3 | Label 1 | 7 | 1 |
| 208 | Treating ADHD | Label 1 | Unlabelled | 1 | 0 |
| 211 | Why are people complaining about this ADHD treatment? #adhd #adhdexplained #fy #fyp | Label 2 | Label 3 | 3 | 2 |
| 218 | Thinking outside the box for treating ADHD | Label 4 | Label 2 | 3 | 1 |
| 223 | Common ADHD Symptoms #adhd #adhders #adhdmanagement | Label 1 | Label 2 | 3 | 1 |
| 226 | The Surprising Link Between Low Dopamine and ADHD Symptoms #adhd #adhdresearch #dopamine | Label 3 | Label 1 | 2 | 0 |
| 230 | POV: How hormones affect ADHD symptoms | Label 2 | Label 1 | 3 | 0 |
| 236 | ADHD coach explains how your diet worsens your ADHD symptoms #adhd #adhdawareness #adhdkids | Label 3 | Label 2 | 3 | 1 |
| 241 | Subtle/hidden signs of adhd. #adhdsigns #adhdawareness #adhd | Label 2 | Label 1 | 3 | 0 |
| 242 | Autistic/ADHD Burnout Signs #autism #adhd | Label 2 | Label 1 | 4 | 0 |
| 247 | Avoid These 3 Foods If You Have ADHD | Label 3 | Label 4 | 3 | 3 |

## Current distribution

| Label | Videos |
|---|---:|
| Label 1 | 110 |
| Label 2 | 49 |
| Label 3 | 64 |
| Label 4 | 20 |
| Unlabelled | 7 |

---

## Video 1 — How ADHD & Depression Alter Your Memory

### Transcript

```text
let's talk about how ADHD and Depression
affect your memory with ADHD you might
forget boring stuff but remember
interesting things really well these
issues have been around since your
childhood and mainly messes with your
working memory depression on the other
hand brings a general lack of interest
in most things it comes in episodes and
slows down your overall thinking the key
difference ADHD symptoms are persistent
while depression related memory issues
typically improve as you're move food
lifts knowing these differences can help
you get the right support remember both
conditions are treatable
```

**Metadata as supplied (views, likes, comments, duration):** `117,864 5,517, 155, 37`

### Revised claim review

**Claim 1:** With ADHD, you may forget "boring" info but remember "interesting" things well

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 2:** ADHD-related memory issues have been present since childhood

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** ADHD "mainly" affects working memory

**Verdict: Supported.** The transcript is discussing memory, not claiming that ADHD consists only of a working-memory problem. The earlier rationale judged a stronger assertion. Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/), [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/).

**Claim 4:** Depression brings a general lack of interest in most things

**Verdict: Supported.** Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression).

**Claim 5:** Depression "comes in episodes"

**Verdict: Supported.** Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression).

**Claim 6:** Depression slows down overall thinking

**Verdict: Supported.** Cognitive slowing is a documented depressive feature; it need not occur in every episode to support this general description. Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression), [DEPRCOG](https://link.springer.com/article/10.1007/s00406-022-01479-5).

**Claim 7:** Key differentiator — ADHD symptoms are persistent, depression-related memory issues improve as mood lifts

**Verdict: Supported.** Retained as a typical course distinction, not a diagnostic test: cognitive problems may persist after mood remission. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DEPRCOG](https://link.springer.com/article/10.1007/s00406-022-01479-5).

**Claim 8:** Both conditions are treatable

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd), [DEPR](https://www.nimh.nih.gov/health/publications/depression).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **8**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **8 / 8 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 2 — ADHD Burnout explained 🧠 #adhd #adhdbrain #burnout

### Transcript

```text
people with ADHD experience burnout more
quickly than neurotypical people let me
explain why this cup is an ADHD person
and this cup is a neurotypical person
the level of sugar in each cup
represents their energy levels in the
morning the neurotypical person will
wake up check their emails get ready and
leave for work this takes minimal effort
for them an ADHD person will wake up
become overwhelmed by their inbox get
decision paralysis over what to wear
probably forget where they left their
car keys leave the house in fluster
anxiously thinking about how they're
going to explain to their boss why
they're late again when the neurotypical
person arrives at work they'll say hi to
their colleagues sit at their desk and
casually complete tasks in order of
priority and importance the ADHD person
will arrive at work sit in their car for
10 minutes preparing their alter ego for
the incoming social interactions they'll
spend the day forcing eye contact and
thinking if that thing they said in the
10: a.m. meeting sounded stupid they'll
have a constant nagging worry of whether
or not they locked their front door
they'll sit at their desk and
```

**Metadata as supplied (views, likes, comments, duration):** `3,477,234 180,381 5,680 61`

### Revised claim review

**Claim 1:** People with ADHD experience "burnout" more quickly than neurotypical people

**Verdict: Unsupported.** Stress/exhaustion is documented; a comparative time-to-burnout rule is not established. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 2:** Morning overwhelm from tasks (inbox), decision paralysis over clothing, and forgetting items (keys)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 3:** Anxious rumination about lateness and explaining it to a boss, framed as an ADHD-driven pattern

**Verdict: Unsupported.** The specific inevitable morning-to-boss anxiety sequence is not established as a general ADHD pattern. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** ADHD people "prepare an alter ego" and force eye contact to get through social interactions at work

**Verdict: Unsupported.** Masking is reported, but an alter ego and forced eye contact cannot be generalized to ADHD workers. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 5:** Constant rumination over whether something said in a meeting "sounded stupid"

**Verdict: Unsupported.** Criticism-related distress is documented; this particular constant rumination pattern is not established. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 6:** Nagging worry about whether they locked the front door, framed as an ADHD trait

**Verdict: Unsupported.** This specific persistent checking-related worry is not a defining or established general ADHD trait. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **1**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **1 / 6 × 100 = 16.67%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 3 — ADHD pattern recognition 🧠 #adhd

### Transcript

```text
People with ADHD have amazing pattern
recognition. Here's seven ways it shows
up in their life. Number seven is often
considered rude. Number one, the bad
vibe radar. You instantly dislike people
that everyone else loves. Six months
later, everyone realizes you were right
about them. Number two, the spoiler
syndrome. You get bored with movies
because you predicted the ending 10
minutes into the intro. You see the
formula while others watch the show.
Number three, predictive listening. You
interrupt people because your brain
auto-completed their sentence 10 seconds
ago and you are waiting for reality to
catch up. Number four, the I told you so
curse. You get annoyed by problems that
haven't happened yet because you have
already calculated the inevitable
outcome. Number five, micro expression
tracking. You notice tiny shifts in tone
or body language that others miss. You
know someone is lying before they even
finish the sentence. Number six, the
novelty cliff. You become obsessed with
a new hobby, master the pattern in 2
weeks, and then quit instantly because
the puzzle is solved. And number seven,
intolerance for repetition. You feel
physical rage when someone repeats
themselves or explain something you
already understood the first time.
```

**Metadata as supplied (views, likes, comments, duration):** `741,718 30,949 1,790 74`

### Revised claim review

**Claim 1:** People with ADHD have "amazing pattern recognition," manifesting in these seven ways

**Verdict: Unsupported.** No adequate evidence was located for the asserted general superiority in pattern recognition. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** "Bad vibe radar" — instantly disliking people who are later proven untrustworthy

**Verdict: Unsupported.** The claimed reliable detection of untrustworthy people is unsubstantiated. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** "Spoiler syndrome" — predicting movie endings early and getting bored because the "formula" is seen

**Verdict: Unsupported.** The claimed superior prediction of movie endings is unsubstantiated. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** "Predictive listening" — interrupting people because your brain "auto-completed" their sentence

**Verdict: Unsupported.** Interrupting is real; the proposed superior-prediction mechanism is unsubstantiated. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** "I told you so curse" — feeling annoyed by problems before they happen due to already "calculating" the outcome

**Verdict: Unsupported.** Unsubstantiated predictive ability, not merely ordinary anticipatory worry. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** "Micro-expression tracking" — noticing tiny nonverbal cues and detecting lies before a sentence finishes

**Verdict: Unsupported.** The claimed lie-detection advantage is unsubstantiated. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** "Novelty cliff" — mastering a hobby quickly, then losing interest once it's "solved"

**Verdict: Unsupported.** Interest fluctuations do not establish unusually rapid mastery. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8:** "Intolerance for repetition" — feeling "physical rage" when someone repeats themselves

**Verdict: Unsupported.** Low frustration tolerance does not establish this specific superior-pattern-recognition mechanism. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **0**; unsupported: **8**; excluded: **0**.
- Supported-claim percentage: **0 / 8 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 4 — 7 signs you might have ADHD with @TheFitnessMarshall #adhd #adhdtiktok #fitnessmarshall

### Transcript

```text
hey everybody today we're going to talk
about the seven signs you might have
ADHD and I've invited my good friend the
Fitness Marshall along to share some of
his tips now the first impulsivity and
the second is poor time management
skills can't do it can't do it it's hard
to manage hard to keep things in line
hard to do things even in order
sometimes order we don't know her three
we can be seen as selfish because we're
really just trying to stay interested
it's not you it's us your brain's trying
to get that dopamine that sweet sweet
dopamine I need a hit sign number four
is our executive functioning can suffer
meaning it's hard for us to juggle a lot
of things
sign number five is difficulty
motivating
you have to do it it's just the way your
brain's wired motivation sign number six
is that we struggle to put things away
where they belong usually we'll actually
get them in the proximity but not where
they belong in sign number seven as we
drive fast everywhere we go gotta get
there but also we're late for dinner so
like I have a recent dry fast that's
true we gotta go bye bye
```

**Metadata as supplied (views, likes, comments, duration):** `48,904 2,654 84 60`

### Revised claim review

**Claim 1:** Impulsivity is a sign of ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Poor time management / difficulty keeping things in order is a sign of ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** People with ADHD can be seen as "selfish" because they're just trying to stay interested/get dopamine

**Verdict: Unsupported.** Dopamine involvement does not establish this explanation of perceived selfishness. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Executive functioning can suffer, making it hard to juggle multiple things

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 5:** Difficulty with motivation is a sign of ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 6:** Difficulty putting things away where they belong (things end up "in proximity" but not put away)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Driving fast everywhere is a sign of ADHD

**Verdict: Unsupported.** Driving risk is associated with ADHD; the blanket “fast everywhere” sign exceeds that evidence. Evidence: [DRIVE](https://pubmed.ncbi.nlm.nih.gov/24238842/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **5**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **5 / 7 × 100 = 71.43%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 5 — The ADHD ‘night owl’

### Transcript

```text
People with ADHD like to stay awake later than neurotypicals, and this has puzzled researchers for 20 years until now. They have recently discovered that the reason people with ADHD are often up late into the night actually has nothing to do with sleep, but more about the fact that the quietness of the night allows their brain to finally feel safe enough to focus. During the day, there's expectations, there's pressure, there's perceived threats. During the day, the ADHD nervous system is trying to survive, making sustained focus very hard. But at night, it's peaceful. The nervous system finally has time to relax, and the ADHD brain can get its best work done. The nighttime peace is quite addictive, so the ADHD person will then delay sleep because it finally feels safe. And this is called revenge bedtime procrastination. So, the ADHD person will often be awake until the sun comes up, but we shouldn't feel shame about this. You're not lacking discipline. You're just chasing the calm.
```

**Metadata as supplied (views, likes, comments, duration):** `311,936 21,242 1,396 54`

### Revised claim review

**Claim 1:** People with ADHD tend to stay awake later at night than neurotypical people

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 2:** This has "puzzled researchers for 20 years until now" and was only "recently discovered"

**Verdict: Unsupported.** No identifiable supporting discovery was located; the claimed novelty is unsubstantiated, not proven fabricated. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 3:** The real reason for late-night wakefulness is that nighttime quiet lets the ADHD brain finally "feel safe enough to focus"

**Verdict: Unsupported.** A general nervous-system safety mechanism was not established. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** During the day, "the ADHD nervous system is trying to survive" due to expectations, pressure, and perceived threats

**Verdict: Unsupported.** Daytime threat-survival is not an established general explanation of ADHD attention. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 5:** Nighttime peace is "addictive," causing ADHD people to delay sleep because it "finally feels safe" — labeled "revenge bedtime procrastination"

**Verdict: Unsupported.** Bedtime procrastination does not establish the asserted ADHD-specific safety/addiction mechanism. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 6:** "You're not lacking discipline, you're just chasing calm" (implying poor sleep habits in ADHD are not related to self-regulation/executive function)

**Verdict: Excluded from scoring.** Supportive closing rhetoric repeats the earlier causal account; it is not a separate independently testable medical assertion.

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **1**; unsupported: **4**; excluded: **1**.
- Supported-claim percentage: **1 / 5 × 100 = 20.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 6 — 5 Signs of High Functioning ADHD

### Transcript

```text
5 Signs of High Functioning ADHD Number 5: You regularly lose important items Number 4: You're constantly interrupting others in the middle of conversations. Number 3: You have a really hard time sitting still. Number 2: You get easily distracted during tedious tasks. And Number 1: You start many tasks but leave them unfinished.
```

**Metadata as supplied (views, likes, comments, duration):** `1,532,072 29,021 1,295 23`

### Revised claim review

**Claim 1:** Framing: ‘high-functioning ADHD’ is a recognized ADHD subtype/category

**Verdict: Excluded from scoring.** The transcript uses an informal descriptor but does not assert a formally recognized diagnostic subtype. The earlier annotation introduced that claim.

**Claim 2:** Regularly losing important items

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Constantly interrupting others mid-conversation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Having difficulty sitting still

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Being easily distracted during tedious tasks

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Starting many tasks but leaving them unfinished

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 7 — ADHD and autistic people are allergic to nonsense #adhd #autism #audhd

### Transcript

```text
People with ADHD and autism, I've noticed something really interesting about them. Like really interesting. I've spoken to thousands of ADHD and autistic people on my podcast, and this is the thing that stands out. They avoid some social situations, not because they're antisocial, but because they have a low tolerance for drama and inauthentic behavior. And that's the thing. People think to be neurodeivergent is to be antisocial, but they're not antisocial. They're not cold or arrogant. They're just allergic to nonsense. Their nervous system learned something really early on, and that's that constant drama equals emotional exhaustion. So now they protect their peace. Small talk feels inauthentic and draining. Fake smiles annoy them. Performative friendships feel unsafe. Silence feels honest. People with ADHD and autism don't avoid people. They avoid emotional labor that goes nowhere. There's a difference. When they do show up, it's for deep conversations. It's intentional. Maybe they have fewer friends, but the value of those friendships is huge. They're not antisocial. They're selective. And that's a sign of high emotional intelligence.
```

**Metadata as supplied (views, likes, comments, duration):** `287,105 20,822 1,191 74`

### Revised claim review

**Claim 1:** People with ADHD and autism avoid social situations due to low tolerance for "drama" and inauthentic behavior, not because they're antisocial

**Verdict: Unsupported.** The exclusive personality-based explanation of social avoidance is unsubstantiated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Neurodivergent people are not "cold or arrogant," they are "allergic to nonsense"

**Verdict: Excluded from scoring.** “Allergic to nonsense” is evaluative rhetoric, not an independently testable clinical assertion.

**Claim 3:** Their "nervous system learned" that constant drama equals emotional exhaustion, so they now "protect their peace"

**Verdict: Unsupported.** The proposed uniform developmental nervous-system mechanism is unsubstantiated. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** Small talk feels draining, fake smiles annoy them, performative friendships feel unsafe, silence feels honest — presented as a shared trait of ADHD and autism

**Verdict: Unsupported.** This fixed emotional profile cannot be generalized to both heterogeneous conditions. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 5:** People with ADHD and autism "don't avoid people, they avoid emotional labor that goes nowhere"

**Verdict: Unsupported.** The exclusive explanation of avoidance is unsubstantiated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** They may have fewer friends but the friendships are highly valuable, and this reflects "high emotional intelligence"

**Verdict: Unsupported.** Having fewer/selective friendships does not demonstrate superior emotional intelligence. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **0**; unsupported: **5**; excluded: **1**.
- Supported-claim percentage: **0 / 5 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 8 — Signs of ADHD You Didn’t Realise #subtle

### Transcript

```text
here are signs other than attention difficulties that you could have ADHD you're always late and that's because it's quite characteristic for people with ADHD to only start getting ready when there's that voice in their head screaming at them to actually do so it may not be hugely late either it could just be 5 or 10 minutes but there's a chronic pattern emerging of this is happening time and time again just always feeling like you're one step behind you also put things off so when there's a new task you actually wait until day 29 or 30 to get it done rather than doing it in the first week you're also generally disorganized and one way to tell this is if you look at the inside of your bag or your drawers and you see that it just is a bomb site in there then that could be a sign now quite frequently you don't see any of those things as an issue and they're just part of your personality quirks and you need someone to get angry at you for it for you to take action to try and relieve those things and when you do that is
```

**Metadata as supplied (views, likes, comments, duration):** `15,647,532 588,271 14,808 60`

### Revised claim review

**Claim 1:** Chronic lateness (even by only 5-10 minutes) is a characteristic ADHD sign, tied to only starting to prepare when internally prompted at the last moment

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Procrastination — waiting until close to a deadline (e.g., day 29-30 of 30) to start a task rather than starting early

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** General disorganization, evidenced by messy bags/drawers

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** These patterns are often dismissed as "personality quirks" rather than recognized as a problem, until someone else reacts negatively

**Verdict: Unsupported.** Underrecognition is real; needing another person to get angry is not an established general requirement. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 9 — 7 Signs You Have ADHD

### Transcript

```text
[Music] seven signs that you have ADHD you watch Tik tocks especially wouldn't shouldn't be emotional regulation it wrong and you can't sleep very well of [Music] course concentrating in loud and forget about it you tend to lose things all the time honey have you seen my headphones uh then I was earning late
```

**Metadata as supplied (views, likes, comments, duration):** `1,178,610 26,365 1,965 40`

### Revised claim review

The supplied transcript is fragmented. Only its intelligible assertions already represented in the inventory are assessed; missing speech is not reconstructed.

**Claim 1:** Watching TikToks (implied excessively/compulsively) is a sign of ADHD

**Verdict: Unsupported.** Use of a named social-media app is not evidence sufficient to identify ADHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Emotional regulation difficulties are a sign of ADHD

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** Difficulty sleeping well is a sign of ADHD

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** Difficulty concentrating in loud/noisy environments is a sign of ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Frequently losing things (e.g., headphones)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Chronic lateness ("running late")

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **5**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **5 / 6 × 100 = 83.33%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 10 — How Caffeine Helps People With ADHD

### Transcript

```text
why does tea or coffee calm me down emotionally when I have ADHD this is super cool so you look at ADHD their minds are moving too fast I get distracted I'm thinking about this I'm thinking about this I'm hyperactive I'm fidgeting you know and what is the medication that we tend to give people who are who have ADHD stimulants wait but if they're moving too fast why am I stimulating them or more importantly what part of the brain am I stimulating what I'm stimulating with people with ADHD is the brakes I'm hyper activating the part of your brain that controls the other parts of your brain this is why tea or coffee helps people with ADHD calm down it hyper activates your frontal lobes which then control or suppress your emotional circuitry so it's kind of weird but we actually want to hyperactivate people with ADHD not slow them down I'm going to strengthen the brakes
```

**Metadata as supplied (views, likes, comments, duration):** `1,070,608 73,515 1,418 50`

### Revised claim review

**Claim 1:** People with ADHD have minds that are "moving too fast," with racing thoughts, distraction, and hyperactivity/fidgeting

**Verdict: Supported.** Mental restlessness/racing thoughts are documented associated experiences; absence from the core symptom list is not grounds for rejection. Evidence: [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Stimulant medications are the standard treatment given to people with ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Stimulant medication works by "hyperactivating the brakes" — i.e., activating the frontal lobes, which then control/suppress other brain regions (including "emotional circuitry")

**Verdict: Supported.** Accepted as an inhibitory-control metaphor. Appropriate dosing aims at improved regulation, not unlimited frontal hyperactivation. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Caffeine (tea/coffee) helps calm people with ADHD via the same "hyperactivating the frontal lobe" mechanism as prescription stimulants

**Verdict: Unsupported.** The proposed caffeine equivalence and predictable calming effect are not established. Evidence: [CAFF](https://www.mdpi.com/2076-3425/13/9/1304), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 11 — The ultimate ADHD test 🧠 #adhd

### Transcript

```text
10 things you didn't know about yourself that are almost certainly ADHD loud chewers send you into a fit of rage you don't like big spoons you don't know why but you just don't if someone asks you for a quick chat without any context you will catastrophize you will think of the worst case scenario and you won't sleep until you get some reassurance that your world isn't about to end you have a minor commitment in the afternoon so you won't be able to do anything else all

day you'll get obsessed with someone or something and disappear from friends for months at a time you've got thousands of screenshots on your phone they were well-intentioned but you never remember to look at them you struggle to clean your home but if a friend comes over suddenly cleaning is quite easy the tiniest criticism will immediately create an overwhelming feeling of anger or sadness within you you get excited when you buy a new notebook but you never use it when you achieve something

you don't feel any sense of accomplishment only a mild sense of relief that it's done
```

**Metadata as supplied (views, likes, comments, duration):** `161,488 8,682 536 70`

### Revised claim review

Several examples can occur in ADHD. They remain unsupported here because the explicit near-certain diagnostic framing is central to the claim, rather than a cautious discussion of associated experiences.

**Claim 1:** Loud chewers send you into a "fit of rage"

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** Disliking "big spoons" for no clear reason

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** Catastrophizing and needing reassurance when someone asks for a "quick chat" with no context

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** A minor afternoon commitment prevents doing anything else all day

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** Becoming obsessed with someone/something and disappearing from friends for months (hyperfocus)

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 6:** Having thousands of unviewed screenshots on your phone

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 7:** Struggling to clean alone but suddenly finding it easy when a friend visits

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 8:** Tiny criticism creates overwhelming anger or sadness

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 9:** Getting excited buying a new notebook but never using it

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 10:** Feeling no sense of accomplishment after achieving something, only relief that it's done

**Verdict: Unsupported.** The opening claims these nonspecific experiences are “almost certainly ADHD”; evidence does not justify that diagnostic inference. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **10**
- Supported: **0**; unsupported: **10**; excluded: **0**.
- Supported-claim percentage: **0 / 10 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 12 — Doctor Explains ADHD Diagnosis, criteria, and why everyone does NOT have “a little ADHD”

### Transcript

```text
Uh, not everybody has a little bit of ADHD. Here's what ADHD actually is. Diagnostic criteria, resources on how to get tested and get diagnosed and how to respond to people who kind of dismiss you when they say, "Oh, everybody has a little bit of ADHD." Just because you're distracted does not mean you have ADHD. My name's Dr. Heidi. I'm a physician and I have ADHD. For starters, I'm pulling straight from the DSM5, which is basically the guide book for all diagnosis in medicine. There's two main subtypes of ADHD: inattentive or hyperactive and impulsive. And you can have a combination of both. These symptoms are present with at least six or more in each category for at least 6 months. And you have to have a majority of these symptoms that were present before age 12. With an attentive, they don't appear to be listening. Trouble following through or following directions, difficulty organizing, reluctant to engage in activities that require sustained mental attention, easily distracted by external stimuli, even noises, senses, forgetful in daily activities, not me losing my phone while I was on the phone with somebody. And then the hyperactive type will be moving, climbing, jumping in places that are inappropriate, unable to have leisurely time. This can be one of the reasons why ADHD people gravitate toward things like drinking so much. We have a higher rates of addiction tendencies. I think a big part of this is because it allows us to wind down because otherwise we're feeling like we're on the go and driven by a motor constantly. Trouble waiting in line, interrupting or intruding or thinking you know what somebody else is going to say and cutting them off mid-con conversation. These symptoms are present in two or more settings like home, school, work, with friends. Other people are noticing this all the time. And the reason I advocate so much for comprehensive testing is because they do not occur where they're explained by another mental disorder that needs to be treated first. You can have mild, moderate, or severe. They exist on a spectrum. If this sounds like you, you can take a look at the adult self-report scale that's present online. And your doctor might offer you a test like the Connor screen or for children, they can offer things like Vanderbilt or Wesler scale. There's plenty more that you can choose from. All of this are part of a comprehensive testing evaluation. Can be really helpful in getting people access to a testing accommodations. If you're looking for more resources, whether you're a child or an adult, take a look at the CHAD website, chad. They can help you find providers in your area, get connected with different resources, and follow me if you like learning more about your ADHD brain. So the next time somebody tells you everybody has a little bit of ADHD, you can give them a list of the different ways in which this affects you personally and professionally or academically.
```

**Metadata as supplied (views, likes, comments, duration):** `4,351 296 17 127`

### Revised claim review

**Claim 1:** Not everybody has "a little bit of ADHD" — being distracted alone doesn't mean you have ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD has two main subtypes/presentations — inattentive or hyperactive-impulsive — plus a combined type

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Diagnosis requires "six or more" symptoms in a category, present for at least 6 months

**Verdict: Unsupported.** Adults aged 17+ need five symptoms; either domain may qualify. “Six ... in each” is materially incorrect as a general rule. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** A "majority" of symptoms must have been present before age 12

**Verdict: Unsupported.** Several symptoms, not a majority, must have existed before age 12. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Inattentive symptoms listed (not listening, trouble following through, disorganization, avoidance of sustained-mental-effort tasks, easily distracted, forgetful)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Hyperactive-impulsive symptoms listed (climbing/moving inappropriately, can't engage in leisure quietly, trouble waiting in line, interrupting)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** People with ADHD have higher rates of addiction/substance use tendencies (e.g., drinking)

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 8:** The reason for this substance use is that it helps "wind down" from feeling constantly driven "by a motor"

**Verdict: Unsupported.** A proposed dominant self-medication explanation is not established by the association with substance-use problems. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 9:** Symptoms must be present in two or more settings (home, school, work, with friends)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 10:** Symptoms must not be better explained by another mental disorder that needs to be treated first

**Verdict: Unsupported.** The differential-explanation criterion does not require treating every other mental disorder first. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 11:** ADHD can be mild, moderate, or severe, existing on a spectrum

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 12:** Testing tools like adult self-report scales, Conners, Vanderbilt, and Wechsler-type scales are part of comprehensive evaluation

**Verdict: Supported.** These can contribute to assessment; Wechsler measures cognitive ability and is not itself an ADHD diagnostic scale. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 13 — added from supplied transcript:** DSM-5 is the guidebook for all diagnoses in medicine.

**Verdict: Unsupported.** It classifies mental disorders, not all medical diagnoses; this spoken assertion was omitted previously. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **13**
- Supported: **8**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **8 / 13 × 100 = 61.54%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 13 — How to Get Diagnosed With ADHD

### Transcript

```text
How do you go about getting diagnosed with ADHD? The doctor sees that you have six out of the nine symptoms of inattention or six out of the nine symptoms of hyperactivity. If you're over 17 years old, then you only need five of those nine symptoms. That means you meet the diagnostic criteria and we're going to say you have ADHD. Let's look at the other end of the spectrum. There would be a lengthy interview lasting for an hour to an hour and a half. There would be several questionnaires that are not just looking at a flat rate of how many symptoms you have, but they would be standardized, possibly IQ testing. And then they could do a continuous performance test. Every time a letter flashes on the screen, you got to press a button. And then they might also look at emotional factors. If you have ADHD, there is a higher chance of having either anxiety or depression. Now, the third way to get diagnosed would probably be somewhere in between those
```

**Metadata as supplied (views, likes, comments, duration):** `15,571 212 14 60`

### Revised claim review

**Claim 1:** Diagnosis is based on having 6 out of 9 symptoms of inattention or 6 out of 9 symptoms of hyperactivity(-impulsivity)

**Verdict: Supported.** This is the childhood symptom-count component, not the whole diagnosis; the sufficiency error is assessed separately in claim 3. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** If you're over 17, you only need 5 of those 9 symptoms

**Verdict: Supported.** The exact cutoff is age 17 and older; the spoken shorthand is read in the stated child/adult comparison. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Meeting either symptom-count threshold alone means "we're going to say you have ADHD" (implying symptom count is sufficient for diagnosis)

**Verdict: Unsupported.** Count alone omits onset, duration, settings, impairment and differential assessment. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** A more thorough diagnostic approach involves a lengthy interview (roughly 1 to 1.5 hours)

**Verdict: Supported.** An interview around 90 minutes is a documented possible component; no universal fixed interview duration is required. Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 5:** Standardized questionnaires (not just raw symptom counts), possible IQ testing, and continuous performance tests (e.g., pressing a button when a letter flashes) may be used

**Verdict: Supported.** Possible adjuncts, not necessary or independently diagnostic tests. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 6:** People with ADHD have a higher chance of also having anxiety or depression

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **5**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **5 / 6 × 100 = 83.33%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 14 — Dangers of Untreated ADHD

### Transcript

```text
let's talk about ADHD when it is left untreated it has bad consequences and when we talk about medicine you always want to know what are the side effects but you also want to ask the question well what are the side effects of not treating ADHD so the Hallmark symptoms are short attention span but not for everything the second one is they're easily distracted it's like the world comes at them too fast the third one is they tend to be disorganized they tend to procrastinate they don't do things until someone's mad at them to get it done and they tend to have impulse control issues so the first thing if you have someone who has ADD it's focus on getting their diet healthy magnesium can help zinc can help omega-3 fatty acids can help but if it doesn't work I will use the medicine because left untreated there's serious problems with addiction School failure bankruptcy and so on
```

**Metadata as supplied (views, likes, comments, duration):** `263,202 8,280 349 60`

### Revised claim review

**Claim 1:** Untreated ADHD has "bad consequences" and it's worth asking about the "side effects" of not treating it

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Hallmark symptom: short attention span, "but not for everything"

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Easily distracted — "the world comes at them too fast"

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Tend to be disorganized and procrastinate, not doing things "until someone's mad at them"

**Verdict: Unsupported.** Organization/procrastination are supported; the stated dependence on someone becoming angry is not. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Tend to have impulse control issues

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** First step should be focusing on diet, with magnesium, zinc, and omega-3 fatty acids specifically named as helpful

**Verdict: Unsupported.** Healthy diet advice does not establish the supplement package as first-line ADHD treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** If diet/supplements don't work, medication should then be used

**Verdict: Unsupported.** Medication need not await failed supplement treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 8:** Untreated ADHD is associated with serious problems including addiction, school failure, and financial/occupational difficulties (e.g., "bankruptcy")

**Verdict: Supported.** The earlier rejection was incorrect: these are documented associations, not claims that every untreated person experiences them. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **5**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **5 / 8 × 100 = 62.50%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 15 — ADHD Explained in 60 seconds

### Transcript

```text
Ever heard people say ADHD is just about being distracted? Well, that's only scratching the surface. ADHD or attention deficit hyperactivity disorder is a neurodedevelopmental condition that affects focus, impulse control, and emotional regulation. It comes in three types: inattentive, losing track of details, forgetfulness, zoning out, hyperactive impulsive, restlessness, talking a lot, acting before thinking, and combined, a mix of both. It's not about laziness. It's about how the brain manages dopamine, the chemical linked to motivation and reward. Here's something mind-blowing. Rates of ADHD diagnosis have nearly doubled worldwide in the past 20 years, and experts believe it's not because more people suddenly have it, but because awareness and recognition are finally catching up, and treatment, it's no longer just medication. Research is now exploring brain training, digital therapies, lifestyle interventions, and even video games designed to improve attention. One of which is FDA approved for kids. So next time you hear ADHD, remember it's not just about distraction.
```

**Metadata as supplied (views, likes, comments, duration):** `618,665 25,002 1,038 60`

### Revised claim review

**Claim 1:** ADHD is "just about being distracted" is an oversimplification — it's more than that

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD is a neurodevelopmental condition affecting focus, impulse control, and emotional regulation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** ADHD comes in three types — inattentive, hyperactive-impulsive, and combined

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Inattentive type involves losing track of details, forgetfulness, zoning out

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Hyperactive-impulsive type involves restlessness, talking a lot, acting before thinking

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** "It's not about laziness. It's about how the brain manages dopamine, the chemical linked to motivation and reward"

**Verdict: Unsupported.** Dopamine is involved, but this presents a single-mechanism explanation of a heterogeneous disorder. Evidence: [STIM](https://www.nature.com/articles/1301164), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 7:** Rates of ADHD diagnosis have "nearly doubled worldwide" in the past 20 years

**Verdict: Unsupported.** No adequate worldwide, comparable 20-year doubling estimate was identified. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 8:** The rise is attributed to improved awareness/recognition rather than more people actually having the condition

**Verdict: Supported.** Retained for the broad role of recognition/diagnostic practices; this does not validate the numerical claim in 7. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 9:** Treatment is no longer just medication — research is exploring brain training, digital therapies, lifestyle interventions, and video games for attention, one of which is FDA-approved for kids

**Verdict: Supported.** The broad authorization claim is supported; technically this is FDA marketing authorization for a device, not proof of a cure. Evidence: [DIGI](https://www.psychiatry.org/news-room/apa-blogs/fda-approves-first-game-based-therapy-for-adhd), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **7**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **7 / 9 × 100 = 77.78%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 16 — 4 Essential Criteria For ADHD Diagnosis #adhd

### Transcript

```text
here are four essential criteria you need to fulfill in order for an ADHD diagnosis number one your inattentive hyperactive impulsive symptoms must be present before the age of 12 years old number two your ADHD symptoms must be present in more than two or more different settings so whether it's at home whether it's at school whether it's at work or other activities number three there is clear evidence that your ADHD symptoms have a significant impact upon the quality of your life whether it be at work whether it be at home in your personal life or in your school or academic settings four symptoms aren't better explained by another mental disorder such as a disorder anxiety disorder or personality disorder
```

**Metadata as supplied (views, likes, comments, duration):** `219 5 0 59`

### Revised claim review

**Claim 1:** Inattentive/hyperactive-impulsive symptoms must be present before age 12

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD symptoms must be present in two or more different settings (home, school, work, other activities)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** There must be clear evidence that symptoms significantly impact quality of life (work, home, personal life, school/academic settings)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Symptoms aren't better explained by another mental disorder, such as an anxiety disorder or personality disorder

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 17 — An ADHD Diagnosis Does Not Mean Medication

### Transcript

```text
Hi I'm Rick Green, I'm a comedian who has a science degree and attention deficit hyperactivity disorder (ADHD). In the videos that I'm making for my YouTube channel Rick has ADHD I often Advocate and recommend getting properly diagnosed, now what I hear from people is two things, one is I couldn't wait to get diagnosed and when I was diagnosed everything started to make sense. Okay there's two or three responses, another response is I really would like to find out but I'm waiting because there's a long waiting line, and I've done a video about that as well. Then there is the I'm pretty sure I have it, I've read all the checklists, took all the online screener tests and so on, but I don't want to have to take drugs, so I'm not going to get diagnosed. So uh, I don't know where you live but nobody can force you to take a medication for anything, if you had a fatal disease and there was medication for it you don't have to take it, they'd recommend you take it, and you might want to learn more and decide if you want to take it. But with ADHD medication despite its wonderful track record most people I know who've tried it, stick with it, it's been a life changer, and some people I know have tried it, didn't like it, and stopped taking it, and that's the thing, you could try it, because I was reluctant, I have to tell you I don't drink, I never smoked any of that. So my friends all did, that that was fun, but I didn't take drugs. So the idea of taking a drug, a medication, that worried me, I was frightened that I was going to turn into a zombie or something, and it actually just made me calmer, but I wasn't zombified. I actually just got more done with less stress and it turned down that noise of the five radio stations that are playing in my head way down so I could sit and actually do taxes, which was shocking to me, shocking, I just did years worth of taxes in one day. So you don't have to take medication, you don't have to do anything, but once you know for sure what's going on believe me you are going to want to try different strategies and tools and techniques, and apps, and all of these things that are going to make life so much easier.
```

**Metadata as supplied (views, likes, comments, duration):** `2,877 298 10 142`

### Revised claim review

**Claim 1:** Getting properly diagnosed with ADHD is worthwhile/recommended

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Nobody can be forced to take medication for any condition, including ADHD; treatment is a personal choice even for serious/fatal conditions

**Verdict: Unsupported.** The unrestricted “nobody ... for anything” assertion overlooks recognized consent exceptions. Evidence: [CONSENT](https://www.nhs.uk/tests-and-treatments/consent-to-treatment/).

**Claim 3 — clarified extraction:** ADHD medication has evidence of benefit; the speaker also recounts mixed experiences among people he knows.

*Original annotation wording:* ADHD medication has a "wonderful track record" and most people who try it stick with it because it's "a life changer"; some try it, don't like it, and stop

**Verdict: Supported.** The general efficacy assertion is supported. “Most people I know” is explicitly anecdotal and is excluded from population-level scoring. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** The speaker's personal experience: medication made him calmer, not "zombified," improved focus/reduced stress, and let him complete tasks (doing years of taxes in one day)

**Verdict: Excluded from scoring.** Personal treatment experience remains excluded.

**Claim 5:** You don't have to take medication — you can try different strategies, tools, techniques, and apps instead

**Verdict: Supported.** Diagnosis does not oblige medication; evidence-based non-drug approaches may be discussed. This does not validate every unnamed app. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 18 — How to get an ADHD diagnosis

### Transcript

```text
[Music] okay sorry about that but if you're watching this video there's a chance you might have adhd so i had to grab your attention right away one of the most common questions that seems to be popping up in the comments section how do i know if i have adhd and what do i do to get properly diagnosed some of the more skeptical folks in the room are thinking hey man doesn't those symptoms don't those just kind of apply to everybody most people do experience these kinds of symptoms to like a minor degree but the difference with adhd is that it's to a major degree it significantly impacts your life somewhere along the line you're going to need to be evaluated now this can come from a psychologist like myself who can give you a psychological evaluation or from a primary medical provider who can do the same thing i wouldn't say i'm just biased because i'm a psychologist but i would say the best kind of evaluation is going to come from a psychologist they're going to take a comprehensive view of what's going on they're going to screen out for anxiety depression post traumatic stress all those kinds of things and you want that you want a comprehensive evaluation check out this website right here psychologytoday.com and you'll be able to find a psychologist in your area by using the filters i'm dr brian i specialize in adhd like and follow this video for more tips and tricks like this see you later
```

**Metadata as supplied (views, likes, comments, duration):** `903 62 5 60`

### Revised claim review

**Claim 1:** Many people wonder how to know if they have ADHD and how to get properly diagnosed (framing/context)

**Verdict: Excluded from scoring.** Introductory framing, not an independent clinical assertion.

**Claim 2:** Some skeptics think ADHD symptoms "apply to everybody"; most people experience these symptoms to a "minor degree," but ADHD involves the same symptoms to a "major degree" that significantly impacts life

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Diagnosis requires evaluation, which can come from a psychologist or a primary medical provider

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 4:** A comprehensive evaluation should screen out other conditions like anxiety, depression, and PTSD

**Verdict: Supported.** Assess alternatives and coexisting conditions; their mere presence does not exclude ADHD. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 5:** Psychologists provide the "best kind" of evaluation compared to other providers (framed as a personal opinion, with an acknowledgment of possible bias)

**Verdict: Excluded from scoring.** An expressly personal, possibly biased preference about evaluators, not a generalized comparative evidence claim.

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **2**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 19 — ADHD Diagnosis Dilemma

### Transcript

```text
so when diagnosing as as a psychologist I feel that in adult ADHD assessments there's a lot of self-report so because someone is already coming from a lot of information and people like I have talked to ask questions what they have read on Google and they come with a diagnosis that they know that they feel that they have ADHD and they just want to prove that they have ADHD so how do how does one go about dealing with that how does one make sure that the diagnosis is correct and their own biasness is not coming into play so there are criteria we need to look at what what see for somebody to be diagnosed there are rating skills and of there there's a clinical interview
```

**Metadata as supplied (views, likes, comments, duration):** `117 7 0 51`

### Revised claim review

**Claim 1:** Adult ADHD assessments often involve significant self-report, and patients may come pre-informed (e.g., from online research) and already convinced they have ADHD, seeking confirmation

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Proper diagnosis requires looking at specific criteria, using rating scales, and conducting a clinical interview (to guard against self-report bias)

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 20 — 12 potential symptoms of ADHD in adults #shorts

### Transcript

```text
here are 12 potential symptoms of ADHD in adults acting quickly without properly thinking things through disorganization and problems prioritizing poor time management skills problems focusing on a task trouble multitasking excessive activity or restlessness poor planning getting easily upset or frustrated at seemingly minor challenges frequent mood swings problems following tasks through and completing them having a quick temper and trouble coping with St
```

**Metadata as supplied (views, likes, comments, duration):** `103,651 2,179 57 31`

### Revised claim review

These are presented as potential experiences. Emotional/stress features are associated problems, not extra DSM symptom-count criteria.

**Claim 1:** Acting quickly without properly thinking things through

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Disorganization and problems prioritizing

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Poor time management skills

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Problems focusing on a task

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Trouble multitasking

**Verdict: Supported.** Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 6:** Excessive activity or restlessness

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Poor planning

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8:** Getting easily upset or frustrated at seemingly minor challenges

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 9:** Frequent mood swings

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 10:** Problems following tasks through and completing them

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 11:** Having a quick temper

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 12:** Trouble coping with stress (cut off in transcript, but discernible)

**Verdict: Supported.** Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

### Revised result

- Eligible fact-checkable claims: **12**
- Supported: **12**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **12 / 12 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 21 — 10 signs of ADHD in women, FULL VIDEO on channel. #adhd #adhdtiktok

### Transcript

```text
here are 10 symptoms of ADHD in women that often get overlooked or misdiagnosed number one daydreaming frequently zoning out or getting lost in thoughts making it difficult to stay focused on task or conversations two chronic perfectionism a constant drive to be Flawless in everything leading to excessive time spent on details and a fear of making mistakes number three excessive talking talking more than usual sometimes without realizing it which can lead to interrupting others or feeling like we just can't stop number four low self self esteem a lack of confidence in abilities often stemming from comparing ourselves to others or feeling inadequate due to the challenges the ADHD brings number five physical restlessness an ongoing feeling of needing to move fidget or be physically active even in situations where it's not socially acceptable or convenient number six chronic forgetfulness constantly forgetting appointments deadlines or tasks even when they're important often leading to feelings of disorganization number seven difficulty maintaining friendships trouble keeping friendships due to impulsive behaviors misso cues or difficulties with emotion regulation leading to misunderstandings number eight emotional impulsivity reacting quickly and intensely to emotions without thinking leading to outbursts or regrets after the fact number nine rejection sensitivity an intense fear of being rejected or criticized can cause excessive anxiety in social situations or lead us to do overcompensating behaviors and number 10 chronic overwhelm feeling constantly overwhelmed by tasks responsibilities and emotions leading to burnout or difficulty managing everyday demands
```

**Metadata as supplied (views, likes, comments, duration):** `146,338 7,306 238 100`

### Revised claim review

Read as a list of possible overlooked experiences in women, not as ten mandatory diagnostic symptoms. The article evidence does not establish that every woman has these features.

**Claim 1:** Daydreaming/zoning out, difficulty staying focused on tasks or conversations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Chronic perfectionism, excessive time on details, fear of mistakes

**Verdict: Supported.** Perfectionism can be compensatory; the previous rejection solely for being outside core criteria was too narrow. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 3:** Excessive talking, sometimes without realizing it, leading to interrupting others

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Low self-esteem stemming from comparing oneself to others or feeling inadequate due to ADHD challenges

**Verdict: Supported.** Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 5:** Physical restlessness, needing to move/fidget even when not appropriate

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Chronic forgetfulness — forgetting appointments, deadlines, tasks

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Difficulty maintaining friendships due to impulsive behavior, missed social cues, or emotion-regulation difficulties

**Verdict: Supported.** Associated relationship difficulties are within the thesis claim scope. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 8:** Emotional impulsivity — reacting quickly/intensely to emotions, leading to outbursts or regret

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 9:** Rejection sensitivity — intense fear of rejection/criticism causing social anxiety or overcompensation

**Verdict: Supported.** Criticism/rejection sensitivity has supporting evidence; this is not an assertion of a separate universally present RSD disorder. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [JUSTICE2](https://pubmed.ncbi.nlm.nih.gov/24878677/).

**Claim 10:** Chronic overwhelm — feeling overwhelmed by tasks/responsibilities/emotions, leading to burnout or difficulty managing daily demands

**Verdict: Supported.** Overwhelm and exhaustion are documented associated difficulties; not a universal course or a new diagnostic criterion. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **10**
- Supported: **10**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **10 / 10 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 22 — Symptoms of ADHD in women #adhd #doctor #shorts #mentalhealth #therapy

### Transcript

```text
let's talk symptoms of adhd in women women with adhd tend to have lower self-esteem they're more likely to be daydreamers they tend to fidget in their chair a lot they might deal with odd eating habits or binge eating they're more likely to be labeled as moody or too sensitive they tend to have difficulty with time management and organization they tend to be more sensitive to rejection and criticism and they're more likely to be anxious and have a serious case of imposter syndrome
```

**Metadata as supplied (views, likes, comments, duration):** `473,399 24,831 726 30`

### Revised claim review

**Claim 1:** Women with ADHD tend to have lower self-esteem

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** More likely to be daydreamers

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Tend to fidget in their chair a lot

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** May deal with odd eating habits or binge eating

**Verdict: Supported.** Evidence: [EATING](https://pubmed.ncbi.nlm.nih.gov/27859581/).

**Claim 5:** More likely to be labeled as "moody" or "too sensitive"

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 6:** Difficulty with time management and organization

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** More sensitive to rejection and criticism

**Verdict: Supported.** The clinical association is supported despite not being a core diagnostic criterion. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 8:** More likely to be anxious and have a "serious case of imposter syndrome"

**Verdict: Unsupported.** Anxiety is associated; the added broad claim of serious impostor syndrome is not sufficiently established. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **7**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **7 / 8 × 100 = 87.50%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 23 — Natural Ways to Help ADHD | Dr. Daniel Amen

### Transcript

```text
what about natural ways to help add often a higher protein lower simple carbohydrate diet exercise can work magnesium has been shown to be helpful as has thinning ashwagandha rhodiola l-tyrosine so there are a number of supplements that can help but you know the most important thing you can do is be in a job you love uh study something you love because love is a stimulant drug
```

**Metadata as supplied (views, likes, comments, duration):** `1,168,024 51,589 1,014 40`

### Revised claim review

The ambiguous spoken token “thinning” is retained in the transcript and is not silently changed to a supplement name.

**Claim 1:** A higher-protein, lower-simple-carbohydrate diet can help ADHD

**Verdict: Unsupported.** A generally healthy diet is distinct from evidence that this specific macronutrient prescription treats ADHD. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 2:** Exercise can work for ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 3:** Magnesium has been shown to be helpful for ADHD

**Verdict: Unsupported.** Evidence is too limited for this unqualified treatment recommendation. Evidence: [MAG](https://pubmed.ncbi.nlm.nih.gov/23808779/).

**Claim 4:** Ashwagandha helps ADHD

**Verdict: Unsupported.** A preliminary mild-pediatric-ADHD trial exists; general established efficacy is not demonstrated. Evidence: [ASH](https://pubmed.ncbi.nlm.nih.gov/42602386/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 5:** Rhodiola helps ADHD

**Verdict: Unsupported.** A registered study is not evidence of clinical benefit. Evidence: [RHOD](https://clinicaltrials.gov/study/NCT02737020).

**Claim 6:** L-tyrosine helps ADHD

**Verdict: Unsupported.** Sustained clinical benefit is not established. Evidence: [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

**Claim 7:** Being in a job/study you love helps because "love is a stimulant drug" (implying engagement/stimulation reduces ADHD symptoms)

**Verdict: Excluded from scoring.** A preference-based recommendation with an explicit metaphor, not a separate testable claim that love is a medication.

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **1**; unsupported: **5**; excluded: **1**.
- Supported-claim percentage: **1 / 6 × 100 = 16.67%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 24 — 11 ways to spot ADHD in women 💚 #adhd #neurodivergent

### Transcript

```text
11 ways to spot ADHD in women they'll get obsessed with someone or something and disappear from friends for months at a time when they achieve something they won't feel any sense of accomplishment only a mild sense of relief that it's done if they have a minor commitment later on today they won't be able to relax and they'll be stuck in waiting mode all day they have a really really strong sense of justice and fairness which is why they react so strongly when people do mean things the hyperactivity is in their heads it's internalized it's like 10 squirrels barreling around on speed up there they were never physically hyperactive so the doctor misdiagnosed them with an anxiety disorder waiting for a slow talker to finish their sentence is excruciatingly painful for them because they've already guessed the end of it in the first few seconds they're highly driven and overachieving but they're also chronically overwhelmed and always on the drink of burnout they'll sit on their best friend's couch once a month to give them moral support so they can clean their house they'll excitedly call people but then ignore their attempts to call them back because the dopamine has left their body they'll often try and Google something but then forget what they were about to Google so they'll check their recent apps to see what triggered the thought but then they forget all about Google they'll get home after a long day of masking try to relax on the sofa but it's impossible because they'll start overthinking every social interaction they've had that day and they'll say things to themselves like why did I say that stupid thing that person must hate me now
```

**Metadata as supplied (views, likes, comments, duration):** `478,389 39,412 1,548 103`

### Revised claim review

**Claim 1:** They get obsessed with someone/something and disappear from friends for months at a time (hyperfocus)

**Verdict: Unsupported.** The months-long disappearance pattern is not established as an identifying ADHD feature. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** When they achieve something they feel no accomplishment, only relief it's done

**Verdict: Unsupported.** The asserted absence of accomplishment is unsubstantiated as a general rule. Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** If they have a minor commitment later today, they can't relax and are stuck in "waiting mode" all day

**Verdict: Unsupported.** Organizational difficulty does not establish this whole-day waiting rule. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** They have a strong sense of justice and fairness, reacting strongly when people do mean things

**Verdict: Supported.** Limited research supports justice sensitivity as an association, not a diagnostic marker or universal moral advantage. Evidence: [JUSTICE](https://pubmed.ncbi.nlm.nih.gov/23223013/), [JUSTICE2](https://pubmed.ncbi.nlm.nih.gov/24878677/).

**Claim 5:** Their hyperactivity is internalized ("in their heads"), they were never physically hyperactive, and were misdiagnosed with an anxiety disorder

**Verdict: Unsupported.** Internal restlessness and misdiagnosis occur; “never physically hyperactive” does not hold as a general female profile. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

**Claim 6:** Waiting for a slow talker is excruciating because they've already guessed the end of the sentence

**Verdict: Unsupported.** The asserted predictive ability and specific pain mechanism are unsubstantiated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** They're highly driven and overachieving, but chronically overwhelmed and near burnout

**Verdict: Unsupported.** The fixed overachiever/near-burnout profile is not generalizable. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 8:** They'll sit on their best friend's couch once a month to give moral support so the friend can clean

**Verdict: Unsupported.** A specific monthly friendship routine is not an established clinical feature. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 9:** They excitedly call people, then ignore callbacks because "the dopamine has left their body"

**Verdict: Unsupported.** Dopamine does not leave the body when a callback is ignored. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 10:** They'll try to Google something, forget what it was, and check recent apps to find the trigger

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 11:** After a day of masking, they overthink every social interaction and engage in harsh self-talk ("that person must hate me now")

**Verdict: Unsupported.** Masking and criticism distress are documented; the inevitable every-interaction rumination sequence is not. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **11**
- Supported: **2**; unsupported: **9**; excluded: **0**.
- Supported-claim percentage: **2 / 11 × 100 = 18.18%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 25 — 3 Underrated symptoms of #ADHD

### Transcript

```text
i'm a psychiatrist let's talk about three underrated symptoms of adhd the first is time management problems some people with adhd have what we refer to as time blindness which just means that it's very difficult for them to tell how much time has passed or how much time they might need to complete a certain task even if it's a task that they do often this can result in frequently being late or even way too early to things they may also put tasks off thinking that they may be able to complete them faster than they actually can underrated symptom of adhd number two is rejection sensitive dysphoria rejection sensitive dysphoria refers to the fact that the nervous system of someone with adhd is highly attuned to any source of rejection or criticism it can become almost physically painful an underrated symptom number three difficulty with managing overeating and binge eating
```

**Metadata as supplied (views, likes, comments, duration):** `540,794 30,091 850 60`

### Revised claim review

**Claim 1:** Time management problems / "time blindness" — difficulty telling how much time has passed or is needed for a task, resulting in being late or too early, and underestimating task duration

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 2:** Rejection sensitive dysphoria — nervous system highly attuned to rejection/criticism, described as an underrated ADHD symptom that can be "almost physically painful"

**Verdict: Unsupported.** Rejection distress is documented, but the asserted general nervous-system explanation and established ADHD symptom status of RSD exceed the evidence. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** Difficulty managing overeating and binge eating as an underrated ADHD symptom

**Verdict: Supported.** Associated binge-eating difficulties fall within the thesis scope. They are not additional DSM criteria. Evidence: [EATING](https://pubmed.ncbi.nlm.nih.gov/27859581/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 26 — These ADHD-Like Struggles Aren’t Always ADHD #shorts

### Transcript

```text
These ADHD-like struggles are always ADHD. You lose the threat in meeting. You can't start until the deadline is breathing down your neck and switching task feels much harder than it should. You start wondering, do I have ADHD? Maybe, but stress, short sleep, low mood, pain, medication effects, or just simply carrying too much can also make your executive skills less reliable. ADHD is a developmental condition, so the pattern usually starts in childhood and affects more than one part of your life. But sometimes adult responsibilities expose a pattern that you've been compensating for all along. So, look at the timeline. Has this followed you since childhood? Does it show up at work, at home, and in daily life? Or did it begin when your workload, your health, or your sleep changed? One overload season doesn't diagnose ADHD, but a lifelong pattern may deserve a closer evaluation.
```

**Metadata as supplied (views, likes, comments, duration):** `15,826 1,120 28 54`

### Revised claim review

The opening contains “always ADHD”, contradicted by the following explicit “maybe” and alternative explanations. The self-correcting discussion is assessed in context; no word is silently repaired.

**Claim 1:** Losing the thread in meetings, being unable to start tasks until deadline pressure, and difficulty switching tasks can occur without ADHD being the cause

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** Stress, short sleep, low mood, pain, medication effects, or being overloaded can make executive skills less reliable (mimicking ADHD)

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 3:** ADHD is a developmental condition, so the pattern usually starts in childhood and affects more than one part of life

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Adult responsibilities can expose a lifelong pattern the person had been compensating for

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 5:** To evaluate whether it's ADHD, look at the timeline — whether it followed you since childhood and shows up at work, home, and daily life, versus only starting when workload/health/sleep changed

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 6:** One overload season doesn't diagnose ADHD, but a lifelong pattern may deserve closer evaluation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 27 — How to Diagnose ADHD

### Transcript

```text
[music] Finally, a scan that can detect ADHD. No, that's not a thing. Let's talk about why. Hi, I'm Dr. Mona. I make sense of all things child development, parenting, and health. So, if you're not already following, click that follow button. Now, I get it. When you're concerned about your child's development, or behavior, the idea of one quick test that gives you answers sounds amazing. But ADHD isn't something a machine can pick up. If there were, mainstream medicine would have incorporated it into practice. And especially as a DO or osteopathic physician, I'm always curious about the mind body connection. But ADHD is a neurodedevelopmental condition, not stress stuck in the nervous system. The brain is wired a little differently, especially in the areas that control attention, activity level, and impulse control. And here's something every parent should know. Most experts don't diagnose ADHD before age four. And that child in the video definitely looks under four. Why? Because toddlers are still developing. It's neurotypical at 2 or 3 years old to be distractable, impulsive, and full of energy. That's development, not ADHD. So, when you see someone offering a neurological insight scan to find the real cause of ADHD behaviors, here's what that really is. These scans measure things like muscle tension, skin temperature, and heart rate patterns. None of that can tell you anything about ADHD, attention, or brain wiring. They look fancy and medical, but they don't diagnose anything. And if your active child is running around, which many are, it can pick up stress that is typical for an active kid. Think of them as a stress snapshot, not a map of your child's wiring or their brain. And worse, they're often marketed to worried parents. Parents who just want answers when no legitimate medical organization recognizes these scans as diagnostic for anything. Here's what we actually know about ADHD. ADHD often runs in families. It shows up in more than one setting, at home, school, or social situations. Diagnosis is based on history and patterns and not machines or marketing. So, when you see a colorful scan claiming to find the root cause of ADHD, take it as a red flag. What your child needs isn't a gimmick. It's understanding, patience, and an evaluation by people who actually study child development. ADHD isn't about broken wiring. It's about different wiring. And when kids get the right support, they can thrive.
```

**Metadata as supplied (views, likes, comments, duration):** `9,124 380 11 147`

### Revised claim review

**Claim 1:** No scan/machine can detect or diagnose ADHD

**Verdict: Supported.** No routine scan independently diagnoses ADHD; validated task-based adjuncts are a different matter. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** ADHD is a neurodevelopmental condition involving different brain wiring in areas controlling attention, activity level, and impulse control (not "stress stuck in the nervous system")

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Most experts don't diagnose ADHD before age 4

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 4:** It's neurotypical for 2-3 year olds to be distractible, impulsive, and full of energy — that's development, not ADHD

**Verdict: Supported.** Ordinary toddler activity is not itself ADHD; this does not rule out clinically exceptional early presentations. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 5:** The described "neurological insight" scans (measuring muscle tension, skin temperature, heart rate) cannot tell you anything about ADHD, attention, or brain wiring

**Verdict: Supported.** Supported in the intended diagnostic sense; physiological measures can record physiological activity without establishing ADHD. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 6:** No legitimate medical organization recognizes these scans as diagnostic for ADHD

**Verdict: Supported.** Restricted to the advertised ADHD diagnostic use, not a claim that temperature/heart-rate measurements have no medical use. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 7:** ADHD often runs in families

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 8:** ADHD shows up in more than one setting — home, school, or social situations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 9:** Diagnosis is based on history and patterns, not machines or marketing

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **9**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **9 / 9 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 28 — Doctors have to BE CAREFUL with ADHD Diagnosis

### Transcript

```text
listen I've been to college we know what we know what like Adderall other stimulus exactly yeah there's High concerns that it can be um diverged look I have a friend and he has ADHD um does he really does he not I don't know I'm not his doctor um I I can't say for sure right but he is diagnosed by somebody receiving at all on a monthly basis and he never takes it he just sells it and it's kind of like a Lifeline for him um so I do understand that there's stuff like that going on we always have to be vigilant that we're not over medicating our children especially with these changing DSM criteria and I know you kind of mentioned the ADHD one but that's one where the criteria has changed a whole bunch in the past several um decades right the criteria has gotten softer it's easier to diagnose ADHD now
```

**Metadata as supplied (views, likes, comments, duration):** `1,812 27 0 44`

### Revised claim review

**Claim 1:** Stimulant medications like Adderall carry high concerns around diversion (being sold/misused rather than taken as prescribed)

**Verdict: Supported.** Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 2:** Doctors/parents always have to be vigilant about not over-medicating children with ADHD

**Verdict: Excluded from scoring.** A general prudential recommendation rather than an independent ADHD efficacy or prevalence assertion.

**Claim 3:** The DSM criteria for ADHD have changed a lot over the past several decades

**Verdict: Supported.** Evidence: [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 4:** The criteria have gotten "softer," making ADHD easier to diagnose now

**Verdict: Supported.** Broadened age/count criteria support easier eligibility for some people; “softer” is evaluative language, not proof of invalid diagnoses. Evidence: [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 29 — The rate of ADHD diagnosis has more than doubled since 2020. WHY?

### Transcript

```text
fun fact the rate of adult diagnosis of ADHD has more than doubled since 2020 now we all know what happened to 2020 no need to go back there but what would make that year specific in terms of this increased rate of diagnosis because that was the year when everybody's life all of our structure and routines and habits got upended and we had to recreate life from scratch well a lot of us did anyways and one thing to know about ADHD is that is really hard to make transitions either long-term transitions like we all had to deal with over the course of the pandemic but also small transitions that can happen at any point in the day like turning off your computer and transitioning from work brain to home brain or transitioning from what you're looking at on a screen to your little kid who is trying to get your attention that task switching is really difficult for adhders so you can see now why 2020 was the big Reckoning for adults with ADHD to finally get that diagnosis
```

**Metadata as supplied (views, likes, comments, duration):** `1,472 137 6 59`

### Revised claim review

**Claim 1:** The rate of adult ADHD diagnosis has more than doubled since 2020

**Verdict: Unsupported.** No population, denominator or endpoint is supplied; the claimed post-2020 doubling is not substantiated. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 2:** 2020's disruption of structure, routines, and habits (the pandemic) is what specifically drove this increase in diagnoses

**Verdict: Unsupported.** A plausible contributor is presented as the explanation of an unverified trend. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 3:** People with ADHD have significant difficulty with transitions — both long-term life transitions and small everyday transitions (e.g., switching from "work brain" to "home brain," or shifting attention from a screen to a person)

**Verdict: Supported.** Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 4:** Task-switching difficulty explains why 2020 was a "big reckoning" leading many adults with ADHD to finally get diagnosed

**Verdict: Unsupported.** Task-switching difficulty does not establish population-level diagnostic causation. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 30 — Diagnostic Criteria ADHD #adhd

### Transcript

```text
this is the diagnostic criteria for ADHD in the UK so there are two potential presentations of ADHD in attentive type and hyperactive and impulsive type and within each section there are a list of diagnostic criteria in the inattentive type it's things like being unable to complete tasks struggling to follow verbal instructions losing things in the hyperactive and impulsive type it's things like talking a lot struggling to wait your turn in a queue being unable to sit still even in a quiet place where you would be expected to sit still now if you are to be diagnosed with one of those presentations you need to tick six of those different traits within that section to get that presentation diagnosis if you tick six within both of those sections you would be diagnosed like me with combined type which means that you have both presentations and in addition if you are an adult it needs to be considered to have a moderate impact on your life that is that you might struggle with things like keeping a job maintaining relationships
```

**Metadata as supplied (views, likes, comments, duration):** `26,800 1,581 39 58`

### Revised claim review

**Claim 1:** There are two potential presentations of ADHD — inattentive type and hyperactive/impulsive type

**Verdict: Supported.** The combined presentation is explicitly included later, so this is understood as two symptom domains. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Inattentive-type criteria include things like being unable to complete tasks, struggling to follow verbal instructions, and losing things

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Hyperactive/impulsive-type criteria include talking a lot, struggling to wait your turn in a queue, and being unable to sit still even where expected to

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** You need to "tick six" traits within a section to receive that presentation's diagnosis

**Verdict: Unsupported.** Five symptoms apply at age 17+; counts are not the whole assessment. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Meeting six criteria in both sections results in a "combined type" diagnosis, meaning both presentations are present

**Verdict: Unsupported.** The same age-threshold error applies to the combined presentation. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** If you are an adult, it needs to be considered to have at least a moderate impact on your life (e.g., struggling to keep a job or maintain relationships)

**Verdict: Supported.** This corresponds to the specified UK guideline context. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **4**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **4 / 6 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 31 — If You Struggle With ADHD Try These 5 Things

### Transcript

```text
Five things I would recommend if you struggle with ADHD, take our ADD type test because what I've learned is ADD like depression, like anxiety, it's not one thing. Stop giving everybody stimulants who have ADD, that's why they have a bad reputation. For the right brain, they're miraculous. For the wrong brain, they're a nightmare. Um, as a psychiatrist for ADHD, I'd stop medicating with alcohol and marijuana is both steal your dopamine. I would limit gadgets and video games because they steal your dopamine. I would exercise that boost dopamine. I'd be on a higher protein, lower simple carbohydrate diet. And I might try elyroine because it helps to boost dopamine.
```

**Metadata as supplied (views, likes, comments, duration):** `11,650 580 13 58`

### Revised claim review

**Claim 1:** ADD/ADHD "is not one thing" like depression or anxiety, implying distinct brain "types" that his own ADD type test can identify

**Verdict: Unsupported.** Heterogeneity is real, but the promoted brain-type test is not validated by that fact. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** Stimulants shouldn't be given to everyone with ADD — "for the right brain they're miraculous, for the wrong brain they're a nightmare," which is why stimulants have a bad reputation

**Verdict: Unsupported.** Individual prescribing is appropriate; the advertised right/wrong brain-type rule is unsubstantiated. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Stop "medicating" ADHD with alcohol and marijuana because they "steal your dopamine"

**Verdict: Unsupported.** The recommendation against self-medication does not validate “stealing dopamine”. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Limit gadgets and video games because they "steal your dopamine"

**Verdict: Unsupported.** The dopamine-depletion account is unsubstantiated. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Exercise should be recommended for ADHD (boosts dopamine)

**Verdict: Supported.** The adjunctive exercise recommendation is supported; dopamine is a proposed contributor, not a guaranteed quantified mechanism. Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 6:** A higher-protein, lower-simple-carbohydrate diet is recommended

**Verdict: Unsupported.** This particular macronutrient regimen is not established treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 7:** L-tyrosine ("elyroine") helps because it boosts dopamine

**Verdict: Unsupported.** The earlier inventory interpreted an ambiguous token as L-tyrosine. That identification is not independently verified; even under that reading sustained ADHD efficacy is unestablished. Evidence: [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **1**; unsupported: **6**; excluded: **0**.
- Supported-claim percentage: **1 / 7 × 100 = 14.29%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 32 — Do You Really Have ADHD? A Psychiatrist Breaks Down the Official Criteria

### Transcript

```text
Let me go through the official formal criteria as far as diagnosing ADHD. Often fails to give close attention to details or makes careless mistakes in school work, work or other activities. Often has trouble holding attention on task tasks or play activities. Often does not seem to listen when spoken to directly. often does not follow through on instructions and fails to finish schoolwork, chores, or duties in the workplace. Often has trouble organizing tasks and activities. Often avoids, dislikes, or is reluctant to do tasks that require mental effort over a long period of time. Often loses things necessary for tasks and activities. keys, wallet, cell phone, pencils, tools, books, easily distractable and often forgetful in daily activities. Now, these are the attent inattentive symptoms. There's also hyperactive symptoms. You mentioned some of them. Inability to sit still, being fidgety. Now, question for you. Part of the diagnostic criteria is that some of these symptoms are present prior to the age of 12 years old. Which then gets us to the question of is adult onset ADHD a
```

**Metadata as supplied (views, likes, comments, duration):** `2,107 28 1 92`

### Revised claim review

**Claim 1:** Often fails to give close attention to details or makes careless mistakes in schoolwork, work, or other activities

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Often has trouble holding attention on tasks or play activities

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Often does not seem to listen when spoken to directly

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Often does not follow through on instructions and fails to finish schoolwork, chores, or workplace duties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Often has trouble organizing tasks and activities

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Often avoids, dislikes, or is reluctant to engage in tasks requiring sustained mental effort

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Often loses things necessary for tasks/activities (keys, wallet, phone, pencils, tools, books)

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8:** Easily distractible and often forgetful in daily activities

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 9:** There are also hyperactive symptoms, including inability to sit still and being fidgety

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 10:** Part of the diagnostic criteria is that some symptoms must be present prior to age 12

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **10**
- Supported: **10**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **10 / 10 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 33 — Self Diagnosing ADHD

### Transcript

```text
this is going to ruffle quite a few feathers but I was just having this conversation with a friend of mine not everyone has ADD not everyone has ADHD and seriously I keep getting targeted for this ad on Tik Tok like literally it's like this tah Health company that that wants to diagnose you with ADHD and send you medication for ADHD and I just feel like not everyone has ADHD and then there are other people who like I also have ADHD like no you don't you're just annoying no everyone's getting too comfortable that's two different things one it's like you know using a clinical term to describe yourself and and that's not the case and another is like the over diagnoses of the population yeah yeah yeah yeah I agree so we've got different but you just reminded me we've got lots of issues and I'm hyper fixating on them today
```

**Metadata as supplied (views, likes, comments, duration):** `12,990 250 34 43`

### Revised claim review

**Claim 1:** Not everyone who claims to have ADHD or self-labels with the term actually has it — casually using "ADHD" as a descriptor (e.g., calling someone "annoying") is not the same as a genuine clinical diagnosis

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** There is overdiagnosis of ADHD happening in the population

**Verdict: Supported.** Evidence supports occurrence of overdiagnosis in some contexts; this cannot establish that the particular people mentioned lack ADHD. Evidence: [OVER](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2778451).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 34 — All 14 behaviour you need for an ADHD diagnosis #adhd #adhdawareness #adhdinwomen

### Transcript

```text
All 14 official ADHD behaviours you need for a diagnosis:
1. Trouble sitting Still
2. Quickly distracted by different stimulating things
3. Difficulty concertrating on things that don't interest you
4. Quickly switching from one activity to another
5. Can't keep internally still
6. Can't wait ur turn in group constellations
7. Often knowing the answer to a question
8. Trouble fulfilling tasks
9. Difficulty trying to play calmy
10. Often not thinking through before doing them
11. Often losing things
12. Frequently disrupting others
13. Talking a lot
14. Often not seeming to be listening
```

**Metadata as supplied (views, likes, comments, duration):** `132,835 4,159 181 42`

### Revised claim review

**Claim 1:** There are 14 "official" ADHD behaviours, and you need all 14 for a diagnosis

**Verdict: Unsupported.** Neither 14 official symptoms nor needing all 14 is correct. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Trouble sitting still

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Quickly distracted by different stimulating things

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Difficulty concentrating on things that don't interest you

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Quickly switching from one activity to another

**Verdict: Supported.** Frequent unfinished activity switching fits attention/follow-through difficulty; it need not be a separately named criterion. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Can't keep internally still

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Can't wait your turn in group settings

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8 — clarified extraction:** Often knowing the answer to a question.

*Original annotation wording:* Often knowing/blurting out the answer to a question

**Verdict: Unsupported.** The transcript says knowing the answer, not blurting it out. The earlier annotation added the behavior that would make this a criterion. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 9:** Trouble fulfilling/completing tasks

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 10:** Difficulty trying to play calmly

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 11:** Often not thinking through before doing things

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 12:** Often losing things

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 13:** Frequently disrupting/interrupting others

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 14:** Talking a lot

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 15:** Often not seeming to be listening

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **15**
- Supported: **13**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **13 / 15 × 100 = 86.67%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 35 — ADHD Late Diagnosis Consequences

### Transcript

```text
People say the ADHD diagnosis is pointless, labeling yourself. Did you know that not being diagnosed can lead to some pretty serious consequences? Two times as many relationships fail when one of the partners has ADHD. Literal jail. Research suggests that between 25 and 45% of people in prison would meet the diagnostic criteria for ADHD, and that's compared to 5% of people in the general population. Addiction. People with ADHD who are not diagnosed still have symptoms and may end up turning to unhelpful coping strategies that can turn into addictions that they can't get away from because they still need a crutch to cope with their ADHD symptoms. Low self-esteem. Shame. ADHDers have received so many more negative messages by the time they're even 10 years old. And this means that they do not feel good about themselves, and this can lead to things like not being able to maintain boundaries, being a people pleaser, and secondary to that, not achieving your academic potential, not achieving your career goals.
```

**Metadata as supplied (views, likes, comments, duration):** `18,953 1,741 47 56`

### Revised claim review

**Claim 1:** Relationships are twice as likely to fail when one partner has ADHD

**Verdict: Unsupported.** No adequate basis for an invariant twofold relationship-failure statistic was located. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Between 25–45% of people in prison meet ADHD criteria, compared with about 5% in the general population

**Verdict: Unsupported.** Screen-positive rates, interview diagnoses, age groups and population denominators are conflated; the quoted range is not an established general estimate. Evidence: [PRISON](https://pubmed.ncbi.nlm.nih.gov/38568877/), [PRISONOLD](https://pmc.ncbi.nlm.nih.gov/articles/PMC4301200/).

**Claim 3:** Undiagnosed ADHD may contribute to maladaptive coping and substance-use problems

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** By age 10, people with ADHD have received so many negative messages that low self-esteem and shame result

**Verdict: Supported.** Repeated criticism and adverse self-esteem effects in childhood are documented. The speaker gives no numerical count, so the earlier rationale was overly restrictive. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 5:** ADHD-related shame then causes weak boundaries, people-pleasing, and unrealized academic/career potential

**Verdict: Unsupported.** The specific causal chain through weak boundaries/people-pleasing is not established by associations with poorer outcomes. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **2**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **2 / 5 × 100 = 40.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 36 — Things that are common after getting a late ADHD Diagnosis: 1

### Transcript

```text
So, you just received a late in life ADHD diagnosis and you're like, "Now what?" I'm an ADHD coach with a late diagnosis and here's what I recommend. First off, it might be nice to know that 6% of US adults have ADHD and over half of them are diagnosed in adulthood. It is super normal to experience grief, anger, feeling overwhelm about where do I even start dealing with this? And even noticing that your ADHD symptoms are worsening. Totally, totally normal. And I promise you, it's temporary. But here's what I recommend you consider doing after that late diagnosis. First off, explore treatment options. Talk to your doctor about medication and lifestyle changes that can aid in ADHD management. And then from there, I recommend taking time to learn about your ADHD. This is so important because when we understand our ADHD brains, it helps us to manage our ADHD better, advocate for ourselves more effectively, be kinder to ourselves, and it gives us the agency we need to make the changes in our lives that need to happen for us to be more successful. There's a ton of information about ADHD on the internet. Not all of it's true. So, I definitely recommend check your sources. And here are a few reliable sources that I really like. And the third thing that I recommend you do is that you find some sort of community for support. A lot of times when we get that ADHD diagnosis, we can feel really alone. I remember feeling like I'm so weird. No one understands me. I don't know anyone like me. And then when I started opening up to my friends, it turns out that a lot of my friends also had ADHD. And it was so validating to be able to connect with people who also had ADHD. Now, if you don't have ADHD friends, there's tons of places for online communities. Add.org or has some really good support groups. And I of course offer a really nice group coaching program if you're looking to connect with other ADHDers and learn about your ADHD and get stuff done and have fun. And I don't know if you need to hear this, but getting diagnosed with ADHD changed everything and nothing for me at the same time. I was still the same person with the same quirks and the same problems. But getting a diagnosis made me realize that the things that I sucked at weren't character flaws. They were just brain differences. And because I understood this, it became the first time in my life that I really started to love myself. And additionally, understanding the root of my challenges allowed me to accommodate myself more effectively. And life slowly became easier and easier all because some doctor smacked some label on me. As controversial as that seems to a lot of people. Anyway, if this was helpful and if you want more ADHD content and support, follow along. I've got group coaching, one-on-one coaching, and a bunch of really helpful resources linked in my bio.
```

**Metadata as supplied (views, likes, comments, duration):** `2,010 271 3 133`

### Revised claim review

**Claim 1:** 6% of US adults have ADHD

**Verdict: Supported.** Supported as the dated 2023 US estimate of current self-reported diagnoses. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 2:** Over half of adults with ADHD are diagnosed in adulthood

**Verdict: Supported.** Supported for that same diagnosed US sample, not necessarily all undiagnosed adults. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 3:** It's "totally normal" to experience grief, anger, and feeling overwhelmed after a late diagnosis, and to notice ADHD symptoms seeming to worsen, and that this is temporary

**Verdict: Unsupported.** Mixed emotions are reported; guaranteed temporary worsening is not established. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 4:** Recommends exploring treatment, including talking to a doctor about medication and lifestyle changes for ADHD management

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** Learning about/understanding your ADHD helps you manage it better and advocate for yourself more effectively

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** Finding community/support groups is recommended after a late diagnosis

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **5**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **5 / 6 × 100 = 83.33%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 37 — “ADHD is Not Real” #wait

### Transcript

```text
I don't think ADHD is a real diagnosis. I think it's a real excuse to give people medication. I think ADHD is essentially a superpower. What ADHD is allows you to concentrate on things that you really enjoy, [music] but you cannot concentrate on things you don't enjoy. I think I have it. >> I could tell you that ADHD is a real diagnosis, but I would much prefer to show you. I'm Dr. Saramed, let's look at the facts. Yeah, aside from the fact that ADHD needs to be negatively impacting your quality of life for you to even be given a diagnosis in the first place. Here is an experiment where a controlled participant, somebody without ADHD, was given a response inhibition task. That is where the brain needs to exercise restraint, and as you can see, there is >> [music] >> plenty of activation here, even if you don't know what those areas mean. And on the right is that same brain being given methylphenidate, that stimulant medication. Remember, this is someone without ADHD. Now, the same task, the same brain slice, but the person has ADHD. Look at how little activation there is here in comparison. But what happens when they're given [music] stimulant medication? There is a significant increase. People with ADHD have different dopamine regulation. Their brains are structured differently. It's heritable, and there are decades of peer-reviewed research which is high-quality backing its existence. [music] I've shown you what it looks like. You choose what to trust, your eyes or just vibe.
```

**Metadata as supplied (views, likes, comments, duration):** `640,767 30,976 5,617 90`

### Revised claim review

The scientific propositions were checked; no video frame or transcript was retrieved. The specific scan display remains unverified.

**Claim 1:** ADHD is essentially a "superpower" — defined as being able to concentrate only on things you enjoy, and not on things you don't enjoy

**Verdict: Excluded from scoring.** This is a quoted position explicitly rebutted by the responding clinician, not an endorsed claim of the video.

**Claim 2:** ADHD needs to be negatively impacting your quality of life for you to even receive a diagnosis

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** A brain-imaging response-inhibition task shows a non-ADHD brain with substantial activation in relevant regions

**Verdict: Supported.** The broad research pattern is plausible; the actual displayed image cannot be authenticated from the transcript alone. Evidence: [FMRI](https://www.nature.com/articles/npp201130).

**Claim 4:** Giving a non-ADHD brain methylphenidate produces some activation change on this same task

**Verdict: Supported.** Stimulants also affect non-ADHD brains; the earlier categorical rejection was incorrect. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** The same task performed by an ADHD brain shows markedly less activation in the relevant region

**Verdict: Supported.** Group/task-specific findings do not apply to every individual brain. Evidence: [FMRI](https://www.nature.com/articles/npp201130).

**Claim 6:** Giving stimulant medication to the ADHD brain produces a "significant increase" in activation

**Verdict: Supported.** The cited research supports task-specific changes, not an independently verified image in this video. Evidence: [FMRI](https://www.nature.com/articles/npp201130).

**Claim 7:** People with ADHD have different dopamine regulation and structurally different brains

**Verdict: Supported.** Population differences and dopamine involvement do not provide a diagnostic scan. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164).

**Claim 8:** ADHD is heritable

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 9:** There are decades of peer-reviewed, high-quality research supporting ADHD's existence as a legitimate diagnosis

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **8**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **8 / 8 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate** — see the limitation below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** Only the scientific propositions were reviewed. The particular scan/image display was not authenticated; the supported group findings do not validate an individual diagnostic scan.

---

## Video 38 — ADHD Is Not Real

### Transcript

```text
attention deficit disorder and ADHD there's no clinical test for this there's no blood test there's no CT scan this is based on someone's opinion about your child using a medication for a behavior problem doesn't really solve the problem it's trying to mask a symptom and there are always side effects
```

**Metadata as supplied (views, likes, comments, duration):** `1,527 31 0 26`

### Revised claim review

**Claim 1:** There's no clinical test for ADHD — no blood test, no CT scan

**Verdict: Supported.** Supported as no stand-alone blood/CT diagnostic test, not as denial that clinical assessment exists. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** ADHD diagnosis is "based on someone's opinion about your child," implying it's merely subjective rather than a legitimate clinical determination

**Verdict: Unsupported.** Clinical judgment is structured and evidence-based, not merely an arbitrary opinion. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Using medication for a behavior problem doesn't solve the problem, it just masks a symptom

**Verdict: Unsupported.** Symptom treatment has demonstrated benefit; lack of a cure does not make it ineffective. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** There are always side effects (implying medication universally causes adverse effects)

**Verdict: Unsupported.** Adverse effects are possible, not inevitable for every person and every treatment. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 39 — ADHD isn't real 🥀

### Transcript

```text
Here, are you one of the ADHD students? >> Yes, I actually am, and I was diagnosed. You're diagnosed It's not a mental illness. No, it's an actual diagnosis from my doctor. >> mentally ill person right now. That is You are mentally ill. You don't understand what it means to be a student. That is horribly offensive, and I will be reporting you to the dean. But, I have accommodations to help me focus in your lecture. >> do you mean? You You just read it. You read the slides. How are you going to focus? >> Some people's brains don't work that way. My grandma can understand when I talk to her. My grandma >> many words are on the screen. How am I supposed to digest all this? That's crazy. >> have mental illness, and you go get your special >> wasn't for This wasn't for rainbow magical drugs that you're taking. It doesn't do anything for you. I don't care. I was told by my doctor You're still doing the ADHD propaganda on all my students. Sure. I was told to use Mind Graph by my doctor to live record the thousands of words you speak that make no sense, and I have it make me notes because it's so hard for me to focus in your class when you speak in this monotone voice. How am I supposed to do that? >> Monotone? Yeah, can you have Yeah. I like the way I'm talking right now.
```

**Metadata as supplied (views, likes, comments, duration):** `22,646 674 23 60`

### Revised claim review

**Claim 1:** Being diagnosed with ADHD means being "mentally ill," and calling a diagnosed student "a mentally ill person"

**Verdict: Supported.** ADHD belongs to the diagnostic classification of mental/neurodevelopmental disorders; that classification does not validate an insult or imply global incompetence. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** ADHD medication ("rainbow magical drugs") "doesn't do anything" for the person taking it

**Verdict: Unsupported.** Categorical medication ineffectiveness is contradicted by treatment evidence. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** A person with ADHD can have genuine difficulty focusing/processing information in a lecture setting (e.g., large amounts of text on a screen, monotone speech), warranting tools like recording lectures and note-taking supports

**Verdict: Supported.** General accommodation needs are supported; this does not verify the named product or an individual doctor recommendation. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 4:** Referring to ADHD accommodations/awareness dismissively as "ADHD propaganda"

**Verdict: Excluded from scoring.** A dismissive evaluative phrase, not an externally verifiable ADHD assertion.

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 40 — Professor said ADHD isn’t real… wait till you see this 😳

### Transcript

```text
Just a reminder, anyone that's claiming that they have, or they do have ADHD, I need you all to understand that if you got a bad grade, I believe you guys need to study a little bit harder. Sorry, I feel like that was incredibly rude. I mean, are you kidding me? I got diagnosed with ADHD at a very young age, and classes like this that are extremely hard and have extremely long lectures and a lot of information, and for you to just say that we need to work harder is absolute >> I mean, I've been teaching this class for about like 10 years, and I've never had any student complain to me about anything. I beg to differ. You have two stars on RateMyProfessor, and a lot of the comments are saying that you are a tough grader and give way too many slides. So, more information is not a good thing for students with ADHD, but clearly you wouldn't understand that because you just don't believe it's a real thing. Luckily, my doctor told me to look up this website called I Hate Reading. You can upload every single lecture slide, and it will make you flashcards, quizzes, so you could actually work with the information.
```

**Metadata as supplied (views, likes, comments, duration):** `15,542 109 45 56`

### Revised claim review

**Claim 1:** Very long, information-dense lectures can be harder for a student with ADHD to process

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 2:** More information is not good for students with ADHD

**Verdict: Unsupported.** Information density can be challenging; more information is not inherently harmful to every ADHD student. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **1**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **1 / 2 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 41 — Cobra on why ADHD isn't real

### Transcript

```text
that's the biggest garbage joke of them all you raise the kid with an iPad and flashing images and these crazy video games designed to be addictive and then you take all that away and sitting in front of a [ __ ] boring textbook of course he doesn't want to pay attention does he rather pay his iPad game but he must pay attention because of discipline when you remove the element of discipline well then he doesn't want to pay attention so he's not going to pay attention then you say he has a disease you're just refusing to discipline your child
```

**Metadata as supplied (views, likes, comments, duration):** `791 20 28 24`

### Revised claim review

**Claim 1:** Children raised with iPads, flashing images, and addictive video games develop attention problems that get mistaken for ADHD, when the real issue is a lack of discipline

**Verdict: Unsupported.** A parenting/discipline-only explanation does not account for ADHD. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** A child not wanting to pay attention to something boring (versus a stimulating video game) reflects a discipline problem rather than a genuine attention disorder, and diagnosing it as ADHD is "refusing to discipline your child"

**Verdict: Unsupported.** Interest-dependent attention does not disprove a neurodevelopmental disorder. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **0**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **0 / 2 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 42 — ADHD Isnt Real

### Transcript

```text
I'm gonna say something really controversial okay I don't believe in ADHD yeah I don't no why is that um I think that our brains all operate on different frequencies and I think that we pay attention to the things that that interest us yeah and for people who have any type of intelligence if it doesn't spark an interest and wanting you to do it why the [ __ ] would you bother with it care yeah so no that makes sense and I understand being hyper right but I I know a whole lot of adults who claim to have ADHD who are overweight and [ __ ] sit and aren't on meds and sit around and don't do [ __ ] with them their lives other than yeah [ __ ] eat bomb bonds and watch TV and talk about how bad their life is the ADHD you would think you would have some sort of like get up and go aspect to it because that's what we all led to believe when kids had add versus ADHD um but I think that a lot of that comes down to children we're we're we're stripping away the creative mindset
```

**Metadata as supplied (views, likes, comments, duration):** `8,784 276 197 55`

### Revised claim review

**Claim 1:** ADHD isn't real — people just naturally pay attention only to things that interest them, and it's normal/expected for anyone with "any type of intelligence" not to bother with things that don't spark interest

**Verdict: Unsupported.** Interest effects do not negate the existence of ADHD. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Adults who "really" have ADHD would be expected to have a "get up and go" quality, and people who are overweight, inactive, and not achieving are just using ADHD as an excuse rather than truly having it

**Verdict: Unsupported.** Physical inactivity or body size does not rule out ADHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** The distinction between "ADD" and "ADHD" as separate things kids "used to" have

**Verdict: Unsupported.** ADD is an older term, not a separate contemporary diagnosis opposed to ADHD. Evidence: [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 4:** Something about modern parenting/upbringing is "stripping away the creative mindset" in children, implying this explains rising ADHD-like behavior

**Verdict: Excluded from scoring.** The unfinished comment about creativity does not actually establish the causal assertion added by the previous annotation.

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **1**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 43 — ADHD is not real! #adhd #adhdawareness #adhdproblems #adhdlife #neurodivergent #neurospicy #fyp

### Transcript

```text
what is ADHD it's just an excuse to be lazy have you heard that before you've been one of those people that have said that that you just AG your ADHD is an excuse and you're just being lazy I'm going to give you an example of what it's like to have an ADHD brain ignore that thing shaking so let's say you got a car you got an Audi so per someone that's neurotypical they'll get in the car and they'll start they turn the key and they start the engine and it's start straight away done and we'll start driving someone with ADHD now it's the same car it's an Ali however the engine parts are faulty you know the glow plugs might need you know replacing or you know so you start the car it's taking some time to start it's going and then it's going to take a while for it to start and then once it starts it'll get going but it's going to take time to speed up Let the clutches gone so that's the best I can explain
```

**Metadata as supplied (views, likes, comments, duration):** `441 7 2 61`

### Revised claim review

**Claim 1:** ADHD is not "just an excuse to be lazy" — it reflects a genuine underlying brain-based difference, not a character flaw or lack of effort

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** People with ADHD (via the car analogy) experience a slower "start-up" — more difficulty initiating tasks and getting going, even though they can eventually get moving, compared to neurotypical people who start tasks immediately

**Verdict: Supported.** Accepted as a metaphor for task-initiation difficulty, not a literal claim of damaged engine-like brain parts. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 44 — Is ADHD a Real Problem? What Makes It a Disorder?

### Transcript

```text
so what makes attention deficit hyperactivity a disorder is that it is causing disorder that it is impairing you there are 18 symptoms on the checklist the official checklist as well as some other criteria like the symptoms should have been present even in childhood but that list of symptoms apply to everybody forgetful lose things can't keep track of things uh interrupt sometimes all of those different things happen to everybody now and then but if they're constant then it might be ADHD so it's easy to look at the list and think well everybody has these symptoms yeah at one time or another but is it impairing no it's not impairing me well maybe you're too close to it maybe you don't notice the difference that other people around you loved ones might notice you might want to check in with them is this something I do a lot and is it a problem
```

**Metadata as supplied (views, likes, comments, duration):** `4,198 374 17 58`

### Revised claim review

**Claim 1:** What makes ADHD a disorder is that it is causing "disorder" — i.e., it is impairing the person, not merely the presence of symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** There are 18 symptoms on the official checklist

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Symptoms should have been present even in childhood

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** These symptoms (forgetfulness, losing things, difficulty keeping track of things, interrupting, etc.) happen to everybody sometimes, but what distinguishes ADHD is that they are constant/persistent rather than occasional

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** A person might not perceive their own symptoms as impairing because they're "too close to it," and checking in with loved ones can reveal whether it's actually a problem

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 45 — How are people with ADHD different from people who don't have ADHD? | Experts answer

### Transcript

```text
how are people with ADHD different from people who don't have ADHD so I have a saying that ADHD doesn't invent new problems it just exacerbates the universal ones we all get distracted sometimes we all forget things we all procrastinate this is not a unique experience only to people with ADHD the big difference is folks with ADHD have these struggles more often it might have a bigger impact on their life it might be more visible to others they might have more emotional stronger feelings about it that's really the big difference it's not a difference in kind it's a difference in degree
```

**Metadata as supplied (views, likes, comments, duration):** `20,095 1,051 16 38`

### Revised claim review

**Claim 1:** ADHD doesn't invent new problems, it exacerbates universal ones — everyone gets distracted, forgets things, and procrastinates sometimes, and this isn't unique to people with ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** The key difference is that people with ADHD have these struggles more often/more frequently

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** The struggles may have a bigger impact on the person's life

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** The struggles might be more visible to others

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 5:** People with ADHD might have stronger emotional feelings about these struggles

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 6:** The overall difference between people with and without ADHD is one of degree, not of kind

**Verdict: Supported.** Accepted as a dimensional description of symptoms and impairment, not a denial of biological heterogeneity. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 46 — Is ADHD real?

### Transcript

```text
one of the myths about ADHD is that people just need to try harder or that they're being lazy when in fact they really are trying hard they're trying hard to make it to that event on time they're trying hard to make sure they respond to every email they're trying hard to focus on a test but there are distractions and other things that happen that make it a struggle ADHD is very real for adults what you might notice is that you're over scheduling you are committing to things when you don't really have the time to commit you're losing track of time easily you might forget to respond to text messages or have 50 unread text messages because it just is a little bit overwhelming to respond to Everything at Once if you're in a relationship or you're partner with someone who is more structured or more rigid it may become annoying to them if they expect things to go one way and you don't always follow through with the plan because you've lost track of time or you have trouble with organizing or planning
```

**Metadata as supplied (views, likes, comments, duration):** `18,658 1,480 54 55`

### Revised claim review

**Claim 1:** A myth about ADHD is that people just need to try harder or are being lazy, when in fact they really are trying hard

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** ADHD is real for adults

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** In adults, ADHD may show up as over-scheduling/over-committing to things without having the time

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Losing track of time easily

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 5:** Forgetting to respond to texts or accumulating many unread messages because responding to everything feels overwhelming

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** In relationships with a more structured/rigid partner, this can cause friction when plans aren't followed through due to lost track of time or organizational/planning difficulties

**Verdict: Supported.** Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 47 — ADHD isn’t a Superpower, it’s a real struggle.

### Transcript

```text
this may be controversial but I'm going to say it anyway I really don't like when people say ADHD is a superpower I get it they probably have good intentions they're trying to highlight creativity high energy or thinking outside the box but let's be real having ADHD is a very serious struggle for many people it's debilitating someone with ADHD might start dozens of projects and not finish a single one because the excitement of starting is exhilarating but the follow through feels unbearable they struggle to focus when it matters most leading to missed deadlines forgotten appointments and constant frustration ADHD can make it harder to keep jobs maintain relationships or even do basic daily tasks impulsivity can lead to Reckless spending risky decisions and higher rates of car accidents the emotional toll overwhelm burnout and feeling like no matter how hard they drive they're always falling behind and when a neurotypical person calls it a superpower itat creates a false expectation it makes people with ADHD feel like if they're struggling it's their fault like they just aren't using their powers correctly that's not how it works yes some people learn to work with ADHD but that doesn't erase the daily struggles it's not some hidden gift waiting to be unlocked it's a real challenge that requires real support saying otherwise doesn't help it just makes people blame themselves for something that was never their fault
```

**Metadata as supplied (views, likes, comments, duration):** `1,167 90 7 90`

### Revised claim review

**Claim 1:** ADHD is not a "superpower" — for many people it is a serious, debilitating struggle rather than a gift

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** People with ADHD might start many projects but not finish them, because starting is exciting but follow-through is hard

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 3:** Struggling to focus when it matters most, leading to missed deadlines and forgotten appointments

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** ADHD can make it harder to keep jobs, maintain relationships, or do basic daily tasks

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 5:** Impulsivity can lead to reckless spending, risky decisions, and higher rates of car accidents

**Verdict: Supported.** Evidence: [DRIVE](https://pubmed.ncbi.nlm.nih.gov/24238842/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 6:** There is significant emotional toll — overwhelm, burnout, and a persistent feeling of falling behind

**Verdict: Supported.** These associated emotional/occupational burdens are documented; the earlier DSM-only rejection was too narrow. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 7:** Calling ADHD a "superpower" creates a false expectation and can make people with ADHD blame themselves for struggling, as if they're just "not using their powers correctly"

**Verdict: Unsupported.** The asserted particular effect of the “superpower” label on others has not been established by the cited criticism research. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **6**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **6 / 7 × 100 = 85.71%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 48 — The Real Difference Between ADHD and Ordinary Forgetfulness

### Transcript

```text
I want y'all to really think about this for a second. So, the problem with ADHD is it is a sensory attentional disorder. So, for a neurotypical person, the more important something is, the more it sinks in. But for ADHD, if we don't ever hear it in the first place, it doesn't matter how important it is because we never heard it. So, people who are neurotypical will also forget things. They won't pay attention 100% of the time, but they don't forget exams. They don't forget projects. They don't forget weddings, right? they don't forget like the big stuff. So, some of that stuff is intact in neurotypical people. So, everyone will forget, but it doesn't happen as often and the consequences are not as severe. Once the consequences are severe and it happens often enough, we turn on this dread mode, this paranoia mode, because we can't trust ourselves when we are relaxed. When we are relaxed, we make mistakes. So let's constantly be in a state of dread.
```

**Metadata as supplied (views, likes, comments, duration):** `119,723 5,469 167 52`

### Revised claim review

**Claim 1:** ADHD is fundamentally a "sensory attentional disorder" where, unlike neurotypical people, information doesn't "sink in" more just because it's important — if it isn't perceived in the first place, importance is irrelevant

**Verdict: Unsupported.** Encoding failures are possible, but ADHD is not established as this exclusive sensory-encoding disorder. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Neurotypical people also forget things and don't pay attention 100% of the time, but they don't forget major events like exams, projects, or weddings

**Verdict: Unsupported.** People without ADHD can forget important events. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** People with ADHD forget things (including significant things) more often than neurotypical people, and the consequences tend to be more severe

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Because consequences become severe and frequent, people with ADHD develop a constant "dread mode" or "paranoia mode," being unable to trust themselves when relaxed, making mistakes when relaxed, and living in a persistent state of dread

**Verdict: Unsupported.** Stress may follow repeated failures; the inevitable relaxed-equals-errors/dread cycle is not established. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 49 — ADHD and Time Blindness

### Transcript

```text
let's look at a fascinating study the light bulb experiment so Dr Russell Barkley a leading expert on ADHD conducted an experiment to explore time perception in individuals with and without ADHD he put participants in a room and showed them a light bulb and he would turn it on for a time and then off again and he'd asked them to estimate how long it had been on and he found something interesting both the ADHD and the non-adhd participants were able to estimate the amount of time the light was on in about the same range of accuracy but here's where things fell apart for the participants with ADHD when Dr Barkley gave them the light switch and asked them to reproduce the time intervals themselves the adhders were not able to reliably reproduce the same time interval with the light as the group with no ADHD symptoms and so adhders were less capable of using their minds to govern their actions around time- sensitive tasks they could perceive time to a varying degree but they could not judge or effectively estimate the amount of time an event or task would take for them to complete
```

**Metadata as supplied (views, likes, comments, duration):** `100,262 6,078 154 61`

### Revised claim review

SOURCE-DETAIL FLAG: the broad timing findings are supported, but the exact narrated light-bulb/switch procedure was not established in the accessible original-study details. Claim 1 is unverified, not disproved. If that procedure is substantiated, its reversal alone changes the ratio to Label 2.

**Claim 1:** Dr. Russell Barkley conducted a "light bulb experiment" studying time perception in people with and without ADHD, turning a light on/off and asking participants to estimate how long it had been on

**Verdict: Unsupported.** Barkley timing studies exist, but the exact light-bulb/switch procedure narrated here was not verified in accessible study details. Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 2:** Both ADHD and non-ADHD participants were able to estimate the amount of time the light was on with roughly similar accuracy (i.e., no significant difference in time estimation)

**Verdict: Supported.** Supported for the IQ-adjusted estimation comparison, not an assertion that every analysis showed no difference. Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 3:** When given the light switch and asked to reproduce the same time interval themselves, ADHD participants could not reliably reproduce it as accurately as non-ADHD participants (i.e., a deficit in time reproduction, not perception)

**Verdict: Supported.** The study supports time-reproduction differences; the exact narrated apparatus remains unverified. Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 4:** This shows that people with ADHD are less capable of using their minds to govern their actions around time-sensitive tasks — they can perceive time to a degree, but struggle to judge/estimate how much time a task will take them to complete

**Verdict: Unsupported.** Laboratory interval reproduction does not directly establish inability to estimate everyday task duration. Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading** — see the limitation below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** The exact narrated light-bulb/switch procedure was not established in accessible original-study details. This is unverified, not disproved. Supporting Claim 1 would change Label 3 to Label 2.

---

## Video 50 — Why Texting is IMPOSSIBLE for ADHD Brains

### Transcript

```text
when someone with ADHD opens a message and begins to type they might get sidetracked by something else they Place their phone down to concentrate on anything else but once they did they forgot they were supposed to reply although this Amnesia is never malicious it can make others feel ignored or mistreated in romantic relationships an extra layer of frustration could be apparent due to ADHD in a partnership each member has particular needs
```

**Metadata as supplied (views, likes, comments, duration):** `3,010 44 4 25`

### Revised claim review

**Claim 1:** Title/framing: texting is ‘impossible’ for ADHD brains

**Verdict: Excluded from scoring.** This assertion is title-only, absent from the spoken transcript; it is outside this transcript-focused review.

**Claim 2:** A person with ADHD may be sidetracked while replying and then forget to finish

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** ADHD-related forgetting to reply is not necessarily malicious or intentional

**Verdict: Supported.** Read as the statement that ADHD-related forgetting itself is unintentional, not that every unanswered message has an innocent cause. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** This pattern can make another person feel ignored or mistreated

**Verdict: Supported.** Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** ADHD can add frustration to romantic relationships, in which partners have different needs

**Verdict: Supported.** Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 51 — Is ADHD Even Real? A Therapist Answers

### Transcript

```text
A parent whose son was diagnosed with ADHD asked me if ADHD is even real. Yes, it is. A lot of people grow up hearing that ADHD is just their laziness or lack of effort or not trying hard enough. But decades of research show that ADHD is a real, significant, distressing, interfering, and legitimate medical problem that can affect your focus, emotions, and everyday life. So, what you're experiencing isn't a personal failure. It's something your brain is genuinely struggling with. If this resonated, consider subscribing, and let's make sense of things together.
```

**Metadata as supplied (views, likes, comments, duration):** `1,119 11 3 40`

### Revised claim review

**Claim 1:** Is ADHD even real? — Yes, it is

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** ADHD is often mistakenly attributed to laziness, lack of effort, or not trying hard enough

**Verdict: Supported.** Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** ADHD is a "real, significant, distressing, interfering, and legitimate medical problem" that can affect focus, emotions, and everyday life

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** Experiencing ADHD symptoms is not "a personal failure" but reflects something the brain is genuinely struggling with

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 52 — ADHD and Time Blindness Explained

### Transcript

```text
Time blindness is one of the most frustrating ADHD symptoms. And here's why it happens. ADHD brains have trouble sensing the passing of time. Instead of feeling time as a continuous flow, it often feels like just two categories, either now or not now. That's why you can hyperfocus for hours on something you enjoy, but completely lose track of the appointment you were supposed to leave for 30 minutes ago. It's not about being careless. It's about how the ADHD brain processes time, motivation, and dopamine. And the fix isn't shame, it's structure. Using timers, visual clocks, or even accountability partners helps bring time back into view, so you're not relying on your brain alone. So, if you've ever wondered why time just disappears with ADHD, now you know. If you found value in this video, follow me for more ADHD tips like
```

**Metadata as supplied (views, likes, comments, duration):** `8,137 470 19 50`

### Revised claim review

**Claim 1:** Time blindness is one of the most frustrating ADHD symptoms

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 2:** ADHD brains have trouble sensing the passing of time

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 3:** Instead of a continuous flow, time feels like two categories — "now" or "not now"

**Verdict: Excluded from scoring.** “Now/not now” is a metaphor for subjective time, not an independently literal two-category clock mechanism.

**Claim 4:** This is why someone can hyperfocus for hours on something enjoyable but completely lose track of an appointment they were supposed to leave for 30 minutes ago

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 5:** It's not about being careless — it's about how the ADHD brain processes time, motivation, and dopamine

**Verdict: Unsupported.** The specific explanatory leap from time problems to dopamine is not established here. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 6:** The fix isn't shame, it's structure — using timers, visual clocks, or accountability partners helps bring time back into view

**Verdict: Supported.** External reminders/structure are reasonable supports, not a guaranteed fix for all impairment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **4**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **4 / 5 × 100 = 80.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 53 — ADHD is NOT a deficit of attention

### Transcript

```text
now let's talk about distractability which is sort of the Cornerstone symptom given the name attention deficit hyperactivity disorder but the interesting thing is that it's a bit of a misnomer because it's not that we have a deficit of attention at all I mean I can pay attention to something that I find riveting forever and forget that i' even have a body or a life or that you know time is passing the problem is that our attention spans are very often disregulated meaning we can't always control what it is our brain wants to pay attention to so if there's something that we're supposed to be doing like a particular class that we're supposed to be taking or doing our taxes but there's something much juicier going on over here then it is literally almost impossible for us to move our brain from the juicy thing over here to the task at hand
```

**Metadata as supplied (views, likes, comments, duration):** `9,916 564 12 49`

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** ADHD does not involve a deficit of attention at all.

*Original annotation wording:* ADHD is NOT a deficit of attention

**Verdict: Unsupported.** The categorical denial exceeds the evidence. Preserved attention for engaging tasks does not eliminate clinically impairing inattention. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 2:** The person can pay attention to something they find riveting for a very long time, losing track of body, time, or surroundings (describing hyperfocus)

**Verdict: Excluded from scoring.** Explicit personal account, not a generalized factual assertion.

**Claim 3:** The core issue is that attention is dysregulated — the person can't always control what their brain chooses to focus on

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** When a required task competes with something more stimulating, redirecting attention is literally almost impossible for people with ADHD.

*Original annotation wording:* When there's a required task (e.g., a class, doing taxes) competing with something more stimulating, it can be "almost impossible" to redirect attention to the required task

**Verdict: Unsupported.** Hyperfocus can involve switching difficulty; a general rule of near-impossibility is not established. The previous extraction added a possibility qualifier. Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **1**.
- Supported-claim percentage: **1/3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 3**.

---

## Video 54 — ADHD vs Anxiety: Key Differences Explained

### Transcript

```text
among the symptoms they have in common are having trouble focusing difficulty finishing tasks and adhering to deadlines agitation sleeplessness making the distinction between the two might be challenging due to their similarities however it is crucial to remember the following the main symptoms of anxiety are trepidation fear and worry the three main characteristics of ADHD are hyperactivity impulsivity and attention the three main characteristics of ADHD are hyperactivity impulsivity and inattention
```

**Metadata as supplied (views, likes, comments, duration):** `1,403 20 0 32`

### Revised claim review

**Claim 1:** ADHD and anxiety share overlapping symptoms including trouble focusing, difficulty finishing tasks/meeting deadlines, agitation, and sleeplessness

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** The main symptoms of anxiety are trepidation, fear, and worry

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 3:** The three main characteristics of ADHD are hyperactivity, impulsivity, and inattention (note: the transcript initially misstates "attention" before self-correcting to "inattention")

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 55 — ADHD + Dyslexia

### Transcript

```text
ADHD and dyslexia have more in common than you might expect. Recognizing these similarities is key to better understanding your child. Firstly, children with ADHD often experience difficulty when it comes to tasks regarding focus and organization. Whereas for children with dyslexia, things such as reading and decoding may be an obstacle. However, for both ADHD and dyslexia, reading and attention challenges are common. If you notice these are present in your child's behavior, be sure to speak with their teacher. You got
```

**Metadata as supplied (views, likes, comments, duration):** `92,363 1,452 93 31`

### Revised claim review

**Claim 1:** ADHD and dyslexia have overlapping features/similarities

**Verdict: Supported.** Evidence: [RD](https://pubmed.ncbi.nlm.nih.gov/20828676/).

**Claim 2:** Children with ADHD often experience difficulty with tasks involving focus and organization

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** For children with dyslexia, reading and decoding are common obstacles

**Verdict: Supported.** Evidence: [RD](https://pubmed.ncbi.nlm.nih.gov/20828676/).

**Claim 4:** For both ADHD and dyslexia, reading and attention challenges are common (i.e., some overlap in symptom presentation between the two)

**Verdict: Supported.** Evidence: [RD](https://pubmed.ncbi.nlm.nih.gov/20828676/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 56 — What you should know about ADHD medication

### Transcript

```text
Three things to know about ADHD medication. One, ADHD medication is not a cure-all. It can help alleviate your ADHD symptoms, but it won't magically cure all your problems, like getting organized or planning things. Two, there are two kinds of ADHD meds, stimulants and non-stimulants, and they can have different side effects. Three, research has shown that if you have ADHD and getting properly treated for it, taking ADHD meds appears to reduce the risk of substance abuse, not increase it.
```

**Metadata as supplied (views, likes, comments, duration):** `343,191 5,918 94 29`

### Revised claim review

**Claim 1:** ADHD medication is not a "cure-all" — it can help alleviate symptoms but won't magically fix everything (e.g., getting organized, planning)

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** There are two kinds of ADHD medications — stimulants and non-stimulants — and they can have different side effects

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Research shows that properly treating ADHD with medication appears to reduce the risk of substance abuse, not increase it

**Verdict: Supported.** The speaker says “appears”: this is compatible with observational risk associations, not proof of prevention. Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 57 — ADHD friendships ❤️ #adhd #adhdbrain #neurodivergent

### Transcript

```text
as ADHD people we do things at Fallout when we love someone we love them like we fully love them if you've got a friend if anyone you know people watching have got a friend who is ADHD if they like you they really like you and they will forget you exist as well and that doesn't actually in their minds There's No in fact I was saying this to my friend recently I was saying you know if I don't hear from you like assume I really like you like don't assume anything's changed because I will see if something's changed like we've got anxious friends who if I don't speak to them they're like she hates me I'm like no I don't I just forgot you existed for a minute
```

**Metadata as supplied (views, likes, comments, duration):** `505,071 31,786 529 32`

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** People with ADHD love intensely/wholeheartedly when they love someone

**Verdict: Unsupported.** A general claim of unusually wholehearted love is unsubstantiated. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 2:** An ADHD friend who likes you will forget that you exist.

*Original annotation wording:* A friend with ADHD may forget you exist for periods of time, but this doesn't mean their feelings toward you have changed

**Verdict: Unsupported.** Literal loss of knowledge of another person’s existence is not established by evidence of ADHD forgetfulness. The earlier review substituted failure to keep in touch. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** If someone with ADHD doesn't reach out, you shouldn't assume anything has changed in the relationship — implying this pattern of going quiet without it reflecting relational change is characteristic of ADHD

**Verdict: Excluded from scoring.** The speaker gives an instruction to her own friends about her own silence; the earlier annotation generalized it to all ADHD relationships.

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **0**; unsupported: **2**; excluded: **1**.
- Supported-claim percentage: **0/2 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Previous reviewed label: **Label 3**.
- Uploaded CSV label: **Label 4**.

---

## Video 58 — 5 Signs of ADHD 🤚🧠 | CBBC #Shorts

### Transcript

```text
five secret signs from my time at school that I had ADHD that nobody ever picked up on one always daydreaming in class and struggling to stay focused especially when it wasn't one of my favorite subjects two forgetting to do my homework or losing it on the rare occasion that I did remember to do it three viting and moving around in my chair cuz I felt like I might explode from sitting still for so long four shouting out the answers to questions because I just could not keep my mouth shut any longer five asking for work in the subjects that I did enjoy because my brain just worked so quickly so those are five of the ways that ADHD showed up for me maybe you can relate to some of them or maybe you won't but we've all got brains that work in different ways
```

**Metadata as supplied (views, likes, comments, duration):** `319,133 4,868 0 43`

### Revised claim review

The experiences are retained. Exclusion does not call them false; the video supplies fewer than two generalized factual claims.

**Claim 1:** Always daydreaming in class and struggling to stay focused, especially in non-favorite subjects

**Verdict: Excluded from scoring.** Explicitly autobiographical, with an express statement that others may not relate. Excluded by the thesis rule for personal experience.

**Claim 2:** Forgetting to do homework, or losing it on the rare occasion it was done

**Verdict: Excluded from scoring.** Explicitly autobiographical, with an express statement that others may not relate. Excluded by the thesis rule for personal experience.

**Claim 3:** Fidgeting and moving around in her chair because she felt like she might "explode" from sitting still too long

**Verdict: Excluded from scoring.** Explicitly autobiographical, with an express statement that others may not relate. Excluded by the thesis rule for personal experience.

**Claim 4:** Shouting out answers to questions because she "could not keep her mouth shut" any longer

**Verdict: Excluded from scoring.** Explicitly autobiographical, with an express statement that others may not relate. Excluded by the thesis rule for personal experience.

**Claim 5:** Asking for extra work in subjects she enjoyed because her brain worked quickly, framed as a "secret sign" of her ADHD

**Verdict: Excluded from scoring.** Explicitly autobiographical, with an express statement that others may not relate. Excluded by the thesis rule for personal experience.

### Revised result

- Eligible fact-checkable claims: **0**
- Supported: **0**; unsupported: **0**; excluded: **5**.
- Supported-claim percentage: **not defined** (no eligible claims).
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 59 — Fake ADHD versus real ADHD #adhd #adhdbrain #adhdselfimprovement

### Transcript

```text
Let's talk about fake ADHD because what most people call fake is actually misunderstood ADHD. I'm Saskia, licensed therapist, ADHD mentor, here to help you heal and understand yourself. ADHD doesn't look the same in everyone. Surprise, surprise. Some people are the classic can't sit still, blurting things out type. Others are quiet, anxious, perfectionistic, masking so hard they look functional on the outside, but they're falling apart on the inside. People think it's fake because they only recognize one version of ADHD. Usually the hyper little boy stereotype, but ADHD in adults, trauma survivors, often hides behind burnout, forgetfulness, emotional overwhelm, and executive dysfunction. So, no, it's not about people faking ADHD for attention or medication. It's about an entire culture finally noticing how ADHD can look different, especially in people who were missed, dismissed, or misdiagnosed for years. Validation isn't overdiagnosing, it's catching up.
```

**Metadata as supplied (views, likes, comments, duration):** `13,046 1,680 90 80`

### Revised claim review

**Claim 1:** ADHD doesn't look the same in everyone — some present as the classic "can't sit still, blurting things out" type, others present quietly, anxiously, or perfectionistically while masking

**Verdict: Supported.** Different presentations and compensatory perfectionism/masking are documented. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** People often think ADHD is "fake" because they only recognize one stereotype (the hyperactive young boy), when ADHD in adults can present differently

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** In adults and trauma survivors, ADHD often "hides behind" burnout, forgetfulness, emotional overwhelm, and executive dysfunction

**Verdict: Supported.** These associated experiences can obscure recognition; this is not a claim that trauma causes all ADHD. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** This isn't about people faking ADHD for attention or medication — it's about wider recognition of how ADHD can look different, especially in those missed/dismissed/misdiagnosed for years

**Verdict: Unsupported.** Underrecognition does not justify categorically excluding overdiagnosis or deliberate symptom simulation. Evidence: [OVER](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2778451).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 60 — ADHD and Motivation

### Transcript

```text
One of the most frustrating things about having ADHD is knowing how important something is to get done and still not being able to motivate yourself to do it. This happens whether it's important to a boss or your parent or a partner, but even if it's important to you. I have been late to so many job interviews, really important ones, but the importance just wasn't a motivating factor for me to get there on time. According to Dr. William Dodson, this is because a neurotypical person is motivated by importance and also rewards and consequences, but an ADHD person isn't motivated by these at all. Instead, we're motivated by five completely separate factors. One would be interest, two would be competition or a challenge. The third one is a sense of urgency. The fourth one is novelty or creativity. And the fifth factor that motivates us is passion.
```

**Metadata as supplied (views, likes, comments, duration):** `255,637 20,571 547 52`

### Revised claim review

**Claim 1:** A common frustration with ADHD is knowing how important a task is but still being unable to motivate yourself to do it, even when it matters to a boss, parent, partner, or yourself

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Being late to important events (e.g., job interviews) despite knowing their importance

**Verdict: Excluded from scoring.** Personal job-interview example; the broader task-initiation claim is already counted in claim 1.

**Claim 3:** According to Dr. William Dodson, neurotypical people are motivated by importance, rewards, and consequences, while people with ADHD are not motivated by these at all

**Verdict: Unsupported.** Rewards and consequences can influence ADHD behavior; “not ... at all” is incorrect. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Instead, people with ADHD are motivated by five separate factors: interest, competition/challenge, urgency, novelty/creativity, and passion

**Verdict: Unsupported.** The exclusive five-factor system is not a validated general motivational law. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **1**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 61 — Rejection sensitivity & ADHD | Experts answer

### Transcript

```text
why am I so sensitive to rejection rejection is hard for everybody but as it turns out people with ADHD often suffer from something called rejection sensitivity dysphoria now you can have rejection sensitivity without ADHD but we often see that they go hand inand and what this means is is that you might misinterpret things and become overly emotional about things an example would be that someone looks at you the wrong way and you immediately become panick that they hate you and what your ADHD does is it gets you stuck you're unable to zoom out and see that he looked at everybody that way or he doesn't even know you and then the emotions become overwhelming and at that point you become disregulated and the problem with that is sometimes you can misinterpret the situation or overreact to the situation and then the person may become defensive or angry and all of a sudden everybody's angry and sensitive and disrupted that's why it's important to take a step back sometimes just take a deep breath count to five see the broader picture and maybe regulate your emotions before you go down the rapit hole
```

**Metadata as supplied (views, likes, comments, duration):** `83,959 3,462 91 53`

### Revised claim review

**Claim 1:** People with ADHD often suffer from something called "rejection sensitivity dysphoria" (RSD), and rejection sensitivity can occur without ADHD but often co-occurs with it

**Verdict: Supported.** Supported as an association of rejection sensitivity; RSD is informal terminology, not a separate established DSM/ICD diagnosis. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [JUSTICE2](https://pubmed.ncbi.nlm.nih.gov/24878677/).

**Claim 2:** This can cause someone to misinterpret situations and become overly emotional — e.g., assuming someone hates them after being looked at "the wrong way"

**Verdict: Supported.** Evidence supports possible sensitivity to ambiguous criticism, not certainty that every interpretation is erroneous. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** Once emotions become overwhelming, the person becomes "dysregulated," which can lead to misinterpreting or overreacting to a situation, causing the other person to become defensive or angry, escalating the conflict

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 4:** Strategies like taking a step back, deep breathing, counting to five, and seeing the broader picture can help regulate emotions before escalating

**Verdict: Supported.** Reasonable regulation strategies, not proof that counting to five treats ADHD. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 62 — The REAL Reason Generic ADHD Strategies May Not Work For You

### Transcript

```text
Hey there. Treatment for ADHD is not one sizefits-all. That's why it can often be very frustrating when you see videos and articles and whatever else you see and you get quick tips and you think, "Oh, I've tried this. It doesn't work." Or, "Oh, that's not never going to work. That person has no idea what they're talking about." I imagine if you've you have ADHD and you've spent a lot of time trying to do different things and have gotten frustrated and felt like nothing's working, those thoughts might have popped into your head. But but here's the thing. One size does not fit all with how you approach it. It's and it's not just about the strategies. The strategies often help a lot and are a big part of it, but it's also about finding the ones that are the right fit for you and also often times when needed working with someone to actually help you to implement them and just to learn a different process to be able to approach it. So next time you're getting frustrated thinking nothing works, you know, I can't do this. Why should I even try or why should I listen to anyone that has all these strategies? Take a step back and really think about what can I do differently? The mindset itself can really help you to keep pushing forward in a positive way. But also, if something's not working, if you keep doing the same thing over and over again, it's not you're probably not going to get better. But if you take a step back, really evaluate what could work, what what could I try doing, how could I approach it differently, and not have it be just about the strategy, but about the approach of actually how you implement the strategy, that can sometimes make a big difference. So, I hope this is helpful in getting you think a little bit more about an individualized approach to ADHD treatment. [Music]
```

**Metadata as supplied (views, likes, comments, duration):** `372 2 0 86`

### Revised claim review

**Claim 1:** Generic ADHD strategies may not work because treatment for ADHD is not one-size-fits-all

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Trying quick-tip strategies from videos/articles without success doesn't necessarily mean the strategies are wrong — it may mean they weren't the right fit for that individual

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Success often depends not just on the strategies themselves, but on finding ones that fit the individual and sometimes working with someone (e.g., a professional) to implement them and learn a different process

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** If something isn't working, repeating the same approach over and over is unlikely to lead to improvement — reevaluating and adjusting the approach (not just the strategy) can make a meaningful difference

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 63 — How ADHD people can focus

### Transcript

```text
some amount of sensory input is necessary for some brains to maintain focus. So you can look at studies of people who have ADHD and if they have some kind of white noise or music in the background then it is easier for them to maintain focus. There are some people who have a lot of difficulty meditating with their eyes closed and in fact the ideal way to meditate according to some traditions is a half-litted gaze. So you're kind of looking like this where they're open a little bit and you're getting some kind of sensory input. So this is another interesting principle of the brain is that if you deprive the brain of sensory input, it will create its own sensory input. People with ADHD will self-stimulate if you force them to sit down and not get any stimulus. So if you take a kid with ADHD and you tell them force them to sit still and listen to the lecture, they'll start going like this, right? They'll start widdling.
```

**Metadata as supplied (views, likes, comments, duration):** `290,292 15,483 253 54`

### Revised claim review

**Claim 1:** Some amount of sensory input is necessary for some brains to maintain focus

**Verdict: Supported.** Evidence: [NOISE](https://pubmed.ncbi.nlm.nih.gov/38428577/).

**Claim 2:** Studies show that people with ADHD find it easier to maintain focus when there's white noise or music in the background

**Verdict: Supported.** Supported as a possible task benefit, not a guarantee for all auditory stimulation. Evidence: [NOISE](https://pubmed.ncbi.nlm.nih.gov/38428577/).

**Claim 3:** Some people have difficulty meditating with eyes fully closed, and some traditions recommend a "half-lidded gaze" allowing some sensory input during meditation

**Verdict: Excluded from scoring.** Meditation-tradition detail is outside the ADHD knowledge claim scope.

**Claim 4:** If the brain is deprived of sensory input, it will create its own sensory input, and people with ADHD will self-stimulate ("fidget"/"widdle") if forced to sit still without any stimulus

**Verdict: Unsupported.** A possible stimulation-regulation hypothesis is presented as a deterministic general mechanism. Evidence: [NOISE](https://pubmed.ncbi.nlm.nih.gov/38428577/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 64 — ADHD might not be the real problem with your brain, it might be something in your sleep.

### Transcript

```text
ADHD might not be the real problem with your brain. It might be something in your sleep that most doctors are not even looking for. Now, the reason this can get mixed up is because of the similarity in brain scans. So, I'll reveal what this is in a moment, but in ADHD, as we know, there's issues in being able to focus. You have dopamine dysregulation, like just all different things stimulate you and distract you. Uh and all that. Very similar brain scan will happen with sleep apnea. Now, it's a little bit different, but you will have the same deficits in attention, reward circuitry, and all that. And in fact, that's why the gold standard of research, a meta-analysis, has shown if you treat sleep apnea, it will reverse a lot of those same issues. So, if you think you have ADHD and you have bad sleep, you're tired, or you just have a dry mouth in the morning, make sure you talk to your doctor about getting some sort of diagnostic work. And if you do have sleep apnea, do something about it. Let me actually be helpful with very low-cost things you can do at home. Sleep on your side. Elevate the head of the bed. Incline the whole bed. Don't eat within 3 to 4 hours before bed. Do some breathing exercises. Do some tongue exercises. All of those things can reduce apnea episodes by about like anywhere from like 10% to 30% each. You just got to stack the things in the right direction. And one more thing that may help with oxygen flow is boosting nitric oxide. If you want to learn more about that, you can go to this link. Or if you're on YouTube, you can press this button over here.
```

**Metadata as supplied (views, likes, comments, duration):** `1,319 98 3 84`

### Revised claim review

**Claim 1:** ADHD might not be the real problem — it might actually be something happening in your sleep (specifically sleep apnea), which doctors often aren't checking for

**Verdict: Supported.** The possibility of an overlooked sleep-disordered-breathing contributor is supported; this is not proof that most clinicians miss it. Evidence: [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 2:** There is similarity between brain scans in ADHD and sleep apnea

**Verdict: Unsupported.** Shared circuits do not substantiate an unspecified “similar scan” comparison or diagnostic substitution. Evidence: [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 3:** Sleep apnea produces the same deficits in attention and reward circuitry as ADHD

**Verdict: Unsupported.** Some cognitive overlap is supported; an identical attention/reward deficit profile is not. Evidence: [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 4:** A "gold standard" meta-analysis has shown that treating sleep apnea will reverse a lot of these same ADHD-like issues

**Verdict: Supported.** A pediatric meta-analysis supports symptom improvement after treating sleep-disordered breathing; it is not proof of reversing all ADHD or adult deficits. Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/).

**Claim 5:** Recommends talking to a doctor about diagnostic workup if you suspect ADHD but have poor sleep, tiredness, or morning dry mouth

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd), [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/).

**Claim 6:** Sleeping on your side, elevating the head of the bed, inclining the whole bed, and avoiding eating within 3-4 hours of bed can help reduce sleep apnea episodes

**Verdict: Unsupported.** Positional measures can help selected patients; the whole bundle including a 3–4-hour food cutoff is not established as stated. Evidence: [OSAPOS](https://www.cochrane.org/evidence/CD010990_are-interventions-keep-people-sleeping-their-side-best-way-treat-obstructive-sleep-apnoea).

**Claim 7:** Breathing exercises and tongue exercises can help reduce sleep apnea episodes

**Verdict: Supported.** Possible benefit with limited certainty; not a substitute for evaluating clinically significant apnea. Evidence: [OSAEX](https://www.cochrane.org/evidence/CD013449_myofunctional-therapy-oropharyngeal-mouth-and-throat-exercises-people-obstructive-sleep-apnoea).

**Claim 8:** These interventions can reduce apnea episodes by roughly 10-30% each

**Verdict: Unsupported.** No evidence supports 10–30% improvement for each measure or adding the percentages together. Evidence: [OSAPOS](https://www.cochrane.org/evidence/CD010990_are-interventions-keep-people-sleeping-their-side-best-way-treat-obstructive-sleep-apnoea), [OSAEX](https://www.cochrane.org/evidence/CD013449_myofunctional-therapy-oropharyngeal-mouth-and-throat-exercises-people-obstructive-sleep-apnoea).

**Claim 9:** Boosting nitric oxide may help with oxygen flow relevant to sleep apnea

**Verdict: Unsupported.** A general nitric-oxide-boosting recommendation is not an established apnea treatment. Evidence: [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **4**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **4 / 9 × 100 = 44.44%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 65 — Can Sugar or Screens Cause ADHD? Here's the Real Answer

### Transcript

```text
# tactiq.io free youtube transcript
# Can Sugar or Screens Cause ADHD? Here's the Real Answer
# https://www.youtube.com/watch/_GorMlXpkYw

00:00:00.080 So, a little while ago, I did this
00:00:01.920 video. ADHD is absolutely not caused by
00:00:04.400 sugar or screens. It is a difference in
00:00:06.400 the brain. And I spoke very imprecisely.
00:00:09.440 What I was trying to say is sugar and
00:00:12.320 screens do not impact ADHD diagnosis.
00:00:16.800 So, the idea is you're not going to eat
00:00:18.880 enough sugar to create ADHD. You're
00:00:21.600 going to create a whole lot of other
00:00:22.560 things, but you're not creating ADHD.
00:00:24.240 You're not going to watch enough phone
00:00:26.400 or be on your phone for long enough to
00:00:28.480 create ADHD. If you have ADHD, are you
00:00:31.760 going to be attracted to that sugar? Oh
00:00:34.160 yeah. Are you going to be attracted to
00:00:36.000 that phone? Oh yeah. All of those
00:00:38.879 dopamine highs that you're getting from
00:00:40.480 there, they are absolutely going to be
00:00:42.320 something that you're going to be more
00:00:43.440 attracted to than other individuals of
00:00:46.000 the neurotypical variety. So, if you
00:00:48.559 think you or a loved one may be
00:00:50.079 struggling with ADHD or a learning
00:00:51.680 disability, check out our quiz at
00:00:53.280 armisassessment.ca.
00:00:56.330 [music]
```

**Metadata as supplied (views, likes, comments, duration):** `1,006 40 0 59`

### Revised claim review

INTERPRETATION FLAG: the screen statement is scored literally as a categorical causal assurance. Reading it more narrowly as no established stand-alone screen cause would make Claim 4 supported and give Label 2 instead of Label 3. The opening summary is not double-counted.

**Claim 1:** "Can Sugar or Screens Cause ADHD?" — implicitly and then explicitly answered as no

**Verdict: Excluded from scoring.** The title/opening summary repeats the sugar and screen assertions assessed in Claims 3 and 4; it is not a third independent causal assertion.

**Claim 2:** ADHD is "a difference in the brain"

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Eating sugar will not create ADHD, though it may cause "a whole lot of other things"

**Verdict: Supported.** Sugar is not established as a cause of the disorder; this does not imply diet has no health effects. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 4:** Watching enough phone/screen time will not create ADHD

**Verdict: Unsupported.** Causation is not established by the observational screen-use literature. However, the categorical assurance that exposure cannot contribute is also stronger than that evidence. This is an unsupported-certainty judgement, not a finding that screens have been proved to cause ADHD. Evidence: [MEDIA](https://pubmed.ncbi.nlm.nih.gov/36562860/).

**Claim 5:** If you have ADHD, you will likely be more attracted to sugar and screens than neurotypical individuals, because of the dopamine highs they provide

**Verdict: Unsupported.** The universal dopamine-high explanation of these preferences is unsubstantiated. Evidence: [MEDIA](https://pubmed.ncbi.nlm.nih.gov/36562860/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **1**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading** — see the limitation below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The categorical screen-causation denial is interpretation-sensitive. Observational associations do not prove that screens cause ADHD. A narrower reading as “no established stand-alone cause” would give Label 2 instead of Label 3.

---

## Video 66 — Is It Anxiety or ADHD?

### Transcript

```text
# tactiq.io free youtube transcript
# Is It Anxiety or ADHD?
# https://www.youtube.com/watch/2FTfvxJDeCs

00:00:00.080 there are certain symptoms that are
00:00:01.800 comparable amongst the illnesses making
00:00:04.759 differentiation challenging this may
00:00:07.040 make diagnosis and treatment approaches
00:00:09.000 more difficult although there is a
00:00:10.920 direct correlation between anxiety and
00:00:13.120 ADHD you can develop a coping mechanism
00:00:16.000 for one or both of them with the correct
00:00:18.320 management plan what is the relationship
00:00:20.600 between anxiety and ADHD having
00:00:23.279 difficulty focusing and being Restless
00:00:25.080 are two of the main symptoms of ADHD
00:00:27.480 that can interfere with day-to-day
00:00:29.400 living and also make it difficult to
00:00:31.759 complete tasks or fulfill commitments
```

**Metadata as supplied (views, likes, comments, duration):** `492 8 0 34`

### Revised claim review

**Claim 1:** Certain symptoms are comparable between anxiety and ADHD, making differentiation challenging, and this may complicate diagnosis and treatment

**Verdict: Supported.** Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2:** There is a "direct correlation" between anxiety and ADHD

**Verdict: Supported.** Read as association/co-occurrence, not direct causal correlation. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 3:** With an appropriate management plan, coping mechanisms can be developed for one or both conditions

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Difficulty focusing and restlessness are two of the main symptoms of ADHD that can interfere with daily living and make it difficult to complete tasks or fulfill commitments

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 67 — Understanding ADHD: Beyond the Common Misconceptions | ADHD Scapegoat Podcast #ADHD #Overwhelm

### Transcript

```text
# tactiq.io free youtube transcript
# Understanding ADHD: Beyond the Common Misconceptions | ADHD Scapegoat Podcast #ADHD #Overwhelm
# https://www.youtube.com/watch/89-AzEujsH4

00:00:00.040 you know when people say oh everybody
00:00:01.439 has a little bit of ADHD no it's like
00:00:04.720 yeah everybody pees but if you get up to
00:00:07.799 pee 60 times in a day there's probably
00:00:10.880 something wrong you know what I mean
00:00:12.440 like there's like it's a
00:00:15.960 very big difference between oh I know
00:00:20.519 I'm in a state of overwhelm as a
00:00:23.400 neurotypical person and now all of these
00:00:26.519 things are bothering me or I'm in a very
00:00:28.960 noisy you know place where people are
00:00:32.279 all with each other where people could
00:00:34.520 get overwhelmed naturally like everyone
00:00:37.680 could get overwhelmed by that but it's
00:00:40.000 being in those situations day in and day
00:00:42.440 out multiple times a day that is what
00:00:46.360 sets apart our experiences
```

**Metadata as supplied (views, likes, comments, duration):** `57 4 0 49`

### Revised claim review

**Claim 1:** The idea that "everybody has a little bit of ADHD" is misleading — using an analogy that everyone urinates, but urinating 60 times a day indicates something is genuinely wrong

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** There's a difference between a neurotypical person feeling overwhelmed occasionally in objectively overwhelming situations (e.g., a noisy, crowded place) versus experiencing that overwhelm repeatedly, day in and day out, multiple times a day

**Verdict: Supported.** Repeated impairment matters; feeling overwhelmed alone does not diagnose ADHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 68 — Adderall explained: what you need to know (and what no one tells you) 💊 #adhd #summeronshorts

### Transcript

```text
# tactiq.io free youtube transcript
# Adderall explained: what you need to know (and what no one tells you) 💊 #adhd  #summeronshorts
# https://www.youtube.com/watch/Eyv7BHr0bOA

00:00:01.280 I must have taken that aderal like 30
00:00:03.840 minutes ago.
00:00:07.200 I'm going to tell you everything that
00:00:08.160 you need to know about Adderall. So,
00:00:09.440 this medication is considered a
00:00:10.719 controlled two substance, which means it
00:00:12.480 has a high potential for abuse and
00:00:14.320 dependence. What you'll notice is at the
00:00:16.000 pharmacy, you'll probably only be able
00:00:17.520 to get a month supply at a time.
00:00:19.359 Usually, you could fill it 2 days early.
00:00:21.039 The reason for the 2-day notice is to
00:00:22.640 prevent people from stockpiling it
00:00:24.320 because actually, sometimes your
00:00:25.680 insurance will let you fill it usually
00:00:27.359 like a week early. And with this
00:00:28.560 medication, it is a firstline option for
00:00:30.880 ADHD. You want to take this in the
00:00:33.360 morning because it will possibly keep
00:00:35.200 you up at night. Initial dose is usually
00:00:36.960 5 milligs once a day for the immediate
00:00:38.719 release. And then adults for the
00:00:39.920 extended release is going to be 10 to 20
00:00:41.600 millig. And fun fact, the AAP
00:00:43.360 guidelines, which are guidelines that
00:00:44.640 pediatricians follow, don't actually
00:00:46.480 recommend dextroetamine in patients less
00:00:49.360 than or equal to 5 years old. Also, a
00:00:51.039 fun fact with these medications is that
00:00:52.640 you don't want to take them with like
00:00:54.000 acidic foods or like vitamin C, for
00:00:56.399 example, because it can actually
00:00:57.920 decrease the absorption of the aderall.
00:01:00.079 And then when it comes to tapering off
00:01:01.760 of the medication, there actually is no
00:01:04.239 tapering if you are taking the
00:01:06.159 appropriate dose. And it can cause a
00:01:08.080 decreased appetite. So to help prevent
00:01:10.000 weight loss, it's actually recommended
00:01:11.600 to have a larger breakfast in the
```

**Metadata as supplied (views, likes, comments, duration):** `815,976 41,275 2,923 74`

### Revised claim review

**Claim 1:** Adderall is considered a Schedule II controlled substance, meaning it has a high potential for abuse and dependence

**Verdict: Supported.** Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 2:** At the pharmacy you'll typically only get a month's supply at a time, and can usually fill it 2 days early to prevent stockpiling, though insurance sometimes allows filling about a week early

**Verdict: Unsupported.** Refill windows depend on law, pharmacy and insurance; no general two-day entitlement/rule was substantiated. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 3:** Adderall is a first-line option for ADHD treatment

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 4:** Take Adderall in the morning because it may keep you up at night

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 5:** Initial dose is usually 5mg once daily for immediate release, and 10-20mg for extended release in adults

**Verdict: Supported.** These are plausible low-dose starting approaches, not universal prescriptions. Official XR adult recommendation is 20 mg; doses are individualized. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 6:** AAP guidelines don't recommend dextroamphetamine in patients ≤5 years old

**Verdict: Supported.** The AAP statement concerns insufficient evidence as initial preschool medication, not an absolute ban on every specialist use. Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 7:** Don't take Adderall with acidic foods or vitamin C because it can decrease absorption

**Verdict: Supported.** Acidifying-agent interactions are real; ordinary food acidity alone does not establish that all acidic foods must be prohibited. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 8:** There is no tapering needed when stopping the medication if you're taking the appropriate dose

**Verdict: Unsupported.** Prolonged use can produce dependence/withdrawal; the unconditional stopping assurance is unwarranted. Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 9:** Adderall can cause decreased appetite, so having a larger breakfast is recommended to help prevent weight loss

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **7**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **7 / 9 × 100 = 77.78%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 69 — What Actually Causes ADHD? Dr. Vishal Kasal Explains the Real Brain Science Behind It

### Transcript

```text
# tactiq.io free youtube transcript
# What Actually Causes ADHD? Dr. Vishal Kasal Explains the Real Brain Science Behind It
# https://www.youtube.com/watch/4aJl1p8nHNw

00:00:00.400 What causes this ADHD? Is it a brain
00:00:04.960 problem that you know no normal
00:00:06.960 development?
00:00:08.559 >> So it is it is a brain problem. The they
00:00:11.280 are still trying to find out the exact
00:00:13.360 reasons but it seems to be
00:00:14.719 multiffactorial in nature. Okay. So uh
00:00:17.920 the there are three things which they
00:00:20.720 have consistently seen. Uh the
00:00:23.680 prefrontal cortex uh is the last one to
00:00:27.279 mature. In people with ADHD, they have
00:00:29.599 seen that the
00:00:32.399 gray matter thickness in the prefrontal
00:00:34.719 cortex is on the lesser side. Ability to
00:00:37.520 think is because of the gray. So that
00:00:40.079 the thickness of that is slightly
00:00:42.719 reduced in people with ADHD. Uh and uh
00:00:46.719 what they have also seen is that it
00:00:50.079 matures or the malination happens in a
00:00:52.879 delayed basis in people with ADHD.
```

**Metadata as supplied (views, likes, comments, duration):** `233 4 0 63`

### Revised claim review

**Claim 1:** ADHD is a brain-related developmental disorder

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** The exact causes of ADHD remain unknown

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** ADHD is multifactorial in nature

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** The prefrontal cortex is the last part of the brain to mature

**Verdict: Supported.** Accepted as lay shorthand for late-maturing association/prefrontal systems, not a single universal finishing date. Evidence: [MATUR](https://pubmed.ncbi.nlm.nih.gov/18024590/).

**Claim 5:** People with ADHD consistently have reduced grey-matter thickness in the prefrontal cortex

**Verdict: Unsupported.** The blanket consistent-thinning claim exceeds age/region-specific group findings. Evidence: [MATUR](https://pubmed.ncbi.nlm.nih.gov/18024590/).

**Claim 6:** The ability to think exists because of grey matter

**Verdict: Unsupported.** Thinking depends on integrated grey- and white-matter networks; this single-tissue explanation is misleading. Evidence: [MATUR](https://pubmed.ncbi.nlm.nih.gov/18024590/).

**Claim 7:** Prefrontal or cortical maturation is delayed in people with ADHD

**Verdict: Supported.** Supported as a group developmental finding, not a rule for each individual. Evidence: [MATUR](https://pubmed.ncbi.nlm.nih.gov/18024590/).

**Claim 8:** Myelination is delayed in people with ADHD

**Verdict: Unsupported.** Cortical-thickness maturation is not a direct measurement of myelination. Evidence: [MATUR](https://pubmed.ncbi.nlm.nih.gov/18024590/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **5**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **5 / 8 × 100 = 62.50%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 70 — ADHD Paralysis: The REAL Reason ADHD Brains Can’t Get Started

### Transcript

```text
# tactiq.io free youtube transcript
# ADHD Paralysis: The REAL Reason ADHD Brains Can’t Get Started
# https://www.youtube.com/watch/8SJh80h5bFE

00:00:00.000 This is a dopamine curve. This line here
00:00:02.320 is baseline, how much dopamine is
00:00:03.880 available in the brain at any given
00:00:05.160 time. For neurotypical brains, dopamine
00:00:07.160 usually rises when they start a task and
00:00:08.920 stays steady because their brain can
00:00:10.160 track the reward at the end. Then, once
00:00:12.200 the task is done, it drops off gently,
00:00:14.200 sometimes there's a little dopamine
00:00:15.440 trough, a little less motivation after,
00:00:17.440 sometimes not. But ADHD brains are much
00:00:19.560 different. They often start from a much
00:00:21.160 lower baseline, which means we may need
00:00:22.800 more dopamine activation to get going in
00:00:24.640 the first place. This is a huge reason
00:00:26.880 why task initiation can feel so dang
00:00:28.640 hard. And that also explains why we can
00:00:30.800 suddenly start when something is
00:00:32.360 interesting because interest boosts
00:00:33.720 dopamine and helps us get over that
00:00:35.120 hump. Why we become suddenly so
00:00:37.440 productive under pressure? Because
00:00:38.640 urgency boosts adrenaline, which pairs
00:00:40.120 with dopamine and helps us get over that
00:00:41.600 start hump, as well.
00:00:43.160 So, when an ADHD person can't start,
00:00:44.680 it's not necessarily that they don't
00:00:45.840 want to. Sometimes, their brain just
00:00:47.560 doesn't have enough activation to cross
00:00:49.440 that start line.
```

**Metadata as supplied (views, likes, comments, duration):** `37,511 2,644 29 51`

### Revised claim review

**Claim 1:** In neurotypical brains, dopamine rises when a person begins a task, remains steady because the brain tracks the eventual reward, and gently decreases after completion

**Verdict: Unsupported.** The schematic curve is not a validated general neurotypical task response. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** ADHD brains generally begin from a much lower baseline dopamine level than neurotypical brains

**Verdict: Unsupported.** No universal low-baseline dopamine measurement establishes ADHD. Evidence: [STIM](https://www.nature.com/articles/1301164), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Difficulty initiating tasks in ADHD is substantially caused by insufficient dopamine activation preventing the brain from crossing a neurological “start line”

**Verdict: Unsupported.** A literal activation threshold is unsubstantiated. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Interest can make it easier for a person with ADHD to begin a task because interest increases dopamine enough to overcome the proposed start threshold

**Verdict: Unsupported.** Interest may aid engagement; the proposed dopamine-threshold mechanism is not demonstrated. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Urgency makes people with ADHD suddenly productive because it increases adrenaline, which combines with dopamine and enables them to cross the task-initiation threshold

**Verdict: Unsupported.** Urgency can affect engagement, but this specified adrenaline/dopamine threshold account is not established. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 6:** When a person with ADHD cannot begin a task, this does not necessarily mean that they do not want to perform it

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **1**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **1 / 6 × 100 = 16.67%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 71

**Title:** ADHD Isn’t a Disease — It’s a Childhood Adaptation | Gabor Maté Explains  
**URL:** https://www.youtube.com/shorts/Y2xh25ZCBFE  
**Views:** 226,045  
**Likes:** 6,413  
**Comments:** 161  
**Duration:** 47 seconds

**Transcript:**

> I can tell you about my own ADHD. And this is where we go back to childhood again. My mother didn't abuse me. She did her best to look after me, but she was stressed, depressed, terrorized, grief-stricken. I'm picking that up as a sensitive infant. Can I fight back, change the situation, or escape? No, none of those. What can I do? Nothing I can do. My brain will tune out as a way of dealing with the stress. So that tuning out, that absent-mindedness, that desire to scatter your attention all over the place, that's not a disease. They say it's an inherited disease. The hell it is. It begins as a coping mechanism which then gets programmed into the brain. And as a lot of these early coping mechanisms function, they help you in the short term, create problems in the long term. And ADD is one of these examples.

### Revised claim review

**Claim 1:** ADHD begins as a coping mechanism in which a child’s brain tunes out in response to early stress, and this mechanism becomes programmed into the brain

**Verdict: Unsupported.** Early adversity can matter without ADHD being exclusively a learned coping mechanism. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD is not inherited

**Verdict: Unsupported.** Denial of inherited liability conflicts with genetic evidence. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** ADHD-related absent-mindedness and scattered attention are not manifestations of a neurodevelopmental disorder

**Verdict: Unsupported.** The general denial of neurodevelopmental disorder is incorrect. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 72

**Title:** ADHD Myths Busted: Understanding the Real Condition  
**URL:** https://www.youtube.com/shorts/dwN-SQSzjZE  
**Views:** 947  
**Likes:** 9  
**Comments:** 1  
**Duration:** 48 seconds

**Status:** # tactiq.io free youtube transcript
# ADHD Myths Busted: Understanding the Real Condition #shorts #adhd #mentalhealth
# https://www.youtube.com/watch/dwN-SQSzjZE

00:00:00.000 As you heard today, we are talking all
00:00:01.880 about ADHD, a term we hear about all the
00:00:04.480 time
00:00:05.600 everywhere and anywhere.
00:00:07.400 15 and 1/2 million adults in the US
00:00:09.960 diagnosed, yet so many people still
00:00:11.880 don't fully understand what it actually
00:00:13.320 is. And he broke down some of the major
00:00:15.640 myths about ADHD like how it's not just
00:00:19.200 a focus issue, that it's highly genetic,
00:00:22.200 that there is early signs people miss
00:00:24.480 like when people talk too much
00:00:27.510 >> [laughter]
00:00:28.560 >> or they're often misdiagnosed as anxiety
00:00:31.600 or depression and how it shows up in
00:00:33.000 relationships. I think if you've ever
00:00:34.960 had questions about ADHD, this is the
00:00:36.720 one to listen to.
00:00:38.440 The breakthrough comes when you stop
00:00:40.200 fighting yourself and start working with
00:00:42.840 your brain instead of against it.
00:00:46.400 Oh, boy.

### Revised claim review

**Claim 1:** Approximately 15.5 million American adults have been diagnosed with ADHD

**Verdict: Supported.** Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 2:** ADHD is not merely a problem with focusing

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** ADHD is highly genetic

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Excessive talking can be an early ADHD sign that people overlook

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** ADHD is often mistaken for anxiety or depression

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 6:** ADHD can affect relationships

**Verdict: Supported.** Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 73

**Title:** NEW ADHD Medication: Centanafadine (Simtriyo) Explained  
**URL:** https://www.youtube.com/shorts/Ua7Pn_iQUFo  
**Views:** 68,688  
**Likes:** 5,582  
**Comments:** 352  
**Duration:** 71 seconds

**Transcript:**

> Did you guys see that we have a new medication for ADHD? This is a new stimulant medication. Instead of targeting just dopamine and norepinephrine, this new medication is targeting three neurotransmitters. It’s Monday, and you know what time it is. It’s time for drug of the day. So today’s medication that we’re going to talk about is serdexmethylphenidate, which is the generic for Azstarys. This just got FDA approved, so please, if I’m saying this wrong, don’t judge me. This is the first FDA-approved medication in a brand-new class of medications called NDSRI, which stands for norepinephrine, dopamine, serotonin reuptake inhibitor. Try saying that five times fast. This medication can be used for ADHD in adults as well as children who are six years of age and weigh at least 20 kg. The starting dose for adults is 210 mg by mouth every morning, and you can increase it to a maximum of 280 mg per day. How this medication works is it’s going to increase norepinephrine, so you’re going to have more alertness and be more attentive. It’s also going to increase dopamine, which is really great for motivation and reward processing. Then there’s serotonin, which honestly isn’t well documented for its purpose in ADHD, but it’s believed that it will probably help with impulsivity and controlling behaviours and emotions. When it comes to side effects, there will be decreased appetite, insomnia, dry mouth, and nausea. If you’re wondering if it will be a controlled substance like Adderall or Vyvanse, we actually don’t know yet because it hasn’t been classified by the DEA, but most likely it will probably be a controlled substance.

### Revised claim review

IDENTITY-CONFLICT FLAG: provisional scoring follows the supplied transcript literally. Several details match Simtriyo in the title instead. No video or transcription was checked or corrected; the intended drug must be resolved by the author before treating this label as final.

**Claim 1 — clarified extraction:** The medication named as Azstarys/serdexmethylphenidate is an FDA-approved stimulant for ADHD.

*Original annotation wording:* Centanafadine (Simtriyo) is a newly FDA-approved stimulant medication for ADHD

**Verdict: Supported.** Azstarys is an approved CNS stimulant. Without a publication date, the relative word new is not independently scored as false. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 2 — clarified extraction:** The named medication belongs to the new norepinephrine–dopamine–serotonin reuptake-inhibitor class.

*Original annotation wording:* Centanafadine inhibits the reuptake of norepinephrine, dopamine, and serotonin and belongs to the NDSRI class

**Verdict: Unsupported.** Triple reuptake inhibition describes centanafadine, not the Azstarys combination named in the transcript. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 3:** The medication being discussed is serdexmethylphenidate, the generic drug in Azstarys

**Verdict: Unsupported.** Azstarys combines serdexmethylphenidate with dexmethylphenidate; one ingredient is not its interchangeable generic name. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 4 — clarified extraction:** The named medication can be used for adults and children aged six or older who weigh at least 20 kg.

*Original annotation wording:* Simtriyo is indicated for adults and for children aged six or older who weigh at least 20 kg

**Verdict: Supported.** An eligible subset is described, but 20 kg is not an Azstarys indication threshold. The text does not say only these patients. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 5 — clarified extraction:** The named medication starts at 210 mg each morning in adults and can increase to 280 mg daily.

*Original annotation wording:* The recommended adult starting dose is 210 mg each morning and may be increased to a maximum of 280 mg daily

**Verdict: Unsupported.** The 210–280 mg regimen belongs to Simtriyo, not Azstarys. This medication/dose mismatch is material. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 6:** Increasing norepinephrine produces alertness and attention, increasing dopamine improves motivation and reward processing, and increasing serotonin probably improves impulsivity and emotional control

**Verdict: Unsupported.** The transmitter-by-transmitter account is not an established clinical mechanism for the named medication. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 7 — clarified extraction:** Decreased appetite, insomnia, nausea and dry mouth can occur with the named medication.

*Original annotation wording:* Decreased appetite, insomnia, nausea, and dry mouth are side effects of Simtriyo

**Verdict: Supported.** These adverse effects can occur with the named stimulant combination. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

**Claim 8 — clarified extraction:** The named medication has not yet been assigned a federal controlled-substance schedule.

*Original annotation wording:* At the time of the video, Simtriyo’s federal controlled-substance schedule had not yet been assigned, although scheduling was expected

**Verdict: Unsupported.** Azstarys is Schedule II; the pending-scheduling wording belongs to the initial Simtriyo label. Evidence: [AZST](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663), [SIM](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **3**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **3 / 8 × 100 = 37.50%**.
- **Reviewed label: Label 3 — Moderately misleading** — see the limitation below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** Title/drug-identity conflict: the supplied transcript names Azstarys/serdexmethylphenidate but several details match Simtriyo/centanafadine. Label 3 is provisional for the literal supplied transcript, not a finding about an authenticated recording.

---

## Video 74

**Title:** The unexpected side effects of using ADHD drugs  
**URL:** https://www.youtube.com/shorts/qc59D-j_K4o  
**Views:** 306,207  
**Likes:** 5,103  
**Comments:** 319  
**Duration:** 60 seconds

**Status:** # tactiq.io free youtube transcript
# The unexpected side effects of using ADHD drugs
# https://www.youtube.com/watch/qc59D-j_K4o

00:00:00.040 now there's a lot of hype around drugs
00:00:01.560 like Aderall and Ridin you're only
00:00:03.399 supposed to use them if a doctor
00:00:04.720 prescribes them for something like ADHD
00:00:06.839 but the reality is lots of people
00:00:08.920 without ADHD take them especially
00:00:10.960 college students they're often seen as
00:00:12.719 these magical pills that can make you
00:00:14.480 study longer Focus harder and cram more
00:00:16.800 info into your brain but is that true
00:00:19.640 and aren't there some dangerous side
00:00:21.199 effects with these drugs most ADHD drugs
00:00:24.439 are stimulants they stimulate and
00:00:26.320 activate your central nervous system
00:00:27.800 within 15 or 20 minutes of popping a
00:00:29.480 pill caffeine is also a stimulant but
00:00:32.159 ADHD drugs are a lot more powerful like
00:00:35.040 Aderall which is one of the most
00:00:36.760 commonly prescribed stimulant
00:00:37.960 medications in the US the active
00:00:40.200 ingredient is a version of amphetamine
00:00:42.280 which has been around a long time
00:00:44.680 remember it's illegal to use ad orall
00:00:46.800 without a prescription and you can
00:00:48.079 experience some really annoying side
00:00:49.760 effects like headaches dry mouth high
00:00:51.920 blood pressure increased heart rate
00:00:53.480 sleep problems weight loss irritability
00:00:55.920 changes in sex drive and erectile
00:00:58.760 dysfunction

### Revised claim review

**Claim 1:** Adderall and Ritalin should be used only when prescribed by an appropriate clinician

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 2:** People without ADHD, particularly college students, sometimes use prescription stimulants nonmedically to study

**Verdict: Supported.** Evidence: [MISUSE](https://pmc.ncbi.nlm.nih.gov/articles/PMC2951617/).

**Claim 3:** Most ADHD medications are stimulants

**Verdict: Supported.** Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** ADHD stimulants activate the central nervous system within 15–20 minutes of taking a pill

**Verdict: Unsupported.** Onset varies by medication and formulation; 15–20 minutes is not a general rule. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 5:** Caffeine is a stimulant, but prescription ADHD stimulants generally exert stronger therapeutic central-nervous-system effects

**Verdict: Supported.** A qualitative comparison, not a caffeine-to-prescription-drug potency conversion. Evidence: [STIM](https://www.nature.com/articles/1301164), [CAFF](https://www.mdpi.com/2076-3425/13/9/1304).

**Claim 6:** Adderall is a commonly prescribed stimulant containing amphetamine salts

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81).

**Claim 7:** Using or possessing Adderall without a prescription is unlawful in the United States

**Verdict: Supported.** The claim is assessed in its stated United States context. Evidence: [DEA](https://www.dea.gov/factsheets/stimulants), [MISUSE](https://pmc.ncbi.nlm.nih.gov/articles/PMC2951617/).

**Claim 8:** Possible stimulant adverse effects include headache, dry mouth, elevated blood pressure or heart rate, insomnia, weight loss, irritability, libido changes, and erectile dysfunction

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **7**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **7 / 8 × 100 = 87.50%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 75

**Title:** Is It Possible To Have ADHD & OCD? | Dr. Daniel Amen  
**URL:** https://www.youtube.com/shorts/G5mL5Xg1VgA  
**Views:** 145,507  
**Likes:** 6,224  
**Comments:** 228  
**Duration:** 53 seconds

**Status:** # tactiq.io free youtube transcript
# Is It Possible To Have ADHD & OCD? | Dr. Daniel Amen
# https://www.youtube.com/watch/G5mL5Xg1VgA

00:00:00.550 so can I have ADHD and OCD at the same
00:00:05.890 time all the time I see it particularly
00:00:09.730 in children and grandchildren of
00:00:12.370 Alcoholics what we see in the brain is
00:00:15.130 the middle front part of the brain works
00:00:18.190 too hard and an area called the inferior
00:00:21.609 orbital prefrontal cortex doesn't work
00:00:23.770 hard enough so it's like you have low
00:00:26.470 levels of both serotonin and dopamine
00:00:30.130 and early in my career I'd use a
00:00:32.950 combination of Prozac and Ritalin
00:00:35.190 miraculous for some patients now I'll
00:00:38.530 use more supplement options like 5-HTP
00:00:42.510 and Rhodiola ashwagandha ginseng and
00:00:47.530 just to help balance the brain happens
00:00:51.010 all the time

### Revised claim review

**Claim 1:** ADHD and OCD can coexist

**Verdict: Supported.** Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 2:** Co-occurring ADHD and OCD occurs particularly among the children and grandchildren of people with alcoholism

**Verdict: Unsupported.** The proposed special predominance among descendants of people with alcoholism was not established. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 3:** Co-occurring ADHD and OCD is explained by an overactive middle-frontal brain region, an underactive inferior orbital prefrontal cortex, and low serotonin and dopamine

**Verdict: Unsupported.** Comorbidity is not established by this scan/neurotransmitter story. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** 5-HTP, rhodiola, ashwagandha, and ginseng balance the brain and treat co-occurring ADHD and OCD

**Verdict: Unsupported.** The listed supplement combination is not an established treatment for this comorbidity. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 76

**Title:** The truth behind lying and ADHD  
**URL:** https://www.youtube.com/shorts/f8ozwm7-7c4  
**Views:** 7,137  
**Likes:** 253  
**Comments:** 6  
**Duration:** 64 seconds

**Status:** # tactiq.io free youtube transcript
# The truth behind lying and ADHD
# https://www.youtube.com/watch/f8ozwm7-7c4

00:00:00.160 We've all heard of fight, flight, or
00:00:02.000 freeze, but researchers have now added a
00:00:03.679 fourth F specifically for ADHDers. And
00:00:06.080 that F is fib. That's right. ADHDers,
00:00:08.720 especially children and teenagers, are
00:00:10.559 known to lie. But they don't do this
00:00:12.160 because of a personality defect. They do
00:00:14.000 this usually for self-preservation.
00:00:15.519 ADHDers, by the time that they are 10
00:00:17.680 years old, they've heard over 20,000
00:00:19.199 corrective messages. This means that
00:00:20.400 they are used to getting in trouble,
00:00:21.760 being disciplined, being redirected,
00:00:23.519 told that they are doing things wrong,
00:00:24.960 and being compared to people who can do
00:00:26.320 things right. ADHD, children, youth,
00:00:28.240 young adults. Sometimes even adults
00:00:29.760 might lie because they're panicking and
00:00:31.119 they need more information. They don't
00:00:32.159 know what story you're looking for and
00:00:33.520 they need more time to consider all of
00:00:35.040 the facts. Sometimes it's because they
00:00:36.880 don't want to be in trouble. They're
00:00:37.920 delaying the inevitable. They're in
00:00:39.280 trouble again. Or it may just be because
00:00:41.440 it's so damaging to their self-esteem to
00:00:43.200 know that one more time they
00:00:44.320 disappointed someone in their life. It's
00:00:45.600 not that we just want to accept lying,
00:00:47.120 but we do want to have an awareness to
00:00:49.280 why an ADHD's immediate impulse reaction
00:00:52.160 is to lie. It's not because they want to
00:00:54.399 be bad or dishonest. It's usually
00:00:56.079 because they are going into protection
00:00:57.840 mode and trying to figure out how to
00:00:59.440 handle this very uncomfortable situation
00:01:01.120 that they find themselves in again and
00:01:02.879 again and

### Revised claim review

**Claim 1:** Researchers have added “fib” as an ADHD-specific fourth response alongside fight, flight, and freeze

**Verdict: Unsupported.** No validated ADHD-specific fourth defensive response called fib was established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** People with ADHD, particularly children and teenagers, are characteristically known to lie

**Verdict: Unsupported.** ADHD is not defined by habitual dishonesty. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** When people with ADHD lie, the usual cause is self-preservation rather than any other motivation

**Verdict: Unsupported.** Diagnosis does not establish a usual motive for lying. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** Every child with ADHD has received more than 20,000 corrective messages by age ten

**Verdict: Unsupported.** The universal age-ten 20,000-message statistic was not substantiated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** People with ADHD lie because panic prevents them from processing the facts or determining what answer another person wants

**Verdict: Unsupported.** Possible individual motives are not an established ADHD-wide mechanism. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 6:** An ADHD person’s immediate impulsive reaction is usually to lie as a form of protection from punishment or damaged self-esteem

**Verdict: Unsupported.** The usual-response stereotype is unsupported. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **0**; unsupported: **6**; excluded: **0**.
- Supported-claim percentage: **0 / 6 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 77

**Title:** ADD vs ADHD: What's the Real Difference?  
**URL:** https://www.youtube.com/shorts/EzZOFz0lj20  
**Views:** 438  
**Likes:** 10  
**Comments:** 0  
**Duration:** 53 seconds

**Status:** # tactiq.io free youtube transcript
# ADD vs ADHD: What's the Real Difference? #shorts
# https://www.youtube.com/watch/EzZOFz0lj20

00:00:00.000 I get this a lot. Um, and would you mind
00:00:02.560 kind of clarifying for us what the
00:00:03.960 differences are and whether or not that
00:00:05.520 difference is uh meaningful?
00:00:08.240 >> Yeah, so
00:00:09.600 ADD stands for attention deficit
00:00:11.880 disorder, and that's just kind of a
00:00:13.560 general umbrella term. ADHD is attention
00:00:17.160 deficit hyperactivity disorder, and so
00:00:19.800 uh
00:00:20.680 there's not a huge difference in in my
00:00:23.400 mind. That's why I tend to use them kind
00:00:25.000 of interchangeably because even when we
00:00:27.600 look at uh the diagnosis and we we
00:00:30.520 diagnose according to the ICD-10 and the
00:00:33.800 DSM, uh there's actually subtypes. So,
00:00:36.240 even though they say ADHD,
00:00:39.240 the subtype would be predominantly uh
00:00:41.600 inattentive, for example, rather than um
00:00:44.280 hyperactive or um yeah.
00:00:46.600 >> So, if it's So, if it's ADHD
00:00:48.120 predominantly inattentive, that is
00:00:50.040 synonymous with ADD, is what you're
00:00:51.800 saying.

### Revised claim review

**Claim 1:** ADD stands for attention deficit disorder

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 2:** ADHD stands for attention-deficit/hyperactivity disorder

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 3:** ADD is commonly used informally as an umbrella term or interchangeably with ADHD

**Verdict: Supported.** Historical/informal usage; ADD is not a separate current DSM diagnosis. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 4:** Diagnostic systems distinguish different ADHD symptom presentations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 5:** What people call ADD generally corresponds to ADHD, predominantly inattentive presentation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 78

**Title:** Autism, ADHD & Down Syndrome Are Not the Same — Understanding the Real Medical Differences  
**URL:** https://www.youtube.com/shorts/h2676KiKjXE  
**Views:** 46,836  
**Likes:** 738  
**Comments:** 8  
**Duration:** 74 seconds

**Status:** # tactiq.io free youtube transcript
# Autism, ADHD & Down Syndrome Are Not the Same — Understanding the Real Medical Differences |Gobinath
# https://www.youtube.com/watch/h2676KiKjXE

00:00:00.160 Autism,
00:00:02.000 ADHD, Down syndrome,
00:00:09.280 ADHD,
00:00:11.920 ADHD.
00:00:14.080 It is can occur along with autism.
00:00:18.320 Separate condition which can be treated
00:00:20.720 with medication. ADHD
00:00:25.359 hyperactive child
00:00:32.479 only therapy.
00:00:45.920 Down syndrome is a chromosome
00:00:48.879 abnormality.
00:00:50.640 There is a chromosome
00:00:55.680 full body every system is affected. So
00:00:58.640 that is a different condition. They may
00:01:00.559 also have mental retardation or heart
00:01:03.520 problem
00:01:05.119 separate neurodyivergent
00:01:07.439 ADHD autism learning disabilities
00:01:11.119 separate condition. Red.

### Revised claim review

The fragment “ADHD hyperactive child only therapy” is ambiguous and was not reconstructed into an additional treatment claim.

**Claim 1:** ADHD can coexist with autism

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** ADHD is a separate condition that can be treated with medication

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Down syndrome is caused by a chromosomal abnormality

**Verdict: Excluded from scoring.** Standalone Down-syndrome background is outside the ADHD coding unit. Evidence: [DOWN](https://www.nichd.nih.gov/health/topics/factsheets/downsyndrome).

**Claim 4:** Down syndrome affects every bodily system

**Verdict: Excluded from scoring.** Outside the ADHD denominator; chromosome involvement does not mean every organ is clinically affected. Evidence: [DOWN](https://www.nichd.nih.gov/health/topics/factsheets/downsyndrome).

**Claim 5:** People with Down syndrome may have intellectual disability or congenital heart problems

**Verdict: Excluded from scoring.** Standalone non-ADHD background; not scored as misinformation. Evidence: [DOWN](https://www.nichd.nih.gov/health/topics/factsheets/downsyndrome).

**Claim 6:** ADHD, autism, learning disabilities, and Down syndrome are separate conditions

**Verdict: Supported.** Distinct conditions may coexist. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [DOWN](https://www.nichd.nih.gov/health/topics/factsheets/downsyndrome).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **3**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 79

**Title:** ADHD Is Not Just a Superpower (and I Will Not Pretend)  
**URL:** https://www.youtube.com/shorts/II6-UVRHCW8  
**Views:** 114  
**Likes:** 1  
**Comments:** 0  
**Duration:** 53 seconds

**Status:** # tactiq.io free youtube transcript
# ADHD Is Not Just a Superpower (and I Will Not Pretend)
# https://www.youtube.com/watch/II6-UVRHCW8

00:00:00.000 Rejection sensitive dysphoria is one of
00:00:02.200 the big reasons why I could never say
00:00:04.720 that ADHD is just a superpower.
00:00:07.520 Are there parts of my experience, my
00:00:10.280 family members experience that are a
00:00:12.760 superpower that I wouldn't trade for the
00:00:14.720 world? Absolutely.
00:00:17.030 >> [laughter]
00:00:17.120 >> Absolutely. The creativity, the
00:00:19.640 problem-solving, the curiosity, um the
00:00:22.880 excitement.
00:00:24.400 Uh there are so many aspects of having
00:00:26.840 ADHD that you couldn't pay me. There's
00:00:30.000 not enough money in the world for me to
00:00:31.920 give it up.
00:00:34.240 But there are parts of the experience,
00:00:36.280 unchangeable parts of the experience of
00:00:38.800 ADHD
00:00:40.680 that
00:00:43.320 are so hard and painful and debilitating
00:00:47.080 that I could never just describe the
00:00:49.280 experience as being a superpower.

### Revised claim review

**Claim 1:** Rejection-sensitive experiences can be particularly distressing for some people with ADHD

**Verdict: Supported.** Rejection-related distress is an associated experience, not a diagnostic subtype. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** Creativity, problem-solving ability, curiosity, and excitement are inherent ADHD “superpowers”

**Verdict: Excluded from scoring.** Personal/family strengths and values were incorrectly generalized in the annotation.

**Claim 3:** ADHD can involve painful and debilitating impairment

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** The painful or debilitating parts of ADHD are unchangeable

**Verdict: Excluded from scoring.** A personal description of valued and painful experiences does not assert that treatment never helps.

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **2**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 80

**Title:** ADHD + Autism = AuDHD. Here's what that can really feel like…  
**URL:** https://www.youtube.com/shorts/wJT9vX_zDck  
**Views:** 153,238  
**Likes:** 6,153  
**Comments:** 174  
**Duration:** 58 seconds

**Transcript:**

> ADHD and autism frequently co-occur. Many people with one or the two diagnoses show elevated traits of both ADHD and autism. Common experiences for ADHD and autism include sensory differences, intense focus on specific interests, rejection sensitivity, executive dysfunction, sleep issues, and emotional regulation. Someone with ADHD is more likely to seek out novelty and make more impulsive decisions, whereas an autistic person is more likely to crave routine, structure, and order. If someone is autistic and has ADHD, they’re known as AuDHD. They may experience an internal struggle and tension between their competing autistic and ADHD traits and a heightened experience of shared traits.

### Revised claim review

**Claim 1:** ADHD and autism frequently co-occur

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** People diagnosed with either condition may show elevated traits associated with the other

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** Sensory differences, executive dysfunction, sleep problems, and emotional-regulation difficulties can occur in both ADHD and autism

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** Intense focus on particular interests can occur in both ADHD and autism

**Verdict: Supported.** Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 5:** Rejection sensitivity is a common feature of both ADHD and autism

**Verdict: Unsupported.** Reports of rejection distress do not establish that it is common in both populations. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 6:** People with ADHD are more likely to seek novelty and make impulsive decisions, whereas autistic people are more likely to prefer routine, structure, and order

**Verdict: Supported.** Broad tendencies, not universal opposites. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 7:** “AuDHD” is a term for a person who has both autism and ADHD

**Verdict: Supported.** Informal combined term, not an additional official diagnosis. Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 8:** Co-occurring autism and ADHD can produce tension between apparently competing traits and a heightened burden from overlapping difficulties

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **7**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **7 / 8 × 100 = 87.50%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 81

**Title:** 13 Ways ADHD Affects Eating Habits #adhd  
**URL:** https://www.youtube.com/shorts/WhUCpl7Ogg4  
**Views:** 7,252  
**Likes:** 530  
**Comments:** 16  
**Duration:** 175 seconds

**Transcript:**

> Here are 13 ways in which ADHD can affect your eating habits. Number one: people with ADHD often have really poor body proprioception, which means that knowing when you're hungry, knowing when you're full, and what that feels like can be really challenging. Number two: really common medications for ADHD, such as Adderall and Vyvanse, can really suppress appetite, which means that trying to rely on hunger cues alone can lead to undereating. Number three: time blindness and hyperfocus can make it really challenging to act on hunger cues when they do arise. Number four: people with ADHD often have a hard time prioritizing things appropriately, so if you notice that you are hungry but you are doing something that your brain says is more important, it can be really difficult to prioritize acting on hunger unless that cue is really intense. Number five: people with ADHD often do really well with routines and structure; however, they also have a really strong need for novelty, which makes meal planning and meal preparation challenging. One part of your brain wants to prepare everything so you do not have to think about it and can eat the same thing every day, while the other part cannot have the same thing every day. Number six: unless that food is a hyperfixation food, at which point you must eat the same thing every day until, suddenly and without warning, the sight of that food makes you want to be sick. Number seven: not getting enough fuel during the day because you are focused on other things, or because your appetite is poor, can affect focus and executive function, making it harder to choose more nourishing, substantial meals in the evening. Number eight: having nourishing things to eat during the day may sound simple, but it requires many steps, which can be overwhelming and exhausting, lead to task avoidance, and cause many people with ADHD to rely on convenience food or takeout. Number nine: cooking can be overstimulating for many people with ADHD because of the sounds, smells, and visual mess. Number ten: food is an accessible and reliable way to boost dopamine when you feel burnt out, which many people with ADHD chronically are, so snacking is probably not merely a lack of willpower or boredom but is meeting core needs. Number eleven: because food can reliably and easily boost dopamine, many people may use it to help with task initiation and completion. Number twelve: for some people with ADHD, food can be a stimming behaviour and help meet stimulation needs. Number thirteen: for many people, eating can feel like the most accessible activity when stuck in “waiting mode.” Because of these dynamics, binge eating is common in the ADHD community.

### Revised claim review

**Claim 1 — clarified extraction:** People with ADHD often have poor “proprioception,” defined as knowing hunger and fullness.

*Original annotation wording:* People with ADHD often have impaired awareness of hunger and fullness signals

**Verdict: Unsupported.** Hunger/fullness awareness is interoception, not proprioception as stated. Evidence: [INTERO](https://pubmed.ncbi.nlm.nih.gov/39905593/).

**Claim 2:** Common stimulant medications such as Adderall and Vyvanse can suppress appetite, and relying only on hunger cues may therefore contribute to undereating

**Verdict: Supported.** Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Time-management difficulties and prolonged absorption in an activity can make it difficult for a person with ADHD to notice or act on hunger cues

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 4:** ADHD-related executive-function and prioritization difficulties can cause a person to postpone eating until hunger becomes intense

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** A combination of reliance on routine and desire for novelty can make meal planning and preparation difficult for people with ADHD

**Verdict: Unsupported.** This opposing-routine/novelty explanation for meal planning was not established. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 6:** People with ADHD characteristically eat one “hyperfixation food” repeatedly and then develop a sudden aversion to it

**Verdict: Unsupported.** The sudden food-aversion cycle is not an established characteristic ADHD pattern. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 7:** Undereating can impair attention and executive performance and make later food decisions more difficult

**Verdict: Supported.** Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 8:** The multiple executive steps involved in obtaining and preparing food can overwhelm some people with ADHD and increase reliance on convenience food or takeout

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 9:** Sounds, smells, and visual clutter during cooking can be overstimulating for people with ADHD

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 10:** Food reliably boosts dopamine in a way that explains ADHD-related snacking and shows that the behaviour is meeting core neurological needs

**Verdict: Unsupported.** Reward effects do not establish correction of an ADHD dopamine deficit. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [STIM](https://www.nature.com/articles/1301164).

**Claim 11:** People with ADHD use food to initiate and complete tasks specifically because food boosts dopamine

**Verdict: Unsupported.** This specific neurological explanation of task-linked eating is not established. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [STIM](https://www.nature.com/articles/1301164).

**Claim 12:** Eating is an ADHD “stimming” behaviour that meets stimulation needs

**Verdict: Unsupported.** A possible individual description does not establish an ADHD clinical mechanism. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 13:** Binge eating is more common among people with ADHD

**Verdict: Supported.** An association, not an inevitable eating pattern. Evidence: [EATING](https://pubmed.ncbi.nlm.nih.gov/27859581/).

### Revised result

- Eligible fact-checkable claims: **13**
- Supported: **7**; unsupported: **6**; excluded: **0**.
- Supported-claim percentage: **7 / 13 × 100 = 53.85%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 82

**Title:** For ADHD, Motivation Is the Wrong Fuel  
**URL:** https://www.youtube.com/shorts/b8eHtXxUGQI  
**Views:** 968  
**Likes:** 20  
**Comments:** 0  
**Duration:** 28 seconds

**Transcript:**

> Stop waiting to feel motivated. Motivation does not work for an ADHD brain; it is the wrong fuel. Your ADHD brain works on urgency, importance, interest, novelty, and challenge, none of which are motivation. We therefore have to manufacture something to make a potentially boring task feel more urgent. This can mean telling someone it will be done by a deadline. It can also mean body doubling. Make the boring task urgent and your brain will switch on.

### Revised claim review

**Claim 1:** Motivation does not work for an ADHD brain and is the “wrong fuel”

**Verdict: Unsupported.** Motivation is not absent or inapplicable to ADHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** ADHD brains operate on urgency, importance, interest, novelty, and challenge rather than motivation

**Verdict: Unsupported.** These influences overlap with motivation and do not constitute a validated exclusive fuel list. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Creating urgency through a deadline or using body doubling will switch an ADHD brain on

**Verdict: Unsupported.** A deadline or company may help individuals but cannot reliably switch the brain on. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 83

**Title:** What 70% of ADHD Diagnoses Get Wrong  
**URL:** https://www.youtube.com/shorts/PRouUk1Ge9I  
**Views:** 56  
**Likes:** 3  
**Comments:** 0  
**Duration:** 63 seconds

**Transcript:**

> The majority of people—truly, around 70%—who come in with an ADHD diagnosis, or who are self-proclaimed ADHD, do not have a neurological ADHD pattern at all. In our world, we look at something called a theta-beta ratio: how much theta production there is relative to beta. Most people think they have ADHD because they are hyperactive, cannot sit still, are easily bored, and so on. A true ADHD person is actually swimming in their own theta. They are in a slower, calmer, more creative, more relaxed state. You cannot be slow, tired, and lethargic during the day, so the brain constantly tries to put itself into an alert state. It produces all this little beta, but it is not sustainable. That is the classic pattern, which most people honestly do not have. Usually, they have a very fast processing speed and a lot of high beta, so it is hard to sit still, but it is a completely different pattern.

### Revised claim review

**Claim 1:** Around 70% of people presenting with an ADHD diagnosis or self-identifying as having ADHD do not have the real neurological ADHD pattern

**Verdict: Unsupported.** The stated 70% false-diagnosis rate is not established. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** A theta-to-beta EEG ratio can identify whether a person has “true” ADHD

**Verdict: Unsupported.** Theta/beta EEG ratio must not replace clinical diagnosis. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** A true ADHD person has excessive theta activity and is characteristically slower, calmer, more creative, and more relaxed

**Verdict: Unsupported.** No single theta pattern or calm/creative personality defines true ADHD. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** The ADHD brain compensates for being slow and lethargic by producing small bursts of beta activity that cannot be sustained

**Verdict: Unsupported.** The compensatory-burst story is not an established mechanism. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** The elevated-theta pattern is the classic real ADHD pattern, while people with high beta and fast processing who cannot sit still have a completely different condition

**Verdict: Unsupported.** Hyperactive ADHD cannot be ruled out using this proposed typology. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **0**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **0 / 5 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 84

**Title:** ADHD and Sleep: Why You Can’t Just “Go to Bed Earlier”  
**URL:** https://www.youtube.com/shorts/HBwhrVp60co  
**Views:** 1,560  
**Likes:** 170  
**Comments:** 13  
**Duration:** 126 seconds

**Transcript:**

> If you have ever told someone with ADHD to just go to bed earlier, here is why that advice usually backfires and four tips that can help. The ADHD brain often struggles with delayed sleep phase. The internal clock or circadian rhythm tends to be shifted later than average. Melatonin does not rise when it should, so even when the body is exhausted, the brain might not feel sleepy until very late. Add low dopamine, difficulty transitioning, and mental overstimulation, and bedtime can become a real challenge. For many people with ADHD, that second wind at night is not random: it is the brain finally getting space to decompress after a long day of masking or structure. It is not about laziness or poor discipline; it is about brain chemistry, nervous-system regulation, and transitions. Four strategies can help. First, get natural light early in the morning, within 30–60 minutes of waking. This anchors the circadian rhythm and helps melatonin rise at the right time later. Second, use a reverse alarm 60–90 minutes before bed to begin transitioning. The ADHD brain struggles with abrupt stops, so this creates space to shift out of hyperfocus gradually. Third, reduce nighttime decision-making by keeping a consistent, predetermined wind-down routine. Fewer choices mean less friction and smoother transitions into rest. Fourth, schedule downtime earlier. If you stay up late to reclaim alone time, unstructured time earlier in the day can reduce “revenge bedtime procrastination.” Sleep challenges in ADHD are rooted in neurobiology and require strategies matched to the way the brain works.

### Revised claim review

**Claim 1:** ADHD is commonly associated with delayed sleep timing, a later circadian phase, and later melatonin onset

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/), [LIGHT](https://pubmed.ncbi.nlm.nih.gov/33121289/).

**Claim 2:** Low dopamine, transition difficulty, and mental overstimulation jointly explain why people with ADHD cannot fall asleep

**Verdict: Unsupported.** Sleep problems are multifactorial; this general low-dopamine mechanism is not established. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** A nighttime “second wind” in ADHD occurs because the brain is finally decompressing after a day of masking or imposed structure

**Verdict: Unsupported.** The masking/decompression explanation was not substantiated. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** ADHD-related sleep difficulties should not automatically be attributed to laziness or poor discipline

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 5:** Morning light exposure can help anchor or advance the circadian rhythm and influence later melatonin timing

**Verdict: Supported.** Evidence: [LIGHT](https://pubmed.ncbi.nlm.nih.gov/33121289/).

**Claim 6 — clarified extraction:** A reminder before bedtime may help a person begin a gradual wind-down rather than stop abruptly.

*Original annotation wording:* A reverse alarm exactly 60–90 minutes before bed helps the ADHD brain shift gradually out of hyperfocus

**Verdict: Supported.** A practical reminder, not proof that 60–90 minutes is the optimum. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** A consistent, predetermined wind-down routine can reduce bedtime friction and support sleep

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 8:** Scheduling unstructured time earlier in the day reduces revenge bedtime procrastination in ADHD

**Verdict: Unsupported.** ADHD-specific efficacy of scheduled downtime for this purpose is not established. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 9:** ADHD sleep problems often require more individualized management than simply instructing the person to go to bed earlier

**Verdict: Supported.** Assessment should consider sleep disorders and medication effects. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **6**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **6 / 9 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 85

**Title:** ADD vs. ADHD | Experts answer  
**URL:** https://www.youtube.com/shorts/CHHKEo8mJJ4  
**Views:** 142,052  
**Likes:** 3,366  
**Comments:** 102  
**Duration:** 48 seconds

**Transcript:**

> What is the difference between ADD and ADHD? Some people with ADHD do not have hyperactive symptoms, so it makes sense in that case to say that they have ADD. Technically, ADD was replaced in the official diagnostic manual by ADHD back in the 1980s. The official name would now be ADHD, predominantly inattentive presentation. That does not roll off the tongue as easily, so it is understandable why people sometimes still use ADD and ADHD interchangeably.

### Revised claim review

**Claim 1:** Some people with ADHD do not display prominent hyperactive symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 2:** “ADD” is no longer the official diagnostic term and was replaced by ADHD in the diagnostic manual during the 1980s

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

**Claim 3:** The current diagnostic description corresponding most closely to what people call ADD is ADHD, predominantly inattentive presentation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [DSMCHANGE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 86

**Title:** How do ADHD symptoms affect your life over the years?  
**URL:** https://www.youtube.com/shorts/iwUNM4XXkag  
**Views:** 47,803  
**Likes:** 4,282  
**Comments:** 114  
**Duration:** 60 seconds

**Transcript:**

> I have seen many people for whom I am the first doctor they have visited for ADHD. They may have had mild symptoms as a child and managed, but something has now changed: the demands of life have outstripped their ability to compensate for the deficit. This usually corresponds to changes in academic or work demands. A person may have been a slow reader at school or had extra energy and trouble settling in class but made it through high school, then struggled to keep up with college-level work and first saw a psychiatrist in college. They may get through college but reach a breaking point in graduate studies. They may do adequately in a first job that does not tax attentional resources heavily, then receive a promotion or higher-intensity job and become unable to keep up. These are examples of how someone can appear all right for a while and then cease to cope.

### Revised claim review

**Claim 1:** ADHD symptoms may exist in childhood but become clearly impairing only when later demands exceed the person’s compensatory abilities

**Verdict: Supported.** Later recognition is not the same as first onset in adulthood; childhood symptoms remain required. Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Transitions to college, graduate study, a promotion, or a more demanding job can expose previously compensated attention and executive-function difficulties

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 87

**Title:** ADHD Sensitivity Isn’t Fragile—It’s Real  
**URL:** https://www.youtube.com/shorts/RDporq3vMy8  
**Views:** 328  
**Likes:** 2  
**Comments:** 0  
**Duration:** 30 seconds

**Transcript:**

> Sensitivity does not mean broken; it means attuned. It means your nervous system is working overtime to keep you safe in a world that has often been harsh and invalidating. ADHD brains do not just take in more; they hold on to it longer. Having “sticky brains” with ADHD means we ruminate more, remember what others forget, and replay conversations in our heads—not because we are fragile, but because our brains are still processing.

### Revised claim review

**Claim 1:** Sensitivity in ADHD means the nervous system is working overtime to provide safety because the person’s environment has been harsh or invalidating

**Verdict: Unsupported.** Sensitivity does not establish the proposed trauma/safety mechanism. Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** ADHD brains take in more information and retain it longer than other brains

**Verdict: Unsupported.** ADHD does not generally confer superior information retention. Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/), [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/).

**Claim 3:** People with ADHD characteristically have “sticky brains,” ruminate more, remember what others forget, and replay conversations because their brains require longer processing

**Verdict: Unsupported.** The superior-memory and prolonged-processing explanation is not established. Evidence: [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 88

**Title:** Does ADHD medication make people with ADHD more likely to become addicts?  
**URL:** https://www.youtube.com/shorts/veuZfd9INVA  
**Views:** 145,330  
**Likes:** 9,898  
**Comments:** 215  
**Duration:** 59 seconds

**Note:** The title concerns medication and addiction, but the transcript delivered by Tactiq discusses laziness, motivation, dopamine, task initiation, and hyperfocus. The annotation below assesses the transcript actually returned.

**Transcript:**

> A myth about ADHD is that people with ADHD lack discipline and are lazy. It can look like laziness, but it is a lack of adequate motivation—a brain-derived motivation, not external motivation. Punishment, shaming, and threats do not motivate. The threat of losing a job may motivate a person who lets self-interest get in the way of work, but a person with ADHD has a brain that does not produce enough dopamine in the nerve circuits controlling motivation and reward. What seems like an easy task to a person without ADHD can seem monumental to a person with ADHD. You know you need to do something, but you are stuck and cannot get out of that mental space. Similarly, with hyperfocus, you can be moving at 50 miles per hour on a task and cannot leave the fast lane. You continue until something forces you out or you run out of steam.

### Revised claim review

**Claim 1:** ADHD-related task difficulties should not automatically be interpreted as laziness or lack of discipline

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Punishment, shame, and threats do not motivate people with ADHD

**Verdict: Unsupported.** An absolute absence of response to consequences is unsupported; this does not endorse shaming. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** ADHD brains do not produce enough dopamine in the motivation and reward circuits

**Verdict: Unsupported.** Catecholamine involvement is not proof of uniformly low production. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** An objectively simple task can feel very difficult to initiate or complete for a person with ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 5:** Intense task absorption can make it difficult for some people with ADHD to disengage and switch activities

**Verdict: Supported.** Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 89

**Title:** Your Child's ADHD Symptoms Might Be Starting in The Gut  
**URL:** https://www.youtube.com/shorts/iu-qdiRN8Ng  
**Views:** 21  
**Likes:** 0  
**Comments:** 0  
**Duration:** 46 seconds

**Transcript:**

> When we talk about gut health, we are not just talking about digesting food. We are talking about everything: the immune system, nervous system, gut-brain connection, hormones, detoxification, mood, behaviour, focus—all of it. The gut is not just processing food; it constantly communicates with the brain. When something is wrong in the gut, the brain feels it strongly. If you look only at the brain, behaviour, or top-level ADHD symptoms, you are looking at the last step of the problem.

### Revised claim review

**Claim 1:** The gastrointestinal system interacts with the immune system, nervous system, and brain

**Verdict: Supported.** Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 2:** Gut health controls or encompasses hormones, detoxification, mood, behaviour, and focus—effectively “everything”

**Verdict: Unsupported.** Gut–brain communication does not establish control of everything or the detoxification explanation. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 3:** The gut communicates continuously and bidirectionally with the brain

**Verdict: Supported.** Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 4:** ADHD symptoms in a child may represent merely the final outward stage of an underlying gut problem

**Verdict: Unsupported.** An association does not establish a gut problem as the underlying cause of ADHD. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 90

**Title:** ⚠️AWARENESS⚠️ #pov symptoms of ADHD that you probably didn’t know about… #shorts #fyp #tiktok #adhd  
**URL:** https://www.youtube.com/shorts/19-xqY2AlnA  
**Views:** 178,133  
**Likes:** 11,171  
**Comments:** 374  
**Duration:** 64 seconds

**Transcript:**

> Symptoms of ADHD that you probably did not know about. A friend declines an invitation to go shopping and the person becomes visibly upset despite saying it is fine. Someone repeatedly clicks a pen and the person becomes distressed by the sound. The person feels constantly tired despite sleeping for eight or nine hours. The person forgets a doctor’s appointment and realizes at 5 p.m. that it was scheduled for 4 p.m. The person edits all day because it needs to be perfect. Finally, the person is asked to do something at 11 rather than 12 and reacts that the one-hour change is a major problem.

### Revised claim review

Applied the same broad associated-feature standard used for Video 21. This list is not a diagnostic test.

**Claim 1:** Intense distress after a perceived rejection is a symptom of ADHD

**Verdict: Supported.** An associated possible experience, not a defining symptom. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** Strong distress caused by a repetitive sound can occur in ADHD

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 3:** Persistent tiredness despite obtaining eight or nine hours of sleep is an ADHD symptom

**Verdict: Supported.** Fatigue is documented; eight or nine hours alone does not establish good-quality sleep or exclude other causes. Evidence: [FATIGUE](https://pubmed.ncbi.nlm.nih.gov/27918087/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** Forgetting or missing an appointment can reflect ADHD-related inattention and time-management difficulty

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 5:** Spending all day intensely editing and seeking perfection is an ADHD symptom

**Verdict: Supported.** Intense absorption and compensatory perfectionism can occur; neither alone diagnoses ADHD. Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 6:** Finding a one-hour schedule change intolerable is an ADHD symptom

**Verdict: Unsupported.** The specific intolerance of a one-hour change is not established as an ADHD sign. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **5**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **5 / 6 × 100 = 83.33%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 91

**Title:** Does This Type Of ADHD Sound Like You?  
**URL:** https://www.youtube.com/shorts/uke3cE__spk  
**Views:** 197,050  
**Likes:** 6,447  
**Comments:** 401  
**Duration:** 46 seconds

**Transcript:**

> treatments for the seven types of add or ADHD type two in attentive add short attention span distractability that not very hyperactive or Restless just trouble getting going what we often see on the scans decreased prefrontal cortex activity decreased cerebellar activity so what really helps them is coordination exercises physical exercis a higher protein lower simple carbohydrate diet stimulating supplements can be really helpful like El tyrosine and sometimes stimulants like Rin or arerol can be just incredibly helpful

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** There are seven distinct types of ADD/ADHD, with inattentive ADD constituting “type two”

**Verdict: Unsupported.** Seven scan-defined types are not validated diagnostic presentations. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Predominantly inattentive ADHD commonly involves short attention, distractibility, little overt hyperactivity, and difficulty initiating tasks

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Brain scans of people with this proposed ADHD type characteristically show decreased prefrontal-cortex and cerebellar activity

**Verdict: Unsupported.** Group imaging differences do not validate this proposed individual type. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Coordination exercises specifically treat inattentive ADHD

**Verdict: Unsupported.** Coordination exercise is not established as a type-two-specific treatment. Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 5:** Physical exercise can help ADHD symptoms

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 6:** A high-protein, low-simple-carbohydrate diet and L-tyrosine supplements treat inattentive ADHD

**Verdict: Unsupported.** The diet/tyrosine combination is not an established treatment for this presentation. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science), [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

**Claim 7:** Stimulants such as methylphenidate or amphetamine can be highly effective for ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **3**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **3 / 7 × 100 = 42.86%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 92

**Title:** Is It Bipolar Disorder or Severe ADHD?  
**URL:** https://www.youtube.com/shorts/UBO8IwWoSTo  
**Views:** 33,552  
**Likes:** 1,057  
**Comments:** 40  
**Duration:** 32 seconds

**Transcript:**

> lot of people who get misdiagnosed with bipolar disorder who actually have severe ADHD because at the end of the day both conditions are impulse control disorders the difference is that with bipolar disorder you expect to see sustained periods of elevated mood or depressed mood and by sustained I'm talking about a week whereas with ADHD you tend to see swings in mood hour by hour uh potentially due to challenges with self regulation

### Revised claim review

**Claim 1:** Some people diagnosed with bipolar disorder may instead have ADHD because the conditions can be confused

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** ADHD and bipolar disorder are both impulse-control disorders

**Verdict: Unsupported.** These are not both impulse-control disorders. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Bipolar disorder is distinguished by elevated or depressed mood lasting approximately one week

**Verdict: Unsupported.** Mania, hypomania and depression have different duration thresholds; a single one-week rule is incorrect. Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** ADHD-related emotional changes may occur over hours and be associated with self-regulation difficulties

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 93

**Title:** How to treat ADHD and depression | Experts answer  
**URL:** https://www.youtube.com/shorts/X7OINBCs3Hk  
**Views:** 5,186  
**Likes:** 155  
**Comments:** 5  
**Duration:** 42 seconds

**Status:** # tactiq.io free youtube transcript
# How to treat ADHD and depression | Experts answer
# https://www.youtube.com/watch/X7OINBCs3Hk

00:00:00.080 how do you treat ADHD and depression so
00:00:02.480 this is pretty straightforward for me
00:00:03.919 obviously both disorders need to be
00:00:05.480 treated but there's a hierarchy here if
00:00:07.279 you're concerned that you have
00:00:08.519 depression at all we always treat that
00:00:10.320 first the first and foremost is making
00:00:12.280 sure that you're safe that you're not
00:00:13.440 feeling hopeless or suicidal the key to
00:00:15.480 that is is that if you properly treat
00:00:17.199 the depression you get the help you need
00:00:18.840 whether it's therapy meds family support
00:00:21.119 it really will have a huge impact on
00:00:23.080 your ADHD because people that are
00:00:24.800 depressed really can't manage their ADHD
00:00:27.359 even if they're on the right meds and
00:00:28.439 even if they have the world's greatest
00:00:29.640 support system if you're suffering from
00:00:31.160 depression you're not going to have the
00:00:32.320 energy or the focus to take the steps
00:00:34.239 you need to feel present and engaged so
00:00:36.680 the key is take care of yourself first
00:00:38.440 make sure you're safe treat the
00:00:39.879 depression and the ADHD will follow

### Revised claim review

**Claim 1:** When ADHD and depression coexist, both disorders need to be treated

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 2:** If a person has depression at all, depression should always be treated before ADHD

**Verdict: Unsupported.** Priority depends on severity, risk and impairment; depression does not invariably come first. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 3:** Safety must be prioritized by assessing whether the person feels hopeless or suicidal

**Verdict: Supported.** Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression).

**Claim 4:** Depression can be treated through therapy, medication, and family or social support

**Verdict: Supported.** Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression).

**Claim 5:** Treating depression will substantially improve ADHD because depressed people cannot manage their ADHD even with appropriate ADHD medication and excellent support, after which “the ADHD will follow”

**Verdict: Unsupported.** Depression treatment does not guarantee that co-occurring ADHD will resolve. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 6:** A person suffering from depression will not have the energy or concentration needed to remain present and engaged

**Verdict: Unsupported.** The categorical inability to stay engaged overstates individual variability. Evidence: [DEPR](https://www.nimh.nih.gov/health/publications/depression).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **3**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **3 / 6 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 94

**Title:** How to cure ADHD (short term)  
**URL:** https://www.youtube.com/shorts/EebrJJf0da0  
**Views:** 375,841  
**Likes:** 11,417  
**Comments:** 253  
**Duration:** 37 seconds

**Transcript:**

> Ah, I can't focus and have bad memory. Why does this happen? That's because you have ADHD. Your brains lack dopamine and norepinephrine. I see. Is there any way to solve this? Not a long-term solution, but if your brain triggers a fight orflight situations, it'll be more focused for a short period. Oh, how can I make my brain do that? Help me. Help me. You want me to help you? Yeah. No regret? Yeah. Okay. If you don't complete your studies in an hour, I'll shoot you. Time starts now. Oh, no. No. Wait. Shut the [ __ ] up. It's study now. 10 seconds just passed. How is that 10 seconds? Come on. I [ __ ] told you. Holy [ __ ]

### Revised claim review

**Claim 1:** Poor focus and memory mean that a person has ADHD

**Verdict: Unsupported.** Poor focus and memory cannot establish ADHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD occurs because the brain lacks dopamine and norepinephrine

**Verdict: Unsupported.** ADHD is not a simple absence of these neurotransmitters. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Acute fight-or-flight arousal can temporarily increase concentration

**Verdict: Supported.** Limited arousal effects are possible; high stress may impair control. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Deliberately threatening a person can provide a short-term solution for ADHD-related concentration problems

**Verdict: Excluded from scoring.** An overt fictional/comedic threat, not an additional literal clinical recommendation.

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **1**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 95

**Title:** Why is ADHD treated with stimulants  
**URL:** https://www.youtube.com/shorts/vNh_1YD40tQ  
**Views:** 73,473  
**Likes:** 2,857  
**Comments:** 86  
**Duration:** 55 seconds

**Transcript:**

> Why is ADHD treated with stimulants? If you have a kid who's got ADD or ADHD, their mind is moving really, really, really fast to begin with. They're having a thousand thoughts a second. They're also fidgety. They move their arms around a lot, hands around a lot, right? They can't sit still. And what we also know is that stimulants tend to like ramp people up. So, I was super confused because it seemed like stimulants should make ADHD worse, right? Don't we want to like slow people with ADHD down? So this is what's really fascinating about stimulants and why we use the ones that we use is because what they actually stimulate is activity in the frontal loes. So the way that stimulants work in ADHD is our brain has a gas pedal and it has a break. The stimulants actually stimulate is the break. So they actually act in the frontal loes and then allow the frontal loes to strengthen the frontal loes to inhibit other parts of our brain. So what we're actually stimulating is our inhibitory circuitry.

### Revised claim review

**Claim 1:** People with ADHD universally have extremely fast thoughts, constant fidgeting, and an inability to sit still

**Verdict: Unsupported.** The universal portrayal excludes inattentive presentations and individual variation. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

**Claim 2:** Stimulant medication enhances activity and catecholamine signalling in prefrontal control circuits

**Verdict: Supported.** Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Stimulants can strengthen inhibitory control, metaphorically stimulating the brain’s “brake” rather than merely making a person more active

**Verdict: Supported.** An explanatory metaphor, not literal brake anatomy. Evidence: [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 96

**Title:** How does ADHD medication work? | Experts answer  
**URL:** https://www.youtube.com/shorts/UiRJfV_CJCQ  
**Views:** 105,787  
**Likes:** 3,292  
**Comments:** 70  
**Duration:** 54 seconds

**Transcript:**

> how does ADHD medication work the short answer is ADHD medication affects how your brain uses dopamine mostly right here in What's called the prefrontal cortex but maybe more importantly is how that shows up in your life and I sometimes say that ADH medication closes the gap between intentions and actions the intentions in your head the actions of what happens out in the world it makes it easier to focus and to pay attention on things especially the boring stuff makes it easier to remember what has been said you know because you paid attention and heard it in the first place it makes it easier to get yourself up and going so you're not as kind of driven by the deadline and just in a bunch of different ways it helps you sort of manage the symptoms of ADHD and Smooths over some of those rough patches and some of that extra work that comes along with unmanaged ADHD

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** ADHD medication affects dopamine use, especially in prefrontal brain systems

**Verdict: Unsupported.** This overgeneralizes dopamine action to ADHD medications as a whole; nonstimulants have differing mechanisms. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** ADHD medication can improve focus, sustained attention, working performance, and task initiation

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Medication can help a person translate intentions into action and reduce dependence on deadline-driven urgency

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 97

**Title:** How Inattentive ADHD Is Treated: Meds, Therapy, or Both?  
**URL:** https://www.youtube.com/shorts/khqGUxMPpM8  
**Views:** 7,807  
**Likes:** 115  
**Comments:** 3  
**Duration:** 120 seconds

**Transcript:**

> How do you first go about treating an inattentive ADHD? Which I don't know about you, but the majority of the ADHD I see, the chief complaints are inattention, trouble with concentrating. Doc, I'm not too restless or hyperactive. I have a real time being on time, motivating, finishing tasks, and concentrating, especially if I'm uninterested. So I think opening up kind of you know the different pathways of treatment I think is important and giving patients kind of the road map of the road you know so to speak is where I would start. So, you know, we typically think of medication-based treatments and non-medication-based treatments. And both of those may be first-line agents. Um, they may be things that are equally effective, but they are things that some people prefer medications, some people prefer non-medication therapies and some perhaps many people would do the best in kind of combined, you know, combined method. So we think about medications um whether they are stimulants or non-stimulants and we think of talk therapy specifically cognitive behavioral therapy as being perhaps you know the best evidence-based methods for our patients. So there is evidence-based therapies for ADHD. That's correct. Just because you have ADHD does not mean that the only answer is just medication. Sure. So, cognitive behavioral therapy is um talk therapy, a flavor of talk therapy, so to speak, or psychotherapy that essentially examines the relationship between thoughts, emotions, and our behaviors. It's something that, you know, is potentially useful in a wide range of different psychiatric illnesses or disorders, mood disorders such as major depressive disorder, bipolar disorder, anxiety disorders. Um, and essentially gives patients, you know, a sense of kind of introspection or insight or thoughts or skills training kind of into their own behaviors and how they impact their lives.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Predominantly inattentive ADHD can involve concentration problems, lateness, difficulty initiating and finishing tasks, and greater difficulty sustaining effort on uninteresting work

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2 — clarified extraction:** Medication and non-medication treatments may be equally effective first-line choices for ADHD.

*Original annotation wording:* Medication and non-medication treatments are generally equally effective and can both be treated as interchangeable first-line options

**Verdict: Unsupported.** Effectiveness and first-line choices depend on age, severity and outcome; therapies are not generally interchangeable. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Some people benefit most from combining medication with psychosocial treatment

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Stimulant and non-stimulant medicines are evidence-based ADHD treatments

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Cognitive behavioural therapy is an evidence-based non-medication treatment for ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Medication is not the only evidence-based approach to ADHD management

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** CBT examines relationships among thoughts, emotions, and behaviours and is also used across mood and anxiety disorders

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **6**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **6 / 7 × 100 = 85.71%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 98

**Title:** Improve ADHD WITHOUT Meds!  
**URL:** https://www.youtube.com/shorts/Ihgo6fo6PBQ  
**Views:** 22,835  
**Likes:** 667  
**Comments:** 32  
**Duration:** 57 seconds

**Transcript:**

> I'm a medical doctor and I'm going to show you how to improve ADHD without medications now is it possible to improve ADHD without medications absolutely of course a lot of the symptoms that you're experiencing from ADHD are probably stemming from your diet and all the garbage that you're eating if your diet consists of ton of processed foods added sugars preservatives then you need to cut those out first because obviously that is causing too much stimulation for you and your body needs to tone it down you may have brain fog constantly feeling tired this can all be the result of your lifestyle and just simply what you're putting in your body what if you switched it up into something more nutritious and beneficial and you need to individualized nutrition plan to start the foundation to creating these profound changes is creating a nutritional plan and a lifestyle modification that will be sustainable and help you with your symptoms

### Revised claim review

**Claim 1:** ADHD symptoms can be improved without medication

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 2:** Many ADHD symptoms probably stem from eating processed food, added sugar, and preservatives

**Verdict: Unsupported.** Dietary associations do not establish that most symptoms stem from these foods. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 3:** Processed food, sugar, and preservatives cause excessive stimulation that must be “toned down” to treat ADHD

**Verdict: Unsupported.** The overstimulation mechanism is not established. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 4:** Diet and lifestyle can contribute to fatigue or subjective brain fog

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 5:** An individualized, nutritious, sustainable eating plan and lifestyle changes can support ADHD management

**Verdict: Supported.** Adjunctive health management, not a cure or guaranteed dietary treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 99

**Title:** Taking breaks from your #adhd meds and what happens  
**URL:** https://www.youtube.com/shorts/RNZhnV3QaDs  
**Views:** 18,734  
**Likes:** 449  
**Comments:** 47  
**Duration:** 61 seconds

**Transcript:**

> Taking breaks from Adderall, this is something that I wish I would have known is it is so important to take breaks from Adderall, Ritalin, Vyvanse because these are stimulant meds. Now, a lot of times if you're on an ADHD med, you know what it's like to be on other meds and you have to take them continuously. And a lot of people will tell you, &quot;Hey, when taking this med you're not going to notice any effects for like 2 weeks, maybe even up to 30 days.&quot; They'll tell you with like a lot of like antidepressants and stuff, &quot;Give it 30 days.&quot; Stimulants are different. Stimulants are immediate. And the thing with this is you don't need a build-up in your system. Now, the unfortunate side with stimulants is guess what? You can build a tolerance to it and it's a dopamine tolerance. Ritalin, Vyvanse, a lot of these drugs that are out there that are ADHD drugs do affect your dopamine. And there is a thing called dopamine tolerance. Dopamine tolerance means is after a while your body becomes accustomed to the certain amount of dopamine. Now, if you're not getting that amount of dopamine, you struggle with depression, you struggle with fatigue, you struggle with just emptiness, you struggle. And it is a mental struggle. And also, you're going to find that

### Revised claim review

**Claim 1:** It is important for everyone taking Adderall, Ritalin, or Vyvanse to take medication breaks

**Verdict: Unsupported.** Medication breaks are individualized, not mandatory for everyone. Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** Stimulant medication acts promptly and does not require several weeks of accumulation before any therapeutic effect appears

**Verdict: Supported.** Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 3 — clarified extraction:** Stimulant use can create a “dopamine tolerance” because the body becomes accustomed to a fixed amount of dopamine.

*Original annotation wording:* Stimulants inevitably create a “dopamine tolerance” in which the body becomes accustomed to a fixed amount of dopamine

**Verdict: Unsupported.** Tolerance can occur; the fixed-dopamine-level mechanism is not established. Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** When a person accustomed to stimulant-related dopamine does not receive it, they necessarily develop depression, fatigue, and emptiness

**Verdict: Unsupported.** Withdrawal symptoms are possible, not inevitable in everyone who misses a dose. Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 100

**Title:** 4 Things You Must Do If You Have ADHD  
**URL:** https://www.youtube.com/shorts/9vF-OcTzlJQ  
**Views:** 58,245  
**Likes:** 2,204  
**Comments:** 26  
**Duration:** 59 seconds

**Transcript:**

> Four things you must do if you have ADHD. Number one, ADHD brains naturally have low dopamine. So move your body every day. Physical movement is the fastest, most natural way to boost dopamine. Number two, your brain can't hold big plans in working memory. So don't trust it to remember what to do next. Write it down. Use sticky notes, alarms. Just plan your day outside your head. Number three, ADHD brains can hyperfocus or crash without warning. That's because your nervous system gets disregulated fast. So, take regular breaks, but don't just scroll. Use the time to reset, breathe, stretch, do something mindful. Number four, sleep like it's non-negotiable. ADHD brains already struggle with focus, memory, and emotional control. Sleep is when your brain repairs that.

### Revised claim review

**Claim 1:** ADHD brains naturally have low dopamine

**Verdict: Unsupported.** ADHD is not established as a uniform low-dopamine state. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Physical movement is the fastest natural way to boost dopamine and should therefore be done daily for ADHD

**Verdict: Unsupported.** The comparative claim fastest natural dopamine boost is not established. Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 3:** ADHD can impair working memory, and external reminders, written plans, alarms, and other organizational aids can help

**Verdict: Supported.** Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** People with ADHD unpredictably hyperfocus or crash because their nervous system rapidly becomes dysregulated

**Verdict: Unsupported.** Hyperfocus and fatigue do not prove this rapid nervous-system mechanism. Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 5:** Regular restorative breaks, breathing, stretching, or mindfulness can support self-regulation

**Verdict: Supported.** Supportive coping measures, not substitutes for indicated treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** Adequate sleep supports attention, memory, and emotional regulation, which are already areas of difficulty for many people with ADHD

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **3**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **3 / 6 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 101

**Title:** How To Cure Attention Deficit Disorder (ADHD) | Gary Brecka  
**URL:** https://www.youtube.com/shorts/qbmqKSGHXbY  
**Views:** 33,795  
**Likes:** 689  
**Comments:** 55  
**Duration:** 31 seconds

**Transcript:**

> the truth is ADHD is not even an attention deficit disorder at all it's an attention overload disorder kids and adults that have this condition of attention deficit or attention deficit hyperactivity disorder they don't have a problem paying attention they have a problem paying attention to too many things and then what the modern medicine wants to do is give you an amphetamine to speed up rce the central nervous system to match the pace of the Mind instead of putting just amino acids into the bloodstream that allow the mind to naturally quiet itself yeah

### Revised claim review

**Claim 1:** ADHD is not an attention-deficit disorder but an “attention-overload disorder” in which people can pay attention and merely attend to too many things

**Verdict: Unsupported.** The exclusive attention-overload redefinition is not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 2:** Amphetamine treats ADHD by speeding up the central nervous system until it matches the fast pace of the person’s mind

**Verdict: Unsupported.** Matching the speed of the mind is not the mechanism of stimulant treatment. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 3:** Putting amino acids into the bloodstream naturally quiets the ADHD mind and is a preferable treatment mechanism

**Verdict: Unsupported.** Amino-acid administration is not an established preferable ADHD treatment. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 102

**Title:** Foods That Help & Hurt ADHD Brains  
**URL:** https://www.youtube.com/shorts/905eX5pmJLo  
**Views:** 35,098  
**Likes:** 948  
**Comments:** 29  
**Duration:** 33 seconds

**Transcript:**

> A lot of people want to know if ADHD can be managed with diet. The answer is that dietary changes can be very, very helpful. Food either hurts ADHD or helps it. The types of foods that hurt ADHD include refined sugar, gluten, bread, pasta, cereals, and processed foods. Foods that contain ingredients that are not real food. Things that help protein, especially lean protein, healthy fats to nourish the brain, fruits, vegetables, and complex carbs.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Dietary changes can help some people manage ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 2:** Every food either hurts ADHD or helps it

**Verdict: Unsupported.** Foods cannot all be divided into ADHD-harming and ADHD-helping categories. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 3:** Refined sugar, gluten, bread, pasta, cereals, and processed foods generally worsen ADHD

**Verdict: Unsupported.** These broad exclusions are not supported as general ADHD treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 4:** Lean protein, healthy fats, fruit, vegetables, and complex carbohydrates are beneficial choices for people with ADHD

**Verdict: Supported.** General nutrition, not a claimed ADHD cure. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 103

**Title:** 4 Supplements I Take Everyday For ADHD As A Naturopathic Doctor  
**URL:** https://www.youtube.com/shorts/ZJw5o3vDzvg  
**Views:** 87,525  
**Likes:** 3,822  
**Comments:** 146  
**Duration:** 49 seconds

**Transcript:**

> four supplements that I take every day for my ADHD as a naturopathic doctor number one is magnesium glycinate due to its calming effects on the nervous system magnesium can reduce hyperactivity and improve sleep number two is a fish oil the omega-3 fatty acids that are found in fish oil are essential for brain health and cognition fish oil has also been shown to improve levels of focus and number three is zinc many individuals with ADHD are low in zinc and proper zinc levels can help with impulsivity and number four is vitamin D3 vitamin D plays many critical roles in the body but one of those is improving dopamine status which is often deficient in those with ADHD for the supplements that I recommend click the link in my bio what supplements do you find helpful for ADHD comment below

### Revised claim review

**Claim 1:** Magnesium glycinate calms the nervous system, reduces ADHD hyperactivity, and improves sleep

**Verdict: Unsupported.** Magnesium glycinate is not established to reduce ADHD hyperactivity and improve sleep. Evidence: [MAG](https://pubmed.ncbi.nlm.nih.gov/23808779/).

**Claim 2:** Omega-3 fatty acids in fish oil support brain health and can improve ADHD attention

**Verdict: Unsupported.** The larger review does not establish improvement in core attention symptoms. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 3:** Many people with ADHD are zinc deficient and normalizing zinc improves impulsivity

**Verdict: Unsupported.** Neither general deficiency nor reliable impulsivity improvement is established. Evidence: [ZINC](https://pubmed.ncbi.nlm.nih.gov/34184967/).

**Claim 4:** Vitamin D3 improves dopamine status, which is commonly deficient in people with ADHD

**Verdict: Unsupported.** Small adjunctive trials do not establish a uniform dopamine-deficiency correction. Evidence: [VITD](https://pubmed.ncbi.nlm.nih.gov/31368773/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **0**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **0 / 4 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 104

**Title:** How I managed my ADHD without medication  
**URL:** https://www.youtube.com/shorts/I37W1lxfEGw  
**Views:** 203,030  
**Likes:** 8,056  
**Comments:** 164  
**Duration:** 44 seconds

**Transcript:**

> people like hey how did you deal with your ADHD you don't take medication I took medication for 13 years I didn't like it and eventually I said no I'm going to figure out how to do this on my own and I'll tell you I can't have sugar if I eat sugar I can see my thoughts change self-doubt negativity frustration it shows up if I don't work out in the morning I just need to break a sweat and then that creates a standard and a belief that comes with me for the rest of my day that allows me to be present and focus in anything I do I've gone uh 2,000 days working out every day today I remember I was doing 75 hard and I forgot my ruck sack and I put my son on my shoulders and I went for a hike he had the best time with me I got my workout so many people that working 9 to5 they're like how do I buy back my time it's like how about you just focus on you

### Revised claim review

No eligible generalized ADHD claim; remains unlabelled.

No eligible generalized ADHD claims were identified in the supplied text.

### Revised result

- Eligible fact-checkable claims: **0**
- Supported: **0**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **not defined** (no eligible claims).
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Unlabelled**.

---

## Video 105

**Title:** 6 ADHD strategies that actually work - more on FULL VIDEO #adhd #adhdkids #therapy  
**URL:** https://www.youtube.com/shorts/mNVGwF9OyR0  
**Views:** 21,308  
**Likes:** 728  
**Comments:** 11  
**Duration:** 44 seconds

**Transcript:**

> Today we're diving into six ADHD strategies that are proven to make a real difference in your life. Strategy number one. Point of performance. Point of performance means setting up reminders or tools in the exact spot where you're likely to get distracted or overwhelmed. An example of this would be like posting a checklist on the garage door of things that you need to bring to work each day. That ensures that you remember everything before leaving. By using this technique, you're giving yourself that help you stay focused exactly when distractions are most likely to occur. While it may take a bit of effort to set up, this will make a huge difference in your ability to get what you need to get done.

### Revised claim review

**Claim 1:** Placing reminders or tools at the location where an ADHD-related lapse is likely to occur can support task completion

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** A checklist placed at the point of performance ensures that a person remembers everything and will make a huge difference

**Verdict: Unsupported.** A checklist may assist but cannot ensure remembering everything. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **1**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **1 / 2 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 106

**Title:** ADHD treatment options explained  
**URL:** https://www.youtube.com/shorts/n8wLCSNUEgY  
**Views:** 3,130  
**Likes:** 26  
**Comments:** 2  
**Duration:** 111 seconds

**Status:** # tactiq.io free youtube transcript
# ADHD treatment options explained
# https://www.youtube.com/watch/n8wLCSNUEgY

00:00:00.080 ADHD is definitely on the rise. Um,
00:00:02.879 rates are increasing in both children
00:00:04.960 and adults. Um, and there is definitely
00:00:08.880 more awareness out there for it.
00:00:11.120 Evidence-based treatment generally falls
00:00:13.360 into two different categories. One being
00:00:15.759 medication, stimulants and
00:00:17.520 non-stimulants, and then behavioral
00:00:19.680 therapy. Um, so this usually involves
00:00:22.160 like parent training and things like
00:00:23.920 that. For younger children below the age
00:00:26.640 of six, AAP, the American Academy of
00:00:29.279 Pediatrics, recommends behavior
00:00:31.840 interventions um before starting
00:00:34.160 medications. Um but for older children
00:00:37.040 um it tends to be a combination of
00:00:39.280 medication with behavioral
00:00:41.040 interventions. Parent training involves
00:00:43.520 improving parent child interactions and
00:00:46.640 also behavior management. So, increasing
00:00:48.960 rewards for positive behaviors and
00:00:51.520 ignoring or extinguishing um undesirable
00:00:54.399 and or unwanted behaviors. There are a
00:00:56.960 lot of things that can improve um ADHD
00:00:59.440 symptoms like um exercise has been one
00:01:01.920 that's been shown to improve uh
00:01:04.720 symptoms. Sleep hygiene is a big one. If
00:01:08.320 you're sleepy, it's really hard to pay
00:01:10.080 attention. Um diet's another one. But
00:01:13.119 also, there could be behavioral
00:01:14.560 interventions within the school system.
00:01:16.880 So, school accommodations and one big
00:01:19.040 one is allowing for movement to occur.
00:01:22.080 And what we're showing with a lot of the
00:01:23.759 research is that um movement might
00:01:26.320 actually be helpful for kids with ADHD.
00:01:28.799 So, to tell a kid with ADHD, make sure
00:01:31.439 you sit down, don't move, could be
00:01:34.240 harmful. Um, and so we're trying to
00:01:37.040 study that to see what are the effects
00:01:38.799 of fidgeting in our lab as well. Um, but
00:01:41.119 all these things don't cure ADHD. And if
00:01:44.079 you don't have these lifestyle changes,
00:01:45.840 it doesn't uh cause ADHD, but it could
00:01:48.799 definitely help.


### Revised claim review

**Claim 1:** ADHD rates are increasing among both children and adults

**Verdict: Supported.** Interpreted as recognized/diagnosed rates, not proof of changing underlying biological prevalence. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [TRENDS](https://pubmed.ncbi.nlm.nih.gov/24464188/).

**Claim 2:** Awareness of ADHD has increased

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 3:** Evidence-based ADHD treatment generally includes stimulant or non-stimulant medication and behavioural interventions

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** For children younger than six, the American Academy of Pediatrics recommends behavioural interventions before medication

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 5:** For older children, ADHD treatment tends to combine medication with behavioural interventions

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 6:** Parent training seeks to improve parent–child interactions and behaviour management by reinforcing desirable behaviour and appropriately reducing reinforcement of undesirable behaviour

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** Exercise has been shown to improve ADHD symptoms

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 8:** Sleep hygiene improves ADHD symptoms, and sleepiness makes attention more difficult

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 9 — clarified extraction:** Sleep, nutrition and other supportive lifestyle measures can help functioning alongside established ADHD care.

*Original annotation wording:* Diet generally improves ADHD symptoms

**Verdict: Supported.** Supportive nutrition, not a blanket elimination-diet efficacy claim. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 10:** Behavioural interventions and accommodations can be implemented within schools

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 11:** Allowing movement or fidgeting may help some children with ADHD

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 12:** Telling a child with ADHD to remain seated and completely still could be harmful

**Verdict: Supported.** Inflexible demands could worsen distress or functioning; the text says could, not inevitably. Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 13:** Exercise, adequate sleep, diet, and accommodations do not cure ADHD; lacking these lifestyle practices does not cause ADHD, although appropriate changes may help with symptoms or functioning

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **13**
- Supported: **13**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **13 / 13 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 107

**Title:** Adults With ADHD Natural Treatments  
**URL:** https://www.youtube.com/shorts/8iooEVtGGs4  
**Views:** 13,109  
**Likes:** 404  
**Comments:** 3  
**Duration:** 53 seconds

**Transcript:**

> So, if you're an adult with ADD and you don't want to take stimulants or you can't take stimulants, um what are some of the natural treatments? Um exercise always uh so important EPA fish oil. So, a lot of omega-3 fatty acids. People think brain and DHA well it's not been shown to be helpful for people have ADD but higher in EPA can be really helpful also rodeiola ashwagandha and tyrrosine uh tyrrosine is the amino acid building block for dopamine and a lot of my patients find or 1500 milligrams of tyrrosine twice a day can make a huge positive difference for

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Exercise can support symptom management in adults with ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 2:** EPA-rich omega-3 supplementation may help ADHD, whereas DHA alone has not shown the same benefit

**Verdict: Unsupported.** Routine clinically reliable EPA benefit is not established by the broader review. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 3:** Rhodiola is an effective natural treatment for adult ADHD

**Verdict: Unsupported.** A trial registration is not efficacy evidence. Evidence: [RHOD](https://clinicaltrials.gov/study/NCT02737020).

**Claim 4:** Ashwagandha is an effective natural treatment for adult ADHD

**Verdict: Unsupported.** The small pediatric study does not establish effective adult treatment. Evidence: [ASH](https://pubmed.ncbi.nlm.nih.gov/42602386/).

**Claim 5:** Taking approximately 1,500 mg of L-tyrosine twice daily can make a major positive difference in ADHD

**Verdict: Unsupported.** The claimed large benefit of this tyrosine regimen is not established. Evidence: [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

**Claim 6 — added from supplied transcript:** Tyrosine is a precursor involved in dopamine synthesis.

**Verdict: Supported.** Biochemical precursor status does not establish treatment efficacy. Evidence: [STIM](https://www.nature.com/articles/1301164), [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **2**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **2 / 6 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 108

**Title:** Episode 53: ADHD  #keepgoing #adhd #adhdawareness #adhdfamily #unconditionyourselfwithnamitathapar  
**URL:** https://www.youtube.com/shorts/Lg6zqlF4PY4  
**Views:** 32,131  
**Likes:** 592  
**Comments:** 5  
**Duration:** 43 seconds

**Transcript:**

 What is ADHD and what are its symptoms? The first component is hyperactivity. They can't sit in one place. They want to touch everything. What is the difference between ADHD and ADD? So It's Attention Deficit  Disorder. So, it's just The attention part. If it's attention hyperactive deficit disorder, then you have the whole thing. Is it something that's life long, because we see a lot of adults with it? It's there. Many of us also have it. Oh, really? We all have them around. 10%, one out of ten kids, has it. Exactly. Let's talk about diagnosis. There's no MRI. There's no CT scan. There's no X-ray. There is no imaging test that can diagnose ADHD. What is the treatment? So, ADHD isn't something that leaves you. It's with you for life.


### Revised claim review

First review of the author-supplied English replacement, 9 September 2026. Questions and repeated lifelong-persistence assertions are not counted again. Minor acronym/word-order slips are not scored as separate medical claims.

**Claim 1 — revised extraction:** Hyperactivity in ADHD can involve difficulty remaining seated and excessive movement or intrusion into activities.

*Original annotation wording:* Hyperactivity in ADHD may include difficulty remaining seated and excessive touching or activity

**Verdict: Supported.** These are recognizable symptom examples. Touching everything is colloquial, not a mandatory criterion or a feature of every presentation. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2 — revised extraction:** ADD is the attention-only disorder, whereas ADHD means having the attention and hyperactivity components together.

*Original annotation wording:* ADD refers only to attention difficulty, whereas ADHD includes attention difficulty plus hyperactivity

**Verdict: Unsupported.** ADD is an older informal term. Current ADHD includes inattentive, hyperactive-impulsive and combined presentations; having both domains is not necessary. The contrast is misleading when offered without that distinction. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 3 — revised extraction:** Approximately one in ten children has ADHD.

*Original annotation wording:* Approximately one in ten children has ADHD

**Verdict: Supported.** Supported as a rough estimate, with population qualification: the 2022 US parent survey estimated current diagnosed ADHD at 10.5% in ages 3–17. This does not establish a worldwide or India-specific 10% rate; prevalence depends on age, setting and case definition. Evidence: [UPD_CDC2022](https://stacks.cdc.gov/view/cdc/160350).

**Claim 4 — revised extraction:** An MRI, CT, X-ray or other brain-imaging test cannot by itself diagnose ADHD.

*Original annotation wording:* MRI, CT, X-ray, or another brain scan cannot presently diagnose ADHD

**Verdict: Supported.** Clinical history and assessment establish the diagnosis; routine imaging is not a stand-alone ADHD test. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 5 — revised extraction:** ADHD never leaves a person and necessarily stays with them for life.

*Original annotation wording:* ADHD never leaves a person and always remains for life

**Verdict: Unsupported.** Persistence into adulthood is common, but an invariant lifelong course is too strong. The longitudinal MTA study found remission and recurrence, with a minority showing sustained remission through its endpoint. This does not prove permanent cure or predict any individual's lifetime course. Evidence: [UPD_REMISSION](https://pubmed.ncbi.nlm.nih.gov/34384227/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the interpretation note below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The ADD/ADHD contrast is scored as present-day diagnostic advice. If it is instead coded solely as an explanation of historical informal terminology, Claim 2 would be supported and the result would be Label 1 (4/5). The roughly 10% statement is supported as an approximate estimate seen in some populations, not as a verified prevalence for India or every country.

---

## Video 109

**Title:** Can ADHD medication make anxiety worse? | Experts answer  
**URL:** https://www.youtube.com/shorts/HDBY2NY4FKM  
**Views:** 13,729  
**Likes:** 258  
**Comments:** 20  
**Duration:** 42 seconds

**Status:** can ADHD medication make anxiety worse if you have a proper diagnosis of ADHD then ADHD medication should not make your anxiety worse but as I've been saying anxiety and ADHD really do overlap and sometimes the symptoms of anxiety mimic ADHD in that case the stimulate medication can make your anxiety worse where I see that quite a bit is with young kids in particular boys who may be hyperactive and are quickly diagnosed with ADHD sort of hyperactive type and are very quickly put on meds and sometimes we see that meds don't help them or actually make them worse in those cases some of the time it's because the primary issue is not actually ADHD it's anxiety and that's why it's so critical to make a really thoughtful diagnosis before you begin treatment

### Revised claim review

**Claim 1:** If a person has been properly diagnosed with ADHD, ADHD medication should not worsen their anxiety

**Verdict: Unsupported.** Stimulants can worsen anxiety even when the diagnosis is correct. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 2:** Anxiety and ADHD can overlap, and symptoms caused by anxiety can resemble ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 3:** If apparent ADHD symptoms are actually caused by anxiety, stimulant medication can worsen the person’s anxiety

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 4:** Hyperactive children, particularly boys, may be diagnosed with ADHD when anxiety is actually the primary problem

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 5:** When ADHD medication does not help or makes someone worse, this can sometimes indicate that the primary condition is anxiety rather than ADHD

**Verdict: Supported.** A reason to reassess, not a diagnostic test based on medication response. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 6:** A thoughtful differential diagnosis is critical before beginning ADHD treatment

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **5**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **5 / 6 × 100 = 83.33%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 110

**Title:** 5 Things To Do If You Struggle With ADHD  
**URL:** https://www.youtube.com/shorts/CvuzzY1P4Bo  
**Views:** 19,884  
**Likes:** 598  
**Comments:** 7  
**Duration:** 60 seconds

**Transcript:**

> So, as a psychiatrist, here's five things I would recommend if you struggle with ADHD. Take our ADD type test because what I've learned is ADD, like depression, like anxiety, is not one thing. Stop giving everybody stimulants who have ADD. That's why they have a bad reputation for the wrong brain. They're a nightmare. As a psychiatrist for ADHD, I'd stop medicating with alcohol and marijuana. They both steal your dopamine. I would limit gadgets and video games because they steal your dopamine. I would exercise that boost dopamine. I'd be on a higher-protein, lower-simple-carbohydrate diet. And I might try L-tyrosine cuz it helps to boost dopamine.

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** A proprietary “ADD type test” can identify different forms of ADHD that require different brain-specific treatment

**Verdict: Unsupported.** The proprietary brain-type classification is not validated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Stimulants should not be given to everybody with ADD because they are a nightmare for the wrong brain.

*Original annotation wording:* Stimulants are a nightmare when given to the “wrong brain,” so clinicians should broadly stop giving them to people with ADD

**Verdict: Unsupported.** Individualized prescribing is appropriate, but the brain-type explanation linked to the preceding proprietary test is not clinically validated. The full compound assertion is scored. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Alcohol and marijuana “steal dopamine” from people with ADHD

**Verdict: Unsupported.** Stealing dopamine is not an established clinical account. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Gadgets and video games “steal dopamine”

**Verdict: Unsupported.** The depletion explanation is not established. Evidence: [MEDIA](https://pubmed.ncbi.nlm.nih.gov/36562860/), [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Exercise can support ADHD management and affects dopamine-related systems

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 6:** A high-protein, low-simple-carbohydrate diet is an established treatment for ADHD

**Verdict: Unsupported.** This dietary prescription is not established ADHD treatment. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** L-tyrosine treats ADHD by boosting dopamine

**Verdict: Unsupported.** Biochemistry does not establish tyrosine efficacy. Evidence: [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **1**; unsupported: **6**; excluded: **0**.
- Supported-claim percentage: **1/7 × 100 = 14.29%**.
- **Reviewed label: Label 4 — Highly misleading**
- Previous reviewed label: **Label 3**.
- Uploaded CSV label: **Label 4**.

---

## Video 111

**Title:** ADHD Medication: What You Need to Know #adhd  
**URL:** https://www.youtube.com/shorts/641oIKC-Pvo  
**Views:** 6,752  
**Likes:** 60  
**Comments:** 8  
**Duration:** 25 seconds

**Transcript:**

> There's three different types of medication options if you have ADHD. Stimulant, non-stimulant, and slowreleasing stimulant. Now, I don't prescribe medication, but the 10 psychiatrists who work at my company, Private Therapy Clinic, do. So, if you want some guidance on medication for ADHD, feel free to get in touch with us and they'll be more than happy to guide you.

### Revised claim review

**Claim 1:** ADHD medication includes stimulant medicines

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 2:** ADHD medication includes non-stimulant medicines

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 3 — clarified extraction:** Slow-release stimulant formulations are among the available ADHD medication options.

*Original annotation wording:* Slow-release stimulant medication is a third medication type separate from stimulant and non-stimulant medication

**Verdict: Supported.** The speaker lists formulations, not mutually exclusive pharmacological classes. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 112

**Title:** ADHD in Children - Treatment Methods with Dr. Chiang  
**URL:** https://www.youtube.com/shorts/0bVUr-oTps0  
**Views:** 2,451  
**Likes:** 18  
**Comments:** 0  
**Duration:** 112 seconds

**Status:** you want to rule out all diagnosis before you settle on ADHD and the reason why is because there are specific treatments for ADHD that will not work if your child doesn't actually have ADHD so stimulate medications that you have heard so that's the first treatment that everybody ask for and that's what schools often ask for because they just want the child to calm down however a child who does not have ADHD the stimulant medications can actually cause them to be more anxious and agitated so it does the opposite of what you would expect just remember they all have side effects um you want to keep a a close eye on that a lot of children don't sleep on simulate medications and they don't eat very well either so you definitely want your pediatrician or other medical doctor to keep a close eye on your child there are what we call behavioral strategies um so sometimes kids can go and see a psychologist or a social worker or any um mental health therapist can teach your child obviously this is when your child's a little bit older I would recommend at least eight when your child is able to understand and make changes um and so they can teach them strategies like how to organize how to manage time um how to one of the common themes of ADH children who do have ADHD is they're very forgetful right they they don't remember things so a lot of times us adults keep reminding them but if they're not going to remember the information provide like let's say visual cues those of us who are older we use a planner organizer and you can definitely start teaching that y um and then what also happens um you know you can also modify you want to make sure your child is getting enough sleep getting enough to eat right if we if they're on stimulate medications their appetite will be less so you want to make sure that all these other things are getting adequate sleep eating enough and so that we don't have other reasons for causing them to be inattentive or hyperactive

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** All diagnoses must be ruled out before settling on ADHD.

*Original annotation wording:* Before diagnosing ADHD, clinicians should rule out every other possible diagnosis

**Verdict: Unsupported.** Other conditions can coexist with ADHD. Differential assessment does not require excluding every other diagnosis. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know).

**Claim 2:** ADHD-specific treatments, including stimulants, will not work in a child who does not actually have ADHD.

*Original annotation wording:* ADHD-specific treatment may not be effective or appropriate when a child’s symptoms are caused by another condition rather than ADHD

**Verdict: Unsupported.** Stimulant effects are not unique to ADHD. Treatment response cannot establish the diagnosis, and absence of ADHD does not imply that stimulants have no cognitive effects. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Stimulant medication is generally the first ADHD treatment everyone requests, and schools frequently request it merely to make children calm down

**Verdict: Unsupported.** The universal school/parent prescribing stereotype is unsupported. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 4:** In a child without ADHD, stimulant medication can cause anxiety and agitation, producing the opposite effect from what was expected

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 5:** ADHD medications can produce adverse effects, so the child should be monitored closely by the prescribing clinician

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 6:** Stimulant medication can interfere with sleep and reduce appetite in children

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 7:** Behavioural and psychological interventions can form part of ADHD treatment and may be provided by appropriately trained mental-health professionals

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 8:** A child should generally be at least eight years old before behavioural strategies can be useful

**Verdict: Unsupported.** Behavioural parent interventions are useful before age eight. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 9:** Children with ADHD may benefit from learning strategies for organization and time management

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 10:** Forgetfulness is a common feature of ADHD, and visual cues, planners, and other reminders may assist affected children

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 11:** Adequate sleep and nutrition should be considered because sleepiness, insufficient food intake, and medication-related appetite reduction can worsen attention or functioning

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **11**
- Supported: **7**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **7/11 × 100 = 63.64%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 2**.

---

## Video 113

**Title:** ADHD medication does âœ¨SO MUCH MOREâœ¨ than just help us focus.  
**URL:** https://www.youtube.com/shorts/moJkfS5gwSs  
**Views:** 21,787  
**Likes:** 868  
**Comments:** 24  
**Duration:** 59 seconds

**Transcript:**

> I think one of the biggest misconceptions about ADHD medication is that all it does for us is help us focus and pay attention. When in reality, it does so much more than that. You don't believe me, do you? Let's see what other people have to say. Part one. What does your medication help you with other than focus and attention? To literally be able to catch a thought. I feel that. Laundry. Helps me to complete uninteresting tasks such as chores without dying of boredom. Mood, productivity, energy levels, motivation. It quiets the noise in my mind. Mood and energy levels. Literal perception of time. Literal. Not overeating, regulating my emotions, staying on task. Less anxiety when I'm taking my medication. I now remember to do things when I think about doing them. Well, most of the time. Better impulse control so I don't start another 1,000 new hobbies when I haven't done anything with the last ones, either. Okay, call me out. Energy and motivation. Motivation. Frustration tolerance, being able to deal with interruptions, emotional regulation. Lots of emotional regulation in here. Task initiation, does it exist without my meds? Same.

### Revised claim review

Only the introductory generalized claim is eligible. Personal treatment testimonials are excluded under the thesis rule.

**Claim 1:** ADHD medication can improve daily functioning beyond narrow concentration and attention

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Medication can improve task initiation, persistence, chore completion, and productivity

**Verdict: Excluded from scoring.** An individual commenter’s experience, not a population claim.

**Claim 3:** Medication can improve working performance, prospective remembering, and impulse control

**Verdict: Excluded from scoring.** An individual account, not an independently verifiable generalized assertion.

**Claim 4:** Medication commonly improves mood, emotional regulation, frustration tolerance, and anxiety

**Verdict: Excluded from scoring.** The compilation reports personal experiences; the annotation added commonly.

**Claim 5:** ADHD medication prevents overeating

**Verdict: Excluded from scoring.** Personal eating experience, not a claim that medication prevents overeating generally.

**Claim 6:** Medication can improve impulse control and make it easier to remain on task

**Verdict: Excluded from scoring.** Another individual comment, not a separate generalized efficacy claim.

### Revised result

- Eligible fact-checkable claims: **1**
- Supported: **1**; unsupported: **0**; excluded: **5**.
- Supported-claim percentage: **1 / 1 × 100 = 100.00%**.
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 114

**Title:** How to manage ADHD paralysis ðŸ§  #adhd #adhdsupport  
**URL:** https://www.youtube.com/shorts/hpfMO7Bp5zA  
**Views:** 175,058  
**Likes:** 13,026  
**Comments:** 408  
**Duration:** 48 seconds

**Transcript:**

> People with ADHD struggle with motivation. So instead of trying to find motivation, it's better to try to find momentum. And you can find momentum by stacking dopamine. For example, if you start your day with a really big task, which needs motivation, which is what we don't have, you'll become overwhelmed, give up, and then spend the rest of the day full of shame, doom scrolling social media. Instead of that, try starting the day with a really small task. That'll give you a little bit of dopamine which you can use to start the next slightly bigger task. Continue this pattern until you've stacked enough dopamine and built enough momentum and use this momentum to attack the bigger tasks later in the day. And by this stage, you'll have so much dopamine that you'll probably even enjoy the big task.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** People with ADHD may have motivational and task-initiation difficulties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** Completing a small task releases a quantity of dopamine that can be “stacked” and then spent on the next task

**Verdict: Unsupported.** Dopamine is not demonstrated as a stackable currency spent on tasks. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Starting the day with a large task will cause a person with ADHD to become overwhelmed, give up, feel shame, and doom-scroll for the rest of the day

**Verdict: Unsupported.** The inevitable failure/shame/doom-scrolling sequence is unsupported. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Breaking a large task into smaller, achievable steps can build behavioural momentum and reduce overwhelm

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Repeated small tasks create so much dopamine that a person with ADHD will probably enjoy a large task later

**Verdict: Unsupported.** The proposed dopamine accumulation and later enjoyment are not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **2**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **2 / 5 × 100 = 40.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 115

**Title:** Adult ADHD: How Can It Impact Your Day-To-Day Life? Dr. Samir Parikh Explains #shorts  
**URL:** https://www.youtube.com/shorts/Giva7EBSdrw  
**Views:** 89,750  
**Likes:** 3,582  
**Comments:** 64  
**Duration:** 58 seconds

**Transcript:**

Adult AHD especially how does it impair the nature of your life so it will affect the quality of your work for sure you will be performing below par or below your ability you will also take a lot more time and energy to be able to function at the level which is expected as compared to others you may struggle in your relationships because of ADHD as well why the attention deficit component is affecting your communication at times the hyperactive impulsive component is bringing out more output than it should and you are always so under pressure and dream because the basic aspects of life that you need to be doing and you are doing are taking so much out of you physically and mentally tiring yes it is it is tiring and it's the unseen most people who have a mental element you don't see it so you just end up giving them the knowledge that go run go jog go do this do that It's not a problem

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** Adult ADHD will affect work quality for sure, with performance below the person’s ability.

*Original annotation wording:* Adult ADHD can impair work quality and cause a person to perform below their underlying ability

**Verdict: Unsupported.** Occupational impairment is documented, but the asserted certainty is unsupported across individuals, settings and treatment circumstances. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know).

**Claim 2:** An adult with ADHD will take a lot more time and energy than others to function at the expected level.

*Original annotation wording:* Adults with ADHD may need more time and effort than peers to meet ordinary performance expectations

**Verdict: Unsupported.** Some adults report substantial compensatory effort. Those reports do not establish this unqualified comparative prediction for an adult solely from the diagnosis. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 3:** Inattention and impulsivity can disrupt communication and relationships.

*Original annotation wording:* Inattention and hyperactive-impulsive symptoms can impair communication and relationships

**Verdict: Supported.** Listening, interruption and impulse-control difficulties can affect relationships. No claim that every relationship will be impaired is needed. Evidence: [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Other people give advice to run or jog and dismiss an unseen mental-health problem.

*Original annotation wording:* Telling a person simply to exercise or try harder is not an adequate response to clinically impairing ADHD

**Verdict: Excluded from scoring.** The prior review inferred a clinical claim that exercise alone is inadequate. No such explicit efficacy assertion is stated here. This reported advice and dismissal is excluded under the clinical-claim scope.

**Claim 5:** Adults with ADHD are always under pressure because basic daily activities are physically and mentally exhausting.

**Verdict: Unsupported.** Stress and fatigue are documented burdens. The word always asserts an unsupported universal frequency; it is not replaced with can. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [FATIGUE](https://pubmed.ncbi.nlm.nih.gov/27918087/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **1**.
- Supported-claim percentage: **1/4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 1**.

---

## Video 116

**Title:** Natural Remedies for Children with #adhd  See Full videos @doinglifewithbridgette on IG  
**URL:** https://www.youtube.com/shorts/wH7Yd3keDvM  
**Views:** 3,780  
**Likes:** 72  
**Comments:** 4  
**Duration:** 61 seconds

**Transcript:**

> okay if your child has uh Focus issues in school or constipation issues this video is for you okay a few months ago I shared a video about what my pediatrician shared with me about what I need to take out of my daughter's diet because she was having issues focusing in school a lot of you guys that resonated with a lot of you guys and I shared that I was going to update you on our journey so here's the update we ended up taking out red dye blue dye sugar most dairies and we reduced amount of Breads and cakes that she that's in her diet we didn't take out everything that she said because that is almost impossible to do and have a normal life but we took out the majority of things and we were able to find her quite a few things that she still loves and it not be too much of a hassle the other thing I want to share with you guys is her the update on her Focus issues so one of the things that we learned is that we needed to add a vitamin into her diet not only

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

The supplied fragment contains no eligible generalized ADHD claim; remains unlabelled.

No eligible generalized ADHD claims were identified in the supplied text.

### Revised result

- Eligible fact-checkable claims: **0**
- Supported: **0**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **not defined** (no eligible claims).
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Unlabelled**.

---

## Video 117

**Title:** ADHD At School: What Actually Helps  
**URL:** https://www.youtube.com/shorts/-NgzixV2Lvw  
**Views:** 4,559  
**Likes:** 93  
**Comments:** 2  
**Duration:** 66 seconds

**Transcript:**

> It's important for parents to be able to, I think, recognize the nature of ADHD and be clear about it. Um, because it can look volal. You're you're not paying attention on purpose. You know, why don't you just listen to sit still? It can really turn into a situation where the parents get overly angry uh and um really um in some ways insulting um to the to the kids like you, you're just not doing things the right way and why in some ways a bad kid. It doesn't mean that they should excuse it, but it it would be that important to be able to say, you know, look, we are understanding this. We want to have you cope with this. Let's see what you can do about getting better. I like to have parents uh really think a lot about um being careful where they spend their attention. To not really focus a lot on the on the negative actions, but to be pretty thorough with regard to praising and noticing things with either a magnifying glass or a microscope. Sometimes you really have to look very very at tiny tiny pieces of behavior that are in the right direction.

### Revised claim review

**Claim 1:** ADHD behaviour that appears deliberate—such as failing to listen or sit still—may reflect symptoms rather than intentional defiance

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Consistently noticing and praising small steps toward desired behaviour can help children with ADHD

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 118

**Title:** Why ADHD Fuels Anxiety  
**URL:** https://www.youtube.com/shorts/Oj7GXqHnO5w  
**Views:** 45,935  
**Likes:** 2,212  
**Comments:** 65  
**Duration:** 60 seconds

**Status:** So imagine your brain's like raising a head. Your fast processing is cranking out a flood of ideas and emotions like oh my gosh, what if I fail my test? What if my teacher gets mad at me? What if I never get a job? What if I what if I write catastrophizing that that verbal processing is just flying down the road, but your ability to like slow down and organize and self soothe lags behind. It's like that lower dot on the IQ score, right? So these are things like adding in here like you're going to be okay. Remember to breathe. This is just your brain making words. There is no evidence that you're going to fail your test. Right? That's what many people with ADHD experience. Their thoughts and feelings move fast, but the tools to regulate those feelings, the metaphorical breaks, cannot keep up. So, anxiety, overwhelm, and emotional outbursts take over. These aren't just behavioral issues. They're not a lack of willpower. They're regulation issues. You might desperately want to stay calm or focused, but your cognitive systems aren't working in sync. And over time, this can lead to chronic anxiety, low self-esteem, fear of failure, especially when you're misunderstood or punished for something you can't yet control.

### Revised claim review

**Claim 1:** ADHD involves unusually fast verbal processing that produces a flood of ideas, emotions, and catastrophic thoughts

**Verdict: Unsupported.** A generally superior verbal-processing speed is not established. Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 2:** In ADHD, the ability to organize thoughts and self-soothe develops or operates more slowly than verbal processing, appearing as a lower score on an IQ profile

**Verdict: Unsupported.** The proposed IQ-profile mechanism is not established. Evidence: [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 3:** Many people with ADHD experience difficulties regulating their emotions

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** Emotional dysregulation in ADHD can contribute to overwhelm and emotional outbursts

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 5:** ADHD-related difficulties staying calm or focused are regulation difficulties rather than simply a lack of desire or willpower

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 6:** Over time, ADHD-related difficulties can contribute to anxiety, low self-esteem, and fear of failure, particularly when the person is repeatedly misunderstood or negatively treated

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **4**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **4 / 6 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 119

**Title:** The Scary Truth Behind ADHD Medication - Andrew Huberman  
**URL:** https://www.youtube.com/shorts/8ePBJv6qqjc  
**Views:** 70,353  
**Likes:** 878  
**Comments:** 84  
**Duration:** 44 seconds

**Transcript:**

> Adderall is basically a combination of amphetamine and dextroamphetamine now some of you probably realize this that Adderall is amphetamine but I'm guessing that there are a good number of you out there perhaps even parents and kids that don't realize that these drugs like cocaine and amphetamine methamphetamine which are incredibly dangerous and Incredibly habit-forming and have high potential for abuse well the pharmaceutical versions of those are exactly what are used to treat ADHD and they're not exactly like cocaine or Methamphetamine but they are structurally and chemically very similar and their net effect in the brain and body is essentially the same which is to increase dopamine primarily but also to increase levels of a neuromodulator called epinephrine or norepinephrine also called noradrenaline and adrenaline those names are the same

### Revised claim review

**Claim 1:** Adderall contains mixed amphetamine salts, including dextroamphetamine and levoamphetamine components

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81).

**Claim 2:** Cocaine, amphetamine, and methamphetamine can be dangerous, habit-forming, and have substantial abuse potential

**Verdict: Supported.** Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 3:** Therapeutic ADHD stimulants are structurally, chemically, and functionally essentially the same as cocaine and methamphetamine

**Verdict: Unsupported.** Different drugs, formulations and use patterns are not chemically/functionally equivalent. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 4:** These drugs have essentially the same brain-and-body effect: increasing dopamine and increasing “epinephrine or norepinephrine,” which are the same chemical

**Verdict: Unsupported.** Epinephrine and norepinephrine are distinct; drug actions also differ. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 120

**Title:** My Child Has ADHD, What Can We Do?  
**URL:** https://www.youtube.com/shorts/ondTuYVB66c  
**Views:** 5,584  
**Likes:** 291  
**Comments:** 12  
**Duration:** 83 seconds

**Status:** hey everyone I'm going to show you a research article on ADHD in in its relation to neural inflammation and oxidative stress and I'm going to give you some tips on things that you can do to help your kid decrease that stress on their body so what we end up finding in kids that have ADHD is a lot of times their brain is inflamed and they have a lot of what's called oxidative stress or simply meaning that they can't detoxify efficiently enough they're they're getting a buildup of waste products and they're getting a lot of oxidants which creates a lot of more inflammation top three things that can play into this is lack of appropriate antioxidants in their body or not enough antioxidants to help combat that autoimmunity is another really big one and then mitochondrial dysfunction which I'm going to go into more detail in a longer video on YouTube but I want to give you a few things that you can do to help with this so use of dietary and natural components to help against oxid stress and neural inflammation and ADHD best things that we can start doing is taking a high amount of omega-3 fatty acids especially DHA and EPA which are mainly found in fish oils an acetylcysteine is a precursor for antioxid or for the antioxidant glutathione so Antoine's great sulphoraphane is found in um broccoli Sprouts cauliflower great for anti-inflammatory and then as many flavonoids as you can get that means eating a lot of different colors and fruits and vegetables those are great ways to get a ton of antioxidants and help decrease that inflammatory load


### Revised claim review

**Claim 1:** Children with ADHD commonly have inflamed brains and substantial oxidative stress

**Verdict: Unsupported.** Peripheral markers do not establish inflamed brains in children with ADHD. Evidence: [OXID](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/).

**Claim 2:** Oxidative stress means that the body cannot detoxify efficiently, causing waste products and oxidants to accumulate and produce further inflammation

**Verdict: Unsupported.** The detoxification explanation is not established. Evidence: [OXID](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/).

**Claim 3:** The three principal factors contributing to ADHD-related neuroinflammation and oxidative stress are insufficient antioxidants, autoimmunity, and mitochondrial dysfunction

**Verdict: Unsupported.** These are not established principal causal factors for ADHD. Evidence: [OXID](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/).

**Claim 4:** Taking high amounts of omega-3 fatty acids, particularly DHA and EPA from fish oil, is among the best interventions for children with ADHD

**Verdict: Unsupported.** High-dose fish oil is not among the best established ADHD interventions. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 5:** N-acetylcysteine is a precursor involved in glutathione production and is therefore a useful intervention for ADHD-related oxidative stress and inflammation

**Verdict: Unsupported.** Precursor biochemistry does not establish ADHD efficacy. Evidence: [OXID](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 6:** Sulforaphane from broccoli sprouts and cauliflower is a suitable anti-inflammatory intervention for ADHD

**Verdict: Unsupported.** Sulforaphane is not an established ADHD intervention. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 7:** Eating varied, differently coloured fruits and vegetables provides flavonoids and other antioxidant nutrients

**Verdict: Excluded from scoring.** Standalone general nutrition background is outside the ADHD coding unit. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 8:** Consuming large amounts of flavonoids and antioxidants will decrease the inflammatory burden associated with a child’s ADHD

**Verdict: Unsupported.** The claimed clinical anti-inflammatory effect is not established. Evidence: [OXID](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **0**; unsupported: **7**; excluded: **1**.
- Supported-claim percentage: **0 / 7 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 121

**Title:** Combating procrastination for people with ADHD  
**URL:** https://www.youtube.com/shorts/ef_JenyvDHw  
**Views:** 192,111  
**Likes:** 16,794  
**Comments:** 222  
**Duration:** 60 seconds

**Transcript:**

> if you've got ADHD your internal clock is going to be impaired but your sensory sensitivity is going to be higher so we're going to have to rely on external trackers of time to help us out calendars reminders I use alarms all the time like even when I'm like procrastinating I'll use an alarm so I have a 20- minute timer set on my phone that's my procrastination timer if I want to play like you know a video game for 20 more minutes like I'm let's say I'm playing Elder ring so I'll literally what I'll do is like I'll set a 20-minute timer and I'll be like okay I should start working now but I'm going to set a 20-minute timer and then 20 minutes rolls around I'm like okay like that's enough like I cuz really think about it when you're like procrastinating you don't want to start work but when you really look back there's been my experience when you look back at the 20 minutes that you wasted you're like was this really worth it to waste this time and the answer is always no the problem is that you don't have that step because you don't have that external anchor that's pulling you in and like actually helping you realize what the hell you're doing so we want to create an external scaffold of reminders timers calendars Etc

### Revised claim review

**Claim 1:** ADHD can impair internal time perception or time management

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 2:** People with ADHD generally have heightened sensory sensitivity

**Verdict: Supported.** A group association with variation, not universal hypersensitivity. Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 3:** External reminders, alarms, calendars, and timers can compensate for ADHD-related time-management and prospective-memory difficulties

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 122

**Title:** ARE YOU TAKING YOUR ADHD MEDICATIONS WRONG?! Pharmacist reviews Proteins role in ADHD #adhd  
**URL:** https://www.youtube.com/shorts/c0HBZZDKTl0  
**Views:** 97,053  
**Likes:** 6,593  
**Comments:** 270  
**Duration:** 63 seconds

**Transcript:**

> fun fact that not enough people know if you take ADHD medication and you crash really hard at the end of the day or you just want to go right back to sleep after you take it, it's probably because you're not eating enough protein because protein is what activates your ADHD medication and you need to be eating protein all throughout the day in order to keep your focus and your energy up that you should be getting from your meds. >> So, I know a lot of you are not going to like this answer and probably come at me, but protein is not actually like activating your ADHD medication. So stimulants work by directly increasing dopamine and norepinephrine activity in our brain. But they don't need protein as fuel to activate them. Let me just give you an analogy. Think of the medication like turning on a light switch. The electricity is already wired in. So you don't have to eat protein to power the house. What protein can do is help stabilize your blood sugar. Because if you take your stimulant on an empty stomach and your blood sugar later drops, you can feel that like tired, shaky, foggy feeling. And that's simply just your body running low on energy. But if you are truly getting sleepy while on a stimulant, I could point more on like when you're taking it, the dose that you're

### Revised claim review

The claim that protein activates medication is quoted and explicitly rebutted; it is not endorsed.

**Claim 1:** Dietary protein is not required to “activate” stimulant ADHD medication

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 2:** Stimulants increase dopamine and norepinephrine signalling in the brain

**Verdict: Supported.** Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Eating protein may support steadier energy and reduce symptoms caused by inadequate food intake, but it does not power the medication

**Verdict: Supported.** Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 123

**Title:** â° ADHD & Time Blindness: The 3x10 Rule That Actually Helps  
**URL:** https://www.youtube.com/shorts/7Jl6RRyHL8I  
**Views:** 7,077  
**Likes:** 114  
**Comments:** 3  
**Duration:** 37 seconds

**Status:** So there are three big problems that those of us with ADHD and executive function challenges have when it comes to managing time. With the ADHD brain one of the three problems with managing time is called time blindness, we tend to be very unrealistic about time and that can get us into a lot of trouble. Number two is because of this time blindness and because of just challenges with time managment and the ADHD brain being late and often what comes with being late is being unprepared and that leads to number three a lot of us with ADHD brains and executive function challenges tend to be poor at planning, poor at forethought right

### Revised claim review

**Claim 1:** People with ADHD and executive-function difficulties have three principal time-management problems: time blindness, lateness or unpreparedness, and poor planning

**Verdict: Excluded from scoring.** An introduction to the following items, not an additional independent claim.

**Claim 2:** People with ADHD tend to experience “time blindness,” meaning difficulty realistically perceiving or estimating time

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 3:** ADHD-related difficulty estimating and managing time can contribute to lateness

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Being late because of ADHD is often accompanied by being unprepared

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** People with ADHD tend to have difficulties with planning and forethought

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 124

**Title:** What if You're Gifted and You Have ADHD? #shorts #adhd  
**URL:** https://www.youtube.com/shorts/BMz8J5J12G0  
**Views:** 206,472  
**Likes:** 15,892  
**Comments:** 584  
**Duration:** 36 seconds

**Transcript:**

> sometimes people think if you're smart you can't have ADHD nope in fact you can actually be gifted and have ADHD there's a term for this it's called twice exceptional twice exceptional is a term used to mean that somebody is outside the norm in two ways they are gifted and they have a disability so if you have ADHD and you're also a gifted student you're twice exceptional this can be harder to recognize the giftedness can mask the disability and vice versa and sometimes we end up looking like a normal student because sometimes we're really great and sometimes we struggle they can seem to cancel each other out but really we need support for both material that's challenging enough for our brains and the support for the impairments that we have

### Revised claim review

**Claim 1:** High intelligence or giftedness does not rule out ADHD, and a gifted student with a disability may be described as twice exceptional

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Giftedness can mask ADHD-related impairment, while ADHD difficulties can mask gifted performance

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** A twice-exceptional student may require both sufficiently challenging material and support for ADHD-related impairment

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 125

**Title:** How To Beat ADHD  
**URL:** https://www.youtube.com/shorts/-UHnJ2NYSRU  
**Views:** 142,635  
**Likes:** 8,780  
**Comments:** 126  
**Duration:** 68 seconds

**Transcript:**

> One of the parts of your brain, if you have ADHD, that does work even better than a neurotypical person is your sensory input. This is what makes us highly distractable. We get so distracted by sensory stimuli. The sensory parts of our brain are hyper sensitive. So instead of an internal biological clock subconsciously measuring things, if we have data written out and we see it with our eyes, that will affect our brain in a more profound way. And now you ask, why is that? That's because our internal sensors are impaired. We're so much more sensitive to things from the outside because our internal biological clock doesn't work. That's a closer example of like a minus two over here, a plus two over here. The problem is that in most cases, this plus two of sensory sensitivity creates problems. Okay? So, time blindness is a huge huge huge thing. And the most important way to do that is to externalize your clocks and pay attention to them. Write things out, measure things to really figure out how long things take. And it's really cool because when I do this with patients, their natural ability to be able to estimate how long tasks take and complete them just goes up. Once you feed that information to your brain, then your brain is able to calculate. It's no longer a question mark. And so things just get

### Revised claim review

**Claim 1:** Sensory processing works better than normal in ADHD and is universally hypersensitive

**Verdict: Unsupported.** Greater sensitivity does not mean universally superior sensory processing. Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 2:** ADHD distractibility is caused by hypersensitive sensory brain regions

**Verdict: Unsupported.** Distractibility is not established as caused by hypersensitive sensory regions. Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** The internal biological clock does not work in ADHD, and enhanced external sensitivity compensates for this impairment

**Verdict: Unsupported.** Time difficulties do not establish a broken clock compensated by heightened senses. Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 4:** Difficulty estimating and monitoring time is common in ADHD

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 5:** External clocks, written estimates, and measuring how long tasks take can improve planning accuracy

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **2**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **2 / 5 × 100 = 40.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 126

**Title:** Can Supplements Help ADHD?  
**URL:** https://www.youtube.com/shorts/F8B8twCBsew  
**Views:** 17,536  
**Likes:** 922  
**Comments:** 19  
**Duration:** 43 seconds

**Transcript:**

> so remember the top supplements for ADHD are going to be an omega-3 fatty acid a b complex vitamin magnesium vitamin D in herbs and mushrooms like ginkgo biloba and lion's mane those are going to be the most effective for being able to focus in you might even be able to find some of those in a combination nootropic formula which could have loads of benefits but remember going back to this again you want to have a diet that's low glycemic low sugar lots of meat lots of vegetables some berries a lot of healthy fat like coconut olive oil and even nut Butters are okay okay but lots of healthy fats lots of protein lots of fiber that's what kids should be eating with ADHD

### Revised claim review

**Claim 1 — clarified extraction:** Omega-3 is among the most effective supplements for ADHD.

*Original annotation wording:* Omega-3 supplementation is one of the better-studied supplements for ADHD

**Verdict: Unsupported.** The transcript says most effective, not merely better-studied; routine efficacy is not established. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 2:** B-complex vitamins, magnesium, and vitamin D are among the most effective general supplements for ADHD focus

**Verdict: Unsupported.** This general efficacy ranking is unsupported. Evidence: [MAG](https://pubmed.ncbi.nlm.nih.gov/23808779/), [VITD](https://pubmed.ncbi.nlm.nih.gov/31368773/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 3:** Ginkgo biloba and lion’s mane are among the most effective ADHD supplements

**Verdict: Unsupported.** These are not established among the most effective ADHD treatments. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 4:** Combination nootropic formulas containing these supplements can provide many ADHD benefits

**Verdict: Unsupported.** The broad benefit claim for unspecified combination formulas is unsubstantiated. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 5:** Children with ADHD should follow a low-glycaemic, low-sugar diet containing large amounts of meat, fat, protein, and fibre

**Verdict: Unsupported.** This universal dietary prescription is not supported by guidelines. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **0**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **0 / 5 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 127

**Title:** How Meditation Helps With ADHD  
**URL:** https://www.youtube.com/shorts/AP_3nc8seEI  
**Views:** 242,998  
**Likes:** 22,574  
**Comments:** 232  
**Duration:** 60 seconds

**Transcript:**

> if you've got ADHD force yourself to focus on one thing you will fail but then bring yourself back to it bring yourself back to it bring yourself back to it and the real thing that happens with ADHD is not strengthening your ability to focus on one thing what actually gets strengthened is your ability to return from a distraction to your task so right now what happens with ADHD this is the tricky thing when you get distracted what is the cost once you open up Tik Tok or YouTube shorts or Instagram reels or whatever 4 5 minutes disappear before you come back to your task when you meditate and as you become an expert meditator you you may get distracted the same amount the difference is that within 5 Seconds you'll return think about that imagine if a distraction did not cost you as much this is how meditation improves ADHD it doesn't actually change the attentional it does change the attentional fundamentals but even without changing the attentional fundamentals it reduces the price you pay for having ADHD that's the real strategy

### Revised claim review

**Claim 1:** A person with ADHD who forces sustained focus on one thing will fail

**Verdict: Unsupported.** Failure of sustained focus is not inevitable. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 2:** Meditation trains a person to notice distraction and return attention to the intended task

**Verdict: Supported.** Evidence: [MIND](https://pubmed.ncbi.nlm.nih.gov/34146899/).

**Claim 3:** Ordinary distraction costs four or five minutes, whereas an expert meditator with ADHD returns within five seconds despite being distracted equally often

**Verdict: Unsupported.** The exact four/five-minute versus five-second comparison is not substantiated. Evidence: [MIND](https://pubmed.ncbi.nlm.nih.gov/34146899/).

**Claim 4:** Mindfulness or meditation may improve attention and reduce functional difficulties associated with ADHD

**Verdict: Supported.** Evidence: [MIND](https://pubmed.ncbi.nlm.nih.gov/34146899/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 128

**Title:** 3 Natural Remedies for ADHD to Try in 2024  
**URL:** https://www.youtube.com/shorts/uigUeHEHkmM  
**Views:** 12,376  
**Likes:** 327  
**Comments:** 21  
**Duration:** 50 seconds

**Transcript:**

> do you have a child with ADHD do you want 2024 to be better than 2023 want more peace less hyperactivity less Defiance and more joy then give these three tips a try change your child's diet cut out highly inflammatory foods like gluten dairy soy artificial flavors and colors and excessive amounts of sugar focus on whole fruits and veggies grass-fed wild C proteins and healthy fats tip two prioritize exercise physical activity is critical for children with ADHD it can improve focus mood and even sleep quality and finally tip three focus on sleep sleep affects many areas of Our Lives including ADHD symptoms need support with these reach out today

### Revised claim review

**Claim 1:** Children with ADHD should remove gluten, dairy, soy, artificial flavours and colours, and excessive sugar because these are inflammatory causes of symptoms

**Verdict: Unsupported.** Blanket elimination and inflammatory causation claims exceed the evidence. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/).

**Claim 2:** A balanced diet emphasizing fruit, vegetables, protein sources, and healthy fats can support a child’s health

**Verdict: Supported.** Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 3:** Physical activity can improve attention, mood, and sleep in children with ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 4:** Sleep quality and duration can influence the severity of ADHD-like and ADHD-related difficulties

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 129

**Title:** How to motivate a teenager with ADHD | Experts answer  
**URL:** https://www.youtube.com/shorts/rwsoOl66VyU  
**Views:** 17,399  
**Likes:** 579  
**Comments:** 24  
**Duration:** 56 seconds

**Transcript:**

> How can you motivate a teenager with ADHD? Okay, so if you have a teenager, especially teenager with ADHD that's not being fully treated, you may have a teenager that doesn't feel very good about themselves. The first thing you need to do is validate, validate, validate. Validate how they're feeling and sort of meet them where they are. Help them to understand that there is a pathway to getting better. So you can't send a teenager to high school without the proper treatment and expect them to flourish and feel good about themselves. However, teenagers really don't love to hear their parents or their therapist talk, talk, talk. With teenagers you've got to meet them where they are. So you have to figure out what they care about. Do they care about their grades getting better? Do they care about having more plans on Saturday night? Do they care about their parents not yelling at them for making their room a mess? Whatever it is they care about, that's your hook. And then from there you need concrete goals. Not just raw, raw, raw. It needs to be we're going to make your grades a little bit better. You're going to start making plans. Whatever it is, if they're on board with you, you've got them there. And that's the way to motivate them. And that's the way you're going to see change.

### Revised claim review

**Claim 1:** A teenager with insufficiently treated ADHD may develop low self-esteem

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Validation and meeting the teenager at their current perspective can support engagement

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 3:** A teenager with ADHD cannot be expected to flourish in high school without formal treatment

**Verdict: Unsupported.** No individual outcome can be guaranteed or ruled out solely by treatment status. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 4:** Motivation can be improved by linking goals to what the teenager values and setting concrete, collaborative objectives

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 130

**Title:** Avoid These 3 Foods If You Have ADHD  
**URL:** https://www.youtube.com/shorts/hVl9srUL9pQ  
**Views:** 68,256  
**Likes:** 2,513  
**Comments:** 89  
**Duration:** 29 seconds

**Transcript:**

> if you have ADHD here are three foods that you should absolutely avoid number one sugar especially refined sugar or added sugar if the label says added sugar or cane sugar or anything like that get it out of your pantry number two artificial dieses artificial dies have been shown in study after study to worsen symptoms of ADHD and number three processed food my rule of thumb in our house is if I read the label and I can't pronounce what's in it it's out

### Revised claim review

**Claim 1:** Every person with ADHD should completely avoid refined or added sugar

**Verdict: Unsupported.** Complete avoidance for everyone is not recommended ADHD care. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 2:** Artificial food colours can worsen behavioural symptoms in some children, including a susceptible subgroup with ADHD

**Verdict: Supported.** Evidence: [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 3:** People with ADHD should avoid processed foods whenever an ingredient name is difficult to pronounce

**Verdict: Unsupported.** Pronounceability does not determine an ingredient’s safety or effect. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 131

**Title:** 5 Serious Risks of Untreated ADHD  
**URL:** https://www.youtube.com/shorts/drZDWizHfks  
**Views:** 8,091  
**Likes:** 359  
**Comments:** 22  
**Duration:** 85 seconds

**Transcript:**

> ADHD isn't just distractability. When it goes unressed, it carries real but preventable risks. Number one is mental health complications. Depression, anxiety, oppositional behavior, conduct problems, and substance use all become more common when ADHD isn't treated. Number two is safety and self harm. Teens and adults face higher risks of suicidal behavior, physical aggression, and involvement with the justice system. Number three is risky decisions. Untreated ADHD is linked to disruptive and mood issues, plus higher rates of dangerous driving, impulsive sexual activity, and other high-risisk behaviors. Number four is physical health. Accidental injuries and trauma go up and so does premature mortality largely from preventable accidents. And number five is school, work, and money. There's more academic underachievement, lower high school and college completion, and more job instability and unemployment. The good news is that ADHD is highly treatable. When you combine structure, sleep, nutrition, lab work, and when appropriate, medication or supplements, outcomes can improve dramatically. And if you're looking for support, tools, and strategies to help manage ADHD naturally, my online ADHD course and community is now open. Click the link below to learn

### Revised claim review

**Claim 1:** ADHD is associated with higher rates of depression, anxiety, oppositional or conduct problems, and substance-use problems

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Adolescents and adults with ADHD have elevated risks of suicidal behaviour, aggression, and criminal-justice involvement

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** ADHD is associated with dangerous driving, impulsive sexual behaviour, and other risky decisions

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** ADHD is associated with accidental injury, trauma, and increased premature mortality, including mortality from accidents

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** ADHD is associated with academic underachievement, lower completion rates, employment instability, and financial difficulties

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** ADHD is treatable, and appropriate multimodal management can improve outcomes

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** Laboratory testing and supplements are standard components that, alongside sleep, nutrition, structure, and medication, dramatically improve ADHD outcomes

**Verdict: Unsupported.** Routine laboratory tests/supplements and dramatic improvement are not established for every ADHD patient. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **6**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **6 / 7 × 100 = 85.71%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 132

**Title:** Understanding ADHD Impulsivity: Regain Control of Your Life  
**URL:** https://www.youtube.com/shorts/io4KFOqAo28  
**Views:** 234,125  
**Likes:** 24,690  
**Comments:** 262  
**Duration:** 56 seconds

**Transcript:**

> do you ever feel like you have no control over your life emotions or things you say a really common struggle for adhders is impulsivity that means interrupting people saying things you immediately regret having chaotic spending habits or struggling with bad habits and addictions without treatment impulsivity can lead to negative consequences like losing a job getting expelled from school or breaking up because it's impulsive it doesn't feel like a choice is made but nobody else knows that ADHD brains don't automatically pause before acting so you have to learn how the first step is becoming familiar with how your brain works the more you understand it the more you can regain control and turn impulsive acts into thoughtful decisions best of all this approach helps other symptoms like emotion regulation learn what your brain does differently and you can learn how to do the things your brain wasn't wired for while keeping the strengths ADHD gives you

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Impulsivity is common in ADHD and can involve interrupting, regretted speech, impulsive spending, or difficulty controlling risky habits

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Poorly managed impulsivity can contribute to serious school, work, financial, and relationship consequences

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** ADHD can impair the pause between an impulse and an action

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Psychoeducation and learning to recognize one’s behavioural patterns can support more deliberate decisions and emotional regulation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 133

**Title:** ADHD in Hindi Childhood Symptoms Hyperactivity impulsivity inattention Treatment #shots  
**URL:** https://www.youtube.com/shorts/I0F7QApBzfw  
**Views:** 263,797  
**Likes:** 9,518  
**Comments:** 145  
**Duration:** 59 seconds

**Transcript:**

ADHD stands for Attention Deficit Hyperactivity Disorder, as the same suggests, it talks about retention and hyperactivity, children actually have a lack of attention, they lack focus after studying for 5 to 10 minutes, their minds wander, if the teacher is teaching they start looking outside the classroom, their thoughts become very disorganized. Hyperactivity actually has two criteria: hyperactivity and impulsivity. Interrupting a conversation or failing to wait for one's turn. Hyperactivity includes excessive talking, running instead of walking, and fidgeting as a key issue. It should be properly assessed from a ADHD perspective. It should also be examined from an IQ perspective and education perspective, because sometimes children are very intelligent, which is why they become bored and when it comes to treatment, methylphenidate and stimulants play a significant role, an occuptational therapist can also help, if any additional morbid issues arise, they will need to be addressed

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** ADHD is attention-deficit/hyperactivity disorder, involving inattention and/or hyperactivity-impulsivity.

*Original annotation wording:* ADHD involves difficulties with attention and/or hyperactivity

**Verdict: Supported.** This is the recognized condition and its symptom structure; not everyone has both domains. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Children with ADHD lose focus after studying for 5–10 minutes and become distracted during lessons.

*Original annotation wording:* A child with ADHD typically loses concentration after exactly ten minutes and begins looking outside

**Verdict: Unsupported.** The stated time window is not established as a general ADHD attention-span rule. The supplied wording is 5–10 minutes, not exactly ten. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Excessive talking, inappropriate running and fidgeting can be hyperactive symptoms.

*Original annotation wording:* Excessive talking and marked restlessness can be hyperactive-impulsive symptoms

**Verdict: Supported.** These are symptom examples assessed against developmental level and context; running instead of walking alone does not diagnose ADHD. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 4:** Hyperactivity has two criteria, hyperactivity and impulsivity, with interruption and difficulty waiting given as examples.

**Verdict: Unsupported.** The examples are recognized symptoms, but the two-criteria formulation is inaccurate. The hyperactivity–impulsivity domain contains nine listed symptoms with age-dependent thresholds. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Assessment should consider ADHD together with educational needs and intellectual ability, since insufficient challenge can resemble attention problems in some bright children.

**Verdict: Supported.** Context and learning profile matter. Giftedness can coexist with ADHD; this does not make high IQ an exclusion criterion or require IQ testing in every assessment. Evidence: [UPD_GIFTED](https://pmc.ncbi.nlm.nih.gov/articles/PMC9688281/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** Stimulants, including methylphenidate, have an established role in ADHD treatment.

**Verdict: Supported.** Methylphenidate is itself a stimulant. NICE recommends it as first-line pharmacological treatment for children aged five and older when medication is indicated; age and clinical need matter. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** An occupational therapist can help a child with ADHD.

**Verdict: Supported.** Supported for selected functional interventions. A randomized Cog-Fun trial found improvements in parent-reported outcomes, but not teacher ratings. This supports 'can help', not every occupational therapy method or a cure. Evidence: [UPD_COGFUN](https://pubmed.ncbi.nlm.nih.gov/27637735/).

**Claim 8:** Co-occurring conditions should be assessed and addressed alongside ADHD.

**Verdict: Supported.** Assessment and treatment planning include coexisting conditions and the individual's needs. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **6**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **6/8 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 2**.

---

## Video 134

**Title:** How to Overcome Executive Dysfunction with ADHD #adhd #executivedysfunction #bodybuilding  
**URL:** https://www.youtube.com/shorts/sJbdUBP47CY  
**Views:** 14,896  
**Likes:** 731  
**Comments:** 24  
**Duration:** 130 seconds

**Transcript:**

> what exactly is executive dysfunction and why is it such a big barrier for people with ADHD Dr Roso Brockley has said that ADHD is not an attention deficit problem is an intention deficit problem a common example is all of us can imagine and remember times when we've stay focused for hours on things that we probably shouldn't be focusing on we never had trouble focusing on playing a video game or watching a really exciting TV show but somehow we can't direct our brain to use the same attention resources on maybe some like homework that we have to do or some project that has a deadline coming up until it's too late really what the executive dysfunction is describing is our brain's ability to properly direct before it's too late what's worse about it is that those of us with ADHD uh can also have more trouble regulating our emotions if someone rejects you or you reject yourself you feel an even more overwhelming sense of grief and sadness the most important thing to overcome executive dysfunction is to somehow snap yourself out of that vicious cycle manage that potential for your emotions to spiral out of control and the key is to just take the tiniest of steps so instead of thinking that you have to complete this paper think that you are going to open the empty Word document and that you are going to reread the prompt or the project description and every time you take these Tiny Steps actually give yourself a check box on the to-do list to give yourself the recognition that you are making forward progress no matter how small they are and that is the most effective way to get out of your spiral and to direct your brain more intentionally and overcome the dysfunction and in flow club we make that easy we encourage everyone to break their tasks down the smallest of steps and we set up our norms and our feature set so that we encourage and celebrate you moving forward every step

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** ADHD is not an attention-deficit problem; it is an intention-deficit problem.

*Original annotation wording:* ADHD is not an attention problem but an “intention-deficit problem”

**Verdict: Unsupported.** Taken as a clinical definition, this incorrectly denies an established symptom domain. A hypothetical metaphorical intention is not used to rescue the assertion. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** People with ADHD have never had trouble focusing on video games or exciting television, but cannot direct the same attention to required work.

*Original annotation wording:* People with ADHD may sustain attention for highly engaging activities while struggling to direct effort toward delayed, less interesting work

**Verdict: Unsupported.** Interest-dependent variation and hyperfocus do not establish never having difficulty with engaging activities or inability to attend to required work. Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 3:** Executive dysfunction can impair directing attention, intention, planning, and action toward future goals

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Emotional-regulation difficulty can accompany ADHD and make rejection or self-criticism feel especially intense

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** Breaking a task into the tiniest steps and checking off each step is the most effective way to overcome executive dysfunction

**Verdict: Unsupported.** Task breakdown can help, but the superlative most effective is not established. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **2**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **2/5 × 100 = 40.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 2**.

---

## Video 135

**Title:** The BEST executive function hack for ADHD  
**URL:** https://www.youtube.com/shorts/UEIe5K14PPk  
**Views:** 31,082  
**Likes:** 951  
**Comments:** 80  
**Duration:** 36 seconds

**Transcript:**

> I just found the best executive function hack and I wanted to share it. Ready? Stop trying to executive function like a neurotypical person. Your ADHD brain is wired differently and it is possibly unable to executive function like a neurotypical person. And by the way, that's completely okay. The sooner we stop putting all the energy into trying to executive function like a neurotypical person, use that energy to creatively solve the problems we need to solve to get from A to B, the sooner we get to go do the things that light us up. And the world is a better place when women with ADHD are doing the things that light them up. So get going. You got this.

### Revised claim review

**Claim 1:** ADHD is associated with executive-function differences that can make neurotypical planning and self-management methods ineffective for some people

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Adapting the environment and using individualized, creative compensatory strategies can help address ADHD-related functional problems

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 136

**Title:** Rejection Sensitive Dysphoria Explained #adhd #adhdbrain #neurodiversity  
**URL:** https://www.youtube.com/shorts/qVJPdnnYctw  
**Views:** 100,856  
**Likes:** 6,943  
**Comments:** 197  
**Duration:** 53 seconds

**Transcript:**

> Why are people with ADHD so sensitive to rejection? Let me explain. This balloon wrapped in duct tape represents a neurotypical person, and this bit of cardboard with a nail attached to it represents a rejection. When the neurotypical person encounters a rejection, it hurts, but the neurotypical person doesn't explode. This balloon represents an ADHD person. It's bright and fun to be around, but because it was exposed to 10,000 more negative messages when it was a child and has always felt a bit different because of that, it's a lot more exposed and therefore more likely to react defensively. So, when the ADHD person encounters the same rejection, it explodes. This often presents as rage, but it can present as an internalized overwhelming feeling of sadness. And the rejection doesn't have to be a big one. Sometimes the tiniest of rejections, like a friend saying they're too busy to see you, can have the same effect.

### Revised claim review

**Claim 1:** People with ADHD are generally extremely sensitive to rejection

**Verdict: Supported.** Associated rejection distress, not a separate universal diagnostic criterion. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [JUSTICE2](https://pubmed.ncbi.nlm.nih.gov/24878677/).

**Claim 2:** A child with ADHD receives exactly 10,000 more negative messages than a neurotypical child

**Verdict: Unsupported.** The exact 10,000-message difference is not established. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** Greater rejection sensitivity in ADHD is caused by those additional childhood messages and by always feeling different

**Verdict: Unsupported.** The fixed causal explanation exceeds the evidence. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** Some people with ADHD can react to perceived rejection with intense anger or overwhelming sadness, even when the rejection appears minor

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 137

**Title:** Links between ADHD and pain #ChronicPain #Pain #ADHD #ADHDAwareness  
**URL:** https://www.youtube.com/shorts/wamvLlHsqk8  
**Views:** 4,915  
**Likes:** 283  
**Comments:** 16  
**Duration:** 90 seconds

**Transcript:**

> I don't know if like many people would immediately see a strong link between ADHD and pain, but actually we know that people with ADHD are much more likely to experience pain. There's some kind of biological elements to it. So, one possible explanation is that people with ADHD and people with chronic pain both have higher levels of inflammation within the nervous system. So, that might be a common factor between the two. And your nervous system is the thing that kind of regulates pain. Yeah, exactly. In ADHD, the brain is kind of telling the muscles to maintain a kind of persistently high muscle tone, which means that the muscles get kind of fatigued and uh uncomfortable and and painful. And actually, some people have proposed that this might partly explain the physical restlessness of ADHD. Essentially, people are feeling ready to go all the time. There's also kind of psychological components to it as well because how we experience pain is very much related to attention. And for people with ADHD, they might have more difficulties with disengaging their attention from pain. There's also evidence actually that people with ADHD have greater pain sensitivity. So they're actually feeling the pain to a greater extent. Why is that? We don't really know. It might be to do with the with the attention. Like it might be more difficult to disengage your attention from the pain. So you're experiencing it like your subjective experience of it is greater. It might be to do with greater sensitivity to do with the inflammation that we're talking about. I think all of these things are kind of like connected and kind of all play a role.

### Revised claim review

**Claim 1:** People with ADHD have an elevated likelihood of chronic or recurrent pain

**Verdict: Supported.** Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/).

**Claim 2:** ADHD and chronic pain share high nervous-system inflammation as a common biological cause

**Verdict: Unsupported.** A shared high-neuroinflammation cause is not established. Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/).

**Claim 3:** In ADHD, the brain tells muscles to maintain persistently high tone, causing fatigue, pain, and physical restlessness

**Verdict: Unsupported.** The proposed persistently elevated muscle-tone mechanism is not established. Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/).

**Claim 4 — clarified extraction:** Difficulty disengaging attention from pain may help explain pain problems in some people with ADHD.

*Original annotation wording:* People with ADHD have pain because they cannot disengage attention from it

**Verdict: Supported.** The speaker offers an attentional explanation as a possibility; it remains a hypothesis. Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/).

**Claim 5:** Some evidence indicates altered or increased pain sensitivity in ADHD

**Verdict: Supported.** Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 138

**Title:** Side Effects of Stimulant Medication Can Worsen ADHD.  
**URL:** https://www.youtube.com/shorts/gr5LVLIib-k  
**Views:** 56,789  
**Likes:** 667  
**Comments:** 81  
**Duration:** 35 seconds

**Transcript:**

> real evidence for Adderall and other stimulant-based medications ready question is why are these things working I mean there's times I feel like it's just like cocaine in a pill form right like these are amphetamines these are hard medications they can have side effects it can start to affect your sleep um and especially when you're talking about ADHD that's one of the things that concerns me a lot with stimulant use sometimes if that the medication effects of the medication is lingering around is something that's going to keep you awake at night and compromised sleep can lead to symptoms of ADHD it can even cause irritability anxiety depression a whole host of issues psychiatrically

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Adderall is essentially cocaine in pill form

**Verdict: Excluded from scoring.** A personal cocaine metaphor; not an endorsed chemical-equivalence assertion.

**Claim 2:** Stimulant ADHD medication can cause insomnia or keep a person awake when its effects extend too late

**Verdict: Supported.** Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 3:** Inadequate sleep can worsen inattention and hyperactivity-like symptoms and contribute to irritability, anxiety, or depressed mood

**Verdict: Supported.** Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 139

**Title:** 5 ADHD Hacks for Teens That Actually Work | Executive Function Tips I ADHD Kids and Parenting  
**URL:** https://www.youtube.com/shorts/I3bs8F4M0f8  
**Views:** 10,063  
**Likes:** 456  
**Comments:** 16  
**Duration:** 54 seconds

**Transcript:**

> Whether you have ADHD or struggle with executive functioning, we all know that just focus isn't a real plan. Here are five hacks that actually work. Hack one, the one song clean. I tell myself to clean for just one song. That's it. Once I start, I usually keep going, but if not, one song is still progress. Hack two, use a visual timer. If I can't see time, I forget it exists. I use a timer so I don't drift into the void. Hack three, alarms with labels. My phone alarms have names like start homework or leave in 10. Hack four, brain dump first. Before I start anything, I do a brain dump. Just a scribble of all my thoughts onto a journal. It clears the mental clutter. Hack five, the next smallest step. Instead of write the whole essay, I just ask what's the next tiniest step, like open my laptop. These don't fix everything, but they help my brain work with me instead of against me.

### Revised claim review

**Claim 1:** Simply telling a person with ADHD to focus is usually less useful than providing a concrete behavioural plan

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Starting a task for one song or another short interval can lower the initiation barrier

**Verdict: Supported.** A practical initiation strategy, not a guaranteed treatment effect. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Visual timers and labelled alarms can support time awareness and prospective remembering

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Writing down current thoughts before starting can reduce subjective mental clutter and aid organization

**Verdict: Supported.** An organizational aid, not a cure. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** Reducing a large assignment to its next smallest action can help task initiation

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 140

**Title:** Do This Instead of Saying "Pay Attention" | Helping Kids With #ADHD Focus  
**URL:** https://www.youtube.com/shorts/c9-pUNaKBDg  
**Views:** 8,348  
**Likes:** 375  
**Comments:** 4  
**Duration:** 54 seconds

**Status:**  for a kid who has ADHD focusing their attention can be genuinely tough to do they're not trying to not pay attention their brains are just busy so making direct eye contact for kids who are comfortable with that and using some kind of physical touch if it's appropriate for the relationship and setting can help better grab their attention like putting your hand on their shoulder during an instruction or in the classroom instead of saying something to the entire class the teacher can give a direct onetoone instruction to make it easier for them like next please write your name also directions that are a little more specific with a reminder of the actual task work best like eyes on me or please write the next sentence or put your code on the hook so instead of pay attention which is harder for them to understand just tell them exactly what to do

### Revised claim review

**Claim 1:** Children with ADHD can genuinely find it difficult to focus or sustain attention

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** A child’s failure to pay attention is not necessarily deliberate

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Establishing eye contact, when comfortable for the child, can help obtain their attention before giving an instruction

**Verdict: Supported.** Only when comfortable for the child; forced eye contact is not endorsed. Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Appropriate physical contact, such as placing a hand on the child’s shoulder, can help obtain their attention

**Verdict: Supported.** Only appropriate, welcome contact; not a requirement for every child. Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Giving a child with ADHD an individual instruction may be easier for them to follow than addressing the entire class

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Clear, brief, and task-specific directions are more helpful than a vague instruction such as “pay attention”

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Specific instructions of this kind always “work best” for children with ADHD

**Verdict: Excluded from scoring.** Repeated summary; always was introduced by the annotation rather than stated. Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 141

**Title:** Can You Have ADHD & OCD? Here's What Helps (From A Psychiatrist)  
**URL:** https://www.youtube.com/shorts/1nHTe9lUAKg  
**Views:** 27,111  
**Likes:** 975  
**Comments:** 39  
**Duration:** 53 seconds

**Transcript:**

> So, can I have ADHD and OCD at the same time? All the time. I see it particularly in children and grandchildren of alcoholics. What we see in the brain is the middle front part of the brain works too hard. And an area called the inferior orbital prefrontal cortex doesn't work hard enough. So, it's like you have low levels of both serotonin and dopamine. And early in my career, I'd use a combination of Prozac and rolin. Miraculous for some patients. Now, I'll use more supplement options like 5HTP and rodeiola ashwagandha gensing and just to help balance the brain happens all the time.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** ADHD and OCD can occur in the same person

**Verdict: Supported.** Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 2:** Co-occurring ADHD and OCD occurs particularly in children or grandchildren of people with alcoholism

**Verdict: Unsupported.** The special family-alcoholism association is not established. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 3:** The comorbidity is caused by an overactive middle-frontal region, an underactive inferior orbital prefrontal cortex, and simultaneous low serotonin and dopamine

**Verdict: Unsupported.** The scan/neurotransmitter mechanism is not established. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** 5-HTP, rhodiola, ashwagandha, and ginseng balance the brain and treat co-occurring ADHD and OCD

**Verdict: Unsupported.** The supplement combination is not established treatment. Evidence: [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 142

**Title:** The Best Career Path if You Have ADHD  
**URL:** https://www.youtube.com/shorts/ZizbA-MtjAs  
**Views:** 183,884  
**Likes:** 5,793  
**Comments:** 149  
**Duration:** 50 seconds

**Transcript:**

> So, for many people with ADHD, the best career is actually not one 50-year career. It's 10 five-year careers or five 10-year careers. And part of it is the whole work world has become more fragmented, and we're accepting more that many career trajectories are going to look not like just one beautiful arc. But I think there's a sort of a normo-centric bias to that is what you should strive for, and if you are changing careers, that's a bad thing. And yet lots of people who do worthwhile things in life, and often because of their more varied experience are bringing more to what they're doing. So I think we need to value that and embrace that as an option and accept that maybe for some people that is an optimal career path.

### Revised claim review

Fewer than two eligible claims; remains unlabelled.

**Claim 1:** For many people with ADHD, the best or optimal career path is five or ten different careers rather than one long career

**Verdict: Excluded from scoring.** A personal career preference and suggested option, not an externally verifiable optimum.

### Revised result

- Eligible fact-checkable claims: **0**
- Supported: **0**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **not defined** (no eligible claims).
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Unlabelled**.

---

## Video 143

**Title:** Adderall vs. Meth: The Truth About ADHD Medication  
**URL:** https://www.youtube.com/shorts/KvEgMRfHgoo  
**Views:** 9,663  
**Likes:** 215  
**Comments:** 72  
**Duration:** 60 seconds

**Transcript:**

> That is so nuts that people take meth. Why would you do that? And yet, what percentage of kids today are on aderall, >> which is the exact same thing, just a slow release, a delayed release meth? >> Absolutely wrong. It is not the exact same thing. Meth and Aderall are not the exact same thing. So, let's break this down. Although stimulants like aderall and vience and the street drug methamphetamine share some chemical similarities, the compounds are not the same. Okay. Prescription ADHD medications are carefully formulated, FDA approved, and taken in controlled doses to treat specific neurological symptoms. In contrast, meth is often illicitly manufactured, far more potent, rapidly absorbed by the brain, and highly addictive.

### Revised claim review

**Claim 1:** Adderall is not simply slow- or delayed-release methamphetamine

**Verdict: Supported.** The opening drug-equivalence assertion is explicitly rebutted. Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 2:** Prescription amphetamines and methamphetamine have chemical and pharmacological similarities but are not the same compound

**Verdict: Supported.** Evidence: [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 3:** Prescription ADHD stimulants are regulated, approved, clinically dosed medicines used to treat defined symptoms

**Verdict: Supported.** Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 4:** Illicit methamphetamine is generally more rapidly delivered, more potent in typical misuse, and highly addictive compared with prescribed oral ADHD stimulants

**Verdict: Supported.** Dose, route and purity distinguish typical illicit use from regulated oral prescribing; prescribed stimulants still have abuse potential. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [DEA](https://www.dea.gov/factsheets/stimulants).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 144

**Title:** ADHD symptoms and when to seek treatment  
**URL:** https://www.youtube.com/shorts/13kWle_1IaE  
**Views:** 9,784  
**Likes:** 65  
**Comments:** 3  
**Duration:** 65 seconds

**Transcript:**

> So the cardinal symptoms of ADHD are inattention, so trouble focusing, paying attention, hyperactivity, so moving around a lot, being really restless, and impulsivity, so doing things without thinking, like blurting out answers, and interrupting, things like that. Many people experience ADHD symptoms. Many of us have trouble paying attention, hyperactivity, being impulsive. But really, it's how severe these symptoms are, how much more relative to people our age and whether or not they're causing clinical impairments. So, is it disrupting aspects of our lives? And the symptoms should be present across multiple settings. So, not just in the home, but at school and in other settings. ADHD tends to be a lifelong disorder, but symptoms do tend to change over time. So as children with ADHD get older, their inattention symptoms tend to remain, but we see the hyperactivity tend to decrease or improve.

### Revised claim review

**Claim 1:** The principal ADHD symptom domains are inattention, hyperactivity, and impulsivity, with examples such as restlessness, blurting, and interrupting

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Diagnosis depends on symptoms being developmentally excessive, sufficiently severe or impairing, and present across more than one setting

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** ADHD often persists over the lifespan, while presentation can change and overt hyperactivity commonly decreases more than inattention with age

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 145

**Title:** Easy Natural Treatments for A.D.D. and A.D.H.D  
**URL:** https://www.youtube.com/shorts/7kVsgjnO1sQ  
**Views:** 4,028  
**Likes:** 128  
**Comments:** 3  
**Duration:** 49 seconds

**Transcript:**

> treatment for ADD and inattentive add is the same as classic very similar even though it's not identified until later the treatments are the same for almost all of these add I like identifying each add so you can see what it is but you're not going to see much variation in the treatment because they're also similar intense aerobic exercise I like to do Jiu Jitsu that's me right there in the the blue ghee the blue uniform um limit video games and T TV especially the the violent and the aggressive ones for somebody who has ADD inattentive add l-tyrosine again helps with the neurotransmitters fish oil where have we heard that before high protein low carb diet

### Revised claim review

**Claim 1:** The proposed ADD subtypes have nearly identical treatments

**Verdict: Supported.** Treatment principles overlap across recognized presentations; this does not validate seven scan types. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Intense aerobic exercise can help ADHD symptoms

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 3:** Limiting video games and television, particularly violent content, treats inattentive ADHD

**Verdict: Unsupported.** Media effects do not establish this dopamine-depletion account. Evidence: [MEDIA](https://pubmed.ncbi.nlm.nih.gov/36562860/).

**Claim 4:** L-tyrosine treats ADHD by helping neurotransmitter production

**Verdict: Unsupported.** Tyrosine efficacy is not established. Evidence: [TYR](https://pubmed.ncbi.nlm.nih.gov/3300376/).

**Claim 5:** Fish-oil supplementation may help ADHD

**Verdict: Unsupported.** Routine clinically reliable fish-oil efficacy is not established. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 6:** A high-protein, low-carbohydrate diet is an established ADHD treatment

**Verdict: Unsupported.** The general dietary treatment prescription is unsupported. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **2**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **2 / 6 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 146

**Title:** How do #periods impact #ADHD symptoms? #pms  
**URL:** https://www.youtube.com/shorts/ddAB8ekxMbY  
**Views:** 61,529  
**Likes:** 2,188  
**Comments:** 64  
**Duration:** 29 seconds

**Transcript:**

> I'm going to explain how your periods impact ADHD symptoms in less than 30 seconds. So, strap in. Two hormones you need to care about here, estrogen and dopamine. Estrogen increases the amount of dopamine made and decreases its breakdown. Dopamine helps you regulate attention and manage motivation. The week before your period, your estrogen levels drop. Less estrogen equals less dopamine equals more problems.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Oestrogen modulates dopamine synthesis, signalling, and breakdown

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Dopamine contributes to attention and motivational processes

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/).

**Claim 3 — clarified extraction:** Premenstrual oestrogen falls, so dopamine falls and ADHD problems increase.

*Original annotation wording:* Premenstrual hormonal changes can worsen ADHD symptoms in some people, potentially partly through oestrogen–dopamine interactions

**Verdict: Unsupported.** Possible hormonal associations do not establish this categorical oestrogen-to-dopamine-to-symptoms sequence. Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 147

**Title:** ADHD Executive Dysfunction explained in 1 minute and simple tips to overcome indecision fatigue  
**URL:** https://www.youtube.com/shorts/mE1Dz-NRaRw  
**Views:** 3,957  
**Likes:** 208  
**Comments:** 6  
**Duration:** 65 seconds

**Transcript:**

> Does your brain look at a to-do list with three very different items but tell you that they all weigh the same? This is a classic example of executive dysfunction. The neurotypical brain will tell you that all of these things weigh very different amounts and that will tell you get it out of the way first. But the ADHD brain does not do that. We have trouble waiting different things. I'm a doctor and I have ADHD. These are my top three ways that I overcame this kind of lack of capacity to make decisions. The first thing you can do is try a really simple coin flip. Heads or tails. The two tasks to pick. One is heads, the other one is tails. You know in your brain that it's not the right decision to make. You're going to pick the other one anyway. It's an intuitive process, but this takes you out of your trying to make decisions in your overwhelmed mind and puts you into that ability to be like, "Okay, that was not the right answer." Next one, lay out a deck of cards. Assign a number to each of these things. Whatever you pick out of the card deck, that's the one that you do first. The last thing I do is plug these into chat GPT and have it tell me which one is the most important. If you want more information about all the things that you can do to help your ADHD brain, check out the link in my bio. I have a school program that you can sign up for.

### Revised claim review

**Claim 1:** ADHD-related executive dysfunction can make prioritizing tasks and comparing their importance difficult

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Neurotypical brains automatically assign the correct weight to tasks, whereas ADHD brains do not

**Verdict: Unsupported.** The dopamine mechanism is not established. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** A coin flip reliably resolves ADHD decision fatigue by revealing the intuitively correct choice

**Verdict: Excluded from scoring.** An individual coping trick, not an efficacy claim for others.

**Claim 4:** Random card selection or asking ChatGPT to choose the most important task is an evidence-based solution to ADHD executive dysfunction

**Verdict: Excluded from scoring.** An individual method, not established ADHD treatment.

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **1**; unsupported: **1**; excluded: **2**.
- Supported-claim percentage: **1 / 2 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 148

**Title:** Being Diagnosed With ADHD As An Adult #adhd #mentalhealth #adultadhd  
**URL:** https://www.youtube.com/shorts/TaxmW5M2ojU  
**Views:** 31,750  
**Likes:** 1,530  
**Comments:** 97  
**Duration:** 61 seconds

**Transcript:**

> When were you diagnosed? >> I was diagnosed when I was 43. Typically what happens, kids get diagnosed and then through that process, the parent kind of goes, "Wait, now little junior is exactly like I was, right? Myself and my daughter, we did it the other way around. I actually got my diagnosis first and then we kind of went, hey, she's just like me." >> So, what made you seek a diagnosis? I I had always experienced, you know, what I know now are pretty common, I guess, feelings that that are associated with ADHD. But really the breaking point was when I I received a promotion into management. By all accounts, you know, my life had been pretty good. You know, things were going great outwardly. Inwardly, there was a tremendous amount of anxiety, even mild depression. That led me to just see a counselor, just see a therapist. Well, I remember telling her, "But I can't have ADHD because I hold down a job and I have a house and I have a family." And she goes, "Yeah, but how hard is it?" I went, "It's tough. It's tough. You know, it feels like I'm walking through 3 ft of water most of the

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** A parent may recognize their own possible ADHD after a child is assessed because ADHD is familial and highly heritable

**Verdict: Supported.** Familial patterns can prompt recognition; no personal family diagnosis was independently checked. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Holding a job, maintaining a home, or having a family does not rule out adult ADHD; impairment may be hidden by substantial effort or become clearer when demands increase

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 149

**Title:** ADHD medication pros and cons  
**URL:** https://www.youtube.com/shorts/5J0ytf28Jpc  
**Views:** 4,324  
**Likes:** 86  
**Comments:** 13  
**Duration:** 100 seconds

**Transcript:**

> I don't take medication for my ADHD, but a lot of people do like that option. Now, I have worked with a lot of people and some people say that ADHD medication has changed their life and other people say that it gave them horrendous anxiety. ADHD medication is not for everyone, but it is for some people. I personally think that people should also do the work and they should learn strategies that help them regulate their emotions and navigate all of the symptoms that go with ADHD as well. But often people do need the medication to get them started and to make things easier first. And I would say if you're going to take medication, please also learn strategies and please also get help with that side of things in whatever shape or form you can actually receive support with the symptoms of ADHD. Now, if you are considering medication for ADHD, we have 10 psychiatrists at my company, Private Therapy Clinic, who can give you very valuable information and can guide you and they can help you know when is it not a good idea to take medication or when is it a good idea to stop medication where you've tried it for a short period of time and the side effects are just not very good. And there's three different types of medication. There is stimulant, non-stimulant and slowrelease stimulant. If you are interested in exploring these options, either medication or ADHD coaching, feel free to get in touch. We can have chat with you and we can let you know the options.

### Revised claim review

**Claim 1:** ADHD medication can be life-changing for some people, can worsen anxiety or cause other adverse effects for others, and is not appropriate for everyone

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 2:** Skills, emotional-regulation strategies, and other supports can complement medication, while medication may make it easier for some people to use those strategies

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 3:** A qualified prescriber can help decide whether medication is appropriate or should be changed or stopped because of adverse effects

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

**Claim 4:** ADHD medication consists of exactly three types: stimulant, non-stimulant, and slow-release stimulant

**Verdict: Supported.** Listing immediate/extended-release options does not assert mutually exclusive medication classes. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 150

**Title:** Elimination Diets for ADHD Treatment  
**URL:** https://www.youtube.com/shorts/Ljhn2NoLonY  
**Views:** 482  
**Likes:** 5  
**Comments:** 0  
**Duration:** 78 seconds

**Transcript:**

> I've heard a lot about elimination diets, [music] removing things like artificial dyes, preservatives, sweeteners, and certain foods. Can you tell me if there's any evidence about using [music] these for children with ADHD? >> There are a lot of elimination diets for ADHD, the fine gold diet being one example, but some are even more restrictive. [music] Research shows that only a small subset of children with ADHD experience [music] improvement on these diets. But if hyperactivity and inattention are improved in [music] 10% of kids when you remove dyes, why not just try it? >> You might, but consider the downsides. Restrictive diets can increase stress around food, worsen picky eating, or lead to nutritional deficiencies if not properly supervised. They can also be difficult to maintain and socially isolating for children. So, what I'm hearing is elimination diets are not a replacement for proven ADHD treatments like behavioral therapies or medication, but in select cases, they may be considered under the guidance of a healthcare provider. >> Yes, ADHD care works best when it's individualized and discussed with all members of your child's treatment team. If you think this information might be helpful for your child, please discuss with your provider before starting an elimination diet.

### Revised claim review

**Claim 1:** Only a minority of children with ADHD show meaningful improvement from broad elimination diets

**Verdict: Supported.** Dietary response is confined to a susceptible subgroup, not all ADHD. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/), [INCA](https://pubmed.ncbi.nlm.nih.gov/21296237/).

**Claim 2:** Removing artificial colours may improve hyperactivity or inattention in a susceptible minority of children

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/), [INCA](https://pubmed.ncbi.nlm.nih.gov/21296237/).

**Claim 3:** Restrictive diets can increase food-related stress, worsen selective eating, cause nutritional deficiencies, be difficult to maintain, and create social burdens

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/), [INCA](https://pubmed.ncbi.nlm.nih.gov/21296237/).

**Claim 4:** Elimination diets are not replacements for established ADHD treatments but may be considered selectively with a healthcare professional and treatment team

**Verdict: Supported.** An approximate subgroup estimate, not an exact universal cure rate. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/), [INCA](https://pubmed.ncbi.nlm.nih.gov/21296237/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 151

**Title:** Natural Recommendations For Kids With ADHD  
**URL:** https://www.youtube.com/shorts/RICPsLSkZX8  
**Views:** 24,795  
**Likes:** 1,207  
**Comments:** 32  
**Duration:** 78 seconds

**Transcript:**

> So stimulants like rolin or aderall are the number one prescribed treatments for kids who have ADHD. It is never number one in my mind. Now I'm not opposed to medicine. I just it's not the first thing I think of. The first thing I think of is what's their diet like? There's a study from Holland that was replicated that showed when you k put kids on an elimination diet. They got rid of gluten, dairy, corn, soy, artificial dyes, and sweeteners, 70% did not have ADD after 3 months. Diet is so important. There's another study with phospatidal searing showing that it can be uh effective. Another study with picnogginal uh marine pine bark uh shown that that can be helpful. You also want to make sure you check their feritin levels. Feritin is a measure of iron storage because low iron. Low feritin levels have been associated with ADD and just giving them feritin sometimes can make a huge positive difference.

### Revised claim review

The treatment word ferritin is taken literally, without correcting the transcript. This is a wording-sensitive judgement; study-positive supplement claims are not treated as established clinical efficacy.

**Claim 1:** Stimulant medicines such as methylphenidate and amphetamine are leading evidence-based treatments prescribed to children with ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Removing gluten, dairy, corn, soy, artificial dyes, and sweeteners caused about 70% of children to no longer have ADHD after three months

**Verdict: Unsupported.** A selected short-term diet response was misrepresented as 70% no longer having ADHD after three months. Evidence: [INCA](https://pubmed.ncbi.nlm.nih.gov/21296237/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/).

**Claim 3 — clarified extraction:** A study suggests phosphatidylserine may help childhood ADHD.

*Original annotation wording:* Phosphatidylserine is an effective treatment for childhood ADHD

**Verdict: Supported.** Preliminary positive studies exist; this does not establish routine efficacy. Evidence: [PS](https://pubmed.ncbi.nlm.nih.gov/33539192/).

**Claim 4 — clarified extraction:** A study suggests maritime pine-bark extract may help childhood ADHD.

*Original annotation wording:* Pycnogenol or maritime pine-bark extract is an effective childhood ADHD treatment

**Verdict: Supported.** Positive small trials exist; overall certainty remains very low. Evidence: [PINERCT](https://www.sciencedirect.com/science/article/pii/S1756464622003164), [PINE](https://www.cochrane.org/evidence/CD008294_using-pine-bark-supplements-help-treat-variety-chronic-diseases).

**Claim 5:** Lower ferritin or iron status has been associated with ADHD in some studies

**Verdict: Supported.** An association, not proof of deficiency in every patient. Evidence: [FERRITIN](https://www.nature.com/articles/s41598-017-19096-x).

**Claim 6:** Giving “ferritin” can produce a major ADHD improvement

**Verdict: Unsupported.** Ferritin is a storage protein/biomarker, not the same as giving iron. The literal claim is not established. Evidence: [FERRITIN](https://www.nature.com/articles/s41598-017-19096-x), [IRON](https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **4**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **4 / 6 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 3 — Moderately misleading**.

**Decision limitation:** The supplied word “ferritin” is assessed literally rather than silently replaced with iron. Preliminary positive supplement studies do not establish routine efficacy. The intended treatment wording may change the label.

---

## Video 152

**Title:** Long-term use of amphetamines and stimulants can cause side effects.  
**URL:** https://www.youtube.com/shorts/vz-z-QRU_KI  
**Views:** 117,148  
**Likes:** 1,890  
**Comments:** 221  
**Duration:** 49 seconds

**Status:** amphetamines like Aderall they are stimulants similar to cocaine similar to caffeine and so when you are on a drug that's a constant stimulant it's going to increase the activity of certain organ systems which over time can be an issue there are going to be side effects and it's important to remember you cannot take a synthetic chemical for long term without there being some sort of side effect within the body even if we don't have a long-term study which that's one of the issues by the way there aren't a lot of long-term studies on the side effects of ADHD medications so prolonged use or short-term high dose usage can result in deterioration of your cognitive or physical abilities damage to the nerve cells

### Revised claim review

**Claim 1:** Amphetamines such as Adderall are stimulants, as are cocaine and caffeine

**Verdict: Supported.** Evidence: [DEA](https://www.dea.gov/factsheets/stimulants), [ADDIR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81).

**Claim 2:** Regular stimulant use increases the activity of certain organ systems and can eventually cause problems

**Verdict: Supported.** Potential harm, not an inevitable outcome. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [CVLONG](https://pubmed.ncbi.nlm.nih.gov/37991787/).

**Claim 3:** A synthetic chemical cannot be taken long-term without causing some bodily side effect

**Verdict: Unsupported.** Synthetic origin does not establish unavoidable harm from long-term use. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 4:** There are not many long-term studies examining the adverse effects of ADHD medication

**Verdict: Supported.** Long-term evidence is more limited than short-term trials; not a claim of no long-term studies. Evidence: [CVLONG](https://pubmed.ncbi.nlm.nih.gov/37991787/).

**Claim 5:** Prolonged stimulant use or short-term use at high doses can deteriorate cognitive or physical abilities

**Verdict: Supported.** High-dose/misuse risks are not evidence of inevitable harm from monitored therapeutic use. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 6:** Prolonged or short-term high-dose stimulant use can damage nerve cells

**Verdict: Unsupported.** Nerve-cell damage is not established for prescribed therapeutic use as framed. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **4**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **4 / 6 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 153

**Title:** 5 Ways To Reduce Hyperactivity  
**URL:** https://www.youtube.com/shorts/yqOaoRdxTDg  
**Views:** 236,151  
**Likes:** 2,645  
**Comments:** 22  
**Duration:** 37 seconds

**Transcript:**

> Five ways to reduce hyperactivity. Hyperactivity is purposeless movement of a child which is very common in autism spectrum disorder. First is make a fixed routine of a child. Second is reduce the calorie intake by low calorie diet like low carbohydrate diet, no chocolates or fast food. Third is nutritional supplementation by vitamin B6 and B12. Fourth is increase physical activity by dancing, swimming, running, cycling and fifth is slow music like bird or river sound.

### Revised claim review

**Claim 1:** Hyperactivity is purposeless movement and is very common as a defining feature of autism spectrum disorder

**Verdict: Unsupported.** Hyperactivity is not defined as purposeless movement or a defining autism feature. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** A predictable routine can help reduce behavioural dysregulation in some autistic or hyperactive children

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Reducing calories and carbohydrates and eliminating chocolate and fast food treats hyperactivity

**Verdict: Unsupported.** This broad dietary prescription is not established treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 4:** Vitamins B6 and B12 reduce hyperactivity

**Verdict: Unsupported.** Routine B6/B12 treatment efficacy is not established. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

**Claim 5:** Regular physical activity may help manage hyperactivity and support regulation

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 6:** Slow music or nature sounds are an established treatment for hyperactivity

**Verdict: Unsupported.** Music/nature sounds are not established treatment for hyperactivity. Evidence: [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **2**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **2 / 6 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 154

**Title:** ADHD Meds: Stimulant vs. Non-Stimulant â€“ How Doctors Decide Whatâ€™s Safe  
**URL:** https://www.youtube.com/shorts/boyStBJXcDU  
**Views:** 2,499  
**Likes:** 20  
**Comments:** 1  
**Duration:** 67 seconds

**Transcript:**

> So when we think about medications we usually think about stimulants and non-stimulants. So um certainly you know having a prior you know medical evaluation or p certainly for you know adults and children at least as a psychiatrist knowing if people have any sort of underlying medical problems usually is a good idea. For example cardiovascular health having things like poorly controlled hypertension high blood pressure can put people at risk for things like heart attack and stroke. We understand that stimulants may have a mild to moderate mild to moderate, you know, risk of increasing blood pressure. Um, so I essentially want to make sure that somebody may have, you know, if they have any sort of concerns with cardiovascular health that at least it's being addressed and it's being targeted by a, you know, an internist, for example, family medicine physician or a cardiologist. Absolutely. So step one, you have your stimulant medications, you have your non-stimulant medications. When evaluating a patient for use of stimulant medications, like Pat is saying, the first thing is first you have to make sure that it's

### Revised claim review

**Claim 1:** ADHD medicines are commonly divided into stimulant and non-stimulant classes

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 2:** A medical history and evaluation for relevant health problems should precede and inform ADHD prescribing

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 3:** Poorly controlled hypertension increases cardiovascular risk, and stimulants can raise blood pressure and heart rate

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 4:** Existing cardiovascular concerns may require management or specialist input when stimulant treatment is considered

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 155

**Title:** HSP & ADHD #adhd #highlysensitiveperson #healing  
**URL:** https://www.youtube.com/shorts/R1O1VbVGqrc  
**Views:** 5,842  
**Likes:** 628  
**Comments:** 74  
**Duration:** 130 seconds

**Status:** # tactiq.io free youtube transcript
# HSP & ADHD #adhd #highlysensitiveperson #healing
# https://www.youtube.com/watch/R1O1VbVGqrc

00:00:00.400 If you are highly sensitive, you may
00:00:02.399 also have ADHD. I've been talking on
00:00:05.040 this for years now, but I'm going to
00:00:06.319 break it down. Highly sensitive people
00:00:09.599 are not mirrored by society or their
00:00:11.599 family most of the time. It's a rare
00:00:14.160 thing. It's becoming more prominent
00:00:15.599 because people are figuring things out.
00:00:17.600 But when you're born that way and you
00:00:18.960 feel different than your family system
00:00:20.640 and you feel different than the world
00:00:22.560 and you think differently and you have a
00:00:24.080 different consciousness, you're going to
00:00:26.000 feel like you don't belong. You're going
00:00:27.519 to have some emotional wounds. I say
00:00:30.160 that a lot of HSPs, highly sensitive
00:00:32.558 people have ADHD because I've seen that
00:00:34.559 in the last 13 years of my work and in
00:00:36.559 myself also a lot of people who are
00:00:39.280 highly sensitive have a lot of wounds
00:00:41.360 which equal trauma which can also be
00:00:43.280 ADHD as a trauma response or ADHD as
00:00:46.640 someone who has multi-dimensional
00:00:48.160 learning in a system that only honors
00:00:51.200 one way. So check it out. When I was
00:00:54.079 younger and diagnosed, I it was so
00:00:56.719 stigmatized. I thought it was such a
00:00:58.320 negative thing, yet I knew inside there
00:00:59.840 was something very positive about it
00:01:01.199 because I was tuning into things that
00:01:03.120 nobody else really could understand. It
00:01:05.600 took me many years to find the clear
00:01:07.119 language to explain things in my way to
00:01:11.040 help others understand things that I was
00:01:13.760 experiencing.
00:01:15.520 But many of you who are coming to me now
00:01:17.360 and say, &quot;I don't know if I'm HSP or
00:01:19.200 ADHD.&quot; I say, &quot;Who cares? You're a
00:01:21.439 highly sensitive soul in a society that
00:01:23.520 was not built for you. Period.&quot; So
00:01:26.080 instead of seeing this as a negative
00:01:27.680 thing or seeing this as a disorder,
00:01:30.400 dysfunction or something working against
00:01:33.200 you because you're so sensitive to
00:01:34.560 everything, we need to really start to
00:01:36.079 heal those wounds and empower ourselves
00:01:37.439 to see that we are the leaders of the
00:01:38.799 new authentic era that is happening
00:01:40.880 here. When we start to empower these
00:01:42.799 sensitivities, for me, my ADHD symptoms
00:01:46.000 disappeared when I went to college
00:01:47.680 because I started doing things my own
00:01:49.119 way and I learned how to have an
00:01:50.479 environment that fed me instead of
00:01:52.240 starved me. So really my work is helping
00:01:54.799 you to not only empower your gifts and
00:01:57.040 heal your wounds which go together but
00:01:58.960 to really step into the purpose you were
00:02:01.200 born to lead because you were born
00:02:02.560 perfect for your purpose. Society wasn't
00:02:04.560 perfect for you. So we are here to
00:02:06.320 create a new one. If you're with me, let
00:02:08.318 me know in the comments.

### Revised claim review

**Claim 1:** A highly sensitive person may also have ADHD

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 2:** Highly sensitive people are rarely understood or “mirrored” by their families or society, although this is becoming more prominent

**Verdict: Excluded from scoring.** General HSP commentary, outside the ADHD claim unit.

**Claim 3:** Highly sensitive people are born with a different consciousness from other people

**Verdict: Excluded from scoring.** A philosophical consciousness assertion, outside this clinical coding unit.

**Claim 4:** Being highly sensitive inevitably causes a person to feel that they do not belong and to develop emotional wounds

**Verdict: Excluded from scoring.** A general HSP narrative, not an eligible ADHD claim.

**Claim 5:** A large proportion of highly sensitive people have ADHD

**Verdict: Unsupported.** The stated large proportion is not established. Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 6:** Emotional wounds are equivalent to trauma

**Verdict: Excluded from scoring.** General trauma terminology rather than an ADHD assertion.

**Claim 7:** ADHD can itself be a trauma response

**Verdict: Unsupported.** Overlap and adversity associations do not establish ADHD itself as a trauma response. Evidence: [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8:** ADHD represents “multidimensional learning” occurring within a society that recognizes only one learning method

**Verdict: Unsupported.** This proposed learning-system explanation is not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 9:** Distinguishing HSP from ADHD does not matter, and ADHD should not be regarded as a disorder or dysfunction

**Verdict: Excluded from scoring.** Personal/valuative framing, not a separately testable clinical assertion.

**Claim 10:** Healing emotional wounds and finding an empowering environment can make ADHD symptoms disappear

**Verdict: Excluded from scoring.** The speaker’s personal healing narrative was generalized by the annotation; excluded.

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **6**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 156

**Title:** TREATING ADHD with Innovative Therapy AT HOME (Dr. Richard Abbey) #shorts  
**URL:** https://www.youtube.com/shorts/G25g5qqHoqo  
**Views:** 1,931  
**Likes:** 48  
**Comments:** 2  
**Duration:** 47 seconds

**Transcript:**

> breaking news everybody did you know you can actually remediate your child's difficulty and help them overcome their problem without external forces you can actually image their brain and see what's going on and all they got to do is watch like a movie because you have a brain computer interface to exercise their brain we've worked with thousands of clients and they have overcome their problem and it's quite amazing when you sit back and you can see what the child can do and realize their potential what is your potential how would you know unless you measure it we show you precisely what the potential is and how to target that and so you can provide that for your child [Music] you

### Revised claim review

**Claim 1:** Brain imaging can precisely reveal a child’s ADHD problem and an at-home brain–computer interface used while watching a movie can remediate or overcome it

**Verdict: Unsupported.** The claimed precise diagnosis and corrective system are not validated. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Thousands of clients have overcome their ADHD-related problem through this system

**Verdict: Unsupported.** The quantitative success claim is not independently substantiated. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** The system can measure a child’s potential precisely and identify exactly how to target it

**Verdict: Unsupported.** Precise measurement of a child’s potential and exactly targeted correction is unsupported. Evidence: [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0 / 3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 157

**Title:** How To Increase Energy In Someone With ADHD  
**URL:** https://www.youtube.com/shorts/Yku6HG8d0Jo  
**Views:** 27,810  
**Likes:** 1,132  
**Comments:** 34  
**Duration:** 33 seconds

**Transcript:**

> so rather than turning to energy drinks which are loaded with all sorts of chemicals outside of caffeine or overdoing it on things like coffee a nice way to increase energy in someone with ADHD would be eleanine eleanine is a natural amino acid it is calming and focusing but for a person with ADHD can also provide a nice amount of energy if you combine that with some B vitamins and ideally bouts of exercise throughout the day that is a good way of keeping energy level up

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** L-theanine is calming and focusing while also providing substantial energy specifically for people with ADHD

**Verdict: Unsupported.** A very small exploratory study does not establish these ADHD benefits. Evidence: [THEAN](https://pubmed.ncbi.nlm.nih.gov/32753637/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science), [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 2:** Combining L-theanine with B vitamins and intermittent exercise is a reliable way to maintain energy in ADHD

**Verdict: Unsupported.** The combination has not been established as a reliable energy treatment. Evidence: [THEAN](https://pubmed.ncbi.nlm.nih.gov/32753637/), [NCCIH](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science), [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **0**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **0 / 2 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Original Markdown label: **Label 4 — Highly misleading**.

---

## Video 158

**Title:** How ADHD leads to intense focus | Andrew Huberman x Joe rogan  
**URL:** https://www.youtube.com/shorts/0Qk1RvuW5Zc  
**Views:** 96,108  
**Likes:** 3,001  
**Comments:** 56  
**Duration:** 25 seconds

**Status:** # tactiq.io free youtube transcript
# How ADHD leads to intense focus | Andrew Huberman x Joe rogan
# https://www.youtube.com/watch/0Qk1RvuW5Zc

00:00:00.040 if you look at kids or adults with ADHD
00:00:02.240 like true attention deficit disorder or
00:00:04.200 hyperactivity disorder you don't always
00:00:05.720 have the hyperactivity what you find is
00:00:07.319 they can focus really well if it's on
00:00:09.639 something they like so a kid with ADD or
00:00:11.559 ADHD that loves video games that kid
00:00:13.639 will play video games with laser focus
00:00:15.360 for 3 hours that sounds like me but then
00:00:17.160 you put them in front of something they
00:00:18.199 don't want to do and they just can't
00:00:19.760 anchor their discipline they just don't
00:00:21.480 have the discipline that also sounds
00:00:23.119 like me

### Revised claim review

**Claim 1:** A person with ADHD does not necessarily exhibit hyperactivity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** People with ADHD may sustain intense concentration on activities they find interesting or rewarding, such as video games

**Verdict: Supported.** Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 3:** When a person with ADHD cannot focus on an unwanted task, the underlying problem is insufficient discipline

**Verdict: Unsupported.** Executive/attention impairment cannot be reduced to inadequate discipline. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 159

**Title:** ADULT ADHD  Symptoms Diagnosis Dr Rajiv Psychiatrist à¤¹à¤¿à¤‚à¤¦à¥€ à¤®à¥‡à¤‚ #adhd  #adultadhd #mentalhealth  
**URL:** https://www.youtube.com/shorts/QTTLA1hpi0U  
**Views:** 28,363  
**Likes:** 829  
**Comments:** 35  
**Duration:** 57 seconds

**Status:** If someone is having addiction inability to stick with a job, unable to mantain relationships, gets irritated, impulsive behavior, loses temper easily, these could be symptoms of ADHD. Interrupting others when talking, unable to wait for his/her turn, fidgeting, inattention symptoms, make silly mistakes, inability for sustained attention, unable to follow instructions, disorganized, short attention span, forgetfulness in daily activities, all these can be symptoms of ADHD

### Revised claim review

CLAIM-BLOCK CORRECTION: the three original annotations were copied from Video 158. They are replaced with this transcript’s actual claims. The transcript itself is unchanged.

**Claim 1 — clarified extraction:** Adult ADHD can be associated with addiction, job difficulties and relationship problems.

*Original annotation wording:* A person with ADHD does not necessarily exhibit hyperactivity

**Verdict: Supported.** The original claim block had been copied from Video 158 and did not describe this transcript. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/).

**Claim 2 — clarified extraction:** Emotional dysregulation can occur in adult ADHD.

*Original annotation wording:* People with ADHD may sustain intense concentration on activities they find interesting or rewarding, such as video games

**Verdict: Supported.** Emotion dysregulation can accompany ADHD. Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3 — clarified extraction:** Hyperactivity and impulsivity can occur in adult ADHD.

*Original annotation wording:* When a person with ADHD cannot focus on an unwanted task, the underlying problem is insufficient discipline

**Verdict: Supported.** Recognized symptom domains. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4 — added from supplied transcript:** Inattention can occur in adult ADHD.

**Verdict: Supported.** Explicitly stated in the supplied transcript. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 160

**Title:** Can ADHD Be Treated Holistically? ðŸ’Š  
**URL:** https://www.youtube.com/shorts/PuRtbsWp8L0  
**Views:** 8,208  
**Likes:** 590  
**Comments:** 7  
**Duration:** 43 seconds

**Transcript:**

> can add be treated without medication the answer is yes add can be addressed holistically through a number of different strategies including exercise especially cardio enhancing blood flow to the front of your brain helps with Focus number two supplements things like Omega-3s phosphoserine ashwagandha jinsang riola but also neuro feedback can be very helpful neuro feedback allows us to train electrical activity in our brain which helps enhance Focus lastly behavioral strategies setting up your workspace to serve you as opposed to distract you

### Revised claim review

**Claim 1:** ADHD can be managed without medication through a combination of non-pharmacological strategies

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Aerobic exercise may improve focus in ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 3:** Omega-3, phosphatidylserine, ashwagandha, ginseng, and rhodiola are effective ADHD supplements

**Verdict: Unsupported.** This supplement list is not established as generally effective ADHD treatment. Evidence: [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children), [PS](https://pubmed.ncbi.nlm.nih.gov/33539192/), [ASH](https://pubmed.ncbi.nlm.nih.gov/42602386/), [RHOD](https://clinicaltrials.gov/study/NCT02737020).

**Claim 4:** Neurofeedback can train patterns of brain activity and may help attention

**Verdict: Unsupported.** Learning EEG feedback is not equivalent to established clinical benefit on blinded ADHD outcomes. Evidence: [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/).

**Claim 5:** Modifying the workspace to reduce distraction can support ADHD functioning

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 161

**Title:** Whatâ€™s the deal with ADHD and skin picking? | Experts Answer  
**URL:** https://www.youtube.com/shorts/0rRIMTVaMOI  
**Views:** 32,603  
**Likes:** 2,485  
**Comments:** 87  
**Duration:** 59 seconds

**Transcript:**

> What's the deal with ADHD and skin picking? Well, skin picking, along with nail biting, nose picking, cheek biting, hair pulling, are collectively known as the body focused repetitive behaviors, or BFRBs. It's a mouthful. Having ADHD absolutely places someone at higher risk for BFRBs. Now, it's not really a surprise as to why. BFRBs are associated with individuals who seek those behaviors to achieve self-soothing, grounding. Sometimes people engage in those behaviors mindlessly, as almost a fidget, whether they're playing with their hair, and then it might result in pulling their hair, or picking at their cuticles, or biting their nails, all of which affect people with ADHD. Studies have also shown that these behaviors can create a dopamine response in the brain, and we know how the ADHD brain craves that dopamine. There are many successful strategies and mindful strategies that can help people with these conditions, so that they don't have to get in your way.

### Revised claim review

**Claim 1:** Skin picking, nail biting, cheek biting, and hair pulling are examples of body-focused repetitive behaviours

**Verdict: Supported.** Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/).

**Claim 2:** ADHD is associated with an increased likelihood of BFRBs

**Verdict: Supported.** Evidence: [BFRBCO](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552165/).

**Claim 3:** BFRBs may function as self-soothing, grounding, sensory stimulation, or automatic fidget-like behaviour

**Verdict: Supported.** Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/).

**Claim 4:** BFRBs produce dopamine specifically because the ADHD brain craves dopamine

**Verdict: Unsupported.** The proposed ADHD dopamine-craving mechanism is not established. Evidence: [STIM](https://www.nature.com/articles/1301164), [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/).

**Claim 5:** Behavioural and mindfulness-based strategies can help manage BFRBs

**Verdict: Supported.** Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **4**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **4 / 5 × 100 = 80.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 162

**Title:** Signs of ADHD in teens | Experts answer  
**URL:** https://www.youtube.com/shorts/tExHmO6lUoI  
**Views:** 4,687  
**Likes:** 159  
**Comments:** 0  
**Duration:** 49 seconds

**Transcript:**

> what are the signs of ADHD in teens one of the big signs is an increase in high-risk Behavior especially among untreated ADHD so kids in high school with untreated ADHD are much more likely to drive quickly to drink too much to vape too much to be impulsive in social media to have poor grades the other things we see in high school is we see an uptick and academic rigor and we see the social stuff just gets more and more stressful trying to manage social media and trying to manage relationships in high school can be really challenging so what we see is kids that are struggling more academically we see kids that maybe are falling behind socially and we see kids with an increase in Risky Behavior so all of those things are signs in high school and the truth is is that ADHD while it's lifelong often gets diagnosed at different ages and stages so it's really important no matter what the age is to identify early and to diagnose and treat it can make a huge difference

### Revised claim review

**Claim 1:** Adolescents with poorly managed ADHD have elevated rates of risky driving, substance use, online impulsivity, and academic problems

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Increased academic and social demands in high school can expose or intensify ADHD-related impairment

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** ADHD often persists over time, may be diagnosed at different ages, and appropriate identification and treatment can substantially improve outcomes

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 163

**Title:** 4 Quiet Signs of ADHD #adhd #adhdtiktok  
**URL:** https://www.youtube.com/shorts/aKeWbltwDIU  
**Views:** 12,804  
**Likes:** 863  
**Comments:** 31  
**Duration:** 75 seconds

**Transcript:**

> here are four signs you might have ADHD and not know it number one you're constantly overwhelmed but never seem to finish anything feeling like there's always too much on your plate can be a common experience with ADHD you might start multiple tasks but because of distraction lack of focus or difficulty prioritizing you often leave them unfinished number two you replay conversations in your head for hours this is often a sign of adhd's emotional impulsivity you may find yourself overthinking past interactions second guessing what you said or how you came across to others number three you organize everything but still feel chaotic even when you try to be organized it might feel like you're efforts don't stick you could spend time arranging things perfectly yet still feel like there's an underlying sense of disarray this can happen because ADHD often affects not just physical organization but also time management and mental Clarity leaving you with a sense of mental clutter and number four you either underperform or overperform ADHD can create a cycle of underperforming because of lack of focus or overperforming as a way to cover up difficulties with perfectionism this list is not meant to diagnose ADHD if you are curious or identify with these signs it's important to reach out to a licensed professional who can help assess your situation and provide guidance tailored to you

### Revised claim review

**Claim 1:** ADHD can involve chronic overwhelm, difficulty prioritizing, starting multiple tasks, and failing to finish them

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Replaying conversations for hours is a sign of “ADHD emotional impulsivity”

**Verdict: Unsupported.** Replaying conversations is not itself emotional impulsivity; the claimed identification is unsupported. Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

**Claim 3:** A person with ADHD may create visible organization while continuing to struggle with time management and mental organization

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** ADHD can contribute to inconsistent performance, including underperformance or compensatory overwork and perfectionism

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** This list cannot diagnose ADHD, and assessment should be obtained from a qualified professional

**Verdict: Supported.** Evidence: [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **4**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **4 / 5 × 100 = 80.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 164

**Title:** 5 Signs of ADHD  
**URL:** https://www.youtube.com/shorts/fm9aVF3T1A4  
**Views:** 326  
**Likes:** 20  
**Comments:** 2  
**Duration:** 61 seconds

**Transcript:**

> five signs of ADHD from a naturopathic doctor number one is appearing high functioning this can look like a workaholic or a very busy individual however under the surface many can be very scattered in their efforts and be spinning their wheels excessively to get things done number two is hyperfocus many individuals have the ability of hyperfocusing on things that they enjoy or find meaningful and cannot focus on things they don't enjoy or don't find meaningful number three is time blindness and difficulty with time management this can tend to go hand inand with hyperfocusing by focusing on things excessively and forgetting about other important areas of life number four is difficulty controlling emotions those of us with ADHD can expend a lot of energy trying to focus and not have much reserves for emotional resilience and number five is impulsive shopping or spending this can also include risk-taking or taking drugs in order to increase levels of dopamine that are typically lower in the ADHD brain If

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** Some people with ADHD appear highly functional or busy while expending excessive effort and remaining disorganized

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 2:** Many people with ADHD can hyperfocus on meaningful activities and cannot focus on activities they do not enjoy or find meaningful.

*Original annotation wording:* People with ADHD can hyperfocus on anything meaningful and cannot focus on anything uninteresting

**Verdict: Unsupported.** Many is retained. However, the unqualified inability in the second part exceeds evidence of difficulty sustaining attention; the earlier review replaced cannot with struggling. Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** ADHD is commonly associated with impaired time management and losing track of time during absorbing activities

**Verdict: Supported.** Evidence: [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 4:** Emotional dysregulation in ADHD occurs because focusing uses up the energy reserves needed for emotional resilience

**Verdict: Unsupported.** The energy-reserve mechanism is not established. Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 5:** Impulsive spending, risk-taking, and drug use in ADHD occur to increase dopamine that is typically low in the ADHD brain

**Verdict: Unsupported.** Risk associations do not establish a uniformly low-dopamine motive. Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **2**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **2/5 × 100 = 40.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Previous reviewed label: **Label 2**.
- Uploaded CSV label: **Label 3**.

---

## Video 165

**Title:** 10 Signs itâ€™s ADHD and Autism (Part 1) #videopodcast  
**URL:** https://www.youtube.com/shorts/znIpbOS8E9M  
**Views:** 69,750  
**Likes:** 3,027  
**Comments:** 82  
**Duration:** 60 seconds

**Transcript:**

> 10 signs that you may have autism and ADHD social interaction is number one so we know autistic people have difficulty with social interaction and communication however those with ADHD can also struggle with social cues and have a hard time waiting for their time to speak or play number two repetitive behaviors now the common sign of autism is repetitive and restrictive behaviors but people with ADHD can also display repetitive movements like tapping their feet or fingers number three sensory sensitivities so autistic people as you know we can be hypo or hyper sensitive so that's like over or under experience okay so imagine being hypersensitive to certain sensory stimuli this is interesting though people with ADHD also experience sensitivity to noise light Touch number four hyperactivity hyperactivity is also a common sign of ADHD

### Revised claim review

The autism facts are part of an explicit ADHD-versus-autism comparison, so remain within the relationship/differential-diagnosis coding unit.

**Claim 1:** Difficulties with social communication and interaction are central features of autism

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 2:** ADHD can interfere with social cues, conversational turn-taking, and waiting during play

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 3:** Restricted and repetitive patterns of behaviour are a core autism domain

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 4:** People with ADHD may show repetitive tapping of the feet or fingers

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 5:** Autism can involve hyper- or hyporeactivity to sensory input

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 6:** Sensitivity to noise, light, or touch can also occur in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 7:** Hyperactivity is a common ADHD feature

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **7**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **7 / 7 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 166

**Title:** Signs of ADHD in pre-teens | Experts answer  
**URL:** https://www.youtube.com/shorts/GVQXwQkmGng  
**Views:** 3,157  
**Likes:** 124  
**Comments:** 7  
**Duration:** 53 seconds

**Transcript:**

> what are the signs of ADHD and prein this is the age where executive functioning begins to really matter both socially and academically so in middle school it's the first time that kids are sort of independent academically they walk around from class to class they're responsible for their own assignments there's a lot less scaffolding so this is a moment where we might see kids that were doing fine in elementary school move into middle school and struggle with remembering to turn in their homework keeping on a schedule understanding where they're supposed to be socially it's also a time where kids are becoming more independent your parents are no longer scheduling playdates for you you're now responsible for initiating communication following through lastly the other thing we see in middle school it's when we begin to see a lot more of ADHD in attentive type in lower school in elementary school we often see disruptive behavior we see hyperactive but in Middle School what you might see are kids that aren't necessarily hyperactive but in the classroom they may be more inattentive and so that may get picked up in middle school where it didn't get picked up in elementary school

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** The increasing organizational and social demands of middle school can reveal previously compensated ADHD difficulties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 2:** ADHD in pre-teens may appear as missed assignments, schedule problems, uncertainty about where to be, and difficulty initiating or following through socially

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 3:** Predominantly inattentive ADHD may be recognized later than disruptive hyperactive behaviour because it is less outwardly noticeable

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 167

**Title:** What can ADHD in kids look like? Examples of ADHD in Children. #Shorts  
**URL:** https://www.youtube.com/shorts/IUsfAbUc6cc  
**Views:** 19,057  
**Likes:** 350  
**Comments:** 8  
**Duration:** 54 seconds

**Transcript:**

> There are a few common situations that I hear over and over again from parents. None of these alone mean that a child has ADHD, but these are complaints that I hear frequently. The first is, they'll sit down with me to do their homework or play really well when it's just the two of us, but when there are kids around, they start looking for more attention or just look kind of uninterested. Another common complaint is, transitions are really hard. They can't stop what they're doing to do something else without a big problem, like getting ready to leave the house or even come to the table for dinner. And the third common complaint is, they have meltdowns and really big emotions and reactions over things that seem small or out of proportion to us. The emotions seem to come out of nowhere. They can go from zero to 10 within a second. This last one makes me think about how for many kids with ADHD, emotions seem to live right below the surface all the time.

### Revised claim review

**Claim 1:** A child with ADHD may perform better one-to-one than in a distracting group setting

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** Difficulty stopping one activity and transitioning to another is common in children with ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** Some children with ADHD show rapid, intense emotional reactions or meltdowns

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** None of these behaviours alone establishes that a child has ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 168

**Title:** 7 Symptoms of ADHD in Adults  
**URL:** https://www.youtube.com/shorts/Wgxv9cwqp9o  
**Views:** 528,053  
**Likes:** 10,771  
**Comments:** 508  
**Duration:** 28 seconds

**Transcript:**

> symptoms of inattentive ADHD in adults number one having a short attention span and being easily distracted number two making careless mistakes for example in school work or during tasks for a job number three appearing forgetful or losing things number four being unable to stick to tasks that seem tedious or time consuming number five appearing to be unable to listen or follow instructions number six constantly changing activities or tasks and number seven having difficulty organizing tasks

### Revised claim review

**Claim 1:** A short attention span and easy distractibility can be adult inattentive ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 2:** Frequent careless mistakes can be an inattentive symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 3:** Forgetfulness and frequently losing necessary items can be inattentive symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 4:** Difficulty persisting with tedious or time-consuming tasks can be an inattentive symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 5:** Appearing not to listen or failing to follow through on instructions can be inattentive symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 6:** Frequently shifting activities without completion can occur in adult ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

**Claim 7:** Difficulty organizing tasks is an inattentive symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NHS](https://www.nhs.uk/conditions/adhd-adults/).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **7**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **7 / 7 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 169

**Title:** Signs of ADHD in Kids - 3 Key Things to Watch For #Shorts  
**URL:** https://www.youtube.com/shorts/UfMqnKVcKcI  
**Views:** 12,566  
**Likes:** 215  
**Comments:** 2  
**Duration:** 46 seconds

**Transcript:**

> How do you really know if signs of ADHD are a problem? Like if they're a normal part of development or a phase or part of a different problem like anxiety or even just a reaction to their environment. Make sure to consider these three key things when it comes to ADHD symptoms. One, how long has this been going on? For many with ADHD, parents can often look back and see signs of these symptoms when their kids were toddlers or pretty young. Number two, does it cause problems both at home and at school or with other caregivers? Are you having trouble managing some of it? Are there teachers telling you there are problems? And number three, are you noticing problems with self-control and self-regulation in multiple ways? Are you seeing several behaviors or challenges in at least one of those categories I mentioned in a previous video? So if you are wondering

### Revised claim review

**Claim 1:** ADHD-like behaviour must be distinguished from normal development, anxiety, and reactions to the environment

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 2:** ADHD symptoms begin early in life, although apparent signs in toddlerhood are not themselves diagnostic

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 3:** Clinically significant symptoms should cause problems across more than one setting or relationship context

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 4:** Diagnosis requires multiple persistent symptoms involving self-control and/or attention rather than a single isolated behaviour

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 170

**Title:** Signs of ADHD in Women  
**URL:** https://www.youtube.com/shorts/Im9JK_08VbE  
**Views:** 30,080  
**Likes:** 974  
**Comments:** 30  
**Duration:** 58 seconds

**Transcript:**

> signs of ADHD in women we don't see the signs as much because women become very good at compensating for the struggles that they have so some of those struggles might be not being able to stay organized balancing your checkbook keeping your schedule organized getting your work projects in on time people might think that you are spaced out all of those executive function skills planning organization attention focus and the way that that plays out very practically is in your schedule and keeping everything running in your home in your work being able to get everything done on time and stay efficient what to do about that is have your brain assessed to see if you are using the brain pattern that creates and perpetuates ADHD that we can use neuroplasticity to change the way that your brain performs

### Revised claim review

**Claim 1:** ADHD may be missed in women because some compensate for or mask their difficulties

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Adult ADHD in women can involve organization, scheduling, deadline, attention, and efficiency difficulties

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** A brain assessment can identify the brain pattern creating and perpetuating ADHD, after which neuroplasticity can be used to change that pattern

**Verdict: Unsupported.** The promised individual brain-pattern identification and corrective intervention are not established. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [EEG](https://www.neurology.org/doi/10.1212/WNL.0000000000003265), [NF](https://pubmed.ncbi.nlm.nih.gov/39661381/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 171

**Title:** 4 signs you may have ADHD. How many do you have? #adhd #adhdinwomen  
**URL:** https://www.youtube.com/shorts/17ozeuKzSR8  
**Views:** 19,609  
**Likes:** 1,115  
**Comments:** 35  
**Duration:** 83 seconds

**Transcript:**

> You thought ADHD meant being bad or being wild, so you assumed you couldn't have it. You struggle to finish tasks even when you're interested in them. You feel chronically overwhelmed, but can hyperfocus on things you love and lose hours doing them. You second guess yourself constantly. Am I just lazy? Am I just irresponsible? You feel like you're always performing in life and underneath it, you're exhausted. Getting an ADHD diagnosis isn't about making excuses. It's about finally understanding yourself and giving yourself the tools you've always deserved. Because ADHD isn't a failure of willpower. It's a different way of moving through the world. And once you know how your brain is wired, you can stop fighting yourself and start building a life that actually fits you. Whether you see yourself in the inattentive type, hyperactive type, combined, or somewhere in between, you're not broken. You're not lazy. You're not too much or not enough. You just deserve support that actually works for the real you. The more we see ADHD as the wide, beautiful spectrum that it is, the more people will stop blaming themselves and start thriving. If this resonated with you, I'd love to hear your story in the comments. And if you know someone who might need to hear this too, please share this video with them. You never know who might be quietly struggling and finally feel seen because of

### Revised claim review

**Claim 1:** ADHD can involve difficulty completing tasks, chronic overwhelm, and prolonged absorption in highly interesting activities

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** ADHD-related impairment is not simply bad behaviour, laziness, irresponsibility, or failed willpower

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** ADHD has predominantly inattentive, predominantly hyperactive-impulsive, and combined presentations and shows wide individual variation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 172

**Title:** If ADHD & Autism overlap, you might see these 10 signsâ€¦ #AuDHD #Neurodivergent  
**URL:** https://www.youtube.com/shorts/zWLOxOAXqOY  
**Views:** 33,394  
**Likes:** 2,040  
**Comments:** 52  
**Duration:** 73 seconds

**Transcript:**

> You know you're neurode divergent, but you're not sure if it's ADHD or autism. What if it's both? Here's 10 signs that it might be in under 60 seconds. You need rigid structure to function, but you can never stick to one because it's far too boring. You hyperfocus on something interesting for hours, but you still can't start the task. You absolutely hate surprises, but equally, you get bored very easily. You crave novelty, but change is far too overwhelming. You plan everything out in perfect detail, then end up doing it all last minute anyway. You love new things, but transitions are impossible. You crave social connection. It leaves you totally drained. You rehearse conversations meticulously, but you still end up interrupting or talking too fast and then overthinking later. You cannot stand certain textures. or sounds or smells, but equally you chase that sensory stimulation. You feel like the ultimate masker, and you feel like you're constantly burning out from it. These things can't diagnose you, but they can give you a clue as to which direction to look in. What do you think? Let me know in the comments.

### Revised claim review

**Claim 1:** Autism and ADHD can occur together

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 2:** Co-occurring autism and ADHD can create tension between a preference for predictability and ADHD-related novelty or stimulation seeking

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 3:** A person with both conditions may intensely focus on an interesting subject while still struggling to initiate required tasks

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 4:** A person with both conditions may dislike surprises and changes while also becoming bored easily or seeking novelty

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 5:** Detailed planning, last-minute completion, and difficult transitions can occur with co-occurring autism and ADHD

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 6:** Social connection may be desired but exhausting, and rehearsed conversations may still involve interruption or rapid speech

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 7:** Both sensory avoidance and sensory seeking can occur

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 8:** Masking may contribute to exhaustion or burnout

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 9:** These experiences cannot diagnose autism, ADHD, or their co-occurrence

**Verdict: Supported.** The explicit no-diagnosis caveat matters when interpreting the possible experiences. Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **9**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **9 / 9 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 173

**Title:** 7 Signs of ADHD in Women No Oneâ€™s Talking About  
**URL:** https://www.youtube.com/shorts/aAiwAdL-XjE  
**Views:** 17,037  
**Likes:** 1,071  
**Comments:** 21  
**Duration:** 155 seconds

**Transcript:**

> Seven hidden signs of ADHD that are often missed in women. Number one is rejection sensitivity. You may feel crushed by criticism that other people may just barely notice. And your body may flood with shame when you think that someone might be disappointed in you. And it's not just like being really sensitive. It's like your whole nervous system going into this high alert zone. Number two is this invisible struggle. So, while you may look calm on the outside, your mind might be racing with worry and self-doubt and that's exhausting like that constant mental like checklist that no one can see that you're managing. And your ADHD doesn't look like hyperactivity. It might be this like quiet storm inside of you. Number three is being lost in your mind. You may zone out mid-con conversation and then suddenly realize you've missed everything that people were just talking about. And your daydreaming isn't really laziness. It's just your brain seeking the stimulation it craves when reality is not providing enough. It's just part of ADHD. Number four is feeling like a fraud. So you worked twice as hard, but you still feel like you're barely keeping up. And that voice telling you you don't belong here is not the truth. It's your ADHD making simple tasks feel overwhelming. Number five is the connection gap. You may desperately want close relationships but feel like there's just this wall, this invisible wall between you and others. And this isn't your fault. It's your brain processing social cues differently in a way that makes it hard to connect. Number six is this learning paradox. Maybe you aced tests, but you can't remember what you learned at all. Your brain might have been hyperfocused on the challenge, but didn't actually store the information long term. This isn't a character flaw. It's just how attention sometimes works in ADHD. And number seven is sensory overload. Certain sounds, smells, textures may completely derail you. This happens to me, too. And your intense reactions are not like being dramatic or whatever. It's your brain processes sensory information differently from other people. The medical system has not given enough attention to how ADHD presents in women. And your struggles are not character flaws. They're just symptoms. They're symptoms of a real neurological difference that deserves care, that deserves understanding, and that deserves support. And feel free to check the links in my bio for more

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Rejection sensitivity with whole-body high alert is a hidden sign of ADHD in women

**Verdict: Supported.** Associated rejection distress, not a unique female diagnostic symptom. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Women with ADHD may show internal restlessness, worry, or compensatory mental effort rather than conspicuous motor hyperactivity

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 3:** Daydreaming in ADHD occurs because the brain seeks stimulation when reality provides too little

**Verdict: Unsupported.** This single stimulation-seeking mechanism is not established. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Some women with ADHD work unusually hard to compensate while still finding routine tasks overwhelming

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 5:** Difficulty forming close relationships in women with ADHD is caused by the brain processing social cues differently

**Verdict: Supported.** Social processing difficulties can contribute; not an exclusive cause. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 6:** A woman may perform well on tests but fail to store the material long term because ADHD hyperfocuses on the challenge without encoding memory

**Verdict: Unsupported.** The asserted hyperfocus-without-encoding mechanism is not established. Evidence: [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/).

**Claim 7:** Sensory over-responsivity can occur in ADHD

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 8:** ADHD has historically been under-recognized in women

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **6**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **6 / 8 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 174

**Title:** How to spot ADHD in women ðŸ’š #adhd #adhdbrain #neurodivergent  
**URL:** https://www.youtube.com/shorts/ohGLvsy4HCg  
**Views:** 1,510,933  
**Likes:** 132,835  
**Comments:** 7,231  
**Duration:** 60 seconds

**Transcript:**

> how to spot ADHD and women in 25 seconds they will overthink everything that's because the hyperactivity is in their heads it's like five squirrels on speed barreling around up there and it never stops ever and this will cause a lot of anxiety which is why so many women were misdiagnosed with an anxiety disorder they will be great in a crisis but can become overwhelmed over something small they will overshare at Social Gatherings and then spend months thinking everyone thought they were too much and now hates them even their best friends they will have a messy room but know the exact location of everything when someone tells them a story they will reply with a similar story they're not trying to make it all about them it's their way of showing they understand they'll be very good at hiding their problems so people will think they're happy maintaining friendships is hard because object permanence makes it easy to forget people exist they will spend their life feeling like they are constantly just barely staying above water they'll wish they could go back in time put their arms around the younger version of themselves and reassure them that everything is going to be okay and that they're not broken just different

### Revised claim review

**Claim 1:** Women with ADHD characteristically overthink because their hyperactivity is located inside the head, which causes anxiety and misdiagnosis

**Verdict: Unsupported.** Internal restlessness does not establish the overthinking-to-anxiety causal account. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Being excellent in crises but overwhelmed by small tasks is a sign of ADHD in women

**Verdict: Unsupported.** Crisis excellence is not established as a characteristic female ADHD sign. Evidence: [STIM](https://www.nature.com/articles/1301164), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Impulsive oversharing followed by prolonged rumination can occur in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

**Claim 4:** Having a messy room while knowing the location of everything is a sign of ADHD in women

**Verdict: Unsupported.** Messiness does not establish knowing where everything is. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 5:** Responding to another person’s story with a similar personal story is an ADHD way of showing empathy

**Verdict: Unsupported.** A conversational style does not establish an ADHD-specific empathy mechanism. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 6:** Women with ADHD may mask or conceal impairment effectively

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 7:** ADHD makes friendships difficult because impaired “object permanence” causes people to forget that friends exist

**Verdict: Unsupported.** Forgetting contact is not loss of object permanence. Evidence: [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/), [WM](https://pubmed.ncbi.nlm.nih.gov/23688211/).

**Claim 8:** Women with ADHD may experience substantial hidden effort and chronic difficulty keeping up with daily demands

**Verdict: Supported.** Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **3**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **3 / 8 × 100 = 37.50%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 175

**Title:** 5 signs your boyfriend or husband may have adhd #mentalhealth #education #adhd #facts #hope  
**URL:** https://www.youtube.com/shorts/JqCE4fsmXaE  
**Views:** 24,695  
**Likes:** 1,103  
**Comments:** 53  
**Duration:** 61 seconds

**Transcript:**

> five signs that your boyfriend or husband has ADHD I just share from experience I was diagnosed add at 13 rediagnosis is back in the '90s I'm 43 now so I've had to live with it a majority of my life and these are five signs that your husband boyfriend probably has ADHD the first one is there conversation hijackers that especially with guys we will jump to the conclusions we will steal your conversation to try and understand and relate because instead of saying hey hun I don't understand this we do it through storytelling instead where we will literally steal your conversation to try and get you to validate that yes we understand your feelings instead though is something that will piss people off it's very common especially with men also to the point where we will jump to the conclusions of trying to solve instead of listening and we don't break it down if somebody wants to vent or if somebody wants to actually have a solution this is one of the big challenges when it comes to ADHD another one is is our forgetfulness with the man uh with guys especially we will lose our keys our wallet our phone we will lose everything it's a lot of different return trips we

### Revised claim review

**Claim 1 — clarified extraction:** Men with ADHD redirect conversations through their own stories to obtain confirmation that they understand the other person’s feelings.

*Original annotation wording:* ADHD-related impulsivity can cause interruption, jumping to conclusions, or redirecting a conversation through one’s own story

**Verdict: Unsupported.** Impulsive interruption can occur, but this specific gendered conversational mechanism and motive are not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 2:** Men with ADHD commonly try to solve a partner’s problem instead of listening because of ADHD

**Verdict: Unsupported.** The proposed male relationship style and ADHD-specific cause are not established. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 3:** Frequently losing keys, a wallet, a phone, or other necessary items can be an inattentive ADHD symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 176

**Title:** Unexpected Physical Symptoms in ADHD #adhd #chronicillness #chronicpain #migraine  
**URL:** https://www.youtube.com/shorts/z1ZyO8BuCPM  
**Views:** 136  
**Likes:** 2  
**Comments:** 0  
**Duration:** 53 seconds

**Transcript:**

> What I found is many of them presented somatically. They had symptoms that weren't part of the core ADHD diagnosis. They had fibromyalgia. They had chronic pain. They had a lot of somatic issues like atypical migraine headaches. They had interstitial cyitis. More recently, I've seen an increase in patients complaining of POTS, postural hypertension. I've seen patients with other complaints. I don't know if you've seen list with an increase in eer Danlopes syndrome. So patients would present in a complex way with psychiatric condition and they were doctor pursuing some of their somatic issues often without good results.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

The POTS term is assessed exactly as supplied. No transcription correction or video retrieval was attempted.

**Claim 1:** Fibromyalgia, chronic pain, and migraine are not core ADHD symptoms but may co-occur at elevated rates

**Verdict: Supported.** Evidence: [PAIN](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/), [MIGRAINE](https://pubmed.ncbi.nlm.nih.gov/37752867/).

**Claim 2:** Interstitial cystitis is a characteristic somatic presentation of ADHD

**Verdict: Excluded from scoring.** The speaker describes a clinic observation, not a generalized prevalence assertion.

**Claim 3:** POTS has recently become more common among patients with ADHD

**Verdict: Excluded from scoring.** A personal clinic trend, not a population trend.

**Claim 4:** Ehlers–Danlos syndrome or joint hypermobility may occur more frequently in neurodevelopmental populations including ADHD

**Verdict: Supported.** Evidence: [HYPERMOB](https://pmc.ncbi.nlm.nih.gov/articles/PMC7882457/).

**Claim 5:** These physical conditions require separate medical evaluation rather than being assumed to arise from core ADHD

**Verdict: Excluded from scoring.** Clinical framing/advice rather than an additional independent fact claim.

**Claim 6 — added from supplied transcript:** POTS means postural hypertension.

**Verdict: Unsupported.** POTS refers to postural orthostatic tachycardia syndrome, not postural hypertension. Evidence: [POTS](https://www.ninds.nih.gov/health-information/disorders/postural-tachycardia-syndrome-pots).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **3**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** The supplied POTS expansion says postural hypertension. The correct term involves tachycardia. This flags wording only; no transcription verification was performed.

---

## Video 177

**Title:** 7 Subtle Signs of Adult ADHD #mentalhealth #adhd #focus #attention  
**URL:** https://www.youtube.com/shorts/vI4_LNUSpK0  
**Views:** 855  
**Likes:** 0  
**Comments:** 0  
**Duration:** 48 seconds

**Transcript:**

Yes, adult ADHD is a real condition. The most common signs would be the inability to sustain attention at times, even restlessness, recklessness, impulsivity, lack of focus, forgetfulness, and forgetfulness. It's also very common, and in some cases, you'll see hyperfocus in adults as well. It's only a disorder if it's affecting your day-to- day functioning. You're experiencing distress as a result of the severity of these symptoms, and it's persistent over a period of time.

### Revised claim review

First review of the author-supplied English replacement, 9 September 2026. Repeated forgetfulness and overlapping focus/attention wording are not counted twice. The list describes possible adult features, not seven independently sufficient diagnostic tests.

**Claim 1 — revised extraction:** Adult ADHD is a recognized condition that can involve inattention, restlessness, impulsivity, risk-taking and forgetfulness.

*Original annotation wording:* Adult ADHD is a real disorder whose common features include persistent inattention, restlessness or hyperactivity, impulsivity, poor focus, and forgetfulness

**Verdict: Supported.** These are recognized adult manifestations or associated behaviors, with variation between people; risk-taking is not a separate required DSM symptom. Evidence: [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know).

**Claim 2 — revised extraction:** Some adults with ADHD experience episodes of intense sustained focus or hyperfocus.

*Original annotation wording:* Intense or prolonged task focus can occur in adults with ADHD

**Verdict: Supported.** Self-report research supports its occurrence. It is neither unique to ADHD nor a formal diagnostic requirement. Evidence: [UPD_HYPER_PUBLISHER](https://link.springer.com/article/10.1007/s12402-018-0272-y).

**Claim 3 — revised extraction:** Persistent ADHD symptoms must affect day-to-day functioning to constitute the disorder.

*Original annotation wording:* ADHD requires persistent symptoms that cause clinically significant distress or day-to-day functional impairment

**Verdict: Supported.** Impairment and persistence are necessary. Childhood onset, multiple settings and exclusion of better explanations also matter; distress alone does not replace impairment. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate** — see the interpretation note below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** Hyperfocus and recklessness are not stand-alone diagnostic criteria. The final statement is treated as describing necessary persistence and impairment, not a complete diagnostic checklist or a requirement that every person report subjective distress.

---

## Video 178

**Title:** ADHD + Autism = AuDHD. Here's what that can really feel likeâ€¦  
**URL:** https://www.youtube.com/shorts/wJT9vX_zDck  
**Views:** 153,283  
**Likes:** 6,155  
**Comments:** 174  
**Duration:** 58 seconds

**Duplicate note:** This URL is identical to video 80 and is retained to preserve the source numbering.

**Transcript:**

> ADHD and autism frequently co-occur. Many people with one or the two diagnosis show elevated traits of both ADHD and autism. Common experiences for ADHD and autism include sensory differences, intense focus on specific interests, rejection sensitivity, executive dysfunction, sleep issues, and emotional regulation. Someone with ADHD is more likely to seek out the novelty and make more impulsive decisions. Whereas an autistic person is more likely to crave routine and structure and order. If someone is autistic and has ADHD, they're known as ADHD. They may experience an internal struggle and tension between their competing autistic and ADHD traits and a heightened experience of shared traits.

### Revised claim review

WORDING FLAG: this differs from Video 80’s supplied AuDHD terminology. The two supplied texts are scored as written; neither transcription nor source identity is corrected.

**Claim 1:** ADHD and autism frequently co-occur

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** People diagnosed with either condition may show elevated traits associated with the other

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** Sensory differences, executive dysfunction, sleep problems, and emotional-regulation difficulties can occur in both conditions

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 4:** Intense focus on particular interests can occur in both ADHD and autism

**Verdict: Supported.** Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 5:** Rejection sensitivity is a common feature of both ADHD and autism

**Verdict: Unsupported.** Reported rejection distress does not establish common prevalence in both conditions. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 6:** ADHD is associated with greater novelty seeking and impulsive decisions, whereas autism is associated with preference for routine and sameness

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 7 — clarified extraction:** Co-occurring autism and ADHD is known as “ADHD”.

*Original annotation wording:* “AuDHD” is an informal term for co-occurring autism and ADHD

**Verdict: Unsupported.** The supplied transcript says ADHD for the combined condition; the original annotation silently changed this to AuDHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 8:** Co-occurrence can create tension between traits and increase the burden of overlapping difficulties

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **6**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **6 / 8 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The supplied combined-condition term is “ADHD”; the original annotation changed it to “AuDHD”. If the author confirms AuDHD, Claim 7 changes and the ratio becomes Label 1.

---

## Video 179

**Title:** What are some signs of ADHD |Psychiatrist in Cardiff  | Dr. Raman Sakhuja  
**URL:** https://www.youtube.com/shorts/gFhyItRmV5g  
**Views:** 190  
**Likes:** 2  
**Comments:** 0  
**Duration:** 41 seconds

**Transcript:**

> so here is my brain and I have had an injury to this brain either through trauma or some other reasons whether it is surgery or any other cause and now I am having difficulties with in attention not able to concentrate or Focus have forgetfulness memory issues what could that be is it primarily an ADHD no that is actually what we call as secondary ADHD after having an injury to the brain for whatever cause

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** New attention, concentration, memory, or executive symptoms arising after a brain injury are not automatically primary developmental ADHD

**Verdict: Supported.** Evidence: [TBI](https://pmc.ncbi.nlm.nih.gov/articles/PMC8276124/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** “Secondary ADHD” is a term used for ADHD-like syndromes emerging after traumatic or other acquired brain injury

**Verdict: Supported.** Evidence: [TBI](https://pmc.ncbi.nlm.nih.gov/articles/PMC8276124/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 180

**Title:** What are impulsive symptoms of ADHD?  
**URL:** https://www.youtube.com/shorts/DbpDokHNpck  
**Views:** 1,230  
**Likes:** 28  
**Comments:** 4  
**Duration:** 61 seconds

**Transcript:**

> do I have ADHD I'm an adult and what are these impulsive symptoms well you would have been impulsive all your life and this may have expressed and you're a child with running around and getting into difficulties running across roads being a Flight Risk people having to your parents having to keep hold of you uh impulsively doing something that seems like a good idea at the time because it is more sensation seeking and it's thrilling but actually it's not really such a good idea when you think about it as an adult you might be have got into debt because you spend you're impulsively spending on the internet online there's no filter between what you think and what you say or between what you think and what you do you can't stop you just do it and that gets you into all sorts of problems you've probably littered with upsetting people people that you care about you don't mean to do it but it just comes out before you can stop it you can find out more on my website

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Adult ADHD impulsivity should have roots in childhood rather than appearing for the first time in adulthood

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Childhood impulsivity may include unsafe running, road behaviour, or acting on thrilling ideas without considering consequences

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Sensation seeking and acting before considering consequences can occur with ADHD impulsivity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Adult impulsivity can contribute to online spending, debt, unfiltered speech, and acting before thinking

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 5:** Impulsive speech or action can unintentionally damage relationships

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 181

**Title:** How does #perimenopause impact #adhd symptoms??  
**URL:** https://www.youtube.com/shorts/NeIXtUf2HxU  
**Views:** 17,221  
**Likes:** 752  
**Comments:** 46  
**Duration:** 43 seconds

**Transcript:**

> explained how perimenopause and menopause impacts ADHD symptoms in less than 60 seconds there are two hormones you need to care about here estrogen and dopamine estrogen increases the amount of dopamine made and decreases its breakdown dopamine helps you regulate attention and manage motivation during perimenopause your estrogen levels start to drop less estrogen less dopamine more problems this includes increased impulsivity distractibility difficulty with organization and problems with time management add on top of that mood swings insomnia physical changes into the mix no wonder you're miserable

### Revised claim review

**Claim 1:** Oestrogen modulates dopaminergic signalling relevant to attention and motivation

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2 — clarified extraction:** When oestrogen falls during perimenopause, dopamine falls and ADHD symptoms increase.

*Original annotation wording:* Perimenopausal hormonal changes can worsen impulsivity, distractibility, organization, and time-management difficulties in some people with ADHD

**Verdict: Unsupported.** The supplied categorical oestrogen/dopamine sequence is stronger than the emerging clinical evidence. Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 3:** Mood changes, insomnia, and other menopausal symptoms can add to functional difficulty

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 182

**Title:** What it means when people with ADHD masking their symptoms?  
**URL:** https://www.youtube.com/shorts/ssUAcwx3kbA  
**Views:** 1,301  
**Likes:** 40  
**Comments:** 0  
**Duration:** 60 seconds

**Transcript:**

> we hear often about people with ADHD masking their symptoms with strategies but what does that really mean well first of all they may not just simply deliberately don't tell anyone about it and that's fear of stigma what will my boss think what will my colleagues think so they just don't tell anyone secondly they may camouflage their behavior and this is the quiet person who can doesn't cause problems or who can hold it together for a short period but it's very difficult to suain thirdly there's what's known as buffering these are protective mechanisms that aim to reduce the impact of stress on psychological well-being this is bravard oh I'm fine I'm okay yeah I'm good or perhaps even a self presentation is being dismissive and arrogant this leads to an underestimation of underlying problems strategies may also be dysfunctional however like using drugs and alcohol promiscuity

### Revised claim review

**Claim 1:** Some people with ADHD conceal their diagnosis because they fear workplace or social stigma

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

**Claim 2:** ADHD masking can involve suppressing visible behaviour or appearing quiet and controlled for a limited period at substantial effort

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

**Claim 3:** Bravado, dismissiveness, or insisting that everything is fine can conceal underlying difficulty

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

**Claim 4 — clarified extraction:** Some people may use alcohol, drugs or sexual behaviour to cope with or conceal difficulties.

*Original annotation wording:* Drug use, alcohol use, and promiscuity are masking strategies characteristic of ADHD

**Verdict: Supported.** Possible maladaptive coping, not a defining or inevitable ADHD behaviour. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 183

**Title:** ADHD or BPD? Spot the Difference!  
**URL:** https://www.youtube.com/shorts/3lHFO_dd0X4  
**Views:** 46,640  
**Likes:** 2,394  
**Comments:** 106  
**Duration:** 32 seconds

**Transcript:**

> Think you might have borderline personality disorder? Not so fast. ADHD can look surprisingly similar. Both involve impulsivity and emotional roller coasters, but here's the key difference. ADHD typically starts in childhood while BPD emerges later in life. ADHD also involves persistent inattention or hyperactivity, which aren't core features of BPD. Remember, only a professional can diagnose you, but knowing these differences can help you advocate for yourself.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** ADHD and borderline personality disorder can both involve impulsivity and emotional lability

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** ADHD begins in childhood, whereas borderline personality disorder is generally identified from adolescence or early adulthood

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** Persistent inattention and/or hyperactivity are central to ADHD but not core BPD criteria

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** Professional assessment is required to distinguish these conditions

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 184

**Title:** 3 symptoms of #ADHD with Main Line Health's psychologist, Jamie DiOrio  
**URL:** https://www.youtube.com/shorts/CUe_7XlxBZU  
**Views:** 1,866  
**Likes:** 15  
**Comments:** 0  
**Duration:** 62 seconds

**Transcript:**

> According to the CDC, approximately one in 17 adults in the US is diagnosed with ADHD and more than half of those adults aren't diagnosed until adulthood. As a licensed psychologist, here are three common symptoms you might not know of that could suggest a person has ADHD. One is internal feelings of restlessness. In other words, person might feel like they constantly have to be moving or doing something or they feel uncomfortable being still for any length of time. Two is frequently getting sidetracked. This is the person who's constantly bouncing from one activity to another to another without actually finishing anything. And three is being forgetful. That might look like forgetting about appointments or forgetting to return phone calls. There are significant benefits to knowing if you have ADHD. Here at Main Line Health, we have the advanced diagnostic tools needed to be able to assess adults for ADHD. Visit our website for more information.

### Revised claim review

The prevalence and age-at-diagnosis statements use the 2023 US survey population and current-diagnosis definition.

**Claim 1:** Approximately one in 17 US adults has a current ADHD diagnosis

**Verdict: Supported.** Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 2:** More than half of currently diagnosed US adults received the diagnosis during adulthood

**Verdict: Supported.** Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 3:** Internal restlessness and frequently becoming sidetracked can be adult ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Frequent forgetfulness, including missed appointments or calls, can be an ADHD symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 185

**Title:** Signs You Might be AuDHD (ADHD & Autism) #autism #audhd #adhd  
**URL:** https://www.youtube.com/shorts/ntRa7aLTo0A  
**Views:** 97,416  
**Likes:** 6,576  
**Comments:** 162  
**Duration:** 64 seconds

**Transcript:**

> signs you might be ADHD. So, what is ADHD? It's meeting the diagnostic criteria for both autism and ADHD, but it's not quite like having two separate brains because you are meeting the criteria with one brain. So, it's kind of its own thing where the nuances of the way that autism and ADHD interact with each other in one person creates almost like a separate experience. So, these are the signs you need structure, but you can't stick to one. You get overwhelmed by too many thoughts or you have no thoughts at all. All the tabs are open or your brain is forced quitting. You crave lots and lots of social connection, but you struggle with small talk. You feel like you're both too much and not enough at the same time. You overexlain everything or you barely speak at all. You plan every single second or you completely wing it chaotically. You have focused interests, but you can't focus on them because you get distracted. If this sounds familiar, you're not broken and you're definitely not alone. You just might be ADHD.

### Revised claim review

WORDING FLAG: no missing syllable or transcription wording was silently repaired. The label is conditional on the supplied wording.

**Claim 1 — clarified extraction:** “ADHD” means meeting the diagnostic criteria for both autism and ADHD.

*Original annotation wording:* “AuDHD” informally refers to meeting diagnostic criteria for both autism and ADHD

**Verdict: Unsupported.** The supplied word is ADHD, whereas the definition describes AuDHD. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** Co-occurrence may create tension between needing structure and struggling to maintain plans or routines

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** A person with both conditions may desire social connection while finding small talk or communication difficult

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 4:** Focused interests can coexist with ADHD distractibility and difficulty directing attention

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 5:** The listed contradictory experiences show that a person probably has AuDHD

**Verdict: Excluded from scoring.** The speaker says might and recommends consideration; probably was added by the annotation.

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The supplied term is “ADHD”, whereas its definition describes co-occurring autism and ADHD. If the author confirms AuDHD, Claim 1 changes and the ratio becomes Label 1.

---

## Video 186

**Title:** What are the symptoms of ADHD? | ABC NEWS  
**URL:** https://www.youtube.com/shorts/DF5KxtWpS3I  
**Views:** 11,432  
**Likes:** 366  
**Comments:** 0  
**Duration:** 66 seconds

**Transcript:**

> Certified ADHD coach Kirsten Lightfoot helps guide neurode divergent clients, but for decades didn't recognize the chemical imbalance in her own brain. She only sought an assessment after her four children were diagnosed. Now aware she also has ADHD, she better understands common symptoms like rejection sensitivity dysphoria or RSD, which can make negative feedback feel like a personal attack. I have significant RSD, so I could remember things where I'd said something slightly wrong when I was five. And so I was able to go back and reframe it as opposed to that it was a fault of mine. >> RSD can also lead to self-doubt and feed into task paralysis described as extreme procrastination. But some symptoms are the exact opposite like hyperfocus, the ability to lock into a subject to the exclusion of everything else for hours, like forgetting to eat or use the bathroom. Understanding the symptoms and learning how to explain our ADHD to friends and family is key. It's unclear how many Australians are living with ADHD because not all are diagnosed.

### Revised claim review

**Claim 1:** ADHD is caused by a “chemical imbalance” in the brain

**Verdict: Unsupported.** A simple chemical-imbalance explanation is not established. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** Rejection-sensitive dysphoria is a common ADHD symptom that makes negative feedback feel like a personal attack

**Verdict: Supported.** RSD is informal terminology for associated rejection distress, not a separate DSM diagnosis. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [JUSTICE2](https://pubmed.ncbi.nlm.nih.gov/24878677/).

**Claim 3 — clarified extraction:** Rejection-related distress can contribute to self-doubt and task avoidance.

*Original annotation wording:* RSD causes self-doubt and ADHD “task paralysis” or extreme procrastination

**Verdict: Supported.** Avoidance/self-doubt can follow rejection distress; not a universal mechanism. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** Prolonged absorption in a subject to the point of neglecting eating or toileting can occur in ADHD

**Verdict: Supported.** Evidence: [HYPER](https://pubmed.ncbi.nlm.nih.gov/30267329/).

**Claim 5:** Australia’s true ADHD prevalence is uncertain because some affected people remain undiagnosed

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [TRENDS](https://pubmed.ncbi.nlm.nih.gov/24464188/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **4**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **4 / 5 × 100 = 80.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 187

**Title:** ADHD Explained: Key Symptoms, Diagnosis Criteria & Early Signs Before Age 12  #rachnabuxani #adhd  
**URL:** https://www.youtube.com/shorts/42c8OIxFS6c  
**Views:** 1,000  
**Likes:** 34  
**Comments:** 9  
**Duration:** 46 seconds

**Transcript:**

So ADHD is attention deficit hyperactive disorder. The DSM is where all these disorders are listed, right? And according to the DSM, it is a disorder if it affects your social and occupational functioning. Any disorder, right? So, if I'm having a hard time focusing because I've just had a death in the family, and now you know I'm grieving, so you know I have a little brain fog, but you know I'm not able to pay attention to many things because I'm in the grieving process, then that is not ADHD. Right? For someone to be diagnosed with ADHD, we have to see the symptoms before they are 12 years of age.

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** According to the DSM, any condition is a disorder if it affects social and occupational functioning.

*Original annotation wording:* DSM diagnosis of ADHD requires clinically significant social, academic, or occupational impairment

**Verdict: Unsupported.** Functional impact alone is not a sufficient universal DSM diagnostic rule, and impairment in both named domains is not required for every disorder. Evidence: [UPD_APA_MENTAL](https://www.psychiatry.org/patients-families/what-is-mental-illness), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Concentration problems attributable only to a recent bereavement are not, by themselves, ADHD.

*Original annotation wording:* Temporary concentration difficulty during grief is not by itself ADHD

**Verdict: Supported.** A developmental history and alternative explanations must be considered. Grief can coexist with ADHD; this example does not rule out previously existing ADHD in a bereaved person. Evidence: [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know).

**Claim 3:** Several ADHD symptoms must have been present before age twelve for a DSM ADHD diagnosis.

*Original annotation wording:* Several ADHD symptoms must have been present before age 12

**Verdict: Supported.** This concerns symptom onset, not necessarily a diagnosis or recognition before twelve. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2/3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 1**.

---

## Video 188

**Title:** Dealing with Trauma-Induced ADHD Symptoms  
**URL:** https://www.youtube.com/shorts/8gWlKupEHAk  
**Views:** 356  
**Likes:** 7  
**Comments:** 0  
**Duration:** 58 seconds

**Transcript:**

> hi everybody I'm Dr Carolyn kokar Ross and today I'm going to be talking to you about childhood adversity and its impact on attention deficit hyperactivity disorder so trauma exposure has been linked to changes in brain structure and function particularly in the areas of the brain responsible for regulating attention impulsivity and emotional regulation all of which are implicated in Ada HD and these brain changes could potentially increase the risk of developing ADHD or exacerbate existing symptoms behavioral patterns can also have an impact children who grow up in families affected by intergenerational trauma may be more likely to experience adversity and stressors themselves which then can contribute to the development of ADHD symptoms

### Revised claim review

**Claim 1:** Childhood adversity and trauma exposure are associated with changes in systems involved in attention, impulse control, and emotional regulation

**Verdict: Supported.** Association and overlapping functions, not proof of a single cause. Evidence: [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/).

**Claim 2:** Adversity may increase the likelihood of ADHD diagnosis or exacerbate existing ADHD symptoms

**Verdict: Supported.** Adversity associations do not establish causal direction. Evidence: [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/).

**Claim 3:** Intergenerational trauma can increase a child’s exposure to adversity and stress, contributing to ADHD-like or ADHD-related symptoms

**Verdict: Supported.** Family/intergenerational association, not deterministic inheritance of trauma. Evidence: [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 189

**Title:** Adult ADHD vs Child ADHD: Symptoms, Diagnosis & Treatment Explained (Dr. Neha Khurana)  
**URL:** https://www.youtube.com/shorts/iIy3ea2Q0s0  
**Views:** 211  
**Likes:** 0  
**Comments:** 1  
**Duration:** 78 seconds

**Transcript:**

> Did you know that there are about 8.7 million adults in the US currently living with ADHD? So, let's talk about it. How is adult ADHD different from childhood ADHD? Well, the symptoms that persist into adulthood are mostly those of inattention. You will find that these individuals have difficulty sustaining mental effort. So, they often procrastinate on their tasks. They have problems with prioritization, time management, and organization. This creates significant challenges as an adult both in their professional and personal lives. There are a lot of options for adults living with ADHD. Primary option includes medications. But there is also non-farmacological support. You can work with a counselor who specializes in treatment of ADHD. You can work with coaches, especially life coaches and executive coaches. And there are also apps that can help you make your to-do lists, help with habit tracking, motivation. When we talk about medications primarily, we're talking about both stimulant and non-stimulant options. I would encourage you to get a diagnosis of ADHD if any of the symptoms seem familiar and to talk to your healthcare provider about starting medication options.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

The 8.7-million estimate is a real published estimate. A later, differently defined survey estimate does not by itself make an undated older statement false.

**Claim 1:** About 8.7 million US adults currently live with ADHD

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Inattention often remains prominent into adulthood while overt hyperactivity may decline

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Adult ADHD can involve difficulty sustaining mental effort, procrastination, prioritization, time management, and organization, impairing work and personal life

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Medication, ADHD-focused counselling, coaching, and organizational tools can support adults

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** Both stimulant and non-stimulant medication options exist

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** Familiar symptoms should lead to a professional diagnostic assessment and discussion of appropriate options rather than self-diagnosis

**Verdict: Supported.** Evidence: [US87](https://pubmed.ncbi.nlm.nih.gov/34806909/), [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **6**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **6 / 6 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 190

**Title:** Treating Depression and ADHD Together  
**URL:** https://www.youtube.com/shorts/SgMCnXVizpA  
**Views:** 11,380  
**Likes:** 329  
**Comments:** 3  
**Duration:** 31 seconds

**Transcript:**

> so if I'm an adult and I have been diagnosed with depression and ADHD do I treat one before the other or both at the same time I think it's always helpful to address both at the same time because at that point I feel like for adults they really have seen the interplay between those two conditions you know they kind of reinforce each other the ADHD least to more emotional disregulation that could include mood disregulation and that mood disregulation makes the ADHD worse probably the best way forward is to treat both at the same time okay

### Revised claim review

**Claim 1:** Depression and ADHD should always be treated simultaneously

**Verdict: Unsupported.** Treatment priority is individualized; simultaneous treatment is not invariably required. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 2:** ADHD and depression can reinforce one another through impairment, stress, and emotional or mood dysregulation

**Verdict: Supported.** Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 3:** Simultaneous treatment is universally the best way forward

**Verdict: Excluded from scoring.** Repetition of the same universal simultaneous-treatment proposition, not a separate claim.

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **1**; unsupported: **1**; excluded: **1**.
- Supported-claim percentage: **1 / 2 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 191

**Title:** The "physical signs" of ADHD #adhd #neurodivergent  
**URL:** https://www.youtube.com/shorts/WeIKUm9u8EM  
**Views:** 55,186  
**Likes:** 1,753  
**Comments:** 82  
**Duration:** 24 seconds

**Transcript:**

> listen to this the physical signs of ADHD bitten fingernails queezed or bleeding face cruises everywhere poor posture shrimping dark circles messy hair and actually looks like they woke up like this all right who wrote this

### Revised claim review

The list is read humorously; scoring assumes endorsement of the supplied trait assertions, which is interpretation-sensitive.

**Claim 1:** Bitten nails, picked or bleeding facial skin, and similar body-focused repetitive behaviours are physical signs of ADHD

**Verdict: Supported.** Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/), [BFRBCO](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552165/).

**Claim 2:** Frequent bruises and poor or “shrimped” posture are physical signs of ADHD

**Verdict: Unsupported.** This stereotype is not established as an ADHD characteristic. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Dark circles, messy hair, and looking newly awakened are physical signs of ADHD

**Verdict: Unsupported.** This stereotype is not established as an ADHD characteristic. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading** — see the limitation below.
- Original Markdown label: **Label 4 — Highly misleading**.

**Decision limitation:** The supplied trait assertions are scored as stated. No humorous or sarcastic intent is inferred.

---

## Video 192

**Title:** Types of ADHD | Inattentive ADHD in Females Symptoms | #ADHD #DrRamanSakhuja  
**URL:** https://www.youtube.com/shorts/IIa4IiCKTNY  
**Views:** 202  
**Likes:** 25  
**Comments:** 0  
**Duration:** 51 seconds

**Transcript:**

> there are three kinds of ADHD the combined form where people have a combination of attention difficulties as well as hyperactivity impulsivity second one is the inattentive predominantly and the third one is that of a predominantly being hyperactive impulsive type inattentive ADHD along with emotional difficulties and emotional regulation problems is often and commonly seen in women which can can be misinterpreted or misdiagnosed as some other condition and that is one reason why there may be a delay in getting women getting diagnosed with ADHD

### Revised claim review

**Claim 1:** ADHD has combined, predominantly inattentive, and predominantly hyperactive-impulsive presentations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 2:** Inattentive presentations and associated emotional difficulties may be under-recognized in women, contributing to delayed or alternative diagnoses

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 193

**Title:** Wellbutrin for ADHD. #wellbutrin #adhd #add  
**URL:** https://www.youtube.com/shorts/dPpoQzDlQzc  
**Views:** 39,707  
**Likes:** 0  
**Comments:** 52  
**Duration:** 41 seconds

**Transcript:**

> when talking about ADHD there are two main groups the stimulant and the non-stimulant medications and non-stimulant medications are things like atomoxetine or Cera or Wellbutrin or buproprion and the National Institute of Mental Health conducted a study to look at broon or Wellbutrin in treating ADHD and adults and what they said is that it had a potential benefit for adults and the only way that you will know is if you take the medication it typically takes anywhere between 2 to 6 weeks in order to see a response but it's definitely something to consider if the stimulants don't work for you I hope that helps

### Revised claim review

Bupropion has possible off-label ADHD benefit with low-certainty evidence. The transcript’s attribution to a particular NIMH study was not independently established; the clinical propositions, not that attribution, are supported.

**Claim 1:** ADHD medicines are broadly grouped into stimulant and non-stimulant options

**Verdict: Supported.** Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Atomoxetine is an approved non-stimulant, while bupropion or Wellbutrin is sometimes used off-label for adult ADHD

**Verdict: Supported.** Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Clinical research suggests that bupropion may benefit some adults with ADHD

**Verdict: Supported.** Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Bupropion may require several weeks before its clinical response is evaluated

**Verdict: Supported.** Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** Bupropion may be considered when stimulants are ineffective, poorly tolerated, or unsuitable

**Verdict: Supported.** Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate** — see the limitation below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The clinical bupropion propositions have supporting evidence, but the specific NIMH study attribution was not established. The label does not authenticate that attribution.

---

## Video 194

**Title:** Hidden Signs of ADHD in Girls That Most People Miss!  
**URL:** https://www.youtube.com/shorts/9QxD5LsyBfM  
**Views:** 10,761  
**Likes:** 251  
**Comments:** 5  
**Duration:** 94 seconds

**Transcript:**

> here are some hidden signs of ADHD in girls ADHD often looks different in girls compared to boys making it harder to recognize one super sensitive to rejection girls with ADH often experience rejection sensitivity dysphoria which makes them deeply affected by feelings of exclusion or criticism they may overreact to perceived rejection and struggle to move past it two emotional disre ation strong emotional responses that are difficult to control are common she may experience intense sadness anger or attachment to others in situations where such reactions seem excessive three lack of motivation while often mistaken for laziness this is actually a result of executive dysfunction making it difficult to initiate and follow through with tasks four time management struggles this can manifest as chronic lateness or conversely excessive anxiety about being late leading to an obsession with punctuality and arriving too early five short-lived interests she may rapidly switch from one passion to another becoming intensely obsessed with something for a while before quickly losing interest in moving on six messiness and disorganization low motivation and executive dysfunction can lead to untiy spaces and difficulty maintaining organization

### Revised claim review

**Claim 1:** ADHD may be less conspicuous in girls and therefore missed more often

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** Rejection-sensitive dysphoria is a hidden sign of ADHD in girls

**Verdict: Supported.** Rejection distress is associated, not a female-specific diagnostic criterion. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** Strong emotional reactions and emotion-regulation difficulty can accompany ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** Executive dysfunction can be mistaken for laziness when it interferes with task initiation and follow-through

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 5:** ADHD can cause chronic lateness, poor time management, or compensatory anxiety about punctuality

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 6:** Rapidly changing intense interests can occur in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 7:** Executive dysfunction can contribute to messiness and difficulty maintaining organization

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **7**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **7 / 7 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 195

**Title:** What do we know about #migraine and #adhd symptoms?  
**URL:** https://www.youtube.com/shorts/BHKuySElH1U  
**Views:** 4,440  
**Likes:** 118  
**Comments:** 1  
**Duration:** 48 seconds

**Transcript:**

> research shows that people with ADHD have a higher prevalence of migraine we know that ADHD and migraine are comorbid and some symptoms of a migraine attack look a lot like ADHD symptoms think inability to focus and restlessness but what do we know about people living with migraine and their ADHD symptoms in a new study published in the Journal of attention disorders shows that adult adults with episodic migraine may have a higher prevalence of ADHD and impulsivity symptoms the study authors said that more research on the relationship between migraine and ADHD can help us understand the causes and connections

### Revised claim review

**Claim 1:** Migraine occurs at a higher rate among people with ADHD

**Verdict: Supported.** Evidence: [MIGRAINE](https://pubmed.ncbi.nlm.nih.gov/37752867/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Migraine attacks can temporarily cause concentration difficulty and agitation or restlessness that resemble ADHD-related problems

**Verdict: Supported.** Evidence: [MIGRAINE](https://pubmed.ncbi.nlm.nih.gov/37752867/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Adults with episodic migraine may show elevated ADHD and impulsivity symptoms

**Verdict: Supported.** Evidence: [MIGRAINE](https://pubmed.ncbi.nlm.nih.gov/37752867/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Further research is needed to determine mechanisms and direction of the association

**Verdict: Supported.** Evidence: [MIGRAINE](https://pubmed.ncbi.nlm.nih.gov/37752867/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 196

**Title:** The Most Common ADHD Symptoms in Women  
**URL:** https://www.youtube.com/shorts/9JJx27vLtx0  
**Views:** 1,746  
**Likes:** 86  
**Comments:** 5  
**Duration:** 53 seconds

**Transcript:**

> hi I'm Dr Lisa Batten I'm a therapist and clinical researcher and I'm here to talk about some of the most common symptoms of ADHD in women number one organized chaos so because organization is such a difficult thing for people with ADHD you often develop coping mechanisms which often looks like baskets or stations where things live it works for you but to the outside eye it can look like chaos number two you take on too much as a go-getter with superpowers you hold yourself to unrealistic standards which can lead to putting way too much on your plate number three decisions are easy and impossible you're either all in without thinking or you're researching every single option and outcome possible and feeling Frozen by indecision number four emotional rollercoaster so you might find that you power through one emotionally devastating event with ease but some minor setback can send you absolutely spiraling

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

Superpowers is rhetorical; the specific content describes possible compensatory overcommitment and hidden difficulty, not established superior ability.

**Claim 1:** Women with ADHD may develop unconventional organizational systems that appear chaotic to others but function as compensation

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** Women with ADHD commonly take on too much because they are go-getters with superpowers and unrealistic standards

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** ADHD can involve both impulsive decisions and prolonged indecision caused by overwhelm

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** Emotional reactions in ADHD may be inconsistent, with some major stressors managed well and minor setbacks producing intense distress

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 197

**Title:** Do I have OCD or ADHD or Both?  
**URL:** https://www.youtube.com/shorts/dW1IrviIBIE  
**Views:** 34,041  
**Likes:** 994  
**Comments:** 0  
**Duration:** 60 seconds

**Transcript:**

> did you know that OCD is sometimes misdiagnosed as ADHD October is ADHD awareness month and I'd like to share some information with you about the similarities and differences between OCD and ADHD both disorders can include problems with concentration sleep time management emotional disregulation and sensory issues however they have several distinct features as well ADHD may include inattention hyperactivity forgetfulness impulsivity or hyper Focus people may use the word obsessed to describe their hyperfixation such as my child is obsessed with trains or I'm obsessed with this new TV show on the other hand obsessions in OCD are unwanted and upsetting which creates anxiety and distress that drives the individual to perform compulsions in some cases individuals may have both OCD and ADHD an in-depth assessment can help clients and their families receive an accurate diagnosis and effective treatment

### Revised claim review

**Claim 1:** OCD and ADHD can be confused because both may involve concentration, sleep, time-management, emotional, or sensory difficulties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 2:** ADHD can include inattention, hyperactivity, forgetfulness, impulsivity, and intense task absorption

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 3:** An ADHD interest described casually as an “obsession” differs from an OCD obsession

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 4:** OCD compulsions are performed in response to distressing obsessions or rigid rules to reduce anxiety or prevent feared outcomes

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

**Claim 5:** OCD and ADHD can co-occur, and detailed assessment is needed to distinguish or diagnose them

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [OCD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 198

**Title:** Understanding Hyperactivity in Children: ASD vs ADHD | Dr. Atul Madaan -Autism Expert  
**URL:** https://www.youtube.com/shorts/jH9oMOMQbUM  
**Views:** 45,219  
**Likes:** 687  
**Comments:** 1  
**Duration:** 68 seconds

**Transcript:**

So, one of the most common problems in our children is hyperactivity. They can't stay calm. They have more energy than necessary. They keep running around and can't be held. So, when we talk about things like this, we call it hyperactivity. Let's understand this a little bit. Whenever I say this, you often tell me in the outpatient department that they become hyperactive. So, that hyperactivity means you people say hyperactivity to someone who gets angry. I'm not talking about hyperactivity. Hyperactivity means they have more energy than necessary. We can't handle it . First, we'll understand it on two levels: autism and ADHD. So, it 's very important for a parent to have clarity about what this hyperactivity is. Is it ADHD or autism? Many people get confused . So, we need to understand whether hyperactivity is relative to autism or ADHD . There's only one way to address it. But it's still important to understand the difference between autism and ADHD .

### Revised claim review

First review of the author-supplied English replacement, 9 September 2026. The supplied 'There's only one way to address it' is retained as the reviewed proposition; the old annotation's stronger 'exactly the same way' wording is not substituted. Repeated explanations of hyperactivity are counted once.

**Claim 1 — revised extraction:** Hyperactivity means excessive activity or difficulty remaining still, not simply becoming angry.

*Original annotation wording:* Hyperactivity refers to excessive or developmentally inappropriate motor activity and difficulty remaining still, not simply anger

**Verdict: Supported.** This distinguishes motor activity from anger; excess energy is a colloquial description, not a measured physiological energy surplus. Evidence: [APA](https://www.psychiatry.org/patients-families/adhd/what-is-adhd).

**Claim 2 — revised extraction:** Hyperactivity may be encountered in children with ADHD and in autistic children.

*Original annotation wording:* Hyperactivity can occur in ADHD and in some autistic children, particularly when ADHD co-occurs

**Verdict: Supported.** These diagnoses can coexist. Hyperactivity is not a core autism criterion, and not every autistic child has ADHD. Evidence: [UPD_ASD_GUIDE](https://link.springer.com/article/10.1186/s12916-020-01585-y).

**Claim 3 — revised extraction:** There is only one way to address the hyperactivity being discussed in autism and ADHD.

*Original annotation wording:* Hyperactivity should be addressed in exactly the same way whether it arises with autism or ADHD

**Verdict: Unsupported.** Support depends on the child's needs and circumstances. Some medication choices overlap when ADHD co-occurs with autism, but that is not one universal treatment; monitoring and broader support can differ. Evidence: [UPD_ASD_GUIDE](https://link.springer.com/article/10.1186/s12916-020-01585-y), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4 — revised extraction:** Assessing autism-related needs and ADHD is important when evaluating a child's hyperactivity.

*Original annotation wording:* Distinguishing autism-related needs from ADHD-related hyperactivity is clinically important

**Verdict: Supported.** A comprehensive assessment can distinguish overlapping behaviors and identify co-occurrence. This is not an either/or test based on hyperactivity alone. Evidence: [UPD_ASD_GUIDE](https://link.springer.com/article/10.1186/s12916-020-01585-y).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the interpretation note below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** Claim 3 is unsupported under the literal one-treatment-route reading. If 'one way' was intended only to mean that both situations need assessment and support, that narrower statement is compatible with guidance and would yield Label 1 (4/4). The transcript does not identify a particular intervention, so its intended meaning is not established here.

---

## Video 199

**Title:** Why I quit taking ADHD medications. Full video @dr.natenoble on YouTube.  #adhd #whyiquit  
**URL:** https://www.youtube.com/shorts/_ndJ-JwvWd4  
**Views:** 92,943  
**Likes:** 797  
**Comments:** 96  
**Duration:** 50 seconds

**Transcript:**

> I started out on Ritalin and then I went to Concerta and then I transitioned to Adderall and then I went to Vyvanse and I don't think I was on any other medicines but that's a pretty good mystery tour of medicines to get a sense for how they work and I stayed on these medicines for several years until I was running a clinic on my own and decided that it was time to quit these are the six reasons why I quit reason number one I'm gonna put a photo up here and I want you to look at this this is a photo of me right after I started the developmental clinic in the city of Des Moines where I still work and I was on as you can see in this photo I was definitely on uh Ritalin at that time and I can tell by looking at myself because that was me 30 pounds ago this me that you see in front of the camera could have eaten that me for breakfast

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

No eligible generalized ADHD claim in the supplied fragment; remains unlabelled.

No eligible generalized ADHD claims were identified in the supplied text.

### Revised result

- Eligible fact-checkable claims: **0**
- Supported: **0**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **not defined** (no eligible claims).
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Unlabelled**.

---

## Video 200

**Title:** Dr. Russell Barkley on ADHD Masking  
**URL:** https://www.youtube.com/shorts/0l51DhnoyPg  
**Views:** 86,647  
**Likes:** 5,143  
**Comments:** 196  
**Duration:** 57 seconds

**Transcript:**

> the brighter people struggle with the disorder longer they're not beli nobody can think that they got as far as they did and have ADHD uh and therefore it's dismissed or trivialized or just go to Starbucks and get a coffee or get a good night sleep take a little omega-3 six oil you know just do something trivial none of which by the way works but the the issue here then is they will eventually crash uh it just takes longer for that crash to happen uh it might be College where we find that uh only about 10% of people with ADHD can complete a college program versus 40% of the population and it has nothing to do with Brilliance intelligence or knowledge it's the demands that college makes on Executive functioning and self-regulation are enormous and unless they um get special help at College they're usually out within one to two semesters they just can't handle the the demands

### Revised claim review

**Claim 1:** High intelligence can allow a person to compensate for ADHD longer and contribute to delayed recognition or dismissal

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 2:** Coffee, adequate sleep, or omega-3 supplementation never helps ADHD-related functioning

**Verdict: Unsupported.** Never helps is too categorical, particularly for adequate sleep; this does not establish omega-3 efficacy. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/), [CAFF](https://www.mdpi.com/2076-3425/13/9/1304), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 3:** Every bright person with ADHD will eventually “crash”

**Verdict: Unsupported.** An eventual crash is not inevitable for everyone. Evidence: [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** Only about 10% of people with ADHD complete college compared with 40% of the general population

**Verdict: Unsupported.** The exact 10% versus 40% comparison is not substantiated for the stated population. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/).

**Claim 5:** Students with ADHD usually leave college within one or two semesters unless they receive special help

**Verdict: Unsupported.** The usual first/second-semester dropout assertion is not substantiated. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **1**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **1 / 5 × 100 = 20.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 201

**Title:** Signs of ADHD in women that no one ever talks about #shorts #ADHD  
**URL:** https://www.youtube.com/shorts/zEi73dGcpfA  
**Views:** 58,747  
**Likes:** 3,313  
**Comments:** 69  
**Duration:** 45 seconds

**Transcript:**

> eight signs of ADHD in women that no one ever talks about so let's talk about them you have an intense fear of letting others down or saying no no matter what you do you don't feel good enough you struggle to verbalize your own feelings and opinions sometimes you overshare or put your foot in your mouth you feel misunderstood but you long for connection you got good grades in school but you don't remember anything you learned you feel like you may have missed out on your passion and Colleen because so much of your energy has been hiding your struggles you have so many dreams and possibilities but you don't know where to start you're not crazy you're not too much you're not a hot mess you're not a drama queen and you're not alone

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

Applied the same associated-feature standard as Videos 21 and 90; no listed experience alone establishes ADHD.

**Claim 1:** Intense fear of disappointing others, inability to say no, and never feeling good enough are signs of ADHD in women

**Verdict: Supported.** Interpreted as possible associated self-esteem/rejection difficulties, not diagnostic or uniquely female signs. Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 2:** Difficulty verbalizing feelings and opinions is a sign of ADHD in women

**Verdict: Supported.** Emotion-expression difficulty can accompany ADHD; the small study does not establish a female-specific identifier. Evidence: [ALEX](https://pubmed.ncbi.nlm.nih.gov/20952350/).

**Claim 3:** Oversharing or speaking impulsively can occur in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 4:** Feeling misunderstood while longing for connection is a sign of ADHD in women

**Verdict: Supported.** Feeling misunderstood and wanting connection are documented associated experiences, not diagnostic tests. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full).

**Claim 5:** Good school grades followed by poor recall of everything learned is a sign of ADHD

**Verdict: Unsupported.** Good grades do not establish inability to retain everything learned. Evidence: [MEM](https://pubmed.ncbi.nlm.nih.gov/24232170/).

**Claim 6:** Women may expend substantial energy concealing or compensating for ADHD difficulties

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/).

**Claim 7:** Having many plans but difficulty deciding where to begin can reflect ADHD-related task-initiation and prioritization difficulty

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **7**
- Supported: **6**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **6 / 7 × 100 = 85.71%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 202

**Title:** How does ADHD affect relationships? | Experts answer  
**URL:** https://www.youtube.com/shorts/uh_Znj8LCkk  
**Views:** 125,352  
**Likes:** 2,777  
**Comments:** 56  
**Duration:** 35 seconds

**Transcript:**

> How does ADHD affect relationships? ADHD affects all relationships. Friendships, romantic relationships, family relationships, colleagues, it affects them all. The ways in which it affects relationships is it impacts communication, impulsivity, executive functioning, poor boundary setting, and just plain getting bored and leaving relationships. But on a high note, people with ADHD are also wonderful people to have in relationships. They can be fun and fun-loving and engaging and really wonderful to be with. So my advice is, if you have ADHD, you just need to be thoughtful and intentional and really willing to stick it out and communicate with your partner.

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** ADHD affects all relationships, including friendships, romantic relationships, family and colleagues.

*Original annotation wording:* ADHD affects every friendship, romantic relationship, family relationship, and workplace relationship

**Verdict: Unsupported.** ADHD can impair relationships, but impairment criteria do not require an effect on every relationship. All is retained rather than replaced with can. Evidence: [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Inattention, impulsivity, communication difficulty, and executive dysfunction can create relationship problems

**Verdict: Supported.** Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** ADHD commonly causes poor boundaries, boredom with partners, and abandonment of relationships

**Verdict: Unsupported.** This common boundary/boredom/abandonment profile is not established. Evidence: [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [IMPACT](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1/3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Previous reviewed label: **Label 2**.
- Uploaded CSV label: **Label 3**.

---

## Video 203

**Title:** Is it ADHD or Sleep Apnea? | Sleep Apnea Symptoms | Psychiatrist in Cardiff | Dr. Raman Sakhuja  
**URL:** https://www.youtube.com/shorts/TcRGf7fj3FQ  
**Views:** 411  
**Likes:** 11  
**Comments:** 1  
**Duration:** 60 seconds

**Transcript:**

> just coming out of Clinic after seeing someone who came to see me for possibility of an ADHD but on exploring had a lifelong history of as sleep difficulty with a lot of snoring with a lot of gasping at night this fragmented sleep which suggests that this gentleman might be having a sleep disorder particularly a sleep disorder breathing difficulty which can lead to problems with attention and concentration memory difficulties emotional difficulties and may look like ADHD but the assessments for Sleep Disorders is very important when talking about looking at neurocognitive syndromes such as adht or any other problems so if any of you or your family members are suffering with a chronic sleep difficulty please go and see a qualified professional who can help you to understand investigate and manage

### Revised claim review

**Claim 1:** Lifelong snoring, gasping during sleep, and fragmented sleep suggest possible sleep-disordered breathing such as obstructive sleep apnoea

**Verdict: Supported.** Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/), [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 2:** Sleep-disordered breathing can cause attention, concentration, memory, and emotional difficulties that resemble or worsen ADHD symptoms

**Verdict: Supported.** Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/), [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 3:** Sleep disorders should be considered during assessment of ADHD-like symptoms

**Verdict: Supported.** Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/), [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 4:** Chronic sleep difficulty should be assessed by a qualified professional

**Verdict: Supported.** Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/), [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 204

**Title:** ADHD and Autism: Causes and Connection  
**URL:** https://www.youtube.com/shorts/Z8Qjvjr9qVs  
**Views:** 331,664  
**Likes:** 14,469  
**Comments:** 379  
**Duration:** 49 seconds

**Transcript:**

> ADHD and autism are neurodevelopmental disorders means that they start early in childhood and affect how your brain grows and functions examples of neurodevelopmental disorders include ADHD autism spectrum disorder or ASD intellectual developmental disorder and learning disorders it is common if you have one to have another one in fact there's a high prevalence of people with Autism Spectrum who also have ADHD the reverse is not as common for people with ADH D to also have ASD but people with ADHD can have features of autism spectrum without having the complete disorder both disorders are highly genetic meaning the genes from them are passed down through [Music] families

### Revised claim review

**Claim 1:** ADHD and autism are neurodevelopmental disorders beginning in the developmental period and affecting brain and behavioural functioning

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Intellectual developmental disorder and specific learning disorders are also neurodevelopmental disorders

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Autism and ADHD frequently co-occur, and ADHD is more common among autistic people than autism is among people with ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** People with ADHD may show autistic traits without meeting full autism diagnostic criteria

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 5:** Both ADHD and autism are highly heritable and aggregate in families

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **5**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **5 / 5 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 205

**Title:** What is ADHD rage? | Experts answer  
**URL:** https://www.youtube.com/shorts/WTuBT-hRoDI  
**Views:** 222,271  
**Likes:** 9,298  
**Comments:** 206  
**Duration:** 54 seconds

**Transcript:**

> people with ADHD they often feel their feelings more strongly if you're excited and you're happy you are a lot of fun to be around and people are going to love it but if you're irritated you're annoyed you're angry that can have a big impact on relationships it's not just that your anger May Spike quickly also those strong feelings can kind of drop off quickly which can also be confusing for family or romantic Partners who have not yet moved on as quickly as perhaps you have part of this is also just generally managing your stress level the more you feel like your life is chaotic and overwhelming the more of a hair trigger you're going to have the stronger your emotional reactions are going to be so there's also that way that ADHD leads to these big Angry rageful reactions

### Revised claim review

**Claim 1:** Some people with ADHD experience emotions more intensely or have difficulty regulating them

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Anger in ADHD may rise and subside rapidly, creating relationship difficulty when others have not recovered at the same rate

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Greater stress, chaos, and overwhelm can lower emotional tolerance and intensify reactions

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** ADHD can contribute to large angry reactions

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 206

**Title:** 3 Common But NOT Normal Symptoms: ADHD  
**URL:** https://www.youtube.com/shorts/vYZSl3_h6Jc  
**Views:** 2,345  
**Likes:** 150  
**Comments:** 8  
**Duration:** 46 seconds

**Transcript:**

> Three common symptoms that are not normal in ADHD. Number one is waking up between two to 3:00 a.m. This is something that I commonly see in many ADHD patients and is usually attributed to dysregulations in cortisol and or blood sugar. Number two is GI issues like upset stomach, constipation, diarrhea, or bloating. This can be the consequence of multiple factors, but one of the most common ones is the anxiety that typically goes along with ADHD, which can disrupt gut function. And number three is missing meals followed up by binge eating. This is something that's very common in those with ADHD and can have a negative impact on blood sugar and cortisol like I mentioned in point one and also in gut health issues like I mentioned in point two. Have you experienced these issues? Let me know in the comments.

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** Waking specifically between 2 and 3 a.m. is a common ADHD symptom caused by cortisol or blood-sugar dysregulation

**Verdict: Unsupported.** The specific waking time and cortisol/glucose explanation are not established. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 2:** Upset stomach, constipation, diarrhoea, and bloating are common ADHD symptoms usually caused by associated anxiety

**Verdict: Unsupported.** The proposed usual anxiety cause of these gut complaints is not established. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 3:** Missing meals followed by binge eating occurs more often among people with ADHD

**Verdict: Supported.** Evidence: [EATING](https://pubmed.ncbi.nlm.nih.gov/27859581/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 4:** This eating pattern explains cortisol dysregulation, the specific 2–3 a.m. waking, and the listed gut problems

**Verdict: Unsupported.** This causal chain from eating to cortisol, waking and gut problems is not established. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/), [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **1**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **1 / 4 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 207

**Title:** What are good sources of iron to help with ADHD symptoms? #adhd #adhders #adhdmoms #irondeficiency  
**URL:** https://www.youtube.com/shorts/975TFf-klP0  
**Views:** 805  
**Likes:** 21  
**Comments:** 0  
**Duration:** 25 seconds

**Transcript:**

> on our last video we talked about how iron deficiency is highly correlated with ADHD symptoms so what are some good source of iron it's safest to increase iron level through food choices for thein supplements some of iron rich foods include meat poultry and fish eggs banana and peas are also a good source of iron as well by the way you can increase iron absorption by serving these foods with those highend vitamin C such as orange or grapefruit juice

### Revised claim review

**Claim 1:** Lower iron or ferritin status has been associated with ADHD symptoms in some studies

**Verdict: Supported.** Association, not proof that every child with ADHD is iron deficient. Evidence: [FERRITIN](https://www.nature.com/articles/s41598-017-19096-x).

**Claim 2:** Increasing dietary iron is generally safer than self-starting iron supplements

**Verdict: Supported.** Evidence: [IRON](https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/).

**Claim 3:** Meat, poultry, fish, eggs, peas, and bananas are all comparably good iron sources

**Verdict: Unsupported.** Bananas are not a rich source of iron. Evidence: [IRON](https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/).

**Claim 4:** Vitamin C consumed with non-haem plant iron can improve absorption

**Verdict: Supported.** Evidence: [IRON](https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 208

**Title:** Treating ADHD  
**URL:** https://www.youtube.com/shorts/0LN2gKiYFOc  
**Views:** 4,722  
**Likes:** 148  
**Comments:** 1  
**Duration:** 37 seconds

**Transcript:**

> so ADHD is one of the conditions that for us is relatively easy to make a big difference fast now I'm not saying that treating ADHD is always easy that's not the case but we have highly effective and excellent treatments for ADHD and people can make big turnarounds between appointments they can go from failing to coming back the next appointment getting all a now there are other conditions in Psychiatry where we see huge turnarounds but a lot of the time it takes a little bit more time and that's why treating ADHD is one of the psychiatrist favorite conditions to treat because it does give us a little bit of immediate gratification when we make a correct diagnosis and someone responds really well

### Revised claim review

Only one generalized eligible claim remains after excluding the personal case outcome.

**Claim 1:** ADHD has highly effective treatments and some patients show substantial improvement relatively quickly after correct diagnosis and treatment

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** A student may move from failing performance to excellent grades between appointments after responding to ADHD treatment

**Verdict: Excluded from scoring.** The improvement from failing grades to As is an individual clinical anecdote, not a population effect estimate.

### Revised result

- Eligible fact-checkable claims: **1**
- Supported: **1**; unsupported: **0**; excluded: **1**.
- Supported-claim percentage: **1 / 1 × 100 = 100.00%**.
- **Reviewed label: Unlabelled** — fewer than two eligible claims.
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 209

**Title:** What is the best physical exercise to manage ADHD symptoms? #adhd #exercise #adhdcoach  
**URL:** https://www.youtube.com/shorts/FWBTslNBfhE  
**Views:** 1,426  
**Likes:** 91  
**Comments:** 8  
**Duration:** 53 seconds

**Transcript:**

> hi I'm ADHD Coach Jeff copper here with two pennies for a copper minute I often get asked is exercise helpful for people with ADHD absolutely if we could put it in a pill it would be the ADHD drug of the century next question what types of exercise should I do that's a real simple answer the ones you will do there's a lot of people out there who prescribe certain amount of exercise and if they make that prescription and you don't do it and it's not doing you any good what I find is it's easier to say do what you will do if you'll walk around the house three times and you do it that's better than thinking you got to do 45 minutes of cardio three times a week so I would encourage you to focus on what you will actually do not what you think you should do U because in the end I think you'll get better results with that hope you enjoyed that Insight take care

### Revised claim review

Drug of the century is rhetorical advocacy for exercise, not a literal drug classification or quantified trial claim.

**Claim 1:** Physical exercise is helpful for people with ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 2:** The most useful exercise plan is one the person can and will perform consistently

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

**Claim 3:** A small completed amount of activity is more beneficial than an ambitious prescription that is never performed

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 210

**Title:** How ADHD Is Diagnosed: Key Symptoms & Overlaps with Autism | Child Behavior Insights  
**URL:** https://www.youtube.com/shorts/P3txKqeXpFQ  
**Views:** 230  
**Likes:** 2  
**Comments:** 0  
**Duration:** 60 seconds

**Status:** # tactiq.io free youtube transcript
# How ADHD Is Diagnosed: Key Symptoms & Overlaps with Autism | Child Behavior Insights
# https://www.youtube.com/watch/P3txKqeXpFQ

00:00:00.160 Say for example if you're seeing a child
00:00:02.000 persistently in school usually we say
00:00:04.319 ADHD is not diagnosed before six years
00:00:06.160 old it's not sure so we prefer that's
00:00:08.639 what it's psychiatric you know
00:00:10.000 association or manual they use
00:00:11.599 guidelines every psychiatrist in the
00:00:13.280 world they use the same thing it's DSMY
00:00:15.360 that's one of the diagnos we use for
00:00:17.279 ADHD so they the treatment is to be
00:00:20.400 started from the age of uh 6 years old
00:00:23.039 you can't start a medication but you can
00:00:24.800 get diagnosed before that but you will
00:00:26.720 see because they're overlapped these are
00:00:28.320 all neurodedevelopment conditions it's
00:00:29.960 autism that is a like you know like ADHD
00:00:33.200 that are over overlapped. Sure. So we
00:00:34.960 see a lot of kids who are autistic also
00:00:37.120 has a ADHD so you pick up on those
00:00:39.680 things how they are behaving how
00:00:41.600 consistent they are. So it's like say
00:00:43.360 for example if a child at home is
00:00:45.600 showing that some of the symptoms but in
00:00:47.280 school is fine he's able to concentrate
00:00:48.800 then that's not ADHD there's something
00:00:50.399 else going on. So it that's the reason
00:00:52.160 why it says the consistent patterns we
00:00:53.760 need to see in two or three uh
00:00:55.920 situations not just in one home or just
00:00:58.879 one in

### Revised claim review

**Claim 1:** ADHD is generally not diagnosed before age six

**Verdict: Unsupported.** ADHD can be assessed and diagnosed before age six. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 2:** Every psychiatrist worldwide uses the DSM to diagnose ADHD

**Verdict: Unsupported.** DSM is not the only diagnostic classification used worldwide. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** ADHD treatment begins at six, and medication cannot be used before that age

**Verdict: Unsupported.** Behavioural treatment and, in selected cases, medication can be used before age six. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 4:** ADHD and autism are overlapping neurodevelopmental conditions and can coexist

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 5:** Symptoms appearing only at home, while the child functions normally at school, ordinarily do not satisfy ADHD’s cross-situational requirement

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 6:** Diagnosis requires a persistent pattern across at least two settings rather than behaviour observed in only one situation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **3**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **3 / 6 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 211

**Title:** Why are people complaining about this ADHD treatment? #adhd #adhdexplained #fy #fyp  
**URL:** https://www.youtube.com/shorts/CEfFK582tyQ  
**Views:** 168  
**Likes:** 7  
**Comments:** 1  
**Duration:** 38 seconds

**Transcript:**

> so let's talk about vians the reason why it's not as effective as it used to be for so many patients is because it recently went generic whenever a medication goes generic they can use the same active ingredient but they have to use different inactive ingredients like a different formulary to make the medication imagine if you went to the store and you grabbed three different sticks of butter and then you came back home and you put them in the pot each one would cook differently melt differently and taste differently that's because each one's made a little bit differently but each one's sold and marketed as butter the same exact thing happens with our medications whenever getting a different generic manufacturer they're making the medication a little bit differently and that can have a impact on how effective a certain medication is

### Revised claim review

**Claim 1:** Vyvanse has become less effective for many patients because generic versions became available

**Verdict: Unsupported.** Generic availability does not establish widespread loss of efficacy. Evidence: [GENERIC](https://www.fda.gov/drugs/generic-drugs/generic-drugs-questions-answers).

**Claim 2 — clarified extraction:** Generic medicines have the same active ingredient, but their inactive ingredients have to be different.

*Original annotation wording:* Generic medicines contain the same active ingredient but may use different inactive ingredients

**Verdict: Unsupported.** The transcript says inactive ingredients have to differ; permitted differences are not mandatory. Evidence: [GENERIC](https://www.fda.gov/drugs/generic-drugs/generic-drugs-questions-answers).

**Claim 3:** Differences among manufacturers can affect tolerability or perceived response for some individuals

**Verdict: Supported.** Evidence: [GENERIC](https://www.fda.gov/drugs/generic-drugs/generic-drugs-questions-answers).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 212

**Title:** Treating ADHD with Prescription Stimulants lowers Substance Use Disorder #ADHD #drugaddiction  
**URL:** https://www.youtube.com/shorts/X_gFpeQKqP8  
**Views:** 188  
**Likes:** 7  
**Comments:** 0  
**Duration:** 44 seconds

**Transcript:**

> I've worked in the jails. I've worked in the streets of Los Angeles, Skid Row. There are people with stimulant abuse disorders. And that's for street drugs for meth for things that are getting them really high. And that's not what you can do with our medications. So, in general, I think there's all of that. And that's even before I tell you that treating ADHD with stimulants decreases the incidence of substance use disorders overall. That's the critical component here. So, when you treat people's core symptoms of their issues, they have less need of going out and using other substances to to self-medicate and they do better overall. That's how I look at

### Revised claim review

**Claim 1:** Prescription stimulant medication cannot be used to become intoxicated in the way illicit stimulants can

**Verdict: Unsupported.** Prescribed stimulants can still cause intoxication or be misused; prescription status does not remove that risk. Evidence: [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions), [DEA](https://www.dea.gov/factsheets/stimulants).

**Claim 2:** Treating ADHD with prescribed stimulants is associated with a lower later risk of substance-use disorders rather than a higher risk

**Verdict: Supported.** An observational association, not a guarantee for an individual. Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

**Claim 3:** The reduction occurs because treatment removes the need to self-medicate with other substances

**Verdict: Unsupported.** The proposed self-medication mechanism is not proved by the association. Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 213

**Title:** Is ADHD medication safe? | Experts answer  
**URL:** https://www.youtube.com/shorts/orSIeHcWXNo  
**Views:** 80,695  
**Likes:** 1,944  
**Comments:** 73  
**Duration:** 35 seconds

**Status:** # tactiq.io free youtube transcript
# Is ADHD medication safe? | Experts answer
# https://www.youtube.com/watch/orSIeHcWXNo

00:00:00.080 is ADHD medication safe so there are
00:00:02.720 hundreds and hundreds of studies that
00:00:04.759 have shown over decades that ADHD
00:00:07.560 medication is both generally safe and
00:00:10.320 also pretty effective it's important to
00:00:12.679 get an accurate diagnosis by a trusted
00:00:15.480 professional if they appropriately
00:00:18.279 prescribe the medication if you take it
00:00:20.880 as it has been prescribed when you put
00:00:22.960 it all together ADH medication can
00:00:25.599 actually improve safety outcomes by
00:00:28.320 helping with impulsivity and
00:00:30.199 distractability and to just make you
00:00:32.479 more aware of the world around you

### Revised claim review

**Claim 1:** Decades of research show that ADHD medications are generally effective and reasonably safe

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 2:** An accurate ADHD diagnosis by a qualified professional is important before medication is prescribed

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 3:** Medication safety depends partly on appropriate prescribing and taking the medicine as directed

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 4:** ADHD medication can improve safety-related outcomes by reducing impulsivity and distractibility

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 214

**Title:** How Gluten and Dairy Sensitivity Can Impact ADHD Symptoms  
**URL:** https://www.youtube.com/shorts/6UdfD37QK0c  
**Views:** 1,811  
**Likes:** 42  
**Comments:** 9  
**Duration:** 83 seconds

**Transcript:**

> Did you know that food sensitivities could be triggering ADHD symptoms? In my experience, the majority of my ADHD patients have issues with gluten or dairy. Let me explain why this matters. When your body reacts to proteins like gluten and wheat or casein and dairy, it can trigger inflammation and disrupt the gut lining. This impacts the gut brain axis, a critical communication pathway influencing neurotransmitters like dopamine and serotonin, both essential for focus, mood, and behavior. However, the gut is incredibly complex. Food sensitivity testing provides valuable insights, but it's only one part of understanding how the gut impacts ADHD symptoms. Factors like microbiome imbalances, chronic stress, and overall diet also play a major role in shaping gut health and its effect on the brain. For many of my patients, identifying food sensitivities is an essential first step. When combined with a holistic approach to gut health, it can lead to life-changing improvements in ADHD symptoms. Food sensitivity testing is a great starting point for uncovering hidden triggers, but managing ADHD naturally involves addressing the entire gut brain connection. If you're interested in testing yourself or your child for food sensitivities and starting your journey toward better gut health, comment sensitivity below to get started.

### Revised claim review

**Claim 1:** Food sensitivities trigger ADHD symptoms, and most ADHD patients have problems with gluten or dairy

**Verdict: Unsupported.** The general gluten/dairy prevalence and trigger claim is unsupported. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/).

**Claim 2:** Gluten or casein reactions disrupt the gut lining and thereby alter dopamine and serotonin enough to cause focus, mood, and behaviour problems in ADHD

**Verdict: Unsupported.** The proposed gut-to-transmitter mechanism is not established. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 3:** Commercial food-sensitivity testing provides valuable diagnostic insight into ADHD triggers

**Verdict: Unsupported.** IgG-style panels do not validate the proposed ADHD food triggers. Evidence: [IGG](https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/igg-food-test).

**Claim 4:** The microbiome, chronic stress, and overall diet can influence gut health and communicate with the brain

**Verdict: Supported.** Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/).

**Claim 5:** Identifying food sensitivities and treating the gut commonly produces life-changing ADHD improvement

**Verdict: Unsupported.** A common life-changing treatment effect is not established. Evidence: [GUT](https://pubmed.ncbi.nlm.nih.gov/33593384/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **1**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **1 / 5 × 100 = 20.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 215

**Title:** 9 symptoms ADHD and Trauma Share Difficulty concentrating  
**URL:** https://www.youtube.com/shorts/1MGzuVuZ-HM  
**Views:** 810  
**Likes:** 41  
**Comments:** 2  
**Duration:** 26 seconds

**Transcript:**

> [Music] nine symptoms ADHD and Trauma share difficulty concentrating poor memory emotional disregulation interactive sleep impulsivity and or restlessness problems connecting with others substance abuse agitation and irritability poor self-esteem if you have hit one or all of these symptoms hit the plus sign to find out how to tell the difference between ADHD and Trauma and talk to your doctor today

**Transcription note:** The first attempt returned no transcript; the single retry succeeded.

### Revised claim review

**Claim 1:** ADHD and trauma-related conditions can both involve concentration and memory difficulties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 2:** Both can involve emotional dysregulation, sleep disturbance, impulsivity or restlessness, agitation, irritability, and low self-esteem

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 3:** Both can be associated with relationship difficulty and substance-use problems

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

**Claim 4:** A clinician should distinguish trauma-related symptoms from ADHD rather than diagnosing from the overlap list

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ACE](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 216

**Title:** How Aerobic Exercise Fixes ADHD Symptoms #ADHD #Exercise #BrainHealth  
**URL:** https://www.youtube.com/shorts/EdOBTCJHs2c  
**Views:** 456  
**Likes:** 22  
**Comments:** 1  
**Duration:** 171 seconds

**Transcript:**

> If you have ADHD, while any movement is good, what if the type of exercise you choose could work even harder for your brain? As a health and rehabilitation psychologist, I'm going to show you the science of strategic movement and how it can fundamentally change the way you manage your ADHD. So, if you want to light up these key brain areas, what's the best way to do it? That's the question we're trying to answer. It's not about moving only. It's about moving with intention. So, let me say that one more time. It's not about just moving or any exercise, but it's about moving with intention. So, first up, let's talk about cognitively engaging exercises like racket sports. Studies have shown sports like tennis, badmington, or table tennis are incredibly powerful because they force you to track a ball. Okay, think about this. predict moves and coordinate your entire body in split second. So from a neurobiological standpoint, the more complex the movements, the more complex the synaptic connections your brain builds. These stronger, more efficient brain networks are then recruited to help you think and learn, improving your processing speed and focus long after your practice is over or the game is over. Next, we have classic aerobic activity. running, cycling, swimming provide an immediate boost in your ability to focus and manage impulses. Often times, some of these exercises need to be done for a longer period of time. So, this happens because aerobic activity reliably boosts dopamine and norepinephrine, particularly in the prefrontal cortex, which is your brain's hub for executive function. But it goes deeper. Exercise doesn't just give you more dopamine. It improves your brain's ability to use it by enhancing receptor sensitivity. I know that's a a lot of scientific terminology here. Let me break it down for a second. So, think of it like upgrading not just the keys, but the locks they fit into. So, the keys are the neurotransmitters like dopamine, norepinephrine, and the locks are basically the receptors on the cell. Okay? So when one neuron releases or increases the dopamine synthesis and secretion and dopamine travels to the next cell, it binds to those locks that we call receptor. So the sensitivity of the receptors get better. You're actively building a stronger, more resilient brain. Now I want to hear from you. What kind of movement or exercise has been a game changer for your ADHD? Share your experiences in the comments. Your story might just be the spark someone else needs to get started. And if you're into more science-based strategies for your ADHD, make sure to subscribe or follow us for more scientific based knowledge and interventions that may help your mental health as well as your physical health hopefully. Thanks guys.

### Revised claim review

**Claim 1:** Cognitively engaging exercise such as racket sports may provide executive and attention benefits for ADHD

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** More complex movement directly builds more complex synaptic connections that are later recruited to improve processing speed and focus

**Verdict: Unsupported.** Clinical exercise findings do not establish the proposed synaptic-complexity mechanism. Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive), [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Aerobic activity can acutely improve attention and inhibitory control

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** Aerobic exercise influences dopamine and norepinephrine systems relevant to prefrontal executive function

**Verdict: Supported.** Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive), [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Exercise reliably improves dopamine-receptor sensitivity and thereby builds a stronger, more resilient ADHD brain

**Verdict: Unsupported.** The asserted reliable receptor-sensitivity mechanism is not established. Evidence: [EXER](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 217

**Title:** Can saffron be used to treat ADHD symptoms?  
**URL:** https://www.youtube.com/shorts/tHNZ5B8LPXA  
**Views:** 7,223  
**Likes:** 27  
**Comments:** 0  
**Duration:** 69 seconds

**Transcript:**

> Today, a parent asked me about using saffron to treat their child's ADHD symptoms, and I wanted to see what you think. >> That's interesting, because there are some small studies that show saffron may have benefits in treating hyperactivity. But again, these are small studies with no long-term data. >> Whereas, we do have lots of long-term data on the safety of stimulant medications for treating ADHD. >> Right. And therapeutic options, like behavioral parent training, organizational skills training, and school-based supports and educational interventions. >> The saffron studies are promising, but we don't have long-term data on their safety or dosing guidelines. So, what else could this family do in the meantime to treat their ADHD? >> There's lots that they can do, including keep a daily routine, use visual schedules, chunk directions into small steps, praise good behaviors, and focus on healthy habits, like sleep, nutrition, and exercise. >> Thanks for all of your ADHD tips.

### Revised claim review

The transcript explicitly presents saffron evidence as preliminary; this is not scored as a claim of established equivalence to stimulants.

**Claim 1:** Small preliminary studies suggest that saffron may improve some childhood ADHD symptoms

**Verdict: Supported.** Evidence: [SAFF](https://pubmed.ncbi.nlm.nih.gov/37864351/).

**Claim 2:** Prescription stimulants have substantially more evidence on efficacy and longer-term safety than saffron

**Verdict: Supported.** Evidence: [SAFF](https://pubmed.ncbi.nlm.nih.gov/37864351/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Behavioural parent training, organizational-skills training, school supports, and educational interventions are evidence-based components of ADHD care

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Routines, visual schedules, instructions divided into smaller steps, praise, sleep, nutrition, and exercise can support management

**Verdict: Supported.** Evidence: [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 218

**Title:** Thinking outside the box for treating ADHD  
**URL:** https://www.youtube.com/shorts/asNscXvGFb4  
**Views:** 96  
**Likes:** 4  
**Comments:** 0  
**Duration:** 81 seconds

**Transcript:**

> millions of Americans are suffering from ADHD attention deficit hyperactivity disorder many are treated with a stimulant adoral Rin some improve some don't many continue to feel tense on those stimulants I'm a physician specializing in hypertension high blood pressure in the blog I described something amazing that I noticed that most psychiatrists are not aware of in treating hyper attention in patients who had also ADHD when I prescribed a certain type of beta blocker that doesn't even get into the brain they improved in their ADH symptoms many felt calmer and some were able to reduce or even stop their adderal it was a real game Cher clearly formal studies are needed but in the meantime the drug is safe in most patients even if you don't have hypertension and the response is quick you'll know within a few days so if you have ADHD and you feel you could be doing better show the blog to your psychiatrist and get a quick trial I think it may help [Music]

### Revised claim review

The ratio label is not weighted by treatment risk. Label 2 does not validate the unsupported beta-blocker recommendation; its clinical importance is much greater than a simple one-third unsupported ratio conveys.

**Claim 1:** A peripherally acting beta blocker produced meaningful ADHD improvement in the speaker’s patients

**Verdict: Excluded from scoring.** The speaker’s own clinical observations are personal case reports, not independently checked patient outcomes.

**Claim 2:** Many patients taking the beta blocker became calmer and reduced or stopped Adderall because their ADHD improved

**Verdict: Excluded from scoring.** Anecdotal patient outcomes, not a generalized quantified efficacy claim.

**Claim 3:** The unnamed beta blocker is safe for most people without hypertension, works within days, and should be tried quickly for ADHD

**Verdict: Unsupported.** The unnamed drug’s safety, prompt response and broad ADHD trial recommendation cannot be established. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [FDASTIM](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions).

**Claim 4 — added from supplied transcript:** Millions of Americans have ADHD.

**Verdict: Supported.** Explicit introductory statement omitted by the original annotation. Evidence: [CDC2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm).

**Claim 5 — added from supplied transcript:** Stimulants are used to treat ADHD, helping some patients but not all.

**Verdict: Supported.** Explicit introductory statement; response varies among individuals. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **2**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 4 — Highly misleading**.

**Decision limitation:** The ratio is not weighted by medical risk. Label 2 does not validate the unsupported recommendation to try an unnamed beta blocker for ADHD.

---

## Video 219

**Title:** ADHD and Hypersensitivity. | #symptoms #adhd #autism #adhdmedication #symptomsofadhd  
**URL:** https://www.youtube.com/shorts/Fpy0MiZ-66k  
**Views:** 961  
**Likes:** 38  
**Comments:** 0  
**Duration:** 45 seconds

**Transcript:**

> let's talk about ADHD and Hyper sensitivity now that that could mean hypers sensitivity to noise to Smells to sounds particular textures and it could be an intense fascination with something or an intense dislike of something often associated with the autistic traits when talking about hypers sensitivity it could you could also be thinking about rejection sensitivity dysphoria RSD and that's something quite different when someone it's when someone experiences great pain and distress over perceived isolation and rejection it's usually been associated with some event in the past for more information about me you'll find in the bio

### Revised claim review

**Claim 1:** Sensitivity to noise, smell, touch, or texture can occur in ADHD

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 2:** Intense sensory likes or dislikes are often associated with autistic traits

**Verdict: Supported.** Evidence: [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** Rejection-sensitive dysphoria refers to intense distress after perceived rejection and is different from sensory sensitivity

**Verdict: Supported.** Informal rejection-distress terminology, not a separate official diagnosis. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 4:** Rejection-sensitive dysphoria is usually caused by a past event

**Verdict: Unsupported.** A usual single past-event cause is not established. Evidence: [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **3**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **3 / 4 × 100 = 75.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 220

**Title:** weird and specific adhd audhd symptoms #adhd #audhd #adhdsymptoms #adhdinwomen #adhdinadults  
**URL:** https://www.youtube.com/shorts/KfhzcWFypmM  
**Views:** 6,522  
**Likes:** 548  
**Comments:** 17  
**Duration:** 71 seconds

**Transcript:**

> You're going to find this creepy and uncomfortable, but here are some eerily specific things that are true about you if you have ADHD or ah DHD. You know that it's not really normal to have to have some sort of noise to fall asleep, like music playing, white noise, the TV on. But I'm guessing your nighttime routine consists of needing some sort of noise like this. And watching all the shapes behind your eyelids move around and do stuff, which by the way, many people actually don't see, but you do. Speaking of sleep, you sleep like this. You also enjoy sleeping with your hand on your face sometimes, or your hands otherwise secured in other weird places, like in your pockets if you have them. You feel a certain type of panicked rage at the way your clothes feel often. The two things that trigger you like no other are decisions and waiting. Often flood your sinks. And decisions, why does anyone ask us to make them? I bet you somewhere in your house, probably in your vicinity, your cabinets or drawers are open. You're in a lot of credit card debt from all your impulsive purchases. One of the main things you buy are new clothes, but you often never wear them because again, sensory issues. We like to resort to the same things that we know feel good.

### Revised claim review

**Claim 1:** Needing background noise to fall asleep is characteristic of ADHD or AuDHD

**Verdict: Unsupported.** This particular sleep requirement is not established as a characteristic ADHD/AuDHD sign. Evidence: [SLEEP](https://pubmed.ncbi.nlm.nih.gov/28064405/).

**Claim 2:** Seeing shapes behind closed eyelids is an ADHD or AuDHD feature

**Verdict: Unsupported.** The visual phenomenon is not established as an ADHD/AuDHD sign. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** Sleeping with a hand on the face or in pockets is characteristic of ADHD or AuDHD

**Verdict: Unsupported.** The sleeping posture is not established as an ADHD/AuDHD sign. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 4:** Clothing textures can cause intense distress in people with ADHD or co-occurring autism

**Verdict: Supported.** Evidence: [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

**Claim 5:** Waiting and decision-making can be especially difficult in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 6:** Frequently flooding sinks is an ADHD or AuDHD symptom

**Verdict: Unsupported.** A mishap is not a distinct ADHD symptom; an inattention mechanism would need qualification. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 7:** Leaving cabinets or drawers open can result from inattention or interrupted task sequences

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 8:** ADHD impulsivity can contribute to excessive spending or credit-card debt, while sensory preferences can influence unused clothing purchases

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [SENS](https://pubmed.ncbi.nlm.nih.gov/40250555/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **4**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **4 / 8 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 221

**Title:** The Biggest Challenge in ADHD Treatment  
**URL:** https://www.youtube.com/shorts/iVh2Zix5rwA  
**Views:** 62,143  
**Likes:** 3,366  
**Comments:** 65  
**Duration (seconds):** 92

**Transcript:**

> The biggest challenges in ADHD, in my opinion, are not the first-level challenges. They're the challenges that we layer on top. If you look at the comorbidity between people with ADHD and depression, 3% of people who are diagnosed with depression will grow up to have ADHD. 70% of people with ADHD will grow up to have depression. So, this is how this goes. I forgot my birthday card. That is a problem in and of itself that could be fixed. Then our mind does something kind of interesting. I've forgotten 7 years in a row. So, not only do I forget my friend's birthday card, now my mind is keeping track of it and it is making me feel worse. Treating ADHD is not just about time blindness, suppression of bodily sensations, executive function deficit, emotional dysregulation. It is also about the consequences of living with those things. I'm an idiot. I'm unreliable. I'm this. I'm that. We have the first layer of primary symptoms and then we layer on top of that things that are harder to beat. And here's the tricky thing. If I start someone on stimulant medication, it only works on layer one. Doesn't really work on layer two. Works on layer two maybe a little bit because it regulates my the amount of guilt that I feel. Reduces the activity of my guilt circuit in the brain. But it doesn't change my sense of identity, which is why I really love, and this is what really confuses people, psychotherapy is equally effective to medication. Works the same. Effect size is the same. When I work with patients with ADHD, I like to do psychotherapy with them as well because we have to do this identity component. You're not a bad friend. You're not a bad person. You have this problem.

### Revised claim review

**Claim 1:** About 3% of people diagnosed with depression will develop ADHD, whereas 70% of people with ADHD will develop depression

**Verdict: Unsupported.** The percentages and direction of developing the disorders are not established as stated. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 2:** ADHD treatment must address both core symptoms and the accumulated shame, guilt, and negative self-beliefs caused by repeated difficulties

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CRIT](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366).

**Claim 3:** Stimulant medication mainly targets core ADHD symptoms and does not by itself directly rewrite a person's identity or long-standing negative beliefs

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Stimulants reduce guilt by decreasing activity in a specific “guilt circuit” in the brain

**Verdict: Unsupported.** The guilt-circuit mechanism is not established. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** Psychotherapy is equally effective to stimulant medication for ADHD, with the same effect size

**Verdict: Unsupported.** Equal effect sizes across medication and psychotherapy are not established. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 6:** Psychotherapy can be useful alongside medication for people with ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **3**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **3 / 6 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 222

**Title:** Effects of Ritalin for ADHD  
**URL:** https://www.youtube.com/shorts/b0ciC7g9_-o  
**Views:** 158,476  
**Likes:** 3,019  
**Comments:** 168  
**Duration (seconds):** 46

**Transcript:**

> give everybody Rin two of the seven types get better and five of them get worse which is why rin's controversial because when it works it can literally take kids from C's and D's hating themselves to A's and B's getting into the university they want to get into so I'm a fan typically I first will go a natural route changing their diet giving them nutrients but if it doesn't work I will use the medicine or recommend the medicine because left untreated there's serious problems with addiction School failure relationship failure bankruptcy and so on and it's personal to me

### Revised claim review

**Claim 1:** ADHD has seven valid types, and Ritalin improves two of them while making the other five worse

**Verdict: Unsupported.** The seven-type treatment-response system is not validated. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** When methylphenidate works, it can substantially improve school functioning and self-esteem

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** Diet changes and nutrient supplements should generally be tried before evidence-based ADHD medication

**Verdict: Unsupported.** Diet/supplements are not generally recommended before age-appropriate evidence-based medication. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 4:** Untreated ADHD is associated with increased risks involving substance use, education, relationships, and finances

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 223

**Title:** Common ADHD Symptoms  #adhd #adhders #adhdmanagement  
**URL:** https://www.youtube.com/shorts/Usba30Csbuc  
**Views:** 61  
**Likes:** 5  
**Comments:** 0  
**Duration (seconds):** 49

**Transcript:**

> what are some symptoms of ADHD being able to sit still especially in a calm or quiet environment constantly fidgeting been unable to concentrate on tasks excessive physical movement excessive talking being unable to wait for your turn acting without thinking and interrupting conversations for more information visit done the number one ADHD curve platform for ADHD diagnosis and personalized treatment plans with poor certified and ADHD car experienced clinicians now offering both in-person and virtual appointments go check that out

### Revised claim review

WORDING FLAG: a possible missing negative would change scoring, but no transcription was checked or altered.

**Claim 1 — clarified extraction:** Being able to sit still, with fidgeting and movement, is an ADHD symptom.

*Original annotation wording:* Difficulty remaining seated, frequent fidgeting, and excessive physical movement can be ADHD symptoms

**Verdict: Unsupported.** The supplied transcript says being able to sit still; the original annotation changed the polarity. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Difficulty concentrating on tasks can be an ADHD symptom

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Excessive talking, difficulty waiting one's turn, acting without sufficient forethought, and interrupting can be ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 1 — Accurate**.

**Decision limitation:** The supplied transcript says “being able to sit still”. A missing negative would reverse Claim 1 and give Label 1; the transcript has not been altered.

---

## Video 224

**Title:** Therapist Shares: How You Answer this One Question Signals if You HaveADHD, Autism, or AuDHD  
**URL:** https://www.youtube.com/shorts/T2KSyaURhdA  
**Views:** 437,274  
**Likes:** 43,773  
**Comments:** 2,368  
**Duration (seconds):** 163

**Transcript:**

> In initial consultations, the assessment has already begun. And one of the telling phrases that I listen for is, "I just want to be a better person. I want to make my life better." And my response now is always, "Okay, what do you mean by that?" If it's autism, what I hear is, "I just feel like I want to be better with people. I want to feel more understood. I want to understand people better." And kind of the delineation here is, a lot of people I work with who are autistic are very pleasant, congenial people. They have a pleasant resting face. But where the disconnect is is they frequently don't know when they put something out into the world, when they say something, whether or not it will land well. And so, in their response, what I hear is a lot of framing, a lot of over-explaining, a lot of checking in with me verbally, because even though the situation is, "I'm here to learn about you, so I can help you. There is no judgment." Even in that space, there's such a fear that what they're saying is going to be taken poorly because it has in their past, that they can't drop the need to overqualify and over-explain themselves. Now, this can just be first-meeting jitters. But what then projects into the future is, in the second meeting, third meeting, fourth meeting, they continue to do that. That is a telltale sign of highly masked, low-support autism. It's being afraid that despite our established relationship, they're afraid of being left. This is in contrast to ADHD, where there's a realization that things go wrong, but generally the person feels pretty likable. And the person doesn't necessarily have problems landing things up front. They have problems with following through. And so, when they say, "I want to be better," it's more about issues with inattention, not following through on obligations, letting other people down, feeling like a failure because you promised to do something, or you could do it when you had enough dopamine, but then when you didn't, you couldn't do it. And so, they're not as cautious about framing things because they're not worried that they're not going to land things. Their version of being better is being more consistent. And then you have ADHD. You have both the upfront, "Oh my gosh, I'm not sure how this is going to land." And you have, "I also feel like I don't have great follow-through in certain areas." And so, you have these autistic reservations about things not landing, but then the ADHD comes in impulsively and says, "Fuck it, let's go." Or they're really great at some social things and not others. Like they're great at things they plan because they control the environment, but they're not great at going to things they haven't planned themselves. With AuDHD, it's kind of like I can be spontaneous within that predetermined width, but outside of that, I'm rigid. And that to me, just in our interactions, how you're framing things, how you're jumping in, how you're not jumping in, starts to help me build a profile of what's sitting in front of me. You are a unique individual. You're your own soundtrack, but ADHD, autism, and AuDHD all come through on these frequencies that disrupt your life in predictable ways. So, if you're wrestling with this internal thought, I need to go to therapy or coaching to be a better person, and you're already thinking you're some kind of neurospicy, answering the question, what does being a better person mean to me? That can help guide whether it's autism, ADHD, or AuDHD. What's been your experience with being assessed for autism, ADHD, or AuDHD? I'd love to hear from you.

### Revised claim review

**Claim 1:** Repeated over-explaining, checking how statements are received, and fear of being left are telltale signs of highly masked, low-support autism

**Verdict: Unsupported.** These nonspecific interpersonal experiences do not establish masked autism. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

**Claim 2:** People with ADHD generally feel likable and do not have difficulty making an initial social impression, unlike autistic people

**Verdict: Unsupported.** The broad favourable ADHD social stereotype is unsupported. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

**Claim 3:** Inattention and difficulty following through on obligations are characteristic ADHD problems

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

**Claim 4:** A person's ability to act depends on whether they have “enough dopamine” at that moment

**Verdict: Unsupported.** Action cannot be reduced to a single sufficient-dopamine threshold. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

**Claim 5:** AuDHD can be identified from a pattern of being spontaneous within a predetermined range but rigid outside it

**Verdict: Unsupported.** This pattern is not a validated way to identify co-occurrence. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

**Claim 6:** Asking what “being a better person” means can guide whether someone has autism, ADHD, or both

**Verdict: Unsupported.** The proposed question cannot determine these diagnoses. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/), [SOCIAL](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full), [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **6**
- Supported: **1**; unsupported: **5**; excluded: **0**.
- Supported-claim percentage: **1 / 6 × 100 = 16.67%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 225

**Title:** Double Trouble: Untreated ADHD Symptoms and their Effect on Depression #adhd #psychnp  #psychiatry  
**URL:** https://www.youtube.com/shorts/V3t3gTgJ8Ns  
**Views:** 32  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 16

**Transcript:**

> in individuals with both depression and ADHD untreated ADHD symptoms May a exacerbate depressive symptoms B mask the severity of depression C increase the risk of substance abuse or D all of the above answer d

### Revised claim review

**Claim 1:** In a person with both ADHD and depression, untreated ADHD symptoms may aggravate depressive symptoms

**Verdict: Supported.** Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 2:** Untreated ADHD masks the severity of depression

**Verdict: Unsupported.** A general masking of depression severity by ADHD is not established. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/).

**Claim 3:** Untreated ADHD is associated with increased substance-use risk

**Verdict: Supported.** Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 226

**Title:** The Surprising Link Between Low Dopamine and ADHD Symptoms #adhd #adhdresearch #dopamine  
**URL:** https://www.youtube.com/shorts/X_I5poyLhh8  
**Views:** 519  
**Likes:** 23  
**Comments:** 1  
**Duration (seconds):** 61

**Transcript:**

> well the problem seems to be that when dopamine is low certain neurons are firing when they shouldn't be this is like a band right we'll go back to our band that's a guitar a bass and a and a person playing the drums and it's as if one of those or several of those instruments are playing notes when they shouldn't be playing all right the pauses in music are just as important as the actual playing of notes when dopamine is too low neurons fire more than they should in these Networks that govern attention this is the so-called low dopamine hypothesis and if you start looking anecdotally at what people with ADHD have done for decades not just recently since the low dopamine hypothesis has been proposed but what they were doing in the 1950s and in the 1940s and the 1960s what you find is that they tend to use recreational drugs or they tend to indulge in

### Revised claim review

**Claim 1 — clarified extraction:** One hypothesis is that altered dopamine signalling contributes to inappropriate firing in attention networks in ADHD.

*Original annotation wording:* ADHD is caused by dopamine being too low, which makes neurons in attention networks fire when they should be silent

**Verdict: Supported.** Explicitly presented as a hypothesis, not an established universal cause. Evidence: [STIM](https://www.nature.com/articles/1301164).

**Claim 2 — clarified extraction:** ADHD has been associated with elevated recreational substance-use problems.

*Original annotation wording:* People with ADHD have historically tended to use recreational drugs because of this low-dopamine state

**Verdict: Supported.** The original annotation added a proved low-dopamine causal explanation. Evidence: [SUDMED](https://pubmed.ncbi.nlm.nih.gov/28659039/), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 227

**Title:** even more weird symptoms of adhd #adhd #audhd #neurodivergent #adhdsymptoms #adhdinwomen  
**URL:** https://www.youtube.com/shorts/2ZvzZ0DyhHU  
**Views:** 4,269  
**Likes:** 332  
**Comments:** 13  
**Duration (seconds):** 61

**Transcript:**

> Are you ready to get creeped out? Because here are some eerily specific things about you if you have ADHD or AudHD. We'll start with that scab in the back of your head, you know, the one that won't go away cuz you won't stop picking it. You constantly chew the inside of your cheeks or pick at your lips. And I bet you if you stick your tongue out right now and look at it, it's bumpy. That's from stimming with your jaw. Betting you sleep like this and you also enjoy covering your face with your hands. Emotions happen quick and intensely and you can be fast to react. You react a bit dramatically. We can be very sensitive, but you're also the first to get over it. Come on already, just move on, right? You've been told, "If you would only apply yourself." You've probably also been accused of being inconsiderate for interrupting or being late, etc. But you have such a strong sense of morals and values. You care so deeply for the greater good. You don't like authority figures. You question everything because you're a firm believer that we should all think for ourselves.

### Revised claim review

**Claim 1:** People with ADHD or AuDHD characteristically pick scalp scabs, chew their cheeks, pick their lips, and develop a bumpy tongue from jaw stimming

**Verdict: Unsupported.** Possible repetitive behaviours do not establish this whole bundle or the tongue mechanism. Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/), [BFRBCO](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552165/).

**Claim 2:** A particular sleeping posture and covering one's face with the hands are characteristic of ADHD or AuDHD

**Verdict: Unsupported.** The sleeping posture is not established as a characteristic ADHD/AuDHD sign. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ASDADHD](https://pubmed.ncbi.nlm.nih.gov/32448170/).

**Claim 3:** ADHD can involve rapid, intense emotional reactions and heightened emotional sensitivity

**Verdict: Supported.** Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 4:** People with ADHD are characteristically the first to recover from strong emotions

**Verdict: Unsupported.** Faster recovery than others is not established. Evidence: [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 5:** People with ADHD characteristically have unusually strong morals, prioritize the greater good, dislike authority, and question everything

**Verdict: Unsupported.** A justice-sensitivity association does not establish superior morals or this personality bundle. Evidence: [JUSTICE](https://pubmed.ncbi.nlm.nih.gov/23223013/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **1**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **1 / 5 × 100 = 20.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 228

**Title:** What is ADHD? (Explained Simply & Funny) | ADHD Symptoms You Didn't Know  
**URL:** https://www.youtube.com/shorts/xW-gp1M8S8M  
**Views:** 126  
**Likes:** 3  
**Comments:** 0  
**Duration (seconds):** 165

**Transcript:**

> Ever opened a drawer, forgot why you opened it, remembered again, but halfway through you're suddenly reorganizing your bookshelf, eating cereal, and googling how many holes are in a straw. Congratulations. You might just have a tiny taste of what ADHD feels like. But don't worry, today we're breaking it down without any complicated brain science or boring textbook talk. Stick around. This might explain a lot about you or that one friend who always interrupts and loses their phone mid call. So, what is ADHD? ADHD stands for attention deficit hyperactivity disorder. But honestly, the name doesn't do it justice. It's not about not paying attention. It's more like paying attention to everything at once all the time. And also, not at all. Yeah, it's weird. Your brain is like 47 browser tabs open. One of them is playing music and you can't figure out which one. Let's say you're writing an email. You start typing, then think, I should grab a snack. On the way to the kitchen, you see a sock on the floor. You pick it up, remember laundry, start a load, forget the snack, return to your computer, stare at the screen, and ask, "Wait, what was I doing again?" That is ADHD. A DHD isn't just about forgetting stuff or being hyper. It affects how your brain regulates focus, emotions, and even time. Ever heard of time blindness? It's like you either have no time or too much time, and both are equally wrong. Also, starting tasks is hard. Finishing them is harder. Remembering to start in the first place, impossible. And yes, there's hyperactivity, too. Sometimes. Some people with ADHD feel like their brain is running a marathon. Others, their brain is running, but their body is stuck in bed. Hyperactivity doesn't always mean bouncing off walls. It can just mean thoughts that never shut up. Like your brain keeps hitting reply all to every single idea. A DHD is basically, "I'm bored. I'm overwhelmed. I'm doing three things at once and none of them are done. Oops, forgot to eat lunch again. Why did I just cry at a dog food commercial? Relatable? You might not be broken. You might just have a different operating system. The good news, ADHD is manageable with tools, structure, maybe therapy or medication. People with ADHD can thrive. In fact, many are creative, quick thinkers, and great in a crisis as long as they remember there is a crisis. So ADHD isn't a flaw. It's not just an excuse. It's a real neurological condition that affects real people. And no, they're not lazy. They just have brains that work a little differently. If this sounded familiar, well, you're not alone. You're not broken. You're just wired with a bit more chaos and curiosity. And honestly, that's kind of brilliant. Thanks for watching. And hey, if you made it to the end without getting distracted, give yourself a gold star or at least a snack. You've earned it.

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** ADHD stands for attention-deficit/hyperactivity disorder

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** ADHD is not about failing to pay attention; it is described as attending to everything at once all the time and also not at all.

*Original annotation wording:* ADHD is not really about inattention; it is essentially paying attention to everything at once

**Verdict: Unsupported.** The initial denial is an eligible clinical assertion. The subsequent explicit comparison does not erase it; no literal browser tabs are attributed to the brain. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** ADHD can affect regulation of attention and can be associated with emotional-regulation and time-management difficulties

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/), [TIME](https://pubmed.ncbi.nlm.nih.gov/11499990/).

**Claim 4:** ADHD makes starting and finishing tasks difficult, and remembering to start in the first place is impossible.

*Original annotation wording:* ADHD can make initiating, organizing, and completing tasks difficult

**Verdict: Unsupported.** The compound claim includes impossibility. Executive difficulties do not establish that a person with ADHD cannot remember to start a task. Evidence: [UPD_NIMH_ADULT](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know).

**Claim 5:** Hyperactivity is not always obvious physical movement and may be experienced as internal restlessness or excessive mental activity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [RACING](https://pubmed.ncbi.nlm.nih.gov/37731878/).

**Claim 6:** ADHD is manageable using individualized supports that may include structure, therapy, and medication, and people with ADHD can thrive

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 7:** Many people with ADHD are creative, quick thinkers and great in a crisis.

*Original annotation wording:* People with ADHD are generally more creative, quicker thinkers, and better in crises

**Verdict: Unsupported.** This is a group assertion, not a personal account. Self-reported strengths do not establish the complete performance profile, especially crisis performance. Many is retained; no comparison with non-ADHD people is added. Evidence: [LIT_STRENGTHS](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.922788/full).

**Claim 8:** ADHD is a real neurodevelopmental condition and its impairments should not be dismissed as laziness

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **5**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **5/8 × 100 = 62.50%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Previous reviewed label: **Label 1**.
- Uploaded CSV label: **Label 2**.

---

## Video 229

**Title:** Treating ADHD with Airway Orthodontics  
**URL:** https://www.youtube.com/shorts/VL_JfdVP-Ws  
**Views:** 608  
**Likes:** 17  
**Comments:** 1  
**Duration (seconds):** 31

**Transcript:** Unavailable

**Status:** # tactiq.io free youtube transcript
# Treating ADHD with Airway Orthodontics
# https://www.youtube.com/watch/VL_JfdVP-Ws

00:00:02.760 often the child even though is
00:00:04.799 hyperactive so there is one medical term
00:00:06.600 called ADHD Attention Deficit
00:00:08.880 Hyperactive
00:00:09.920 Disorder doctors diagnose it but then
00:00:12.240 the doctors don't know how to treat it
00:00:14.320 because it is related to the airway
00:00:15.920 which is why Airway Orthodontics become
00:00:17.480 so important you treat the airway the
00:00:19.720 Sleep improves the child probably can be
00:00:22.240 weaned of ADHD so it's something which
00:00:25.279 is upcoming and I'm sure we'll spread
00:00:26.880 awareness in future

### Revised claim review

**Claim 1:** Doctors diagnose ADHD but do not know how to treat it

**Verdict: Unsupported.** Evidence-based ADHD treatment exists. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** ADHD is fundamentally related to airway obstruction

**Verdict: Unsupported.** Sleep-disordered breathing can mimic or worsen symptoms; it does not establish ADHD as fundamentally airway obstruction. Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/).

**Claim 3:** Airway orthodontics is therefore an important ADHD treatment

**Verdict: Unsupported.** Airway orthodontics is not thereby established ADHD treatment. Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/), [SDBREVIEW](https://journals.sagepub.com/doi/10.1177/10870547241232313).

**Claim 4:** Treating an airway disorder can improve a child’s sleep and behaviour

**Verdict: Supported.** Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/).

**Claim 5:** Treating the airway will probably allow a child to be “weaned off ADHD”

**Verdict: Unsupported.** Treating a sleep/airway condition does not generally permit someone to be weaned off developmental ADHD. Evidence: [SDB](https://pubmed.ncbi.nlm.nih.gov/24581717/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **1**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **1 / 5 × 100 = 20.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 230

**Title:** POV: How hormones affect ADHD symptoms  
**URL:** https://www.youtube.com/shorts/2KQDWpKfdIw  
**Views:** 6,478  
**Likes:** 302  
**Comments:** 8  
**Duration (seconds):** 40

**Transcript:**

> Ever wonder why your ADHD symptoms change throughout the month? It could be your hormones. When estrogen's up, dopamine's up. Suddenly, I am the queen of productivity. Thank you. Hyperfocus. Confidence level 100 to zero real quick. Why am I suddenly overthinking every single thing? When estrogen crashes, I guess my brain does, too. Progesterone's high, and so is the urge to procrastinate. Everything feels harder to get done. Shout out to my hormones for constantly switching up my ADHD symptoms and making my emotions heightened even more.

### Revised claim review

**Claim 1:** ADHD symptoms can vary across the menstrual cycle in association with hormonal changes

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/).

**Claim 2:** When estrogen rises, dopamine necessarily rises enough to produce productivity, hyperfocus, and confidence

**Verdict: Excluded from scoring.** Personal comic account of productivity/confidence, not a generalized hormonal guarantee.

**Claim 3:** Falling estrogen can be associated with worsening ADHD symptoms

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/).

**Claim 4:** High progesterone directly causes procrastination and makes tasks harder for people with ADHD

**Verdict: Excluded from scoring.** Personal account of procrastination; the annotation added a generalized direct causal assertion.

**Claim 5:** Hormonal fluctuations can intensify emotional symptoms in some people with ADHD

**Verdict: Supported.** Evidence: [SEXHORM](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **2**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 231

**Title:** Understanding ADHD | Types, Symptoms & Treatment #adhd  
**URL:** https://www.youtube.com/shorts/9QeT3vIV-oI  
**Views:** 18  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 85

**Transcript:**

> ADHD can make everyday life challenging, especially when it comes to focusing, staying organized, and maintaining attention on tasks or activities. In simpler terms, it can make it hard for someone to concentrate or stay on track with daily tasks. According to the Diagnostic and Statistical Manual of Mental Disorders, the fifth edition or the DSM5, ADHD is defined as a neurodedevelopmental disorder characterized by a persistent pattern of inattention, hyperactivity, and impulsivity that interferes with a person's daily functioning and development. This means it causes long-term challenges in paying attention or controlling energy levels, which can disrupt daily life. Children with inattentive ADHD often lose or forget things they need for tasks like books or homework. They may seem like they are not paying attention when spoken to directly and struggle to stay focused on tasks or play activities. They may also find it hard to organize their activities and follow instructions, leaving tasks incomplete. This means they may start things but have trouble finishing them. Children with hyperactive impulsive ADHD may fidget a lot, meaning they have difficulty staying still, or they may move around when it's not appropriate, such as getting up in the middle of class. They might talk excessively or interrupt others, find it hard to wait their turn in conversations or activities, and often blurt out answers before questions are finished. These behaviors can lead to trouble, not because they don't care, but because they struggle to control their actions.

### Revised claim review

**Claim 1:** ADHD is a neurodevelopmental disorder involving a persistent, impairing pattern of inattention and/or hyperactivity-impulsivity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Losing needed items, seeming not to listen, difficulty sustaining attention, disorganization, and failing to finish tasks can be inattentive ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Fidgeting, leaving one's seat, excessive talking, interrupting, difficulty waiting, and blurting answers can be hyperactive-impulsive ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** These behaviours may reflect impaired self-regulation rather than a child simply not caring

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 232

**Title:** Do you have ADHD? Ways to detect signs and symptoms. #adhd #adhdtreatment #homeopathictreatment  
**URL:** https://www.youtube.com/shorts/PNJw7AOMzMc  
**Views:** 4,372  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 167

**Transcript:**

> hi friends this is Dr annali today let's talk about ADHD what is ADHD and how do you identify whether you have ADHD or whether your child has ADHD so ADHD is seen both in children as well as in adults to start off with uh let's start with children so normally parents uh whose kids have ADHD they will complain that the child is not sitting too long is not focusing too long is hyperactive physically hyper like running around around from one place to another place uh they don't tend to take commands very easily and do not follow them a lot of times they may be Fearless okay there's no fear so you have to be super strict with them for example to even make them sit they can be very impulsive uh and may lack a lot of patience okay so if you tell them to sit for too long or even like for example when you go out uh and you tell them to wait for the elevator to come or the lift to come or for their turn they will not wait wait they will be very impulsive and very impatient uh they would want to do things very quickly okay and their reactions could be very sudden that's what impulsivity means children at home will you know tend to be rowing around running around all the time they won't be sitting and doing what's being told to them they can be sometimes destructive uh they could have social issues where they would not play games appropriately not wait for their turn could be do dominating in school we normally see children to have complaints where again they don't sit don't finish their homework a lot of kids are not able to write and read you see for writing you need to focus okay and you need to be patient uh children generally with ADHD will have issues with writing uh they can be very um you know disorganized uh they would not know where their books are where their pens are Etc Okay so this is in short what children would look like in ADHD whereas as his child grows up uh you know and becomes an adult or purely cases where we see ADH in adults you may not see physical hyperactivity however you will see them to be uh you know disorganized can't plan things into the future uh procrastinating will not do things timely will not stay to their commitments will get bored will change jobs very quick quickly will be tuned off in the in in short basically you're talking to them and their you know mind is somewhere else so children and adults may present things a little differently I hope you are able to identify if you have ADHD and seek treatment thank you

### Revised claim review

**Claim 1:** ADHD occurs in both children and adults, and visible hyperactivity may become less prominent with age

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Inattention, disorganization, impulsivity, impatience, excessive movement, and difficulty waiting or completing work can be ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Children with ADHD are generally fearless and parents need to be “super strict” with them

**Verdict: Unsupported.** Fearlessness and a universal super-strict parenting prescription are unsupported. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 4:** Destructiveness, dominating other children, and inability to read or write are characteristic ADHD features

**Verdict: Unsupported.** Destructiveness and inability to read/write are not characteristic ADHD features as asserted. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 5:** Adults with ADHD may have difficulty planning, organizing, meeting commitments, sustaining attention, and managing procrastination

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 233

**Title:** Psychologist tip for treating ADHD #adhdinsights #adhd #adhdtiktok  
**URL:** https://www.youtube.com/shorts/ODq79X0VH3w  
**Views:** 1,213  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 60

**Transcript:**

> when you're treating ADHD one of the things that I've learned as a psychologist and I keep it in my mind every single day is to whenever possible work with the ADHD instead of against the ADHD so functionally what this is going to look like is for example if you're doing some kind of brain training like a mindfulness based intervention for ADHD if I tell a person to like sit there don't move and we're doing like a traditional mindfulness based meditation and this person's really high on the end of hyperactive and impulsive symptoms it's going to be a living hell for them but you don't have to do this right you can train mindfulness in all kinds of ways that involve movement you can do things like mindful balancing or mindful walking or a whole host of other ways that you could train this skill and do this brain training in ways that work with the ADHD instead of directly against it so it's just something to keep in mind you don't want to be bashing your face into a brick wall when you could be doing the exact same types of interventions and treatments for ADHD in a way that works so much better for the person

### Revised claim review

**Claim 1:** ADHD interventions should be adapted to the person's symptom pattern and practical needs rather than delivered in one rigid form

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [MIND](https://pubmed.ncbi.nlm.nih.gov/34146899/).

**Claim 2:** Mindfulness practice can be adapted to include walking, balancing, or other movement for someone who finds motionless meditation difficult

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [MIND](https://pubmed.ncbi.nlm.nih.gov/34146899/).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **2**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **2 / 2 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 234

**Title:** Recognising ADHD Symptoms #adhd #adhdsigns  
**URL:** https://www.youtube.com/shorts/KvwttROx9hg  
**Views:** 6  
**Likes:** 2  
**Comments:** 0  
**Duration (seconds):** 52

**Transcript:**

> think you might have ADHD let's speed through the symptoms in 40 seconds in attention you're easily distracted forgetful and have trouble following instructions your life total disorganized chaos hyperactivity you're always on the Move talking non-stop making impulsive decisions and fidgeting like there's no tomorrow impulsivity you're the conversation interruptor the Act without thinker and patience what's that if you're nodding along think that's so me remember only a professional can diagnose ADHD but hey at least now you know what to look out for and if you don't have ADHD congrats on making it through this rapid fire video without getting distracted if this sounds like you you're not alone ADHD is manageable talk to a pro

### Revised claim review

**Claim 1:** Distractibility, forgetfulness, difficulty following instructions, and disorganization can be inattentive ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Excessive movement or talking, fidgeting, interrupting, acting without sufficient forethought, and difficulty waiting can be hyperactive-impulsive ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Only a qualified professional should diagnose ADHD, and the condition is manageable

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AQAS](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 235

**Title:** ADHD Symptoms in Children | Recognize Early Signs & Behaviors  
**URL:** https://www.youtube.com/shorts/mdTLEkiXrFs  
**Views:** 88  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 74

**Transcript:**

> Sir, how can parents recognize if their child has ADHD? What are the symptoms that can be seen? >> That's a very important question, madam. What happens is, for example, if you tell a child to sit here and he is unable to sit still in that place, he keeps running here and there repeatedly. Running, jumping, playing, playing, playing. One of the things is restlessness. The second thing is low concentration. For example, if he is playing with a toy, how long does he actually play with that toy? Usually, even if you give a child a toy car, their interest in that car lasts for at least 2 to 3 days. But that's not the case with ADHD. 10 minutes and they're on to the next toy. In just 10 minutes, they move on to another toy. Very capricious, very restless. So, the second symptom I mentioned is low concentration. The third is violence, rage, anger. What does that mean? These children experience a much higher intensity of anger. If we scold a child, they usually get angry only for a moment. But in this case, the anger is momentary. However, its intensity is extremely explosive. They might smash a phone, throw things around, or break their toys. This anger, this rage is a result of their hyperactivity. It's not really the child's own anger. It's because of the condition that they act out in this

### Revised claim review

**Claim 1:** Inability to remain seated, excessive running, and restlessness can be childhood ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 2:** Difficulty sustaining attention and rapidly abandoning activities can be childhood ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 3:** A typical child remains interested in one toy for two to three days, whereas a child with ADHD changes toys after ten minutes

**Verdict: Unsupported.** The two/three-day versus ten-minute comparison is not a valid general developmental threshold. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 4:** Explosive rage, violence, and destruction are core ADHD symptoms caused by hyperactivity rather than the child's own anger

**Verdict: Unsupported.** Rage and violence are not core hyperactivity symptoms with this established cause. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **2**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **2 / 4 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 236

**Title:** ADHD coach explains how your diet worsens your ADHD symptoms #adhd #adhdawareness #adhdkids  
**URL:** https://www.youtube.com/shorts/pp5vRw9UkYg  
**Views:** 524  
**Likes:** 10  
**Comments:** 0  
**Duration (seconds):** 41

**Transcript:**

> there was a study Again by bore at Al and he talks about how obviously a diet high in sugar a diet high in um you know processed foods which we are moving towards more and more you know in this modern world that we live in is directly related to worsening ADHD symptoms and you spoke about you know a high protein diet and how that's important where my expertise here would come in would be in terms of binge eating is another core morbidity of ADHD Right comes back to impulse control Right comes back to that

### Revised claim review

The named study attribution is unclear in the supplied text. No missing name or causal language was reconstructed.

**Claim 1 — clarified extraction:** Higher sugar/processed-food dietary patterns have been associated with ADHD symptoms.

*Original annotation wording:* A diet high in sugar and processed food directly worsens ADHD symptoms

**Verdict: Supported.** Directly related in the transcript is treated as an association, not proof of causation. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 2:** A high-protein diet is an important ADHD treatment

**Verdict: Unsupported.** A high-protein diet is not an established primary ADHD treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 3:** Binge-eating problems occur more often with ADHD and may relate partly to impulsivity

**Verdict: Supported.** An association; not an inevitable eating disorder. Evidence: [EATING](https://pubmed.ncbi.nlm.nih.gov/27859581/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **2**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **2 / 3 × 100 = 66.67%**.
- **Reviewed label: Label 2 — Slightly misleading** — see the limitation below.
- Original Markdown label: **Label 3 — Moderately misleading**.

**Decision limitation:** The supplied “directly related” language is treated as association, not proven causation. The unclear named-study attribution was not reconstructed.

---

## Video 237

**Title:** Does my Child have ADHD? | Child ADHD Test  
**URL:** https://www.youtube.com/shorts/BGnez2Eg3M8  
**Views:** 5,687  
**Likes:** 0  
**Comments:** 4  
**Duration (seconds):** 52

**Transcript:**

> ladhd test ADHD in children is a neurodevelopmental disorder characterized by difficulties with attention hyperactivity and impulsivity which can affect their daily functioning and behavior answer these five simple questions to find out if your child may have ADHD does your child often have difficulty paying attention to details and making careless mistakes does your child frequently have trouble staying focused on tasks does your child frequently seem forgetful or easily distracted does your child frequently display excessive levels of energy does your child often struggle with following instructions organizing tasks or completing assignments if you answered yes to three or more questions your child may have ADHD get comprehensive child ADHD test available in the comments section

**Transcription note:** Tactiq initially returned no transcript; one delayed retry succeeded.

### Revised claim review

The illustrative questions are assessed together as a screening-rule claim, not counted as five additional diagnoses.

**Claim 1:** Childhood ADHD is a neurodevelopmental disorder involving impairing inattention and/or hyperactivity-impulsivity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 2:** Answering “yes” to three of these five questions means a child may have ADHD

**Verdict: Unsupported.** The invented three-of-five cutoff is not a validated diagnostic threshold. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

### Revised result

- Eligible fact-checkable claims: **2**
- Supported: **1**; unsupported: **1**; excluded: **0**.
- Supported-claim percentage: **1 / 2 × 100 = 50.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 238

**Title:** Can treating anxiety help with ADHD symptoms? #adhd  
**URL:** https://www.youtube.com/shorts/3QKpTCK4yio  
**Views:** 245  
**Likes:** 1  
**Comments:** 0  
**Duration (seconds):** 67

**Transcript:**

> When you try to look at the symptoms of anxiety in general, they can feel very similar. And having too much to do can create anxiety because you just don't feel that you can stay calm and focused long enough to complete a task. So that pretty much is what anxiety does to us. So, can calming anxiety help with the symptoms of ADHD? And I've seen it happen a lot. It can. So, if you're already feeling anxious that you're not able to complete basic tasks like laundry, getting meals ready, getting the kids to school or or yourself to appointments on time. that can create anxiety and selfbullying and it also shifts you into what we call the survival state. So,

### Revised claim review

**Claim 1:** Anxiety can resemble or worsen concentration and task-completion difficulties that also occur in ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 2:** Repeated difficulty completing everyday responsibilities can generate anxiety and harsh self-criticism

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Treating co-occurring anxiety can improve some difficulties experienced by a person with ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 239

**Title:** Treating ADHD + Major Depression â€” Smarter Strategies  
**URL:** https://www.youtube.com/shorts/Lem1e_m6zKc  
**Views:** 1,375  
**Likes:** 35  
**Comments:** 2  
**Duration (seconds):** 50

**Transcript:**

> about the treatment of ADHD and major depressive disorder together. Now, this is something that can happen and does occur clinically. So, what can you do in those cases? I want to choose a medication that's going to treat both disorders. So, I can choose adamoxitine. I can choose as the serotonin norepinephrine re-uptake inhibitors. They have evidence to support their use in both major depressive disorder as well as ADHD. So you could you can use either of those choices to treat both disorders. Now if you want to go with a different medication, you can use the dopamine norepinephrine reuptake inhibitor buproprion. That also is a very good option here because it has evidence to support its use in both major depressive disorder as well as ADHD.

### Revised claim review

**Claim 1:** Atomoxetine is an evidence-based medication that can treat both ADHD and major depressive disorder

**Verdict: Unsupported.** Atomoxetine is not established treatment for major depressive disorder. Evidence: [ATMDD](https://pubmed.ncbi.nlm.nih.gov/17822337/).

**Claim 2:** Serotonin-norepinephrine reuptake inhibitors can generally be selected to treat both ADHD and major depressive disorder

**Verdict: Unsupported.** SNRIs as a class are not established dual ADHD/MDD treatment. Evidence: [COMDEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

**Claim 3:** Bupropion has evidence for major depressive disorder and may also help adult ADHD

**Verdict: Supported.** Possible off-label ADHD benefit with low-certainty evidence, alongside established depression use. Evidence: [BUP](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **1**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **1 / 3 × 100 = 33.33%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 240

**Title:** What Skipping Breakfast Does To ADHD Symptoms  
**URL:** https://www.youtube.com/shorts/0RcR0Fufluc  
**Views:** 6,780  
**Likes:** 440  
**Comments:** 31  
**Duration (seconds):** 106

**Transcript:**

> Skipping breakfast doesn't affect every brain the same way. The ADHD prefrontal cortex already uses glucose less efficiently than a neurotypical brain, and skipping that first meal makes the gap even worse. Glucose is the brain's primary fuel, and the prefrontal cortex, the area responsible for focus, impulse control, and emotional regulation is the most metabolically demanding region in the brain. Research shows that ADHD brains use glucose differently in regions tied to attention and impulse control, meaning the ADHD brain doesn't process fuel as efficiently in the exact area responsible for focus and self-regulation. That's part of why it feels drops in blood sugar faster and harder than a neurotypical brain. So, when an ADHD brain goes 10 to 14 hours overnight without food and doesn't refuel in the morning, you're asking an already inefficient system to perform on empty. What follows looks a lot like ADHD symptoms, but turned up. Your irritability, brain fog, emotional reactivity. Low blood sugar produces nearly the same symptom profile as ADHD itself, and cortisol rises to compensate, putting the nervous system into a stress state that further compromises focus. For an ADHD child, this often looks like a meltdown by 10:00 a.m. or complete disengagement at school. The behavior gets labeled, but the biology gets ignored. So, a few things that actually work with ADHD kids in the morning. Lead with protein and fat, not cereal or toast alone. Protein and fat both stabilize blood sugar for hours, while refined carbs spike it and crash it. If your child isn't hungry first thing, that's normal for ADHD. Try something small and easy, like a smoothie with protein powder and nut butter, a hard-boiled egg, or even leftover dinner. Food doesn't have to look like breakfast to count as breakfast. What's worked in your house for getting kids to eat in the morning? Comment below.

**Transcription note:** Tactiq initially returned no transcript; one delayed retry succeeded.

### Revised claim review

**Claim 1:** The ADHD prefrontal cortex generally uses glucose less efficiently than a neurotypical brain, and breakfast skipping widens this metabolic gap

**Verdict: Unsupported.** The proposed general glucose-metabolism gap and breakfast effect are not established. Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Glucose is a major fuel for the brain and the prefrontal cortex contributes to attention, impulse control, and emotional regulation

**Verdict: Supported.** Evidence: [STIM](https://www.nature.com/articles/1301164), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 3:** People with ADHD feel blood-sugar drops faster and more severely than neurotypical people

**Verdict: Unsupported.** The asserted comparative sensitivity to glucose drops is not established. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 4:** Overnight fasting followed by breakfast skipping predictably amplifies ADHD symptoms because low blood sugar produces nearly the same symptom profile and raises cortisol

**Verdict: Unsupported.** The predictable causal sequence is not established. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 5:** Breakfast skipping typically causes an ADHD child's mid-morning meltdown or school disengagement

**Verdict: Unsupported.** Typical mid-morning meltdown causation is not established. Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 6:** A breakfast containing protein and fat can produce steadier post-meal energy than refined carbohydrate alone

**Verdict: Supported.** Evidence: [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 7:** Lack of appetite first thing in the morning is normal for ADHD itself

**Verdict: Unsupported.** Appetite varies and medication can suppress it; this is not established as normal for ADHD itself. Evidence: [ADDXR](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 8 — added from supplied transcript:** The prefrontal cortex is the most metabolically demanding brain region.

**Verdict: Unsupported.** The asserted regional metabolic ranking was not established. Evidence: [STIM](https://www.nature.com/articles/1301164).

### Revised result

- Eligible fact-checkable claims: **8**
- Supported: **2**; unsupported: **6**; excluded: **0**.
- Supported-claim percentage: **2 / 8 × 100 = 25.00%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 241

**Title:** Subtle/hidden signs of adhd. #adhdsigns #adhdawareness #adhd  
**URL:** https://www.youtube.com/shorts/2_X6xxckK20  
**Views:** 493  
**Likes:** 0  
**Comments:** 1  
**Duration (seconds):** 55

**Transcript:**

> what are some subtle signs that you have ADHD one of the biggest signs is that whenever you start a task you tend to switch over to doing something else because you get distracted halfway through and the cycle typically repeats over and over until you've done like seven other tasks that you weren't supposed to do so for example you might start doing the dishes and you might realize oh wait I also need to do my laundry might as well get that started and then while you're kind of going to do your laundry you'll end up finding a pair of jeans that you completely forgot existed and then you'll realize oh you need to kind of put this on an outfit that you have and then you'll start Googling stuff on Pinterest and it's all over at that point another subtle sign is if you constantly like chew up straws cups anything that's in your hands will get torn Reds it is impossible for me to not chew on a straw or to not rip up any little piece of paper that's given to me or fold it up into a ton of little small pieces this is because restlessness and hyperactivity is a very common symptom and fidgeting is a very good way for us to typically get out a lot of our hyperactivity without us really realizing it this is often times something that we don't even think about doing we just start doing it and then people will comment on it and that's when we'll be like oh I didn't even realize I just ate half of the straw hope these help thank you for watching and take care

### Revised claim review

**Claim 1:** Repeatedly abandoning one task for another because of distraction can be a sign of ADHD

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2 — clarified extraction:** Repetitive chewing, tearing or folding objects can occur as fidgeting or related repetitive behaviour in ADHD.

*Original annotation wording:* Constantly chewing straws or cups and tearing or folding anything held are subtle signs that a person has ADHD

**Verdict: Supported.** Possible repetitive/fidget behaviours, not sufficient or unique diagnostic signs. Evidence: [BFRB](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/), [BFRBCO](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552165/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Fidgeting can be an expression of restlessness or hyperactivity that happens with little conscious awareness

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 242

**Title:** Autistic/ADHD Burnout Signs #autism #adhd  
**URL:** https://www.youtube.com/shorts/53pfZO461lM  
**Views:** 10,228  
**Likes:** 963  
**Comments:** 28  
**Duration (seconds):** 76

**Transcript:**

> A common consequence for late diagnosed autistic and ADHD people is neurode divergent burnout. This is when the demands of life and the lack of support catch up with our body and our brains. However, it's possible to be in burnout and not necessarily realize you're in burnout. You might think that you are experiencing, say, depression or a physical illness. So, I'm going to share some of the common signs of autistic and ADHD burnout so that if you notice any of those signs, you know kind of what direction to look in for support. Constant exhaustion even after you've rested. Headaches. Body aches. Increased sensory sensitivities which might make us feel like we can't leave the house without becoming overwhelmed. Brain fog. Forgetfulness. Losing your words mid-sentence. Finding tasks that you could previously easily do. Impossible. Anxiety. Irritability. Even less tolerance for change. Withdrawing from social contact or no longer finding the things that used to give you joy enjoyable. More frequent meltdowns. More frequent shutdowns. more frequent sensory overloads. Burnout isn't a personal failure. It's a sign that the load has been too heavy for too long. And also, when you're in burnout, it can feel like maybe you're just permanently going to be like this. So, don't panic. You can recover from it and you can build a life that works for you and is less likely to lead to burnout.

**Transcription note:** Tactiq initially returned no transcript; one delayed retry succeeded.

### Revised claim review

**Claim 1:** Prolonged demands and inadequate support can contribute to a burnout-like state in late-diagnosed autistic or ADHD people

**Verdict: Supported.** Evidence: [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 2:** Burnout-like exhaustion can be confused with depression or physical illness

**Verdict: Supported.** Overlap does not exclude depression or medical illness. Evidence: [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/).

**Claim 3 — clarified extraction:** Burnout-like states in autistic or ADHD people may involve exhaustion, reduced functioning, sensory overload and emotional or cognitive difficulties.

*Original annotation wording:* Exhaustion, headaches, body aches, sensory sensitivity, brain fog, word-finding difficulty, anxiety, irritability, withdrawal, and more meltdowns form a reliable sign list for autistic or ADHD burnout

**Verdict: Supported.** The transcript presents possible experiences, not a reliable validated test. Evidence is stronger for autistic burnout than a distinct ADHD-burnout syndrome. Evidence: [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** Recovery is possible and reducing sustained demands while increasing appropriate support may help

**Verdict: Supported.** Recovery is possible, not guaranteed on a fixed timetable. Evidence: [BURN](https://pubmed.ncbi.nlm.nih.gov/32851204/), [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate** — see the limitation below.
- Original Markdown label: **Label 2 — Slightly misleading**.

**Decision limitation:** The described experiences are treated as possible associated burnout-like difficulties. Evidence is stronger for autistic burnout than for a distinct ADHD-burnout syndrome; the list is not a validated test.

---

## Video 243

**Title:** Signs of ADHD in Adults You Might Overlook #mentalhealth   #adhdawareness  #mentalwellness #adhd  
**URL:** https://www.youtube.com/shorts/w9i6Obj-UyE  
**Views:** 755  
**Likes:** 8  
**Comments:** 0  
**Duration (seconds):** 37

**Transcript:**

> ADHD isn't just for kids. It affects adults, too. Here are three signs that you may be overlooking. Sign number one, difficulty prioritizing tasks. You might feel overwhelmed by to-do list or you might be procrastinating on important task. Second sign, forgetfulness in daily life. Do you frequently misplace your keys or forget appointments? This isn't just being a scatterbrain. It could be a symptom of ADHD. Sign number three, troubles regulating emotions. Intense emotions like frustrations and irritability can be harder to manage.

### Revised claim review

**Claim 1:** ADHD can persist into adulthood

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 2:** Difficulty prioritizing, procrastination, forgetfulness, losing items, and missing appointments can be adult ADHD features

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** Adults with ADHD may have greater difficulty regulating frustration, irritability, and other intense emotions

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 244

**Title:** ADHD Symptoms Quiz: Do You Have ADHD? Doctor Explains the Warning Signs #ADHD | Doctor Explains  
**URL:** https://www.youtube.com/shorts/Rp-yx6UGTsU  
**Views:** 245  
**Likes:** 0  
**Comments:** 0  
**Duration (seconds):** 54

**Transcript:**

> Have you ever found yourself struggling [music] to focus? You find yourself starting one task and easily getting distracted by another task. These are very common symptoms [music] that my patients have come to see me about. In this video, I'm going to go through a quick quiz, [music] which will help you to spot the signs and symptoms of ADHD. ADHD stands for attention [music] deficit hyperactivity disorder. ADHD is more than just difficulty paying [music] attention. It's a complex neurodevelopmental condition [music] that affects both children and adults. Many people experience symptoms of inattention or difficulty focusing. For a person with ADHD, it generally has a larger impact >> [music] >> and it happens much more often. It can have a significant impact on their work, studies, relationships. So, that's why it's important [music] to be aware of the condition and the symptoms.

### Revised claim review

**Claim 1:** ADHD stands for attention-deficit/hyperactivity disorder and is a neurodevelopmental condition affecting children and adults

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 2:** Difficulty sustaining focus and being easily distracted can be ADHD symptoms

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

**Claim 3:** In ADHD, symptoms occur more frequently and produce greater impairment in work, study, or relationships than ordinary lapses of attention

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 245

**Title:** How I Treat ADHD Without Meds (As A Psychiatrist)  
**URL:** https://www.youtube.com/shorts/EUKNGT8Iag4  
**Views:** 9,516  
**Likes:** 141  
**Comments:** 6  
**Duration (seconds):** 61

**Transcript:**

> saw a 16-year-old kid and the family was referred to us for ADHD treatment. And they had tried a couple of supplements with like some success, but the kid didn't really believe in them. And so we did a whole evaluation, right? And so I definitely think that he has ADHD like for sure. Inattention symptoms, some hyperactivity, but also a lot of impulsivity, some of the substance use associated with that, and a lot of irritability outbursts too associated. And so um you know, what we came to realize was that a lot of his diet that he was eating was like cheeseburgers and fries and um diet sodas, right? Drinking a lot of not a lot of alcohol, but was drinking some alcohol, right? Smoking some MJ as well. And uh sleep-wise, I think he was getting maybe decent sleep like 7-8 hours, but not like the 9 or 10 that kids need. And

**Transcription note:** Tactiq initially returned no transcript; one delayed retry succeeded.

### Revised claim review

**Claim 1:** ADHD can involve inattention, hyperactivity, and impulsivity

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Substance use and irritability outbursts can be associated with adolescent ADHD

**Verdict: Supported.** Evidence: [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [ED](https://pubmed.ncbi.nlm.nih.gov/32164655/).

**Claim 3:** A 16-year-old generally needs about nine or ten hours of sleep

**Verdict: Supported.** Nine to ten hours is within the recommended eight-to-ten-hour teen range, not an identical requirement for everyone. Evidence: [TEENSLEEP](https://pmc.ncbi.nlm.nih.gov/articles/PMC5078711/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **3**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **3 / 3 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 246

**Title:** 6 Natural Remedies To Support ADHD In Kids  
**URL:** https://www.youtube.com/shorts/ldr41Y_KKL0  
**Views:** 205,378  
**Likes:** 4,766  
**Comments:** 81  
**Duration (seconds):** 73

**Transcript:**

> what are some of the natural ways for treating ADHD in children number one diet make sure their diet consists of High Protein healthy fiber healthy fats whole grains and try to eliminate pro-inflammatory food such as gluten dairy and sugar number two hydration make sure they getting plenty of water without any added sugar or caffeine number three sleep make sure they are on a structured routine and regimen so they are getting a good quality and quantity of Sleep Number Four getting plenty of outdoor exercise sunlight reducing screen time and getting them to start incorporating yoga and deep breathing number five behavior strategies and intervention it is most important for parents to acknowledge good behavior and praise them for their good behavior and try to give them directions which are small and discreet which can be done easily last but not the least you want to make sure your child's diet is supplemented with high quality multivitamins and fish oil my name is Dr Niha kinara and I am one of the Child and Adolescent psychiatrist here at Aman Clinic specializing in ADHD

### Revised claim review

**Claim 1:** A balanced diet, adequate hydration, consistent sleep, and regular physical activity can support the health and functioning of a child with ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 2:** Children with ADHD should eliminate gluten, dairy, and sugar because these are pro-inflammatory causes of symptoms

**Verdict: Unsupported.** Blanket dietary elimination and inflammatory causation are not supported. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 3:** Outdoor activity, reduced excessive screen exposure, yoga, and breathing exercises may help with regulation

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 4:** Praising desired behaviour and giving brief, manageable directions are useful behavioural strategies

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

**Claim 5:** Every child with ADHD should receive high-quality multivitamins and fish-oil supplements

**Verdict: Unsupported.** Universal multivitamin/fish-oil prescribing is not established ADHD care. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/), [PUFA](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children).

### Revised result

- Eligible fact-checkable claims: **5**
- Supported: **3**; unsupported: **2**; excluded: **0**.
- Supported-claim percentage: **3 / 5 × 100 = 60.00%**.
- **Reviewed label: Label 2 — Slightly misleading**
- Original Markdown label: **Label 2 — Slightly misleading**.

---

## Video 247

**Title:** Avoid These 3 Foods If You Have ADHD  
**URL:** https://www.youtube.com/shorts/hVl9srUL9pQ  
**Views:** 68,266  
**Likes:** 2,513  
**Comments:** 89  
**Duration (seconds):** 29

**Transcript:**

> if you have ADHD here are three foods that you should absolutely avoid number one sugar especially refined sugar or added sugar if the label says added sugar or cane sugar or anything like that get it out of your pantry number two artificial dieses artificial dies have been shown in study after study to worsen symptoms of ADHD and number three processed food my rule of thumb in our house is if I read the label and I can't pronounce what's in it it's out

**Duplicate note:** This URL duplicates video 130 and retains the same claim assessment while preserving the current metadata snapshot.

### Revised claim review

Updated under the author’s literal-wording instruction on 9 September 2026. Explicit categorical wording is scored without inferring a softer intended meaning. Unchanged claims retain the preceding evidence review.

**Claim 1:** Every person with ADHD should avoid refined or added sugar

**Verdict: Unsupported.** Complete sugar avoidance for everyone is not established ADHD care. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

**Claim 2:** People with ADHD should absolutely avoid artificial dyes because studies show that they worsen ADHD symptoms.

*Original annotation wording:* Artificial food colours can worsen ADHD-related behaviour

**Verdict: Unsupported.** The earlier extraction retained only possible behavioural effects. The stated blanket avoidance recommendation is not supported as generally applicable ADHD treatment. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [ELIM](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/).

**Claim 3:** People with ADHD should avoid processed food whenever an ingredient name is difficult to pronounce

**Verdict: Unsupported.** Pronounceability is not a safety or efficacy criterion. Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [DIET](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/).

### Revised result

- Eligible fact-checkable claims: **3**
- Supported: **0**; unsupported: **3**; excluded: **0**.
- Supported-claim percentage: **0/3 × 100 = 0.00%**.
- **Reviewed label: Label 4 — Highly misleading**
- Previous reviewed label: **Label 3**.
- Uploaded CSV label: **Label 3**.

---

## Video 248

**Title:** Ask a Pharmacist: What ADHD Medication Is Right for Me?  
**URL:** https://www.youtube.com/shorts/aTg3BYrbL-Q  
**Views:** 13,933  
**Likes:** 169  
**Comments:** 0  
**Duration (seconds):** 37

**Transcript:**

> choosing an ADHD medication there are two main types of medication used to treat ADHD stimulants and non-stimulants for most adults with ADHD treatment with a stimulant is generally the first step for children the best ADHD treatment involves a combination of parent and child behavior therapy school interventions and if necessary medication the best ADHD medication for you or your child depends on your individual circumstances it may take patience and trial and error to find the fit talk to your provider and your pharmacist to discuss your options and medication availability

### Revised claim review

**Claim 1:** ADHD medicines are commonly divided into stimulant and non-stimulant options

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 2:** A stimulant is generally a first-line medication option for most adults with ADHD

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 3:** Childhood ADHD care may combine parent or child behavioural intervention, school support, and medication when indicated

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

**Claim 4:** Selecting an ADHD medication is individualized and may require monitored trial and adjustment with a prescriber

**Verdict: Supported.** Evidence: [NICE](https://www.ncbi.nlm.nih.gov/books/NBK493361/), [AAP](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Video 249

**Title:** What is HYPERACTIVE ADHD?  
**URL:** https://www.youtube.com/shorts/a8WtC3pndMM  
**Views:** 735  
**Likes:** 29  
**Comments:** 0  
**Duration (seconds):** 58

**Transcript:** Unavailable

**Status:** # tactiq.io free youtube transcript
# What is HYPERACTIVE ADHD?
# https://www.youtube.com/watch/a8WtC3pndMM

00:00:00.000 One of the rarest forms of ADHD's
00:00:01.720 hyperactive only ADHD. Most people have
00:00:04.520 either hyperactive and inattentive ADHD,
00:00:06.800 which is called combined or mixed ADHD,
00:00:09.120 or they have inattentive only.
00:00:11.040 Inattentive is what we think of when we
00:00:12.560 typically think of ADHD. So, struggling
00:00:14.560 with organizations, struggling to
00:00:16.040 remember things, spacing out during
00:00:17.600 conversations, stuff like that. But
00:00:19.400 hyperactive ADHD is the other side of
00:00:21.720 ADHD, where you're constantly moving,
00:00:23.360 you constantly need to be doing
00:00:24.400 something, you constantly have really
00:00:25.720 impulsive decisions, you can't wait for
00:00:27.720 other people to finish talking before
00:00:29.200 you start talking. And people with
00:00:30.880 hyperactive only have only those traits
00:00:33.200 and none of the inattentive traits. So,
00:00:34.720 they often don't get flagged for ADHD.
00:00:37.160 Because they're not struggling to get
00:00:38.200 stuff done, they're not really going to
00:00:39.680 be procrastinating very often, they have
00:00:41.360 clean rooms. But the difficulty comes
00:00:43.440 from the fact that they are always on,
00:00:45.160 always on the go, and they can never
00:00:46.760 stop to rest or relax. With this subtype
00:00:49.240 of ADHD, while you get a lot more done,
00:00:51.080 you do tend to burn out very, very often
00:00:53.520 and way more easily. If you have this
00:00:55.200 subtype, comment your experiences down
00:00:56.840 below.

### Revised claim review

**Claim 1:** Predominantly hyperactive-impulsive ADHD is one of the rarer presentations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 2:** Most people with ADHD have either the predominantly inattentive or combined presentation

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 3:** Predominantly inattentive ADHD can involve disorganization, forgetfulness, and appearing to space out during conversations

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 4:** Predominantly hyperactive-impulsive ADHD can involve excessive movement, feeling driven to remain active, impulsive decisions, difficulty waiting, and interrupting

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 5:** People with the predominantly hyperactive-impulsive presentation have no inattentive traits whatsoever

**Verdict: Unsupported.** Predominantly does not mean complete absence of inattentive traits. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 6:** People with this presentation are often overlooked because they complete tasks, rarely procrastinate, and maintain clean rooms

**Verdict: Unsupported.** The clean-room/task-completion profile is not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 7:** People with predominantly hyperactive-impulsive ADHD may feel continuously active, “on the go,” or unable to relax

**Verdict: Supported.** Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 8:** People with this presentation generally accomplish more than other people

**Verdict: Unsupported.** Greater accomplishment is not established for this presentation. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

**Claim 9:** This presentation causes people to burn out much more frequently and easily

**Verdict: Unsupported.** The claimed comparative burnout frequency is not established. Evidence: [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria), [CONS](https://pubmed.ncbi.nlm.nih.gov/33549739/), [WORK](https://link.springer.com/article/10.1186/s12888-022-04409-w).

### Revised result

- Eligible fact-checkable claims: **9**
- Supported: **5**; unsupported: **4**; excluded: **0**.
- Supported-claim percentage: **5 / 9 × 100 = 55.56%**.
- **Reviewed label: Label 3 — Moderately misleading**
- Original Markdown label: **Label 3 — Moderately misleading**.

---

## Video 250

**Title:** The Hidden Signs of ADHD in Girls: Why Theyâ€™re Often Missed  
**URL:** https://www.youtube.com/shorts/0ScyPCNk0So  
**Views:** 1,810  
**Likes:** 47  
**Comments:** 0  
**Duration (seconds):** 52

**Transcript:**

> why do girls with ADHD so often go unnoticed it's partly because their symptoms are subtle and often internalized imagine a girl who's daydreaming during class taking extra time on assignments or appearing well behaved but struggling to keep up on progress reports she's described as bright but needs to try harder masking the underlying challenges she faces even girls who exhibit hyperactive traits often work harder to fit societal expectations suppressing their struggles to avoid standing out this masking Behavior makes it harder for teachers parents and even doctors to recognize ADHD and girls it's not just about being distracted it's about a constant effort to keep up while battling an invisible challenge by spreading awareness of these hidden signs we can break the cycle and help girls with ADHD get the diagnosis and support they deserve

### Revised claim review

**Claim 1:** Girls with ADHD are often overlooked partly because their symptoms may be less externally disruptive or more internalized

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 2:** Daydreaming, taking unusually long on assignments, and appearing well behaved while struggling can be signs of ADHD in girls

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 3:** Some girls suppress or compensate for difficulties to meet social expectations, making ADHD harder for adults and clinicians to recognize

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

**Claim 4:** Better awareness of less visible presentations can help affected girls receive appropriate assessment and support

**Verdict: Supported.** Evidence: [FEMALE](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/), [DSM](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria).

### Revised result

- Eligible fact-checkable claims: **4**
- Supported: **4**; unsupported: **0**; excluded: **0**.
- Supported-claim percentage: **4 / 4 × 100 = 100.00%**.
- **Reviewed label: Label 1 — Accurate**
- Original Markdown label: **Label 1 — Accurate**.

---

## Preservation and arithmetic verification

250 ordered video sections are retained. The recorded ledger contains 786 supported assertions, 388 unsupported assertions and 58 excluded items. Every CSV label and count is computed from that ledger. All 250 supplied Markdown preambles are retained, and all 250 CSV transcript cells match the reviewed wording after whitespace normalization. Original CSV metadata and the 241 unrelated transcript cells are preserved exactly as parsed cell values.

## Complete current label register

| Video | Eligible | Supported | Unsupported | Excluded | Label |
|---:|---:|---:|---:|---:|---|
| 1 | 8 | 8 | 0 | 0 | Label 1 |
| 2 | 6 | 1 | 5 | 0 | Label 3 |
| 3 | 8 | 0 | 8 | 0 | Label 4 |
| 4 | 7 | 5 | 2 | 0 | Label 2 |
| 5 | 5 | 1 | 4 | 1 | Label 3 |
| 6 | 5 | 5 | 0 | 1 | Label 1 |
| 7 | 5 | 0 | 5 | 1 | Label 4 |
| 8 | 4 | 3 | 1 | 0 | Label 2 |
| 9 | 6 | 5 | 1 | 0 | Label 1 |
| 10 | 4 | 3 | 1 | 0 | Label 2 |
| 11 | 10 | 0 | 10 | 0 | Label 4 |
| 12 | 13 | 8 | 5 | 0 | Label 2 |
| 13 | 6 | 5 | 1 | 0 | Label 1 |
| 14 | 8 | 5 | 3 | 0 | Label 2 |
| 15 | 9 | 7 | 2 | 0 | Label 2 |
| 16 | 4 | 4 | 0 | 0 | Label 1 |
| 17 | 4 | 3 | 1 | 1 | Label 2 |
| 18 | 3 | 3 | 0 | 2 | Label 1 |
| 19 | 2 | 2 | 0 | 0 | Label 1 |
| 20 | 12 | 12 | 0 | 0 | Label 1 |
| 21 | 10 | 10 | 0 | 0 | Label 1 |
| 22 | 8 | 7 | 1 | 0 | Label 1 |
| 23 | 6 | 1 | 5 | 1 | Label 3 |
| 24 | 11 | 2 | 9 | 0 | Label 3 |
| 25 | 3 | 2 | 1 | 0 | Label 2 |
| 26 | 6 | 6 | 0 | 0 | Label 1 |
| 27 | 9 | 9 | 0 | 0 | Label 1 |
| 28 | 3 | 3 | 0 | 1 | Label 1 |
| 29 | 4 | 1 | 3 | 0 | Label 3 |
| 30 | 6 | 4 | 2 | 0 | Label 2 |
| 31 | 7 | 1 | 6 | 0 | Label 4 |
| 32 | 10 | 10 | 0 | 0 | Label 1 |
| 33 | 2 | 2 | 0 | 0 | Label 1 |
| 34 | 15 | 13 | 2 | 0 | Label 1 |
| 35 | 5 | 2 | 3 | 0 | Label 3 |
| 36 | 6 | 5 | 1 | 0 | Label 1 |
| 37 | 8 | 8 | 0 | 1 | Label 1 |
| 38 | 4 | 1 | 3 | 0 | Label 3 |
| 39 | 3 | 2 | 1 | 1 | Label 2 |
| 40 | 2 | 1 | 1 | 0 | Label 3 |
| 41 | 2 | 0 | 2 | 0 | Label 4 |
| 42 | 3 | 0 | 3 | 1 | Label 4 |
| 43 | 2 | 2 | 0 | 0 | Label 1 |
| 44 | 5 | 5 | 0 | 0 | Label 1 |
| 45 | 6 | 6 | 0 | 0 | Label 1 |
| 46 | 6 | 6 | 0 | 0 | Label 1 |
| 47 | 7 | 6 | 1 | 0 | Label 1 |
| 48 | 4 | 1 | 3 | 0 | Label 3 |
| 49 | 4 | 2 | 2 | 0 | Label 3 |
| 50 | 4 | 4 | 0 | 1 | Label 1 |
| 51 | 4 | 4 | 0 | 0 | Label 1 |
| 52 | 5 | 4 | 1 | 1 | Label 1 |
| 53 | 3 | 1 | 2 | 1 | Label 3 |
| 54 | 3 | 3 | 0 | 0 | Label 1 |
| 55 | 4 | 4 | 0 | 0 | Label 1 |
| 56 | 3 | 3 | 0 | 0 | Label 1 |
| 57 | 2 | 0 | 2 | 1 | Label 4 |
| 58 | 0 | 0 | 0 | 5 | Unlabelled |
| 59 | 4 | 3 | 1 | 0 | Label 2 |
| 60 | 3 | 1 | 2 | 1 | Label 3 |
| 61 | 4 | 4 | 0 | 0 | Label 1 |
| 62 | 4 | 4 | 0 | 0 | Label 1 |
| 63 | 3 | 2 | 1 | 1 | Label 2 |
| 64 | 9 | 4 | 5 | 0 | Label 3 |
| 65 | 4 | 2 | 2 | 1 | Label 3 |
| 66 | 4 | 4 | 0 | 0 | Label 1 |
| 67 | 2 | 2 | 0 | 0 | Label 1 |
| 68 | 9 | 7 | 2 | 0 | Label 2 |
| 69 | 8 | 5 | 3 | 0 | Label 2 |
| 70 | 6 | 1 | 5 | 0 | Label 3 |
| 71 | 3 | 0 | 3 | 0 | Label 4 |
| 72 | 6 | 6 | 0 | 0 | Label 1 |
| 73 | 8 | 3 | 5 | 0 | Label 3 |
| 74 | 8 | 7 | 1 | 0 | Label 1 |
| 75 | 4 | 1 | 3 | 0 | Label 3 |
| 76 | 6 | 0 | 6 | 0 | Label 4 |
| 77 | 5 | 5 | 0 | 0 | Label 1 |
| 78 | 3 | 3 | 0 | 3 | Label 1 |
| 79 | 2 | 2 | 0 | 2 | Label 1 |
| 80 | 8 | 7 | 1 | 0 | Label 1 |
| 81 | 13 | 7 | 6 | 0 | Label 3 |
| 82 | 3 | 0 | 3 | 0 | Label 4 |
| 83 | 5 | 0 | 5 | 0 | Label 4 |
| 84 | 9 | 6 | 3 | 0 | Label 2 |
| 85 | 3 | 3 | 0 | 0 | Label 1 |
| 86 | 2 | 2 | 0 | 0 | Label 1 |
| 87 | 3 | 0 | 3 | 0 | Label 4 |
| 88 | 5 | 3 | 2 | 0 | Label 2 |
| 89 | 4 | 2 | 2 | 0 | Label 3 |
| 90 | 6 | 5 | 1 | 0 | Label 1 |
| 91 | 7 | 3 | 4 | 0 | Label 3 |
| 92 | 4 | 2 | 2 | 0 | Label 3 |
| 93 | 6 | 3 | 3 | 0 | Label 3 |
| 94 | 3 | 1 | 2 | 1 | Label 3 |
| 95 | 3 | 2 | 1 | 0 | Label 2 |
| 96 | 3 | 2 | 1 | 0 | Label 2 |
| 97 | 7 | 6 | 1 | 0 | Label 1 |
| 98 | 5 | 3 | 2 | 0 | Label 2 |
| 99 | 4 | 1 | 3 | 0 | Label 3 |
| 100 | 6 | 3 | 3 | 0 | Label 3 |
| 101 | 3 | 0 | 3 | 0 | Label 4 |
| 102 | 4 | 2 | 2 | 0 | Label 3 |
| 103 | 4 | 0 | 4 | 0 | Label 4 |
| 104 | 0 | 0 | 0 | 0 | Unlabelled |
| 105 | 2 | 1 | 1 | 0 | Label 3 |
| 106 | 13 | 13 | 0 | 0 | Label 1 |
| 107 | 6 | 2 | 4 | 0 | Label 3 |
| 108 | 5 | 3 | 2 | 0 | Label 2 |
| 109 | 6 | 5 | 1 | 0 | Label 1 |
| 110 | 7 | 1 | 6 | 0 | Label 4 |
| 111 | 3 | 3 | 0 | 0 | Label 1 |
| 112 | 11 | 7 | 4 | 0 | Label 2 |
| 113 | 1 | 1 | 0 | 5 | Unlabelled |
| 114 | 5 | 2 | 3 | 0 | Label 3 |
| 115 | 4 | 1 | 3 | 1 | Label 3 |
| 116 | 0 | 0 | 0 | 0 | Unlabelled |
| 117 | 2 | 2 | 0 | 0 | Label 1 |
| 118 | 6 | 4 | 2 | 0 | Label 2 |
| 119 | 4 | 2 | 2 | 0 | Label 3 |
| 120 | 7 | 0 | 7 | 1 | Label 4 |
| 121 | 3 | 3 | 0 | 0 | Label 1 |
| 122 | 3 | 3 | 0 | 0 | Label 1 |
| 123 | 4 | 4 | 0 | 1 | Label 1 |
| 124 | 3 | 3 | 0 | 0 | Label 1 |
| 125 | 5 | 2 | 3 | 0 | Label 3 |
| 126 | 5 | 0 | 5 | 0 | Label 4 |
| 127 | 4 | 2 | 2 | 0 | Label 3 |
| 128 | 4 | 3 | 1 | 0 | Label 2 |
| 129 | 4 | 3 | 1 | 0 | Label 2 |
| 130 | 3 | 1 | 2 | 0 | Label 3 |
| 131 | 7 | 6 | 1 | 0 | Label 1 |
| 132 | 4 | 4 | 0 | 0 | Label 1 |
| 133 | 8 | 6 | 2 | 0 | Label 2 |
| 134 | 5 | 2 | 3 | 0 | Label 3 |
| 135 | 2 | 2 | 0 | 0 | Label 1 |
| 136 | 4 | 2 | 2 | 0 | Label 3 |
| 137 | 5 | 3 | 2 | 0 | Label 2 |
| 138 | 2 | 2 | 0 | 1 | Label 1 |
| 139 | 5 | 5 | 0 | 0 | Label 1 |
| 140 | 6 | 6 | 0 | 1 | Label 1 |
| 141 | 4 | 1 | 3 | 0 | Label 3 |
| 142 | 0 | 0 | 0 | 1 | Unlabelled |
| 143 | 4 | 4 | 0 | 0 | Label 1 |
| 144 | 3 | 3 | 0 | 0 | Label 1 |
| 145 | 6 | 2 | 4 | 0 | Label 3 |
| 146 | 3 | 2 | 1 | 0 | Label 2 |
| 147 | 2 | 1 | 1 | 2 | Label 3 |
| 148 | 2 | 2 | 0 | 0 | Label 1 |
| 149 | 4 | 4 | 0 | 0 | Label 1 |
| 150 | 4 | 4 | 0 | 0 | Label 1 |
| 151 | 6 | 4 | 2 | 0 | Label 2 |
| 152 | 6 | 4 | 2 | 0 | Label 2 |
| 153 | 6 | 2 | 4 | 0 | Label 3 |
| 154 | 4 | 4 | 0 | 0 | Label 1 |
| 155 | 4 | 1 | 3 | 6 | Label 3 |
| 156 | 3 | 0 | 3 | 0 | Label 4 |
| 157 | 2 | 0 | 2 | 0 | Label 4 |
| 158 | 3 | 2 | 1 | 0 | Label 2 |
| 159 | 4 | 4 | 0 | 0 | Label 1 |
| 160 | 5 | 3 | 2 | 0 | Label 2 |
| 161 | 5 | 4 | 1 | 0 | Label 1 |
| 162 | 3 | 3 | 0 | 0 | Label 1 |
| 163 | 5 | 4 | 1 | 0 | Label 1 |
| 164 | 5 | 2 | 3 | 0 | Label 3 |
| 165 | 7 | 7 | 0 | 0 | Label 1 |
| 166 | 3 | 3 | 0 | 0 | Label 1 |
| 167 | 4 | 4 | 0 | 0 | Label 1 |
| 168 | 7 | 7 | 0 | 0 | Label 1 |
| 169 | 4 | 4 | 0 | 0 | Label 1 |
| 170 | 3 | 2 | 1 | 0 | Label 2 |
| 171 | 3 | 3 | 0 | 0 | Label 1 |
| 172 | 9 | 9 | 0 | 0 | Label 1 |
| 173 | 8 | 6 | 2 | 0 | Label 2 |
| 174 | 8 | 3 | 5 | 0 | Label 3 |
| 175 | 3 | 1 | 2 | 0 | Label 3 |
| 176 | 3 | 2 | 1 | 3 | Label 2 |
| 177 | 3 | 3 | 0 | 0 | Label 1 |
| 178 | 8 | 6 | 2 | 0 | Label 2 |
| 179 | 2 | 2 | 0 | 0 | Label 1 |
| 180 | 5 | 5 | 0 | 0 | Label 1 |
| 181 | 3 | 2 | 1 | 0 | Label 2 |
| 182 | 4 | 4 | 0 | 0 | Label 1 |
| 183 | 4 | 4 | 0 | 0 | Label 1 |
| 184 | 4 | 4 | 0 | 0 | Label 1 |
| 185 | 4 | 3 | 1 | 1 | Label 2 |
| 186 | 5 | 4 | 1 | 0 | Label 1 |
| 187 | 3 | 2 | 1 | 0 | Label 2 |
| 188 | 3 | 3 | 0 | 0 | Label 1 |
| 189 | 6 | 6 | 0 | 0 | Label 1 |
| 190 | 2 | 1 | 1 | 1 | Label 3 |
| 191 | 3 | 1 | 2 | 0 | Label 3 |
| 192 | 2 | 2 | 0 | 0 | Label 1 |
| 193 | 5 | 5 | 0 | 0 | Label 1 |
| 194 | 7 | 7 | 0 | 0 | Label 1 |
| 195 | 4 | 4 | 0 | 0 | Label 1 |
| 196 | 4 | 4 | 0 | 0 | Label 1 |
| 197 | 5 | 5 | 0 | 0 | Label 1 |
| 198 | 4 | 3 | 1 | 0 | Label 2 |
| 199 | 0 | 0 | 0 | 0 | Unlabelled |
| 200 | 5 | 1 | 4 | 0 | Label 3 |
| 201 | 7 | 6 | 1 | 0 | Label 1 |
| 202 | 3 | 1 | 2 | 0 | Label 3 |
| 203 | 4 | 4 | 0 | 0 | Label 1 |
| 204 | 5 | 5 | 0 | 0 | Label 1 |
| 205 | 4 | 4 | 0 | 0 | Label 1 |
| 206 | 4 | 1 | 3 | 0 | Label 3 |
| 207 | 4 | 3 | 1 | 0 | Label 2 |
| 208 | 1 | 1 | 0 | 1 | Unlabelled |
| 209 | 3 | 3 | 0 | 0 | Label 1 |
| 210 | 6 | 3 | 3 | 0 | Label 3 |
| 211 | 3 | 1 | 2 | 0 | Label 3 |
| 212 | 3 | 1 | 2 | 0 | Label 3 |
| 213 | 4 | 4 | 0 | 0 | Label 1 |
| 214 | 5 | 1 | 4 | 0 | Label 3 |
| 215 | 4 | 4 | 0 | 0 | Label 1 |
| 216 | 5 | 3 | 2 | 0 | Label 2 |
| 217 | 4 | 4 | 0 | 0 | Label 1 |
| 218 | 3 | 2 | 1 | 2 | Label 2 |
| 219 | 4 | 3 | 1 | 0 | Label 2 |
| 220 | 8 | 4 | 4 | 0 | Label 3 |
| 221 | 6 | 3 | 3 | 0 | Label 3 |
| 222 | 4 | 2 | 2 | 0 | Label 3 |
| 223 | 3 | 2 | 1 | 0 | Label 2 |
| 224 | 6 | 1 | 5 | 0 | Label 3 |
| 225 | 3 | 2 | 1 | 0 | Label 2 |
| 226 | 2 | 2 | 0 | 0 | Label 1 |
| 227 | 5 | 1 | 4 | 0 | Label 3 |
| 228 | 8 | 5 | 3 | 0 | Label 2 |
| 229 | 5 | 1 | 4 | 0 | Label 3 |
| 230 | 3 | 3 | 0 | 2 | Label 1 |
| 231 | 4 | 4 | 0 | 0 | Label 1 |
| 232 | 5 | 3 | 2 | 0 | Label 2 |
| 233 | 2 | 2 | 0 | 0 | Label 1 |
| 234 | 3 | 3 | 0 | 0 | Label 1 |
| 235 | 4 | 2 | 2 | 0 | Label 3 |
| 236 | 3 | 2 | 1 | 0 | Label 2 |
| 237 | 2 | 1 | 1 | 0 | Label 3 |
| 238 | 3 | 3 | 0 | 0 | Label 1 |
| 239 | 3 | 1 | 2 | 0 | Label 3 |
| 240 | 8 | 2 | 6 | 0 | Label 3 |
| 241 | 3 | 3 | 0 | 0 | Label 1 |
| 242 | 4 | 4 | 0 | 0 | Label 1 |
| 243 | 3 | 3 | 0 | 0 | Label 1 |
| 244 | 3 | 3 | 0 | 0 | Label 1 |
| 245 | 3 | 3 | 0 | 0 | Label 1 |
| 246 | 5 | 3 | 2 | 0 | Label 2 |
| 247 | 3 | 0 | 3 | 0 | Label 4 |
| 248 | 4 | 4 | 0 | 0 | Label 1 |
| 249 | 9 | 5 | 4 | 0 | Label 3 |
| 250 | 4 | 4 | 0 | 0 | Label 1 |

## Sources consulted

The earlier source registry is retained. Sources reopened for the literal-wording pass on 9 September 2026 were DSM, NICE (the public 2019 Bookshelf edition), STIM, WORK, HYPER, UPD_NIMH_ADULT and UPD_APA_MENTAL. LIT_STRENGTHS is newly added. The other source records retain their previous access dates; inclusion does not mean every full paper was reopened in this pass. Source presence and arithmetic verification do not establish independent clinical agreement.

- **DSM** — [American Academy of Pediatrics: DSM-5 Criteria](https://eqipp.aap.org/courses/adhd/mn/clinical-guide/popups/dsm-5-criteria). Public DSM-based criteria: two symptom domains, age-dependent thresholds, childhood onset, persistence, multiple settings and impairment. Informal symptom examples are not stand-alone diagnostic tests. Access recorded: 2026-09-06.
- **APA** — [American Psychiatric Association: What is ADHD?](https://www.psychiatry.org/patients-families/adhd/what-is-adhd). Clinical overview, diagnostic differential, adult examples, providers, associated low self-esteem and criticism sensitivity, and treatments. Access recorded: 2026-09-06.
- **NICE** — [NICE NG87: ADHD diagnosis and management (NCBI Bookshelf edition)](https://www.ncbi.nlm.nih.gov/books/NBK493361/). Clinical assessment, shared decisions, age-specific treatment, psychological interventions, diet and supplements, monitoring. Public September 2019 edition; do not represent this as a full 2026 update. Access recorded: 2026-09-06.
- **CONS** — [Faraone et al. (2021): World Federation of ADHD International Consensus Statement](https://pubmed.ncbi.nlm.nih.gov/33549739/). Evidence synthesis on diagnosis, causes, cognitive variability, associated impairment and treatment; abstract plus indexed full-text passages. Not proof of every social-media mechanism. Access recorded: 2026-09-06.
- **WM** — [Alderson et al. (2013): ADHD and working memory in adults, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/23688211/). Working-memory impairment can persist in adult ADHD; not a universal deficit. Access recorded: 2026-09-06.
- **MEM** — [Skodzik et al. (2017): Long-term memory performance in adult ADHD, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/24232170/). ADHD memory difficulties extend beyond working memory; encoding/learning can contribute. Access recorded: 2026-09-06.
- **DEPR** — [NIMH: Depression](https://www.nimh.nih.gov/health/publications/depression). Anhedonia, cognitive/concentration complaints, slowing, episodes and available treatments. Access recorded: 2026-09-06.
- **DEPRCOG** — [Kriesche et al. (2023): Cognitive impairment in acute and remitted major depression, systematic review](https://link.springer.com/article/10.1007/s00406-022-01479-5). Cognitive deficits can improve but can also persist during remission; memory recovery is not a reliable binary differential test. Access recorded: 2026-09-06.
- **ED** — [Beheshti et al. (2020): Emotion dysregulation in adults with ADHD, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/32164655/). Emotional lability and negative emotional responses are associated with ADHD, without becoming unique diagnostic criteria. Access recorded: 2026-09-06.
- **SLEEP** — [Coogan and McGowan (2017): Circadian function, chronotype and chronotherapy in ADHD, systematic review](https://pubmed.ncbi.nlm.nih.gov/28064405/). Evening preference and delayed circadian/sleep timing are associated with ADHD. This does not establish a threat-safety or revenge-bedtime mechanism. Access recorded: 2026-09-06.
- **RACING** — [Martz et al. (2023): Disentangling racing thoughts from mind wandering in adult ADHD](https://pubmed.ncbi.nlm.nih.gov/37731878/). Racing thoughts and mental restlessness occur in ADHD; they are not exclusive to bipolar disorder or a diagnostic test. Access recorded: 2026-09-06.
- **WORK** — [Oscarsson et al. (2022): Stress and work-related mental illness among working adults with ADHD](https://link.springer.com/article/10.1186/s12888-022-04409-w). Qualitative evidence of occupational stress, compensation and exhaustion. Does not measure a universal faster time to burnout. Access recorded: 2026-09-06.
- **CRIT** — [Beaton et al. (2022): Experiences of criticism in adults with ADHD](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0263366). Qualitative evidence of criticism, low self-esteem and emotional responses; cannot establish a universal RSD prevalence or a specific neural mechanism. Access recorded: 2026-09-06.
- **EATING** — [Nazar et al. (2016): Eating disorders comorbid with ADHD, systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/27859581/). Elevated association with eating disorders, including binge eating; not an ADHD diagnostic criterion or proof of a specific dopamine mechanism. Access recorded: 2026-09-06.
- **STIM** — [Arnsten (2006): Stimulants: Therapeutic Actions in ADHD](https://www.nature.com/articles/1301164). Therapeutic catecholamine modulation can improve prefrontal regulation in people with and without ADHD. Excessive stimulation can impair function. Access recorded: 2026-09-06.
- **CAFF** — [Perrotte et al. (2023): Effects of caffeine on main symptoms in children with ADHD, systematic review and meta-analysis](https://www.mdpi.com/2076-3425/13/9/1304). Randomized pediatric trials do not establish caffeine as an effective replacement for ADHD medication; adult calming and diagnostic claims cannot be inferred. Access recorded: 2026-09-06.
- **DRIVE** — [Vaa (2014): ADHD and relative risk of accidents in road traffic, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/24238842/). ADHD is associated with driving risks/citations; does not imply that every driver with ADHD always speeds. Access recorded: 2026-09-06.
- **CONSENT** — [NHS: Consent to treatment](https://www.nhs.uk/tests-and-treatments/consent-to-treatment/). Consent is the ordinary rule; emergency, incapacity and Mental Health Act exceptions disprove the unrestricted claim that nobody can ever be treated without consent. Access recorded: 2026-09-06.
- **AQAS** — [Adamou et al. (2024): The adult ADHD assessment quality assurance standard](https://pmc.ncbi.nlm.nih.gov/articles/PMC11327143/). Comprehensive assessment uses a clinical interview and differential assessment; an initial diagnostic interview around 90 minutes is described, with further work as needed. Access recorded: 2026-09-06.
- **DIGI** — [APA (2020): FDA Approves First Game-Based Therapy for ADHD](https://www.psychiatry.org/news-room/apa-blogs/fda-approves-first-game-based-therapy-for-adhd). FDA-authorized game-based therapy exists for attention in pediatric ADHD; regulatory authorization is not a cure or replacement for all care. Access recorded: 2026-09-06.
- **JUSTICE** — [Schäfer and Kraneburg (2015): ADHD and Justice Sensitivity—A Pilot Study](https://pubmed.ncbi.nlm.nih.gov/23223013/). Pilot evidence for justice sensitivity; not a validated diagnosis, universal moral virtue or all-population law. Access recorded: 2026-09-06.
- **JUSTICE2** — [Bondü and Esser (2015): Justice and rejection sensitivity in children and adolescents with ADHD symptoms](https://pubmed.ncbi.nlm.nih.gov/24878677/). Youth ADHD symptoms associated with victim justice sensitivity and anxious/angry rejection sensitivity; facet and population limits apply. Access recorded: 2026-09-06.
- **FEMALE** — [Young et al. (2020): Females with ADHD, expert consensus statement](https://pmc.ncbi.nlm.nih.gov/articles/PMC7422602/). Female underrecognition, internalizing problems, compensation/masking and lifespan clinical context; no single uniform female presentation. Access recorded: 2026-09-06.
- **NCCIH** — [NCCIH: ADHD and Complementary Health Approaches—What the Science Says](https://www.nccih.nih.gov/health/providers/digest/adhd-and-complementary-health-approaches-science). Inconclusive evidence for many supplements/diets; some approaches have limited targeted benefits. Absence from standard treatment is not proof that a treatment can never help. Access recorded: 2026-09-06.
- **EXER** — [Huang et al. (2023): Chronic Exercise for Core Symptoms and Executive Functions in ADHD, meta-analysis](https://publications.aap.org/pediatrics/article/151/1/e2022057745/190271/Chronic-Exercise-for-Core-Symptoms-and-Executive). Exercise can have adjunctive benefits; not evidence for a cure or a fixed immediate response. Access recorded: 2026-09-06.
- **MAG** — [Ghanizadeh (2013): Systematic review of magnesium therapy for ADHD](https://pubmed.ncbi.nlm.nih.gov/23808779/). Small/limited studies do not establish routine magnesium treatment; deficiency correction is a distinct indication. Access recorded: 2026-09-06.
- **TYR** — [Reimherr et al. (1987): Open trial of L-tyrosine for attention deficit disorder](https://pubmed.ncbi.nlm.nih.gov/3300376/). Small uncontrolled trial, with loss of initial benefit; not established sustained ADHD treatment. Access recorded: 2026-09-06.
- **ASH** — [Naik et al. (2026): Efficacy and safety of ashwagandha root extract in children and adolescents with mild ADHD](https://pubmed.ncbi.nlm.nih.gov/42602386/). A short trial reports improvement in mild pediatric ADHD. This preliminary finding is not established general ADHD efficacy or long-term safety. Access recorded: 2026-09-06.
- **RHOD** — [ClinicalTrials.gov: Rhodiola rosea in adults with ADHD, NCT02737020](https://clinicaltrials.gov/study/NCT02737020). A trial registration identifies investigation, not demonstrated efficacy; no adequate reported result was located to support the general treatment claim. Access recorded: 2026-09-06.
- **FDASTIM** — [FDA: Updating warnings for prescription stimulants](https://www.fda.gov/drugs/drug-safety-communications/fda-updating-warnings-improve-safe-use-prescription-stimulants-used-treat-adhd-and-other-conditions). Misuse, diversion, addiction and overdose risks require counseling and monitoring; prescribed oral treatment is not equated with illicit high-dose use. Access recorded: 2026-09-06.
- **DSMCHANGE** — [Epstein and Loren (2013): Changes in the definition of ADHD in DSM-5](https://pmc.ncbi.nlm.nih.gov/articles/PMC3955126/). Adult symptom threshold and age-of-onset criteria changed. Broader eligibility does not mean diagnostic criteria or impairment ceased to exist. Access recorded: 2026-09-06.
- **SOCIAL** — [Morellini et al. (2022): Social cognition in adult ADHD, systematic review](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.940445/full). Some social-cognition and emotion-recognition difficulties are documented with variable results; neither total absence of empathy nor superior lie detection follows. Access recorded: 2026-09-06.
- **CDC2023** — [Staley et al., CDC MMWR (2024): ADHD diagnosis, treatment and telehealth use in US adults, 2023](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a1.htm). 6.0% estimated current self-reported adult diagnoses; 55.9% first diagnosed at age 18 or later. This is a dated US diagnosis estimate, not worldwide biological prevalence. Access recorded: 2026-09-06.
- **TIME** — [Barkley, Murphy and Bush (2001): Time perception and reproduction in young adults with ADHD](https://pubmed.ncbi.nlm.nih.gov/11499990/). Estimation differences became nonsignificant after IQ adjustment; reproduction deficits remained. Laboratory timing is not identical to estimating real-life task completion. Access recorded: 2026-09-06.
- **HYPER** — [Hupfeld, Abagis and Shah (2019): Living in the zone—hyperfocus in adult ADHD](https://pubmed.ncbi.nlm.nih.gov/30267329/). Self-report evidence of hyperfocus and attention absorption; does not imply superior skill, universal intensity or a diagnostic test. Access recorded: 2026-09-06.
- **SUDMED** — [Quinn et al. (2017): ADHD medication and substance-related problems](https://pubmed.ncbi.nlm.nih.gov/28659039/). Observational within-person analyses associate medication periods with fewer substance-related events; not proof that medication prevents addiction in every individual. Access recorded: 2026-09-06.
- **OVER** — [Kazda et al. (2021): Overdiagnosis of ADHD in children and adolescents, systematic scoping review](https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2778451). Evidence of overdiagnosis/overtreatment in some youth contexts; does not erase simultaneous underdiagnosis or justify rejecting an individual diagnosis. Access recorded: 2026-09-06.
- **RD** — [Willcutt et al. (2010): Etiology and neuropsychology of comorbidity between reading disability and ADHD](https://pubmed.ncbi.nlm.nih.gov/20828676/). Distinct but frequently co-occurring difficulties with shared cognitive risks; reading disability is not synonymous with ADHD. Access recorded: 2026-09-06.
- **FMRI** — [Rubia et al. (2011): Methylphenidate normalizes fronto-striatal underactivation during interference inhibition](https://www.nature.com/articles/npp201130). Task/group-specific imaging effects; cannot diagnose a person from a generic brain image. Access recorded: 2026-09-06.
- **PRISON** — [Fazel and Favril (2024): ADHD in adult prisoners, updated meta-analysis](https://pubmed.ncbi.nlm.nih.gov/38568877/). Adult prison prevalence estimates depend strongly on sampling and assessment; not a universally applicable 25–45% rate. Access recorded: 2026-09-06.
- **PRISONOLD** — [Young et al. (2015): Meta-analysis of ADHD prevalence in incarcerated populations](https://pmc.ncbi.nlm.nih.gov/articles/PMC4301200/). Earlier synthesis shows high, heterogeneous estimates; screening, clinical interviews and age groups must not be conflated. Access recorded: 2026-09-06.
- **TRENDS** — [Polanczyk et al. (2014): ADHD prevalence estimates across three decades, systematic review and meta-regression](https://pubmed.ncbi.nlm.nih.gov/24464188/). Methodologically adjusted prevalence did not show a three-decade rise; diagnosis counts and underlying prevalence are distinct. Access recorded: 2026-09-06.
- **NOISE** — [Nigg et al. (2024): White/pink noise and task performance in youth with ADHD, systematic review and meta-analysis](https://pubmed.ncbi.nlm.nih.gov/38428577/). Small average task benefits; no universal benefit from all music/noise and no diagnostic test. Access recorded: 2026-09-06.
- **SDB** — [Sedky et al. (2014): ADHD and sleep-disordered breathing in pediatric populations, meta-analysis](https://pubmed.ncbi.nlm.nih.gov/24581717/). Sleep-disordered breathing is associated with ADHD-like symptoms; improvement after treatment is possible, but it does not establish that all ADHD is sleep apnea. Access recorded: 2026-09-06.
- **SDBREVIEW** — [Sleep Disordered Breathing and Risk for ADHD: Review of Supportive Evidence and Proposed Underlying Mechanisms (2024)](https://journals.sagepub.com/doi/10.1177/10870547241232313). Underrecognition and overlapping cognitive/neurobiological features are discussed; overlap is not identity or a scan-based differential diagnosis. Access recorded: 2026-09-06.
- **OSAEX** — [Rueda et al. (2020): Myofunctional therapy for obstructive sleep apnoea, Cochrane review](https://www.cochrane.org/evidence/CD013449_myofunctional-therapy-oropharyngeal-mouth-and-throat-exercises-people-obstructive-sleep-apnoea). Some short-term benefits, with limited certainty; not a fixed additive percentage for each exercise. Access recorded: 2026-09-06.
- **OSAPOS** — [Srijithesh et al. (2019): Positional therapy for obstructive sleep apnoea, Cochrane review](https://www.cochrane.org/evidence/CD010990_are-interventions-keep-people-sleeping-their-side-best-way-treat-obstructive-sleep-apnoea). Position can help selected positional apnea; efficacy is not uniform or automatically additive with other changes. Access recorded: 2026-09-06.
- **ADDXR** — [DailyMed: Adderall XR prescribing information, revised April 2026](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aff45863-ffe1-4d4f-8acf-c7081512a6c0). Formulation-specific doses, Schedule II status, adverse effects, acidifying-agent interactions, dependence and withdrawal. Access recorded: 2026-09-06.
- **ADDIR** — [DailyMed: Adderall immediate-release prescribing information](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?audience=consumer&setid=f22635fe-821d-4cde-aa12-419f8b53db81). Age-specific starting doses, morning administration, interactions and adverse reactions. Access recorded: 2026-09-06.
- **AAP** — [Wolraich et al. (2019): AAP clinical practice guideline for ADHD in children and adolescents](https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis). Assessment from age four, multimodal care, preschool behavior intervention first; methylphenidate when indicated, rather than dextroamphetamine as initial preschool drug. Access recorded: 2026-09-06.
- **MATUR** — [Shaw et al. (2007): ADHD is characterized by a delay in cortical maturation](https://pubmed.ncbi.nlm.nih.gov/18024590/). Longitudinal group differences in cortical thickness maturation, particularly prefrontal areas; not an individual developmental age or direct measure of myelination. Access recorded: 2026-09-06.
- **MEDIA** — [Thorell et al. (2024; online 2022): Longitudinal associations between digital media use and ADHD symptoms, systematic review](https://pubmed.ncbi.nlm.nih.gov/36562860/). Bidirectional associations and methodological limitations prevent a simple proof of causation or categorical proof of no influence. Access recorded: 2026-09-06.
- **AZST** — [DailyMed: Azstarys prescribing information](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=00b5e716-5564-4bbd-acaf-df2bc45a5663). Azstarys combines serdexmethylphenidate and dexmethylphenidate; its mechanism, doses and Schedule II classification differ from centanafadine. Access recorded: 2026-09-06.
- **SIM** — [FDA: Simtriyo (centanafadine), initial prescribing information (2026)](https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/218145s000lbl.pdf). Norepinephrine/dopamine/serotonin reuptake inhibitor, age/weight eligibility and 210–280 mg adult regimen. These details must not be assigned to Azstarys. Access recorded: 2026-09-06.
- **INTERO** — [Bruton et al. (2025): Diminished interoceptive accuracy in ADHD, systematic review](https://pubmed.ncbi.nlm.nih.gov/39905593/). Limited, mixed evidence for interoceptive differences. Hunger/fullness are interoceptive signals, not proprioception (limb/body position). Access recorded: 2026-09-06.
- **EEG** — [Gloss et al. (2016): AAN practice advisory on EEG theta/beta ratio in ADHD diagnosis](https://www.neurology.org/doi/10.1212/WNL.0000000000003265). EEG theta/beta ratio must not replace a standard clinical evaluation; no single true-ADHD EEG pattern. Access recorded: 2026-09-06.
- **ASDADHD** — [Young et al. (2020): consensus guidance on co-occurring ADHD and autism](https://pubmed.ncbi.nlm.nih.gov/32448170/). Clinical co-occurrence and management; individual traits vary. Access recorded: 2026-09-06.
- **OCD** — [Cabarkapa et al. (2019): co-morbid OCD and ADHD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6700219/). Comorbidity and treatment; not validation of scan-defined subtypes. Access recorded: 2026-09-06.
- **DOWN** — [NICHD: About Down syndrome](https://www.nichd.nih.gov/health/topics/factsheets/downsyndrome). Background checked for scope; standalone non-ADHD facts are excluded. Access recorded: 2026-09-06.
- **SENS** — [Sensory Processing in Individuals With ADHD: systematic review and meta-analysis (2025)](https://pubmed.ncbi.nlm.nih.gov/40250555/). Sensory differences are associated, not unique diagnostic signs. Access recorded: 2026-09-06.
- **LIGHT** — [van Andel et al. (2021): randomized chronotherapy trial in adults with ADHD and delayed sleep phase](https://pubmed.ncbi.nlm.nih.gov/33121289/). Specific melatonin and morning-light protocol, not a universal sleep treatment. Access recorded: 2026-09-06.
- **GUT** — [Sukmajaya et al. (2021): systematic review of gut microbiota and ADHD](https://pubmed.ncbi.nlm.nih.gov/33593384/). Preliminary associations do not establish a gut cause or detox treatment. Access recorded: 2026-09-06.
- **DIET** — [Pinto et al. (2022): Eating Patterns and Dietary Interventions in ADHD](https://pmc.ncbi.nlm.nih.gov/articles/PMC9608000/). Dietary associations, intervention evidence and limitations. Access recorded: 2026-09-06.
- **DEA** — [DEA: Stimulants factsheet](https://www.dea.gov/factsheets/stimulants). Pharmacology, abuse risks and controlled status. Access recorded: 2026-09-06.
- **MISUSE** — [Arria et al. (2010): Nonmedical Prescription Stimulant Use among College Students](https://pmc.ncbi.nlm.nih.gov/articles/PMC2951617/). College stimulant misuse; not an endorsement of nonmedical use. Access recorded: 2026-09-06.
- **PUFA** — [Gillies et al. (2023), Cochrane: polyunsaturated fatty acids for ADHD](https://www.cochrane.org/evidence/CD007986_polyunsaturated-fatty-acids-pufa-supplements-attention-deficit-hyperactivity-disorder-adhd-children). No established core-symptom benefit; limited responder findings do not establish general efficacy. Access recorded: 2026-09-06.
- **ZINC** — [Talebi et al. (2022): zinc supplementation systematic review and dose-response meta-analysis](https://pubmed.ncbi.nlm.nih.gov/34184967/). Limited trial findings; total symptom scores and specific impulsivity effects must be distinguished. Access recorded: 2026-09-06.
- **VITD** — [Gan et al. (2019): vitamin D supplementation systematic review/meta-analysis](https://pubmed.ncbi.nlm.nih.gov/31368773/). Small adjunctive trials and low-certainty evidence; not proof of a uniform dopamine deficit. Access recorded: 2026-09-06.
- **OXID** — [Joseph et al. (2013): Oxidative Stress and ADHD, a meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC5293138/). Peripheral markers cannot demonstrate brain inflammation or validate detox treatments. Access recorded: 2026-09-06.
- **PAIN** — [Battison et al. (2023): Associations between Chronic Pain and ADHD in Youth, scoping review](https://pmc.ncbi.nlm.nih.gov/articles/PMC9857366/). Association and experimental pain findings; mechanisms remain uncertain. Access recorded: 2026-09-06.
- **MIND** — [Oliva et al. (2021): mindfulness-based interventions in ADHD, systematic review/meta-analysis](https://pubmed.ncbi.nlm.nih.gov/34146899/). Possible benefit with limitations; no guaranteed seconds-to-refocus effect. Access recorded: 2026-09-06.
- **NHS** — [NHS: ADHD in adults](https://www.nhs.uk/conditions/adhd-adults/). Symptoms, assessment and support. Access recorded: 2026-09-06.
- **SEXHORM** — [Osianlis et al. (2025): ADHD and Sex Hormones in Females, systematic review](https://pmc.ncbi.nlm.nih.gov/articles/PMC12145478/). Emerging heterogeneous evidence; not a universal oestrogen-dopamine formula. Access recorded: 2026-09-06.
- **PS** — [Bruton et al. (2021): phosphatidylserine for pediatric ADHD, systematic review/meta-analysis](https://pubmed.ncbi.nlm.nih.gov/33539192/). Preliminary positive trials do not establish routine clinical efficacy. Access recorded: 2026-09-06.
- **PINE** — [Cochrane (2020): pine-bark supplements for chronic disorders](https://www.cochrane.org/evidence/CD008294_using-pine-bark-supplements-help-treat-variety-chronic-diseases). Very limited certainty for treatment conclusions. Access recorded: 2026-09-06.
- **PINERCT** — [Weyns et al. (2022): French maritime pine-bark extract in pediatric ADHD](https://www.sciencedirect.com/science/article/pii/S1756464622003164). A positive clinical trial, not proof of general established efficacy. Access recorded: 2026-09-06.
- **NF** — [Westwood et al. (2025): Neurofeedback for ADHD, systematic review/meta-analysis](https://pubmed.ncbi.nlm.nih.gov/39661381/). Blinded outcomes do not establish general efficacy as a stand-alone treatment. Access recorded: 2026-09-06.
- **INCA** — [Pelsser et al. (2011): INCA restricted-elimination-diet randomized trial](https://pubmed.ncbi.nlm.nih.gov/21296237/). Short-term selected-sample symptom response is not a population cure rate. Access recorded: 2026-09-06.
- **ELIM** — [Nigg and Holton (2014): Restriction and Elimination Diets in ADHD Treatment](https://pmc.ncbi.nlm.nih.gov/articles/PMC4322780/). Subgroup response and limitations; supervision and nutritional adequacy matter. Access recorded: 2026-09-06.
- **CVLONG** — [Zhang et al. (2024): ADHD medication and long-term cardiovascular disease risk](https://pubmed.ncbi.nlm.nih.gov/37991787/). Observational association; does not establish identical risk for every patient. Access recorded: 2026-09-06.
- **THEAN** — [Kahathuduwa et al. (2020): L-theanine–caffeine crossover study in boys with ADHD](https://pubmed.ncbi.nlm.nih.gov/32753637/). Small exploratory study; not established treatment efficacy. Access recorded: 2026-09-06.
- **BFRB** — [Grant and Chamberlain (2021): Trichotillomania and Skin-Picking Disorder, an update](https://pmc.ncbi.nlm.nih.gov/articles/PMC9063575/). Body-focused repetitive behaviours and clinical distinctions. Access recorded: 2026-09-06.
- **BFRBCO** — [Okumuş et al. (2022): Body Focused Repetitive Behavior Disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC10552165/). Comorbidities and repetitive behaviours; not ADHD diagnostic criteria. Access recorded: 2026-09-06.
- **HYPERMOB** — [Kindgren et al. (2021): ADHD/autism in children with hypermobility disorders](https://pmc.ncbi.nlm.nih.gov/articles/PMC7882457/). Clinical sample association, not verification of a particular clinic anecdote. Access recorded: 2026-09-06.
- **POTS** — [NINDS: Postural Tachycardia Syndrome](https://www.ninds.nih.gov/health-information/disorders/postural-tachycardia-syndrome-pots). POTS terminology and physiology. Access recorded: 2026-09-06.
- **TBI** — [Asarnow et al. (2021): pediatric traumatic brain injury and ADHD, meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC8276124/). Secondary ADHD after significant injury; not all concussion causes ADHD. Access recorded: 2026-09-06.
- **ACE** — [Zhang et al. (2022): adverse childhood experiences and ADHD, systematic review/meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC9575611/). Association is not proof of causal direction. Access recorded: 2026-09-06.
- **US87** — [Schein et al. (2022): Economic burden of ADHD among adults in the United States](https://pubmed.ncbi.nlm.nih.gov/34806909/). Published estimate of 8.7 million adults; distinguish reference years and case definitions. Access recorded: 2026-09-06.
- **BUP** — [Verbeeck et al. (2017), Cochrane: bupropion for adult ADHD](https://pmc.ncbi.nlm.nih.gov/articles/PMC6485546/). Possible off-label benefit with low-certainty evidence. Access recorded: 2026-09-06.
- **MIGRAINE** — [Gonzalez-Hernandez et al. (2024): ADHD in adults with migraine](https://pubmed.ncbi.nlm.nih.gov/37752867/). Observed clinical association, not proof of causation. Access recorded: 2026-09-06.
- **IMPACT** — [French et al. (2024): impacts associated with ADHD, umbrella review](https://pmc.ncbi.nlm.nih.gov/articles/PMC11151783/). Broad functional and health associations; outcomes are not inevitable. Access recorded: 2026-09-06.
- **GENERIC** — [FDA: Generic Drugs, Questions and Answers](https://www.fda.gov/drugs/generic-drugs/generic-drugs-questions-answers). Bioequivalence and inactive ingredients; differences are permitted, not mandatory. Access recorded: 2026-09-06.
- **IRON** — [NIH Office of Dietary Supplements: Iron, health-professional factsheet](https://ods.od.nih.gov/factsheets/Iron-HealthProfessional/). Iron sources, deficiency and appropriate supplementation. Access recorded: 2026-09-06.
- **SAFF** — [Seyedi-Sahebari et al. (2024): Crocus sativus and ADHD, systematic review](https://pubmed.ncbi.nlm.nih.gov/37864351/). Preliminary small trials, with insufficient evidence for firm routine-treatment conclusions. Access recorded: 2026-09-06.
- **IGG** — [AAAAI: The myth of IgG food-panel testing](https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/igg-food-test). These tests do not establish the proposed food intolerance or treatment pathway. Access recorded: 2026-09-06.
- **BURN** — [Raymaker et al. (2020): Defining Autistic Burnout](https://pubmed.ncbi.nlm.nih.gov/32851204/). Qualitative autistic-burnout findings, not validation of an ADHD-specific screening checklist. Access recorded: 2026-09-06.
- **TEENSLEEP** — [American Academy of Sleep Medicine: pediatric sleep-duration consensus (2016)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5078711/). Teen sleep-duration range, not an identical requirement for every adolescent. Access recorded: 2026-09-06.
- **ATMDD** — [Bangs et al. (2007): atomoxetine in adolescents with ADHD and major depression](https://pubmed.ncbi.nlm.nih.gov/17822337/). ADHD and depression outcomes differ; not established antidepressant efficacy. Access recorded: 2026-09-06.
- **COMDEP** — [McIntosh et al. (2009): adult ADHD and comorbid depression, consensus algorithm](https://pmc.ncbi.nlm.nih.gov/articles/PMC2695217/). Individualized treatment priority by severity, impairment and risk. Access recorded: 2026-09-06.
- **FERRITIN** — [Tseng et al. (2018): peripheral iron levels in children with ADHD, systematic review/meta-analysis](https://www.nature.com/articles/s41598-017-19096-x). Ferritin and iron-deficiency associations; not proof that everyone needs iron. Access recorded: 2026-09-06.
- **ALEX** — [Edel et al. (2010): Alexithymia, emotion processing and social anxiety in adults with ADHD](https://pubmed.ncbi.nlm.nih.gov/20952350/). Clinical associated difficulties; sample average was not much above community comparisons. Access recorded: 2026-09-06.
- **FATIGUE** — [Rogers et al. (2017): Fatigue in an adult ADHD population](https://pubmed.ncbi.nlm.nih.gov/27918087/). Fatigue is documented in ADHD but is nonspecific and not a stand-alone diagnostic sign. Access recorded: 2026-09-06.
- **UPD_CDC2022** — [Danielson et al. (2024): ADHD prevalence among US children and adolescents in 2022](https://stacks.cdc.gov/view/cdc/160350). Original national parent-survey study: 10.5% current diagnosed ADHD, 11.4% ever diagnosed, ages 3–17. Does not estimate worldwide or India-specific prevalence. Access recorded: 2026-09-09.
- **UPD_REMISSION** — [Sibley et al. (2022): Variable patterns of remission from ADHD in the MTA study](https://pubmed.ncbi.nlm.nih.gov/34384227/). Original longitudinal study; remission, recurrence and sustained remission through follow-up. Does not establish permanent cure or universal persistence. Access recorded: 2026-09-09.
- **UPD_NIMH_ADULT** — [NIMH: ADHD in adults — 4 things to know](https://www.nimh.nih.gov/health/publications/adhd-what-you-need-to-know). Adult manifestations, developmental history, differential assessment and available treatments; variable functioning and support needs. Access recorded: 2026-09-09.
- **UPD_GIFTED** — [François-Sévigny et al. (2022): Parents’ and teachers’ perceptions of gifted children with and without ADHD](https://pmc.ncbi.nlm.nih.gov/articles/PMC9688281/). Original comparative study and clinical context concerning giftedness, overlapping behaviors and multi-informant assessment. High intelligence does not exclude ADHD. Access recorded: 2026-09-09.
- **UPD_COGFUN** — [Hahn-Markowitz et al. (2020): Cog-Fun occupational therapy for children with ADHD — randomized trial](https://pubmed.ncbi.nlm.nih.gov/27637735/). Context-specific benefits on parent reports, without significant teacher-reported group effects. Supports selected functional help, not blanket efficacy of all OT. Access recorded: 2026-09-09.
- **UPD_HYPER_PUBLISHER** — [Hupfeld et al. (2019): Living “in the zone” — hyperfocus in adult ADHD, publisher record](https://link.springer.com/article/10.1007/s12402-018-0272-y). Original self-report study, abstract and publisher change-history notice. Supports possible hyperfocus, not a stand-alone diagnostic criterion. Access recorded: 2026-09-09.
- **UPD_HYPER_CORRECTION** — [Hupfeld et al. (2019): Correction to Living “in the zone”](https://link.springer.com/article/10.1007/s12402-019-00296-6). Correction record consulted alongside the original publisher page, which identifies a missing hobby-subscale response option. No precise frequency estimate is derived here. Access recorded: 2026-09-09.
- **UPD_APA_MENTAL** — [American Psychiatric Association: What is mental illness?](https://www.psychiatry.org/patients-families/what-is-mental-illness). General definition involving significant changes and distress and/or functional problems; this is not a sufficient universal diagnostic rule. Access recorded: 2026-09-09.
- **UPD_ASD_GUIDE** — [Young et al. (2020): Expert consensus on identification and treatment of co-occurring ADHD and autism — full text](https://link.springer.com/article/10.1186/s12916-020-01585-y). Comprehensive assessment, co-occurrence and individualized behavioral, environmental and medication support. Access recorded: 2026-09-09.
- **LIT_STRENGTHS** — [Schippers et al. (2022): A qualitative and quantitative study of self-reported positive characteristics of individuals with ADHD](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2022.922788/full). A convenience sample described perceived strengths. The authors distinguish subjective reports from demonstrated abilities and call for objective validation. Crisis performance was not tested. Access recorded: 2026-09-09.
