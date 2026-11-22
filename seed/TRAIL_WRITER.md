# Trail writer instructions

A trail is a guided walk through one subject of the store, for the site's
Universe view: the reader picks a subject, its results light up, and the
trail takes them from result to result, with a short passage of prose at each
step explaining what the step says and why it follows. Each trail is a stored
document generated from a recipe, so it regenerates when the store changes.

You write the trails for the subjects you are given. For each subject:

## 1. Choose the spine (6 to 10 results)

Work in /home/claude/zero-divisors. Read store/subjects.yaml for the
subject's title and scope. List the subject's entities:

    python3 - <<'EOF'
    from tp.model import load_store
    s = load_store('store')
    for k, e in sorted(s.entities.items()):
        if e.meta.get('subject') == 'SUBJECT' and e.kind in ('claim', 'prediction'):
            print(k, '|', e.status, '|', e.title, '|', (e.levels.get('one-liner') or '')[:140])
    EOF

Choose 6 to 10 results that tell the subject's story to a newcomer: where it
starts, the key steps, the headline results, and, where the subject has them,
its predictions or refutations. Prefer results whose lay level is written.
Each step should build on the earlier ones (check `derivations` uses edges).
Results from other subjects may appear if the story needs them, but keep most
of the spine in the subject. Do not include definitions (kind object).

## 2. Write the recipe

recipes/trail-SUBJECT.yaml :

    doc: trail-SUBJECT
    title: '<the subject title>'
    author: Leon Butler
    level: lay
    spine: [ ...your ids, in the order you want them... ]
    show: spine-only
    include:
      assumptions: always
      refutations: none
      predictions: in-cone
    on_refuted: keep-as-refutation
    format: latex-series
    budget:
      abstract_words: [60, 160]
    trail: true

Then generate it:  python3 -m tp doc recipes/trail-SUBJECT.yaml --store store
The generator orders the results by dependency (premises first); your spine
order is a preference, not a guarantee.

## 3. Write the prose

Read documents/trail-SUBJECT/blocks.json. Write
documents/trail-SUBJECT/prose.json mapping every prose slot (blocks of type
abstract, framing, transition) to its text, then run

    python3 -m tp regen trail-SUBJECT --store store

and read documents/trail-SUBJECT/audit.json. Fix every D101 to D106 and
D109 that comes from your prose, and repeat until only D110 remains.

What each slot is in a trail:
- abstract: the trail's opening card, 60 to 160 words: what this region of
  the subject is about, what the reader will see, and why it matters.
- introduction: one or two sentences on how the walk is ordered.
- i:<section>: one sentence opening each section.
- t:<previous>><next>: the step's explanation, shown beside the next result.
  Two to four sentences: what the next result says, in plain words, and why
  it follows from or matters after the previous one. This is the heart of the
  trail. It may restate the next result (tag [[c:<next id>]]) or a result
  already met (tag its id).
- conclusion: two or three sentences drawing the thread together, naming the
  assumptions the trail rests on (the postulates in "What we assume").

Tagging rule (the audit enforces it). Every sentence ends with exactly one tag:
  [[c:<claim id>]]  when the sentence states or summarises that claim. The
                    claim must be in this document. Any number in the sentence
                    must appear in that claim's own text.
  [[t]]             when the sentence only links, motivates or signposts and
                    asserts no new fact: no digits and no maths in it.

Style (revised 2026-10-27 after Leon's review: the old maths-free, long-paragraph prose read
as "big unbroken paragraphs devoid of mathematics"). The page shows each step's one-line
statement on the step card, so the prose explains why the step follows rather than restating it.
- Paragraphs of at most three short sentences, separated by a blank line in the slot text.
- Where a step has a defining formula, show it once as a display \[ ... \] inside the
  [[c:<id>]] sentence that states it, before that sentence's tag. Put no full stop inside the
  display (the audit's sentence splitter would cut there); let the tag follow the closing \].
  At most one display per step; inline $...$ where it helps a sentence.
- Every formula and number must match the cited claim's own text: read its formal level first.
- No maths and no digits in [[t]] sentences (the audit flags them as D103); a sentence that needs
  a symbol cites the claim that defines it.
- Say in words what each symbol is the first time it appears. Plain British English otherwise;
  explain jargon the first time; keep every condition visible ("assuming Hypothesis (S)");
  claim nothing beyond the claims' own texts; no em dashes; never "honest", "honestly",
  "load-bearing" or "clever"; geometric algebra language; macros only from store/notation.yaml;
  do not cite paper or theorem numbers or paper names.
trail-standard-algebra is the worked example of this style.

Touch only your own recipes and documents folders; never edit store/. Keep
scratch scripts in /tmp/claude-0/-home-claude/f5c21aa3-33bd-54d7-a8e9-4d9b5d6a3726/scratchpad/trails-<your group>/.
Report, per subject: the spine, the number of steps, and the final audit.
