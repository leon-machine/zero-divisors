---
id: synthesis.c-loc-entropy-clause-curvature-independent-density
kind: claim
version: 3
title: 'A curvature-independent horizon entropy density is one constant, 1/4'
status: proved
region: synthesis
subject: einstein
tags: [counting-rules, horizons, entropy-premises, forcing-and-uniqueness, curvature-and-field-equations, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-22-cloc
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.imported-jacobson-clausius-1995@2
  - synthesis.quarter-from-temperature@1
  - synthesis.de-sitter-entropy-pi-n-squared@5
  - synthesis.imported-kerr-surface-gravity-entropy@2
  - synthesis.clausius-route-newton-constant-is-residue@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_lorentz_transitive_on_horizon_data
- kind: check
  ref: check.py::check_boost_rescales_ray_fixes_plane
- kind: check
  ref: check.py::check_eta_from_temperature
- kind: check
  ref: check.py::check_clausius_forces_constant_density
- kind: proof
  derivation: main
extraction:
  open_problem: op.derive-c-loc
  note: >-
    On (C_loc), clause (i). What is proved: (1) a Lorentz lemma, transitivity of the proper
    orthochronous group on (future null ray, orthogonal spacelike edge plane), with a stabiliser that
    rescales the ray and fixes the plane's area; so a density depending only on the flat tangent data
    of a horizon element is one constant. The substantive input is the hypothesis itself: independence
    of the density from the curvature and the matter at the point, which are O(1) point values, not
    small in the patch size. That hypothesis excludes by assumption the curvature-dependent (Wald-type)
    entropy densities of the Ricci-polynomial extensions, which are what black-hole data cannot
    exclude; so the selection of Einstein's equations over those extensions on this route comes from
    curvature independence, not from locality. (2) Under (P), (R), Hawking's hypothesis and the
    identification of the hole's thermodynamic entropy with the integral of the density (one mode set),
    eta = lim S/A = 1/4 with no count and no nu; with a period p in place of the regular one,
    eta = p kappa/(8 pi). De Sitter and Kerr agree. The count form eta = 4 pi nu <s> is the area-law
    condition; the calibration returns G_cl = G, a consistency, not a determination of G. (3) Under
    S = integral of eta dA, the Clausius relation alone already forces eta constant at first order in the
    patch. Fix round 2026-10-22-cloc: restated after review (the earlier title said the form was forced
    by locality); ray gap in the lemma closed; calibration hypothesis stated; Clausius clause added;
    the Killing-to-Rindler step no longer used; independent placement said to be excluded.
    Transport-absent.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the flat tangent data are the physical vectors at the point of the invertible region of a gravitational field on flat spacetime with their flat product (the tangent Minkowski space of the derived metric), curvature is the field strength, the stress-energy is T(a), and the gradient condition reads k.D eta = 0 for physical null k; the transitivity lemma now notes that all tangent spaces are one space of physical vectors. Signature (-,+,+,+) kept as declared. Content and hypotheses unchanged; proof given a pointer to the dictionary Fact. Check strengthened: the four spanning vectors are asserted null (only their rank was tested); samples moved to module level. Version 2 -> 3.'
---

## formal
Signature $(-,+,+,+)$ in this statement and its proof, with $Q(v)$ the square of a vector $v$; the store's $(+,-,-,-)$ changes the sign of $Q$ and of every inner product below and nothing else. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Let the flat tangent data of a local Rindler horizon element at a point $p$ of its invertible region be the space of physical vectors at $p$ with the flat product (the tangent Minkowski space $(T_{p}M, g_{p})$ of the derived metric), a future null ray $[\ell]$ and the spacelike two-plane $\Pi \subset \ell^{\perp}$ of the edge element, as in Fact \claimref{synthesis.imported-jacobson-clausius-1995}. Call (Loc) the condition: \emph{the entropy of a small patch of a horizon is, at leading order in the size of the patch, the integral over its cross-section of a density $s$ per unit area whose value at each point depends only on the isometry class of the flat tangent data there; in particular $s$ is independent of the curvature (the field strength $\mathcal{R}$) and of the stress-energy $T$ at the point, and of the normalisation of the boost.}
\begin{enumerate}
\item[(i)] \emph{(One constant.)} The proper orthochronous Lorentz group acts transitively on pairs (future null ray, spacelike two-plane orthogonal to it): for future null $\ell$, $n$ with $\ell\cdot n \neq 0$, at most two reflections in spacelike vectors carry $(\ell_{0}, n_{0}, \Pi_{0}) = (e_{0} + e_{1}, e_{0} - e_{1}, \langle e_{2}, e_{3}\rangle)$ to $(c\ell, \mu n, \{\ell, n\}^{\perp})$ with $c, \mu > 0$ ($c = 1$ unless $\ell$ is a positive multiple of $\ell_{0}$), carrying an orthonormal basis of $\Pi_{0}$ to one of $\{\ell, n\}^{\perp}$. The stabiliser of the data contains the boosts of the $(\ell, n)$ plane, which rescale $\ell$ by every positive factor (the normalisation of the boost flow, through which the acceleration $a$ labels it) and fix $\Pi$ pointwise, and the rotations of $\Pi$; both preserve the area element of $\Pi$. All tangent spaces are isometric: in Gauge Theory Gravity the physical vectors at every point are the vectors of one Clifford algebra with its fixed flat product. Hence under (Loc) the density is one constant $\eta$, independent of the point, the null direction, the edge plane, the frame and the acceleration.
\item[(ii)] \emph{(The number, with no count.)} Assume (P) and (R) and Hawking's thermodynamic hypothesis as in Theorem \claimref{synthesis.quarter-from-temperature} (internal energy $M$, $dS = dM/T$ along the Schwarzschild family, $S \to 0$ as $M \to 0$), so that $S(M) = A/4$; and assume that this thermodynamic entropy is the integral of the density of (Loc) over the horizon cross-section up to $o(A)$ as $M \to \infty$ (the hole's entropy and the horizon density describe one set of degrees of freedom, not two). Then $\eta = \lim_{M\to\infty}S/A = \tfrac14$. The value depends on the temperature normalisation and on Hawking's hypothesis: with a period $p$ of imaginary Killing time in place of the regular $2\pi/\kappa$, the same steps give $\eta = p\kappa/8\pi$. The entropies the store holds for the de Sitter horizon, $S_{\Lambda} = \pi N^{2}$ for area $4\pi N^{2}$ (Theorem \claimref{synthesis.de-sitter-entropy-pi-n-squared}), and for the Kerr horizon, $A_{+}/4$ (Fact \claimref{synthesis.imported-kerr-surface-gravity-entropy}), give the same $\eta$ under the same identification. No count and no $\nu$ enter. The count form $\eta = 4\pi\nu\langle s\rangle$ of clause (i) of Premise \claimref{synthesis.c-loc-local-horizon-premise} then holds if and only if $16\pi\nu\langle s\rangle = 1$, the area-law condition of Theorem \claimref{synthesis.clausius-route-newton-constant-is-residue}(iii).
\item[(iii)] \emph{(What clause (i) adds.)} Under the hypotheses of (ii) and at leading order, the entropy content of clause (i) of Premise \claimref{synthesis.c-loc-local-horizon-premise}, an entropy $\eta\,\delta A$ with $\eta$ one universal constant (hypothesis (b) of Fact \claimref{synthesis.imported-jacobson-clausius-1995}), is equivalent to (Loc), with $\eta = \tfrac14$. Its mode-count content, boundary modes at the epoch density, is not implied by (Loc).
\item[(iv)] \emph{(Constancy from Clausius alone.)} Independently of (Loc): if the entropy of a local Rindler horizon patch is $\int\eta\,dA$ for a $C^{1}$ function $\eta$ on the invertible region, the Clausius relation of Fact \claimref{synthesis.imported-jacobson-clausius-1995}(c) at first order in the patch forces $k \cdot D\eta = 0$ ($k^{a}\nabla_{a}\eta = 0$) for every physical null $k$ at every point, hence $\eta$ constant on a connected region: the heat $\delta Q$ and the area change are of second order in the affine extent $\lambda_{0}$ of the patch (vanishing expansion at $p$), while a gradient of $\eta$ along the generators changes the entropy at first order, by $-\lambda_{0}\,k^{a}\nabla_{a}\eta$ per unit area.
\end{enumerate}

