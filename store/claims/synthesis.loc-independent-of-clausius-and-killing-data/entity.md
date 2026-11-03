---
id: synthesis.loc-independent-of-clausius-and-killing-data
kind: claim
version: 4
title: The curvature-independence clause (Loc) is independent of the Clausius relation, of (R$_{\mathrm{loc}}$) and of every $\Lambda$-vacuum horizon datum of the store; a density $\tfrac14(1 + c\,S_{ab}S^{ab})$ passes all of them and differs from $\tfrac14$ in the Einstein static universe, and on the integrated reading such failures are confined to spacetimes with no calibrated vacuum point
status: proved
region: synthesis
subject: einstein
tags: [horizons, curvature-and-field-equations, thermal-premises, counting-rules]
proposed_by:
  kind: ai
  session: 2026-10-23-toe
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
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - synthesis.c-loc-entropy-clause-curvature-independent-density@3
  - synthesis.black-hole-data-do-not-fix-field-equations@6
  - synthesis.sds-clausius-fixes-area-constant@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_vacuum_density_is_one_quarter
- kind: check
  ref: check.py::check_einstein_static_universe_model
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.c-loc-local-horizon-premise
  - synthesis.c-loc-entropy-clause-curvature-independent-density
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'The model is built on premise (C_loc) version 2 (differences reading); under version 3 (integrated reading) its conclusion is the confinement in clause (iv): failures of (Loc) only on spacetimes with no calibrated vacuum point. The independence statement for the differences reading is unchanged. Version 1 -> 2.'
  open_problem: op.derive-loc-and-r-loc
  note: >-
    Answers the (Loc) half of the open problem in its second form: a model of the other premises in which
    (Loc) fails. The model assigns local horizons the density one quarter times (1 + c S_ab S^ab), S the
    tracefree Ricci tensor, so it equals one quarter on every Lambda-vacuum metric and leaves every
    Lambda-vacuum horizon datum, every calibration and the temperature clause untouched; the Clausius relation
    holds on every local horizon of the Einstein static universe with a renormalised coupling, where the
    density is not one quarter. On the integrated reading the stored constancy result confines such
    failures to spacetimes with no point of calibrated vacuum curvature. That no postulate of the store
    fixes the entropy of non-Killing horizons or the coupling of matter in the field equations is a survey,
    stated as such. Transport-absent, and the store-specific exact form of a point known in substance:
    Jacobson's Clausius argument with a curvature-dependent density yields a different theory (Eling,
    Guedens and Jacobson 2006, f(R), cited from memory), so this is a modest result, an exact model, not a
    new mechanism. The first-order rate of the Euler entropy on any local patch is filed alongside,
    synthesis.euler-entropy-first-order-rate-on-local-patches; the cutoff count on Schwarzschild-de Sitter
    is filed alongside, synthesis.cutoff-count-is-not-a-local-density-on-sds; the temperature clause's
    independence is filed alongside, synthesis.r-loc-independent-sets-matter-coupling. Literature cited from memory in the proof: the Einstein static
    universe and its stereographic form.
  flags:
  - 'beyond one flat chart: the closed spatial slices of the Einstein static universe'
  maintainer_pass_gtg:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the admissible pairs are (gravitational field on flat spacetime, matter), S_ab is the trace-free part of the Ricci map of the field strength, Lambda-vacua are fields with R(a) = Lambda a, and the curvature scalars are scalars of the field strength. Flagged beyond one flat chart: the Einstein static universe of (ii) has closed spatial slices; its local content (S_ab S^ab = 3/a^4, the dust, the Clausius balance at every point) is that of a gravitational field on flat spacetime on any chart omitting one point of each slice. Signature (-,+,+,+) kept as declared. Model, clauses (i) to (iv) and their strength unchanged; proof given a pointer to the dictionary Fact.'
---

