---
id: mass.imported-flat-model-twistor-chart-infinity
kind: claim
version: 7
title: "Imported: the flat model, the conformal spinor chart, and the infinity bivector"
status: proved
region: mass
subject: conformal-spacetime
tags: [conformal-model, conformal-spinors, frozen-point]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T11, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.fock-model-complexified-ascended-algebra@8
  - correspondence.incidence-relation-chart@5
  - correspondence.one-statement-three-languages@5
  - correspondence.spin-representation@6
  - correspondence.spinor-identification@7
  - mass.imported-flat-model-twistor-chart-infinity-external@1
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T11.py
  tags:
  - label:fact:chart
- kind: check
  ref: check.py::check_null_embedding_and_forced_coefficient
- kind: check
  ref: check.py::check_simple_iff_null_and_planes
- kind: check
  ref: check.py::check_scale_function_is_sigma_slot
- kind: check
  ref: check.py::check_sl_action_is_isomorphism_onto_so
- kind: check
  ref: check.py::check_infinity_bivector_simple_iff_flat
locators:
  paper: T11
  number: Fact 2.3
  label: fact:chart
  line: 422
extraction:
  maintainer_pass:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 6 -> 7. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: in T11''s Lambda^2 C^4 model: the null embedding X(x) with the forced -1/2, Q = -2 det on the x-slot, simple iff null, the scale function as sigma-slot, sl(4) -> so(Lambda^2, eps) an isomorphism, and the infinity bivector simple iff Lambda = 0. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested (the simple-iff-flat test now collects the simple samples and asserts they are exactly [0]). Version 5 -> 6.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  env: fact
  context_refs:
  - correspondence.fock-model-complexified-ascended-algebra
  - correspondence.incidence-relation-chart
  - correspondence.one-statement-three-languages
  - correspondence.spin-representation
  - correspondence.spinor-identification
  - interior.sign-fixed-internally
  - mass.de-sitter-scale-frozen-point
  outside_pilot_cites:
  - ButlerT6
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    removed:
    - interior.sign-fixed-internally
    note: The sign lemma of the interior paper is cited only as a place where the scale function is used,
      not as a source, so it was removed; the de Sitter scale lemma that proves the flat-model dictionary
      was not added because it uses this fact (it would be circular).
  source_title: "Imported: the flat model, the twistor chart, and the infinity twistor"
  source_formal: |-
    On a conformally flat region the ambient bundle is trivial: its fibre is one fixed vector space $V$ with the ambient pairing, parallel sections are constant vectors, and the canonical tractor at the point $x$ is $X(x) = n_{0} + x - \tfrac12 Q(x)\, n_{\infty}$, with $n_{0}, n_{\infty}$ null, $\ip{n_{0}}{n_{\infty}} = +1$, $x$ in their orthogonal complement, and $Q(x) = \ip{x}{x} = g(x,x)$ the flat quadratic form, so that $\ip{X(x)}{X(x)} = 0$ identically. The scale function of a constant vector $V$ is its $\sigma$-slot in the flat scale, $\sigma_{V}(x) = \ip{X(x)}{V}$. The complexification of $V$ is $\Lambda^{2}\T$ for $\T$ the twistor space (the chirality half of the ascended Dirac module), with pairing $\ip{U}{U'} = \varepsilon(U \wedge U')$ for the volume form $\varepsilon$ on $\Lambda^{4}\T$ that the identification fixes; a bivector is simple iff its norm vanishes; the mixed slot carries $\ip{x}{x} = -2\det x$ in the chart's components \cite[Thm.~4.2(2)]{ButlerT9}; a twistor splits as $Z = (\omega, \pi)$ with $\omega$ in the two-plane $\Sc$ whose Pl\"ucker bivector is $n_{\infty}$ and $\pi$ in the two-plane $\Sc'$ whose Pl\"ucker bivector is $n_{0}$. The action of $\mathfrak{sl}(\T)$ on $\Lambda^{2}\T$ by $A\cdot(u \wedge v) = Au \wedge v + u \wedge Av$ is a Lie algebra isomorphism onto $\mathfrak{so}(\Lambda^{2}\T, \varepsilon)$, and the infinity twistor of a scale is the image of its scale tractor: for a vacuum with $\Lambda = 0$ it is covariantly constant and simple, the Pl\"ucker bivector of the infinity line. \emph{Provenance:} the flat model as a fixed vector space with the point embedding is \cite[\S4.2]{ButlerT6}, the scale function $\sigma = \ip{X}{I}$ recovering $g = \sigma^{-2}\eta$ is used in \cite[Lem.~4.8]{ButlerT6}, and the general form of the dictionary (parallel sections are constant vectors, with $\sigma$-slot $\ip{X(x)}{V}$) is \cite[\S2]{BEG1994}; in the form needed here it is elementary and is proved in one paragraph inside Lemma \claimref{mass.de-sitter-scale-frozen-point}; the chirality half is \cite[Thm.~3.1]{ButlerT9}; the identification $V_{\C} = \Lambda^{2}\T$ with its pairing, the normalisation of $\varepsilon$, the simplicity criterion, and the equivariance of the identification are \cite[Thm.~3.4]{ButlerT9}; the chart, the identification of the incidence relation with the completion's own chart, the spin isomorphism, and the infinity twistor are \cite[Thm.~4.2, Cor.~4.8, Prop.~5.2]{ButlerT9}, in that paper's sign conventions, machine-verified there. The spinor bracket $\br{\pi^{1}\pi^{2}} = \varepsilon^{AB}\pi^{1}_{A}\pi^{2}_{B}$, the null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ of a twistor, and the conformal generators as Hermitian quadratics $\bar{Z}_{\alpha}Z^{\beta}$ in the twistor variables are classical \cite{PenroseRindler1986, Hughston1979}.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space, twistors and the infinity twistor to the conformal spinor space, conformal spinors and the infinity bivector in all levels and the restating proof, and wrote the chart halves as $\\Som$, $\\Spi$ (they were $\\Sc$, $\\Sc'$). Penrose's two-spinor index notation and the cited classical material are kept."
