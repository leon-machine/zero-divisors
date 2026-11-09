---
id: synthesis.georgi-jarlskog-weight-free-on-the-stored-relations
kind: claim
version: 1
title: 'The 126 weight against the 10 is free on the stored relations'
status: proved
region: synthesis
subject: standard-model
tags: [flavour-and-mixing, seesaw-and-majorana, undetermined-input, spinor-modules]
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
  - synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square@2
  - synthesis.georgi-jarlskog-square-of-majorana-element@3
  - standard-model.majorana-element@7
  - standard-model.invariant-pairing-five-modes@5
  - families.doublet-direction-module-georgi-jarlskog-clebsch@6
  - standard-model.imported-clebsch-structure-seesaw@1
  - synthesis.majorana-scale-is-126-doublet-vev@3
  - synthesis.majorana-scale-free-on-pati-salam-route@5
  - standard-model.neutrino-dirac-matrix-charged-fermions@6
  - synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition@1
  - synthesis.residual-s2-fixes-120-family-form@1
  - standard-model.fits-record-level@6
  - standard-model.imported-spinor-bilinears@1
  - neutrino.breaking-relation@3
  - standard-model.space-symmetric-doublet-mass-forms-two@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_operator_functions_of_the_majorana_element_give_only_the_ten
- kind: check
  ref: check.py::check_weighting_of_the_pair_part_moves_the_lepton_quark_ratio
- kind: check
  ref: check.py::check_h_mu_fixes_every_stored_relation_and_moves_the_down_type_126
- kind: check
  ref: check.py::check_two_models_of_the_premises_differ_in_the_second_family_factor
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square
  - synthesis.majorana-scale-free-on-pati-salam-route
