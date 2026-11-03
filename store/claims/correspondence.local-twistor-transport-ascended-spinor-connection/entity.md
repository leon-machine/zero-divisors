---
id: correspondence.local-twistor-transport-ascended-spinor-connection
kind: claim
version: 7
title: "The conformal spinor connection is Penrose's local twistor transport"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [conformal-spinors, tractors, dictionaries]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.chiral-planes-summand-spaces@5
  - correspondence.clifford-side-ordering-shift@3
  - correspondence.imported-stabilisers-flat-model@3
  - correspondence.imported-tractor-connection-local-twistor-transport@6
  - correspondence.spin-representation@6
  - correspondence.fock-model-complexified-ascended-algebra@7
  - std-algebra.bivector-lie-algebra@1
  proof: proof-main.tex
- name: standard-route
  uses:
  - correspondence.imported-tractor-connection-local-twistor-transport-external@1
  proof: proof-standard-route.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:prop:localtwistor
- kind: check
  ref: check.py::check_gtg_fields_torsion_free_and_store_curvature
- kind: check
  ref: check.py::check_tractor_gauge_field_decomposition
- kind: check
  ref: check.py::check_grading_weights_and_spinor_blocks
- kind: check
  ref: check.py::check_summand_composite_and_equivariance
locators:
  paper: T09
  number: Prop 4.10
  label: prop:localtwistor
  line: 593
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-26
    date: '2026-10-26'
    note: 'Grounding pass 2026-10-26: cites std-algebra.bivector-lie-algebra where the proof uses them. Version 6 -> 7.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in GTG form for de Sitter and dust FLRW fields (hb, Omega, store curvature sign): torsion, Schouten map, the tractor gauge field''s Levi/soldering/Schouten split, grading weights, the spinor blocks on S_omega, S_pi, and the summand composite. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the conformal manifold may be the invertible region of a gravitational field on flat spacetime (spin, lift trivial), where the displayed decomposition is literally the tractor gauge field Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)) with u_p = ninf, X_p = n0, e_a = hb^{-1}(a); the general statement is kept.'
  env: proposition
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  unresolved_refs:
  - rem:ltconvention
  outside_pilot_cites:
  - ButlerT6
  typing:
    by: ai-typing-pass
    added:
    - correspondence.fock-model-complexified-ascended-algebra
    - correspondence.imported-tractor-connection-local-twistor-transport-external
    note: 'Added the Fock model because the statement builds the spin bundle from it; added a standard-route
      through the imported tractor and local-twistor literature bundle, since the paper says the identification
      is standard there, with the doubt that that bundle is a citation list rather than a statement of
      the identification. Levels pass: the lay now carries the spin assumption on the conformal manifold,
      and the technical and one-liner state it as an assumption rather than folding it into ''conformal
      spin manifold''.'
  source_title: "Local twistor transport is the ascended spinor connection"
  source_formal: |-
    Let $\mathcal{T}$ be the tractor bundle of \cite[\S 4]{ButlerT6} and $\T M$ its spin bundle: the rank-four complex bundle with fibre $\T$, carried by the fibrewise Fock model of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}, associated to a lift of the $SO(2,4)$ tractor bundle to $\mathrm{Spin}(2,4)$. We assume the conformal manifold is spin, so that the lift exists globally; every statement below is local, and locally a lift always exists. At a point, write $X_p$ for the canonical (tautological) null direction of $\mathcal{T}_p$, and, in a scale, $u_p$ for the null direction with $\ip{X_p}{u_p} = 1$ singled out by the splitting. Then:
    \begin{enumerate}
    \item the connection of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(i) decomposes, in the scale, as
    \[
    \nabla_a \;=\; \nabla^{g}_a \;-\; u_p \wedge e_a \;+\; X_p \wedge \mathrm{P}(e_a),
    \]
    where $\nabla^g$ couples the Levi factor only: the soldering summand is valued in $u_p\wedge W_\C$ and the Schouten summand in $X_p \wedge W_\C$, with $W_\C = (W_{1,3})_\C$ the complexified Minkowski complement, the latter in the nilradical of the parabolic stabilising $X_p$;
    \item on the spinor bundle, with $\Spi$ the plane of $\Psi(X_p)$ (the point's own line: the canonical subbundle) and $\Som$ the plane of $\Psi(u_p)$, the grading element $E := u_p\wedge X_p$ acts with eigenvalue $+\tfrac12$ on $\Som$ and $-\tfrac12$ on $\Spi$; consequently the soldering summand ($E$-weight $+1$) maps $\Spi \to \Som$ and annihilates $\Som$, and the Schouten summand ($E$-weight $-1$) maps $\Som \to \Spi$ and annihilates $\Spi$;
    \item the induced spinor connection therefore has, in the scale splitting $Z = (\omega, \pi)$ with $\omega \in \Som$, $\pi \in \Spi$, the form
    \[
    \nabla^{\T M}_a(\omega, \pi) = \bigl(\nabla^g_a\omega + \sigma_a\pi,\ \nabla^g_a\pi + \tau_a\omega\bigr),
    \]
    where $\sigma_a := \rho(-u_p\wedge e_a)|_{\Spi\to\Som}$ is the soldering summand and $\tau_a := \rho(X_p\wedge\mathrm{P}(e_a))|_{\Som\to\Spi}$ the Schouten summand.
    The summands are Levi-equivariant in the direction $e_a$, so by Lemma \claimref{correspondence.chiral-planes-summand-spaces}(2) each is the unique map of its type up to a scalar: under Levi-equivariant identifications of $\Som$, $\Spi$ with Penrose's $S^B$, $S_{B'}$, and the \emph{metric-normalised} identification of $W_\C$ with $S^B\otimes S^{B'}$ (the one under which $g_{ab}$ corresponds to $\varepsilon_{AB}\varepsilon_{A'B'}$, Penrose and Rindler's own, fixed up to sign), with $a = AA'$ and $c = CC'$ in the convention of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(ii), $\sigma_a$ is the $\varepsilon$-contraction $\pi_{A'} \mapsto \varepsilon_A{}^B\pi_{A'}$ times a constant $c_1$ and $\tau_a$ is the Schouten contraction $\omega^B \mapsto \mathrm{P}_{AA'BB'}\omega^B$ times a constant $c_2$. The constants depend on the relative scale of the two spinor identifications, which multiplies $c_1$ by $\lambda$ and $c_2$ by $\lambda^{-1}$ (the sign freedom of the third flips both, so it changes neither their product nor anything not already realised by $\lambda = -1$), so their product is invariant and is fixed by the composite of the summands on $\Som$:
    \[
    \sigma_a\,\tau_c \;=\; \tfrac12\,c(e_a)\,c(\mathrm{P}(e_c))\big|_{\Som} \;=\; \tfrac12\,\mathrm{P}_{ac}\,\id_{\Som} + \rho\bigl(e_a\wedge\mathrm{P}(e_c)\bigr)\big|_{\Som} .
    \]
    Local twistor transport (Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(ii)) has the same form, with summand composite $\omega^B \mapsto -\varepsilon_A{}^B\,\mathrm{P}_{CC'DA'}\,\omega^D$. Hence the local twistor bundle is $\T M$ and local twistor transport is the spinor square root of the tractor connection, exactly when the two composites agree, which is a single convention this identification imports: the sign and normalisation of $\mathrm{P}_{AA'BB'}$ in \cite{PenroseRindler86} relative to the Schouten tensor of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(i) (Remark \ref{rem:ltconvention}).
    \end{enumerate}
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed the spin bundle to the conformal spinor bundle \\CS M with fibre \\CS and stated the conclusion as: Penrose's local twistor bundle and transport are the conformal spinor bundle and its connection, the spinor square root of the tractor connection. Penrose and Rindler's two-spinor conventions and the factors $i$ of his transport formula, used in the proof's composite, are kept as imported, since the dictionary gives no GA reading for them; the grading element $E = u_p\\wedge X_p$ keeps the paper's symbol, which is not the dictionary's $E = e_+e_-$."
  i4_conversion:
    by: ai-i4-pass
    date: 2026-10-21
    converted: []
    kept:
    - "Penrose composite $i\\,\\varepsilon_A{}^B(i\\,\\mathrm{P}\\omega)$ and the factors $i$ of his transport formula: the conformal spinors unit $I_6$ in two-spinor notation, set by the earlier pass"
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - correspondence.fock-model-complexified-ascended-algebra
    stated_role:
    - correspondence.imported-tractor-connection-local-twistor-transport-external