## technical
Clause (i) of the local-horizon premise gives every small horizon an entropy $\eta$ per unit area, with $\eta$ one universal constant, realised by the series' boundary modes at their epoch density. This result separates what in that clause is assumed from what follows. If the entropy density of a small horizon patch depends only on the flat tangent data of the patch, a null ray and an edge plane, and in particular not on the curvature (the field strength of the gravitational field), the matter or the boost normalisation at the point, the density must be one constant: Lorentz transformations carry any null ray with its edge plane to any other, and the boosts that change the observers' acceleration leave the edge plane and its area untouched. So universality and area proportionality are automatic once the entropy is assumed local and independent of the curvature and matter at the point. This assumption excludes the curvature-dependent entropies of higher-curvature theories, whose densities depend on the field strength, which are what would otherwise separate Einstein's equations from their extensions; on this route Einstein's equations are selected by it, not by locality. The one number is fixed by the Schwarzschild family: under the series' univalence and regularity premises, Hawking's thermodynamic hypothesis, and the identification of the hole's entropy with the integral of the density, the density is $\tfrac14$, without any count of modes and without $\nu$; it would be $p\kappa/8\pi$ for another period $p$, and the de Sitter and Kerr entropies agree. The boundary-mode form of the density, $4\pi\nu\langle s\rangle$, equals $\tfrac14$ exactly at the area-law condition that defines the registered $\nu$. Because the calibration uses the Schwarzschild solution and the $G$ that defines the Planck cell, Jacobson's argument would then return that same $G$: a consistency, not a determination of Newton's constant. Separately, if the entropy is the integral of a density that varies from point to point, the Clausius relation already forces that density to be constant, at first order in the size of the patch.

