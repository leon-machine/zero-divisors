---
id: synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping
kind: claim
version: 1
title: 'The residue requires two arrays per unit on average and fixes no grouping'
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, counting-rules, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-09-solvable
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-09-solvable
review: draft
derivations:
- name: main
  uses:
  - synthesis.residue-from-mode-entropy@4
  - synthesis.half-integer-weight-array-carries-half-ln2@5
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.capacity-per-mode-independent-of-helicity@2
  - synthesis.slot-module-light-ray-arrays-are-weyl-components@3
  - synthesis.de-sitter-entropy-pi-n-squared@6
  - dark-matter.stored-asymmetry-charge-not-number@12
  assumes:
  - singularity.q-joint-quasi-freeness-s-wave@3
  - singularity.c2-cell-density@4
  - synthesis.window-reading-array-killing-energy@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mean_two_arrays_is_what_the_residue_requires
- kind: check
  ref: check.py::check_no_single_ladder_pair_and_no_zero_offset_union_carries_ln2
- kind: check
  ref: check.py::check_light_rays_are_arrays_over_content_not_registered_units
- kind: proof
  derivation: main
extraction:
  maintainer_pass:
    by: maintainer-2026-11-09
    date: '2026-11-09'
    note: 'Leon approved the assumes edges named at acceptance: (Q) singularity.q-joint-quasi-freeness-s-wave@3, (C2) singularity.c2-cell-density@4 and the window reading synthesis.window-reading-array-killing-energy@1, used directly, are now assumed (the proof cites (Q) by claimref); statement unchanged.'
  open_problem: op.residue-killing-weights
  note: >-
    Attack item 1 of op.residue-killing-weights, second branch: "show which unit the residue requires given
    sixteen Weyl components per generation". Premise set at the pinned versions: the past cone of the problem's
    entities ((P), (R), (R_Lambda), (Q) version 3, (N+), the window reading, (C1) to (C3), (IC), J3, the
    slot-module hypothesis, tameness, F1 to F4, the tower premises reached through the slot module, and imports).
    The derivation attempt was registered first: a derivation of the unit needs a premise that groups arrays into
    registered units; none of the premises mentions a grouping, (C2) leaves its density free by its own
    statement, and the one structural unit, a ladder pair, carries less than ln 2 at the weights of (Q) version 3,
    so the attempt was killed and the result is the requirement and the independence. It makes the stored
    independence (argued) a proof in the form the proved content allows: with sixteen Weyl components per
    generation fixed, the free datum is the grouping, not a number of copies. Clause (iii) corrects a count in a
    stored statement: the number pi N^2/ln 2 that dark-matter.stored-asymmetry-charge-not-number attributes to
    light rays is the number of registered units, c/2 per light ray for c arrays per light ray; that argument uses
    only that N is common and is unaffected. Prior art, cited from memory, not premises: the species and cutoff
    degeneracy of entanglement entropy (L. Susskind and J. Uglum, Phys. Rev. D 50 (1994) 2700), of which (i) is
    the series' form. Transport-absent. What is not claimed: a derivation of the unit; anything about which
    fields form the light-ray sea (c is left as a parameter beyond the fermion content). The postulates used
    directly, (Q), (C2) and the window reading, are assumed; the other postulates of the
    cone (P1 to P5, R1 to R3, H1, T14's (U), (I), (P), (R), (R_Lambda), (IC), (C1), (C3), J3, the rate inputs
    (L, U), the slot-module, common-ceiling and indifference premises, tameness) are audited in the proof.
---

