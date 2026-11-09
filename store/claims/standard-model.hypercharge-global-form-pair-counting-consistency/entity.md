---
id: standard-model.hypercharge-global-form-pair-counting-consistency
kind: claim
version: 5
title: Hypercharge from the global form, pair counting, and consistency
status: proved
region: standard-model
subject: standard-model
tags:
- hypercharge-and-anomalies
- recovers-known-physics
- forcing-and-uniqueness
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T12, deposited version
review: typed
derivations:
- name: main
  uses:
  - standard-model.chirality-two-halves-spinor-module-conjugation@6
  - standard-model.imported-anomaly-coefficients@1
  - standard-model.imported-pair-systems-two-chirality-halves@5
  - standard-model.quarks-leptons-two-level-fermion-content@5
  - standard-model.hyp-s-slot-statistics@10
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T12.py
  tags:
  - label:thm:hypercharge
- kind: check
  ref: check.py::check_orientation_fixed_by_anomaly
- kind: check
  ref: check.py::check_one_handed_singlet_spectrum
- kind: check
  ref: check.py::check_anomaly_free_and_unique
- kind: check
  ref: check.py::check_hypotheses_necessary
locators:
  paper: T12
  number: Thm 5.5
  label: thm:hypercharge
  line: 1119
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the listing orientation by the anomaly, the one-handed singlet spectrum, anomaly freedom with uniqueness as an exact polynomial, and the necessity of both hypotheses. Version 4 -> 5.'
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: Converted the twistor-level doublets, the full and empty twistor, the single-twistor Fock space
      and the halves T, T' to conformal-spinor language and S, S' at every level and in the proof; the
      anomaly arithmetic is untouched.
  source_title: Hypercharge from the global form, pair counting, and consistency
  source_formal: 'With $Y$ the hypercharge defined before Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content},
    and with Hypothesis (S) wherever a twistor-level doublet enters:

    \begin{enumerate}

    \item (Under (S).) The one-handed listing keeps the states of even total mode number and conjugates
    the odd ones, or the reverse; the choice is the particle-antiparticle orientation. Write $(j, k)$
    for the component of the five-mode state space with $j$ slot modes and $k$ pair modes occupied (mode
    counts, not the pair of representation dimensions used elsewhere in this paper, for which see the
    caption of Figure \ref{fig:hierarchy}). In the listing that keeps the quark doublet, the component
    $(1,1)$, as a particle, the lepton doublet is the full twistor, the component $(1,3)$, $Y_{L} = -1/2$,
    and the empty twistor, the component $(1,0)$, appears only as its conjugate. The $[SU(2)]^{2}U(1)$
    anomaly coefficient of the two doublets, $3Y_{Q} + Y_{L}$ with the three the colour multiplicity,
    is then the identity $3 \cdot \tfrac16 - \tfrac12 = 0$; it would equal $1$ if the empty twistor were
    listed as the particle instead, so the anomaly confirms the orientation the listing fixed. Pair counting
    fixes $|Y_{L}/Y_{Q}| = 3$; the parity fixes the sign.

    \item (Unconditional as a computation on the single-twistor Fock space, like Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3).)
    Listed by the handedness of (1), the single-twistor sector gives the singlet spectrum. Here $\T =
    \Lambda^{\mathrm{even}}W$ and $\T'' = \Lambda^{\mathrm{odd}}W$ are the two chirality halves (Fact
    \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the listing keeping the
    even grades and conjugating the odd ones gives

    \[

    (1)_{0} \;\oplus\; (\bar{3})_{-2/3} \;\oplus\; (\bar{3})_{+1/3} \;\oplus\; (1)_{+1},

    \]

    that is $\nu^{c}$, $u^{c}$, $d^{c}$, $e^{c}$ with hypercharges $0, -\tfrac23, +\tfrac13, +1$: the
    observed singlet spectrum, with the fourth singlet at hypercharge zero. (The listing by the opposite
    handedness is the conjugate of this one, the same spectrum in the opposite convention.) Under (S)
    the single-twistor grade-$k$ states are the $(0, k)$ components, the states with no slot mode and
    $k$ pair modes occupied (their content $\Lambda^{k}\C^{3}$ and weight $-2k$ match, and irreducibles
    are determined by content and weight), so their parity is the total parity and this listing is the
    same listing as in (1).

    \item (Consistency, and uniqueness given the content; under (S) for the doublets.) With the content
    of (1) and (2), all four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients}
    hold. Conversely, for the field content $Q = (2,3)$, $L = (2,1)$, $u^{c} = (1,\bar{3})$, $d^{c} =
    (1,\bar{3})$, $e^{c} = (1,1)$, all listed in one handedness, together with a fourth singlet of hypercharge
    zero or no fourth singlet, and $Y_{Q} = 1/6$ as the normalisation, the four conditions determine $Y_{L}$,
    $Y(e^{c})$ and $\{Y(u^{c}), Y(d^{c})\}$ uniquely, and the solution is the spectrum of (1) and (2).
    Both hypotheses are necessary: with a fourth singlet of unconstrained hypercharge the conditions admit
    a one-parameter family, and if the doublets were listed in the opposite handedness from the singlets
    the $[SU(3)]^{2}U(1)$ and cubic sums would be $-\tfrac23$ and $+\tfrac49$ rather than zero.

    \end{enumerate}'
  env: theorem
  typing:
    by: ai-typing-pass
    note: 'All four existing edges are premises cited in the proof and were kept; Hypothesis (S) is not
      a store entity, and the paper gives no standard-route sentence for the anomaly uniqueness. Hypothesis
      pass: assumes standard-model.hyp-s-slot-statistics added because its statement holds under Hypothesis
      (S). Levels pass: lay now keeps the handedness, normalisation and fourth-singlet hypotheses of the
      uniqueness clause.'
    added:
    - standard-model.hyp-s-slot-statistics
  small_findings_pass:
    by: ai-small-findings-pass
    date: '2026-10-22'
    finding: CONTRADICTIONS_STRUCTURE M3
    note: 'Namesake note added: "empty/full conformal spinor" here are the (1,0) and (1,3) doublet components;
      T15 uses "empty/filled conformal spinor" for the grade-zero and grade-three singlets. Content unchanged.'
    open_problem: op.small-findings
  open_problem: op.small-findings
  context_refs:
  - neutrino.empty-twistor
  maintainer_pass:
    by: maintainer-2026-10-22
    date: '2026-10-22'
    note: 'Hypothesis (S) (standard-model.hyp-s-slot-statistics) is now a proved claim derived from the new postulate standard-model.slot-module-hypothesis (Leon''s decision to restate (S) as the weaker constituent hypothesis), so the edge to it moves from assumes to uses, pin unchanged; the content of this entity is unchanged and its holds_given now reaches the slot-module hypothesis through (S).'
