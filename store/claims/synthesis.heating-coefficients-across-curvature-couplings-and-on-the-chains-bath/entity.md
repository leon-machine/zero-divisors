---
id: synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath
kind: claim
version: 1
title: Heating coefficients across curvature couplings and on the chain's bath
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, mirror-sector, seesaw-and-majorana, undetermined-input]
proposed_by:
  kind: ai
  session: 2026-11-18-leads
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Fable 5.2
  role: proposal and drafting
  source: run 2026-11-18-leads
review: draft
derivations:
- name: main
  uses:
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@2
  - synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt@1
  - synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point@4
  - synthesis.seeding-remainder-excludes-perturbative-pati-salam@3
  - synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off@2
  - standard-model.chain@8
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_scalar_channel_weight_at_unequal_couplings
- kind: check
  ref: check.py::check_stored_readings_move_no_stated_figure
- kind: check
  ref: check.py::check_tilt_window_on_the_doublets_uses_up_the_margin
- kind: check
  ref: check.py::check_chain_bath_enters_coefficient_and_threshold_and_raises_the_margins
lineage:
  motivated_by:
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order
  - synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt
  - synthesis.seeding-remainder-excludes-perturbative-pati-salam
extraction:
  open_problem: op.curvature-coupling-across-subjects
  note: >-
    Filed against the link recorded on 18 November between the curvature coupling's open problem and the
    dark towers' heating: the scalar weights of the production rate carry (1 - 6 xi)^2. Registered before
    the computation: that at the stored readings (0 for the doublets, 1/6 for an attachment module) no
    stated figure moves (it does not); that the tilt window's coupling on the doublets would lose a stored
    conclusion (it uses up the margin of one clause and leaves it undecided, which is weaker than
    registered); and that the heating constrains the open datum (it does not, for the Standard Model's
    four scalars). Not registered, and found while asking which scalars are in the bath: the stored
    coefficients take the bath to be the Standard Model's content, as their texts say, while on the chain
    of the stored Pati-Salam clause, under Hypothesis (S), the content between the intermediate and the
    unification scale has 21 vectors, 48 Weyl fields and 188 real scalars, and the temperatures of that
    clause lie in that interval. Clause (iii) computes what follows. A first version of it changed the
    bath in the coefficient only and concluded that the stored margins fall and that one case fails at
    the tree-level coupling; that was wrong: the bath also enters the threshold, through the expansion
    rate and the entropy of the yield, and with both the margins rise. The version here is the corrected
    one, and its check holds the wrong figures as the case in which the threshold is left at the stored
    bath. It does not correct the stored results, which state their bath and are conservative on the
    chain. The case of four copies of the chain's own content is a construction of this result; no stored
    statement asks about it. Not done: thresholds at the intermediate scale (the species are taken
    massless, including the right-handed neutrinos, whose masses are of the order of the comparison
    temperature, an effect of a few percent on the count), thermal masses, the chains without the
    (15,2,2), the content above the unification scale, the running of any coupling. Transport-absent:
    arithmetic on the stored rate and the stored yield.
---