## formal
Assume the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy} (the counted units carry the entropy $A/4$, the area-law hypothesis), with the arrays of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} version 3, weights $\kappa(k + \tfrac12)$, each carrying $\tfrac12\ln 2$ at the Hawking temperature (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}), sixteen per generation per light ray (Theorem \claimref{synthesis.slot-module-light-ray-arrays-are-weyl-components}). A \emph{grouping} assigns each array to one registered unit; let $\bar u$ be the mean number of arrays per unit.
\begin{enumerate}
\item[(i)] \emph{(No premise fixes the grouping; proved.)} Every premise of the cone holds for every grouping: they constrain modes, arrays, their weights and states, and the density of (C2) (Premise \claimref{singularity.c2-cell-density}, which leaves $\nu$ free), and none mentions how arrays are grouped. J3 (\claimref{hawking.joint-j3-s-wave-reduction}) partitions the modes into $(\omega, \ell, m, s)$ channels and, with (Q) version 3, puts one array in each helicity channel; it supplies a candidate grouping (units as channels, or as the two helicity channels of one $(\omega, \ell, m)$, the choice \claimref{synthesis.capacity-per-mode-independent-of-helicity}(iii) records J3 as deciding) but no premise identifies a registered unit with a channel or a pair of channels, so the grouping stays free. Reading the density $\nu$ of (C2), which counts fermionic modes per Planck cell with one ladder pair per point, as a density of registered units of arrays is the framing of the problem, not (C2)'s literal text. The models differ in the residue, $\kappa_{c} = 1/(2\bar u\ln 2)$, and in $\nu$ by the same factor.
\item[(ii)] \emph{(What the residue requires; proved.)} The registered residue $\kappa_{c} = 1/(4\ln 2)$ holds exactly when $\bar u = 2$: on average two arrays per unit, eight units per generation, whatever the sizes of the individual units (of the $231$ groupings of a generation's sixteen arrays by size, exactly the $22$ with eight units qualify; uniform units qualify only at two arrays). No smaller structural unit qualifies: a boundary mode is one ladder pair of capacity $\ln 2$ (\claimref{synthesis.capacity-per-mode-independent-of-helicity}), and at these weights every mode has $|x| \ge \pi$, where $s(\pi) < 0.21 < \ln 2$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}). At the offset $0$ an array carries more than $\ln 2$ (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(ii)), so no union of whole arrays averages $\ln 2$ there; only the zero-weight mode does, with the rest of its array outside the count.
\item[(iii)] \emph{(Light rays are not registered units.)} With $c$ arrays per light ray, the light rays per Planck area per modular period are $1/(2c\ln 2)$, independent of the grouping, and on the cosmological horizon, under (R$_{\Lambda}$) with the same weights and $S = \pi N^{2}$ (\claimref{synthesis.de-sitter-entropy-pi-n-squared}), they number $2\pi N^{2}/(c\ln 2)$; the registered units number $\pi N^{2}/\ln 2$ exactly at $\bar u = 2$, which is $c/2$ units per light ray: $8n_{g}$ for the fermion content, which is $c$ under J3's reading of the integer-weight channels as currents of the arrays, $24$ at three generations. The count $\pi N^{2}/\ln 2$ is therefore that of registered units, not of light rays, as \claimref{dark-matter.stored-asymmetry-charge-not-number} worded it before its version 10 (its argument uses only that $N$ is common, which stands).
\end{enumerate}
So the residue does not fix the count unit; it requires its mean to be two arrays, an input recorded by decision, and the registered density $\nu = 1/(16\pi\ln 2)$ of \claimref{pred.boundary-mode-density} rests on that input.

## technical
Under the area-law hypothesis the residue is one over four times the mean entropy per counted unit. Each array of (Q) version 3 carries exactly half of $\ln 2$ at the Hawking temperature, so the residue takes its registered value exactly when the counted units hold two arrays on average, eight per generation of sixteen Weyl components; units of unequal size with that mean do equally well, and a uniform unit must be a pair. Nothing in the premises says how arrays are grouped, and the cell-density premise leaves the density free, so every grouping gives a model of the premises with its own residue: the unit is a recorded input. The literal structural unit, one ladder pair, cannot carry the capacity at these weights, since no mode has zero weight; at the other offset an array carries more than $\ln 2$, so no union of arrays fits there. The light rays are fewer than the registered units: their number is fixed by the area law and the number $c$ of arrays per light ray, $2\pi N^{2}/(c\ln 2)$ on the cosmological horizon, which is $c/2$ times fewer than the $\pi N^{2}/\ln 2$ registered units, twenty-four times fewer for three generations of fermions.

## lay
The series predicts how densely a black hole's horizon is packed with the elementary carriers of its entropy, and that prediction depends on what counts as one carrier. The natural building blocks each carry exactly half a bit's worth of entropy, so the prediction comes out right only if a carrier is, on average, two blocks. This result shows that nothing in the theory's assumptions decides how blocks are grouped into carriers: every grouping is consistent, and only the average of two gives the predicted density. It also corrects a count: the number of light rays on the universe's horizon is smaller than the number of carriers, by a factor set by how many blocks each light ray holds, twenty-four for the known three generations of matter particles.

## one-liner
Under the area law the residue $1/(4\ln 2)$ holds exactly when the counted units average two arrays of (Q) version 3 (eight per generation, any unit sizes); no premise fixes the grouping, no single ladder pair qualifies, and the light rays number $2\pi N^{2}/(c\ln 2)$, $c/2$ times fewer than the registered units.
