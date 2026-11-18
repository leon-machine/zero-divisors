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
  - synthesis.gravitational-pair-production-from-the-operator-source-at-first-order@1
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
  ref: check.py::check_chain_bath_lowers_the_margins_and_its_scalars_decide_the_copies
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
    under Hypothesis (S) the content between the intermediate and the unification scale has 21 vectors, 48
    Weyl fields and 64, 68 or 188 real scalars, and both the ceiling reheating and the temperatures of the
    Pati-Salam clause lie in that interval. Clause (iii) computes what follows. It does not correct the
    stored results, which state their bath; whether they should be restated with the chain's bath where
    they are on the chain is the maintainer's decision, and the floors' entities are being restated in
    this run for another reason. Not done: thresholds at the intermediate scale (the species are taken
    massless), thermal masses, the content above the unification scale, the running of any coupling.
    Transport-absent: arithmetic on the stored rate.
---

## formal

Theorem \claimref{synthesis.gravitational-pair-production-from-the-operator-source-at-first-order}(v) gives, under its hypothesis (OS) or on the standard account, at tree level and for free massless species, the coefficient $\alpha_{j}$ of pair creation $\Gamma_{j} = \alpha_{j}T^{8}/\bar{M}_{P}^{4}$ of a species $j$ from a bath of $N_{s}$ real scalars of trace weights $\tau_{i} = (1 - 6\xi_{i})^{2}$, $N_{w}$ chiral fermions and $N_{v}$ vectors. For a produced light content $D$ of $n_{s}$ real scalars of trace weights $\tau_{j}$, $n_{w}$ chiral fermions and $n_{v}$ vectors put $C_{D} = n_{s} + 3n_{w} + 12n_{v}$, $\tau_{D} = \sum_{j \in D}\tau_{j}$, $\tau_{B} = \sum_{i}\tau_{i}$, and $c(D) = \sum_{j \in D}\alpha_{j}$, the summed coefficient that the stored seeding results use. Write $c^{*} = 13.4949$ for the threshold of Proposition \claimref{synthesis.seeding-remainder-excludes-perturbative-pati-salam}(i), computed there with its inputs at the ends that weaken its conclusion, and call $(c^{*}/c)^{1/4}$ the \emph{margin} at $c$ (the factor by which the seeding temperature exceeds the largest allowed $M_{3}$).
\begin{enumerate}
\item[(i)] \emph{(The couplings enter through one product; proved.)}
\[
c(D) \;=\; \frac{\pi^{3}}{17280}\left[\frac{C_{D}\,(N_{s} + 12N_{v}) + 5\,\tau_{D}\,\tau_{B}}{225} + \frac{49\,C_{D}\,N_{w}}{4800}\right],
\]
and the weight of scalars to scalars with two different couplings is $(\pi/180)(1 + 5\tau_{1}\tau_{2})$. So the coefficient of a produced vector or fermion depends on no curvature coupling; $c(D)$ does not depend on the couplings of one side when the scalars of the other are conformally coupled or absent; and $c(D)$ is least when $\tau_{D}\tau_{B} = 0$ and increases with every $|1 - 6\xi|$.
\item[(ii)] \emph{(The Standard Model's four scalars; computed.)} For the bath $(4, 45, 12)$ and a copy of that content, $c/\pi^{3} = 1519247/82944000 + (\tau_{D}\tau_{B} - 16)/777600$. At the stored reading of the doublets' coupling, $\xi = 0$ on both sides (Theorem \claimref{synthesis.no-single-curvature-coupling-serves-the-sakharov-zero-and-the-kasner-tilt}), this is the stored $0.5679$. With the scalars of either side or of both at the conformal value $\tfrac16$ it is lower by the fraction $5120/4557741$, about $0.11$ percent ($c = 0.5673$; the temperature floors, which go as $c^{1/4}$, by $0.03$ percent): the margins $2.2$ and $1.5$ of the stored clause, and its count of more than $23$ Standard-Model contents are unchanged, and $c$ stays below one. With every one of the four real scalars of the bath and of each copy at a coupling in the stored tilt window $[1.522584375, 1.548079215]$ (Theorem \claimref{synthesis.tree-level-curvature-couplings-stay-blue-at-the-isotropic-kasner-point}), $\tau$ lies between $66.18$ and $68.70$, $c$ rises to between $3.362$ and $3.578$ ($5.92$ to $6.30$ times the stored value), and four contents have $c$ from $13.448$ to $14.313$: this crosses $c^{*}$ at a coupling between $1.5239$ and $1.5241$, inside the window, and the margin $1.5$ of the stored clause becomes a number between $0.98$ and $1.01$. With the same inputs at their central values $c^{*}$ is between $14.44$ and $14.45$ and is not reached (margins $1.002$ to $1.018$). So over the window that clause is not decided at four contents. With the window's coupling on the bath's scalars only, $c$ rises by a factor between $1.07$ and $1.08$. One further real scalar at the window's coupling raises a Standard-Model copy's $c$ by $2$ to $3$ percent if it is in the bath only and by a factor $1.35$ to $1.38$ if it is in the bath and in the copy; produced alone from the Standard Model's bath it has $5.8$ to $6.0$ times the coefficient of a minimally coupled scalar, between half of one vector's and one vector's.
\item[(iii)] \emph{(The chain's bath; computed.)} On the chain under Hypothesis (S) the stored content between $M_{I}$ and $M_{U}$ is $21$ vectors, $48$ Weyl fields and $N_{s} = 64$, $68$ or $188$ real scalars (a real or complex bidoublet and the complex $(10,1,3)$, and with the complex $(15,2,2)$; Theorem \claimref{synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off}(ii), Theorem \claimref{standard-model.chain}). The stored clause compares at temperatures up to $M_{3} < 5.35 \times 10^{11}$ GeV, $28$ times that chain's $M_{I} = 1.9 \times 10^{10}$ GeV, and the ceiling reheating $6 \times 10^{14}$ GeV lies below the stored values of $M_{U}$. With the bath $(N_{s}, 48, 21)$, all species taken massless: the coefficient of a vector is $1.70$, $1.71$, $2.19$ times its value from the Standard Model's bath, whatever the couplings; the odd towers' $22$ vectors have $c = 0.897$, $0.906$, $1.158$ and margin above $1.96$, $1.96$, $1.84$ (and below $1.97$, $1.97$, $1.85$), where ``above $2.2$'' is stored; four Standard-Model contents, with all scalars at $\xi = 0$, have margin above $1.36$, $1.36$, $1.27$ (and below $1.37$, $1.37$, $1.28$), where ``above $1.5$'' is stored; and at $N_{s} = 188$ the threshold $c^{*}$ is $256$ vector species or $10$ Standard-Model contents, where $560$ and $23$ are stored. For four copies of the chain's own content ($C_{D} = N_{s} + 396$): with all scalars at $\xi = 0$, $c = 6.91$, $7.11$, $15.89$, margins $1.18$, $1.17$ and, for $N_{s} = 188$, $c > c^{*}$ (margin $0.96$); with all scalars conformal, $c = 6.25$, $6.37$, $10.25$, margins $1.21$, $1.21$, $1.07$. For $N_{s} = 188$ and one coupling for all scalars, $c < c^{*}$ holds exactly on an interval of $\xi$ whose ends lie in $(0.021, 0.022)$ and $(0.311, 0.313)$: it contains the conformal value and not the tree-level value $0$. For $N_{s} = 64$ and $68$ the copies reach $c^{*}$ only for $\xi$ beyond $0.46$ (or below $-0.12$).
\end{enumerate}
\emph{Reading (argued).} Which stored coupling applies to which scalar of the heating: the bath's and the copies' scalars are fields of the content with an action, for which the stored reading is the tree-level value $0$, the value the stored coefficients assume; the conformal value belongs to the attachment's helicity-zero module, a property of its spectrum, and would lower $c$ by $0.11$ percent if a scalar of either side were read as such a module; the scalar of the tilt fit is no stored field, and (ii) gives what it would do as a further light scalar. On the Standard Model's four scalars the heating does not constrain the open datum: no stated figure separates $0$ from $\tfrac16$, and the tilt window is reached only on the one-field reading that the stored result excludes on other grounds, where it uses up one margin without reversing the clause at central inputs. The dependence that matters is elsewhere: the stored clause (i) is on the chain, and at its temperatures the chain's bath is not the Standard Model's. With the chain's bath the exclusion stands for the contents the clause names, with margins above $1.84$ and $1.27$ at $N_{s} = 188$ where $2.2$ and $1.5$ are stated, and for four copies of the chain's own content with the $(15,2,2)$ it holds or fails according to the curvature couplings of the chain's scalars, which the store does not fix: it fails at the tree-level value and holds at the conformal one. Scope: the hypotheses of the rate theorem (tree level, free massless species, zero chemical potentials, no occupation of the produced species); thresholds at $M_{I}$ and thermal masses are ignored; the content above $M_{U}$ is not stored; nothing here uses the energy per creation event.

## technical

The gravitational heating rate of the store has scalar channels that depend on the curvature coupling through $\tau = (1 - 6\xi)^{2}$. Summed over a produced content $D$ from a bath, the coefficient is
$c = \frac{\pi^{3}}{17280}\bigl[\frac{C_{D}(N_{s} + 12N_{v}) + 5\tau_{D}\tau_{B}}{225} + \frac{49C_{D}N_{w}}{4800}\bigr]$,
so the couplings enter only through the product of the two trace sums. Vectors and fermions are blind to them, and one conformal side switches the dependence off.

For the Standard Model's bath and a copy of it the trace term is $16/777600$ of $c/\pi^{3}$, $0.11$ percent. Between the two stored readings, $0$ for the doublets and $\tfrac16$ for an attachment module, nothing moves. The tilt window near $1.53$ would raise $c$ about sixfold if all doublets carried it, which brings four contents to the stored threshold $c^{*} = 13.49$ of the Pati-Salam clause: the crossing is at $\xi = 1.524$, inside the window, and at central inputs $c^{*} = 14.44$ is not reached. That clause would then be undecided; but the one-field reading is excluded by the stored result on other grounds.

The larger effect is the bath. The stored coefficients use the Standard Model's content $(4, 45, 12)$. On the chain, between the intermediate and unification scales, the content is $(N_{s}, 48, 21)$ with $N_{s} = 64$, $68$ or $188$, and the Pati-Salam clause compares at temperatures in that interval. Then a vector's coefficient is $1.7$ to $2.2$ times larger, the clause's margins $2.2$ and $1.5$ become $1.84$ and $1.27$ at $N_{s} = 188$, and four copies of the chain's own content have $c = 15.9$ at $\xi = 0$ (above $c^{*}$) and $10.3$ at the conformal value (below it): for that content the clause holds only for $0.022 \le \xi \le 0.311$.

## lay

The store holds a rate at which gravity alone heats hidden sectors from the hot early plasma. For spinless particles that rate depends on a number that says how the particle feels the curvature of spacetime, and the store uses three different values of that number in three places. This result asks whether the choice matters for the heating.

For the plasma of known particles it does not: between the two values the store actually assigns, the heating changes by about one part in a thousand, and no stored conclusion moves. The third value, which was fitted elsewhere to the pattern of the primordial fluctuations, would raise the heating sixfold if the Higgs field carried it, enough to leave one stored exclusion undecided; but the store already rules that reading out for other reasons.

What does matter is which particles are in the plasma. One stored exclusion is argued inside a specific unified model, and at the temperatures it considers that model's plasma contains many more particles than the known ones. Counting them, the exclusion still stands for the cases it names, but with less room than stated, and for a hidden sector as rich as the model itself it stands or falls with the curvature number of the model's spinless particles.

## one-liner

The summed heating coefficient depends on curvature couplings only through $5\tau_{D}\tau_{B}/225$: for the Standard Model's bath and a copy of it the stored readings $0$ and $\tfrac16$ differ by $0.11$ percent, the tilt window on all doublets would bring four contents to the stored threshold $c^{*} = 13.49$ (crossing at $\xi = 1.524$; not reached at central inputs), and with the chain's bath $(N_{s}, 48, 21)$, $N_{s} = 64, 68, 188$, the stored margins $2.2$ and $1.5$ become $1.84$ and $1.27$ at $N_{s} = 188$ while four copies of the chain's content are below $c^{*}$ only for $0.022 \le \xi \le 0.311$.
