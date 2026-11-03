---
id: synthesis.integrated-loc-curvature-clause-forced-matter-clause-independent
kind: claim
version: 1
title: On the integrated reading of (Loc), the Clausius relation with the de Sitter calibration forces a continuous entropy density to 1/4 on every admissible field whose local data approach calibrated data; so a continuous density depending on curvature alone that keeps the flat Friedmann fields with $w \in [0,1]$ and $\Lambda \ge 0$ admissible is 1/4 at every curvature they pass through, the Einstein static universe's among them; a density that depends on matter as well escapes with every field satisfying Einstein's equations at the calibrated coupling admissible
status: proved
region: synthesis
subject: einstein
tags: [thermal-premises, horizons, curvature-and-field-equations, counting-rules]
proposed_by:
  kind: ai
  session: 2026-10-31-all-open
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
  - synthesis.c-loc-entropy-clause-curvature-independent-density@3
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - synthesis.loc-independent-of-clausius-and-killing-data@4
  - synthesis.imported-gtg-dictionary@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_friedmann_instant_curvature
- kind: check
  ref: check.py::check_friedmann_equations_and_affine_path
- kind: check
  ref: check.py::check_einstein_static_universe_is_a_friedmann_inflection_instant
- kind: check
  ref: check.py::check_flat_friedmann_reach
- kind: check
  ref: check.py::check_degree_zero_density_escapes_on_flat_dust
- kind: check
  ref: check.py::check_matter_dependent_density_counter_model
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.c-loc-local-horizon-premise
  - synthesis.euler-entropy-first-order-rate-on-local-patches
  - synthesis.de-sitter-entropy-pi-n-squared
extraction:
  open_problem: op.derive-loc-and-r-loc
  flags:
  - 'beyond one flat chart: the Einstein static universe of (iii) and (v) has closed spatial sections; the statements are local and are made on its stereographic chart, an open part of flat spacetime'
  note: >-
    Attack line 1 of the open problem (the confined gap on the integrated reading). The stored confinement says
    a curvature-dependent density that is constant on each field can fail only on fields with no calibrated
    vacuum point; the problem's statement narrowed this (argued) to fields whose arguments are constant
    everywhere. This result replaces both by a sharper pair. For a continuous density, constancy along a field
    plus calibration at the limit points of its local data gives 1/4 on every field whose data approach de Sitter
    or flat data, and the flat Friedmann fields carry every isotropic Weyl-free curvature with beta > 0 and
    -2 beta <= alpha < beta to such a limit; the Einstein static universe has exactly the curvature of the flat
    dust Friedmann-Lambda field at its inflection instant, so the stored counter-model survives only because its
    admissible class omits those Friedmann fields. The narrowing is false for discontinuous densities (a
    degree-zero ratio is constant along flat dust Friedmann while its arguments vary). The matter clause is
    independent in the strongest form: eta = 1/4 (1 + c Q), Q the square of the departure from Einstein's
    equations at the calibrated coupling, is 1/4 on every Einstein-with-G pair and 1/2 on an Einstein static
    universe where the Clausius relation holds. So what (Loc) adds on the integrated reading is curvature
    independence off the calibrated paths and one coupling for fields whose data stay away from calibrated data.
    Transport-absent: the content is Jacobson's argument read with a local density; GTG supplies the frame and
    the exact curvature computations. Literature cited from memory: the curvature of the flat Friedmann metric at a general instant
    (standard; checked exactly at tabulated instants). That the flat Friedmann fields with w in [0,1] and Lambda >= 0
    expand forever with rho decreasing to 0 is derived in the proof.