## formal
Units $\hbar = c = G = 1$, signature $(-,+,+,+)$, $\mathrm{Ric}$ positive on spheres (the $\Ric^{\circ}$ of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}), $S_{ab} = R_{ab} - \tfrac14 R\,g_{ab}$ the tracefree Ricci tensor, for a gravitational field $(\hb, \Omega)$ on flat spacetime the trace-free part of the Ricci map of its field strength, read in components with the derived metric $g$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). Fix a constant $c \neq 0$ and let $\mathcal{M}_{c}$ be the following assignment: every local Rindler horizon patch through $p$ changes its entropy as $\delta S = \eta(p)\,\delta A$ with
\[
\eta(p) \;=\; \tfrac14\bigl(1 + c\,S_{ab}S^{ab}(p)\bigr),
\]
the patch's boundary modes are in the state that (R$_{\mathrm{loc}}$) of Premise \claimref{synthesis.c-loc-local-horizon-premise} prescribes, and the admissible pairs (gravitational field, matter) are those satisfying hypotheses (H1) to (H4) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} with this density. (H1) thus holds in $\mathcal{M}_{c}$ by construction; the content is that the admissible class contains the $\Lambda$-vacua unchanged and a spacetime on which $\eta \neq \tfrac14$. On the integrated reading the class is small ($S_{ab}S^{ab}$ must be constant on each admissible field; Reissner-Nordstr\"om with its Maxwell field, $S_{ab}S^{ab} = 4Q^{4}/r^{8}$, is not admissible). The entropy here is decoupled from any mode count, as in version 2 of the premise, which dropped the mode-count reading: (R$_{\mathrm{loc}}$) is imposed on the state, and $\mathcal{M}_{c}$ is not a model of version 1, where the entropy of a fixed mode set in the (R$_{\mathrm{loc}}$) state would fix $\eta$.
\begin{enumerate}
\item[(i)] \emph{(Vacuum data unchanged.)} On every field with $\mathrm{Ric} = \Lambda g$ (Ricci map $\Lambda$ times the identity), in particular the Schwarzschild, Kerr, Schwarzschild-de Sitter and de Sitter fields, $S_{ab} = 0$ and $\eta = \tfrac14$, and (H1) holds with $T = 0$. So every statement of the store about these geometries (horizon temperatures under (R) and (R$_{\Lambda}$), the Clausius integrals along the Schwarzschild and Schwarzschild-de Sitter families of Theorems \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(ii) and \claimref{synthesis.sds-clausius-fixes-area-constant}, the cutoff counts of Theorem \claimref{synthesis.black-hole-data-do-not-fix-field-equations}(iii) on Schwarzschild) holds in $\mathcal{M}_{c}$ exactly as in the store; whatever tension those statements already have among themselves is inherited, not created (the literal cutoff count on Schwarzschild-de Sitter, identified with the horizon modes, already disagrees with $A_{b}/4$: filed alongside, synthesis.cutoff-count-is-not-a-local-density-on-sds), and the calibration of Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(ii) returns $\tfrac14$.
\item[(ii)] \emph{(A spacetime where it fails.)} Let $a > 0$ and let $(g, T)$ be the Einstein static universe $-dt^{2} + a^{2}d\Omega_{3}^{2}$ with dust at rest of density $\rho$, $8\pi\rho = 2(1 + 3c/a^{4})/a^{2}$. Then $S_{ab}S^{ab} = 3/a^{4}$ everywhere, $\eta = \tfrac14(1 + 3c/a^{4}) \neq \tfrac14$, the dust is conserved, and for every point and every null $k$
\[
T(k,k) - \frac{\eta}{2\pi}\,\mathrm{Ric}(k,k) \;=\; 0 ,
\]
so the leading defect of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}(2) vanishes and (H1) holds on every local Rindler patch, on the differences reading and, since $\eta$ is constant on this spacetime, on the integrated reading. Its field equations are $G_{ab} + \Lambda_{J}g_{ab} = 8\pi G_{e}T_{ab}$ with $G_{e} = 1/(4\eta)$ and integration constant $\Lambda_{J} = 1/a^{2}$ (equal to a given $\Lambda$ for $a^{2} = 1/\Lambda$). Inside the Einstein static universe alone the density is constant; the density law of $\mathcal{M}_{c}$ depends on curvature: it is $\tfrac14$ on every $\Lambda$-vacuum and $\tfrac14(1 + 3c/a^{4})$ on the Einstein static universe, and (Loc), which forces one universal constant by Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(i), fails in $\mathcal{M}_{c}$.
\item[(iii)] \emph{(Independence.)} Hence (Loc) does not follow from (R$_{\mathrm{loc}}$), from (H1) to (H4) on either reading of (H1), or from the $\Lambda$-vacuum horizon data of the store.
\item[(iv)] \emph{(Where the integrated reading confines it.)} If the entropy of a patch is $\int\eta\,dA$ with $\eta$ a $C^{1}$ function on the invertible region that depends only on the curvature scalars at the point (scalars of the field strength), and (H1) holds, then by Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(iv) $\eta$ is constant on each connected spacetime (a gravitational field on a connected invertible region); if the spacetime contains one point whose curvature scalars are those of a point of a Schwarzschild, Schwarzschild-de Sitter or de Sitter horizon (for example any region of exact de Sitter, or a vacuum exterior close enough to a horizon), then $\eta = \tfrac14$ throughout it. So on the integrated reading (Loc) can fail only in spacetimes with no such point, of which (ii) is one.
\end{enumerate}
\emph{Beyond one flat chart.} The closed spatial slices of the Einstein static universe in (ii) are global and are not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region are in Gauge Theory Gravity (on any chart of the Einstein static universe that omits one point of each slice, the field strength, the dust and the Clausius balance at every point are as stated), and the closed spatial slices are read on the manifold assembled from the derived metric's charts.

