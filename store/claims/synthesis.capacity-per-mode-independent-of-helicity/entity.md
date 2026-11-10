---
id: synthesis.capacity-per-mode-independent-of-helicity
kind: claim
version: 2
title: The capacity per boundary mode does not depend on the helicity reading
status: proved
region: synthesis
subject: entropy
tags: [boundary-modes, mode-counting, ladder-pairs, counting-rules]
proposed_by:
  kind: ai
  session: colony-2026-10-22
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
  - scrambling.pair-mode-qubit-one-object@5
  - synthesis.residue-from-mode-entropy@4
  - scrambling.residue-each-convention@4
  - scrambling.mode-count@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_mode_one_qubit
- kind: check
  ref: check.py::check_grouping_rescales_unit_only
- kind: proof
  derivation: main
extraction:
  maintainer_pass_2026_10_22:
    by: ai-maintainer-pass
    note: 'W503: the lay level now states the entropy-matching hypothesis of synthesis.residue-from-mode-entropy under which clauses (ii) and (iii) hold.'
  open_problem: op.helicity-per-boundary-mode
  note: >-
    Narrows op.helicity-per-boundary-mode (the factor-of-two half is a choice of unit) without
    resolving it: its success criterion, J3 proved, is untouched. The factor-of-two half: the capacity per boundary mode
    is ln 2 because a boundary mode is one ladder pair (scrambling.pair-mode-qubit-one-object), not
    because of the helicity lift, so in the capacity convention, under the entropy-matching
    hypothesis of synthesis.residue-from-mode-entropy, the residue's value and the registered
    nu = 1/(16 pi ln 2), both counts of ladder pairs, do not depend on joint J3. In the Fock reading
    two helicity channels have four joint occupation states, that is two ladder pairs, so "one mode
    carries both helicities" means two ladder pairs counted as one unit: the residue per such unit is
    halved and the ladder-pair density unchanged. J3 itself, the channel identification (whether the
    horizon's A/4 is matched by one or two helicity channels per (omega, l, m)), stays open. Housekeeping consequence for the maintainer:
    clause (iv) of scrambling.residue-each-convention reaches its value through the collar Fact,
    which bundles the coframe weights with the J3 lift; re-deriving (iv) from
    scrambling.pair-mode-qubit-one-object would remove J3 from the holds-given of
    pred.boundary-mode-density along that route.
---

## formal
A boundary mode is one ladder pair (Proposition \claimref{scrambling.pair-mode-qubit-one-object}): its state space is two-dimensional and its maximal entropy is $\ln 2$, whatever it registers. Hence:
\begin{enumerate}
\item[(i)] Under either reading of the helicity lift the capacity of one boundary mode is $\ln 2$. In the Fock reading a helicity channel's two states are empty and occupied, so two helicity channels have four joint occupation states, that is two ladder pairs; a capacity $2\ln 2$ is the capacity of such a unit of two ladder pairs, which is two boundary modes in the sense of Proposition \claimref{scrambling.pair-mode-qubit-one-object}, not one.
\item[(ii)] Under the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy}, group the counted ladder pairs into units of $h$ pairs ($h = 1$: one helicity per unit; $h = 2$: both helicities of a species per unit). The residue per unit is $\kappa_{c}^{(h)} = 1/(4\langle s\rangle_{h}) = \kappa_{c}^{(1)}/h \ge 1/(4h\ln 2)$, with equality exactly when every ladder pair is maximally mixed. The number of ladder pairs per Planck area per modular period, the equality case, and the registered mode density $\nu$ of Theorem \claimref{scrambling.mode-count} (fermionic modes per Planck cell) are the same for $h = 1$ and $h = 2$.
\item[(iii)] Consequently, in the capacity convention and under the hypothesis of Theorem \claimref{synthesis.residue-from-mode-entropy}, the values $\kappa_{c} = 1/(4\ln 2)$ and $1/(8\ln 2)$ of the capacity convention (Proposition \claimref{scrambling.residue-each-convention}(ii), (iv)) are one count of ladder pairs expressed in two units, not two physical alternatives, and the value per boundary mode, $1/(4\ln 2)$, follows from Proposition \claimref{scrambling.pair-mode-qubit-one-object} without the channel identification J3. What J3 decides is how ladder pairs group into the $(\omega, \ell, m, s)$ channels of a species, and so whether the horizon's entropy is matched by one or two helicity channels per $(\omega, \ell, m)$, a field-theory question this result does not settle.
\end{enumerate}

## technical
A boundary mode is one creation-annihilation pair, a qubit, so its entropy is at most $\ln 2$ however the helicity question is answered. Two helicity channels, each empty or occupied, have four joint states, which is two ladder pairs; a capacity of $2\ln 2$ belongs to two pairs counted as one unit. Under the entropy-matching hypothesis of the reformulated residue, grouping the counted pairs into units of two halves the residue per unit and leaves the number of pairs per Planck area, the equality case and the registered mode density unchanged.

So in the capacity convention the residues $1/(4\ln 2)$ and $1/(8\ln 2)$ are one count in two units. The value per boundary mode follows from the identity of a boundary mode with a ladder pair, not from the helicity lift, and joint J3 decides how the pairs group into the field's channels, including how many helicity channels per partial wave match the horizon's entropy.

## lay
A question left open was whether one of the series' black-hole boundary modes stores one polarisation of a massless particle or both, which seemed to change a key calibration number by a factor of two. It does not. Each boundary mode is a single quantum bit, so it holds at most one bit of entropy whichever way the polarisations are assigned; two polarisations need two bits. Counting pairs of modes as one unit halves the number of units but not the number of bits. In the counting the series uses, and assuming the horizon's entropy is matched by its modes' entropy (the hypothesis behind the calibration), the predicted number of such bits on each patch of horizon is the same either way. Which polarisations of which particles those bits correspond to is still an open field-theory question.

## one-liner
A boundary mode is one ladder pair, so its capacity is $\ln 2$ under either helicity reading; $1/(4\ln 2)$ and $1/(8\ln 2)$ are one ladder-pair count in two units, and in the capacity convention the registered density $\nu$, a count of ladder pairs, does not depend on J3.
