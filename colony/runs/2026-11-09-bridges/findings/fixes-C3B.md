# Fixes C3B, run 2026-11-09-bridges (referee R3, sections 2, 3, 4; FIXROUND.md)

All fixes applied in place in proposals/<id>/. No fix rebutted. Script of the edits:
work/C3B/fixround.py. runcheck after the edits: 5 of 5 functions pass in each of the three proposals.

## synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product
1. Novelty of (vii): "the mean entropy of a sector ..." removed from "New here"; what stays new is the rational
   difference Delta with its bounds and the comparison with the stored deficit bounds. The note now says the
   closed form is the two-block case of equation (45) of Bianchi, Hackl, Kieburg, Rigol and Vidmar
   (arXiv:2112.06959, checked on the web by the referee), rederived here from Page's Fact. The technical level
   and the proof of (vii) say the same in one sentence each.
2. Parity average: formal level, technical level and proof (iv) now say the state is fixed by
   x -> (x + Gamma x Gamma)/2, the stored single-mode average with the total parity in place of sigma, the
   l-mode form being a definition here; the proof adds why mode-by-mode application would be wrong (it erases
   the pair coherence). Note: the uses edge is for the one-mode case only.
3. Delta's size at the technical level: "between 1/(2mn) and 1/(2mn) + 1/(2n^2), about 3/(4m^2) at the
   crossing"; the proof records that the upper bound is below 1/(2mn) + 1/(2n^2).
4. descent-lift.imported-fermionic-operations-are-even-reduced named in the note (content derived in the
   algebra and sharpened; dropping the import is a maintainer decision); Bravyi and Kitaev 2002, Araki and
   Moriya 2003 added to the prior art.
5. Formal (vii) parenthesis rewritten (sector value against the Fact's value, with Delta = 1/6 and
   6553/144144).
6. Conditional inputs: one-liner and lay level name the two imports; technical level says both are
   conditional on them.
7. Clause (v) last sentence and the proof: "Reading the pairs of Theorem ... as these pair states, ...".
8. Fate table: "at version 3" for the two eviction results.
9. Banuls, Cirac and Wolf 2007; Friis, Lee and Bruschi 2013 stay "cited from memory".
Direction ruling: this entity keeps its uses edges to the eviction results; the sector lemma stays inline, and
the note says it is cut to a citation of the finite-averages result after acceptance.

## synthesis.eviction-keeps-one-replica-saddle (version 4)
1. Total-parity wording: formal preamble, technical level, amendments defect text, end of "The split" in the
   proof.
2. Stale notes: "(through version 3; removed at version 4)" appended at both places that named the Lubkin Fact
   as cited.
3. Amendments defect text now records that the claimref to synthesis.imported-haar-average-purity is removed
   from the proof.
4. "at Leon's request (his decision of 9 November 2026)"; the note's `by:` no longer carries a run name.
5. Proof (i) and (e): "reading the pairs of that theorem as the pair states of (e)".
6. No change (stored function name and comment concern the abstract column).

## synthesis.eviction-keeps-one-of-catalan-many-replica-saddles (version 4)
1. Amendments: second sentence added (the stored upper bound was proved only as
   C_n d^{1-n} + (n! - C_n) d^{-n-1} and verified for n = 2, 3, 4, d = 2, 4, 8). Formal (iii) now states the
   proved bound beside the verified one.
2. Amendments: "the even states (fixed by the total-parity average)"; no edge to the single-mode theorem added.
3. Docstring of the new check function says the trace count is enumerated at three cases only and the general
   count is the proof's.
4. "at Leon's request (his decision of 9 November 2026)"; `by:` as above.
5. Technical level: "as does the average on a parity sector".
6. Repin to version 4 of the one-saddle theorem: maintainer, after acceptance (unchanged).

## Left for the maintainer
- Retirement of synthesis.imported-haar-average-purity (still referenced in the formal text of
  synthesis.imported-haar-moments-of-random-pure-state@2 and in open_problems.yaml).
- After acceptance: cut the sector lemma here and in the Catalan proof to a citation of the finite-averages
  result; repin.

check4: pending (orchestrator)