## formal

Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v) gives, under its hypothesis (OS) or on the standard account, at tree level and for free massless species, the coefficient $\alpha_{j}$ of pair creation $\Gamma_{j} = \alpha_{j}T^{8}/\bar{M}_{P}^{4}$ of a species $j$ from a bath of $N_{s}$ real scalars of trace weights $\tau_{i} = (1 - 6\xi_{i})^{2}$, $N_{w}$ chiral fermions and $N_{v}$ vectors. For a produced light content $D$ of $n_{s}$ real scalars of trace weights $\tau_{j}$, $n_{w}$ chiral fermions and $n_{v}$ vectors put $C_{D} = n_{s} + 3n_{w} + 12n_{v}$, $\tau_{D} = \sum_{j \in D}\tau_{j}$, $\tau_{B} = \sum_{i}\tau_{i}$, and $c(D) = \sum_{j \in D}\alpha_{j}$, the summed coefficient that the stored seeding results use. Write $c^{*} = 13.4949$ for the threshold of Proposition \claimref{synthesis.seeding-remainder-excludes-perturbative-pati-salam}(i), computed there with its inputs at the ends that weaken its conclusion and with the Standard Model's bath in the yield ($\kappa_{s} = 145.3$ at $g_{*} = g_{s} = 100$), and call $(c^{*}/c)^{1/4}$ the \emph{margin} at $c$ (the factor by which the seeding temperature exceeds the largest allowed $M_{3}$).
\begin{enumerate}
\item[(i)] \emph{(The couplings enter through one product; proved.)}
\[
c(D) \;=\; \frac{\pi^{3}}{17280}\left[\frac{C_{D}\,(N_{s} + 12N_{v}) + 5\,\tau_{D}\,\tau_{B}}{225} + \frac{49\,C_{D}\,N_{w}}{4800}\right],
\]
and the weight of scalars to scalars with two different couplings is $(\pi/180)(1 + 5\tau_{1}\tau_{2})$. So the coefficient of a produced vector or fermion depends on no curvature coupling; $c(D)$ does not depend on the couplings of one side when the scalars of the other are conformally coupled or absent; and $c(D)$ is least when $\tau_{D}\tau_{B} = 0$ and does not decrease when any $|1 - 6\xi|$ grows (it is constant in the couplings of one side when the other side's trace sum vanishes).
\item[(ii)] \emph{(The Standard Model's four scalars; computed.)} For the bath $(4, 45, 12)$ and a copy of that content, $c/\pi^{3} = 1519247/82944000 + (\tau_{D}\tau_{B} - 16)/777600$. At the stored reading of the doublets' coupling, $\xi = 0$ on both sides (Theorem \claimref{synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt}), this is the stored $0.5679$. With the scalars of either side or of both at the conformal value $\tfrac16$ it is lower by the fraction $5120/4557741$, about $0.11$ percent ($c = 0.5673$; the temperature floors, which go as $c^{1/4}$, by $0.03$ percent): the margins $2.2$ and $1.5$ of the stored clause, and its count of more than $23$ Standard-Model contents are unchanged, and $c$ stays below one. With every one of the four real scalars of the bath and of each copy at a coupling in the stored tilt window $[1.522584375, 1.548079215]$ (Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}), $\tau$ lies between $66.18$ and $68.70$, $c$ rises to between $3.362$ and $3.578$ ($5.92$ to $6.30$ times the stored value), and four contents have $c$ from $13.448$ to $14.313$: this crosses $c^{*}$ at a coupling between $1.5239$ and $1.5241$, inside the window, and the margin $1.5$ of the stored clause becomes a number between $0.98$ and $1.01$. With the same inputs at their central values $c^{*}$ is between $14.44$ and $14.45$ and is not reached (margins $1.002$ to $1.018$). So over the window that clause is not decided at four contents. With the window's coupling on the bath's scalars only, $c$ rises by a factor between $1.07$ and $1.08$. One further real scalar at the window's coupling raises a Standard-Model copy's $c$ by $2$ to $3$ percent if it is in the bath only and by a factor $1.35$ to $1.38$ if it is in the bath and in the copy; produced alone from the Standard Model's bath it has $5.8$ to $6.0$ times the coefficient of a minimally coupled scalar, between half of one vector's and one vector's. (These are statements about $c$; the threshold's own dependence on the bath, clause (iii), is one to two percent for one further scalar and is not included.)
\item[(iii)] \emph{(The chain's bath enters twice; computed.)} The stored clause is on the chain with the complex bidoublet, the complex $(10,1,3)$ and the complex $(15,2,2)$, whose content between $M_{I} = 1.9 \times 10^{10}$ GeV and $M_{U} = 3.4 \times 10^{16}$ GeV under Hypothesis (S) is $21$ vectors, $48$ Weyl fields and $188$ real scalars (Theorem \claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}(ii), Theorem \claimref{standard-model.chain}); the clause compares at temperatures up to $M_{3} < 5.35 \times 10^{11}$ GeV, $28$ times that $M_{I}$. Take the bath there to be $(188, 48, 21)$, all species massless. It enters in two places. In the coefficient: a vector's is $2.19$ times its value from the Standard Model's bath, whatever the couplings. In the threshold: the stored yield is $Y = c\,T^{3}/(3\kappa_{s}M_{P}^{3})$ with $\kappa_{s} = \sqrt{\pi^{2}g_{*}/90}\,(2\pi^{2}/45)\,g_{s}$, so $c^{*}$ is proportional to $g^{3/2}$ at $g_{*} = g_{s} = g$; here $g = 188 + \tfrac78 \cdot 96 + 42 = 314$ and $c^{*}$ rises by $3.14^{3/2} = 5.56$ to $75.1$. Together the margins of the stored clause rise: for the odd towers' $22$ vectors ($c = 1.158$) the margin is between $2.83$ and $2.84$, where above $2.2$ is stored, and for four Standard-Model contents with all scalars at $\xi = 0$ ($c = 5.087$) it is between $1.95$ and $1.97$, where above $1.5$ is stored; the threshold is $1425$ vector species or $59$ Standard-Model contents, where about $560$ and more than $23$ are stored. (With the bath changed in the coefficient alone the same $c$ against $13.4949$ would give $1.84$ and $1.27$; that comparison is inconsistent and is not a result.) As a construction of this result, which no stored statement asks about, take four copies of the chain's own content ($C_{D} = 584$) with one coupling for all scalars: $c = 15.89$ at $\xi = 0$ and $10.25$ at $\xi = \tfrac16$, margins $1.47$ and $1.65$, and $c < c^{*}$ exactly on an interval of $\xi$ whose ends lie in $(-0.141, -0.140)$ and $(0.473, 0.474)$, which contains both stored readings. The ceiling reheating $6 \times 10^{14}$ GeV lies below every stored two-loop unification scale (the least is $8.9 \times 10^{14}$ GeV), so the same bath would apply there on the chain; the floors are not recomputed here. The chains without the $(15,2,2)$ ($64$ or $68$ real scalars, other intermediate scales) are not the clause's and are not treated.
\end{enumerate}
\emph{Reading (argued).} Which stored coupling applies to which scalar of the heating: the store fixes a reading only for the rung field's doublets, the tree-level value $0$, argued in the stored result; the bath's four real scalars are the components of such a doublet, and the stored coefficients assume $0$ for them; the scalars of a copy carry the same value if the copy has the same action, which is the stored description of the mirror and is not proved here; the conformal value belongs to the attachment's helicity-zero module, a property of its spectrum, and would lower $c$ by $0.11$ percent if a scalar of either side were read as such a module; the scalar of the tilt fit is no stored field, and (ii) gives what it would do as a further light scalar; the chain's scalars above $M_{I}$ have no stored coupling. The heating does not constrain the open datum. On the Standard Model's four scalars no stated figure separates $0$ from $\tfrac16$, and the tilt window is reached only on the one-field reading that the stored result excludes on other grounds, where it uses up one margin without reversing the clause at central inputs. On the chain the larger bath dilutes the yield faster than it raises the coefficient, so the stored clause, computed with the Standard Model's bath, is conservative there: its exclusion stands with larger margins, and the curvature couplings of the chain's scalars do not decide it at either stored reading, even in the constructed case of four copies of the chain's content. Scope: the hypotheses of the rate theorem (tree level, free massless species, zero chemical potentials, no occupation of the produced species); $g_{*} = g_{s}$ counted for massless species, with the right-handed neutrinos included although the heaviest has a mass of the order of the comparison temperature (a few percent); thresholds at $M_{I}$ and thermal masses are ignored; the content above $M_{U}$ is not stored; nothing here uses the energy per creation event.

## technical

The gravitational heating rate of the store has scalar channels that depend on the curvature coupling through $\tau = (1 - 6\xi)^{2}$. Summed over a produced content $D$ from a bath, the coefficient is
$c = \frac{\pi^{3}}{17280}\bigl[\frac{C_{D}(N_{s} + 12N_{v}) + 5\tau_{D}\tau_{B}}{225} + \frac{49C_{D}N_{w}}{4800}\bigr]$,
so the couplings enter only through the product of the two trace sums. Vectors and fermions are blind to them, and one conformal side switches the dependence off.

For the Standard Model's bath and a copy of it the trace term is $16/777600$ of $c/\pi^{3}$, $0.11$ percent. Between the two stored readings, $0$ for the doublets and $\tfrac16$ for an attachment module, nothing moves. The tilt window near $1.53$ would raise $c$ about sixfold if all doublets carried it, which brings four contents to the stored threshold $c^{*} = 13.49$ of the Pati-Salam clause: the crossing is at $\xi = 1.524$, inside the window, and at central inputs $c^{*} = 14.44$ is not reached. That clause would then be undecided; but the one-field reading is excluded by the stored result on other grounds.

The bath itself matters more than its couplings, and it enters twice. The stored coefficients use the Standard Model's content $(4, 45, 12)$. On the chain of the stored Pati-Salam clause, between the intermediate and unification scales, the content is $(188, 48, 21)$, and the clause compares at temperatures in that interval. Then a vector's coefficient is $2.19$ times larger; but the yield also falls, because the expansion rate and the entropy grow with the bath, $Y = c\,T^{3}/(3\kappa_{s}M_{P}^{3})$ with $\kappa_{s}$ proportional to $g^{3/2}$, and the threshold rises $5.56$ times, to $c^{*} = 75.1$ at $g = 314$. The net effect is that the clause's margins rise, from $2.2$ and $1.5$ to $2.84$ and $1.96$: the stored clause is conservative on its own chain. Four copies of the chain's own content, a case constructed here, have $c = 15.9$ at $\xi = 0$ and $10.3$ at the conformal value, both below the threshold (margins $1.47$ and $1.65$); they would reach it only for $\xi$ below $-0.14$ or above $0.47$. On the chain's bath neither stored assignment, $0$ or $\tfrac16$, decides the clause; the tilt window's coupling on the chain's scalars is not treated.

## lay

The store holds a rate at which gravity alone heats hidden sectors from the hot early plasma. For spinless particles that rate depends on a number that says how the particle feels the curvature of spacetime, and the store uses three different values of that number in three places. This result asks whether the choice matters for the heating.

For the plasma of known particles it does not: between the two values the store actually assigns, the heating changes by about one part in a thousand, and no stored conclusion moves. The third value, which was fitted elsewhere to the pattern of the primordial fluctuations, would raise the heating sixfold if the Higgs field carried it, enough to leave one stored exclusion undecided; but the store already rules that reading out for other reasons.

Which particles are in the plasma matters more, and in two opposite ways. One stored exclusion is argued inside a specific unified model, and at the temperatures it considers that model's plasma contains many more particles than the known ones. More particles heat the hidden sectors faster, but they also make the universe expand faster and dilute what is produced, and the second effect wins. So the stored exclusion, which was computed with the known particles only, holds with more room to spare when the model's own plasma is counted, and at the two values of the curvature number that the store assigns, the answer is the same.

## one-liner

Under the hypotheses of the stored rate theorem (tree level, free massless species), the summed heating coefficient depends on curvature couplings only through $5\tau_{D}\tau_{B}/225$: for the Standard Model's bath and a copy of it the stored readings $0$ and $\tfrac16$ differ by $0.11$ percent, the tilt window on all doublets would bring four contents to the stored threshold $c^{*} = 13.49$ (crossing at $\xi = 1.524$; not reached at central inputs), and on the chain of the stored Pati-Salam clause the bath $(188, 48, 21)$ raises a vector's coefficient $2.19$ times and the threshold $5.56$ times (through $\kappa_{s} \propto g^{3/2}$), so the stored margins $2.2$ and $1.5$ become $2.84$ and $1.96$ and neither stored assignment of a coupling, $0$ or $\tfrac16$, decides the clause.
