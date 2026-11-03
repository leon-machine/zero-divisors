# Changes since the deposited version

The official version of every Transport Paper is the one deposited on Zenodo. A paper the Lab
generates from its store can differ from it, because results are corrected, restated or
added after the deposit. The Lab marks every such difference.

## The baseline

`deposits/` holds the LaTeX source of each deposited version and `deposits/deposits.yaml`
records, per paper, the DOI, the printed version, the file and its sha256. The 20 sources
recorded on 2026-10-27 were copied from TP_Papers_Suite, and each printed version was read
from the paper's `\date` line. If the file on Zenodo differs from the suite copy, record the
Zenodo file instead.

When a new version is deposited:

    python -m tp.deposits record T12 --tex path/to/T12_standard_model.tex \
        --doi 10.5281/zenodo.NNNNNNN --version 2.1
    python -m tp regen t12-regenerated --store store     # and the paper's other documents
    python -m tp.pdfs --only t12-regenerated
    python -m tp.site

The marks then clear, apart from changes made after that deposit.

## What counts as a change

A result is compared with the deposit of the paper that states it (`locators.paper`). So a
Fact that T5 imports from T6 is compared with T6's deposit. The comparison is textual, after
a normalisation that undoes what extraction does to a source:

- cross-references, citations and labels are dropped;
- layout, float and font commands are dropped;
- braces and whitespace are dropped.

The statement or proof is unchanged when the remainder occurs in the deposited source.

- **Revised: statement, proof, or both.** The words or mathematics differ. A change of
  notation or terminology counts, such as `Q(v)` for the square of a vector, or the GTG
  restatements.
- **Citations only.** The only difference is a citation added in parentheses, as the
  grounding passes add them. It is counted but not marked.
- **Added.** The deposited paper did not state the result. Results brought in from elsewhere
  are counted but not marked: cited facts, another paper's premises, the series' refutations
  and predictions.
- **Withdrawn.** A result of the deposited paper that the store has since refuted or removed.

## How much a revision matters

Each revised result is put in one of three classes.

- **Corrected.** The deposited version was wrong or claimed too much, and the edit fixes it.
- **Changed.** The content changed by a later decision, not because the deposit was wrong. Examples: a scope or clause added, a new proof route, a premise restated, a merge.
- **Reworded.** Only wording, notation, terminology or citations changed; the mathematics and the claim are as deposited. This is the minor class.

The class is a judgement. It is recorded once per result in `deposits/classification.yaml`, with a one-line reason and the entity version it applies to.

- The first pass (27 October 2026) was a review of every revision, reading the word diff against the deposit together with the store's notes.
- A later edit to the result returns it to the rules until it is classified again.
- The rules never say "corrected". They say "reworded" only when every recorded edit is a wording pass, or when, with nothing on record, the only differences are citations or a word or two with no mathematics. Anything else is "changed", shown as not yet reviewed.

To set a class by hand:

    python -m tp.deposits set <entity> --class reworded --by leon --reason "Notation only."

To make a new edit name its own class, add the `--kind` flag to the bump:

    tp bump <id> --kind correction --note "..."      # or change, or wording

The note is then recorded as starting "Correction:", "Change:" or "Wording:".

## Where it shows

- **The PDF.** The notice box carries one summary sentence. Each revised or added result has
  a coloured margin mark: red for corrected, orange for changed, grey for reworded, blue for added. A closing section, *Changes since the deposited version*, lists each one
  with its deposited number and the store's dated notes (the three most recent, clipped).
- **The page.** The Documents detail card shows the summary and a "What changed" list, and
  each item opens the reader at that result. In the reader, a marked result opens to the
  store's notes and, for a labelled result, its statement and proof as deposited.

`python -m tp.deposits summary` prints the counts for every deposited paper.
`python -m tp.deposits report <doc>` lists the changes in one document.
