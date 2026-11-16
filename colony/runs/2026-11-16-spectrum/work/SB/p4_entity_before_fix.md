---
id: synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta
kind: claim
version: 1
title: 'Sparse quasi-free deposits need super-Planckian quanta on a flat slice'
status: proved
region: synthesis
subject: dark-energy
tags: [no-go, confronted-with-data, car-algebra, needs-continuum]
proposed_by:
  kind: ai
  session: 2026-11-16-spectrum
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-16-spectrum
review: draft
derivations:
- name: main
  uses:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise@4
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb@5
  - synthesis.imported-planck-2018-lcdm-parameters@3
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pauli_count_and_energy_inequality
- kind: check
  ref: check.py::check_ceiling_of_the_shot_term_in_hubble_masses
- kind: check
  ref: check.py::check_thresholds_under_the_three_conversions
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise
  - synthesis.finite-range-descent-deposit-cannot-seed-cmb
extraction:
  open_problem: op.descent-state-and-spectrum
  note: >-
    Attack item 3 of the open problem: sparse or energetically broad quasi-free deposits, which the stored
    shot-noise bound leaves open because their number of quanta is not fixed by the record. What fixes it is the
    energy budget: the density at the descent is the record's, so few quanta means much energy in each. The
    stored shot term, the exclusion principle for the soft quanta and the recorded density together bound the
    shot term by the energy of the most energetic quantum in units of the Hubble mass. The conversion of the
    contrast into the curvature perturbation is not fixed by the stored statements, so the result is given under
    three named conversions, each a hypothesis here: a flat slice with the deposit at rest on it (the stored
    reading), a flat slice with the deposit's own momentum noise, and a slice of uniform expansion. Under the two
    flat-slice conversions the item closes for deposits whose quanta are quanta of a field on the collar
    (energies below the Planck mass, an argued criterion, not a stored premise); under uniform expansion the
    count closes nothing, and what bounds a deposit there is the shape of its spectrum against the observed band.
    Kill condition written before the computation: a sparse deposit that reaches the measured amplitude on the
    whole observed band with quanta below the Planck mass refutes the closing. None exists under the flat-slice
    conversions (clauses (iv), (v)); under uniform expansion thermal quanta already meet the necessary condition
    at the top of the window, so the closing is not claimed there. Transport-absent: the argument uses the
    variance bound of the CAR algebra, the exclusion principle and the Friedmann relation; the Clifford reading
    of the variance bound is the stored result's. The three conversions follow from the linearised constraint
    equations of the gauge fields and the radiation-era solutions (standard, from memory); they are hypotheses
    of this result and are to be pinned to a stored statement of the conversion when one exists. The energy
    spread at fixed number is covered by the same inequality, since only the largest energy enters. The deposits
    are gauge-invariant, as in the cited clause (iv); paired deposits fall under the cited general bound but not
    under that clause, and are not treated here.
