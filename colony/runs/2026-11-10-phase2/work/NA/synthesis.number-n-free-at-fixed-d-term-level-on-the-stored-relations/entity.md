---
id: synthesis.number-n-free-at-fixed-d-term-level-on-the-stored-relations
kind: claim
version: 1
title: 'N is free at fixed D-term level on the stored relations'
status: proved
region: synthesis
subject: dark-energy
tags: [the-number-n, undetermined-input, cosmological-constant, finite-models]
proposed_by:
  kind: ai
  session: 2026-11-10-phase2
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-10-phase2
review: draft
derivations:
- name: main
  uses:
  - synthesis.d-term-level-free-at-fixed-n@1
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion@3
  - synthesis.smallness-monomials-exact-hierarchy-casimir@3
  - synthesis.de-sitter-entropy-pi-n-squared@6
  - synthesis.de-sitter-mode-count@3
  - standard-model.trichotomy-what-kind-number@11
  - standard-model.imported-frozen-point-dictionary@9
  - synthesis.promoted-norm-one-global-pair@5
  - synthesis.einstein-route-makes-n-initial-data@4
  - dark-energy.under-action-written-norm-parameter-laws@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_vacua_at_one_level_and_two_values_of_n
- kind: check
  ref: check.py::check_dimensionless_spectrum_equal_and_weak_scale_moves_only_through_h4
- kind: check
  ref: check.py::check_stored_relations_with_n_hold_in_both_models
- kind: check
  ref: check.py::check_isometry_and_rescaling_join_the_two_frozen_points
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.number-n-registered-free-input
  - synthesis.d-term-level-free-at-fixed-n
  - standard-model.trichotomy-what-kind-number
extraction:
  open_problem: op.rung-unit
  note: >-
    The mirror of synthesis.d-term-level-free-at-fixed-n (the level free at fixed N): here N is moved at fixed
    level. It does not re-register N, which Premise synthesis.number-n-registered-free-input (version 1) holds as
    an input; it shows that the premise's refutation condition is not met by anything stored. No open problem of
    the store is attached to N itself (op.t12-n-after-the-count is settled); the field names op.rung-unit, whose
    independence item this completes from the other side. What "the stored relations" covers, so that the label is
    exact: (a) a pattern search of the formal level of all 1371 claims for N, M_P/H, G Lambda, pi N^2, N^-2, v/H,
    the values 10^60, 10^61, 10^120, 10^122 and the tag the-number-n (45 entities, each read at one-liner level
    and the proved ones with a formula at formal level); (b) a second search for a cosmological symbol (Lambda,
    H^2, Q(I), Hubble) together with a gravitational one (M_P, G, Planck) outside (a) (77 entities, titles read,
    twelve read at one-liner level); (c) the union of the past cones of the 45 entities of (a): 519 entities, of
    which 40 are postulates, each postulate's formal text searched for the same symbols (hits: the rung-unit
    premise, (C1), (C2), the local-horizon premise, the cosmological-horizon regularity premise, the intrinsic
    clock; each either contains no Lambda or contains it only in a definition that the rescaling carries along).
    The search is by pattern and reading, not a formal audit of every derivation: the clause "no other stored
    relation contains N" is argued on that basis; the relations listed in (iii) are proved to hold in the models.
    Readings at conjectured status are not relations of the premise set: the exponential reading of the tower
    (standard-model.why-large) assigns no value to N by its own text; the dating observation and the Dirac
    coincidence concern the record. Stored and excluded: a Majorana scale tied to v/H by the frame boost
    (synthesis.majorana-scale-not-carried-by-rung-frame-boost), a pion-scale N^(2/3) (a failed route of
    families.absolute-scale-clean-negative-result). Not treated: whether the horizon mode count must be an integer
    (no stored statement says so; if imposed it would restrict N^2 to a discrete set and leave it unfixed).
    Transport-absent: the statement is about gravity's two constants and the rung field's action; the frozen
    point enters only through its norm. The transitivity argument of (iv) is elementary (two reflections) and
    classical.
---

