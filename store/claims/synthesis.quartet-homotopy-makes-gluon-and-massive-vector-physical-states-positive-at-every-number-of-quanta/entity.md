---
id: synthesis.quartet-homotopy-makes-gluon-and-massive-vector-physical-states-positive-at-every-number-of-quanta
kind: claim
version: 2
title: 'Under clauses (K1) and (K2) of the Krein-form premise (the polarisation states carry the Gupta-Bleuler form $-u\cdot w$, the ghost pair the pairing $\langle c, \bar c\rangle_K = 1$), the free BRST charge of the gluons (at null momenta) and of the massive W and Z in the Feynman-''t Hooft gauge (with their Goldstone modes) has a one-particle contracting homotopy whose second quantisation counts the unphysical quanta, so at every number of quanta its cohomology is the Fock space of the transverse polarisations, two per gluon and three per massive vector, and the Krein form is positive on it with radical the image of the charge'
status: proved
region: synthesis
subject: quantum-fields
tags: [gauge-fields, car-algebra, representation-theory, recovers-known-physics]
proposed_by:
  kind: ai
  session: 2026-11-02-qft-full
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.field-theory.single-algebra-field
derivations:
- name: main
  uses:
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts@2
  - field-theory.imported-statistics-no-go-palatial-algebra@2
  - field-theory.imported-tower-limit@3
  - standard-model.gauge-algebra-minimal-massive-composite@4
  - synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum@3
  - synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1
  assumes:
  - synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_one_particle_quartets_and_homotopies
- kind: check
  ref: check.py::check_second_quantised_homotopy_counts_quartet_quanta
- kind: check
  ref: check.py::check_cohomology_is_the_positive_physical_fock_space
- kind: check
  ref: check.py::check_broken_gauge_algebra_one_particle_count
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts
extraction:
  maintainer_pass:
    by: maintainer-2026-11-02
    date: '2026-11-02'
    note: 'Version 1 -> 2, by Leon''s decisions of 2026-11-02: an assumes edge to the Krein-form premise synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields@2 (its clauses (K1), (K2) are hypotheses of the result), cited by claimref in the formal Reading and the proof; the one-particle form of (K1) is noted as restated (not derived) by the Clifford-conjugation result; the Gribov result accepted with it is cited by claimref at the formal level and in the proof and by id in this note (no uses edge: a statement of scope). Statement and check unchanged.'
  open_problem: op.qft-non-abelian-gauge-fields
  note: >-
    Answers the problem's first attack line on positivity beyond three quanta, at the free (asymptotic) level and
    under the Krein-form premise. The stored result computed the ghost-number-zero cohomology of the free charge at
    one null momentum up to three quanta and left every number of quanta to the imported quartet mechanism. Here a
    one-particle odd operator R1 with Q1 R1 + R1 Q1 = P (the projection onto the quartet span along the physical
    span) is exhibited; second quantisation is a homomorphism of Lie superalgebras, so the second-quantised R
    satisfies Q R + R Q = N_q, the number of quartet quanta, and the cohomology at every number of quanta is the
    Fock space of the physical span, positive because that span is Krein-positive and Krein-orthogonal to the
    quartets. This covers every colour and every finite set of momenta (direct sums), and the massive vectors of the
    broken weak factor with one Goldstone mode each, where nilpotency forces the Goldstone coefficient
    beta^2 = Q(p) (the Feynman-'t Hooft shell). The quartet mechanism is standard (Kugo and Ojima; the frame imported
    in synthesis.imported-brst-kugo-ojima-strocchi-and-gribov); the homotopy argument is the standard proof, written
    out and checked exactly on the store's representations (palatial polynomials for the bosons, tower floors for
    the ghosts). Not proved: the interacting statement, which needs Kugo and Ojima's hypotheses on the asymptotic
    fields (asymptotic completeness, the asymptotic charge being the linear one; for unbroken colour their criterion
    for the absence of massless coloured asymptotic states); the derivation of the Krein form (clauses K1 and K2 are
    conditions of the result, stated in words); the field-level Goldstone terms of the differential; the breaking
    pattern itself (the neutral aligned vacuum of the two doublets is input; the rank of the Goldstone map is then
    computed). The construction is perturbative: beyond perturbation theory gauge fixing has Gribov copies (the
    lattice result
    synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law).
    All operators here are real, so they commute with i = I4. Transport-absent.