---
## formal
\emph{Setting.} Units $\hbar = c = 1$. As in Proposition \claimref{synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise}(iv), let the deposit on the descent slice be a homogeneous gauge-invariant quasi-free state of fermion modes with one-particle energies $\omega_{p} \ge |p|$, let $x_{p} = \Tr X_{p}$ be its density of quanta at momentum $p$ above the descended vacuum ($X_{E} = (E - E_{0})^{2} + E(1 - E) = \bigoplus_{p}X_{p}$, the trace over the $g$ internal states at each momentum), and let $\rho_{F} = \int\omega_{p}x_{p}\,d^{3}p/(2\pi)^{3} = f\rho$ be the energy density it carries, a share $f \le 1$ of the total density $\rho$ at the descent. All quantities are physical ones at the descent: $\kappa = k/a_{d}$ is the physical wavenumber of the comoving mode $k$, $X = H_{d}/\kappa = a_{d}H_{d}/k$, the descended field is the spatially flat radiation-dominated one with $H_{d}^{2} = \tfrac{8\pi G}{3}\rho$, and $M_{H} = \tfrac{4\pi}{3}\rho H_{d}^{-3} = 1/(2GH_{d})$ is the Hubble mass. Write $\omega_{\max}$ for the supremum of $\omega_{p}$ over the support of $x_{p}$, and
\[
s(\kappa) = \frac{3\kappa^{3}}{2\pi^{2}\rho^{2}}\int(\omega_{p} + \kappa)^{2}x_{p}\,\frac{d^{3}p}{(2\pi)^{3}}
\]
for the shot term of the cited clause, for the deposit's contribution $\delta$ to the contrast of the total density: $\Delta_{\delta}^{2}(k)^{1/2} \le \Delta_{\delta,\mathrm{vac}}^{2}(k)^{1/2} + s(\kappa)^{1/2}$.
\begin{enumerate}
\item[(i)] \emph{(The exclusion principle counts the soft quanta.)} $0 \le X_{p} \le 1$, so $x_{p} \le g$; the quanta with $\omega_{p} < \kappa$ number at most $g\kappa^{3}/6\pi^{2}$ per unit volume; and
\[
\int(\omega_{p} + \kappa)^{2}x_{p}\,\frac{d^{3}p}{(2\pi)^{3}} \;\le\; (\omega_{\max} + \kappa)\Bigl(2\rho_{F} + \frac{g\kappa^{4}}{6\pi^{2}}\Bigr).
\]
\item[(ii)] \emph{(The shot term in Hubble masses.)} With $\eta = g\kappa^{4}/(6\pi^{2}\rho) = 4gGH_{d}^{2}/(9\pi X^{4})$,
\[
s(\kappa) \;\le\; \frac{2(2f + \eta)}{\pi}\,\frac{1}{X^{3}}\,\frac{\omega_{\max} + \kappa}{M_{H}}.
\]
\item[(iii)] \emph{(Momentum noise.)} Let $u$ be the longitudinal part of the deposit's momentum density divided by $\rho + p = \tfrac43\rho$. Its shot term obeys the same bound as the energy's: $\Delta_{u}^{2}(k)^{1/2} \le \Delta_{u,\mathrm{vac}}^{2}(k)^{1/2} + \tfrac34 s(\kappa)^{1/2}$.
\item[(iv)] \emph{(What an amplitude needs.)} Let the conserved curvature perturbation outside the Hubble length be $\mathcal{R} = \alpha\,\delta + \beta\,u$ with coefficients depending on $X$ alone. Then $\Delta_{\mathcal{R}}^{2}(k)^{1/2} \le |\alpha|\,\Delta_{\delta,\mathrm{vac}}^{2}(k)^{1/2} + |\beta|\,\Delta_{u,\mathrm{vac}}^{2}(k)^{1/2} + D(k)$ with $D = (|\alpha| + \tfrac34|\beta|)\,s^{1/2}$ the part the deposit's quanta can carry. Three conversions, each a hypothesis: (C0) flat slice, deposit at rest on it, $\mathcal{R} = \delta/4$ (the stored reading), $D = \tfrac14 s^{1/2}$; (C1) flat slice with the deposit's momentum noise, $|\alpha| = \tfrac14$, $|\beta| = 2X$, $D = \tfrac14(1 + 6X)s^{1/2}$; (CA) slice of uniform expansion, to leading order in $1/X$, $|\alpha| = \tfrac32X^{2}$, $\beta = 0$, $D = \tfrac32X^{2}s^{1/2}$. By (ii), $D(k)^{2} \ge A$ requires
\[
\frac{\omega_{\max} + \kappa}{M_{H}} \;\ge\; \frac{8\pi AX^{3}}{2f + \eta}\ \ \text{(C0)}, \qquad \frac{8\pi AX^{3}}{(2f + \eta)(1 + 6X)^{2}}\ \ \text{(C1)}, \qquad \frac{2\pi A}{9(2f + \eta)X}\ \ \text{(CA)}.
\]
\item[(v)] \emph{(Numbers.)} Take $k = a_{0}H_{0}$, the largest observed scale, and $A = 2.0 \times 10^{-9}$, the lower record value of $A_{s}$ at the pivot (Fact \claimref{synthesis.imported-planck-2018-lcdm-parameters}), which the measured red spectrum exceeds at larger scales, and the stored $X > 4.96 \times 10^{7}$ at $T_{d} = 1$ MeV and $X > 7.27 \times 10^{22}$ at $T_{d} = 10^{12}$ GeV (Theorem \claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}(iii), with its $g_{*} = 10.75$ and $106.75$ and the reduced Planck mass $\bar M_{P} = 2.435 \times 10^{18}$ GeV); $f \le 1$ and $\eta < 10^{-20}$. Under (C0) some quantum has $\omega_{\max} > 3.0 \times 10^{15}\,M_{H}$ at $1$ MeV and $> 9.6 \times 10^{60}\,M_{H}$ at $10^{12}$ GeV; equivalently a white contrast reaching $16A$ at $X$ is $16AX^{3} > 3.9 \times 10^{15}$ at the descent's Hubble scale. Under (C1) $\omega_{\max} > 0.034\,M_{H}$ at $1$ MeV and $> 5.0 \times 10^{13}\,M_{H}$ at $10^{12}$ GeV, which with $M_{H}/\bar M_{P} = 4\sqrt{90/g_{*}}\,(\bar M_{P}/T_{d})^{2}$ is more than $2.3 \times 10^{42}$ and $1.1 \times 10^{27}$ reduced Planck masses; between the two ends the (C1) bound in Hubble masses increases with $X$. The bounds are stated for $f \le 1$; a smaller share raises them, in proportion to $1/f$ once $\eta$ is neglected. Under (CA) the condition is weak: at the pivot at $T_{d} = 10^{12}$ GeV ($X > 3.2 \times 10^{20}$, $A \le 2.2 \times 10^{-9}$, $f = 1$) it reads $\omega_{\max} + \kappa \ge c\,M_{H}$ with $c < 2.5 \times 10^{-30}$, while $T_{d} > 10^{-20}\,M_{H}$ there, so quanta of thermal energy meet it with more than nine orders to spare.
\end{enumerate}
Consequently the number of quanta of a deposit that does not conserve entropy is fixed by the energy budget of the descent, not by the record of the entropy: a quasi-free fermion deposit whose shot noise reaches the measured amplitude at the present Hubble scale through a flat-slice conversion contains quanta each of more than $10^{27}$ reduced Planck masses, at every reheating temperature of the window and for every share of the density, and with the deposit at rest on the slice each of more than $10^{15}$ Hubble masses. \emph{Reading (argued).} Such a quantum is not a quantum of a field on a Robertson-Walker collar of the descent (its energy exceeds the Planck mass by more than twenty-seven orders, and under (C0) the contrast is far above one at the Hubble scale), so within the setting of the cited clause and of Premise (HD) a sparse or energetically broad quasi-free deposit does not carry the measured amplitude under either flat-slice conversion; the criterion "energies below the Planck mass" is not a stored premise. Under the uniform-expansion conversion the count excludes nothing: there a deposit is bounded by the shape of its spectrum on the observed band, which this result does not address.

