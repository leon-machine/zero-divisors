---
id: synthesis.slaved-field-failure-is-a-first-order-signal-from-a-classical-source-and-no-stored-premise-bounds-it
kind: claim
version: 1
title: 'The slaved field''s failure as a first-order signal, and what the store holds about it'
status: proved
region: synthesis
subject: quantum-fields
tags: [quantum-gravity, entanglement, finite-models, measurement-and-records]
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
outside_ga:
  kind: other
  why: the lattice field of the stored model and its retarded response are integer recursions outside the algebra, and the free field of its clause (4), used here only by citation, obeys canonical commutation relations; the matter factor, the device's unit and the expectation values are computed in Cl(1,2)
derivations:
- name: main
  uses:
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation@1
  - synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane@1
  - field-theory.operator-newtonian-coupling@4
  - synthesis.locality-of-the-attached-free-fields-fixes-their-statistics@5
  - synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field@3
  - synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number@4
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_matter_algebra_has_a_central_unit_and_the_device_is_a_unit
- kind: check
  ref: check.py::check_classical_source_shifts_the_detection_probability_at_first_order
- kind: check
  ref: check.py::check_signal_exists_at_172_of_502_spacelike_events
- kind: check
  ref: check.py::check_gravitational_size_of_the_phase_in_the_window
- kind: check
  ref: check.py::check_curvature_level_of_the_cutoff_premise_is_not_reached_outside_the_bodies
lineage:
  motivated_by:
  - pred.gravity-entangles-standard-phase
  - synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation
extraction:
  open_problem: op.gravitational-field-at-null-momentum
  note: >-
    Filed against the first two attack items of the problem: state the condition, and the localisation floor.
    Registered before the computation: "cannot be observed" means that the largest change of Alice's detection
    probability caused by Bob's choice at a spacelike event, eps, satisfies eps sqrt(N) < 1 over N runs, with
    the threshold eps < 1e-3 for the proposed experiments; kill conditions: no first-order term in the lattice
    model (not met: the term is nonzero at 172 of 502 spacelike events); a nonzero term with the free part (not
    met, by the stored result); a dependence of the signal on the width of a wave packet of Bob's device (not
    met: the device is a number); a stored bound on localisation or on the product of two masses from the
    cutoff premises (not found). The working notes of 12 October 2026 behind the registered prediction
    (Project documents, not in the repository; their notebook rows were read) withdrew a claim of safety that
    rested on an assumed floor on localisation at the Planck length. That floor belongs to a different effect:
    the reading of the which-path record by a probe, which lowers the visibility at second order (the argument
    of Belenchia et al. 2018, cited from memory). The stored failure is a commutator, hence a first-order effect,
    and its direct reading needs no probe with a wave packet; this result is about that reading. The
    hypothesis (D), that a device couples to the field by the model's own coupling under unitary evolution, is
    a hypothesis of this result; without a coupling of some kind the field is not observable and the condition
    has no content. The gravitational numbers of clause (5) are argued from the model and from the stored static
    coupling extended as in the stored result's Reading; they use the constants G, hbar and c as rational
    enclosures. The survey (S) is a reading of the stored texts at the pinned versions and is labelled as such;
    the cutoff premises and the local-horizon premise are read there and in clause (6), not assumed, so the
    result carries no edge to them.
    Decisions for the maintainer, unchanged: whether the series requires its gravitational field to commute with
    matter observables at spacelike separation. New for that decision: neither unitarity nor the cutoff premises
    supply the condition or hide its failure; in the proposed experiments the failure would be ten orders below
    observation with no floor at all; and for a classical source mass above about the Planck mass squared divided
    by the superposed mass it would not be small.
---

