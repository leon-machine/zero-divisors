---
id: synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet
kind: claim
version: 2
title: 'Late-time Hawking state from the ground state on the ingoing sheet'
status: proved
region: synthesis
subject: thermality
tags: [horizons, thermal-premises, hawking-temperature, car-algebra, modular-theory, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-10-24-all-open
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
- name: Claude Opus 5.5
  role: lemmas (iii) and (iv) split out into synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation, which the proof now cites
  version: 2
  source: maintainer pass 2026-11-07
review: draft
outside_ga:
  kind: complex-analysis
  why: 'the generator kernels (i/2 pi)(u - u'' + i0)^{-1} and their thermal and log forms, the Fourier and Laplace transforms on L^2 of a null line and the regularised Synge function sigma + i epsilon(...) are boundary values and contour arguments of scalar kernels; the prefactor and the boundary value carry one complex unit, so writing the prefactor alone as I_4 would split it, and the i0 of a time function or of a spacetime vector cannot be a pseudoscalar; the Mellin powers |u|^{-1/2 + iw} of the proof belong to the same analysis'
about:
- obj.hawking.continuum-mode-space
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation@1
  - synthesis.positive-null-energy-gives-r-premises@6
  - hawking.i-state-continuum@5
  - hawking.imported-quasi-free-kms-reduces-two@2
  - sheaf.gauge-field-cometric@3
  - synthesis.imported-gtg-dictionary@1
  - singularity.euclidean-section-period@5
  - synthesis.r-loc-needs-sheet-labelled-modes@3
  assumes:
  - hawking.joint-j3-s-wave-reduction@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_regular_reparametrisation_keeps_the_ground_state_singularity
- kind: check
  ref: check.py::check_scaling_limit_is_the_ground_state
- kind: check
  ref: check.py::check_kruskal_functions_in_the_painleve_gullstrand_gauge
- kind: check
  ref: check.py::check_ingoing_generator_crosses_the_horizon_regularly
- kind: check
  ref: check.py::check_exterior_half_is_the_i_state_at_the_hawking_temperature
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.n-plus-null-ground-state
  - singularity.r-regularity-fixed-locus
  - angle.imported-theorems-deliver-their-hypotheses
  - hawking.greybody-inheritance-under-interface-premise
extraction:
  maintainer_pass_clause_split:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 1 -> 2, at Leon''s decision of 7 November 2026: the lemmas (iii) (the null-vacuum singularity is the same in every regular parameter) and (iv) (a bounded remainder scales away under the weight-1/2 dilation), which use no premise, are now the separate result synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation, its (i) and (ii), and the proofs of (iii) and (iv) cite it (here the Killing flow beta_tau is that dilation with epsilon = e^{-kappa tau}; the Boulware example stays here). Statement unchanged; assumes edge to J3 kept; the pin to synthesis.positive-null-energy-gives-r-premises moves from 4 to 6 (statement unchanged there). The checks of (iii) and (iv) are kept and also record the new premise. Notation as the sweep left it.'
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'No unit replaced: the i of the kernels 1/(U - U'' + i0), their powers and the Mellin powers is complex analysis on L^2 of a generator, kept whole. Declared complex-analysis; the wholesale alternative is listed for Leon.'
  open_problem: op.collapsing-hole-state
  flags:
  - 'beyond one flat chart: the collapsing matter is a different gravitational field on the same background, with the Painleve-Gullstrand field outside it (Birkhoff, literature); the late-time statements are made in the Painleve-Gullstrand chart, which covers both sides of the future horizon'
  note: >-
    States the condition the open problem asks for and derives the flux from it on the continuum carrier.
    The condition is the one premise (N+) already in the store, posed on the other sheet: not on the future
    horizon's own generators (which have no past half for a collapse hole) but on the ingoing null generator
    through each point of the horizon, which has an exterior and an interior half, and in its short-distance
    (scaling-limit) form, which the late-time limit of the Killing flow realises exactly because that flow
    dilates the Kruskal parameter at rate kappa. Two lemmas make the condition a sufficient one with a parametrisation-free statement: the
    class of states whose generator kernel is the ground-state singularity plus a remainder bounded near the
    point is the same in every regular parameter (the difference of the weight-1/2 ground-state kernels is a
    Schwarzian times the separation; a weight-h kernel has a continuous Schwarzian remainder for every h at
    most 1), and the scaling limit of every state in the class is the ground state; the same limit is reached
    by every finite-rank change of the symbol, so the class is sufficient, not necessary. The analytic core is the standard one (Hawking 1975;
    Fredenhagen and Haag 1990, who derive the flux from the short-distance behaviour at the horizon;
    the propagation of short-distance regularity from the collapse region, Fulling, Sweeny and Wald 1978;
    all cited from memory and not imported): transport-absent there. New to the store: the form on the
    series' CAR carrier, the identification of the collapse condition as (N+) on the ingoing sheet in its
    local form, the exact Painleve-Gullstrand form of the Kruskal functions with the dilation and the
    sign change across the horizon, and the reading of Hartle-Hawking, Unruh and Boulware as ground-state
    conditions on two sheets, one sheet, and the Killing flow of one half. The identification of the
    outgoing sector near the horizon with one chiral CAR field per light ray, a function of U on the ingoing
    generator, is the stored s-wave reduction premise (J3), used as a hypothesis and named in the title; the
    passage of the near-horizon state to infinity needs Premise (I) and the stored greybody inheritance, which
    are cited and not redone, so the result is stated for the near-horizon outgoing modes. A companion proposal filed alongside
    (synthesis.collapse-in-vacuum-regular-at-future-horizon-selects-hawking-temperature) supplies what this
    statement leaves as hypothesis: that the in-vacuum of a null-shell collapse is in the short-distance class,
    with the flux computed exactly, and that among late-stationary states only the temperature kappa/2pi is
    regular across the future horizon; the two may be merged at the orchestrator's choice. Lemma (iv) is the
    non-stationary form of the dilation-fixed-point lemma that the proposal
    synthesis.stationary-horizon-state-is-its-own-edge-scaling-limit (filed alongside) states within the stationary
    class at the bifurcation edge of a Killing horizon (a stationary state is its own scaling limit there; a
    remainder bounded near the edge suffices); here the dilation's fixed point is the future horizon itself,
    on the Painleve-Gullstrand chart, and the state is not assumed stationary, only its late-time limit is
    taken. Cross-check from the literature, cited from memory and flagged: the late-time flux kappa^2/(48 pi)
    per complex chiral fermion that the I-state at 2 pi/kappa carries is the two-dimensional anomaly flux of
    Robinson and Wilczek (2005), which a result filed alongside on the residue-0 chirality anomaly
    reaches from the other side.
---
## formal
Work on flat spacetime with the vectors of $\Cl(1,3)$, gravity the pair of gauge fields $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and take the Schwarzschild field of mass $M$ in the Painlev\'e-Gullstrand gauge of Fact \claimref{sheaf.gauge-field-cometric}, $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, invertible on $r > 0$, with $t$ the background time label of that gauge (derived line element $dt^{2} - (dr + \beta\,dt)^{2} - r^{2}d\Omega^{2}$, a reading). The background translation $t \mapsto t + \tau$ is a symmetry of the gravitational field, with physical Killing vector $K = \hb^{-1}(e_{t})$ (Fact \claimref{synthesis.imported-gtg-dictionary}(vi)); the future horizon $\mathcal{H}^{+} = \{r = 2M\}$ is its Killing horizon, with surface gravity $\kappa = 1/(4M)$ (Theorem \claimref{singularity.euclidean-section-period}). Write $s = \sqrt{r/2M}$ and $\rho = s^{2}$.
\begin{enumerate}
\item[(i)] \emph{(The Kruskal functions in this gauge.)} On $r > 0$ put
\[
U \;=\; -\,e^{-\kappa t}\,(s - 1)\,e^{s^{2}/2 + s}, \qquad V \;=\; e^{\kappa t}\,(s + 1)\,e^{s^{2}/2 - s}.
\]
Both are smooth on the invertible region; $UV = -(\rho - 1)e^{\rho}$; $U = 0$ exactly on $\mathcal{H}^{+}$, $U < 0$ outside and $U > 0$ inside, with $\partial_{s}U = -s^{2}e^{s^{2}/2 + s}e^{-\kappa t} \ne 0$; $V > 0$ everywhere. With $u = t - \int dr/(1 - \beta)$ and $v = t + \int dr/(1 + \beta)$ the retarded and advanced Eddington-Finkelstein labels of the derived metric, $U = -e^{-\kappa u}$ and $V = e^{\kappa v}$, because $\kappa\int dr/(1 \mp \beta) = s^{2}/2 \pm s + \ln|s \mp 1|$. The symmetry acts as $U \mapsto e^{-\kappa\tau}U$, $V \mapsto e^{\kappa\tau}V$: dilations of the two Kruskal functions at rate $\kappa$, of opposite sense.
\item[(ii)] \emph{(The ingoing sheet.)} The level sets of $V$ are null hypersurfaces whose generators, the radial ingoing free-fall null worldlines $v = \mathrm{const}$, cross $\mathcal{H}^{+}$ with $r$ an affine parameter ($\Gamma^{r}{}_{rr} = 0$ in the chart $(v, r)$ of the derived metric, Fact \claimref{synthesis.imported-gtg-dictionary}(iii)) and $U$ a regular parameter on them: along $v = \mathrm{const}$, $U = -e^{-\kappa v}(\rho - 1)e^{\rho}$ and $dU/d\rho = -e^{-\kappa v}\rho\,e^{\rho} \ne 0$, equal to $-e^{1 - \kappa v}$ on the horizon. The level sets of $U$ are the null hypersurfaces generated by the outgoing radial free-fall null worldlines, so under the s-wave reduction premise (J3), Premise \claimref{hawking.joint-j3-s-wave-reduction}, which reduces each channel of a massless field to a two-dimensional boundary mode, the outgoing sector near $\mathcal{H}^{+}$ is one chiral field per light ray constant along them, a function of $U$ and the transverse labels, and its carrier on the ingoing generator through a point $p$ of $\mathcal{H}^{+}$ is the continuum mode space $\CAR(L^{2}(\R, dU)\otimes K)$ of Definition \claimref{obj.hawking.continuum-mode-space}, the sheet of $p$ generated by the ingoing null direction in the sense of Proposition \claimref{synthesis.r-loc-needs-sheet-labelled-modes}. The symmetry acts on it as the boost $\beta_{\tau}(\psi(U)) = e^{-\kappa\tau/2}\,\psi(e^{-\kappa\tau}U)$, future-directed on the exterior half $U < 0$ and the reverse on the interior half $U > 0$. The generator has both halves at the crossing for every hole, collapse included; its interior half ends at $r = 0$, where $U = e^{-\kappa v}$, so the affine parameter runs over a half-line, the exact translation group of (N$_{+}$) does not act on it, and only the local form below can be posed.
\item[(iii)] \emph{(Lemma: the ground-state singularity is the same in every regular parameter.)} (Theorem \claimref{synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation}(i).) For the weight-$\tfrac12$ fields of the carrier and a $C^{3}$ reparametrisation $\xi$ of the generator with $\xi' > 0$, the ground-state kernels of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(i) in the two parameters differ by a kernel continuous across the diagonal and vanishing on it:
\[
\frac{\xi'(U)^{1/2}\,\xi'(U')^{1/2}}{\xi(U) - \xi(U') + i0} \;-\; \frac{1}{U - U' + i0} \;=\; \frac{S_{\xi}(U)}{12}\,(U - U') + O\bigl((U - U')^{2}\bigr), \qquad S_{\xi} = \frac{\xi'''}{\xi'} - \frac32\Bigl(\frac{\xi''}{\xi'}\Bigr)^{2},
\]
the squared ratio of the two kernels being $1 + \tfrac16 S_{\xi}(U)(U - U')^{2} + O((U - U')^{3})$. The kernel $1/(U - U' + i0)$ is covariant in this way only with the weight $\tfrac12$ (with weight $0$ or $1$ attached to it the difference is singular on the diagonal unless $\xi' \equiv 1$); a weight-$h$ field with its own kernel $(U - U' + i0)^{-2h}$ has the continuous remainder $\tfrac{h}{6}S_{\xi}(U)(U - U')^{2 - 2h} + \dots$ for every $h \le 1$, equal to $S_{\xi}/6$ on the diagonal at $h = 1$. Where $\xi'$ vanishes the ratio vanishes. Hence the class of gauge-invariant quasi-free states on the carrier whose two-point kernel is the ground-state kernel plus a remainder bounded near a point of the generator is the same in $U$, in $r$ and in the affine parameter.
\item[(iv)] \emph{(Lemma: the late-time limit is the scaling limit, and it is the ground state.)} (Theorem \claimref{synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation}(ii), with $\varepsilon = e^{-\kappa\tau}$.) Let $\omega$ be a gauge-invariant quasi-free state on $\CAR(L^{2}(\R, dU)\otimes K)$ whose two-point kernel is $W_{0}(U, U') + R(U, U')$, with $W_{0}(U,U') = \tfrac{i}{2\pi}\tfrac{1}{U - U' + i0}\otimes\id_{K}$ the kernel of the ground state $\omega_{0}$ for the $U$-translations and $R$ bounded on a neighbourhood of $(0, 0)$. Then for all $f, g \in L^{1}\cap L^{2}$, $\lim_{\tau\to\infty}\omega(\beta_{\tau}(\psi^{*}(f)\psi(g))) = \omega_{0}(\psi^{*}(f)\psi(g))$, and by quasi-freeness (Fact \claimref{hawking.imported-quasi-free-kms-reduces-two}) $\omega\circ\beta_{\tau} \to \omega_{0}$ on the whole carrier: under the weight-$\tfrac12$ dilation by $\varepsilon = e^{-\kappa\tau}$ the singular part is invariant and the remainder's contribution is $\varepsilon\iint \bar f(x')g(x)R(\varepsilon x, \varepsilon x')\,dx\,dx' \to 0$. The condition is sufficient, not necessary: the proof uses only $\varepsilon\iint\bar f g R(\varepsilon x, \varepsilon x') \to 0$, which holds for every bounded $R$ and also for every finite-rank change of the symbol (the dilated test functions tend weakly to zero), so states outside the class can have the same limit. A remainder homogeneous of degree $-1$, as the Boulware-type state (the ground state for the symmetry's own flow on the exterior half) has, is unbounded near the origin and survives the limit unchanged, so that state is not in the class and its limit is not $\omega_{0}$.
\item[(v)] \emph{(The condition and the flux.)} Let the hole be formed by collapse, with the Painlev\'e-Gullstrand field outside the matter, so that at late times the ingoing generator through a point $p$ of $\mathcal{H}^{+}$ lies in that field on both sides of the horizon. Condition (N$_{+}^{\mathrm{coll}}$): the state of the outgoing modes on the ingoing sheet through $p$ is in the class of (iii), that is, its kernel along the generator is the ground-state singularity in a regular parameter plus a remainder bounded near $p$ (short-distance regularity across $\mathcal{H}^{+}$; equivalently, by (iv), its scaling limit at $p$ is the ground state for the ingoing null translations: the premise (N$_{+}$) of Theorem \claimref{synthesis.positive-null-energy-gives-r-premises} posed on this sheet in its local form). Under (N$_{+}^{\mathrm{coll}}$) the late-time state of the exterior outgoing modes under the symmetry is the restriction of $\omega_{0}$ to $\CAR(L^{2}(\R_{-}, dU)\otimes K)$, which by Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(ii), a statement of CAR algebra on $L^{2}(\R, du)$ that applies to any generator carrying the translations and the weight-$\tfrac12$ dilation, applied to the half on which the boost $\beta_{\tau}$ is future-directed, is the continuum I-state of Theorem \claimref{hawking.i-state-continuum} at $\beta = 2\pi/\kappa = 8\pi M$ for the symmetry's flow: jointly KMS, even, the unique KMS state there, Fermi-Dirac with occupation $(1 + e^{2\pi\varpi/\kappa})^{-1}$ in Killing frequency $\varpi$. This is the late-time state of the near-horizon outgoing modes of the collapse hole at temperature $\kappa/2\pi = 1/(8\pi M)$ on the series' continuum carrier; it is Hawking's flux at infinity under Premise (I), Premise \claimref{hawking.premise-i-interface-identification}, which carries each near-horizon channel's occupancy to the asymptotic channel, with the stored greybody inheritance, neither redone here. The interior half carries the partner modes, KMS at the same $\beta$ for the reversed flow, and $\omega_{0}$ on the whole generator is pure. No past half of $\mathcal{H}^{+}$ enters. Not claimed here, and proved in a companion result filed alongside: that the in-vacuum of a null-shell collapse is in the class, with the flux computed exactly at all times, and that among late-stationary states only the temperature $\kappa/2\pi$ is regular across $\mathcal{H}^{+}$.
\item[(vi)] \emph{(Reading.)} The eternal hole's condition in (N$_{+}$) is a ground state on both sheets at the bifurcation surface, the whole generators of $\mathcal{H}^{+}$ and of the past horizon (Hartle-Hawking type). (N$_{+}^{\mathrm{coll}}$) is a ground state on the ingoing sheet alone, in the scaling limit at $\mathcal{H}^{+}$, the ingoing sector being left to the data of the collapse's past (Unruh type). The ground state for the symmetry's flow on the exterior half alone (Boulware type) is outside the class by (iv). (N$_{+}^{\mathrm{coll}}$) is a sufficient condition of ground-state type: by (iii) and (iv) it holds for every state whose generator kernel is the ground-state singularity plus a bounded remainder, the one-dimensional form of a short-distance (Hadamard-type) condition, and the same late-time state is reached by every finite-rank change of the symbol; which a state regular across $\mathcal{H}^{+}$ has; that the state built from regular data before the collapse stays regular at $\mathcal{H}^{+}$ is the literature's propagation result (argued here; cited from memory, not imported), shown exactly for the collapse of a null shell in a companion result filed alongside.
\end{enumerate}
\emph{Beyond one flat chart.} The Painlev\'e-Gullstrand chart covers both sides of $\mathcal{H}^{+}$, so (i) to (v) are statements on one flat chart with one gravitational field; the collapsing matter is a different gravitational field on the same background, joined to the Painlev\'e-Gullstrand field at the matter's surface (Birkhoff, literature), and only the late-time region outside the matter is used.

## technical
The stored premise (N$_{+}$) asks for a ground state for the affine null translations along a horizon's generators, and the stored restriction theorem turns it into the Hawking temperature by cutting the generator at the bifurcation surface. For a hole formed by collapse the future horizon's generators have no past half, and the open problem asked for an Unruh-type condition in its place. The answer is that the same premise is to be posed on the other sheet. Through every point of the future horizon runs the ingoing null generator, which crosses the horizon from the exterior to the interior and so has two halves for every hole. The outgoing modes, the ones that reach infinity, are the field's data along that generator, parametrised by the Kruskal function $U$, and the hole's symmetry dilates $U$ at the surface-gravity rate. In the Painlev\'e-Gullstrand gauge of the store, which covers both sides of the horizon, $U = -e^{-\kappa t}(s - 1)e^{s^{2}/2 + s}$ with $s = \sqrt{r/2M}$, an exact smooth function changing sign on the horizon.

Two lemmas carry the argument. First, for the series' weight-one-half fields the ground-state kernel is the same in every regular parameter up to a continuous remainder vanishing on the diagonal (a Schwarzian times the separation); so the class of short-distance-regular states, kernel plus a bounded remainder, is parametrisation-free. Second, since late Killing time is a dilation of $U$ towards zero, the late-time state of the outgoing modes is exactly the scaling limit of the state at the horizon, and for every state in the class that limit is the ground state. Restricted to the exterior half it is the continuum I-state at $\beta = 2\pi/\kappa$, by the stored theorem: the Hawking flux. The condition is therefore (N$_{+}$) on the ingoing sheet in its local form; it is implied by short-distance regularity across the horizon, and it is sufficient rather than necessary, since finite-rank changes of the symbol reach the same limit. The Boulware-type state, whose remainder is homogeneous of degree $-1$, is outside it. The outgoing sector is taken as one chiral field per light ray (the s-wave reduction premise), and the state is that of the near-horizon modes; carrying it to infinity is the interface premise and the greybody inheritance. Hartle-Hawking, Unruh and Boulware read as ground-state conditions on two sheets, one sheet, and the Killing flow of one half. The analytic core is standard (Fredenhagen and Haag); the store gains the condition in its own terms, the sheet reading, and the exact gauge form of the Kruskal functions.

## lay
A black hole that forms from a collapsing star has no past horizon, so the series' rule for the temperature of an eternal black hole, which looks at both sides of a horizon's light rays, cannot be applied as it stands. This result finds the rule that does apply. Through every point of the horizon there is a second family of light rays, the ones falling in; those cross the horizon from outside to inside and so always have two halves. The radiation that escapes to infinity is carried by the field's values along those infalling rays, measured in a coordinate that the hole's own time flow squeezes towards the horizon. Waiting a long time is the same as looking at ever shorter distances from the horizon, and at short distances any field that is not singular at the horizon looks like its own vacuum. Cutting that vacuum at the horizon, by a result already in the series, gives a thermal state at Hawking's temperature. So the condition for a collapsing hole is the series' existing vacuum condition, applied to the infalling rays and only at short distances; it is enough for the thermal outcome, though not the only condition that gives it. One state that fails it is the one that would make the horizon a place of infinite energy. The result treats each light ray's field as a one-dimensional field, an assumption the series states separately.

## one-liner
For a collapse hole, with the outgoing sector reduced to one chiral CAR field per light ray (J3), the thermal condition is (N$_{+}$) posed on the ingoing sheet through each point of the future horizon, whose generator has both halves, in its local (scaling-limit) form; in the Painlev\'e-Gullstrand gauge $U = -e^{-\kappa t}(s-1)e^{s^{2}/2+s}$ is a regular parameter on that generator dilated at rate $\kappa$ by the symmetry, the late-time state of the near-horizon exterior outgoing modes is exactly the scaling limit and hence the continuum I-state at $\beta = 2\pi/\kappa$ (Hawking's flux at infinity under Premise (I)); the condition is sufficient, holding for every state whose generator kernel is the ground-state singularity plus a bounded remainder, a class the same in every regular parameter for the weight-$\tfrac12$ kernel (Schwarzian difference), and the Boulware-type state is outside it.
