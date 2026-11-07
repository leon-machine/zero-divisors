---
id: synthesis.clausius-is-window-first-law-plus-boost-charge-conservation
kind: claim
version: 3
title: 'Clausius from the window''s first law and boost-charge conservation'
status: proved
region: synthesis
subject: einstein
tags: [thermal-premises, boundary-modes, horizons, car-algebra, mode-counting, needs-continuum]
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
- name: Claude Opus 5.5
  role: notation pass, imaginary unit written as the geometric-algebra pseudoscalar
  version: 3
  source: maintainer pass 2026-11-07 (GA units)
review: draft
about:
- obj.hawking.boundary-mode-algebra-windows-boost-dynamics
- obj.hawking.continuum-mode-space
derivations:
- name: main
  uses:
  - synthesis.boundary-mode-first-law-of-entanglement@7
  - hawking.i-state@4
  - field-theory.second-quantisation@6
  - hawking.i-state-continuum@5
  - synthesis.boundary-mode-thermal-entropy@2
  - synthesis.residue-from-mode-entropy@4
  - synthesis.imported-null-plane-modular-hamiltonian-first-law@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_second_quantisation_carries_conservation
- kind: check
  ref: check.py::check_window_identity_and_joint_identity
- kind: check
  ref: check.py::check_detuned_coupling_breaks_clausius
- kind: check
  ref: check.py::check_zero_weight_window_absorbs_no_heat
- kind: check
  ref: check.py::check_horizon_boost_charge_chiral
- kind: check
  ref: check.py::check_continuum_carrier_boost_charge
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - synthesis.boundary-mode-first-law-of-entanglement
  - synthesis.hole-mass-is-ground-energy-label
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'The unit of the generator''s mode space (the continuum mode space, a GA-built mode space) is now written I_4: the stress density T_vv, the dilation generator h = kappa I_4(u d_u + 1/2), the Mellin modes u^{-1/2 + I_4 w} and the polarised boost-charge identity, numbers read in span{1, I_4}; no bare i remains.'
  maintainer_pass:
    by: maintainer-2026-10-23
    date: '2026-10-23'
    note: 'Version 2: clause (7)''s continuum first law now rests on the new imported Fact synthesis.imported-null-plane-modular-hamiltonian-first-law (Leon''s decision 14), added to uses and touched by check_continuum_carrier_boost_charge, so "argued, not proved" became "given the imported Fact" at every level and nothing stronger; and "zero weight (the registered residue)" now says one mode per counted unit, since under (Q) version 3 (weights kappa(k + 1/2)) the registered residue is also realised by two arrays at nonzero weight. Version 1 -> 2.'
  open_problem: ein.clausius-hypothesis
  note: >-
    A reduction of the Clausius hypothesis (H1) of the stored Einstein derivation, by standard statistical
    mechanics on the series' windows: with the temperature clause of the local-horizon premise read as a
    condition on the window's state before matter crosses, (H1) at first order follows from the window's
    first law and conservation of the total boost charge, window plus matter, by the joint dynamics of the
    patch (hypothesis (J) here), once the window's entropy change is read as eta delta A ((Loc) on the
    window). The defect is a relative entropy; clauses (2) and (3) are the standard entropy-production
    identities of quantum thermodynamics (Esposito, Lindenberg and Van den Broeck 2010; Reeb and Wolf 2014;
    cited from memory) in the present roles of window and matter; a detuned coupling (an exact model) shows (J) is not implied by
    the rest; and the zero-weight case, the registered residue read as one mode per counted unit, shows that the route is closed there on a
    fixed window (the heat must then change the mode set; its energy ledger under the every-instant
    reading of the temperature clause is the proposal synthesis.clausius-heat-exceeds-created-modes-killing-energy,
    filed alongside). Zero-weight windows lie outside the Definition's windows (whose weights are
    positive); clause (5) treats them as the limit at which the registered residue sits in its one-mode-per-unit reading. Matter's boost charge is the second quantisation dGamma(k) of the
    one-particle boost generator (field-theory.second-quantisation (3)); its identification with
    int T_ab chi^a dSigma^b for a general field is the standard Noether statement, cited from memory
    (Wald 1984, Weinberg 1995 ch. 7), and checked exactly here only for a chiral mode on a horizon
    generator. Clause (7), the series' form of a known result (the null-plane modular Hamiltonian is the
    boost charge of the field on the horizon), proves that if the patch's modes and the crossing matter are
    one field on the generators, the window's boost Hamiltonian and the matter's boost charge are one
    quadratic form, dGamma(h) = int chi^u T_uu du, so (J) holds identically. That the first law then holds
    for that field's entropy differences on the continuum follows given the imported Fact
    synthesis.imported-null-plane-modular-hamiltonian-first-law: the dilation generator has
    purely continuous spectrum, so the continuum carrier has no Gibbs windows of the store's Definition, and
    a point-spectrum discretisation replaces h by an h_d whose second quantisation is no longer the boost
    flux; the continuum statement is Araki's relative entropy with the null-plane modular Hamiltonian
    (Wall 2011; Casini, Teste and Torroba 2017; Faulkner et al. 2016; now imported as that Fact, checked
    against the sources), with entropy read as differences on a type III algebra. The state on that carrier is the stored continuum I-state; the
    proposal synthesis.positive-null-energy-gives-r-premises, filed alongside, derives it from positivity of
    the null translations (not cited as a premise). The local-horizon premise is named in the text but not used as a premise (no assumes edge):
    the theorem is conditional on the window's state, which the premise's temperature clause supplies.
    Transport-absent: statistical mechanics of the series' windows and the series' second quantisation.