---
## formal
Units $\hbar = c = G = 1$. Store sign (Fact \claimref{synthesis.imported-gtg-dictionary}): signature $(+,-,-,-)$ on the physical vectors, $\mathcal{R}(B)$ the curvature of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), $\mathcal{R}(b)$ its Ricci map, $\mathcal{G}(b)$ its Einstein map, de Sitter $\mathcal{R}(B) = \tfrac{\Lambda}{3}B$, field equations $\mathcal{G}(b) + \Lambda b = -8\pi G_{e}\,T(b)$, a perfect fluid at rest $T(b) = (\rho + p)(b\cdot\gamma_{0})\gamma_{0} - p\,b$. Write $t = 2\pi T$ and ${}^{\circ}$ for the trace-free part of a symmetric map. The \emph{local data} at a point $p$ are $\mathcal{R}$ and $t$ at $p$, up to proper Lorentz transformations of the physical vectors; the density is taken independent of the patch's null direction and edge plane, as in Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(iv) (a function on the invertible region). On the integrated reading of Premise \claimref{synthesis.c-loc-local-horizon-premise} the entropy of a cut is $\int\eta\,dA$; here $\eta(p) = f(\text{local data at } p)$ for a function $f$ that is continuous and makes $\eta$ a $C^{1}$ function on each admissible field (a gravitational field with matter on a connected open part of its invertible region, derived metric $C^{3}$, satisfying hypotheses (H1) to (H4) of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius} with this density). \emph{Calibrated data}: de Sitter curvature $\tfrac{\Lambda}{3}B$, $\Lambda > 0$, with $t = 0$, where the store's de Sitter entropy gives $\eta = \tfrac14$ (Theorem \claimref{synthesis.c-loc-entropy-clause-curvature-independent-density}(ii)), and their limit $\Lambda \to 0$, the flat data.
\begin{enumerate}
\item[(i)] \emph{(Asymptotic calibration.)} If an admissible field contains points whose local data converge to calibrated data, then $\eta = \tfrac14$ throughout it and its field equations hold with $G_{e} = 1$.
\item[(ii)] \emph{(Friedmann instants.)} For the flat Friedmann field $\hb^{-1}(e_{0}) = e_{0}$, $\hb^{-1}(e_{i}) = a(t)\,e_{i}$, at an instant with $a = 1$, $\dot a = a_{1}$, $\ddot a = a_{2}$: $\mathcal{R}(\gamma_{i}\wedge\gamma_{j}) = a_{1}^{2}\,\gamma_{i}\wedge\gamma_{j}$, $\mathcal{R}(\gamma_{0}\wedge\gamma_{i}) = a_{2}\,\gamma_{0}\wedge\gamma_{i}$, and the Weyl part vanishes. With a perfect fluid at rest, $s = 8\pi G_{e}\rho > 0$, $p = w\rho$, and $\Lambda$, the field equations hold at the instant if and only if $a_{1}^{2} = (s + \Lambda)/3$ and $a_{2} = -s(1 + 3w)/6 + \Lambda/3$, so $\mathcal{R}$ is $\tfrac{\Lambda}{3}B$ plus $s$ times a fixed operator. For $w \in [0, 1]$ and $\Lambda \ge 0$ the expanding field has $\rho$ decreasing continuously to $0$ as $t \to \infty$, so its local data tend to calibrated data. Every isotropic Weyl-free curvature with space-plane value $\beta > 0$ and time-plane value $\alpha$, $-2\beta \le \alpha < \beta$, is the curvature at an instant of such a field (with $w \in [0,1]$, $\Lambda \in [0, 3\beta)$).
\item[(iii)] \emph{(The curvature clause.)} Hence, if $f$ depends on the curvature only and the admissible class contains the flat Friedmann fields of (ii), each with the coupling its Clausius relation fixes, then $f = \tfrac14$ at every isotropic Weyl-free curvature with $\beta > 0$ and $-2\beta \le \alpha \le \beta$. The Einstein static universe of radius $A$, with any perfect fluid, has the curvature $\beta = 1/A^{2}$, $\alpha = 0$ of the flat dust Friedmann field with $\Lambda = 1/A^{2}$ at its inflection instant ($8\pi G_{e}\rho = 2/A^{2}$, $\ddot a = 0$). So every continuous curvature-only density, the density $\tfrac14(1 + c\,S_{ab}S^{ab})$ of Theorem \claimref{synthesis.loc-independent-of-clausius-and-killing-data} among them, is $\tfrac14$ at the Einstein static universe's curvature once those Friedmann fields are admissible; that model escapes because its admissible class (fields on which $S_{ab}S^{ab}$ is constant) omits them.
\item[(iv)] \emph{(Not the constancy of the arguments.)} Along flat dust Friedmann with $\Lambda = 0$ the scalar curvature varies while $S_{ab}S^{ab} = \tfrac34\mathcal{R}^{2}$ at every instant, so the density $\tfrac14(1 + c\,S_{ab}S^{ab}/\mathcal{R}^{2})$ is the constant $\tfrac14(1 + \tfrac34 c)$ there and (H1) holds with $G_{e} = 1/(1 + \tfrac34 c)$, on a field whose arguments vary along every null direction. That density is not defined at Ricci-flat data, so it is not continuous at the calibrated flat data; for continuous densities the confinement takes the form (i).
\item[(v)] \emph{(The matter clause is independent.)} Let $X(b) = \mathcal{R}^{\circ}(b) + 4\,t^{\circ}(b)$, $Q = \sum_{m} X(\gamma_{m})\cdot X(\gamma^{m})$ and $\eta = \tfrac14(1 + cQ)$, a polynomial in the local data. On every pair satisfying the field equations with $G_{e} = 1$ and any $\Lambda$, $X = 0$ and $\eta = \tfrac14$, so every such pair is admissible. On the Einstein static universe of radius $2$ with $\Lambda = \tfrac14$ and dust $t(b) = \tfrac14(b\cdot\gamma_{0})\gamma_{0}$, with $c = \tfrac{16}{3}$: $Q = \tfrac{3}{16}$, $\eta = \tfrac12$, the field equations hold with $G_{e} = \tfrac12$, and the leading Clausius defect $t(k,k) + \eta\,k\cdot\mathcal{R}(k)$ vanishes for every null $k$, so (H1) holds on every patch. With Clausius, calibration, continuity and every field satisfying Einstein's equations at $G_{e} = 1$ admissible, the independence of $\eta$ from matter is not derived.
\item[(vi)] \emph{(What (Loc) adds.)} On the integrated reading, beyond the Clausius relation, the calibration and continuity, (Loc) adds (a) curvature independence at curvature values that no asymptotically calibrated admissible field passes through, and (b) one coupling for admissible fields whose local data stay away from calibrated data, of which the Einstein static universe is an example.
\end{enumerate}
Beyond one flat chart: the Einstein static universe's spatial sections are closed; every statement about it is local and is made on its stereographic chart.

