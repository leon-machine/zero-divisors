---
id: synthesis.d-term-level-free-at-fixed-n
kind: claim
version: 1
title: 'The D-term level is free at fixed N on the stored relations'
status: proved
region: synthesis
subject: standard-model
tags: [undetermined-input, the-number-n, symmetry-breaking, finite-models]
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
  - synthesis.rung-field-on-the-lift-locus@5
  - synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus@6
  - synthesis.rung-field-level-needed-off-balance-and-not-right-invariant@5
  - synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion@3
  - synthesis.smallness-monomials-exact-hierarchy-casimir@3
  - standard-model.trichotomy-what-kind-number@12
  - families.why-kinematic-attacks-had-fail@4
  - synthesis.einstein-route-makes-n-initial-data@4
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2
  - synthesis.imported-fayet-iliopoulos-level-only-for-abelian-factors@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_two_frames_are_vacua_with_the_same_dimensionless_spectrum
- kind: check
  ref: check.py::check_the_two_models_differ_in_xi_g_at_equal_n
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.rung-unit-second-free-number
  - synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion
extraction:
  open_problem: op.rung-unit
  note: >-
    The independence item of op.rung-unit: show that no stored premise or relation fixes the constant of the laws
    xi G (equivalently v/M_P), which the register already holds as a free input (Premise
    synthesis.rung-unit-second-free-number, version 3); this does not re-register it. The premise set of the
    problem's eight entities at their pinned versions (union of past cones, 248 entities) is (F1)-(F4), the
    slot-module premise, the indifference premise, (C_loc), sheaf tameness, P2 and P3 for the towers, the rung-unit
    premise and imported Facts (Henneaux-Teitelboim promotion, Fayet-Iliopoulos level only for abelian factors,
    left-right bidoublet, Coleman-Weinberg and Gildener-Weinberg, B-mixing inputs, the two-doublet scalon sum, de
    Sitter representations, tractor, frozen-point and GTG imports, the record's M_P/H); Premise (N) is added because
    the claim is at fixed N. A search of the store's formal texts for M_P or Planck together with a weak-scale
    quantity returns the identities used here, the induced-gravity result (G only through an unfixed cut-off), the
    trichotomy rescaling and its kinematic reading, the Majorana-scale results (Hubble-unit Majorana vev excluded),
    the lift-locus results (H enters at relative (H/v)^4), the rung-frame results (rung-unit-is-frame-boost, rung-unit-transverse-to-norm: the frame, no G), the scale-free potential result (synthesis.scale-free-rung-potentials-need-the-flat-physical-branch, on the cone Q = 0, a different locus), the transmutation and quartic-running results (masses and couplings, no G), and readings at conjectured status (programme.n-parameter-of-the-laws, standard-model.dating-descent, standard-model.one-number-explain); none fixes xi G. Postulates of the cone with claimrefs included, beyond those named above: (P), (Q), (R) of the boundary modes, (R_Lambda), the Krein premise, R1-R3 and H1 of the towers (reached through the induced-Newton result), P2, P3 and sheaf tameness; none contains xi or a weak-sector scale.
    Derivation attempts (attack item 2), argued: a level that is an su(2)_R-breaking remnant of the Pati-Salam stage,
    xi = c v_R^2 with c a number, is a G-free relation; the chain fixes v_R against M_Z from the gauge data, so it
    could fix v/v_R (a test) and never xi G. A level proportional to Lambda, xi = k H^2, makes v/H the law (the
    branch the register's version 2 held) and needs k of order 10^88, a new dimensionless constant. Transport-absent:
    the rung field's action and gravity's two constants; the series content is the rung field on the lift locus.
---

## formal
Take the D-term action of Theorem \claimref{synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus} on the null-lift locus $L = \{Q(c) = -H^{2}\}$, $H^{2} = \Lambda/3$, with an added invariant $W(\mathsf{N}) = \kappa\mathsf{N}^{2}$, $\kappa \ge 0$, so $V = V_{D} + \kappa\mathsf{N}^{2}$ with $V_{D} = \tfrac12\bigl(g^{2}\sum_{j}\mu_{j}^{2} + g'^{2}(\mu_{Y} - \zeta)^{2}\bigr)$, $\xi = 2\zeta$, the lift family $c_{\lambda}$ ($\alpha = (H^{2}/\lambda, 0)$, $\beta = (-\lambda, 0)$, $\mathsf{N} = \tfrac12(H^{4}/\lambda^{2} + \lambda^{2})$, $m = \tfrac12(H^{4}/\lambda^{2} - \lambda^{2})$), Newton's constant $G = M_{P}^{-2}$ and $N = M_{P}/H$.
\begin{enumerate}
\item[(i)] \emph{(A vacuum in every frame.)} For every $\lambda > 0$, $\lambda \neq H$, the level $\xi(\lambda) = m(\lambda)(g^{2} + g'^{2} + 8\kappa)/g'^{2}$ makes $c_{\lambda}$ a charge-preserving critical point of $V$ on $L$, with $\xi/m > 1$, $M_{W}^{2} = \tfrac12 g^{2}\mathsf{N}$, $M_{Z}^{2} = \tfrac12(g^{2} + g'^{2})\mathsf{N}$, $m_{h}^{2} = M_{Z}^{2} + 4\kappa\mathsf{N}$ and the charged pair at $m_{\pm}^{2} = M_{W}^{2} + 4\kappa\mathsf{N}$, all positive. Every tree mass squared is a fixed multiple of $\mathsf{N}(\lambda)$, so the dimensionless tree spectrum is the same in every frame.
\item[(ii)] \emph{(Two models at equal $N$.)} Two frames $\lambda_{1} \neq \lambda_{2}$ with $\mathsf{N}(\lambda_{1}) \neq \mathsf{N}(\lambda_{2})$ give two models with the same $G$, $\Lambda$ and so $N$ ($G\Lambda = 3N^{-2}$), the same $g$, $g'$, $\kappa$, lift locus and dimensionless tree spectrum, and different $v^{2} = 2\mathsf{N}$, $(v/M_{P})^{2} = 2\mathsf{N}/(H^{2}N^{2})$ and $\xi G$. At $H^{2} = 1$, $G = \tfrac{1}{100}$ ($N = 10$), $g = \tfrac23$, $g' = \tfrac12$, $\kappa = \tfrac15$, the frames $\tfrac13$ and $\tfrac15$ give $\mathsf{N} = \tfrac{41}{9}$ and $\tfrac{313}{25}$, $\xi G = \tfrac{826}{2025}$ and $\tfrac{10738}{9375}$, $(v/M_{P})^{2} = \tfrac{41}{450}$ and $\tfrac{313}{1250}$; at $N = 10^{61}$ the frames $10^{-44}H$ and $2 \times 10^{-44}H$ give $(v/H)^{2} > 10^{87}$ and values of $(v/M_{P})^{2}$ in a ratio between $3$ and $5$.
\item[(iii)] \emph{(What the stored relations say in both.)} In both models the stored relations that contain $G$ or $M_{P}$ together with a weak-sector quantity hold: $Gv^{2}N^{2} = (v/H)^{2}$ and, for each tree mass, $(m/M_{P})^{2}N^{2} = m^{2}/H^{2}$ (Theorem \claimref{synthesis.smallness-monomials-exact-hierarchy-casimir}), identities; on the boundary $V_{D} = \tfrac12\bigl(\tfrac14 g^{2}m^{2} + g'^{2}(\tfrac{m}{2} - \zeta)^{2}\bigr)$ contains no $H$ (Theorem \claimref{synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion}); the level sits on the hypercharge, the centre (Fact \claimref{synthesis.imported-fayet-iliopoulos-level-only-for-abelian-factors}); the induced Newton coupling of Theorem \claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off} matches $G$ in each through its own cut-off; and Premise (N) (\claimref{synthesis.number-n-registered-free-input}) and the rung-unit premise (\claimref{synthesis.rung-unit-second-free-number}) assert only that $N$ and $\xi G$ are inputs.
\end{enumerate}
The models use the branch $W = \kappa\mathsf{N}^{2}$, whose charged pair the record excludes (\claimref{synthesis.rung-field-charged-scalar-sum-rule}); they are models of the premise set and the stored relations at their pinned versions, not of the record, which is what independence needs.
So no stored premise or relation fixes $\xi G$, and it is not a function of $N$, of the gauge couplings or of $W$: a dynamics that derived it would have to supply a relation, not an identity, containing both $G$ (or $M_{P}$) and a weak-sector scale, and the store holds none.

## technical
The weak scale's constant of the laws, the D-term level in Planck units, is shown to be unconstrained by everything the store holds, at fixed $N = M_{P}/H$. On the null-lift locus the D-term potential plus the second invariant $\kappa\mathsf{N}^{2}$ has a charge-preserving vacuum in every frame of the lift family, at the level that frame needs; with this $W$ every tree mass squared is an exact multiple of the rung field's norm, so the dimensionless spectrum is the same in every frame, and only the overall size of the weak scale against the Planck mass moves. Two such vacua, at the same Newton constant and cosmological constant, are two models of the stored relations with different $\xi G$ and different $v/M_{P}$. The stored relations that mix the Planck and weak scales are identities, hold in both, or reach $G$ through a free cut-off. The check verifies the vacuum, the Hessian masses on the locus and the model values exactly in two frames, and the ratio of $v/M_{P}$ in two realistic frames at $N = 10^{61}$.

Independence costs nothing the register has not already paid: $\xi G$, about $(2 \times 10^{-17})^{2}$ in $v/M_{P}$, is a recorded input of the laws, and every use of the weak scale in Planck or Hubble units ($v/H \approx 2 \times 10^{44}$ at the measured $N$) is a value taken from the record. Two routes to a derivation fail for a stated reason: a level left over from the Pati-Salam breaking is a relation without $G$, so it can relate the weak scale to the intermediate scale but not to the Planck scale; a level proportional to $\Lambda$ needs a new constant of order $10^{88}$.

## lay
The theory has two numbers it does not explain: the ratio of the Planck mass to the Hubble rate, and the size of the weak scale (set by the Higgs field) against the Planck mass. The second is recorded as an input. This result checks that nothing the theory has stored secretly fixes it. It builds two exact versions of the theory's Higgs-like field, identical in gravity, in the cosmological constant and in every coupling, which differ only in one constant of the field's potential. Both satisfy every assumption and stored formula of the theory (the simple potential used is ruled out by collider data, which does not matter for this question, since it is about what the theory's own assumptions fix); in both every particle mass ratio is the same; only the weak scale in Planck units differs. Every stored formula that mentions both scales holds in both versions. So the weak scale against gravity is a free input, as recorded.

## one-liner
With $W = \kappa\mathsf{N}^{2}$ every frame $c_{\lambda}$ of the lift family is a stable vacuum at $\xi = m(g^{2} + g'^{2} + 8\kappa)/g'^{2}$ with all tree masses squared fixed multiples of $\mathsf{N}$; two frames at equal $G$, $\Lambda$ ($N$) and couplings are models with different $\xi G$ and $v/M_{P}$, in which every stored relation mixing the Planck and weak scales holds (on a branch the record excludes; models of the premises, not of the record), so no stored relation fixes $\xi G$.