---

## formal
Units $\hbar = c = 1$. Let $F$ be a window of the boundary-mode algebra with its boost dynamics (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}), $H_{F} = \sum_{j \in F}\omega_{j}N_{j}$ in the time of a boost field $\chi$ of surface gravity $\kappa$, $\beta = 2\pi/\kappa$, and $\rho_{I}$ the restriction to $F$ of the state of Theorem \claimref{hawking.i-state}, the Gibbs state of $\beta H_{F}$ (the state that the temperature clause (R$_{\mathrm{loc}}$) of the local-horizon premise prescribes for a patch's window before matter crosses). Let the matter be a second-quantised field over a finite-dimensional one-particle space $\mathfrak{h}_{m}$ (finitely many matter modes crossing the patch) with self-adjoint one-particle boost generator $k$, so that its boost charge is $d\Gamma(k)$, the $\mathrm{span}\{1, I_{4}\}$ part of $\Psi^{*}k\Psi$ (Theorem \claimref{field-theory.second-quantisation}(3)). A \emph{process} is a unitary $U$ on the joint Fock space applied to $\rho_{I} \otimes \rho_{m}$, $\rho_{m}$ any matter state; write $\rho'$ for the result, $\rho_{F}'$ and $\rho_{m}'$ for its marginals, $\delta Q := \Tr(\rho_{m}\,d\Gamma(k)) - \Tr(\rho_{m}'\,d\Gamma(k))$ for the boost energy the matter loses, $\Delta S_{F} := S(\rho_{F}') - S(\rho_{I})$, and $S(\cdot\,\|\,\cdot)$ for relative entropy. Consider the hypothesis
\begin{enumerate}
\item[(J)] \emph{(Boost-charge conservation.)} $U$ commutes with $H_{F}\otimes 1 + 1\otimes d\Gamma(k)$.
\end{enumerate}
Then:
\begin{enumerate}
\item \emph{(Conservation is a one-particle condition.)} $[d\Gamma(a), d\Gamma(b)] = d\Gamma([a, b])$, so a quadratic coupling $d\Gamma(v)$ on $\mathfrak{h}_{F} \oplus \mathfrak{h}_{m}$, with $H_{F} = d\Gamma(w)$, conserves the total boost charge if and only if $[v, w \oplus k] = 0$: it couples only modes of equal boost weight.
\item \emph{(Clausius from the first law.)} Under (J), $\Delta S_{F} = \beta\,\delta Q - S(\rho_{F}'\,\|\,\rho_{I})$ exactly. The defect is nonnegative, vanishes only for $\rho_{F}' = \rho_{I}$, and is of second order in $\rho_{F}' - \rho_{I}$. Hence $\Delta S_{F} = \delta Q/T_{\chi}$, $T_{\chi} = \kappa/2\pi$, at first order in the change of the window's state, and $\Delta S_{F} \le \delta Q/T_{\chi}$ always. (This is the standard first-law identity of a Gibbs state, combined with (J).)
\item \emph{(The matter's modular Hamiltonian reading.)} For every process, with or without (J), $\Delta S_{F} = \beta\,\delta Q + I(F{:}m)_{\rho'} + S(\rho_{m}'\,\|\,\sigma_{m}) - S(\rho_{m}\,\|\,\sigma_{m})$, where $\sigma_{m}$ is the Gibbs state of $\beta\,d\Gamma(k)$, whose modular Hamiltonian is $\beta\,d\Gamma(k)$ up to a constant (the boost-KMS state of the matter on the patch, when it exists), and $I(F{:}m)_{\rho'}$ is the mutual information created. Under (J) the defects balance: $S(\rho_{F}'\,\|\,\rho_{I}) + I(F{:}m)_{\rho'} = S(\rho_{m}\,\|\,\sigma_{m}) - S(\rho_{m}'\,\|\,\sigma_{m})$. (This is the standard entropy-production identity of a system coupled unitarily to a thermal state, with the window and the matter in the roles stated.)
\item \emph{(Without (J) the relation fails.)} For a window mode of weight $\omega_{F}$ coupled by number-conserving hopping to a matter mode of weight $\omega_{m} \neq \omega_{F}$, the first-order coefficients of $\Delta S_{F}$ and $\beta\,\delta Q$ are $\beta\omega_{F}\,\delta n$ and $\beta\omega_{m}\,\delta n$, $\delta n \neq 0$ the occupation transferred: the window's first law and its state hold, and (H1) fails. So (J) does not follow from the window's state and its first law.
\item \emph{(Zero weight.)} If every mode of $F$ has zero weight (a limit outside the windows of the Definition, whose weights are positive, admitted here because one realisation of the registered residue sits there), the case in which each counted unit is one mode carrying $\ln 2$ and the residue takes its registered value (Theorem \claimref{synthesis.residue-from-mode-entropy}; under the weight clause of version 3 of Premise (Q), $\omega_{k} = \kappa(k + \tfrac12)$, the registered value is also realised by two arrays per counted unit at nonzero weight, to which this clause does not apply), then $H_{F} = 0$, under (J) $\delta Q = 0$ for every process, and $\Delta S_{F} = -S(\rho_{F}'\,\|\,\rho_{I}) \le 0$: a fixed window of zero-weight modes absorbs no boost energy and its entropy can only fall. On that reading a nonzero heat can raise the horizon entropy only by changing the window's mode set, not through the first law of a fixed window.
\item \emph{(The boost charge on a generator.)} On a horizon generator with affine parameter $v$ and $\chi = \kappa v\,\partial_{v}$, a chiral mode $\psi(v)$ supported in the patch, with $T_{vv} = \tfrac{I_{4}}{2}(\bar\psi\psi' - \bar\psi'\psi)$ (the mode space's complex unit is the field theory's unit $I_{4}$, numbers read in $\mathrm{span}\{1, I_{4}\}$), has $\int \chi^{v}T_{vv}\,dv = \kappa\ip{\psi}{I_{4}(v\partial_{v} + \tfrac12)\psi}$: the boost flux through the generator is the expectation of the one-particle generator of dilations of $v$, whose second quantisation is the boost charge $d\Gamma(k)$ above.
\item \emph{(The continuum carrier: (J) as an identity; the first law there given the imported Fact.)} Let the patch's modes on a generator be the continuum mode space (Definition \claimref{obj.hawking.continuum-mode-space}) over $L^{2}(\R_{+}, du)\otimes K$, the half of the generator beyond the edge with affine parameter $u$ and $\chi = \kappa u\,\partial_{u}$, the boost acting as $\psi(u) \mapsto e^{\kappa t/2}\psi(e^{\kappa t}u)$ with one-particle generator $h = \kappa\,I_{4}(u\partial_{u} + \tfrac12)$ (eigenvalue $-\kappa w$ on $u^{-1/2 + I_{4}w}$), in the continuum I-state at $\beta$ (Theorem \claimref{hawking.i-state-continuum}). If the patch's modes and the matter crossing the patch are one field on these generators, then by the polarised form of (6) the window's boost Hamiltonian and the matter's boost charge are one quadratic form, $d\Gamma(h) = \int\chi^{u}T_{uu}\,du$, on modes vanishing at the edge, so (J) holds identically (proved). That the first law (2) then holds for that field's entropy differences on the continuum follows given the imported Fact \claimref{synthesis.imported-null-plane-modular-hamiltonian-first-law}: $h$ has purely continuous spectrum, so the continuum carrier has no Gibbs windows of the Definition (and a point-spectrum discretisation replaces $h$ by an operator whose second quantisation is no longer the boost flux), and the statement is Araki's relative-entropy form with the null-plane modular Hamiltonian $\beta\,d\Gamma(h) = 2\pi\int u\,T_{uu}\,du$, which by that Fact gives $\Delta S_{F} = \beta\,\delta Q - S(\rho_{F}'\,\|\,\rho_{I})$ for entropy differences, hence (2), on the type III algebra of the half-generator. This is the series' form of the known statement that the null-plane modular Hamiltonian is the boost charge of the field on the horizon. On modes shared by both sheets of an edge the temperature clause for both sheets forces zero weight, and then (5) applies instead.
\end{enumerate}
\emph{Consequence for the Einstein derivation.} If the patch's window is in the state above before matter crosses, (J) holds, the window's state changes at the order of the heat (so the defect of (2) is of order $\delta Q^{2}$, that is $\lambda_{0}^{4}$ in the patch of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, two orders beyond the balance), and the window's entropy change is the horizon's, $\eta\,\delta A$, then the Clausius hypothesis (H1) of that theorem holds at the order it is used, with $\delta Q$ the boost flux of the matter. The temperature clause is used here as a condition on the window's state before the crossing: by (2) and Klein's inequality the window's state after a process with $\delta Q \neq 0$ is not $\rho_{I}$, so the clause read as a condition at every instant on a fixed window is incompatible with (2).

## technical
Jacobson's Clausius relation, hypothesis (H1) of the stored derivation of Einstein's equations, is the step at which matter enters gravity. This result asks what the series' own objects supply toward it. The boundary-mode window of a local patch, in the state the temperature clause prescribes, is a Gibbs state of the boost Hamiltonian at inverse temperature $2\pi/\kappa$, so its modular Hamiltonian is $\beta H_{F}$ plus a constant and its entropy obeys the first law: the entropy change equals $\beta$ times the change of its boost energy, up to a relative-entropy defect of second order. The matter field is second-quantised, and its boost charge is the second quantisation of the one-particle boost generator; on a horizon generator this is exactly the boost flux $\int\chi^{v}T_{vv}\,dv$ of a chiral mode. The missing link is that the boost energy the matter loses is the boost energy the window gains. That is the hypothesis (J), and the reduction holds with the temperature clause read as the window's state before the crossing: the joint dynamics of matter and window conserves the total boost charge. Because second quantisation turns commutators of one-particle operators into commutators of their second quantisations, (J) for a quadratic coupling is a one-particle condition: the coupling joins only modes of equal boost weight. Given (J), the first law of the window, a standard identity of Gibbs states, is the Clausius relation at first order; (H1) itself then follows once the window's entropy change is read as $\eta\,\delta A$. Without (J) it fails: an exact two-mode model with a detuned coupling keeps the window's state and first law and breaks the relation at first order. A second reading puts the matter's stress tensor into a modular Hamiltonian: if the matter on the patch has a boost-KMS state, its modular Hamiltonian is $\beta$ times its boost charge, and for any process the window's entropy change is $\beta\,\delta Q$ plus the mutual information created plus the change of the matter's distance from that state; with (J) these defects balance exactly (the standard entropy-production identity of quantum thermodynamics). The zero-weight case, where one mode per counted unit sits at the registered residue (under the weight clause of (Q) version 3 the residue is also realised by two arrays at nonzero weight, which this case does not cover), is degenerate: the window's boost Hamiltonian vanishes, (J) then lets no boost energy in, and the window's entropy can only fall, so there the first-law route to (H1) is closed on a fixed window and heat can raise the horizon entropy only by changing the mode set (zero-weight windows are a limit outside the Definition's windows; the energy ledger of such a change, under the reading of the temperature clause at every instant, is the subject of synthesis.clausius-heat-exceeds-created-modes-killing-energy, filed alongside). On the continuum carrier of a generator, where the horizon modes and the crossing matter are one field, the window's boost Hamiltonian is the matter's boost charge, $d\Gamma(h) = \int\chi^{u}T_{uu}\,du$ as quadratic forms, so (J) is an identity there (proved; the series' form of the known statement that the null-plane modular Hamiltonian is the horizon boost charge). That the first law then holds for that field's entropy differences, leaving only the identification of the entropy change with $\eta\,\delta A$, follows given the imported Fact on the null-plane modular Hamiltonian and Araki's relative entropy (Wall; Casini, Teste and Torroba; Faulkner et al.): the dilation generator has no point spectrum, so there are no Gibbs windows on the continuum, and the first law there is the relative-entropy form that Fact supplies. The identities are checked exactly in two-mode models with rational Boltzmann factors and occupations, logarithms reduced to prime exponents. Transport-absent.

## lay
In Jacobson's derivation of Einstein's equations, the step where matter enters gravity is the assumption that the energy of matter falling across a small horizon raises the horizon's entropy by that energy divided by the temperature. This result asks whether the series' own quantum objects explain that step. The horizon's quantum modes, in the thermal state the series assumes, obey a standard law: their entropy rises by their energy gain divided by the temperature, up to a small correction. So the step follows if the energy matter loses is exactly the energy the horizon modes gain, that is, if the coupling between matter and horizon conserves the relevant energy (the boost energy). That conservation is the one extra ingredient, and an explicit small model shows it does not follow from the rest: a coupling that does not conserve it breaks the relation. If the horizon modes and the infalling matter are the same quantum field living on the horizon's light rays, the conservation is automatic, because the two energies are then one quantity; that the entropy law then carries over to that continuous setting follows given an imported fact of quantum field theory on light-like surfaces. Where the series' registered counting sits in its one-mode-per-unit reading, with horizon modes of zero energy, the route closes: such modes are already at maximum entropy and cannot absorb energy, so infalling matter can raise the horizon entropy only by adding new modes, which this mechanism does not describe.

## one-liner
Given the temperature clause as the window's thermal state before matter crosses, the Clausius relation $\delta S = \delta Q/T$ for the boost energy of matter follows at first order when the joint dynamics conserves the total boost charge (a one-particle resonance condition under second quantisation), fails in an exact detuned model, and at zero weight (the registered residue read as one mode per counted unit) cannot hold on a fixed window, whose entropy can then only fall; when the patch's modes and the matter are one field on the generators' continuum, (J) is an identity ($d\Gamma(h) = \int\chi^{u}T_{uu}\,du$), and the first law there (given the imported Fact on the null-plane modular Hamiltonian) leaves (Loc).