## technical
The Clausius route derives Einstein's equations from (Loc), whose content is that the entropy per unit area of a small horizon patch is one constant. On the integrated reading the Clausius relation already forces the density to be constant along each gravitational field, and the store records that a curvature-dependent density can then fail only on fields with no calibrated vacuum point. This result sharpens that in both directions.

For a continuous density, a field whose local data come arbitrarily close to calibrated data has density $\tfrac14$, because the density is constant along it and tends to $\tfrac14$. Flat Friedmann universes with ordinary fluids and $\Lambda \ge 0$ are such fields: they dilute toward de Sitter or flat space. At each instant their curvature is isotropic and Weyl-free, and between them they pass through every such curvature with $\beta > 0$ and $-2\beta \le \alpha < \beta$. The Einstein static universe, the store's example of an escape, has exactly the curvature of the flat dust Friedmann universe with the same $\Lambda$ at the instant its expansion stops decelerating. So a density depending on curvature alone cannot single it out if the Friedmann universes are admissible. The stored counter-model survives only because its admissible class omits them. Conversely, the narrowing to fields whose arguments are constant is false without continuity: a degree-zero ratio of curvature scalars is constant along flat dust Friedmann although the scalars vary.

Matter is different. The square $Q$ of the departure from Einstein's equations at the calibrated coupling is a polynomial in curvature and stress. It vanishes on every solution at $G = 1$, so the density $\tfrac14(1 + cQ)$ leaves every standard solution admissible with density $\tfrac14$. Yet on an Einstein static universe the same density takes the value $\tfrac12$, with the Clausius relation satisfied and Newton's constant halved. What (Loc) adds on the integrated reading is curvature independence off the calibrated paths and one coupling for fields that never approach calibrated data.

## lay
To get Einstein's equations from heat flow across horizons, one assumes that every small piece of horizon carries the same entropy per unit area. Earlier work showed that the heat-flow law already forces this entropy to be the same throughout any one universe, but possibly different in different universes. This result asks when that loophole can actually be used. If the entropy depends smoothly on how strongly space is curved, the loophole closes for any universe that thins out toward empty space, and expanding universes of ordinary matter pass through every isotropic curvature on their way, including that of Einstein's static universe, the old example of an escape. If the entropy may also depend on the matter itself, the loophole stays open: an explicit rule gives the standard value in every ordinary universe and a different value, with a weaker gravity, in Einstein's static universe.

## one-liner
On the integrated reading, Clausius plus the de Sitter calibration forces a continuous horizon entropy density to 1/4 on every admissible field whose local data approach de Sitter or flat data; a continuous density depending on curvature alone that keeps the flat Friedmann fields with $w \in [0,1]$, $\Lambda \ge 0$ admissible is therefore 1/4 at every isotropic Weyl-free curvature with $\beta > 0$, $-2\beta \le \alpha < \beta$ they pass through, the Einstein static universe's included; a density depending on matter, $\tfrac14(1 + cQ)$ with $Q$ the square of the departure from Einstein's equations, keeps every Einstein solution admissible and is $\tfrac12$ on an Einstein static universe.