---

## formal
Let $\mathcal{T}$ be the tractor bundle of \cite[\S 4]{ButlerT6} and $\CS M$ its spin bundle, the conformal spinor bundle: the rank-four complex bundle with fibre the conformal spinor space $\CS$, carried by the fibrewise Fock model of Theorem \claimref{correspondence.fock-model-complexified-ascended-algebra}, associated to a lift of the $SO(2,4)$ tractor bundle to $\mathrm{Spin}(2,4)$. We assume the conformal manifold is spin, so that the lift exists globally (on the invertible region of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), an open subset of flat spacetime, it does); every statement below is local, and locally a lift always exists. At a point, write $X_p$ for the canonical (tautological) null direction of $\mathcal{T}_p$, and, in a scale, $u_p$ for the null direction with $\ip{X_p}{u_p} = 1$ singled out by the splitting. Then:
\begin{enumerate}
\item the connection of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(i) decomposes, in the scale, as
\[
\nabla_a \;=\; \nabla^{g}_a \;-\; u_p \wedge e_a \;+\; X_p \wedge \mathrm{P}(e_a),
\]
(for a gravitational field on flat spacetime, with $u_p = \nInf$, $X_p = \nO$ and $e_a = \hb^{-1}(a)$, this is the gauge field $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$ of Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}, $\nabla^{g}$ being $\Omega(a)$), where $\nabla^g$ couples the Levi factor only: the soldering summand is valued in $u_p\wedge W_\C$ and the Schouten summand in $X_p \wedge W_\C$, with $W_\C = (W_{1,3})_\C$ the complexified Minkowski complement, the latter in the nilradical of the parabolic stabilising $X_p$;
\item on the spinor bundle, with $\Spi$ the plane of $\Psi(X_p)$ (the point's own line: the canonical subbundle) and $\Som$ the plane of $\Psi(u_p)$, the grading element $E := u_p\wedge X_p$ acts with eigenvalue $+\tfrac12$ on $\Som$ and $-\tfrac12$ on $\Spi$; consequently the soldering summand ($E$-weight $+1$) maps $\Spi \to \Som$ and annihilates $\Som$, and the Schouten summand ($E$-weight $-1$) maps $\Som \to \Spi$ and annihilates $\Spi$;
\item the induced spinor connection therefore has, in the scale splitting $Z = (\omega, \pi)$ with $\omega \in \Som$, $\pi \in \Spi$, the form
\[
\nabla^{\CS M}_a(\omega, \pi) = \bigl(\nabla^g_a\omega + \sigma_a\pi,\ \nabla^g_a\pi + \tau_a\omega\bigr),
\]
where $\sigma_a := \rho(-u_p\wedge e_a)|_{\Spi\to\Som}$ is the soldering summand and $\tau_a := \rho(X_p\wedge\mathrm{P}(e_a))|_{\Som\to\Spi}$ the Schouten summand.
The summands are Levi-equivariant in the direction $e_a$, so by Lemma \claimref{correspondence.chiral-planes-summand-spaces}(2) each is the unique map of its type up to a scalar: under Levi-equivariant identifications of $\Som$, $\Spi$ with Penrose's $S^B$, $S_{B'}$, and the \emph{metric-normalised} identification of $W_\C$ with $S^B\otimes S^{B'}$ (the one under which $g_{ab}$ corresponds to $\varepsilon_{AB}\varepsilon_{A'B'}$, Penrose and Rindler's own, fixed up to sign), with $a = AA'$ and $c = CC'$ in the convention of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(ii), $\sigma_a$ is the $\varepsilon$-contraction $\pi_{A'} \mapsto \varepsilon_A{}^B\pi_{A'}$ times a constant $c_1$ and $\tau_a$ is the Schouten contraction $\omega^B \mapsto \mathrm{P}_{AA'BB'}\omega^B$ times a constant $c_2$. The constants depend on the relative scale of the two spinor identifications, which multiplies $c_1$ by $\lambda$ and $c_2$ by $\lambda^{-1}$ (the sign freedom of the third flips both, so it changes neither their product nor anything not already realised by $\lambda = -1$), so their product is invariant and is fixed by the composite of the summands on $\Som$:
\[
\sigma_a\,\tau_c \;=\; \tfrac12\,c(e_a)\,c(\mathrm{P}(e_c))\big|_{\Som} \;=\; \tfrac12\,\mathrm{P}_{ac}\,\id_{\Som} + \rho\bigl(e_a\wedge\mathrm{P}(e_c)\bigr)\big|_{\Som} .
\]
Penrose's local twistor transport (Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(ii)) has the same form, with summand composite $\omega^B \mapsto -\varepsilon_A{}^B\,\mathrm{P}_{CC'DA'}\,\omega^D$. Hence Penrose's local twistor bundle is the conformal spinor bundle $\CS M$ and his local twistor transport is the conformal spinor connection, the spinor square root of the tractor connection, exactly when the two composites agree, which is a single convention this identification imports: the sign and normalisation of $\mathrm{P}_{AA'BB'}$ in \cite{PenroseRindler86} relative to the Schouten tensor of Fact \claimref{correspondence.imported-tractor-connection-local-twistor-transport}(i) (Remark \ref{rem:ltconvention}).
\end{enumerate}

