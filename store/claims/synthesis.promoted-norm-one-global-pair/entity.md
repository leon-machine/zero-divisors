---
id: synthesis.promoted-norm-one-global-pair
kind: claim
version: 4
title: Under the Henneaux-Teitelboim promotion the norm mode becomes the one global pair of that reduction, the Goldstone count stays nine against nine, and N becomes initial data
status: proved
region: synthesis
subject: dark-energy
tags:
- the-number-n
- undetermined-input
- cosmological-constant
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
derivations:
- name: main
  uses:
  - dark-energy.imported-henneaux-teitelboim-promotion@5
  - dark-energy.point-infinity-has-no-physical-fluctuation@4
  - dark-energy.under-action-written-norm-parameter-laws@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_pointwise_count_with_norm_mode
- kind: check
  ref: check.py::check_multiplier_sector_one_global_pair
- kind: check
  ref: check.py::check_liouville_density_depends_on_multiplier
lineage:
  motivated_by:
  - dark-energy.under-action-written-norm-parameter-laws
about:
- obj.dark-energy.four-ways-number-enters-theory-shape
- obj.synthesis.gtg-flat-spacetime-gauge-fields
extraction:
  maintainer_pass_2:
    by: maintainer-2026-10-24
    date: '2026-10-24'
    note: 'Gauge Theory Gravity wording pass at Leon''s request (2026-10-24): curved-spacetime and conformally-flat wording restated in terms of the gravitational field on flat spacetime (a nonvanishing gravitational field; the Weyl part of the field strength vanishes, the conformally flat derived metric kept as a reading; global content read on an atlas of flat charts patched by gauge transformations). Wording only; statements, proofs'' arguments and checks unchanged. Version 3 -> 4. Referee fixes to the GTG wording pass (2026-10-24): ''a gravitational field of nonvanishing field strength'' (gauge-independent) in place of ''a nonvanishing gravitational field''; global content read on several charts of flat spacetime, each with its own gravitational field, glued by displacement and rotation gauge transformations (complexified charts for the half-flat manifold, the conformal compactification for a conformal boundary); ''not carried by the store''s one-chart fields'' in place of ''no single gravitational field carries''; equivalence statements weakened where the old text was weaker; remaining curved-spacetime phrases in lay text restated. Wording only.'
  notation_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: Squares of vectors written Q(v) in place of the inner product of a vector with itself; no change of content.
  open_problem: op.henneaux-teitelboim-promotion
  note: Carries the promotion branch of the decision through the series' own count. The local Goldstone count is unchanged, the promotion adds one global pair (Lambda, cosmic time), N becomes initial data, and the only measure the promotion itself names is the Liouville measure, which depends on which function of the norm is promoted.
  flags:
  - 'beyond one flat chart: the compact spatial slice Sigma of M = R x Sigma (the one global pair)'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity (FLAG): the spacetime M carries a gravitational field (hb, Omega) on flat spacetime; the compact spatial slice Sigma of M = R x Sigma, on which the reduced phase space H^0 x H^3 gives the one global pair, carries the Section 14 flag and a flags entry; the pointwise count (i) and d lambda = 0 of (ii) are local. Clauses (i)-(v) unchanged.'
---

## formal
\emph{Setting.} Promote the norm as in Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}: in the three-argument functional of Proposition \claimref{dark-energy.point-infinity-has-no-physical-fluctuation}, replace the number $\Lambda$ in the Stelle-West constraints $Q(I) = \Lambda/3$, $Q(V) = -3/\Lambda$ by a positive function $\lambda$ on spacetime $M$, on which gravity is a gravitational field $(\hb, \Omega)$ (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), and add $c\int_{M}\lambda\,dT$ with $c \ne 0$ a constant and $T$ a $3$-form field. Take $M = \R \times \Sigma$ with $\Sigma$ compact, connected and orientable.
\begin{enumerate}
\item[(i)] \emph{(Pointwise count.)} At each point the linearised constraints are three independent conditions on the thirteen components of $(\delta I, \delta V, \delta\lambda)$; the ten remaining directions are the nine images of the broken generators and the norm mode $n = (I/2\lambda, -V/2\lambda, 1)$ of Proposition \claimref{dark-energy.under-action-written-norm-parameter-laws}. Unitary gauge removes every fluctuation of $(I, V)$ except the multiple $\delta\lambda\,n$.
\item[(ii)] \emph{(No local norm mode.)} Varying $T$ gives $d\lambda = 0$, so on connected $M$ the multiplier is a constant $\Lambda$ and the norm mode enters as one number $\delta\Lambda$, constant over spacetime. No local fluctuation of $(I, V, \lambda)$ survives unitary gauge: the local Goldstone count is nine broken generators against nine eaten directions, as without the promotion, and the graviton still carries no $(\delta I, \delta V, \delta\lambda)$ polarisation.
\item[(iii)] \emph{(One global pair.)} In $c\int\lambda\,dT$ the pullback $T_{\Sigma}$ of $T$ to a slice is conjugate to $\lambda$, and the components of $T$ along the time direction are multipliers for the constraint $d\lambda|_{\Sigma} = 0$, which generates $T_{\Sigma} \mapsto T_{\Sigma} + d\theta$. The reduced phase space of the $(\lambda, T)$ sector is $H^{0}(\Sigma) \times H^{3}(\Sigma) \cong \R^{2}$, paired by integration over $\Sigma$: exactly one canonical pair $(\Lambda, \tau)$, $\tau = \int_{\Sigma}T_{\Sigma}$, and no local degree of freedom.
\item[(iv)] \emph{(Kind of number.)} The promoted functional has no parameter left in the norm, and for every $\Lambda > 0$ the solutions of the unpromoted equations with parameter $\Lambda$, together with a $T$ solving the $\lambda$-equation, are solutions of it. So $N = M_{P}\sqrt{3/\Lambda}$ is not constant on its solution space: in the sense of Definition \claimref{obj.dark-energy.four-ways-number-enters-theory-shape} it is (I), initial data, and not (P).
\item[(v)] \emph{(The measure the promotion names.)} The Liouville measure of the reduced pair is $|c|\,d\Lambda\,d\tau$, so the Liouville density per unit $\tau$ is constant in $\Lambda$ and its integral over $\Lambda > 0$ diverges. This is a density on the reduced phase space, not a normalised weight over histories: on a solution $\tau$ advances by an amount that depends on the solution. If instead a function $g$ of the norm is promoted, $c\int g(\lambda)\,dT$, the Liouville density per unit $\tau$ is $|c\,g'(\Lambda)|$: constant for the norm $Q(I) = \Lambda/3$ that the Fact transcribes, $3|c|/\Lambda^{2}$ for $\ell^{2} = 3/\Lambda$. The promotion names a measure only together with the choice of $g$. With the transcribed choice, a cutoff $\Lambda \le \Lambda_{\max}$, and the convention that every value of $\Lambda$ is given the same $\tau$-range, the measure of $\Lambda \le \Lambda_{\mathrm{obs}}$ is the fraction $\Lambda_{\mathrm{obs}}/\Lambda_{\max}$, which equals $3/N^{2}$ for $\Lambda_{\max} = M_{P}^{2}$; without both assumptions no fraction is defined.
\end{enumerate}