## formal
\emph{Setting.} The model of Theorem \claimref{synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation}: one quantum on two paths, $P_{1} = vw$, $P_{2} = wv$ in $\Cl(1,1)$ (\claimref{synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane}), source $J = c_{1}P_{1} + c_{2}P_{2}$ acting at site $0$ at the times $t' = 0, \dots, 5$, recombiner $U = p + q\,e_{2}$, detection $O = U^{-1}P_{1}U$ at the event $(0, 8)$, retarded response $G$, and $S(n,t) = \sum_{t'}G(n,t;t')$. Here $\Cl(1,1)$ is taken inside $\Cl(1,2)$, $e_{3}^{2} = -1$, whose pseudoscalar $I = e_{1}e_{2}e_{3}$ is central with $I^{2} = -1$ and is the unit of the phases. The elements $e_{1}$, $Ie_{2}$, $Ie_{3}$ anticommute and square to $1$, and $P_{1} = \tfrac12(1 + Ie_{3})$. A \emph{state} is an idempotent $\rho = \tfrac12(1 + a\,e_{1} + b\,Ie_{2})$, $a^{2} + b^{2} = 1$ (the quantum on both paths with equal weight and a relative phase), with expectation $\langle x\rangle = 2\br{\rho x}_{0}$; $x^{\dagger}$ denotes the conjugation that reverses products, fixes $e_{1}$ and negates $e_{2}$, $e_{3}$.

\emph{Hypothesis (D) (the device).} Bob holds a classical source of strength $\lambda$, a number, which he may place at the event $(n,t)$. It couples to the field by the model's own coupling with $\lambda$ in place of $J$, and the evolution is by units of the algebra: the device acts by $V = \exp(-I\lambda\,\phi_{n}(t))$, the form of the kicks in clause (4) of the stored model.
\begin{enumerate}
\item[(1)] \emph{(The slaved field is a unitary model; proved.)} With no free part, $\phi_{n}(t) = gJ\,S(n,t)$ and $V = \exp(-I\lambda g S\,J) = e^{-I\lambda gSc_{1}}P_{1} + e^{-I\lambda gSc_{2}}P_{2}$, a unit with $V^{-1} = V^{\dagger}$. So the evolution of the slaved model with the device is unitary, and unitarity does not imply that the field commutes with the detection.
\item[(2)] \emph{(The signal; proved.)} Put $\vartheta = \lambda\,g\,S(n,t)\,(c_{1} - c_{2})$. Then $V^{-1}e_{1}V = e_{1}\cos\vartheta + Ie_{2}\sin\vartheta$, and for a device placed not later than the detection
\[
\langle V^{-1}OV\rangle - \langle O\rangle = pq\,\bigl[a\,(\cos\vartheta - 1) + b\,\sin\vartheta\bigr] = \lambda\,\langle I\,[\phi_{n}(t), O]\rangle + O(\lambda^{2}), \qquad \langle I\,[\phi_{n}(t), O]\rangle = g\,S(n,t)\,(c_{1} - c_{2})\,pq\,b .
\]
Its absolute value is at most $|\sin(\vartheta/2)|$, with equality at $p = q$, $a = -\sin(\vartheta/2)$, $b = \cos(\vartheta/2)$. The change is of first order in the device's strength wherever the stored commutator is nonzero and the state has $b \neq 0$; no property of the device other than the number $\lambda$ enters.
\item[(3)] \emph{(Where; computed.)} On the stored grid the coefficient $g\,S\,(c_{1} - c_{2})\,pq\,b$ is nonzero at $172$ of the $502$ events spacelike to the detection. At $32$ of the $252$ such events not later than the detection the device, acting first, changes Alice's probability as in (2); at the $140$ later ones the same commutator makes the expectation of the field depend on whether Alice recombined.
\item[(4)] \emph{(With the free part; from the stored result.)} If the field has the free part of the stored model's clause (4), the first-order coefficient is $-g\sum_{t'}(G + \Delta)\,(c_{1} - c_{2})\,pq\,b$, which vanishes at all $502$ events.
\item[(5)] \emph{(Gravitational size; the estimate is argued, its numbers computed.)} Take the stored static coupling (Proposition \claimref{field-theory.operator-newtonian-coupling}) with the field of a body at each event a function of its commuting numbers, as in the stored result's Reading; let body $A$ of mass $m_{A}$ be on two paths a distance $d$ apart for longer than the light-crossing time, and let the device be a mass $m_{B}$ on the line of the two paths at distance $D$ from their midpoint. By (D) the phase between the paths while the device is present for a time $T$ is $\vartheta = G m_{A}m_{B}\,T\,|1/r_{1} - 1/r_{2}|/\hbar$, and the part accumulated at events spacelike to the detection has $T \le D/c$, so
\[
\vartheta \;\le\; \Phi_{w} = \frac{G\,m_{A}m_{B}}{\hbar c}\;D\,\Bigl|\frac{1}{r_{1}} - \frac{1}{r_{2}}\Bigr| , \qquad r_{1,2} = D \mp \tfrac12 d ,
\]
(a formulation that divides the energy of the pair between the two bodies' fields gives half of this). For $m_{A} = m_{B} = 10^{-14}$ kg, $d = 250\,\mu$m, $D = 450\,\mu$m: $\Phi_{w} = 1.27 \times 10^{-13}$, a change of probability below $6.4 \times 10^{-14}$, ten orders below the registered threshold $10^{-3}$ and needing more than $10^{26}$ runs. For the same superposition and a source of one kilogram at one metre, $\Phi_{w} = 5.3 \times 10^{-3}$, above the threshold; for a tonne, $5.3$. $\Phi_{w}$ is of order one when $m_{A}m_{B}\,D|1/r_{1} - 1/r_{2}|$ is the square of the Planck mass, $4.7 \times 10^{-16}$ kg$^{2}$.
\item[(6)] \emph{(The cutoff premises; computed.)} Premises \claimref{singularity.c1-curvature-cutoff} and \claimref{singularity.c2-cell-density} place boundary modes on the surface where $2M/r^{3} = 1$ in Planck units. For a tonne that level is below $10^{-90}$ at ten centimetres from its centre, and it is reached only at a radius below $10^{-31}$ m, which is inside the radius $2M$ of a hole of that mass: the surface does not exist in the configuration of (5).
\end{enumerate}
\emph{(S) What the store holds (a survey of the stored texts at the pinned versions; not part of the proved clauses).} (a) Theorem \claimref{synthesis.locality-of-the-attached-free-fields-fixes-their-statistics} concerns the bracket of a free scalar, spinor or photon field with itself; it does not treat the gravitational gauge field or a bracket of a field with matter observables. (b) Fact \claimref{synthesis.imported-dimock-dirac-car-algebra-on-a-gravitational-field} gives the Dirac field anticommutators that vanish at spacelike separation on a given gravitational field, which there is a background and not an element of the matter algebra. (c) Theorem \claimref{synthesis.interacting-fields-of-causal-perturbation-theory-keep-the-spin-statistics-connection-at-even-ghost-number} makes the interacting fields local to every order for interaction densities that are Wick monomials of the attached free fields at one point; its list holds no gravitational coupling, and the interaction of two sources through a slaved field is not of that form. (d) The stored static coupling is an equal-time coupling of the numbers of distant bodies: read as an evolution it changes one body's phase at once according to the other's number; it is a static limit and states no condition at spacelike separation. (e) The unitarity premise of the registered prediction does not imply the condition, by (1), and under it the failure is a signal, by (2). (f) Premises (C1), (C2) are read in the store as a calibration on the Schwarzschild family and say nothing of bodies or fields away from the cutoff surface; clause (Loc) of Premise \claimref{synthesis.c-loc-local-horizon-premise} is an entropy density on local horizons with no mode count. None bounds the localisation of a body, the product of two masses or $\Phi_{w}$. (g) The conventions record the question as not decided. So no stored premise implies that the gravitational field commutes with matter observables at spacelike separation, none makes a failure unobservable, and the store puts no other condition in its place.

\emph{Reading (argued).} The stored result says that a slaved field fails to commute with the later detection of its source. Read operationally, with (D), that failure is a change of the detection probability of first order in the strength of a classical source placed at a spacelike event: the source's interaction energy with the field is an operator on the matter, and a unitary evolution lets it act on the matter at once. Because the device is a number, no bound on how well anything can be localised makes this unobservable; what makes it small is the size of $G m_{A}m_{B}/\hbar c$. In the proposed experiments it is ten orders below observation with no floor of any kind, and it is of order one for a classical source of a few hundred kilograms at a metre from a superposed mass of $10^{-14}$ kg, if that source can be put in place within the light-crossing time (a source moving at speed $v$ reaches the fraction $v/c$ of this, argued). The floor on localisation at the Planck length that appears in the literature belongs to a different, second-order effect, the lowering of the visibility when a probe with a wave packet reads the which-path record; there it comes from the fluctuations of the field's free part (cited from memory), so a field with no free part cannot borrow it. The cutoff premises do not supply it either. The requirement itself remains a decision the store has not taken; this result says what follows either way: if commutation is required, (1) to (3) are a failure of the slaved field that nothing stored repairs; if it is not, (5) is the size of what is being accepted.

## technical
The stored lattice model shows that a field slaved to an operator source fails to commute with the source's later detection at spacelike separation. This result reads that failure as a signal and asks what in the store could forbid or hide it.

Put the two-path quantum in $\Cl(1,2)$, whose central pseudoscalar is the unit of phases. Let Bob hold a classical source of strength $\lambda$ which couples to the field by the model's own coupling (hypothesis (D)). With no free part the field is $gJS$, the device acts by the unit $\exp(-I\lambda gSJ)$, and Alice's detection probability changes by $pq[a(\cos\vartheta - 1) + b\sin\vartheta]$ with $\vartheta = \lambda gS(c_{1} - c_{2})$: first order in $\lambda$, at most $|\sin(\vartheta/2)|$. The model is unitary, so unitarity does not imply commutation; it turns the failure into a signal. On the stored grid this happens at $32$ of the $252$ spacelike events not later than the detection ($172$ of $502$ in all). With the free part the first-order term vanishes (the stored result).

The device is a number: no wave packet, so no floor on localisation hides the signal. Its gravitational size within the light-crossing time is at most $\Phi_{w} = (Gm_{A}m_{B}/\hbar c)\,D|1/r_{1} - 1/r_{2}|$ (argued): $1.3 \times 10^{-13}$ for the proposed experiments, ten orders below the registered threshold; $5 \times 10^{-3}$ for a kilogram at a metre; of order one when the product of the masses reaches the square of the Planck mass.

The cutoff premises (C1), (C2) concern a surface that does not exist outside a hole (the curvature level is below $10^{-90}$ near a tonne). A survey of the stored locality statements finds none that implies the condition for the gravitational field.

Ledger: transport-absent. Standard quantum mechanics of a two-path system and Newtonian estimates; the question is the series' own.

## lay
An earlier result built a small exact model of a field that has no freedom of its own and only repeats what its source did, and found that such a field fails a test of locality. This result asks what that failure would look like in a laboratory, and whether anything already in the series would prevent it from being seen.

The answer to the first question is simple. If someone far away places an ordinary heavy object near such a field, the interference pattern of the distant particle that sources the field shifts at once, before any signal at the speed of light could arrive. Nothing delicate is needed at the far end: an ordinary mass will do. This is why a limit on how sharply things can be located, which had been suggested as a protection, does not help.

The answer to the second question is that the series holds nothing that forbids this, and nothing that hides it in principle. What hides it in practice is that gravity between small masses is extremely weak: in the experiments now being designed the effect would be about ten billion times too small to see. For a source of some hundreds of kilograms next to the same experiment it would not be small, though placing such a source quickly enough is itself out of reach.

The result does not say that the series must require locality of this kind for gravity. It says what each choice costs.

## one-liner
In the stored lattice model, a classical source of strength $\lambda$ placed at a spacelike event and coupled to the slaved field by the model's own coupling changes the detection probability by $pq[a(\cos\vartheta - 1) + b\sin\vartheta]$, $\vartheta = \lambda gS(c_{1} - c_{2})$, of first order in $\lambda$ and at most $|\sin(\vartheta/2)|$ (nonzero at $32$ of $252$ events not later than the detection), in a unitary model and with no wave packet involved; argued from this, the gravitational size is at most $(Gm_{A}m_{B}/\hbar c)\,D|1/r_{1} - 1/r_{2}|$, $1.3 \times 10^{-13}$ in the proposed experiments, and no stored premise, the cutoff premises included, implies commutation or bounds the failure.
