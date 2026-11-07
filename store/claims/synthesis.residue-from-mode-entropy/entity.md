---
id: synthesis.residue-from-mode-entropy
kind: claim
version: 4
title: The calibration residue re-expressed as a reciprocal mode entropy
status: proved
region: synthesis
subject: entropy
tags: [mode-counting, boundary-modes, counting-rules, undetermined-input, needs-continuum]
proposed_by:
  kind: ai
  session: residue-2026-10-22
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.cosmological-horizon-boundary-modes
derivations:
- name: main
  uses:
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.quarter-from-temperature@1
  - synthesis.de-sitter-entropy-pi-n-squared@6
  - synthesis.de-sitter-temperature-frozen-point-norm@7
  assumes:
  - singularity.p-univalence@2
  - singularity.r-regularity-fixed-locus@4
  - synthesis.r-lambda-regularity-cosmological-horizon@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_residue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - scrambling.residue-each-convention
  - scrambling.no-recount-reaches-quarter
  - pred.boundary-mode-density
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.de-sitter-mode-count
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 1 -> 2, note only, statement and proof unchanged. Clause (vi), with its values ln 2 + epsilon per array and 0.3470 arrays per Planck area per period, and the reading of (ii) that the registered value means zero-weight counted modes, were computed under Premise (Q) version 2, whose weight clause is kappa k with one zero-weight mode per array. Premise (Q) version 3 (Leon''s decision of 23 October) takes kappa(k + 1/2), with no zero-weight mode. At that offset one array carries exactly (1/2) ln 2 at the Hawking temperature (synthesis.half-integer-weight-array-carries-half-ln2 (i), given the theta-function identities), so with a counted unit of two arrays the unit carries exactly ln 2 with every fermion mode at nonzero weight, and under the area-law hypothesis the registered 1/(4 ln 2) is reproduced. The equality case of (ii) is therefore the realisation in which a counted unit is one fermion mode; it is one of two realisations, not forced. Clause (vi) stays true as a statement about the offset kappa k, and its last sentence (a derivation fixing the weights as (Q) does would refute (IC)) applies to version 2''s weights only. Clause (v) is unaffected. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3. Check strengthened: (vi) brackets pinned by rounding both ends to 0.02725, 0.7204, 0.3470, 0.3607; the (ii) and (iv) bounds pinned as attained minima; the strict de Sitter ratio pinned at 4/3; samples moved to module level. Version 3 -> 4.'
  flow_note: phase flow e^{-i omega t} on the modes (the T05 Thm 7.16 sense).
  note: 'The attempt of 22 October 2026 to settle T08''s calibration residue. The referee''s verdict, adopted: reformulated, not settled. It shows that under the area-law hypothesis the residue is the reciprocal of four times the counted modes'' mean thermal entropy, that the registered value is the zero-weight case, that the counted modes'' energy is below M/2, and that (Q) taken literally misses the registered value by about four per cent.'
---

