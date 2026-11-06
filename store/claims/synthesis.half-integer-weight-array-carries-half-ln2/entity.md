---
id: synthesis.half-integer-weight-array-carries-half-ln2
kind: claim
version: 4
title: 'With half-integer weights the s-wave array carries half of ln 2'
status: proved
region: synthesis
subject: entropy
tags: [mode-counting, boundary-modes, bosonisation, counting-rules, undetermined-input, needs-continuum]
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
review: draft
derivations:
- name: main
  uses:
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.residue-from-mode-entropy@4
  - state-selection.where-fermi-dirac-comes@5
  - singularity.bosonisation-bridge-s-wave-sector@7
  - synthesis.imported-theta-function-identities@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_half_offset_half_bit
- kind: check
  ref: check.py::check_zero_offset_value
- kind: check
  ref: check.py::check_recurrence_signs
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - singularity.q-joint-quasi-freeness-s-wave
  - synthesis.residue-from-mode-entropy
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2 -> 3, note only, statement and proof unchanged. The text identifies delta = 0 as the weight convention of Premise (Q); that is (Q) version 2. Premise (Q) version 3 (Leon''s decision of 23 October) adopts delta = 1/2, the offset whose array entropy (1/2) ln 2 is computed in (i), as a consequence of reading the modes as spinor fields of boost weight 1/2 under (N+). Under version 3, (i) is the array entropy of the adopted premise and (iii) its count: two arrays carry one registered mode''s ln 2, with no zero-weight mode. The closing sentence (which offset the modes have is not decided here) remains true of this theorem; the offset is now fixed by decision, not by derivation. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 3 -> 4.'
  maintainer_pass_2026_10_22:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Maintainer pass: the theta-function identities, cited from memory, are now the imported Fact synthesis.imported-theta-function-identities, added to uses and cited in the statement, proof and check; the condition leaves the title and the formal, technical and one-liner levels still name the import (the rigorous 10^-57 bound needs none). Version 1 -> 2.'
  open_problem: pr.q-quasi-freeness
  note: >-
    Bears on the weight half of (Q). Theorem synthesis.residue-from-mode-entropy(vi) shows that
    no reading of (Q)'s weights kappa k reproduces the registered residue. The weights kappa k
    are one of two particle-hole symmetric offsets of an evenly spaced array (the classification
    is clause (iv) of synthesis.q-splits-maximum-entropy-affine-weights, filed alongside); the
    other, kappa(k + 1/2), puts the sea level between two sites and has no zero-weight mode. For
    that offset the array's thermal entropy at the Hawking temperature is exactly ln 2 / 2, by
    Jacobi's theta-function identities at the self-dual point tau = i (the imported Fact
    synthesis.imported-theta-function-identities); independently of them it is within 10^-57 of
    ln 2 / 2 by rigorous rational bounds. Under the entropy-matching hypothesis two such arrays
    carry the capacity of one registered boundary mode. Which units are counted, and which offset
    is right, remain open: this is a computation, not a derivation of the residue, and it does not
    identify arrays with helicity channels. Transport-absent except for the rotor sign.
---