## formal
Take the setting of Theorem \claimref{synthesis.d-term-level-free-at-fixed-n}: the D-term action of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus} on the null-lift locus $L_{H} = \{Q(c) = -H^{2}\}$, $H^{2} = \Lambda/3 = Q(I_{\Lambda})$ for the frozen point $I_{\Lambda}$, with the added invariant $\kappa\mathsf{N}^{2}$, $\kappa \ge 0$; the lift family $c_{\lambda}$ with $\mathsf{N}(\lambda) = \tfrac12(H^{4}/\lambda^{2} + \lambda^{2})$ and $m(\lambda) = \tfrac12(H^{4}/\lambda^{2} - \lambda^{2})$; the level $\xi$; Newton's constant $G = M_{P}^{-2}$ and $N = M_{P}/H$. Fix $G$, the couplings $g$, $g'$, $\kappa$ and a level $\xi > 0$, and put $m^{*} = g'^{2}\xi/(g^{2} + g'^{2} + 8\kappa)$.
\begin{enumerate}
\item[(i)] \emph{(A vacuum at the same level for every $N$.)} For every $H > 0$ the frame $\lambda_{H}$ with $\lambda_{H}^{2} = \sqrt{m^{*2} + H^{4}} - m^{*}$ satisfies $0 < \lambda_{H} < H$, $m(\lambda_{H}) = m^{*}$ and $\mathsf{N}(\lambda_{H}) = \sqrt{m^{*2} + H^{4}}$, and by part (i) of that theorem $c_{\lambda_{H}}$ is a charge-preserving critical point of the potential on $L_{H}$ at the level $\xi$, with every tree mass squared a positive multiple of $\mathsf{N}$ that depends on $g$, $g'$, $\kappa$ only. So every pair $(N, \xi G)$ of positive numbers is realised by a model with the given couplings, and the ratios of tree masses are the same in all of them.
\item[(ii)] \emph{(Two exact models.)} With $G = 1008^{-2}$, $g = \tfrac23$, $g' = \tfrac12$, $\kappa = \tfrac15$ and $\xi = \tfrac{171808}{9}$, so $m^{*} = 2080$: the model $A$ with $H = 48$, $\lambda = 32$ and the model $B$ with $H = 63$, $\lambda = 49$ have $N = 21$ and $N = 16$, $\mathsf{N} = 3104$ and $4481$, the same ratios $M_{W}^{2}/M_{Z}^{2} = \tfrac{16}{25}$, $m_{h}^{2}/M_{Z}^{2} = \tfrac{413}{125}$, $m_{\pm}^{2}/M_{Z}^{2} = \tfrac{368}{125}$, and different $(v/M_{P})^{2} = 2G\mathsf{N}$, with $\mathsf{N}_{B}^{2} - \mathsf{N}_{A}^{2} = H_{B}^{4} - H_{A}^{4}$. At $N = 10^{61}$ against $2 \times 10^{61}$ with $v/M_{P} = 2 \times 10^{-17}$ the relative change of $(v/M_{P})^{4}$ is below $10^{-176}$.
\item[(iii)] \emph{(The stored relations that contain $N$ hold in every model of (i).)} $G\Lambda = 3N^{-2}$, $(H/M_{P})^{2} = N^{-2}$ and, for each tree mass $\mu$, the Casimir value $(\mu/M_{P})^{2}N^{2} = \mu^{2}/H^{2}$ (Theorem \claimref{synthesis.smallness-monomials-exact-hierarchy-casimir}) are identities in $N$; the horizon entropy $\pi N^{2}$ and the mode count $4\pi\kappa_{c}N^{2}$ (Theorems \claimref{synthesis.de-sitter-entropy-pi-n-squared}, \claimref{synthesis.de-sitter-mode-count}) are functions of $N$ that no stored relation fixes by another route (the count is a density times an area, and no stored statement asserts that it is an integer; were integrality imposed, $N^{2}$ would be confined to a discrete set and still not fixed); $Gv^{2}N^{2} = (v/H)^{2}$ is an identity and $\mathsf{N}^{2} = m^{*2} + H^{4}$ is the stored dependence of the weak scale on $H$ at fixed level (Theorem \claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}); the discrete invariants of Theorem \claimref{standard-model.trichotomy-what-kind-number}(1) do not contain $I_{\Lambda}$. Under the Henneaux-Teitelboim promotion the models of (i) with one $\xi G$ are solutions of one theory, $N$ being constant on each and taking every positive value (Theorems \claimref{synthesis.promoted-norm-one-global-pair}, \claimref{synthesis.einstein-route-makes-n-initial-data}); under the action as written they are the members of the family of theories indexed by $\Lambda$ (Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}).
\item[(iv)] \emph{(The kinematic clause, proved for natural scale-free constructions.)} Let $(V, Q)$ be the ambient real quadratic space and $\Phi$ a function on $\{I \in V : Q(I) > 0\}$ with $\Phi(\gamma I) = \Phi(I)$ for every isometry $\gamma$ of $(V, Q)$ and $\Phi(sI) = \Phi(I)$ for every $s > 0$. Then $\Phi$ is constant. At fixed $M_{P}$, $N = M_{P}/\sqrt{Q(I)}$ is invariant under isometries and homogeneous of degree $-1$, so it takes every positive value and is not a function of such $\Phi$. Under the reading of "a construction from the conformal class and the pair structure alone" as a construction of this kind, this is the observation-level reading in Theorem \claimref{standard-model.trichotomy-what-kind-number}(1), proved. The clause covers only constructions that do not contain $G$: it says nothing about a relation between $Q(I)$ and the Planck scale, which is the business of (i) to (iii). The change of $N$ in (i) is a change of the datum $\Lambda$ at fixed $G$ and is not a symmetry: a dilation acting on every scale ($G \to G/s^{2}$, $H \to sH$, $m^{*} \to s^{2}m^{*}$) fixes $N$ and $\xi G$.
\end{enumerate}
The models use the branch $W = \kappa\mathsf{N}^{2}$, whose charged pair the record excludes, as in Theorem \claimref{synthesis.d-term-level-free-at-fixed-n}: they are models of the premise set and the stored relations at their pinned versions, not of the record. What is held fixed is $\xi G$, not $v/M_{P}$, which depends on $N$ through $\mathsf{N}^{2} = m^{*2} + H^{4}$. So, given the stored relations found by the search described in the extraction note, none fixes $N$ at fixed $\xi G$, and with that theorem the two registered inputs are jointly free: a derivation of $N$ would have to supply a relation, not an identity, between $Q(I_{\Lambda})$ in Planck units and numbers the premises fix, and the store holds none.