---

## formal
With $Y$ the hypercharge defined before Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}, and with Hypothesis (S) wherever a doublet at the level of one conformal spinor (a twistor-level doublet) enters:
\begin{enumerate}
\item (Under (S).) The one-handed listing keeps the states of even total mode number and conjugates the odd ones, or the reverse; the choice is the particle-antiparticle orientation. Write $(j, k)$ for the component of the five-mode state space with $j$ slot modes and $k$ pair modes occupied (mode counts, not the pair of representation dimensions used elsewhere in this paper, for which see the caption of Figure \ref{fig:hierarchy}). In the listing that keeps the quark doublet, the component $(1,1)$, as a particle, the lepton doublet is the full conformal spinor, the component $(1,3)$, $Y_{L} = -1/2$, and the empty conformal spinor, the component $(1,0)$, appears only as its conjugate (here both phrases name doublet components of the one-slot listing; the neutrino paper uses ``empty'' and ``filled conformal spinor'' for the grade-zero and grade-three singlets of the single-spinor sector, different objects, Proposition \claimref{neutrino.empty-twistor}). The $[SU(2)]^{2}U(1)$ anomaly coefficient of the two doublets, $3Y_{Q} + Y_{L}$ with the three the colour multiplicity, is then the identity $3 \cdot \tfrac16 - \tfrac12 = 0$; it would equal $1$ if the empty conformal spinor were listed as the particle instead, so the anomaly confirms the orientation the listing fixed. Pair counting fixes $|Y_{L}/Y_{Q}| = 3$; the parity fixes the sign.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, like Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3).) Listed by the handedness of (1), the sector of a single conformal spinor gives the singlet spectrum. Here $\CS = \Lambda^{\mathrm{even}}W$, the conformal spinor space, and $\CSm{} = \Lambda^{\mathrm{odd}}W$ are the two chirality halves (Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the listing keeping the even grades and conjugating the odd ones gives
\[
(1)_{0} \;\oplus\; (\bar{3})_{-2/3} \;\oplus\; (\bar{3})_{+1/3} \;\oplus\; (1)_{+1},
\]
that is $\nu^{c}$, $u^{c}$, $d^{c}$, $e^{c}$ with hypercharges $0, -\tfrac23, +\tfrac13, +1$: the observed singlet spectrum, with the fourth singlet at hypercharge zero. (The listing by the opposite handedness is the conjugate of this one, the same spectrum in the opposite convention.) Under (S) the grade-$k$ states of a single conformal spinor are the $(0, k)$ components, the states with no slot mode and $k$ pair modes occupied (their content $\Lambda^{k}\C^{3}$ and weight $-2k$ match, and irreducibles are determined by content and weight), so their parity is the total parity and this listing is the same listing as in (1).
\item (Consistency, and uniqueness given the content; under (S) for the doublets.) With the content of (1) and (2), all four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients} hold. Conversely, for the field content $Q = (2,3)$, $L = (2,1)$, $u^{c} = (1,\bar{3})$, $d^{c} = (1,\bar{3})$, $e^{c} = (1,1)$, all listed in one handedness, together with a fourth singlet of hypercharge zero or no fourth singlet, and $Y_{Q} = 1/6$ as the normalisation, the four conditions determine $Y_{L}$, $Y(e^{c})$ and $\{Y(u^{c}), Y(d^{c})\}$ uniquely, and the solution is the spectrum of (1) and (2). Both hypotheses are necessary: with a fourth singlet of unconstrained hypercharge the conditions admit a one-parameter family, and if the doublets were listed in the opposite handedness from the singlets the $[SU(3)]^{2}U(1)$ and cubic sums would be $-\tfrac23$ and $+\tfrac49$ rather than zero.
\end{enumerate}

