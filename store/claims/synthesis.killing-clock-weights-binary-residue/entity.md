---
id: synthesis.killing-clock-weights-binary-residue
kind: claim
version: 4
title: 'Killing-clock weights make the residue binary'
status: proved
region: synthesis
subject: entropy
tags: [mode-counting, boundary-modes, undetermined-input, forcing-and-uniqueness, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 4
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.singularity.geometric-modular-condition-g
- obj.synthesis.cosmological-horizon-boundary-modes
derivations:
- name: main
  uses:
  - scrambling.clock-inventory-boundary-modes@5
  - hawking.modular-structure-completed-pair@3
  - scrambling.boundary-mode-space-matrix@4
  - singularity.plane-rate@4
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.residue-from-mode-entropy@4
  - synthesis.residue-common-weight-particle-hole@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_mode_algebra_and_unit_rapidity
- kind: check
  ref: check.py::check_clock_forces_binary_weights
- kind: check
  ref: check.py::check_q_weights_not_a_clock
- kind: check
  ref: check.py::check_binary_residue
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.residue-from-mode-entropy
  - singularity.q-joint-quasi-freeness-s-wave
  - obj.synthesis.cosmological-horizon-boundary-modes
outside_ga:
  kind: complex-analysis
  why: 'the Killing flow Ad(e^{it sum omega_j K_j}), K_j = sigma_j/2, acts on the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares'
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced; every bare i stays and is declared outside_ga (complex-analysis): the Killing flow Ad(e^{it sum omega_j K_j}), K_j = sigma_j/2, acts on the boundary-mode algebra, whose modes descend from the atom of the spacetime radial plane and anticommute with I_4 (conventions, known limits 1 and 2), as its defining object declares.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 1 -> 2, note only, statement and proof unchanged. Clause (v) concerns Premise (Q) version 2''s weights kappa k. Premise (Q) version 3 (Leon''s decision of 23 October) takes kappa(k + 1/2). For those weights (K1) holds exactly on windows whose weights share one magnitude, a single mode or a particle-hole pair {k, -1-k}, with c = |k + 1/2|, and (K2) fails on every window, since no weight has magnitude kappa: the weights of (Q) version 3 and (K) are incompatible on every window. In (iii) and (iv) the registered value needs zero-weight counted modes when each counted unit is one mode; under (Q) version 3 the registered residue is also realised, outside (K), by two arrays at nonzero weights (synthesis.half-integer-weight-array-carries-half-ln2 (iii)). Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 2 -> 3.'
  open_problem: op.residue-killing-weights
  note: >-
    Attacks the first bullet of the problem (the weights from the boost generator, not from (Q))
    with the store's own clock inventory. The weights of the geometric modular condition are
    free; requiring that the Killing flow on the counted modes be a clock, the flows the
    inventory converts to Schwarzschild time at the one surface gravity, leaves each counted mode
    two options, moved at x = 2 pi or fixed at x = 0. The residue then lies on one curve in the
    moved fraction, and under rotation invariance takes one of two values. The completed pairs of
    the boost planes are moved, so the registered value needs counted modes the Killing clock
    fixes. Representation theory on the transport's completed pairs: transport-convenient, with
    clause (ii) resting on the completed pair the transport adjoins. Conditional on (K) and, for
    (iii) and (iv), on the area-law hypothesis; it does not settle the residue.
---

## formal
Let the counted boundary modes of a window be $n$ completed pairs $(v_{j}, v_{j}^{*})$, with $N_{j} = v_{j}^{*}v_{j}$ and boost generators $K_{j} = \sigma_{j}/2 = N_{j} - \tfrac12$ (Proposition \claimref{hawking.modular-structure-completed-pair}), and let the Killing flow on them be $\operatorname{Ad}(e^{it\sum_{j}\omega_{j}K_{j}})$ in Schwarzschild time, with the weights $\omega_{j}$ of Definition \claimref{obj.singularity.geometric-modular-condition-g}. In rapidity $\lambda = \kappa t$ (Proposition \claimref{singularity.plane-rate}) its real generator is $X = \sum_{j}(\omega_{j}/\kappa)K_{j}$, with $\operatorname{ad}_{X}v_{j} = -(\omega_{j}/\kappa)v_{j}$ and $\operatorname{ad}_{X}v_{j}^{*} = (\omega_{j}/\kappa)v_{j}^{*}$. Assume

(K) $X$ is a clock in the sense of Lemma \claimref{scrambling.clock-inventory-boundary-modes}(ii) at unit rapidity, which is two assumptions: (K1) the nonzero adjoint eigenvalues of $X$ on the mode operators have one magnitude; (K2) that magnitude is one in the Killing flow's own rapidity $\lambda = \kappa t$, the parameter that Proposition \claimref{singularity.plane-rate} converts to Schwarzschild time. The Lemma normalises a clock's parameter by convention, which rescales $X$ and does not constrain the weights of a given flow, so (K2) is a separate assumption: Proposition \claimref{singularity.plane-rate} supports it for pairs in the boost plane, and for any other counted mode it is assumed. Under (K1) alone the statements below hold with $\pm c\kappa$ in place of $\pm\kappa$ for one $c > 0$, and the moved value $s(2\pi)$ becomes $s(2\pi c)$.

Then:
\begin{enumerate}
\item[(i)] (two weights) every counted mode has $\omega_{j} \in \{-\kappa, 0, \kappa\}$, so $x_{j} = 2\pi\omega_{j}/\kappa \in \{-2\pi, 0, 2\pi\}$: a counted mode is either moved by the clock, at $|x_{j}| = 2\pi$, or fixed by it, at $x_{j} = 0$. Without (K) the weights are free, and a diagonal generator with two distinct nonzero $|\omega_{j}|$ has no common rapidity (Lemma \claimref{scrambling.clock-inventory-boundary-modes}(iii));
\item[(ii)] (the pairs of the flow's own plane are moved) a counted mode whose ladder is a completed pair in the plane of the flow's bivector, as for the Definition's flow, whose bivector at every point of $E$ is $\sigma_{r}$, and for each mode of Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes}, a copy of the Killing plane's pair, is moved: the pair diagonalises the boost with weights $-1, +1$ (Proposition \claimref{hawking.modular-structure-completed-pair}(2)), so $\omega_{j} = \pm\kappa$. Zero weight needs a counted mode on which the Killing clock acts trivially;
\item[(iii)] (one curve) under the hypotheses of Theorem \claimref{synthesis.residue-from-mode-entropy}, with $f \in [0,1]$ the fraction of counted modes the clock moves and $s$ the mode entropy of Theorem \claimref{synthesis.boundary-mode-thermal-entropy},
\[
\kappa_{c} \;=\; \frac{1}{4\bigl((1 - f)\ln 2 + f\,s(2\pi)\bigr)} ,
\]
strictly increasing in $f$: $\kappa_{c} = 1/(4\ln 2)$, the registered value, exactly when $f = 0$, and $\kappa_{c} = 1/(4s(2\pi)) \in (18.413, 18.414)$ when $f = 1$, larger than the registered value by the factor $\ln 2/s(2\pi) \in (51.05, 51.06)$;
\item[(iv)] (binary under rotation invariance) under the hypotheses of Theorem \claimref{synthesis.residue-common-weight-particle-hole}(i) the counted modes share one weight, so $f \in \{0, 1\}$ (this split is that theorem's; (K) fixes the moved value at $x = 2\pi$): the residue is $1/(4\ln 2)$ if the Killing clock fixes the counted modes and $1/(4s(2\pi))$ if it moves them, and by (ii) the second case holds when the counted modes are completed pairs of the boost planes;
\item[(v)] ((Q) is not a clock) the weights $\omega_{k} = \kappa k$ of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave} on an array $k = -j, \ldots, j$ form a clock for $j = 1$ and for no $j \geq 2$: on an array with some $|k| \geq 2$ the s-wave weights and (K) are incompatible;
\item[(vi)] (de Sitter) for the boundary modes of the cosmological horizon, $\omega_{j} > 0$ by Definition \claimref{obj.synthesis.cosmological-horizon-boundary-modes}, and (K) gives $\omega_{j} = \kappa_{\Lambda}$ for every $j$; under the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy}(iv), $|J| = \pi N^{2}/s(2\pi)$, with $|J|/(\pi N^{2}) \in (73.65, 73.66)$.
\end{enumerate}
So (K) fixes the weights, which the Definition leaves free, up to one binary choice per mode, and the question which modes are counted becomes whether the Killing clock moves them. This does not derive the residue: (K) is a hypothesis that the series does not make, (iii), (iv) and (vi) inherit the area-law hypothesis, and which modes are counted stays open.

## technical
The series leaves the Killing weights of the counted boundary modes free, and the calibration residue depends on them: under the area-law hypothesis it is the reciprocal of four times the counted modes' mean thermal entropy, at its registered value exactly when every counted mode has zero weight. Here the weights are constrained by an extra assumption, not made in the series, phrased with the store's clock inventory: the Killing flow on the counted modes is a clock (every mode it moves, it moves at one common rapidity) and that rapidity is the flow's own, $\lambda = \kappa t$. Under it each mode has two options, moved at weight $\pm\kappa$ (so $x = 2\pi$ and entropy $s(2\pi)$, between $0.013577$ and $0.013578$ nats) or fixed at weight zero (entropy $\ln 2$). With the common magnitude left free the moved weight is $\pm c\kappa$ instead.

So, under the area-law hypothesis, the residue lies on one curve, $1/(4((1-f)\ln 2 + f\,s(2\pi)))$ in the moved fraction $f$: the registered $1/(4\ln 2)$ when no counted mode is moved, between $18.413$ and $18.414$ when all are. The rotation invariance of the stored common-weight theorem already forces one common weight, so only the two end values remain; the assumption fixes the second of them. A completed pair lying in the plane of the boost is always moved, with weights $\mp 1$, so if the counted modes are the completed pairs of the boost planes, as the geometric modular condition and the de Sitter definition describe them, and the assumption holds, the residue is the second value; the registered value needs counted modes that the Killing clock leaves fixed. The s-wave weights $\kappa k$ of premise (Q) are not a clock on any array containing $|k| \ge 2$. At the cosmological horizon the clock gives every mode weight $\kappa_{\Lambda}$, so the entropy $\pi N^{2}$ needs $\pi N^{2}/s(2\pi)$ modes.

## lay
How much information a black hole's counted boundary modes hold depends on the energy each one carries, and the series never fixed those energies. This result fixes them under an extra assumption, not made in the series: that the hole's time flow runs every mode it moves at one common rate, the rate of the flow itself. Then each mode either carries exactly one unit of the hole's natural energy or none at all. The modes with none hold a full bit each and give the number the series registered as a prediction; the modes with one unit hold less than a fiftieth of a bit, and if every counted mode were of that kind the number would be more than fifty times larger. If the counted modes are the pairs built in the plane of the time flow, and the assumption holds, they are of the moving kind and the registered value is not obtained; it needs counted modes that the time flow leaves untouched. The result also relies on the area law, which the series holds under test. Which modes are counted stays open, but the question is now a yes-or-no one for each mode.

## one-liner
If the Killing flow on the counted modes is a clock at unit rapidity, each mode has weight $0$ or $\pm\kappa$, so under the area-law hypothesis the residue is $1/(4((1-f)\ln 2 + f\,s(2\pi)))$ in the moved fraction $f$, binary under rotation invariance ($1/(4\ln 2)$ or $1/(4s(2\pi))$), and the boost-plane pairs are moved.