## lay
The local-horizon assumption gives every small horizon an entropy proportional to its area, with the same constant everywhere. This result shows that "the same constant everywhere" is automatic once one assumes that the entropy per area of a small piece of horizon depends only on how the piece sits among the flat directions at its point, and not on how strong the gravitational field is there or what matter is present. That second part is a real assumption: theories of gravity with extra curvature terms give entropies that do depend on the strength of the gravitational field, and this assumption is what rules them out. Given it, a change of viewpoint or of the observer's acceleration turns any small horizon into any other without changing its area, so the entropy per area can only be one number. That number is then fixed by black holes: if a black hole's entropy is the sum of this density over its horizon, and under the series' assumptions about its temperature and Hawking's thermodynamic reasoning, the constant is one quarter, with no need to count modes. The series' mode count gives the same quarter only at the value of its calibration constant that was chosen to match black-hole entropy, as already known.

## one-liner
If the entropy density of a small horizon patch depends only on its flat tangent data (null ray and edge plane of physical vectors), not on the curvature (field strength), matter or boost normalisation at the point (an assumption that excludes Wald-type higher-curvature entropies), the Lorentz group forces one universal constant $\eta$; under (P), (R), Hawking's hypothesis and the identification of the Schwarzschild hole's entropy with the integral of that density, $\eta = \tfrac14$ with no count and no $\nu$ ($p\kappa/8\pi$ for another period $p$; de Sitter and Kerr agree), so the entropy content of clause (i) of (C$_{\mathrm{loc}}$) is equivalent to that condition and $\eta = 4\pi\nu\langle s\rangle$ is the area-law condition; and under $S = \int\eta\,dA$ the Clausius relation alone forces $\eta$ constant at first order.