## technical
Given the stored rung-field action on the null-lift locus with the second invariant $\kappa\mathsf{N}^{2}$, a fixed D-term level in Planck units and fixed couplings, there is a stable vacuum for every value of the cosmological constant, at the frame where the hypercharge moment equals the level's value; so the number $N = M_{P}/H$ can be moved freely while the level, the couplings and every ratio of tree masses stay put. Two exact models, with $N = 21$ and $N = 16$, are exhibited. The stored relations that contain $N$ are either identities in $N$, definitions of quantities that scale with $N$ (the horizon entropy and mode count), or the stored weak dependence of the weak scale on $H$ at fixed level, and each holds in both models. Under the promoted action the models are solutions of one theory; under the action as written they are members of the family of theories indexed by $\Lambda$.

The observation-level reading of the trichotomy result, that no kinematic construction can fix $N$, is proved under a stated definition: a function of the frozen point that is invariant under the isometries of the ambient form and under positive rescaling is constant on frozen points of positive norm, because two reflections and a rescaling carry any one to any other, while $N$ has degree $-1$. That "no other stored relation contains $N$" is argued from a pattern search of the whole store and the joint past cone of the results that mention $N$ (519 entities, 40 postulates), not from a formal audit of every derivation. The models are not models of the record: the simple second invariant has a charged pair that collider data exclude.

## lay
The theory has one enormous number it does not explain, the ratio of the Planck mass to the scale set by the cosmological constant, and records it as an input. This result checks that nothing the theory has stored secretly fixes it. Assuming the theory's stored equations for its Higgs-like field, it builds two exact versions of the theory that agree in the strength of gravity, in every coupling and in the constant that sets the weak scale, and differ only in the cosmological constant; both satisfy every stored formula in which the big number appears, and in both every particle mass ratio is the same. It also proves a statement previously held only as a reading: provided a construction uses only the shape of the theory's basic geometric data and not their overall size, it cannot produce the number. So, given what is stored, the big number is a free input, independently of the weak scale's own free input. The search for stored formulas was done by pattern and reading, which is why that part is labelled as argued.

## one-liner
At fixed $G$, D-term level $\xi G$ and couplings (with $W = \kappa\mathsf{N}^{2}$) the frame with $m = m^{*}$ is a vacuum for every $H$, so every $(N, \xi G)$ is realised with the same tree mass ratios; every stored relation containing $N$ found by a search of the store holds in all these models (models of the premises, not of the record), and a function of the frozen point invariant under isometries and rescaling is constant, so under these premises nothing stored fixes $N$.