## technical
With hypercharge $Y = q/6$, and Hypothesis (S) wherever a doublet at the level of one conformal spinor enters, chirality is the parity of the mode number. In the one-handed listing that keeps the quark doublet $(2,3)_{1/6}$ as a particle, the lepton doublet is the full conformal spinor with $Y_{L} = -\tfrac12$, and the $[SU(2)]^{2}U(1)$ anomaly coefficient $3Y_{Q} + Y_{L} = 3 \cdot \tfrac16 - \tfrac12 = 0$ confirms that orientation (the other would give $1$). Pair counting fixes $|Y_{L}/Y_{Q}| = 3$ and the parity fixes the sign.

Unconditionally, on the Fock space of a single conformal spinor, keeping the even grades and conjugating the odd ones gives the singlets $(1)_{0} \oplus (\bar{3})_{-2/3} \oplus (\bar{3})_{+1/3} \oplus (1)_{+1}$, that is $\nu^{c}$, $u^{c}$, $d^{c}$, $e^{c}$. With this content all four anomaly conditions hold; conversely, for this field content in one handedness, with $Y_{Q} = \tfrac16$ and a fourth singlet of hypercharge zero or absent, the conditions fix the other hypercharges uniquely. Both hypotheses are needed: a free fourth singlet admits the family $Y + t(B - L)$, and listing the doublets in the opposite handedness spoils two of the four sums.

## lay
Hypercharge is one of the charges that decide how particles feel the electroweak force. Here it is read off from how the symmetry acts on the composite's states, with the quark doublet carrying one sixth. Under a stated hypothesis about the state space, counting pairs and keeping track of handedness yields the lepton doublet and the four singlet particles with their observed hypercharges. The consistency conditions a quantum gauge theory must satisfy then hold, and given that particle content, all listed with one handedness, with the quark doublet's one sixth as the unit and a fourth singlet that is neutral or absent, they allow no other choice of charges.

## one-liner
Under Hypothesis (S) for the doublets, the composite's states carry the observed hypercharges of one generation, which satisfy all four anomaly conditions and are the unique solution for that content with $Y_{Q} = \tfrac16$.
