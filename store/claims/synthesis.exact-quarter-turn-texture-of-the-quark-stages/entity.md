---
id: synthesis.exact-quarter-turn-texture-of-the-quark-stages
kind: claim
version: 1
title: 'Conjecture: the exact quarter-turn texture of the quark stages'
status: conjectured
region: synthesis
subject: generations
tags: [flavour-and-mixing, mass-generation, undetermined-input, open-problem]
proposed_by:
  kind: ai
  session: maintainer-2026-11-16
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction and decision
- name: Claude Fable 5.2
  role: drafting
  source: maintainer pass 2026-11-16 (anomaly)
review: draft
derivations:
- name: main
  note: 'no proof: the texture is conjectured; the consequences listed in the statement are clauses of the two results named here, at their stored versions'
  uses:
  - synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion@1
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase@4
lineage:
  motivated_by:
  - synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion
  - synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase
  - synthesis.colour-angle-registered-free-input
extraction:
  open_problem: op.second-order-breaking
  maintainer_pass_2026_11_16:
    by: maintainer-2026-11-16
    date: '2026-11-16'
    note: >-
      New conjecture, stored by Leon's decision D1 of 16 November 2026 beside the registration of the
      physical colour angle: the exact quarter-turn texture is recorded as a conjecture and is not adopted
      as a premise. It is the one reading of clause (iv) of the determinant-phase result on which the quark
      mass determinant is real with a nonzero commutator invariant, and on it the stored Cabibbo relation
      has no free phase. The statement carries its hypotheses, says that no symmetry protects it and that
      its sign is not fixed, and names its two refutation conditions. The one-loop mass phase on the
      texture is not computed; it is recorded as an attack item of op.second-order-breaking. Literature,
      cited from memory and not imported: Hermitian quark mass matrices from a generalised parity in
      left-right models (Mohapatra and Senjanovic 1978; Beg and Tsao 1978), of which the up matrix here is
      the twin under the exchange of the first two families.
---

## formal
\emph{Setting.} Scalars of family matrices are read in $\mathrm{span}\{1, I_{4}\}$ and $^{*}$ is $I_{4} \mapsto -I_{4}$ on entries. The quark Dirac mass matrices have the stage form of clause (iv) of Theorem \claimref{synthesis.phase-of-the-quark-mass-determinant-on-the-covariant-completion}, which is that of Proposition \claimref{synthesis.cabibbo-from-one-type-quark-stages-selects-near-quarter-turn-phase}: $M_{q} = c_{q}\bigl(\J + \delta_{q}(E + X_{q})\bigr)$, $q = u, d$, with $\J$ the matrix of ones, $E = e_{3}e_{3}^{\mathsf{T}}$ and $X_{q}$ odd under the exchange $P_{12}$ of the first two families.

\emph{Conjecture (the exact quarter-turn texture).} At tree level the quark stages satisfy:
\begin{enumerate}
\item[(T1)] \emph{(one-type symmetric second stages)} $X_{q} = t_{q}S_{q}$ with $S_{q}$ real, symmetric and $P_{12}$-odd, with entries $p_{q}$, $r_{q}$;
\item[(T2)] \emph{(real first stages)} $c_{q}$ real and nonzero, and $\delta_{q}$ real and nonzero, of either sign, with $R_{q} = (p_{q} - 2r_{q})^{2} + \delta_{q}p_{q}^{2} \neq 0$ (no massless quark);
\item[(T3)] \emph{(an exact quarter turn between the sectors)} one sector's second-stage coefficient is real and the other's is a real multiple of $I_{4}$: $t_{d}$ real and nonzero and $t_{u} = I_{4}\tau$ with $\tau$ real and nonzero, or the same with the two sectors exchanged.
\end{enumerate}
None of (T1) to (T3) is a stored statement: the stored quark-stage result allows any complex coefficient and says nothing on $c_{q}$, a unit factor on $c_{u}$ is exactly the freedom of the covariant completion, and the breaking lemma has $\delta$ real and no more (clause (iv) of the Theorem). On the covariant completion the texture is realised, off the balanced frame, by exactly one pair of symmetric family matrices $(Y, \tilde{Y})$ (clause (i) there).

\emph{What follows from it, by clauses of the two results it rests on (proved there, at tree level and at the order of the breaking lemma; nothing is proved here).} (a) $\Theta = \det M_{u}\det M_{d} = (c_{u}c_{d})^{3}(\delta_{u}\delta_{d})^{2}(t_{u}t_{d})^{2}R_{u}R_{d}$ is real and nonzero, of sign $-\sigma$ with $\sigma = \operatorname{sgn}(c_{u}c_{d}R_{u}R_{d})$: the mass phase $\theta_{M}$ is $0$ for $\sigma < 0$ and a half turn for $\sigma > 0$ (clause (iv) of the Theorem). (b) The up-down phase $\phi$ of the stored quark-stage result is an exact quarter turn, $\cos\phi = 0$; written for $t_{d}$ real, $M_{d}^{*} = M_{d}$ and $P_{12}M_{u}^{*}P_{12} = M_{u}$, the up matrix being the twin of a Hermitian matrix; the commutator invariant $D = \det[H_{u}, H_{d}]$ is nonzero generically, so that the Jarlskog invariant is then nonzero, and the up and down spectra are unequal (ibid.). (c) With $\cos\phi = 0$ the Cabibbo element has no free phase:
\[
|V_{us}|^{2} = \frac{x + y}{(1 + x)(1 + y)}, \qquad x = \frac{m_{d}}{m_{s}}, \quad y = \frac{m_{u}}{m_{c}},
\]
so $|V_{us}|$ follows from two mass ratios (clause (i) of the Proposition). At the central ratios of the $N_{f} = 2{+}1{+}1$ lattice averages it gives $|V_{us}| \in (0.22256, 0.22257)$, inside the stored window $W = (0.22176, 0.22705)$, and at those of the $N_{f} = 2{+}1$ averages $(0.22054, 0.22055)$, just below $W$ (clause (iii) there).