## technical
The stored shot-noise bound removes dense quasi-free deposits and leaves sparse or energetically broad ones, because the bound scales inversely with the number of quanta and the record of the entropy does not fix that number for a deposit that reaches today's radiation by producing entropy. The number is fixed another way. The total density at the descent is known from the Friedmann relation at the reheating temperature, so a deposit with few quanta has much energy in each. The stored shot term is an integral of $(\omega + \kappa)^{2}$ over the quanta. It is at most the largest quantum energy times the integral of $\omega + \kappa$, and the second integral is the energy density plus $\kappa$ times the number density; the exclusion principle bounds the number of quanta softer than $\kappa$ by the number of modes in the momentum ball of radius $\kappa$, which is negligible, and the harder ones contribute at most the energy density again. Dividing by the square of the density and using the Friedmann relation turns the bound into the energy of the hardest quantum in Hubble masses, divided by the cube of the factor by which the mode lies outside the Hubble length. The same holds for the momentum density, whose one-body form obeys the same inequality mode by mode. How much shot noise an amplitude needs depends on how the contrast converts into the curvature perturbation, and the stored statements do not fix this; three conversions are therefore carried as hypotheses. On a flat slice with the deposit at rest the curvature perturbation is a quarter of the contrast, and the measured amplitude at the present Hubble scale needs quanta of more than $10^{15}$ Hubble masses: the white contrast would be far above one at the descent's Hubble scale, which is the stored finite-range obstruction seen from the side of the quanta. On a flat slice with the deposit's own momentum noise the conversion gains a factor of the order of the distance outside the Hubble length, and the quanta needed are a few percent of a Hubble mass at $1$ MeV, rising with the temperature in Hubble masses and never below $10^{27}$ reduced Planck masses in the window: lumps of the mass scale of the Hubble volume, not field quanta. On a slice of uniform expansion the conversion gains the fourth power in the spectrum, the condition falls far below thermal energies at the top of the window, and the count is no obstruction; the uniform-expansion reading has to be confronted through the shape of the spectrum instead.

## lay
One loophole in the earlier result was a deposit with very few particles: few particles means large random variation from place to place, perhaps as large as the measured ripples. But the total energy of the newborn universe is known, so few particles means each one carries an enormous energy. Working this out, a deposit sparse enough to make the measured ripples would need particles each weighing more than a billion billion billion Planck masses, heavier than whole regions of the universe at that time. Those are not particles of any field; they would be black holes. So the loophole closes, provided the ripples are read off the deposit in the way the earlier result assumed. There is another way of reading them, in which the geometry of space rather than the expansion rate takes up the unevenness of the deposit; in that reading the argument does not close the loophole, and the question becomes whether the pattern has the right dependence on scale.

## one-liner
With the density at the descent fixed by the record, the stored shot term is at most $\tfrac{2(2f + \eta)}{\pi}X^{-3}(\omega_{\max} + \kappa)/M_{H}$, so a quasi-free fermion deposit reaching the measured amplitude at the present Hubble scale needs a quantum above $3.0 \times 10^{15}$ Hubble masses on a flat slice at rest and above $1.1 \times 10^{27}$ reduced Planck masses on a flat slice with its own momentum noise, at every reheating temperature of the window; under the uniform-expansion conversion the condition is met by thermal quanta and the count closes nothing.