extraction:
  open_problem: op.pair-sector-current
  note: >-
    Attack item 3 of op.pair-sector-current: prove the 126 coefficient relative to the 10 independent of every
    stored relation. The premise set of the problem's eight entities at their pinned versions (their union of past
    cones) is (F1)-(F4), the slot-module premise, the indifference premise and imported Facts (Clebsch structure
    and seesaw, spinor bilinears, Pati-Salam branching, grade dictionary, anomaly coefficients, Fock
    representation, Cauchy decomposition, Chevalley and Witt, tractor and GTG imports); none names a coupling
    weight. The relations audited for invariance (not premises: no step assumes them) are on the Pati-Salam route: Premise (EW), the Majorana
    scale premise and its theorems, the neutrino Dirac mass matrix under (EW), Hypothesis (U) and its reading under
    (EW), the residual-S_2 and S_3 statements, the chain and v_R, and the neutrino-sector premises (H) and real
    breaking, which act on M_nu and M_R; (EW) and (U) are not in uses because no step assumes them and taking both would carry the stored contradicts link (entry reading). The stored Majorana scaling f -> lambda f, w -> w/lambda keeps w_d f
    fixed, so it does not free the 126 coefficient (the problem's text); h_mu moves w_d alone. Before the
    independence route a derivation was attempted (attack item 1): clause (i) shows that a coupling through
    operator functions of the Majorana element cannot give the down-type rung vector a Georgi-Jarlskog term, and the
    canonical pair weightings computed in the run (the u(3) Casimir of the pair modes gives x(10) + y(GJ) with
    (x, y) = (3, 3/2), (B - L)^2 gives (1/3, -2/3), P_4 gives (0, -3/32), the degree parts G_2k of T T^dag give
    multiples of the 10 or nothing) give every kind of ratio, none selected by a premise. The indifference premise
    is untouched by h_mu, a uniform scalar on family space that adds no partition, assignment or ordering (argued).
    Transport-absent: Clifford algebra on the module and linear algebra on family matrices; the series content is
    that T, the pairing, P_4 and the Clebsch structure are stored.
---

## formal
Work on the module $\Lambda^{\bullet}(W \oplus R_{2})$ with the Majorana element $T = v_{1}\cdots v_{5}$ (Proposition \claimref{standard-model.majorana-element}), mass forms $B(\psi, X\varphi)$ on the sixteen with the pairing of Lemma \claimref{standard-model.invariant-pairing-five-modes}, the rung vectors $w_{4}$ (down-type) and $v_{4}$ (up-type), the $10$ form of $w_{4}$ and the Georgi-Jarlskog form of $w_{4}(B - L)\chi$ (Proposition \claimref{families.doublet-direction-module-georgi-jarlskog-clebsch}), and the pair part $P_{4} = \tfrac{3}{32}(B - L)(-1)^{N_{P}}$ of $TT^{\dagger}$, a $(15,1,1)$ (Theorem \claimref{synthesis.georgi-jarlskog-is-rung-vector-times-pair-part-of-majorana-square}); and on the Pati-Salam route with the Clebsch structure of Fact \claimref{standard-model.imported-clebsch-structure-seesaw}, $M_{u} = \sum_{a}v_{u}^{a}Y_{a} + w_{u}f + c_{u}h$, $M_{\nu} = \sum_{a}v_{u}^{a}Y_{a} - 3w_{u}f + c_{\nu}h$, $M_{d} = \sum_{a}v_{d}^{a}Y_{a} + w_{d}f + c_{d}h$, $M_{e} = \sum_{a}v_{d}^{a}Y_{a} - 3w_{d}f + c_{e}h$, $M_{R} = v_{R}f$, $m_{\nu} = -M_{\nu}M_{R}^{-1}M_{\nu}^{\mathsf{T}}$.
\begin{enumerate}
\item[(i)] \emph{(Functions of the Majorana element.)} $T^{2} = (T^{\dagger})^{2} = 0$, $TT^{\dagger}T = T$ and $T^{\dagger}TT^{\dagger} = T^{\dagger}$, so $1, T, T^{\dagger}, TT^{\dagger}, T^{\dagger}T$ span the algebra generated by $T$ and $T^{\dagger}$. For every element $E$ of it the mass form of $w_{4}E$ is a multiple of the $10$ form (only $1$ contributes); for $v_{4}E$ the one further form, from $T^{\dagger}T$, has symmetric part half the $10$'s neutrino entry and no quark entry. So a coupling of the rung vector to operator functions of $T$ and $T^{\dagger}$ gives the down-type sector no Georgi-Jarlskog term: that term needs the $(15,1,1)$ projection of $TT^{\dagger}$, a linear map on its expansion in Majorana monomials, which the stored structure supplies and does not weight.
\item[(ii)] \emph{(The weight moves the ratio.)} For numbers $a, b$, $w_{4}(a + bP_{4})$ gives the symmetric form with quark entries $a - \tfrac{b}{32}$ and lepton entries $a + \tfrac{3b}{32}$ in units of the $10$'s, and no antisymmetric part, so the lepton-to-quark ratio is $(32a + 3b)/(32a - b)$ (that the symmetric doublet forms span the $10$ and $T_{\mathrm{GJ}}$ forms with $y_{e}/y_{d}$ free is Proposition \claimref{standard-model.space-symmetric-doublet-mass-forms-two}; what is added here is the weight of $P_{4}$ and the Clebsch identification): $1$ at $b = 0$, $-3$ at $a = 0$, $+3$ at $b/a = \tfrac{32}{3}$. With $(a, b) = (v_{d}Y_{kk}, -32w_{d}f_{kk})$ on a family $k$ these are the down-type and charged-lepton entries $v_{d}Y + w_{d}f$ and $v_{d}Y - 3w_{d}f$ of the Clebsch structure without a $120$: the module weight $b/a$ is the $126$ coefficient relative to the $10$, $w_{d}f$ against $v_{d}Y$.
\item[(iii)] \emph{(A symmetry of the stored relations.)} For real $\mu \neq 0$ let $h_{\mu}$ act on the Pati-Salam data by $w_{d} \mapsto \mu w_{d}$, all else fixed (composed, when the electroweak normalisation of the doublet vevs is imposed, with $(Y_{a}, v_{u}^{a}, v_{d}^{a}) \mapsto (Y_{a}/k, kv_{u}^{a}, kv_{d}^{a})$ on one $10$, which fixes every Dirac mass matrix). Then $M_{u}$, $M_{\nu}$, $M_{R}$ and $m_{\nu}$ are invariant; so are Premise (EW) (\claimref{standard-model.premise-ew-equal-weight}), $(M_{u})_{33} = m_{t} = 4w_{u}f_{33}$ with $(M_{\nu})_{33} = 0$ in its basis; the heavy-direction Majorana entry $(M_{R})_{33} = m_{t}v_{R}/(4w_{u})$ of Theorem \claimref{synthesis.majorana-scale-is-126-doublet-vev} and Premise \claimref{synthesis.majorana-scale-free-input}; without a $120$, $\hat{f} = \mathrm{Sym}(M_{d} - M_{e})/(M_{d} - M_{e})_{33} = f/f_{33}$ and $M_{\nu} = M_{u} - m_{t}\hat{f}$ (Proposition \claimref{standard-model.neutrino-dirac-matrix-charged-fermions}), hence Hypothesis (U) in both readings as Theorem \claimref{synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition}(i) states them, conditions on $\hat{f}$ with $m_{b}/m_{t}$ a given number; the chain and $v_{R}$; and the $S_{3}$- or $S_{2}$-invariance of every family matrix. The antisymmetric parts of the Dirac mass matrices are unchanged, and $\mathrm{Sym}(M_{d} - M_{e}) = 4\mu w_{d}f$. On the module $h_{\mu}$ is $b \mapsto \mu b$ in the down-type coupling of (ii).
\item[(iv)] \emph{(Models.)} Let $v_{u} = v_{d} = w_{u} = 1$, $f = \mathrm{diag}(\tfrac{1}{10}, 1, 1)$ and $Y = \mathrm{diag}(-\tfrac{1}{10}, -1, 3)$, so that $M_{u} = \mathrm{diag}(0, 0, 4)$, $M_{\nu} = \mathrm{diag}(-\tfrac25, -4, 0)$, (EW) holds exactly and $\sigma_{1}(M_{\nu}) = m_{t}$ (the top reading of (U)). Then $w_{d} = \tfrac13$ gives $(M_{e})_{22}/(M_{d})_{22} = 3$ and $w_{d} = \tfrac15$ gives $2$, with $M_{u}$, $M_{\nu}$, $M_{R}$ and $m_{\nu}$ equal; and $w_{d} = \tfrac15$ with $v_{d} = \tfrac{47}{45}$ gives $\tfrac{37}{19}$ with $\sigma_{1}(M_{d}) = (M_{d})_{33} = \tfrac{10}{3}$ equal to that of $w_{d} = \tfrac13$, $v_{d} = 1$, so the bottom reading of (U), read on the model's own $m_{b}$, fails in both ($\sigma_{1}(N) = 1$ against $m_{b}/m_{t} = \tfrac56$) and does not separate them. The diagonal model satisfies every postulate of the cone and of the relations audited: (EW), (U) in its eigenvalue (top) reading, Premise (H) ($m_{\nu}$ has the eigenvalue $0$), Premise (M) ($v_{R} = 1000$ against doublet vevs of $1$), the real-breaking assumption (all data real), the face identification and the indifference premise, which speak of no coupling weight; so a model of all of them with $w_{d}f \neq 0$ exists, as the invariance under $h_{\mu}$ requires. With an $S_{3}$-invariant Majorana matrix, $f = (\alpha\Pi + M_{3}\J/3)/v_{R}$, $\mathrm{Sym}(M_{d} - M_{e}) = 4\mu w_{d}f$ stays $S_{3}$-invariant and its light-plane value $4\mu w_{d}\alpha/v_{R}$ (Theorem \claimref{synthesis.residual-s2-fixes-120-family-form}(iii)) moves with $\mu$.
\end{enumerate}
Premise (EW) and Hypothesis (U) are not premises of this result: no step assumes them; they are relations the models are shown to satisfy, which is what an independence proof needs. (U) is satisfied in its eigenvalue (top) reading, in which Theorem \claimref{synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition} shows it consistent with (EW); the store's contradicts link between (U) and (EW) concerns the entry reading $(M_{\nu})_{33} = m_{t}$, and taking both as premises would carry it.
So no stored relation fixes the $126$ coefficient relative to the $10$ in the down-type sector, on the Majorana route (the weight $b/a$) or on the Pati-Salam route ($w_{d}f$ against $v_{d}Y$): the relations determine it only through the down-quark and charged-lepton matrices, $\mathrm{Sym}(M_{d} - M_{e}) = 4w_{d}f$, so the second family's factor $3$ is an input taken from the record, and with it $m_{b}/m_{\tau}$ at $M_{I}$. Premise (EW) fixes a $126$-to-$10$ ratio only in the up sector along the heavy direction, $v_{u}Y_{33} = 3w_{u}f_{33}$ in its basis.

## technical
The open number of the problem, the weight of the $(15,1,1)$ part of the Majorana square against the rung vector's $10$ term, is shown to be unconstrained by every relation the store holds. First, a coupling through functions of the Majorana element itself cannot produce it: $T$ and $T^{\dagger}$ generate a five-dimensional algebra, and the down-type rung vector times any element of it gives a multiple of the $10$ form, so the Georgi-Jarlskog form appears only after projecting the square on a Pati-Salam component. Second, the weight $b/a$ of that projection sets the lepton-to-quark ratio of the down-type form as $(32a + 3b)/(32a - b)$, and on each family it is exactly the Clebsch structure's $w_{d}f$ against $v_{d}Y$.

Third, scaling the $126$'s down-type doublet admixture $w_{d}$ alone leaves the up and neutrino Dirac mass matrices, the Majorana matrix, the light neutrino matrix, Premise (EW), the Majorana scale premise, the neutrino Dirac mass matrix under (EW) and with it Hypothesis (U) in its eigenvalue readings (with $m_{b}/m_{t}$ given; models satisfy the top reading), the chain and the family symmetries unchanged, and multiplies the symmetric part of $M_{d} - M_{e}$ by the same factor. The stored Majorana scaling moves $w_{u}$ and $w_{d}$ together against $f$ and so fixes $w_{d}f$; this one moves $w_{d}$ alone. Exact models with the same up, neutrino and Majorana sectors have second-family factors $3$, $2$ and $\tfrac{37}{19}$, the last at the same bottom mass. So the factor $3$ is not derived: it is read from the measured masses. The check verifies all four clauses exactly, on the $32$-dimensional module and on two family-matrix models (one diagonal, one with off-diagonal entries and a $120$) for four values of $\mu$.

## lay
In the version of the theory where quarks and leptons are unified, the mass of the strange quark and of the muon come from two kinds of Higgs field: one gives them equal masses, the other gives the muon three times the strange quark's mass, which is what the measurements suggest at very high energies. How much of each kind enters is a number. This result shows that nothing the theory has stored fixes that number. A coupling built from the theory's heavy-neutrino element alone gives only the equal-mass kind. Changing the weight of the second kind, through one unmeasured Higgs mixing, leaves every stored relation true, including the assumptions about the heavy neutrino and the top quark. Only the masses of the down-type quarks and the charged leptons change. So the factor three is taken from the data, not predicted.

## one-liner
Operator functions of the Majorana element give the down-type rung vector only the $10$; the $(15,1,1)$ weight $b/a$ sets $m_{\mu}/m_{s}$ as $(32a + 3b)/(32a - b)$ and is $w_{d}f$ against $v_{d}Y$; $w_{d} \mapsto \mu w_{d}$ fixes every stored relation ((EW), the Majorana scale, (U) in its eigenvalue reading, the chain) and moves $\mathrm{Sym}(M_{d} - M_{e})$ by $\mu$, so the second family's factor $3$ is an input.