## formal
Assume (P) (Premise \claimref{singularity.p-univalence}) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}). Let $J$ be the boundary modes of a Schwarzschild hole registered in one modular period, of Killing weights $\omega_{j}$, and suppose that they carry the hole's thermodynamic entropy: with $s$ the thermal entropy of one mode (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}) and $S = A/4$ the entropy that the series' temperature fixes (Theorem \claimref{synthesis.quarter-from-temperature}),
\[
\sum_{j \in J} s(x_{j}) \;=\; \frac{A}{4}, \qquad x_{j} = \frac{2\pi\omega_{j}}{\kappa} .
\]
Write $\kappa_{c} := |J|/A$ for the residue, the counted modes per Planck area of horizon per modular period, and $\langle s\rangle := |J|^{-1}\sum_{j} s(x_{j})$. Then:
\begin{enumerate}
\item[(i)] $\kappa_{c} = 1/(4\langle s\rangle)$: the residue is the reciprocal of four times the counted modes' mean thermal entropy;
\item[(ii)] $\kappa_{c} \ge 1/(4\ln 2)$, with equality if and only if every counted mode has zero Killing weight. The capacity-convention residue of T08, and with it the registered value $\nu = 1/(16\pi\ln 2)$ of the boundary-mode prediction, is therefore, under this hypothesis, equivalent to the counted modes being at zero weight, maximally mixed; a count that includes modes of nonzero weight needs more of them;
\item[(iii)] $\ln 2$ enters the residue as the entropy of a maximally mixed fermion, as T08's own remark on $\nu$ records, not through any count, which is consistent with T08's proof that no rational recount of the exceptional set reaches $1/(4\ln 2)$;
\item[(iv)] the same holds at the cosmological horizon under (P) and (R$_{\Lambda}$) (Premise \claimref{synthesis.r-lambda-regularity-cosmological-horizon}), with $S_{\Lambda} = \pi N^{2}$ (Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}) and the temperature $\kappa_{\Lambda}/2\pi$ (Theorem \claimref{synthesis.de-sitter-temperature-frozen-point-norm}) in place of the hole's: if the cosmological horizon's counted modes carry its entropy, $|J| > \pi N^{2}/\ln 2$, strictly, since the Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes} requires $\omega_{j} > 0$; under the hypothesis the capacity value of Theorem \claimref{synthesis.de-sitter-mode-count} is then excluded;
\item[(v)] (the energy tension) for $x > 0$, $\beta\omega n < s(x)$, so the counted modes' Killing excitation energy $E$ satisfies $\beta E < \sum_{j} s(x_{j}) = A/4$, that is $E < TS = M/2$, and $E = 0$ in the equality case of (ii): the internal energy $M$ of Theorem \claimref{synthesis.quarter-from-temperature} is not the counted modes' energy, and read literally the two hypotheses together exclude the equality case of (ii);
\item[(vi)] (Premise (Q) taken literally) with the weights $\omega_{k} = \kappa k$ of (Q), one zero-weight mode per array and the rest at $x = 2\pi|k|$, an array carries $\ln 2 + \varepsilon$ nats, $\varepsilon = 2\sum_{k \ge 1} s(2\pi k) \in (0.02724, 0.02726)$, so $\ln 2 + \varepsilon \in (0.7203, 0.7205)$. Counting every mode of an array drives $\langle s\rangle$ to $0$ and $\kappa_{c}$ upwards; counting arrays gives $1/(4(\ln 2 + \varepsilon)) \in (0.3469, 0.3471)$ arrays per Planck area per period, against the registered $1/(4\ln 2) = 0.3607$; counting only the zero-weight modes leaves $\varepsilon$ nats per array outside $A/4$. So no reading of (Q) reproduces the registered value.
\end{enumerate}
Under this hypothesis the residue is equivalent to the Killing weights of the counted modes, with the registered value as its zero-weight extreme. The hypothesis $\sum_{j} s(x_{j}) = A/4$ is the area-law condition that T08's circularity fence holds under test, so this is a conditional reformulation, not an admissible derivation of the residue from the structure of the boundary modes, and it neither meets nor fails the kill condition of the boundary-mode prediction. By (vi), were Premise (Q) promoted to a derivation, it would return a residue other than the registered one, and the kill condition would then refute (IC). The weights, and which modes are counted, remain open.

## technical
The entropy paper leaves one number undetermined, the calibration residue: how many boundary modes are counted per Planck area of horizon in each modular period. It also proves that no rational recount of cells can give the value it needs. Here the residue is re-expressed, under one hypothesis: that the counted modes carry the hole's thermodynamic entropy, which the series' temperature fixes at a quarter of the area. Each mode at that temperature carries at most $\ln 2$, and exactly $\ln 2$ only at zero energy. So the residue is the reciprocal of four times the average entropy per counted mode. It is at least $1/(4\ln 2)$, and equals the registered value $1/(4\ln 2)$ precisely when every counted mode has zero energy.

The $\ln 2$ is the entropy of one maximally mixed fermion, as the entropy paper itself remarks, which is consistent with its proof that no counting rule produces it. At the cosmological horizon the count is strictly above $\pi N^{2}/\ln 2$, since its modes have nonzero weight. Two cautions. The counted modes' energy is below half the hole's mass, and zero at the registered value, so the mass is not their energy. And the hypothesis is the very area-law match the entropy paper holds under test, so this re-expresses the residue rather than deriving it. Taken literally, the singularity paper's s-wave weights give $0.3470$ arrays per Planck area per period, not the registered $0.3607$, whichever modes are counted: if those weights were ever promoted to a derivation, the boundary-mode prediction's kill condition would refute the intrinsic-clock premise.

## lay
The series needs one number to turn its count of a black hole's boundary modes into the hole's entropy. That number could not be found by counting, and the series proved it never could be. This result re-expresses that number. It is really about how much information each mode holds, and a mode holds its maximum, one bit, only if it carries no energy. If the counted modes are exactly the zero-energy ones, the number takes the value the series registered as a prediction; if some carry energy, more modes are needed. So the open question becomes a sharper one: which modes are counted, and what energies do they carry? The one energy assignment the series has, its s-wave convention, gives a number about four per cent below the registered prediction.

## one-liner
If the counted boundary modes carry the entropy $A/4$, the residue is $1/(4\langle s\rangle) \ge 1/(4\ln 2)$, the registered value exactly at zero weight; the s-wave weights of (Q) give $0.3470$ instead, so the residue is re-expressed, not derived.