## technical
The local-horizon premise has two clauses; this result concerns (Loc), which says the entropy per unit area of a small horizon patch does not depend on the curvature or the matter at the point. The open problem asks either for a derivation of (Loc) from the series' structure or for a model of the other premises in which it fails. Here is such a model. Give every local horizon the density one quarter times $(1 + c\,S_{ab}S^{ab})$, where $S_{ab}$ is the tracefree part of the Ricci tensor. In every vacuum with a cosmological constant this tracefree part vanishes, so every vacuum black-hole and de Sitter horizon the store treats keeps its temperature, its entropy $A/4$ and every calibration built on them; the temperature clause is untouched. In the Einstein static universe filled with dust the density is $\tfrac14(1 + 3c/a^{4})$, not one quarter, and Jacobson's Clausius balance still holds on every local horizon there, with a correspondingly renormalised Newton coupling and the usual cosmological constant $1/a^{2}$.

So nothing in the Clausius relation, in the temperature clause or in the $\Lambda$-vacuum horizon data forces (Loc). The Clausius relation holds in the model by construction of its admissible class; what is shown is that this class keeps every vacuum and contains a spacetime where the density is not one quarter. The model needs the entropy decoupled from a mode count, as in the premise's second version. This is the store's exact form of a point known in substance from Jacobson-type derivations with curvature-dependent entropy (Eling, Guedens and Jacobson), not a new mechanism. A survey of the store's postulates finds none that fixes the entropy of non-Killing horizons or the coupling of matter in the field equations, so the model differs from the store's intended reading only where no postulate speaks; that part is a survey, not a theorem. The curvature-independence clause is therefore a genuine premise: it fixes $\eta$, hence, together with the temperature clause (whose independence is filed alongside, synthesis.r-loc-independent-sets-matter-coupling), the matter coupling of gravity, the separation the stored black-hole-data result locates. On the integrated reading, where entropy is the integral of the density, the stored constancy result does more: the density is constant on each connected spacetime, hence one quarter on any spacetime containing a single point with the curvature of a calibrated horizon, so failures are confined to spacetimes like the static universe that contain none. The static universe's closed spatial slices are global and are not carried by the store's one-chart fields, so they are read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations. On the differences reading of the premise's second version even that confinement is absent. The first-order Euler-entropy rate on local patches, which excludes the Euler term on the integrated reading, is filed alongside, synthesis.euler-entropy-first-order-rate-on-local-patches.

## lay
To derive Einstein's equations from thermodynamics one assumes that every small piece of horizon carries the same entropy per unit area, whatever the gravitational field strength or matter there. Could that follow from the rest of the series? This result says no, by example. Imagine a world where the entropy per area is a quarter plus a small extra amount that grows with the matter-induced part of the gravitational field strength. Around black holes and in empty space with a cosmological constant that extra amount is zero, so every black-hole and cosmological-horizon fact the series relies on is unchanged. But in a universe uniformly filled with dust it is not zero, and the heat-balance argument still works there, just with a slightly different strength of gravity. So the equal-entropy-everywhere assumption is doing real work: it is what fixes how strongly matter sources the gravitational field, and the rest of the series does not supply it.

## one-liner
A local-horizon density $\tfrac14(1 + c\,S_{ab}S^{ab})$ equals $\tfrac14$ on every $\Lambda$-vacuum, so it keeps every $\Lambda$-vacuum horizon datum, (R$_{\mathrm{loc}}$) and the Clausius relation, yet is $\tfrac14(1 + 3c/a^{4})$ in the dust-filled Einstein static universe where Clausius still balances: (Loc) is independent of them; on the integrated reading such failures need a spacetime with no calibrated vacuum point.