---

## formal
Units and signature of the store. A one-particle space is a real space $V$ with a $\mathbb{Z}_2$ grading (bosonic polarisation and Goldstone modes even, ghosts odd), an orthonormal basis for a positive form and a fundamental symmetry $J$ (a signed permutation of that basis), with Krein form $\langle x, y\rangle_K = \langle x, Jy\rangle$. Its Fock space $S(V)$ is the graded-symmetric algebra (bosons: the palatial polynomials of Fact \claimref{field-theory.imported-statistics-no-go-palatial-algebra}, with the positive form $\langle z^n, z^m\rangle = n!\,\delta_{nm}$ of the setting of \claimref{synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts}; ghosts: the tower floors of Fact \claimref{field-theory.imported-tower-limit}), with Krein form $\langle x, \Gamma(J)y\rangle$; $d\Gamma(X)$ is the graded derivation extending a one-particle operator $X$.
\begin{enumerate}
\item[(i)] \emph{(The homotopy lemma; proved.)} Let $Q_1$ be odd with $Q_1^2 = 0$ and Krein-self-adjoint, $V = V_{\mathrm{ph}} \oplus V_{q}$ a Krein-orthogonal sum with $Q_1V_{\mathrm{ph}} = 0$, and $R_1$ odd with $Q_1R_1 + R_1Q_1 = P_{q}$, the projection onto $V_{q}$ along $V_{\mathrm{ph}}$. Then $Q_{B} = d\Gamma(Q_1)$ is nilpotent and Krein-self-adjoint, $Q_{B}R + RQ_{B} = N_{q}$ for $R = d\Gamma(R_1)$ and $N_{q} = d\Gamma(P_{q})$ the number of quanta in $V_{q}$, $\ker Q_{B} = S(V_{\mathrm{ph}}) \oplus \operatorname{im}Q_{B}$, and the cohomology of $Q_{B}$ is $S(V_{\mathrm{ph}})$, in every number of quanta and at ghost number zero only. If $V_{\mathrm{ph}}$ is Krein-positive, the Krein form on $\ker Q_{B}$ is positive semi-definite with radical $\operatorname{im}Q_{B}$, and positive definite on the cohomology.
\item[(ii)] \emph{(Gluons; proved.)} For each colour and each null momentum $k$, with polarisation modes carrying the Gupta-Bleuler form $-u\cdot w$ and a ghost pair with $\langle c, \bar c\rangle_K = 1$, the free charge of \claimref{synthesis.self-adjoint-brst-charge-needs-a-krein-form-and-the-tower-supplies-the-ghosts}, $Q_1u = -(k\cdot u)c$, $Q_1\bar c = k$, has the homotopy $R_1k = \bar c$, $R_1c = -\bar k$, zero on $\bar k$ and on the transverse plane, where $\bar k$ is null with $k\cdot\bar k = 1$; $V_{q} = \mathrm{span}\{k, \bar k, c, \bar c\}$ and $V_{\mathrm{ph}} = \{k, \bar k\}^{\perp}$, which is Krein-positive. So by (i) the physical space at every number of quanta, for any number of colours and any finite set of null momenta, is the Fock space of the transverse polarisations, positive.
\item[(iii)] \emph{(Massive vectors in the Feynman-'t Hooft gauge; proved.)} For a vector of momentum $p$, with the Goldstone and ghost modes at the same momentum (the Feynman-'t Hooft gauge), with $Q(p) > 0$ and a Goldstone mode $\phi$ of Krein norm $1$, Krein self-adjointness fixes $Q_1u = -(p\cdot u)c$, $Q_1\phi = \beta c$, $Q_1\bar c = p + \beta\phi$, and $Q_1^2 = 0$ exactly when $\beta^2 = Q(p)$. Then $V_{q} = \mathrm{span}\{p, \phi, c, \bar c\}$ has a homotopy, and $V_{\mathrm{ph}} = p^{\perp}$, three-dimensional and Krein-positive: the physical space is the Fock space of three polarisations.
\item[(iv)] \emph{(Exact checks; computed.)} For $k = 5\gamma_0 + 3\gamma_1 + 4\gamma_2$, $\bar k = \tfrac{1}{50}(5\gamma_0 - 3\gamma_1 - 4\gamma_2)$, and $p = 5\gamma_0 + 4\gamma_1$, $\beta = 3$: the one-particle statements (with $\beta = 2$ not nilpotent; physical Krein Gram $25, 1$ and $9, 1, 1$); $Q_{B}^2 = 0$, Krein self-adjointness and $Q_{B}R + RQ_{B} = N_{q}$ on every sector with at most four quanta (gluon) and three quanta (massive); ghost-number-zero cohomology of dimensions $1, 2, 3, 4, 5$ (gluon), $1, 3, 6, 10$ (massive) and $1, 4, 10, 20$ (two colours), with Krein signature $(\dim H, 0, \operatorname{rank})$ on $\ker Q_{B}$.
\item[(v)] \emph{(The gauge algebra broken by two doublets; computed, given the vacuum as input.)} Take the twelve generators of Theorem \claimref{standard-model.gauge-algebra-minimal-massive-composite} acting on the two hypercharge-$\tfrac12$ doublets of \claimref{synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum} (eight real scalars), with a neutral aligned vacuum $(0, v_1)$, $(0, v_2)$ as input (the breaking pattern is not derived here). The Goldstone map $T_a \mapsto (T_a\phi_1, T_a\phi_2)$ has rank $3$, so nine vectors stay massless (its kernel: colour and one $\mathfrak{u}(1)$ mixing $T_3$ and hypercharge) and three are massive. The one-particle direct sum of the corresponding spaces of (ii) and (iii) is Krein-self-adjoint with a homotopy, has $27$ physical polarisations per momentum with Krein signature $(27, 0, 0)$, and $8 - 3 = 5$ scalars remain physical.
\end{enumerate}
\emph{Reading.} Under clauses (K1) and (K2) of the Krein-form premise (KF, \claimref{synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields}; the one-particle form of (K1) is restated in the store as the trace form of Clifford conjugation, \claimref{synthesis.clifford-conjugation-is-the-twistor-adjoint-and-its-trace-form-is-the-one-particle-gupta-bleuler-form}, which does not derive the premise), that the polarisation states carry the Gupta-Bleuler form $-u\cdot w$ and the ghost pair the pairing $\langle c, \bar c\rangle_K = 1$, the free (asymptotic) gluons and the massive vectors (Feynman-'t Hooft gauge) have a positive physical space at every number of quanta, which the stored result had only up to three quanta; this is the quartet mechanism of Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(ii), proved here in its free form by an explicit homotopy. The interacting statement is not proved: it needs Kugo and Ojima's hypotheses on the asymptotic fields, and the whole construction is perturbative, since beyond perturbation theory the covariant gauge condition has Gribov copies (Fact \claimref{synthesis.imported-brst-kugo-ojima-strocchi-and-gribov}(iv); computed copies on the weak rotor lattice in \claimref{synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law}). The polarisation form used is the momentum-independent Gupta-Bleuler form $-u\cdot w$ (Feynman gauge); forms with a part along $k$ are not treated. All operators are real, so the unit $i = I_4$ commutes with them. Transport-absent.

## technical
The stored covariant gauge fixing of the series' gauge fields showed, under the Krein-form premise, that the free BRST charge at one null momentum has a positive physical space, computed exactly up to three quanta. Positivity at every number of quanta is the content of the Kugo-Ojima quartet mechanism, and its free form has a short proof that the computation can follow exactly. On the one-particle space the unphysical modes (the polarisation along $k$, its partner $\bar k$, the ghost and the antighost) form a quartet, and there is an odd operator $R_1$ with $Q_1R_1 + R_1Q_1$ equal to the projection onto the quartet. Second quantisation turns graded commutators of one-particle operators into graded commutators of their Fock-space lifts, so the lifted $R$ satisfies $Q_{B}R + RQ_{B} = N_{q}$, the number of quartet quanta. Every closed state with at least one quartet quantum is then exact, $x = Q_{B}(Rx)/n$, so the cohomology is the Fock space of the transverse polarisations, in every number of quanta. The Krein form is positive there because the transverse polarisations have positive Gupta-Bleuler norm and are Krein-orthogonal to the quartet.

The same structure covers the massive vectors of the broken weak factor in the Feynman-'t Hooft gauge, where the Goldstone and ghost modes share the vector's momentum: with a Goldstone mode of positive norm, self-adjointness fixes the charge and nilpotency forces the Goldstone coefficient to satisfy $\beta^2 = Q(p)$, the Feynman-'t Hooft shell; the quartet is the polarisation along $p$, the Goldstone mode and the ghost pair, and the physical modes are the three polarisations orthogonal to $p$. For the gauge algebra broken by the stored two doublets, with a neutral aligned vacuum taken as input, the rank of the Goldstone map is computed to be three: nine massless vectors with two polarisations and three massive ones with three, $27$ in all and all Krein-positive, and five physical scalars. The checks confirm each step exactly for rational momenta, including the Fock-space identity $Q_{B}R + RQ_{B} = N_{q}$ sector by sector and the cohomology dimensions, and that the computation reproduces the stored dimensions $1, 2, 3, 4$ and continues them.

What is not proved is the interacting statement. Kugo and Ojima derive it from hypotheses on the asymptotic fields: asymptotic completeness, the asymptotic charge being the linear one, and, for unbroken colour, a condition excluding massless coloured asymptotic states. None of these follows from the series' structures, and the Krein form itself remains a premise.

## lay
In the standard quantum theory of the strong and weak forces, the force fields carry unphysical parts, which come with negative probabilities, and ghost particles that cancel them. The cancellation works because the unphysical modes come in groups of four whose contributions vanish. Earlier work on the series checked this for states with up to three particles. This result proves it for any number of particles, for the gluons of the strong force and for the heavy W and Z of the weak force in one standard choice of gauge, by an explicit operator that counts the unphysical particles: any allowed state containing them is equivalent to zero, so the surviving states are made only of the physical polarisations, and they have positive probabilities. It holds for free particles and assumes two parts of the negative-norm bookkeeping the series has adopted as a premise; it is a statement of perturbation theory; the fully interacting case still rests on the standard assumptions of the literature.

## one-liner
Under clauses (K1) (Gupta-Bleuler form $-u\cdot w$) and (K2) (ghost pairing $\langle c, \bar c\rangle_K = 1$) of the Krein-form premise, the free BRST charge of the gluons (null $k$) and of the massive W and Z in the Feynman-'t Hooft gauge (Goldstone coefficient $\beta^2 = Q(p)$ forced) has a one-particle homotopy $Q_1R_1 + R_1Q_1 = P_q$ whose second quantisation gives $Q_BR + RQ_B = N_q$, so at every number of quanta the cohomology is the positive Fock space of the transverse polarisations (two per gluon, three per massive vector; 27 per momentum for the gauge algebra broken by the two doublets, vacuum taken as input); perturbative; the interacting case needs Kugo and Ojima's asymptotic hypotheses; transport-absent.