## technical
On a conformal manifold, assumed spin so that the lift to $\mathrm{Spin}(2,4)$ exists globally (every statement being local), let $\CS M$ be the rank-four spin bundle of the tractor bundle, with fibre the conformal spinor half $\CS$ of the fibrewise Fock model. In a scale the tractor connection splits as $\nabla_a = \nabla^g_a - u_p\wedge e_a + X_p\wedge\mathrm{P}(e_a)$, which for a gravitational field on flat spacetime is the $\Cl(2,4)$ gauge field $\Omega(a) - \nInf\wedge\hb^{-1}(a) + \nO\wedge\mathrm{P}(\hb^{-1}(a))$, a Levi part plus a soldering summand valued in $u_p\wedge W_\C$ and a Schouten summand valued in $X_p\wedge W_\C$, where $X_p$ is the tautological null direction and $u_p$ its partner singled out by the scale. The grading element $E = u_p\wedge X_p$ acts as $+\tfrac12$ on $\Som$ and $-\tfrac12$ on $\Spi$, so the soldering summand maps $\Spi\to\Som$, the Schouten summand maps $\Som\to\Spi$, and the induced spinor connection reads $\nabla_a(\omega,\pi) = (\nabla^g_a\omega + \sigma_a\pi,\ \nabla^g_a\pi + \tau_a\omega)$.

