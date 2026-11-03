---
id: note.singularity.setting-introduction
kind: note
version: 1
title: Introduction
status: setting
subject: singularity
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T05, deposited version
comments_on:
- singularity.degeneration-exactly
- singularity.imported-no-c-number-repair
- singularity.imported-no-equivariant-value-wall
- singularity.deficit-theorem-cost-descent-exactly
locators:
  paper: T05
  number: Setting
  section: Introduction
  line: 1222
---

## formal
The information paradox is usually posed as a conflict between two theories. This paper poses it as a comparison of entropies computed in two algebras, and computes them.

The setting is gauge theory gravity (GTG), the formulation of general relativity in the spacetime algebra $\Cl(1,3)$ due to Lasenby, Doran and Gull \cite{LDG1998}, in which gravity is a gauge field $\hb$, a position-dependent linear map on vectors, and every metrical statement is built from $\hb^{-1}$: the theory's geometric content exists exactly where $\hb$ is invertible. Section \ref{sec:locate} sets the theory out exactly, field equations, connection bivector and gauge laws included, because the chain's first step is a statement about those equations and must be made in them. For Schwarzschild in the Newtonian gauge, $\hb$ is invertible in closed form at every $r > 0$, horizon included, and is unimodular there, so nothing determinant-like ever degenerates: the divergence is carried entirely by the connection bivector, and at $r = 0$ the description fails in every gauge, through a null kernel, in the exact rescaled-limit sense of Proposition \claimref{singularity.degeneration-exactly}. The singularity is a division-by-zero locus in the literal, algebraic sense, and the transport principle of this series, the root paper T1 \cite{ButlerT1}, is a general theory of exactly such loci: it classifies the obstruction, forces a minimal completion, and quantifies what any return to the original level must lose. Its operational form is the six-step transport algorithm of \cite[\S 8.1, Table 1]{ButlerT1}, and this paper is that algorithm run end to end on the black hole; Table \ref{tab:algmap} gives the step-by-step correspondence.

The paper runs the resulting chain from the classical field to the Page curve, numbered by the transport algorithm of the root paper with the physics expanded where it lies (Steps 1 to 3, 4a to 4e, 5, 6a and 6b), each step carrying its declared status (proved, or proved from named premises). The steps are summarised in Table \ref{tab:chain} and constitute the paper's outline. Steps 1 through 5 are theorems, at their stated scopes: the location and type of the failure, the forced ascent to $\Cl(2,4)$, the installation of canonical anticommutation relations where classical repair is barred, on the approach by Fact \claimref{singularity.imported-no-c-number-repair} and at the boundary itself by Fact \claimref{singularity.imported-no-equivariant-value-wall}, the selection of the boost plane and its rate, the identity of boost and number operator, single-mode thermality at exactly $\TH$ with the state's marginals fixed by univalence and one regularity premise rather than assumed, the bosonic Planck sector by bosonisation in the s-wave-reduced sector under the named joint quasi-freeness premise (Q), and the lossy descent with its exact multi-mode cost (Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly}). Steps 6a and 6b remain conditional in substance, but every condition is a \emph{named postulate}: the boundary-mode capacity is a theorem from three axioms (curvature cutoff, cell density, counted epoch, the causal-epoch integral computed exactly in Lemma \claimref{singularity.causal-epoch-computed-exactly}), the radiation entropy of the rate model is an exact identity from localisation, purity, capacity, injection and boundary-mode locality, with the Page envelope its corollary and exact saturation confined to the zero-frequency idealisation, of which the linear weights supply exactly one mode, the sea level, so no window of two or more members ever saturates, the no-attic condition is derived rather than assumed, and the envelope with its endpoint needs no typicality and no assumption about where correlations are placed, boundary-mode locality being the one dynamical premise. The chain's conclusion on the paradox is a dissolution rather than a resolution: information is lost at the $\Cl(1,3)$ level and preserved at the $\Cl(2,4)$ level, these are the same physics read at two levels, and the discrepancy between the levels is not destruction but a fixed algebraic projection whose thermal output is the Hawking flux itself and whose size is an equation: the relative entropy of Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly}, carried entirely by the correlations of the quanta (Corollary \claimref{singularity.deficit-carried-quanta-correlations}).

The paper also contains an exactly solvable finite-mode model (Section \ref{sec:model}) in which the dissolution can be followed step by step, at both levels. In the model, every single radiated quantum is \emph{provably, exactly} thermal, by a parity-protection lemma stating that no encoding by phase scrambling can be visible to any single-quantum measurement; the joint radiation state is pure; the information is recoverable from inter-quanta correlations; the mutual-information computation per emission, together with the Page-shaped entropy sequence, is computed in exact arithmetic and machine-verified; and the multi-mode descent is applied to the radiation outright (Section \ref{subsec:descentapplied}), so that the two-level conclusion is exhibited in exact numbers (Table \ref{tab:model} and Proposition \claimref{singularity.two-levels-finite-model}) rather than argued. The model is a toy by construction and is offered as one: its value is that every claim in it is a computation, so the chain's conceptual endpoint (thermality as the record of what the projection cannot see; correlations as its carrier) is exhibited rather than argued.

