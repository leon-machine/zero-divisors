# Prose writer instructions (document generation)

You write the connecting prose of one generated document. The document is
/home/claude/suite/transport_lab/documents/<doc>/ . Read blocks.json there:
it is the document in order. Claim blocks (type theorem, fact, postulate,
refutation, prediction) carry the claim's text; you must not change them.
You write ONLY the prose slots, which are the blocks whose type is
"abstract", "framing" or "transition". Their "id" is the slot name.

Write /home/claude/suite/transport_lab/documents/<doc>/prose.json : a JSON
object mapping every prose slot id to its text. Cover every slot.

Tagging rule (the audit enforces it). Every sentence ends with exactly one tag:
  [[c:<claim id>]]  when the sentence restates or summarises that claim. The
                    claim must be in this document (it has a block "c:<id>").
                    Any number in the sentence must appear in that claim's
                    text (formal, technical, lay or one-liner level).
  [[t]]             when the sentence only links, motivates or signposts and
                    asserts no new fact. A [[t]] sentence contains no digits
                    and no maths ($...$).
Put the tag after the full stop, e.g. "The descent is a parity average. [[c:singularity.descent-parity-average]]"

What to write:
- abstract: 150 to 250 words (tags not counted), stating what the document
  establishes, in the order the document does. Mostly [[c:...]] sentences.
- introduction: one paragraph saying what the reader will see and why the
  order is what it is.
- i:<section>: one or two sentences opening each section.
- t:<previous>><next>: ONE short sentence that carries the reader from the
  previous claim to the next one (the ids are in the slot name; "^" means the
  start of a section run). Usually [[t]]. Vary the wording.
- conclusion: a short paragraph drawing the thread together, including what
  is assumed (the postulates listed under "What we assume").

Style: claim nothing beyond the claims' own texts; keep their hypotheses;
no em dashes (no U+2014, no "---"); never the words "honest" or "honestly";
British spelling; plain, direct sentences; do not cite paper or theorem
numbers. Maths only inside [[c:...]] sentences, in $...$.

When done, run from /home/claude/suite/transport_lab:
    python3 -m tp regen <doc> --store store
and read documents/<doc>/audit.json. Fix every D101-D106 and D109 finding
that comes from your prose (edit prose.json, run regen again). D107 (pending
claim levels), D108 and D110 are not yours. Report the final audit counts.