---

## formal
On a region where the gravitational field is a pure dilation $\hb = \sigma$ of the flat background in some gauge (so the Weyl part of the field strength vanishes; derived metric $\sigma^{-2}\eta$) the ambient bundle is trivial: its fibre is one fixed vector space $V$ with the ambient pairing, parallel sections are constant vectors, and the canonical tractor at the point $x$ is $X(x) = n_{0} + x - \tfrac12 Q(x)\, n_{\infty}$, with $n_{0}, n_{\infty}$ null, $\ip{n_{0}}{n_{\infty}} = +1$, $x$ in their orthogonal complement, and $Q(x) = \ip{x}{x} = g(x,x)$ the flat quadratic form, so that $Q(X(x)) = 0$ identically. The scale function of a constant vector $V$ is its $\sigma$-slot in the flat scale, $\sigma_{V}(x) = \ip{X(x)}{V}$. The complexification of $V$ is $\Lambda^{2}\CS$ for $\CS$ the conformal spinor space (twistor space; the chirality half of the ascended Dirac module), with pairing $\ip{U}{U'} = \varepsilon(U \wedge U')$ for the volume form $\varepsilon$ on $\Lambda^{4}\CS$ that the identification fixes; a bivector is simple iff its norm vanishes; the mixed slot carries $Q(x) = -2\det x$ in the chart's components \cite[Thm.~4.2(2)]{ButlerT9}; a conformal spinor splits as $Z = (\omega, \pi)$ with $\omega$ in the two-plane $\Som$ whose Pl\"ucker bivector is $n_{\infty}$ and $\pi$ in the two-plane $\Spi$ whose Pl\"ucker bivector is $n_{0}$. The action of $\mathfrak{sl}(\CS)$ on $\Lambda^{2}\CS$ by $A\cdot(u \wedge v) = Au \wedge v + u \wedge Av$ is a Lie algebra isomorphism onto $\mathfrak{so}(\Lambda^{2}\CS, \varepsilon)$, and the infinity bivector of a scale (the infinity twistor) is the image of its scale tractor: for a vacuum with $\Lambda = 0$ it is covariantly constant and simple, the Pl\"ucker bivector of the infinity line. \emph{Provenance:} the flat model as a fixed vector space with the point embedding is \cite[\S4.2]{ButlerT6}, the scale function $\sigma = \ip{X}{I}$ recovering $g = \sigma^{-2}\eta$ is used in \cite[Lem.~4.8]{ButlerT6}, and the general form of the dictionary (parallel sections are constant vectors, with $\sigma$-slot $\ip{X(x)}{V}$) is \cite[\S2]{BEG1994}; in the form needed here it is elementary and is proved in one paragraph inside Lemma \claimref{mass.de-sitter-scale-frozen-point}; the chirality half is \cite[Thm.~3.1]{ButlerT9}; the identification $V_{\C} = \Lambda^{2}\CS$ with its pairing, the normalisation of $\varepsilon$, the simplicity criterion, and the equivariance of the identification are \cite[Thm.~3.4]{ButlerT9}; the chart, the identification of the incidence relation with the completion's own chart, the spin isomorphism, and the infinity bivector are \cite[Thm.~4.2, Cor.~4.8, Prop.~5.2]{ButlerT9}, in that paper's sign conventions, machine-verified there. The spinor bracket $\br{\pi^{1}\pi^{2}} = \varepsilon^{AB}\pi^{1}_{A}\pi^{2}_{B}$, the null momentum $p_{AA'} = \pi_{A}\bar\pi_{A'}$ of a conformal spinor, and the conformal generators as Hermitian quadratics $\bar{Z}_{\alpha}Z^{\beta}$ in the conformal spinor variables are classical \cite{PenroseRindler1986, Hughston1979}.

## technical
On a region where the gravitational field is a pure dilation $\hb = \sigma$ of the flat background in some gauge (so the Weyl part of the field strength vanishes; derived metric $\sigma^{-2}\eta$) the ambient bundle is trivial with one fixed fibre $V$: parallel sections are constant vectors, the canonical tractor is $X(x) = n_0 + x - \tfrac12 Q(x)\,n_\infty$ with $n_0, n_\infty$ null and $\ip{n_0}{n_\infty} = 1$, so $Q(X(x)) = 0$, and a constant vector $V$ has scale function $\sigma_V(x) = \ip{X(x)}{V}$.

Complexified, $V_\C = \Lambda^2\CS$ with $\ip{U}{U'} = \varepsilon(U \wedge U')$; null bivectors are exactly the simple ones, the mixed slot carries $Q(x) = -2\det x$, and a conformal spinor splits as $Z = (\omega, \pi)$ along the planes of $n_\infty$ and $n_0$. The action of $\mathfrak{sl}(\CS)$ on $\Lambda^2\CS$ is an isomorphism onto $\so(\Lambda^2\CS, \varepsilon)$, and the infinity bivector of a scale is its scale tractor, covariantly constant and simple when $\Lambda = 0$. Classical ingredients from twistor theory (the spinor bracket, the null momentum $p_{AA'} = \pi_A\bar\pi_{A'}$, the generators as Hermitian quadratics) are imported alongside.

## lay
This gathers in one place the flat-space set-up that the mass paper builds on. A point of flat spacetime is represented by a light-like vector in a six-dimensional space, and that space can be rebuilt from pairs of four-component spinors of the conformal algebra. In this picture the conformal symmetries act on those spinors as matrices, and the bivector at infinity that records the choice of scale is, when the cosmological constant vanishes, a fixed line in the projective spinor space.

## one-liner
Imported: on the flat model the point embedding is null, $V_\C = \Lambda^2\CS$ with null meaning simple, $\mathfrak{sl}(\CS) \cong \so(\Lambda^2\CS, \varepsilon)$, and for $\Lambda = 0$ the infinity bivector is constant and simple.