\emph{What it is not, and does not claim.} It is a texture at tree level, not the consequence of a symmetry of the coupled theory: the two sectors are fixed by two different conjugations, plain conjugation for one and conjugation composed with $P_{12}$ for the other, and a conjugation common to both gives $D = 0$; so nothing stored protects it against corrections. The sign $\sigma$ is not fixed by anything stored, so the conjecture gives a mass phase of zero or of a half turn and does not say which; only the first is a small angle, and a half turn, which also conserves CP, is not excluded by the imported neutron bound (Fact \claimref{synthesis.imported-physical-colour-angle-and-its-shift-under-quark-rephasing}(iv)). The mass phase at one loop is not computed: in the covariant coupling the second doublet couples with the two family matrices exchanged, so a correction below the neutron bound is not to be presumed (argued, not computed). The conjecture says nothing about the coefficient of the colour four-form, to which the mass phase is only added, so it does not fix the physical colour angle, which stays the registered free input of Premise \claimref{synthesis.colour-angle-registered-free-input}. It is not selected by a stored structure: the store selects $|\cos\phi| < \tfrac12$ from the data and nothing more, and the quarter turn is one of five candidate phases with rational cosine of which the data allow only this one, and that only within the spread of the lattice averages.

\emph{Refutation conditions.} (R1) \emph{The parameter-free Cabibbo relation.} The conjecture is refuted, at the order of the breaking lemma, if $|V_{us}|$ computed from the measured ratios $m_{d}/m_{s}$ and $m_{u}/m_{c}$ by the formula of (c) lies outside the measured window of $|V_{us}|$; at present the two sets of lattice averages put it inside and just below $W$, so the relation is allowed and not yet tested. (R2) \emph{The mass phase at one loop.} It is refuted, as a texture that keeps the determinant real to the accuracy the record requires, if the one-loop mass phase on the texture is computed and exceeds the neutron bound of Fact \claimref{synthesis.imported-neutron-dipole-bound-and-its-conversion-to-the-colour-angle}, about $2 \times 10^{-10}$; the physical angle could then be small only by a cancellation against the coefficient of the four-form, which the registered premise allows and does not explain.

## technical
The store's quark-stage result fits the Cabibbo angle with one free number, a relative phase between the up and down second stages, and the data put it within $30^{\circ}$ of a quarter turn. The determinant-phase result shows that on one-type symmetric stages with real first stages and one sector's second stage real, the determinant of the quark mass matrices is real exactly when that phase is an exact quarter turn. This entry records the corresponding texture as a conjecture: real first stages, symmetric one-type second stages, one sector's second stage real and the other's a real multiple of $I_{4}$. On it the mass phase is zero or a half turn at tree level, the commutator invariant is generically nonzero, so CP violation in the mixing survives, and the Cabibbo element is given by the two light mass ratios with no free phase, a relation that the present lattice ratios allow and do not yet test. The conjecture carries its hypotheses and is weaker than it may look: the pattern is not enforced by a symmetry, the sign that decides between zero and a half turn is free, the one-loop mass phase is not computed, and the coefficient of the colour four-form is untouched, so the physical colour angle remains a registered free input. It is refuted by the parameter-free Cabibbo relation failing against sharper mass ratios, or by a computed one-loop mass phase above the neutron bound.

## lay
The measured mixing between the first two families of quarks asks for a phase close to a quarter turn between the up-type and the down-type quarks. This entry records a guess: that the phase is exactly a quarter turn and that everything else in the simplest part of the quark mass pattern is real. If so, two things follow. The part of the strong CP angle that comes from the quark masses would be either zero or exactly a half turn, with nothing yet saying which. And the mixing between the first two families would be fixed by quark mass ratios alone, which can be tested as those ratios are measured better. The guess is not backed by any symmetry of the framework, and effects beyond the simplest approximation, which have not been calculated, could spoil it.

## one-liner
Conjecture: one-type symmetric quark stages with real $c_{q}$, real nonzero $\delta_{q}$, one sector's second stage real and the other's a real multiple of $I_{4}$ (an exact quarter turn); then, by the stored results, $\det M_{u}\det M_{d}$ is real (mass phase $0$ or a half turn according to $-\operatorname{sgn}(c_{u}c_{d}R_{u}R_{d})$, not fixed) with $D \neq 0$ generically, and $|V_{us}|^{2} = (x + y)/((1 + x)(1 + y))$ with no free phase; a tree-level texture protected by no symmetry, silent on the coefficient of the four-form; refuted by the parameter-free Cabibbo relation or by a computed one-loop mass phase above the neutron bound.