A word on the standard of proof, binding throughout. The environments Theorem, Proposition and Lemma, with a Proof, are reserved for results proved \emph{in this paper}, at the standard of T1 \cite{ButlerT1}. Results proved elsewhere that the chain needs are stated as \textbf{Facts (imported)}, with their precise provenance; the typography tracks the epistemic content, so a reader can see at a glance which links of the chain this paper carries and which it inherits. Four links not previously proved are proved here outright: the finite-dimensional modular theory behind Step 4d; the state selection that completes it, the identification of the descent with the fermion parity average and the rigidity theorem that follows (Theorems \claimref{singularity.descent-parity-average}, \claimref{singularity.ascended-marginals-are-diagonal}, \claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}); the curvature behind Step 4b, derived in the gauge formalism in the text (Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}), with the appendix as an independent metric-picture cross-check; and the multi-mode descent behind Steps 5 and 6b, with its deficit theorem (Theorem \claimref{singularity.deficit-theorem-cost-descent-exactly}).

Throughout, the physics the chain touches is kept in the text deliberately: $\Cl(2,4)$ as the conformal algebra and the twistor connection (Step 3), Israel's thermofield double and the Bisognano-Wichmann-Sewell mechanism (Step 4d), the island dictionary and the Hayden-Preskill mirror (Step 6b). These points of contact frame what kind of object the chain produces at each stage; the derivations do not depend on them.

 \begin{tabular}{c>{ \arraybackslash}p{4.7cm}>{ \arraybackslash}p{4.6cm}l}
\toprule
Step & Content & Key formula & Status \\
\midrule
1 & \emph{locate the failure}: unipotent ray; cones fold & $\hb = 1 - \beta P$, $P^2 = 0$ & proved \\
2 & \emph{diagnose the type}: N, and type C excluded & $p - q \equiv 6 \bmod 8$ & proved, given Facts \ref{fact:schwtame}, \claimref{singularity.imported-one-sided-completion-singularity} \\
3 & \emph{apply the rule}: the forced ascent; conformal/twistor algebra & $\Cl(1,3) \to \Cl(2,4)$: $vv^* {+}\, v^*v = 1$ & proved, given Facts \ref{fact:schwtame}, \claimref{singularity.imported-one-sided-completion-singularity} \\
4a & \emph{compute in the completion}: the transport instantiated; operators forced & $\iota(s,x,t) = (2t, x, \tfrac12 s)$ & proved, given Facts \ref{fact:schwtame}, \claimref{singularity.imported-one-sided-completion-singularity} \\
4b & \emph{compute in the completion}: curvature selects the plane; the rate & $R(B) = -\tfrac{M}{r^3}S(B)$; $\kappa = 1/4M$ & proved (Schw.) \\
4c & \emph{compute in the completion}: boost $=$ number operator $=$ descent projectors & $\sigma = e_0 e_1 = 2N - 1$ & proved, given Facts \ref{fact:schwtame}, \claimref{singularity.imported-one-sided-completion-singularity} \\
4d & \emph{compute in the completion}: thermality; the marginals fixed, the joint state free & $\tan\theta = e^{-\omega/2T}$; $\beta = 2\pi/\kappa$ & proved from (P), (R) \\
4e & \emph{compute in the completion}: photons by bosonisation; Bose-Einstein at $\TH$ & $[a_m, a_{-m}] = m$ & proved (s-wave; the Planck factor from (Q)) \\
5 & \emph{descend, and state what descent costs}: deficit $=$ correlations & $S(E\rho) - S(\rho) = \rel{\rho}{E\rho}$ & proved; the reading by Prop.~\claimref{singularity.p-reduced-metric-level-reading-many} \\
6a & \emph{iterate, or stop}: the clock stops; boundary-mode capacity; area law & $dN_{\mathrm{6a}}/dt = \nu/\TH$; $C = N_{\mathrm{6a}}\ln 2$ & proved from (C1)-(C3) \\
6b & \emph{iterate, or stop}: two levels; Page envelope; eviction & $S_R = \sum_{k \in W} h_k \leq \min(\Sth, C)$ & proved from (L), (U), (C), (I), (L$_E$) \\
\midrule
-- & \textbf{new}: finite-mode correlation model, both levels & exact & proved (model) \\
\bottomrule
\end{tabular}

\emph{The transport chain, with statuses. The step names in italics are those of the transport algorithm of \cite[\S 8.1]{ButlerT1}, verbatim, and the section titles carry the same names; Table \ref{tab:algmap} gives the bijection. Each status is argued where the step is proved, and every premise is a named one stated in the text: univalence (P) and horizon regularity (R), the KMS condition at the period the Euclidean section fixes, imposed mode by mode, in Step 4d; joint quasi-freeness (Q) in Step 4e; the metric-level reading $\EN$, licensed in Step 5 by Proposition \claimref{singularity.p-reduced-metric-level-reading-many} up to its definitional antecedent; the capacity postulates (C1)-(C3) in Step 6a; localisation (L), purity (U), capacity (C) and injection (I), collected as Premise \claimref{singularity.rate-models-kinematic-inputs-l-u} in Step 6b, with boundary-mode locality (L$_E$) stated as Premise \claimref{singularity.l-boundary-mode-locality} in Step 4d and used in Step 6b, of which (L)'s exhaustiveness clause is the one carrying conjectural weight, and (I)'s freshness clause, like (L$_E$)'s never-return clause, is the rate model's own assumption rather than an import. Given them the statements are theorems; Step 6b uses no typicality and claims the envelope, the exact rising branch, the quantified falling branch and the endpoint; exact saturation of the falling branch holds only in the zero-frequency idealisation, of which the linear weights supply exactly one mode.}

## technical
pending

## lay
pending

## one-liner
pending