\emph{Beyond one flat chart.} The compact spatial slice $\Sigma$ of $M = \R \times \Sigma$, on which the reduced phase space of (iii) is $H^{0}(\Sigma) \times H^{3}(\Sigma)$, is global and is not carried by a single gravitational field $(\hb, \Omega)$ on flat spacetime; the statements above that hold on the invertible region (the pointwise count (i) and the equation $d\lambda = 0$ of (ii)) are in GTG, and the compact slice is read on the manifold assembled from the derived metric's charts.

## technical
The decision left open is whether the cosmological constant is a parameter of the series' action or the value of a field whose constancy is an equation of motion. This result carries the second branch through. Its new content is the series' own count with the norm mode and the change in which kind of number $N$ is; the one global pair and the absence of local degrees of freedom are the Henneaux-Teitelboim reduction itself, applied here to the norm. Pointwise nothing changes: with the norm free there are ten constrained directions, nine of them gauge and the tenth the norm mode already found in the store. The promotion's own equation says the multiplier is constant, so the norm mode is a single number for the whole universe, not a field: no new local degree of freedom appears and the graviton count is untouched. The 3-form that carries the promotion has no local degrees of freedom either; on a closed slice it leaves exactly one number, its integral, the cosmic time conjugate to the cosmological constant. The cochain check exhibits this on lattice 3-tori, where the constraint leaves the constants and the gauge freedom leaves only the total. Under the promotion the number N therefore varies across the solutions of one theory, which is what initial data means in the series' classification. Finally, the only measure over the cosmological constant that the promotion supplies without a further choice is the Liouville measure of its one canonical pair. Its density per unit of the conjugate time is flat in whichever function of the norm is promoted, so it is fixed only with that choice; for the norm itself it is flat in the cosmological constant. Only with a cutoff at the Planck scale and the convention that every value gets the same range of conjugate time does this become a fraction, about $3/N^{2}$, for values as small as the observed one; on actual histories the conjugate time advances by a solution-dependent amount, so the convention is a choice. A computation filed alongside, synthesis.promoted-norm-weyl-clock-flat-weight, finds that the conjugate time advances by the Weyl-squared integral, and that under the no-boundary hypothesis the round four-sphere has weight one at every cosmological constant, so no factor of the action favours small values; with that, the smallness of the cosmological constant stays unexplained under the promotion. Reading, not proved here: since the conjugate time is global, the cosmological constant commutes with every local observable, so the I-state of the cosmological horizon lives in one sector of fixed cosmological constant, and a state with a definite cosmic time spreads over sectors and is KMS at no single temperature. Its compact spatial slice, on which the one global pair lives, is global: no single gravitational field on flat spacetime carries it, so that part is read on several charts of flat spacetime, each carrying its own gravitational field, glued on overlaps by displacement and rotation gauge transformations.

## lay
The series has a choice to make about the cosmological constant: is it a fixed setting of the laws, or a quantity that happens to have the value it has in our universe, as a starting condition would? The standard way to make it the second is to let it be a field and add an equation saying the field cannot vary. This result works out what that choice adds to the series. Nothing local: there is still no new particle or wave, and the count of the series' hidden directions is unchanged. What it adds is a single pair of numbers for the whole universe, the cosmological constant and a cosmic clock reading that goes with it. With that choice, the number N that sets the scale of the universe becomes a starting condition rather than a law. The natural way of weighing the possible values that the choice supplies treats every value equally per unit of the cosmic clock, so it does not explain why the observed value is so small; and even that weighing depends on which version of the quantity is made into a field.

## one-liner
Under the Henneaux-Teitelboim promotion the norm mode becomes that reduction's one global pair $(\Lambda, \tau)$ with no local mode, the Goldstone count stays nine against nine, $N$ becomes initial data, and the Liouville density per unit $\tau$, the only measure the promotion names, is flat in whichever function of the norm is promoted.