By uniqueness of the equivariant maps, $\sigma_a$ and $\tau_a$ are Penrose's $\varepsilon$-contraction and Schouten contraction up to constants $c_1$, $c_2$, whose product is invariant and fixed by the composite $\sigma_a\tau_c = \tfrac12 c(e_a)c(\mathrm{P}(e_c))|_{\Som}$. Penrose's local twistor transport has the same form, so his local twistor bundle is $\CS M$ and his transport is the conformal spinor connection, the spinor square root of the tractor connection, exactly when the two composites agree, which is a single imported convention: the sign and normalisation of Penrose and Rindler's $\mathrm{P}_{AA'BB'}$ relative to the tractor Schouten tensor.

## lay
Two older formalisms describe the geometry of conformal spacetime: tractors, a six-component bundle with its own connection, and Penrose's four-component bundle with its own transport rule. Assuming the conformal spacetime is spin, so that the tractor bundle has spinors (locally they always exist), this result shows that those spinors, built from the completion's Fock model, carry a connection with exactly the shape of Penrose's transport rule. The two agree completely once one sign and normalisation convention for the curvature term is matched, and that convention is the only thing imported.

## one-liner
Assuming the conformal manifold is spin, the spinor connection induced from the tractor connection has exactly the form of Penrose's local transport of four-component spinors, and the two coincide up to one imported sign and normalisation convention for the Schouten term.