## formal
Let $\{\psi_{k}\}_{k \in \Z}$ be the fermion array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector} with evenly spaced weights $\omega_{k} = \kappa(k + \delta)$, $\delta \in \{0, \tfrac12\}$, in the quasi-free state with the marginals of (P) and (R), so that mode $k$ has $x_{k} = 2\pi\omega_{k}/\kappa = 2\pi(k + \delta)$ and entropy $s(x_{k})$ (Theorem \claimref{synthesis.boundary-mode-thermal-entropy}); write $S_{\delta} := \sum_{k \in \Z}s(x_{k})$ for the entropy of one array. The value $\delta = 0$ is the weight convention of Premise \claimref{singularity.q-joint-quasi-freeness-s-wave}; $\delta = \tfrac12$ places the sea level midway between two sites. Then:
\begin{enumerate}
\item[(i)] $S_{1/2} = 2\sum_{k \geq 0}s((2k + 1)\pi) = \tfrac12\ln 2$ exactly, by the classical identities of the Jacobi theta functions and the Dedekind eta function (Fact \claimref{synthesis.imported-theta-function-identities}: Jacobi's quartic identity $\vartheta_{3}^{4} = \vartheta_{2}^{4} + \vartheta_{4}^{4}$, the identity $\vartheta_{2}\vartheta_{3}\vartheta_{4} = 2\eta^{3}$, and the behaviour of $\vartheta_{2}, \vartheta_{3}, \vartheta_{4}, \eta$ under $\tau \mapsto -1/\tau$); without those identities, $|S_{1/2} - \tfrac12\ln 2| < 10^{-57}$ by rigorous rational bounds;
\item[(ii)] $S_{0} = \ln 2 + 2\sum_{k \geq 1}s(2\pi k) \in (0.720396698946605, 0.720396698946606)$, the value $\ln 2 + \varepsilon$ of Theorem \claimref{synthesis.residue-from-mode-entropy}(vi), and $1/(4S_{0}) \in (0.3470310, 0.3470311)$;
\item[(iii)] under the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy} with whole arrays as the counted units, the number of arrays per Planck area per modular period is $1/(4S_{\delta})$: for $\delta = \tfrac12$ this is $1/(2\ln 2)$ (given (i); to relative accuracy $10^{-56}$ without the identities), twice the registered density $1/(4\ln 2)$ of boundary modes, so that two arrays carry the capacity $\ln 2$ of one registered boundary mode; for $\delta = 0$ it is the value in (ii), which is not a multiple $p/q$ of $1/(4\ln 2)$ with $q \le 4$.
\end{enumerate}
For $\delta = \tfrac12$ the Killing flow at one modular period is the parity automorphism (filed alongside, synthesis.q-splits-maximum-entropy-affine-weights, clause (iv)); this is the sign that one Euclidean period carries on the odd sector, $R_{2\pi} = -1$ (Proposition \claimref{state-selection.where-fermi-dirac-comes}), whereas for $\delta = 0$ the flow at one modular period is the identity. This identifies a property of the offset left open by (Q), not a derivation of the residue: which units are counted, and which offset the boundary modes have, are not decided here.

## technical
The weights $\omega_k = \kappa k$ of Premise (Q) are one of two evenly spaced, particle-hole symmetric ways to lay out the s-wave fermion array; the other shifts every weight by $\kappa/2$, so that the sea level falls between two modes and no mode has zero weight. The store's reformulation of the calibration residue showed that the first choice, read literally, misses the registered value: one array carries $\ln 2 + \varepsilon$ nats at the Hawking temperature, between $0.7203966$ and $0.7203967$.

For the second choice the array carries exactly $\tfrac12\ln 2$. The array's partition function at the Hawking temperature is the ratio $\vartheta_{3}/\eta$ at the point $\tau = i$, where the time after which the array's flow returns to itself equals the thermal period; that ratio is invariant under the exchange of the two periods, which removes the energy term from the entropy, and the classical theta identities give the ratio $\sqrt{2}$ there. Independently of those identities, rigorous rational bounds place the entropy within $10^{-57}$ of $\tfrac12\ln 2$. Under the entropy-matching hypothesis, two such arrays carry exactly the capacity of one registered boundary mode. The second choice also matches the series' account of why the spectrum is Fermi-Dirac: after one modular period its flow is minus the identity on the fermions, the sign one Euclidean period carries; its weights $\kappa(k + \tfrac12) = 2\pi T_{\mathrm{H}}(k + \tfrac12)$ are the fermionic Matsubara frequencies, while (Q)'s $\kappa k$ are the bosonic ones.

## lay
The series models the quantum modes at a black hole's boundary as an evenly spaced ladder of energies, and one of its assumptions fixes where the ladder sits: with a rung at exactly zero energy. The other natural choice puts zero midway between two rungs. This result computes what that second choice would mean. At the Hawking temperature each ladder then holds exactly half a bit of entropy, a consequence of classical identities of special functions, so two ladders hold one bit, the amount the series assigns to each counted boundary mode; with the series' current choice no whole number of ladders matches. The second choice also fits the series' explanation of why the radiation obeys fermion statistics. It does not settle which choice nature makes or what is being counted.

## one-liner
With weights $\kappa(k + \tfrac12)$ the s-wave array's entropy at the Hawking temperature is exactly $\tfrac12\ln 2$ by the imported classical theta-function identities (within $10^{-57}$ by rigorous bounds without them), so two arrays carry one registered boundary mode's $\ln 2$ under entropy matching; with (Q)'s weights $\kappa k$ it is $\ln 2 + \varepsilon$.
