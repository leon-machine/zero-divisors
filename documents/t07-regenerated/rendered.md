# Hawking Radiation from the Ledger: State, Continuum, Lift, and the Finite-Ledger Seam (regenerated from the store)

**Abstract.** This paper is a quantum companion to T5: it supplies the state, the continuum, and the four-dimensional lift between T5's single-mode core and the physical Hawking spectrum, each claim at its tier. Tier A: among the quasi-free states of the boundary modes' CAR algebra exactly one is KMS for the geometry's boost at the Hawking temperature, the I-state; existence is window-exact, carried to the full algebra by imported inductive-limit results; the KMS identity itself forces the pairing to vanish and the symbol to be Fermi-Dirac, all modes at once, extending T5's single-mode occupancy theorem; uniqueness beyond the class is the imported ideal-Fermi-gas theorem; and the statements carry to the continuum on a dense core. Tier B, the joints itemised: the helicity lift and greybody inheritance, whose only joint proved in this paper, the homogeneity $-2s-2$, is promoted to a stated result from inside the proof of the twistor paper's dictionary theorem; the exterior coincides with general relativity on the invertible region at $\Lambda = 0$, so the flux prediction equals Hawking's, filtering included. Tier A again: the finite mode space's deviations from the free-boson current algebra are edge-supported by an exact commutator identity; and, on the linear s-wave ladder of T5's premise (Q), an exact Planck factor with proven exponential window tails. The $\ell_P^2/A$ scale of generic corrections is a dimensional reading at modelling level; the per-observable scaling is open. Open and named: axiomatic selection of the dynamics, the lift beyond assembly, the Kerr continuum. Exact-arithmetic checks verify the identities.

## What we assume

**Postulate 1 (Joint J3: the s-wave reduction (modelling)).** The current boson of the s-wave theory is the s-wave reduction of each four-dimensional massless field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction: the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode.

**Postulate 2 (Premise (I): the interface identification).** The horizon-sector state feeds the exterior modes in the standard way, i.e.\ the occupancy of each near-horizon channel is carried to the corresponding asymptotic channel by the exterior propagation.

**Postulate 3 ((P): univalence).** Physical states of the boundary modes are even: $\omega \circ \alpha = \omega$, equivalently $\omega$ annihilates the odd sector $\Aod$.

**Postulate 4 ((Q): joint quasi-freeness, with the s-wave weights at the half-integer offset).** In the stationary idealisation of the boundary modes, and for this step alone, the joint state of the mode array is taken to be the gauge-invariant quasi-free state with the marginal data that (P) and (R) (Premise \claimref{singularity.r-regularity-fixed-locus}) fix unconditionally (Theorem \claimref{singularity.rate-discharge-hypothesis-iii}, Corollary \claimref{singularity.chains-state-class-stability}): writing $\psi_k$ for the fermion modes of the array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, its two-point function is $\langle \psi^\dagger_k \psi_l \rangle = \delta_{kl}\,n_k$, and every higher correlation function factorises by Wick's theorem, so that all connected correlators vanish and the joint state is KMS at $\beta = 2\pi/\kappa$ for the joint modular flow. The mode weights are evenly spaced with the array's sea level midway between two sites,
\[
\omega_k = \kappa\bigl(k + \tfrac12\bigr), \qquad k \in \Z ,
\]
so that no mode has zero weight, the weights are symmetric under the particle-hole relabelling $k \mapsto -1-k$, and the Killing flow at one modular period $2\pi/\kappa$ is the parity automorphism $\psi \mapsto -\psi$.

\emph{Why this offset.} The weights $\omega_k$ of Definition \claimref{obj.singularity.geometric-modular-condition-g} are fixed nowhere else in the framework: given (P), (R) and the quasi-free clause, an affine law $\omega_k = ck + d$ is what the currents' being normal modes of the boost flow requires, particle-hole symmetry leaves exactly two offset classes, $d = 0$ and $d = c/2$, and the slope is the value $\beta c = 2\pi$ (Theorem \claimref{synthesis.q-splits-maximum-entropy-affine-weights}(ii), (iv)). The class $d = c/2$ is adopted as a consequence of one reading, not as a bare premise: the array's modes are read as the discretised modes of the field theory's spinor fields on the horizon's light rays, $\psi(u) \mapsto e^{\kappa t/2}\psi(e^{\kappa t}u)$, of boost weight $\tfrac12$ (the weight at which the boost preserves the anticommutator), in the state that Premise \claimref{synthesis.n-plus-null-ground-state} (N$_{+}$) selects, a ground state for the affine null translations of the generators (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}). A field of boost weight $\tfrac12$ changes sign under a full turn of the regular Euclidean section, and $\kappa(k + \tfrac12)$ is the offset at which the array's Killing flow at one modular period carries that sign (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}). The reading is a decision, not a derivation: the Euclidean-period sign $R_{2\pi} = -1$ (Proposition \claimref{state-selection.where-fermi-dirac-comes}) holds in a KMS state of the array at either offset, so identifying the array's real-time recurrence at one period with it is part of the reading.

\emph{On the continuum.} The joint KMS part of this premise is not a separate assumption on the continuum mode space of a horizon's generators: there it follows from (N$_{+}$), whose null ground state restricts on either side of the edge to the continuum I-state at $\beta = 2\pi/\kappa$, jointly KMS and even (Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(ii), (iii)). The stationary array statement here is its point-spectrum discretisation, on which (N$_{+}$) itself cannot be posed (part (iv) there). The quasi-free clause is a hypothesis of (N$_{+}$) as well, and (N$_{+}$) does not give the weight clause.

\emph{Consequences of the offset.} At these weights one array carries exactly $\tfrac12\ln 2$ at the Hawking temperature, given the classical theta-function identities, so under the entropy-matching hypothesis two arrays carry the capacity $\ln 2$ of one registered boundary mode with no zero-weight mode (Theorem \claimref{synthesis.half-integer-weight-array-carries-half-ln2}(i), (iii)); the current sector of one array is one oscillator tower, one helicity channel, at either offset (Theorem \claimref{synthesis.array-ln2-is-zero-mode-doublet-one-tower}(ii), (iv)), so one registered mode then corresponds to two arrays and two helicity channels. Since every mode has nonzero weight, the gluing equation of Theorem \claimref{singularity.rate-discharge-hypothesis-iii} fixes $\beta$ at every mode of the array, and the zero-weight scopes of Theorems \claimref{singularity.descended-form-state-independent}, \claimref{singularity.universality-temperature-under-g} and \claimref{singularity.rate-discharge-hypothesis-iii} do not arise on it.

\emph{Version 2.} The source states the weight clause as $\omega_k = \kappa k$ with the sea level at $k = 0$, one mode of zero weight at which the gluing equation fixes $n_0 = \tfrac12$ but not $\beta$. Results computed under that offset refer to version 2.

**Postulate 5 ((R): regularity at the fixed locus).** For every mode $k$ and every pair $a, b$ of elements of its ladder $\{v_k, v_k^{*}\}$, the correlation function $F_{a,b}(t) := \omega\bigl(a\,\alpha_t(b)\bigr)$ of the Killing flow $\alpha_t = \operatorname{Ad}(e^{it\omega_k K_k})$, an entire function of $t$, continues in imaginary Killing time to a single-valued function on the regular Euclidean section of the Schwarzschild gravitational field on flat spacetime (Proposition \claimref{singularity.euclidean-section-period}; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}): its two orderings are the two sides of the cut, and they meet after one period,
\[
F_{a,b}\bigl(t + i\,p\bigr) \;=\; \omega\bigl(\alpha_t(b)\,a\bigr), \qquad p = \frac{2\pi}{\kappa} .
\]
In words: each single-mode marginal is KMS for the Killing flow at exactly the period the Euclidean section's smoothness at its tip dictates. The regularity is local, posed at the tip of the Euclidean section (a polar chart about the tip of the Wick-rotated flat background); for a state that is KMS for the Killing flow, this is also the period at which it is regular across the horizon locus in the Painlev\'e-Gullstrand chart.

\emph{Note (continuum restatement).} Posed on the continuum of the horizon's null generators (Definition \claimref{obj.hawking.continuum-mode-space}), the content of (R) for the eternal (Kruskal) hole follows from Premise \claimref{synthesis.n-plus-null-ground-state}: by Theorem \claimref{synthesis.positive-null-energy-gives-r-premises}(iii) the generators' modes are then jointly KMS for the Killing flow at $\beta = 8\pi M$. The wording above, on the ladders $\{v_{k}, v_{k}^{*}\}$ with a phase-acting flow, is a discretisation of that statement, recovered only for modes of vanishing Mellin width; (N$_{+}$) itself cannot be posed on point spectrum. A hole formed by collapse is not covered by (N$_{+}$), and (R) remains a premise. (The whole generator of the eternal horizon, which that case of (N$_{+}$) uses, lies beyond one flat chart; see that premise.)

## Introduction



**setting  (Introduction).** T5 of this series \cite{ButlerT5} computes a six-step chain from the Schwarzschild gauge field to the Page curve. Two of its links are deliberately minimal, and say so: single-mode thermality is proved from two named premises, (P) univalence and (R) the KMS condition at the geometric period, with the occupancy derived from the gluing identity \cite[Prems.~7.8 and 7.19, Thm.~7.20]{ButlerT5}; and the bosonic Planck sector is derived in the s-wave-reduced theory under a joint quasi-freeness premise \cite[Prem.~8.1]{ButlerT5}. Between that core and the physical Hawking spectrum stand four questions, and this paper answers them at their correct levels.

\emph{Which state?} the section ``The state input: the I-state'' proves the I-state theorem, the I-state being the series' name for the framework's distinguished equilibrium state $\omega_I$: among the quasi-free states of the CAR algebra of the boundary modes there is exactly one that is KMS for the geometry's boost at the Hawking temperature, and the KMS identity forces its two-point data outright, the pairing to zero and the symbol to Fermi-Dirac (Theorem \claimref{hawking.i-state}). T5 derives the single-mode occupancy the same way; the increment here is operator-level and simultaneous across all modes, with uniqueness inside the quasi-free class proved, and uniqueness beyond it imported with provenance. What is genuinely open is the \emph{selection} of the dynamics from a geometric axiom, and the section ``The state input: the I-state'' poses that open problem precisely, in the terms T5's own selection analysis fixes.

\emph{Which algebra carries the mode continuum?} the section ``The mode continuum'' extends the single-mode statements over the tower's CAR limit \cite{ButlerT3}: the finite-window statements are exact theorems, the inductive-limit results are imported as Facts with provenance, and the result is free-fermion thermal field theory as the algebra carrying the near-horizon boundary modes.

\emph{How does the two-dimensional core become four-dimensional radiation?} the section ``The four-dimensional lift'' assembles the lift with its joints itemised: helicity is the charge of the twistor storey (one level of the completion tower), and the Penrose homogeneity $-2s-2$ is proved from the ordering shift of the twistor paper \cite[Thm.~5.7]{ButlerT9} in Proposition \claimref{hawking.homogeneity-ordering-shift} (the computation appears inside that theorem's proof; the proposition promotes it to a stated result); greybody factors are inherited verbatim, because the series' exterior description coincides with general relativity on the invertible region at $\Lambda = 0$ \cite{ButlerT6}, so the flux prediction equals Hawking's, filtering included.

\emph{What does the finite boundary mode space change?} the section ``The finite boundary mode space, and the $\ell_P^2/A$ correction'' proves that the deviations of the finite boundary mode space from the infinite current algebra are edge-supported, with the exact edge identity and quantified tails: the corrections are area-suppressed at their proven rates, and the resulting $\ell_P^2/A$ correction is stated as a prediction. The Weinberg-Witten triage against the composite-graviton reading is recorded there as this paper's own claim.

**setting  (Prior art).** The prior work is acknowledged once, here. Hawking's radiance is \cite{Hawking1975}. The thermofield-double reading of the eternal black hole is Israel's \cite{Israel1976}; the identification of modular flow with the boost for wedge algebras is Bisognano-Wichmann \cite{BisognanoWichmann1976}, with Sewell's black-hole reading \cite{Sewell1982}. Quasi-free states of the CAR algebra and their two-point calculus are Araki's \cite{Araki1971}; KMS theory, the ideal Fermi gas, and the inductive-limit results are standard in Bratteli-Robinson \cite{BratteliRobinson1997}. The geometric-modular-action programme, the candidate axiom for state selection, is Buchholz-Dreyer-Florig-Summers \cite{BDFS2000}. The Penrose transform is \cite{Penrose1969, EPW1981}; greybody filtering through the Regge-Wheeler and Teukolsky barriers is \cite{ReggeWheeler1957, Teukolsky1973, Page1976}. The boson-fermion correspondence and the charge-zero Fock isomorphism are classical two-dimensional field theory \cite{FrenkelKac1980}. Weinberg-Witten is \cite{WeinbergWitten1980} and the soft-graviton universality is \cite{Weinberg1964}. What this paper claims as new is the transport assembly: the I-state theorem at the operator level, all modes at once, with pairing and symbol both forced by the KMS identity (the single-mode occupancy is derived the same way in \cite{ButlerT5}); the exact finite-window continuum statements and the limit with its imports declared; the promotion of the homogeneity computation inside the proof of \cite{ButlerT9}'s dictionary theorem to a stated result the transform can consume; the identification of the lift's remaining joints with theorems of this series (the exterior exactness of \cite{ButlerT6}); and the quantified edge-support of the finite-mode corrections.

**setting  (Contribution).** At the standard of \cite{ButlerT1}, with imports as Facts and the assembly joints itemised where a result is assembled.

\begin{enumerate}
\item The single-mode modular structure reproved self-contained, and the I-state theorem: existence of the quasi-free state whose modular clock is the geometry's clock, with gauge invariance and the Fermi-Dirac symbol both forced by the KMS identity, extending T5's single-mode derivation \cite[Thm.~7.20]{ButlerT5} to the full algebra, all modes at once; uniqueness beyond the quasi-free class as a corollary of the imported ideal-Fermi-gas theorem; the selection problem posed against T5's own analysis (the section ``The state input: the I-state'').
\item The continuum: exact finite-window KMS theorems, the inductive-limit assembly with its imports stated as Facts, free-fermion thermal field theory (the section ``The mode continuum'', Remark \claimref{note.hawking.free-fermion-thermal-field-theory-israels}).
\item The lift: the Penrose homogeneity $-2s-2$ stated and proved from the twistor paper's ordering shift (Proposition \claimref{hawking.homogeneity-ordering-shift}; the computation appears inside the proof of \cite[Thm.~5.7]{ButlerT9}, and is promoted here to a result the transform can consume), discharging the homogeneity half of the successor problem the twistor paper assigns to this paper, the transform itself staying open; the helicity lift and greybody inheritance assembled with every joint flagged, the interface premise (I) named in the statement (the section ``The four-dimensional lift'').
\item The $\ell_P^2/A$ correction: the exact edge identity for the finite window's current commutator, quantified tails, the area-suppressed reading, and the Weinberg-Witten triage (the section ``The finite boundary mode space, and the $\ell_P^2/A$ correction'').
\item Machine verification of the computational identities in exact arithmetic \cite{ButlerVerifyT7}.
\end{enumerate}

## Setting and imports



**setting  (Setting and imports).** Units are $G = c = \hbar = k_B = 1$ throughout, so for Schwarzschild the surface gravity is $\kappa = 1/4M$, the Hawking temperature is $\TH = \kappa/2\pi = 1/8\pi M$, the modular period is $\beta := 1/\TH = 8\pi M$, and areas are in Planck units, $\ell_P = 1$. (Two symbols are nonetheless kept visible where they carry the point: $\hbar$ in the section ``The four-dimensional lift'', where the ordering shift is a multiple of it, and $\ell_P$ in the section ``The finite boundary mode space, and the $\ell_P^2/A$ correction'', where the corrections scale as $\ell_P^2/A$, $A$ the horizon area.)

**setting  (The single mode, self-contained).** The unit of the boundary mode space is a completed null pair: vectors $v, v^*$ with $v^2 = (v^*)^2 = 0$ and $vv^* + v^*v = 1$, the ladder pair the transport principle adjoins \cite{ButlerT1}. Everything modular about a single mode is elementary and is proved here outright, per the series' standard.



**Theorem 6 (Modular structure of the completed pair).** Let $(v, v^*)$ be a completed pair and $\sigma := v^*v - vv^*$. Then:
\begin{enumerate}
\item $\sigma^2 = 1$; in the hyperbolic atom $\Cl(1,1)$ with $v = \tfrac12(e_0 + e_1)$, $v^* = \tfrac12(e_0 - e_1)$, one has $\sigma = e_0 e_1$: the unit boost bivector of the plane (relabelling the pair reverses the orientation);
\item the rotor flow $R_\lambda := \exp(\lambda\sigma/2)$ acts by $R_\lambda\, v\, R_\lambda^{-1} = e^{-\lambda}v$ and $R_\lambda\, v^*\, R_\lambda^{-1} = e^{+\lambda}v^*$: the pair diagonalises the boost with opposite weights;
\item the spectral projectors $\tfrac12(1 \pm \sigma)$ are the occupation projectors $v^*v$ and $vv^*$;
\item in the Fock representation the boost generator is the shifted number operator, $\tfrac12\sigma = N - \tfrac12$;
\item the bivector space of $\Cl(1,1)$ is one-dimensional, so the boost flow is the unique one-parameter rotor flow of the atom \emph{up to reparametrisation of the flow parameter and orientation}: the algebra fixes the orbits of any rotor-implemented modular flow, but not its speed, which is exactly the normalisation Remark \claimref{note.hawking.what-now-proved-open-problem} (the section ``The state input: the I-state'') leaves open.
\end{enumerate}

*Proof.* (1) $\sigma^2 = v^*vv^*v + vv^*vv^* - v^*v\,vv^* - vv^*\,v^*v = v^*v + vv^* - 0 - 0 = 1$, using $vv^*v = v$, $v^*vv^* = v^*$ and the vanishing squares. In $\Cl(1,1)$, by \claimref{std-algebra.vector-squares}: $v^*v = \tfrac14(e_0 - e_1)(e_0 + e_1) = \tfrac14(e_0^2 - e_1^2 + e_0e_1 - e_1e_0) = \tfrac14(1 + 1 + 2e_0e_1) = \tfrac12(1 + e_0e_1)$, so $\sigma = v^*v - vv^* = e_0e_1$ in this orientation; relabelling the pair reverses it. (2) From $vv^*v = v$ and the vanishing squares, $\sigma v = (v^*v - vv^*)v = -vv^*v = -v$ and $v\sigma = v(v^*v - vv^*) = vv^*v = +v$. The first relation gives $e^{\lambda\sigma/2}\,v = v\,e^{-\lambda\sigma/2}$ term by term in the exponential series, so $R_\lambda\, v\, R_\lambda^{-1} = v\,e^{-\lambda\sigma}$. Since $\sigma^2 = 1$, $e^{-\lambda\sigma} = \cosh\lambda - \sigma\sinh\lambda$ (\claimref{std-algebra.bivector-exponential}), and the second relation collapses it on the left factor: $v\,e^{-\lambda\sigma} = v(\cosh\lambda - \sinh\lambda) = e^{-\lambda}v$. The $v^*$ computation is the mirror image, with both signs reversed. (3) $\tfrac12(1 + \sigma) = \tfrac12(1 + v^*v - vv^*) = \tfrac12(v^*v + vv^* + v^*v - vv^*) = v^*v$, and likewise for the complement. (4) In the two-dimensional Fock module ($v^* = $ creation, $v = $ annihilation, $N = v^*v$): $\tfrac12\sigma = \tfrac12(v^*v - vv^*) = \tfrac12(N - (1 - N)) = N - \tfrac12$. (5) The bivector space of $\Cl(1,1)$ is the line $\R\,e_0e_1$, so every one-parameter rotor group is of the form $\lambda \mapsto \exp(c\lambda\sigma/2)$ for some real $c$: the same orbits at a rescaled parameter, which is the reparametrisation the statement reserves. The verification script checks every clause in exact arithmetic, including the finite conjugation of clause (2) at a rational rapidity.




**Fact (imported) 7 (Imported: modular descent, its premises, and the geometric normalisation (external ingredients)).** The results from outside the series on which \claimref{hawking.imported-modular-descent-premises-geometric-normalisation} draws, as cited there: J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math. Phys. 17 (1976), 303--321; G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states, Ann. Phys. 141 (1982), 201--224; W. Israel, Thermo-field dynamics of black holes, Phys. Lett. A 57 (1976), 107--110.

*Provenance:* J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math. Phys. 17 (1976), 303--321.; G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states, Ann. Phys. 141 (1982), 201--224.; W. Israel, Thermo-field dynamics of black holes, Phys. Lett. A 57 (1976), 107--110..



**Theorem 8 (Imported: modular descent, its premises, and the geometric normalisation).** Let the ascended algebra of a horizon pair carry a state that is pure, invariant under the boost flow of Proposition \claimref{hawking.modular-structure-completed-pair}, and entangling across the pair (cyclic and separating for the one-sided subalgebra). Then the descended state is KMS for the phase flow $\operatorname{Ad}(e^{it\sigma/2})$ of the same generator at \emph{some} inverse temperature $\beta \in \R$ of rapidity, and the hypotheses leave $\beta$ free, its sign included; the Gibbs \emph{form} of the descended state is state-independent. Positivity and the value are supplied by T5's named premises: under (P) univalence and (R) the KMS condition at the geometric period (one modular period equal to one rapidity period $2\pi$, i.e.\ Schwarzschild time $2\pi/\kappa$, the Euclidean period $8\pi M$), the descended state is Fermi-Dirac at $\beta = 2\pi$ of rapidity, which is the physical temperature $\TH = \kappa/2\pi = 1/8\pi M$; the boost plane is the one the shape operator scales by $-2$, and $\kappa = 1/4M$ is proved from the gauge field. Per mode of Schwarzschild frequency $\omega$ the reduced density matrix is the Fermi-Dirac matrix $\mathrm{diag}(1, e^{-\omega/\TH})/Z$. \emph{Provenance:} T5 \cite[Thms.~7.3 and 7.6, Prems.~7.8 and 7.19, Prop.~7.18, Thm.~7.20, Cor.~6.4]{ButlerT5}, with $\kappa = 1/4M$ from the gauge field in \cite[App.~A]{ButlerT5}; premise (R) is proved irreducible there, the temperature being no algebra-intrinsic quantity \cite[Thm.~7.16]{ButlerT5}. The wedge-modular mechanism is Bisognano-Wichmann-Sewell \cite{BisognanoWichmann1976, Sewell1982}, and the thermofield reading is Israel's \cite{Israel1976}.

*Proof.* Let the ascended algebra of a horizon pair carry a state that is pure, invariant under the boost flow of Proposition \claimref{hawking.modular-structure-completed-pair}, and entangling across the pair (cyclic and separating for the one-sided subalgebra). Then the descended state is KMS for the phase flow $\operatorname{Ad}(e^{it\sigma/2})$ of the same generator at \emph{some} inverse temperature $\beta \in \R$ of rapidity, and the hypotheses leave $\beta$ free, its sign included; the Gibbs \emph{form} of the descended state is state-independent. Positivity and the value are supplied by T5's named premises: under (P, \claimref{singularity.p-univalence}) univalence and (R, \claimref{singularity.r-regularity-fixed-locus}) the KMS condition at the geometric period (one modular period equal to one rapidity period $2\pi$, i.e.\ Schwarzschild time $2\pi/\kappa$, the Euclidean period $8\pi M$), the descended state is Fermi-Dirac at $\beta = 2\pi$ of rapidity, which is the physical temperature $\TH = \kappa/2\pi = 1/8\pi M$; the boost plane is the one the shape operator scales by $-2$, and $\kappa = 1/4M$ is proved from the gauge field. Per mode of Schwarzschild frequency $\omega$ the reduced density matrix is the Fermi-Dirac matrix $\mathrm{diag}(1, e^{-\omega/\TH})/Z$. \emph{Provenance:} T5 \cite[Thms.~7.3 and 7.6, Prems.~7.8 and 7.19, Prop.~7.18, Thm.~7.20, Cor.~6.4]{ButlerT5} (\claimref{singularity.modular-descent}, \claimref{singularity.euclidean-section-period}, \claimref{singularity.rate-discharge-hypothesis-iii}, \claimref{singularity.matching-steps-4b-4c-join-equation}, \claimref{singularity.descended-form-state-independent}), with $\kappa = 1/4M$ from the gauge field in \cite[App.~A]{ButlerT5}; premise (R) is proved irreducible there, the temperature being no algebra-intrinsic quantity \cite[Thm.~7.16]{ButlerT5} (\claimref{singularity.rate-rigidity-temperature-not-algebra-intrinsic}). The wedge-modular mechanism is Bisognano-Wichmann-Sewell \cite{BisognanoWichmann1976, Sewell1982}, and the thermofield reading is Israel's \cite{Israel1976}.

This restates \claimref{hawking.imported-modular-descent-premises-geometric-normalisation-external}, \claimref{singularity.computed}.




**Theorem 9 (Imported: the algebra of the boundary modes is the CAR algebra).** For even transport charge, the completed complexified limit of the tower of iterated completions is $\Cl(p,q)_\C \otimes \CAR$, the ground algebra tensored with the CAR algebra of countably many fermionic modes, and the mode operators are the adjoined null pairs themselves ($a_j = v_j^* = w_j$, $a_j^\dagger = v_j$, with the Fock adjointness). Here the \emph{transport charge} is the mod-8 invariant the tower's completions advance and the \emph{lineage} is the tower of iterated completions itself, both as in \cite{ButlerT3}; the physical lineage has charge six, so the theorem applies. \emph{Provenance:} the tower paper \cite[Prop.~4.1, Thms.~5.3 and 5.6]{ButlerT3}.

*Proof.* For even transport charge, the completed complexified limit of the tower of iterated completions is $\Cl(p,q)_\C \otimes \CAR$, the ground algebra tensored with the CAR algebra of countably many fermionic modes, and the mode operators are the adjoined null pairs themselves ($a_j = v_j$, $a_j^\dagger = v_j^*$, with the Fock adjointness). Here the \emph{transport charge} is the mod-8 invariant the tower's completions advance and the \emph{lineage} is the tower of iterated completions itself, both as in \cite{ButlerT3}; the physical lineage has charge six, so the theorem applies. \emph{Provenance:} the tower paper \cite[Prop.~4.1, Thms.~5.3 and 5.6]{ButlerT3} (\claimref{tower.algebraic-limit-even-charge}, \claimref{tower.car-limit-even-charge}, \claimref{tower.ladder-pairs-satisfy-car-vectors}).




**Fact (imported) 10 (Imported: the s-wave bosonic sector (external ingredients)).** The results from outside the series on which \claimref{hawking.imported-s-wave-bosonic-sector} draws, as cited there: I. B. Frenkel and V. G. Kac, Basic representations of affine Lie algebras and dual resonance models, Invent. Math. 62 (1980), 23--66.

*Provenance:* I. B. Frenkel and V. G. Kac, Basic representations of affine Lie algebras and dual resonance models, Invent. Math. 62 (1980), 23--66..



**Theorem 11 (Imported: the s-wave bosonic sector).** Two halves, at two levels. \emph{Unconditional:} on a window of the boundary mode space, the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, with an exact finite-window operator identity whose deviation is a difference of edge operators; and the bilinear subalgebra is globally invariant under the modular boost. \emph{Conditional on T5's Premise (Q), joint quasi-freeness with the s-wave weights:} the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature (an instance of Lemma \claimref{hawking.kms-restricts-invariant-subalgebras} below), giving the Bose-Einstein occupancy at $\TH$ for the s-wave sector; the linear weight assignment is the s-wave reduction's convention, adopted there as part of the premise. \emph{Provenance:} T5 \cite[Prem.~8.1, Thm.~8.2]{ButlerT5}; the correspondence itself is classical \cite{FrenkelKac1980}. The exact edge identity is reproved, in the form this paper needs, as Proposition \claimref{hawking.current-commutator-exactly-edge-split} below.

*Proof.* Two halves, at two levels. \emph{Unconditional:} on a window of the boundary mode space, the number-conserving bilinears (currents) satisfy the free-boson commutation relations exactly in the completed limit, with an exact finite-window operator identity whose deviation is a difference of edge operators; and the bilinear subalgebra is globally invariant under the modular boost. \emph{Conditional on T5's Premise (Q) (\claimref{singularity.q-joint-quasi-freeness-s-wave}), joint quasi-freeness with the s-wave weights:} the restriction of the Fermi-Dirac KMS state to the bilinear subalgebra is KMS at the same temperature (an instance of Lemma \claimref{hawking.kms-restricts-invariant-subalgebras} below), giving the Bose-Einstein occupancy at $\TH$ for the s-wave sector; the linear weight assignment is the s-wave reduction's convention, adopted there as part of the premise. \emph{Provenance:} T5 \cite[Prem.~8.1, Thm.~8.2]{ButlerT5} (\claimref{singularity.bosonisation-bridge-s-wave-sector}); the correspondence itself is classical \cite{FrenkelKac1980}. The exact edge identity is reproved, in the form this paper needs, as Proposition \claimref{hawking.current-commutator-exactly-edge-split} below.

This restates \claimref{hawking.imported-s-wave-bosonic-sector-external}.




**Theorem 12 (Imported: the exterior is exactly general relativity).** On the region where the gauge field is invertible, and at $\Lambda = 0$, the series' description coincides exactly with classical general relativity: the field equations are equivalent to the Einstein equations, and the vacuum equations are exactly the covariant constancy of the scale tractor. \emph{Provenance:} \cite[Fact 2.1, Thms.~4.5 and 4.7]{ButlerT6} (Thm.~4.7 is the complementary $\Lambda \neq 0$ case), resting on Lasenby-Doran-Gull's equivalence theorem.

*Proof.* On the region where the gauge field is invertible, and at $\Lambda = 0$, the series' description coincides exactly with classical general relativity: the field equations are equivalent to the Einstein equations, and the vacuum equations are exactly the covariant constancy of the scale tractor. \emph{Provenance:} \cite[Fact 2.1, Thms.~4.5 and 4.7]{ButlerT6} (\claimref{interior.covariant-form-vacuum-equations}, \claimref{interior.imported-equivalence-einstein-equations}) (Thm.~4.7 is the complementary $\Lambda \neq 0$ case), resting on Lasenby-Doran-Gull's equivalence theorem.




**Theorem 13 (Imported: the conformal storey (twistor storey), and the ordering shift).** The spinor module of the completed algebra $\Cl(2,4)$ is the conformal spinor space $\CS = \Cl^+(2,4)P$ (twistor space), of dimension $4$ over the complex unit $I_6$ (a \emph{storey} is the series' word for one level of the completion tower, as in \cite{ButlerT9}), the palatial commutation relation $[Z^\mu, \bar Z_\nu] = \hbar\,\delta^\mu_\nu$ on the quadratic (palatial) quantisation of the storey ($\bar Z$ the dual of $Z$ under the reversion form $h$), and, for $M \in \mathfrak{gl}(\CS)$, the symmetrised quadratic $q(M) := \tfrac12\bigl(Z^\mu M_\mu^{\ \nu}\bar Z_\nu + \bar Z_\nu M_\mu^{\ \nu} Z^\mu\bigr)$. (Indices on $\CS$ are written $\mu, \nu$ throughout; $\alpha$ and $\beta$ are reserved for the modular dynamics and its inverse temperature.) Symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator $q(\id)$ by $-\hbar/2$ per complex dimension of $\CS$, totalling $-2\hbar$ (equivalently, $q(M) = \sum M_\mu^{\ \nu} Z^\mu \bar Z_\nu - \tfrac{\hbar}{2}\tr M$); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$, a shift of minus one half per fermionic mode: the two storeys carry the same signed ordering shift. \emph{Provenance:} the correspondence paper \cite[Thm.~3.1, Rem.~3.2, \S 5, Lem.~5.5, Prop.~5.6, Thm.~5.7]{ButlerT9}; the homogeneity consequence is computed inside the proof of its Theorem 5.7 and is promoted to a stated result as Proposition \claimref{hawking.homogeneity-ordering-shift} below.

*Proof.* The spinor module of the completed algebra $\Cl(2,4)$ is the conformal spinor space $\CS = \Cl^+(2,4)P$ (twistor space), of dimension $4$ over the complex unit $I_6$ (a \emph{storey} is the series' word for one level of the completion tower, as in \cite{ButlerT9}), the palatial commutation relation $[Z^\mu, \bar Z_\nu] = \hbar\,\delta^\mu_\nu$ on the quadratic (palatial) quantisation of the storey ($\bar Z$ the dual of $Z$ under the reversion form $h$), and, for $M \in \mathfrak{gl}(\CS)$, the symmetrised quadratic $q(M) := \tfrac12\bigl(Z^\mu M_\mu^{\ \nu}\bar Z_\nu + \bar Z_\nu M_\mu^{\ \nu} Z^\mu\bigr)$. (Indices on $\CS$ are written $\mu, \nu$ throughout; $\alpha$ and $\beta$ are reserved for the modular dynamics and its inverse temperature.) Symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator $q(\id)$ by $-\hbar/2$ per complex dimension of $\CS$, totalling $-2\hbar$ (equivalently, $q(M) = \sum M_\mu^{\ \nu} Z^\mu \bar Z_\nu - \tfrac{\hbar}{2}\tr M$); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$, a shift of minus one half per fermionic mode: the two storeys carry the same signed ordering shift. \emph{Provenance:} the correspondence paper \cite[Thm.~3.1, Rem.~3.2, \S 5, Lem.~5.5, Prop.~5.6, Thm.~5.7]{ButlerT9} (\claimref{correspondence.fock-model-complexified-ascended-algebra}, \claimref{correspondence.clifford-side-ordering-shift}, \claimref{correspondence.symmetrised-quadratics-palatial-algebra}, \claimref{correspondence.shared-core-ordering-dictionary}); the homogeneity consequence is computed inside the proof of its Theorem 5.7 and is promoted to a stated result as Proposition \claimref{hawking.homogeneity-ordering-shift} below.




**Definition 14 (The boundary-mode algebra, windows, and the boost dynamics).** Fix a countable mode set $J$ with Schwarzschild frequencies $\omega_j > 0$ ($j \in J$), the frequencies the geometry assigns to the boundary modes (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}). \emph{Provenance of $J$:} the boundary modes are the ladder pairs of the blown-up singular boundary, one per point, aggregated over the s-wave channels into the countable array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}, an identification the singularity paper makes and flags. By convention here (it is in neither the singularity paper nor the thermality paper, and reconciles the array's weights $\kappa k$, $k \in \mathbb{Z}$, with $\omega_j > 0$), the modes below the level enter $J$ through their particle-hole conjugates, so that every frequency is positive, and the one zero-frequency mode of the array lies outside $J$; the bookkeeping is filed alongside (synthesis.s-wave-array-is-a-boundary-mode-set). The tower of iterated completions is the algebra's model, not the source of its countability: its limit is the CAR algebra with the adjoined null pairs as modes (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), while on the physical closure one ascent completes the description and further rungs lie on shadow walls outside the physical region (Corollary \claimref{tower.answers-iteration-question}). The \emph{boundary-mode algebra} $\mathfrak{A}$ is the CAR algebra over $\ell^2(J)$ (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), the C*-inductive limit of the \emph{window algebras} $\mathfrak{A}_F$, $F \subset J$ finite, each $\mathfrak{A}_F \cong \End(\Lambda^\bullet \C^F)$ of dimension $4^{|F|}$. The \emph{boost dynamics} is the one-parameter group $\tau_t$ acting on generators by $\tau_t(a_j) = e^{-i\omega_j t}\,a_j$, with $t$ Schwarzschild time: the quasi-free flow whose one-particle Hamiltonian is $h = \mathrm{diag}(\omega_j)$; it preserves every window. In rapidity $\lambda = \kappa t$ the same flow has boost weights $\omega_j/\kappa$ and modular temperature $2\pi$ (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); in Schwarzschild time the inverse temperature is $\beta = 1/\TH = 2\pi/\kappa$, and this normalisation is used throughout.

## The state input: the I-state



**setting  (The state input: the I-state).** T5 proves single-mode thermality from its premises (P) and (R), deriving the occupancy from the gluing identity, and says exactly what is premised. This section lifts the statement to the full mode algebra: within the quasi-free class the state is unique and its two-point data are forced outright, all modes at once; given the dynamics, even the class restriction can be removed, by a theorem of the literature; what cannot yet be derived is the dynamics-selection axiom itself, and that open problem is posed at the end, against T5's own selection analysis.

**setting  (Two elementary lemmas).** We write $\alpha_t$ for a finite-dimensional dynamics; on a window $F$ the relevant instance is $\alpha_t = \tau_t|_{\mathfrak{A}_F}$, generated by $H_F$, the second quantisation of $h|_F$.



**Theorem 15 (Gibbs states are KMS, and conversely, in finite dimensions).** Let $\mathfrak{B} = \End(\C^m)$, let $H$ be diagonal in the basis $(\xi_a)$ with eigenvalues $\lambda_a$, all distinct or not, let $\alpha_t = \mathrm{Ad}(e^{itH})$, and $\beta \in \R$. Then the Gibbs state $\omega_G(x) := \tr(e^{-\beta H}x)/\tr(e^{-\beta H})$ satisfies the KMS identity
\[
\omega_G(x\,y) \;=\; \omega_G\bigl(y\,\alpha_{i\beta}(x)\bigr), \qquad \alpha_{i\beta}(x) := e^{-\beta H}x\,e^{\beta H},
\]
for all $x, y$; and it is the \emph{unique} $\alpha$-KMS state at $\beta$ on $\mathfrak{B}$, degenerate spectrum included.

*Proof.* The identity is cyclicity of the trace:
\[
\omega_G\bigl(y\,\alpha_{i\beta}(x)\bigr) = \tr\bigl(e^{-\beta H}y\,e^{-\beta H}x\,e^{\beta H}\bigr)/Z = \tr\bigl(e^{-\beta H}xy\bigr)/Z = \omega_G(xy),
\]
the trailing $e^{\beta H}$ moved around the trace to cancel the inner factor. Conversely write $\omega(x) = \tr(\rho x)$ and evaluate the KMS identity on matrix units $x = E_{ab}$, $y = E_{cd}$: since $\alpha_{i\beta}(E_{ab}) = e^{-\beta(\lambda_a - \lambda_b)}E_{ab}$ and $\tr(\rho\,E_{ab}E_{cd}) = \delta_{bc}\,\rho_{da}$, the identity reads
\[
\delta_{bc}\,\rho_{da} \;=\; e^{-\beta(\lambda_a - \lambda_b)}\,\delta_{da}\,\rho_{bc}
\qquad \text{for all } a, b, c, d.
\]
Taking $c = b$ and $d = a$ gives $\rho_{aa} = e^{-\beta(\lambda_a - \lambda_b)}\rho_{bb}$: Gibbs ratios between all diagonal entries. Taking $c = b$ and $d \neq a$ gives $\rho_{da} = 0$ (the right side carries $\delta_{da} = 0$), for every pair $d \neq a$, degenerate eigenvalues included: $\rho$ is diagonal. So $\rho = e^{-\beta H}/Z$, and the KMS state is unique. The verification script performs the solve symbolically for the mode algebra $\Mat_2$ with $H = \omega N$ and confirms both clauses as identities of rational functions in the Boltzmann factor.




**Theorem 16 (KMS restricts to invariant subalgebras).** If $\omega$ is $\alpha$-KMS at $\beta$ on $\mathfrak{B}$ and $\mathfrak{C} \subseteq \mathfrak{B}$ is a unital subalgebra with $\alpha_t(\mathfrak{C}) = \mathfrak{C}$, then $\omega|_{\mathfrak{C}}$ is KMS at $\beta$ for $\alpha|_{\mathfrak{C}}$.

*Proof.* For $x, y \in \mathfrak{C}$ the correlation function $t \mapsto \omega(y\,\alpha_t(x))$ is computed entirely from elements of $\mathfrak{C}$ (invariance keeps $\alpha_t(x) \in \mathfrak{C}$), and is the same function of $t$ whether $x, y$ are regarded in $\mathfrak{C}$ or in $\mathfrak{B}$. Its continuation to the closed strip is unique (a function analytic on the strip and continuous on its closure is determined by its boundary restriction to the real line, by uniqueness of analytic continuation), so the strip function and the KMS boundary identity transfer verbatim from $\mathfrak{B}$ to $\mathfrak{C}$.




**Fact (imported) 17 (Imported: quasi-free states of the CAR algebra).** For every operator $A$ on $\ell^2(J)$ with $0 \le A \le 1$ (the \emph{symbol}) there is a unique gauge-invariant state $\omega_A$ on $\mathfrak{A}$ with two-point function $\omega_A(a^\dagger(f)\,a(g)) = \ip{g}{Af}$ and all higher truncated functions zero (Wick determinants). More generally, a quasi-free state (all truncated functions beyond second order vanishing) is determined by its full two-point data, the symbol together with the pairing $P(f, g) := \omega(a^\dagger(f)\,a^\dagger(g))$, and gauge invariance is exactly $P = 0$. On a finite window with diagonal symbol this is the explicit product state $\bigotimes_j \rho_j$, $\rho_j = \mathrm{diag}(1 - n_j,\, n_j)$ in the occupation basis, which the script realises exactly. \emph{Provenance:} Araki \cite{Araki1971}; \cite[\S 5.2]{BratteliRobinson1997}.

*Provenance:* H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.2.



**Fact (imported) 18 (Imported: KMS passes to inductive limits).** Let a C*-algebra be the closure of an increasing union of subalgebras, each globally invariant under a one-parameter dynamics, and let a state be KMS at $\beta$ on each subalgebra for the restricted dynamics. Then the state is KMS at $\beta$ on the whole algebra: the analytic-element requirement is checked on the dense union and passes to the closure. \emph{Provenance:} \cite[Prop.~5.3.25]{BratteliRobinson1997}.

*Provenance:* O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., Prop.~5.3.25.



**Fact (imported) 19 (Imported: quasi-free KMS reduces to the two-point level).** For the CAR algebra over a one-particle space with the quasi-free dynamics of a self-adjoint one-particle Hamiltonian, a gauge-invariant quasi-free state is KMS at $\beta$ if and only if its two-point function satisfies the two-point KMS identity: through the Wick-determinant structure, the analytic-continuation requirement for products of generators reduces to the two-point level. \emph{Provenance:} Araki \cite{Araki1971}; \cite[\S 5.3]{BratteliRobinson1997}.

*Provenance:* H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.3.



**Theorem 20 (The I-state).** Consider the boundary-mode algebra with its boost dynamics (Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics}) at inverse temperature $\beta = 1/\TH = 2\pi/\kappa$.
\begin{enumerate}
\item \emph{(Existence, exactly on windows.)} The quasi-free state $\omega_I$ with the Fermi-Dirac symbol
\[
A_I \;=\; \bigl(1 + e^{\beta h}\bigr)^{-1}, \qquad\text{i.e.}\qquad n_j = \frac{1}{e^{\omega_j/\TH} + 1},
\]
restricts on every window to the Gibbs state of $H_F = \sum_{j \in F}\omega_j N_j$ and is KMS there, exactly (Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite}); it is the unique quasi-free extension of these window states, and it is $\tau$-KMS at $\beta$ on the full algebra by Fact \claimref{hawking.imported-kms-passes-inductive-limits}.
\item \emph{(Gauge invariance is forced.)} If a quasi-free state of $\mathfrak{A}$ is $\tau$-KMS at $\beta$, its pairing vanishes: the state is gauge-invariant automatically.
\item \emph{(The symbol is derived.)} Its symbol then satisfies the operator identity $A(1 + e^{-\beta h}) = e^{-\beta h}$, equivalently $A = e^{-\beta h}(1 - A)$, whence $A = A_I$: within the quasi-free class, the state whose modular clock is the geometry's clock is unique, and its two-point data are forced.
\end{enumerate}

*Proof.* (1) On a window $F$, the quasi-free state with diagonal symbol is the product state of Fact \claimref{hawking.imported-quasi-free-states-car-algebra} with $n_j = (1 + e^{\beta\omega_j})^{-1}$, which is exactly the Gibbs density matrix of $H_F$: $e^{-\beta H_F} = \bigotimes_j \mathrm{diag}(1, e^{-\beta\omega_j})$, normalised; the script builds the two sides independently and confirms the identity in exact arithmetic. Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite} gives the KMS identity on the window, exactly; the script verifies it on a three-mode window at rational Boltzmann factors, on a spanning set of pairs. The windows are nested with dense union and the dynamics preserves each, so Fact \claimref{hawking.imported-kms-passes-inductive-limits} passes the KMS property to $\mathfrak{A}$.
(2) Apply the KMS identity to the pair $x = a^\dagger(f)$, $y = a^\dagger(g)$, with $f, g$ supported in windows (so that $\alpha_{i\beta}(a^\dagger(f)) = a^\dagger(e^{-\beta h}f)$ is again a generator):
\[
P(f, g) \;=\; \omega\bigl(a^\dagger(f)\,a^\dagger(g)\bigr) \;=\; \omega\bigl(a^\dagger(g)\,a^\dagger(e^{-\beta h}f)\bigr) \;=\; P(g,\, e^{-\beta h}f).
\]
Antisymmetry of creation operators gives $P(f, g) = -P(g, f)$, so $P(g, (1 + e^{-\beta h})f) = 0$ for all $f, g$ in the dense span of the windows; $1 + e^{-\beta h}$ is bounded with bounded inverse and preserves that span, so $P = 0$.
(3) Apply the KMS identity to the pair $x = a^\dagger(f)$, $y = a(g)$:
\[
\omega\bigl(a^\dagger(f)\,a(g)\bigr) \;=\; \omega\bigl(a(g)\,a^\dagger(e^{-\beta h}f)\bigr)
\;=\; \ip{g}{e^{-\beta h}f} - \omega\bigl(a^\dagger(e^{-\beta h}f)\,a(g)\bigr),
\]
using the CAR $\{a(g), a^\dagger(f')\} = \ip{g}{f'}$. In symbols: $\ip{g}{Af} = \ip{g}{e^{-\beta h}f} - \ip{g}{Ae^{-\beta h}f}$ for all $f, g$ supported in windows, i.e.\ $A(1 + e^{-\beta h}) = e^{-\beta h}$ on the dense span, i.e.\ $A = e^{-\beta h}(1+e^{-\beta h})^{-1} = (1 + e^{\beta h})^{-1} = A_I$ (all four operators bounded, $h \ge 0$ here). By (2) and Fact \claimref{hawking.imported-quasi-free-states-car-algebra}, the state is determined by its two-point data, which are forced, so $\omega = \omega_I$. The mode-diagonal scalar identity $n = e^{-\beta\omega}(1-n)$, equivalently the detailed balance $n/(1-n) = e^{-\beta\omega}$, is checked by the script as an exact identity of rational functions.




**Fact (imported) 21 (Imported: ideal-Fermi-gas uniqueness).** For the CAR algebra over a one-particle space with self-adjoint $h$ and the induced quasi-free dynamics, the $\beta$-KMS state is unique and equals the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$. \emph{Provenance:} \cite[Ex.~5.3.2 and \S 5.3]{BratteliRobinson1997}; the quasi-free calculus is \cite{Araki1971}.

*Provenance:* O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., Ex.~5.3.2 and \S 5.3; H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442..



**Theorem 22 (Full uniqueness, given the dynamics).** Among all states of $\mathfrak{A}$, $\omega_I$ is the unique $\tau$-KMS state at $\beta$.

*Proof.* Fact \claimref{hawking.imported-ideal-fermi-gas-uniqueness}, whose hypotheses Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} satisfies; the quasi-free state it names has symbol $A_I$, which is $\omega_I$ by Fact \claimref{hawking.imported-quasi-free-states-car-algebra}.


**Remark  (What is now proved, and the open problem).** Three levels, stated separately. \emph{Proved here:} within the quasi-free class the state is unique, with gauge invariance and the Fermi-Dirac symbol both forced by the KMS identity (Theorem \claimref{hawking.i-state}); in this sense the I-state is the framework's equilibrium vacuum, and the quasi-free restriction is a convenience of proof, removed at the next level. \emph{Imported:} given the boost dynamics and $\beta$, full uniqueness among all states (Corollary \claimref{hawking.full-uniqueness-given-dynamics}, from Fact \claimref{hawking.imported-ideal-fermi-gas-uniqueness}). \emph{Open, and named:} deriving the dynamics itself, i.e.\ an axiom selecting the boost flow and its temperature from the geometry. T5 has already treated this question at the level of a single factor: its geometric modular condition (G) is formulated and rejected there as over-determining the boundary modes, its premise (R) is proved irreducible, its rate-rigidity theorem shows the temperature is not algebra-intrinsic, and the resulting state class is recorded \cite[Def.~7.12, Thms.~7.16 and 7.28, Cor.~7.32]{ButlerT5}. The question this paper poses is different and remains open: a \emph{net-level} selection in the style of geometric modular action \cite{BDFS2000}, demanding that the modular groups of a net of boundary-mode algebras act geometrically and deriving the boost identification for the whole net rather than assuming it. Within the single atom the algebra already forces the orbits of any rotor-implemented flow, though not its speed (Proposition \claimref{hawking.modular-structure-completed-pair}(5)); the execution for the net is a successor problem (the section ``Scope, and successor problems''). \emph{Point of contact:} the I-state on a horizon pair is Israel's thermofield double \cite{Israel1976}, and its GNS representation is the Araki-Wyss doubling; the non-equilibrium state of the descent, the cosmological state problem, is outside this paper's scope (successor problem 5).

## The mode continuum



**setting  (The mode continuum).** The boundary mode space of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} has countably many modes because the boundary modes, the ladder pairs of the blown-up singular boundary, one per point, are aggregated over the s-wave channels into the countable array of Theorem \claimref{singularity.bosonisation-bridge-s-wave-sector}. The tower of iterated completions is the algebra's model, not the source of the count: its limit is the CAR algebra with the adjoined null pairs as modes (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}), while on the physical closure one ascent completes the description (Corollary \claimref{tower.answers-iteration-question}). The physical spectrum is emitted into a continuum of frequencies and a tower of angular channels, and this section carries the state theorem across that idealisation with the levels declared: what is exact, what is an inductive-limit result, and what is a modelling identification are separated.



**Definition 23 (Continuum mode space).** Let $\mathfrak{h}$ be a separable complex Hilbert space (the one-particle space; for the Schwarzschild s-wave sector, $L^2(\R_+, d\omega)$; with angular channels, a direct sum of copies indexed by $(\ell, m)$ and species), and let $h$ be self-adjoint on $\mathfrak{h}$ (the one-particle Hamiltonian of Schwarzschild time; for the s-wave sector, multiplication by the frequency $\omega$; self-adjointness, not positivity, is what the theorems below use, and the section ``The finite boundary mode space, and the $\ell_P^2/A$ correction'''s bilateral ladder is an instance with spectrum unbounded below). The \emph{continuum mode space} is the CAR algebra $\CAR(\mathfrak{h})$ with the quasi-free (Bogoliubov) dynamics $\tau_t(a(f)) = a(e^{ith}f)$. The countable mode space of Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics} is the case $\mathfrak{h} = \ell^2(J)$; the CAR functor turns isometric inclusions of one-particle spaces into unital embeddings of algebras, so refining the tower's mode set into a dense subset of the continuum realises $\CAR(\mathfrak{h})$ as the completed union of tower-type subalgebras: the continuum is the tower's limit re-parametrised, not a new object.



**Theorem 24 (The I-state on the continuum).** For the continuum mode space at $\beta = 2\pi/\kappa$, with $h$ self-adjoint:
\begin{enumerate}
\item the quasi-free state $\omega_I$ with symbol $A_I = (1 + e^{\beta h})^{-1}$ is $\tau$-KMS at $\beta$: the two-point KMS identity is the computation of clause (3) run in reverse on the core, and Fact \claimref{hawking.imported-quasi-free-kms-reduces-two} lifts it from the two-point level to the state. When $h$ has pure point spectrum, the finite spectral windows (spans of finitely many eigenvectors) are literal instances of the section ``The state input: the I-state'''s exact window theorem, proved outright; this is the case of the tower's mode space, Definition \claimref{obj.hawking.boundary-mode-algebra-windows-boost-dynamics};
\item the pairing of any quasi-free $\tau$-KMS state vanishes, by the computation of Theorem \claimref{hawking.i-state}(2) performed on the core of clause (3);
\item the symbol derivation holds verbatim on the core: for $f$ in a bounded spectral subspace of $h$ (their union over cut-offs is a dense, $\tau$-invariant core on which $e^{-\beta h}f$ is defined and $a^\dagger(f)$ is entire analytic for $\tau$), the KMS identity forces $\ip{g}{A(1 + e^{-\beta h})f} = \ip{g}{e^{-\beta h}f}$, hence $A = A_I$ on the core and, $A$ and $A_I$ both bounded, everywhere: within the quasi-free class the continuum I-state is unique with derived two-point data. ($e^{-\beta h}$ may be unbounded when $h$ is unbounded below; the identity is only ever used on the core, and $A_I$ is bounded for every self-adjoint $h$.)
\end{enumerate}
Fact \claimref{hawking.imported-ideal-fermi-gas-uniqueness} is stated for general self-adjoint $h$, so Corollary \claimref{hawking.full-uniqueness-given-dynamics} also holds verbatim for the continuum mode space: among all states, $\omega_I$ is the unique $\tau$-KMS state.

*Proof.* (3) is the computation of Theorem \claimref{hawking.i-state}(3) with the stated core in place of the window span: the core is $\tau$-invariant, $e^{-\beta h}$ preserves it and is bounded on it, and density plus boundedness of $A$ and $A_I$ extend the bounded identity $A = A_I$ from the core to $\mathfrak{h}$; the unbounded identity is used only on the core, where $1 + e^{-\beta h}$ acts bijectively. (2) is Theorem \claimref{hawking.i-state}(2) on the same core. (1): the state $\omega_{A_I}$ exists for the symbol $0 \le A_I \le 1$ (Fact \claimref{hawking.imported-quasi-free-states-car-algebra}); its two-point function satisfies the two-point KMS identity by (3) read backwards, and Fact \claimref{hawking.imported-quasi-free-kms-reduces-two} upgrades the two-point identity to the KMS property of the state. What this paper certifies independently, and the script checks exactly, is the window case, where no imported calculus is needed. The closing uniqueness clause rests on \claimref{hawking.imported-ideal-fermi-gas-uniqueness}, which gives a unique $\beta$-KMS state, the quasi-free state with symbol $(1 + e^{\beta h})^{-1}$, for any self-adjoint $h$.




**Fact (imported) 25 (Imported: the thermal representation).** The GNS representation of $\CAR(\mathfrak{h})$ in the state $\omega_I$ is the Araki-Wyss representation: a doubled Fock space carrying two commuting copies of the CAR, with the GNS vector entangling them pairwise and the modular operator of the GNS vector implementing exactly the flow $\tau$ at inverse temperature $\beta$. \emph{Provenance:} Araki-Wyss \cite{ArakiWyss1964}; textbook form \cite[\S 5.3]{BratteliRobinson1997}.

*Provenance:* H. Araki and W. Wyss, Representations of canonical anticommutation relations, Helv. Phys. Acta 37 (1964), 136--159.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.3.

**Remark  (Free-fermion thermal field theory, and Israel's double).** Fact \claimref{hawking.imported-thermal-representation} is the continuum instance of T5's single-mode picture: the doubling is the completed pair structure mode by mode, the GNS vector is the thermofield double, and the modular flow is the boost. ``Free-fermion thermal field theory as the algebra carrying the mode continuum'' is now a theorem-backed description: the algebra is $\CAR(\mathfrak{h})$ (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra} plus Definition \claimref{obj.hawking.continuum-mode-space}), the state is the I-state (Theorem \claimref{hawking.i-state-continuum}), and the representation it generates is the standard thermal one. \emph{Point of contact:} Israel's thermofield reading of the eternal black hole \cite{Israel1976} is exactly this representation with the second copy read as the far wedge; T5's eviction dynamics runs inside it.

**Remark  (Which dynamics, and at what level).** The one-particle Hamiltonian $h$ was supplied by the geometry: the Schwarzschild frequency of each boundary mode, with the temperature's coefficient fixed by the surface gravity (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); in rapidity the weights are $\omega/\kappa$ at modular temperature $2\pi$. Two notes on scope. First, the greybody filtering of the section ``The four-dimensional lift'' does \emph{not} deform $h$ or the KMS structure: transmission through the exterior barrier is a property of the propagation from the horizon to infinity, not of the horizon algebra; conflating the two is what the interface premise (I) of Assembly \claimref{hawking.greybody-inheritance-under-interface-premise} guards against, and it is named in that assembly's statement. Second, the identification of the mode set (which $(\omega, \ell, m)$ channels, with which degeneracies) is a modelling input from the standard near-horizon reduction; the theorems of this section are exact for whatever separable $(\mathfrak{h}, h)$ that input delivers; the algebra supplies the theorems and the physics supplies the input.

## The four-dimensional lift



**setting  (The four-dimensional lift).** The results so far are stated for the boundary modes, in the effectively two-dimensional near-horizon theory whose unit is the hyperbolic atom. The physical spectrum is four-dimensional radiation sorted by helicity and angular momentum and filtered by the exterior geometry. This section assembles the lift. It is the paper's principal assembly section, its Tier B, and the helicity assembly's joints are itemised by name so that each carries its own provenance: one joint is a classical theorem, one is a theorem of this series completed in Proposition \claimref{hawking.homogeneity-ordering-shift} below, and one is modelling, flagged as such; the greybody assembly itemises three more and adds one named premise, (I), its only non-theorem joint. What the lift does and does not claim is bounded in Remark \claimref{note.hawking.what-lift-does-does-not-claim}.



**Fact (imported) 26 (Imported: the Penrose transform).** Massless free fields of helicity $s$ on (suitably convex regions of complexified) Minkowski space (complexified with the unit $I_4$, points $u + I_4 w$) are in natural isomorphism with the first cohomology of the corresponding region of the conformal spinor space $\CS$ (twistor space) with coefficients in $\mathcal{O}(-2s-2)$: the homogeneity $-2s-2$ classifies the helicity-$s$ field. \emph{Provenance:} Penrose \cite{Penrose1969}; the sheaf-cohomological form \cite{EPW1981}.

*Provenance:* R. Penrose, Solutions of the zero-rest-mass equations, J. Math. Phys. 10 (1969), 38--39.; M. G. Eastwood, R. Penrose and R. O. Wells, Cohomology and massless fields, Commun. Math. Phys. 78 (1981), 305--351..



**Theorem 27 (The homogeneity $-2s-2$ is the ordering shift).** On functions on the conformal spinor space $\CS$ (twistor functions), realise the palatial relation of Fact \claimref{hawking.imported-twistor-storey-ordering-shift} by $\bar Z_\nu = -\hbar\,\partial/\partial Z^\nu$ (the realisation with the palatial sign $[Z^\mu, \bar Z_\nu] = +\hbar\,\delta^\mu_\nu$), let $\Upsilon := Z^\mu \partial_\mu$ be the homogeneity (Euler) operator, its eigenvalue written $\mathsf{h}$ in sans serif to keep it clear of the one-particle Hamiltonian $h$, and let the helicity operator be one half the distinguished charge, $\mathsf{s} := \tfrac12\, q(\id)$, the standard helicity operator on $\CS$ (twistor helicity) \cite{Penrose1969, EPW1981} in the symmetric ordering that Fact \claimref{hawking.imported-twistor-storey-ordering-shift} forces storey-wide. Then, as an operator identity,
\[
q(\id) \;=\; -\hbar\,(\Upsilon + 2),
\]
so a function on $\CS$ homogeneous of degree $\mathsf{h}$ is an eigenfunction of $\mathsf{s}$ with eigenvalue $s\hbar$ if and only if
\[
\mathsf{h} \;=\; -2s - 2.
\]
The $-2$ is exactly the ordering shift: without the symmetric-ordering shift of $-\hbar/2$ per complex dimension (over the complex unit $I_6$) the offset would vanish. Combined with Fact \claimref{hawking.imported-penrose-transform}, the classification parameter of the Penrose transform is the completion's own $\mathfrak{u}(1)$ charge, its offset supplied by the ordering. The computation is not new to the series: it appears, without being stated as a result, inside the proof of \cite[Thm.~5.7]{ButlerT9}, where T9's script also checks it; what this proposition adds is the statement at result level, in the transform's context, discharging the homogeneity half of the successor problem T9 assigns to this paper (the transform itself stays open).

*Proof.* With $\bar Z_\nu = -\hbar\,\partial_\nu$,
\[
q(\id) \;=\; \tfrac12\sum_\mu\bigl(Z^\mu \bar Z_\mu + \bar Z_\mu Z^\mu\bigr)
\;=\; \sum_\mu Z^\mu \bar Z_\mu + \tfrac12\sum_\mu [\bar Z_\mu, Z^\mu]
\;=\; -\hbar\,\Upsilon - \tfrac12\cdot 4\hbar \;=\; -\hbar\,(\Upsilon + 2),
\]
the commutator term being $\sum_\mu[\bar Z_\mu, Z^\mu] = -4\hbar$ by the palatial relation, one $-\hbar$ per complex dimension of $\CS$ (over $I_6$); halved by the symmetrisation, this is Fact \claimref{hawking.imported-twistor-storey-ordering-shift}'s shift of $-\hbar/2$ per complex dimension, totalling $-2\hbar$, and it is the only place the ordering enters. On a homogeneity-$\mathsf{h}$ eigenfunction, $\Upsilon f = \mathsf{h} f$, so $\mathsf{s} f = -\tfrac{\hbar}{2}(\mathsf{h} + 2)\,f$, and $\mathsf{s} f = s\hbar f$ if and only if $\mathsf{h} = -2s - 2$. The script verifies the displayed operator identity on all monomials of degree at most three in the four components of $Z \in \CS$, and the resulting homogeneity table at $s = \pm 1, \pm 2$. The reading of $\mathsf{h}$ as the classification parameter of the transform rests on \claimref{hawking.imported-penrose-transform}, which classifies helicity-$s$ fields by homogeneity $-2s-2$.




**Theorem 28 (The helicity lift, with its joints itemised).** Helicity is not additional structure imported into the framework: it is the eigenvalue of the distinguished $\mathfrak{u}(1)$ charge of the completion's conformal storey (the twistor storey: $\Cl(2,4)$ with its conformal spinor space $\CS$), and the four-dimensional mode space of each massless species has a canonical place in it. The joints, each with its provenance:
\begin{enumerate}
\item (\emph{Joint J1: the transform, classical.}) By Fact \claimref{hawking.imported-penrose-transform}, the helicity-$s$ mode space is the cohomology at homogeneity $-2s-2$; photon kinematics are at homogeneities $-4$ and $0$ ($s = \pm1$), graviton kinematics at $-6$ and $+2$ ($s = \pm2$).
\item (\emph{Joint J2: the charge, proved in the series.}) The ordering shift is proved in the correspondence paper (Fact \claimref{hawking.imported-twistor-storey-ordering-shift}), and Proposition \claimref{hawking.homogeneity-ordering-shift} derives the homogeneity $-2s-2$ from it: the classification parameter of Joint J1 is an internal charge of the completion, so the helicity ladder is part of the ascended kinematics rather than a phenomenological label.
\item (\emph{Joint J3: the reduction, modelling.}) The current boson of the s-wave theory (Fact \claimref{hawking.imported-s-wave-bosonic-sector}) is the s-wave reduction of each such four-dimensional field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction, each helicity sector identified through the transform of Joint J1: the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode, which is where Definition \claimref{obj.hawking.continuum-mode-space}'s modelling input enters, flagged as such in Remark \claimref{note.hawking.which-dynamics-what-level}.
\end{enumerate}
The composite statement is the conjunction of the three joints with the provenance displayed: J1 is classical, J2 is Fact \claimref{hawking.imported-twistor-storey-ordering-shift} together with Proposition \claimref{hawking.homogeneity-ordering-shift}, and J3 is the one modelling joint. The homogeneity table is checked by the script.

*Proof.* The assembly itemises its joints in its statement; each joint carries its own provenance there.

Helicity is not additional structure imported into the framework: it is the eigenvalue of the distinguished $\mathfrak{u}(1)$ charge of the completion's conformal storey (the twistor storey: $\Cl(2,4)$ with its conformal spinor space $\CS$), and the four-dimensional mode space of each massless species has a canonical place in it. The joints, each with its provenance:
\begin{enumerate}
\item (\emph{Joint J1: the transform, classical.}) By Fact \claimref{hawking.imported-penrose-transform}, the helicity-$s$ mode space is the cohomology at homogeneity $-2s-2$; photon kinematics are at homogeneities $-4$ and $0$ ($s = \pm1$), graviton kinematics at $-6$ and $+2$ ($s = \pm2$).
\item (\emph{Joint J2: the charge, proved in the series.}) The ordering shift is proved in the correspondence paper (Fact \claimref{hawking.imported-twistor-storey-ordering-shift}), and Proposition \claimref{hawking.homogeneity-ordering-shift} derives the homogeneity $-2s-2$ from it: the classification parameter of Joint J1 is an internal charge of the completion, so the helicity ladder is part of the ascended kinematics rather than a phenomenological label.
\item (\emph{Joint J3 (\claimref{hawking.joint-j3-s-wave-reduction}): the reduction, modelling.}) The current boson of the s-wave theory (Fact \claimref{hawking.imported-s-wave-bosonic-sector}) is the s-wave reduction of each such four-dimensional field, and the lift from the boundary modes to the field is the standard partial-wave reconstruction, each helicity sector identified through the transform of Joint J1: the near-horizon reduction of field theory on the Schwarzschild exterior identifies each $(\omega, \ell, m, s)$ channel with a two-dimensional mode, which is where Definition \claimref{obj.hawking.continuum-mode-space}'s modelling input enters, flagged as such in Remark \claimref{note.hawking.which-dynamics-what-level}.
\end{enumerate}
The composite statement is the conjunction of the three joints with the provenance displayed: J1 is classical, J2 is Fact \claimref{hawking.imported-twistor-storey-ordering-shift} together with Proposition \claimref{hawking.homogeneity-ordering-shift}, and J3 is the one modelling joint. The homogeneity table is checked by the script.




**Theorem 29 (Greybody inheritance, under the interface premise).** \emph{Premise (I), the interface identification:} the horizon-sector state feeds the exterior modes in the standard way, i.e.\ the occupancy of each near-horizon channel is carried to the corresponding asymptotic channel by the exterior propagation. This is the same assumption every derivation of Hawking flux makes, from \cite{Hawking1975} onward, and it is this assembly's one non-theorem joint. Under (I), the emitted flux in each channel $(\omega, \ell, m, s)$ equals (with $\mathcal{N}$ the count of emitted quanta)
\[
\frac{d\mathcal{N}}{dt\,d\omega} \;=\; \frac{1}{2\pi}\,\Gamma_{s\ell m}(\omega)\; n_\pm(\omega), \qquad
n_\pm(\omega) = \frac{1}{e^{\omega/\TH} \pm 1}
\]
(the upper sign for the fermionic species, the lower for the bosonic sector), with $\Gamma_{s\ell m}$ the classical transmission coefficient through the Regge-Wheeler or Teukolsky barrier. The joints: (i) the barriers and their transmission coefficients are properties of the exterior metric, and by Fact \claimref{hawking.imported-exterior-exactly-general-relativity} the framework's exterior description \emph{is} classical general relativity on the invertible region, exactly and not asymptotically, so $\Gamma_{s\ell m}$ is inherited verbatim, mode by mode \cite{ReggeWheeler1957, Teukolsky1973}; (ii) the occupancies at the horizon are Theorem \claimref{hawking.i-state-continuum} for the fermionic species and Fact \claimref{hawking.imported-s-wave-bosonic-sector}'s (Q)-conditional half for the bosonic sector, both at exactly $\TH$ with the temperature's coefficient fixed geometrically (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); (iii) given (I), the displayed formula is the definition of filtered thermal flux: the framework's flux prediction equals Hawking's \cite{Hawking1975, Page1976}, greybody structure included.

*Proof.* The assembly itemises its joints in its statement; each joint carries its own provenance there.

\emph{Premise (I) (\claimref{hawking.premise-i-interface-identification}), the interface identification:} the horizon-sector state feeds the exterior modes in the standard way, i.e.\ the occupancy of each near-horizon channel is carried to the corresponding asymptotic channel by the exterior propagation. This is the same assumption every derivation of Hawking flux makes, from \cite{Hawking1975} onward, and it is this assembly's one non-theorem joint. Under (I), the emitted flux in each channel $(\omega, \ell, m, s)$ equals (with $\mathcal{N}$ the count of emitted quanta)
\[
\frac{d\mathcal{N}}{dt\,d\omega} \;=\; \frac{1}{2\pi}\,\Gamma_{s\ell m}(\omega)\; n_\pm(\omega), \qquad
n_\pm(\omega) = \frac{1}{e^{\omega/\TH} \pm 1}
\]
(the upper sign for the fermionic species, the lower for the bosonic sector), with $\Gamma_{s\ell m}$ the classical transmission coefficient through the Regge-Wheeler or Teukolsky barrier. The joints: (i) the barriers and their transmission coefficients are properties of the exterior metric, and by Fact \claimref{hawking.imported-exterior-exactly-general-relativity} the framework's exterior description \emph{is} classical general relativity on the invertible region, exactly and not asymptotically, so $\Gamma_{s\ell m}$ is inherited verbatim, mode by mode \cite{ReggeWheeler1957, Teukolsky1973}; (ii) the occupancies at the horizon are Theorem \claimref{hawking.i-state-continuum} for the fermionic species and Fact \claimref{hawking.imported-s-wave-bosonic-sector}'s (Q)-conditional half for the bosonic sector, both at exactly $\TH$ with the temperature's coefficient fixed geometrically (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); (iii) given (I), the displayed formula is the definition of filtered thermal flux: the framework's flux prediction equals Hawking's \cite{Hawking1975, Page1976}, greybody structure included.


**Remark  (What the lift does and does not claim).** The section's claim is deliberately bounded: the \emph{spectrum} of the four-dimensional radiation is derived (occupancies theorem-grade at the horizon under the named premises, filtering inherited exactly on the invertible region, the helicity location derived from the ordering shift). What is not claimed is a derivation of four-dimensional field \emph{dynamics} from the boundary modes: that is the task of the action paper T10 \cite{ButlerT10} and, for the emergent transverse geometry that would make Joint J3 itself a theorem, of the entropy paper T8 \cite{ButlerT8}, the fuzzy-sphere question being shared between T8 and T10. The lift beyond assembly level is a named successor problem (the section ``Scope, and successor problems'').

## The finite boundary mode space, and the $\ell_P^2/A$ correction



**setting  (The finite boundary mode space, and the $\ell_P^2/A$ correction).** The bosonisation bridge of T5 rests, at one joint, on the charge-zero Fock isomorphism of the \emph{infinite} chiral fermion \cite{FrenkelKac1980}, while the physical boundary mode space is finite: $L$ modes, with $L$ of order the horizon area $A$ in Planck units. This section proves that everything the finite window changes is supported at its edges, with the exact operator identity and quantified tails, and then records the reading: the corrections are area-suppressed, so the joint's finite-mode correction takes the form of a prediction.

**setting  (The exact edge identity).** Fix a window of $L$ fermionic modes $\psi_1, \dots, \psi_L$ (CAR: $\{\psi_k, \psi_l^\dagger\} = \delta_{kl}$, all other anticommutators zero) and the currents
\[
a_m \;:=\; \sum_{k=1}^{L-m} \psi_k^\dagger\,\psi_{k+m}, \qquad 1 \le m < L .
\]



**Theorem 30 (The current commutator, exactly, with its edge split).** In the finite window, exactly and as an operator identity,
\[
[\,a_m,\, a_m^\dagger\,] \;=\; B_m - T_m, \qquad
B_m := \sum_{k=1}^{m} N_k, \qquad T_m := \sum_{k=L-m+1}^{L} N_k ,
\]
with $N_k = \psi_k^\dagger\psi_k$: the deviation from the infinite-volume central value is a difference of \emph{edge operators}, supported on the lowest and highest $m$ modes. Consequently, for $2m \le L$, on every state in which the bottom $m$ levels are filled and the top $m$ levels are empty (an \emph{edge-clean} state), $[a_m, a_m^\dagger]$ acts as the scalar $m$: the free-boson relation holds exactly, not asymptotically, on the edge-clean subspace. Moreover $[a_m, a_{m'}] = 0$ for all $m, m'$, exactly; and for $m \neq m'$ the cross commutator $[a_m, a_{m'}^\dagger]$ is a difference of bilinears supported on the lowest and highest $\max(m, m')$ modes, which annihilates every state that is edge-clean at depth $\max(m, m')$.

*Proof.* The fermionic bilinear commutator is $[\psi_a^\dagger\psi_b,\ \psi_c^\dagger\psi_d] = \delta_{bc}\,\psi_a^\dagger\psi_d - \delta_{ad}\,\psi_c^\dagger\psi_b$, an instance of the CAR (\claimref{std-algebra.witt-basis-car}). With $a_m^\dagger = \sum_{l=1}^{L-m}\psi_{l+m}^\dagger\psi_l$:
\[
[a_m, a_m^\dagger] = \sum_{k,l=1}^{L-m}\bigl(\delta_{k+m,\,l+m}\,\psi_k^\dagger\psi_l - \delta_{k l}\,\psi_{l+m}^\dagger\psi_{k+m}\bigr)
= \sum_{k=1}^{L-m} N_k - \sum_{k=m+1}^{L} N_k ,
\]
after shifting the index of the second sum. The shared middle range cancels pairwise: for $2m \le L$ the terms $k = m{+}1, \dots, L{-}m$ appear in both sums and cancel, leaving $B_m - T_m$; for $2m > L$ the two sums instead share the empty middle and the overlap $k = L{-}m{+}1, \dots, m$ of $B_m$ and $T_m$ cancels on the right-hand side, so the identity $\sum_{1}^{L-m} N_k - \sum_{m+1}^{L} N_k = B_m - T_m$ holds in both regimes. On an edge-clean state (which requires $2m \le L$ to be non-vacuous), $B_m$ acts as $m$ (each bottom mode occupied) and $T_m$ as $0$. For the cross commutators, the same computation gives
\[
[a_m, a_{m'}] = \sum_{k}\psi_k^\dagger\psi_{k+m+m'} - \sum_{k}\psi_k^\dagger\psi_{k+m+m'} = 0
\]
exactly, both surviving sums running over the same range $1 \le k \le L - m - m'$; and, for $m > m'$,
\[
[a_m, a_{m'}^\dagger] = \sum_{k=1}^{m'}\psi_k^\dagger\psi_{k+m-m'} \;-\; \sum_{k=L-m+1}^{L-m+m'}\psi_k^\dagger\psi_{k+m-m'},
\]
every surviving index within $\max(m,m')$ of an edge. Each bottom term annihilates an edge-clean state because its target level $k$ is occupied; each top term because its source level $k + m - m'$ lies in the empty top band. The case $m < m'$ follows by taking adjoints, $[a_m, a_{m'}^\dagger] = [a_{m'}, a_m^\dagger]^\dagger$, with the same band support; it annihilates edge-clean states by the mirrored argument (creation onto an occupied bottom level, lowering of an empty top level). The script verifies the identity on the full Fock space of an eight-mode window, state by state.


**setting  (The Planck factor, and the window tails).** This subsection works on the bilateral ladder, $k \in \Z$ with equal level spacing $\epsilon$: the idealisation of a deep sea, an instance of Definition \claimref{obj.hawking.continuum-mode-space} with $h = \epsilon\,\mathrm{diag}(k)_{k \in \Z}$, unbounded below. The currents of the section ``The exact edge identity'' extend to the bilateral sums $a_m = \sum_{k \in \Z}\psi_k^\dagger\psi_{k+m}$, read term by term inside I-state expectations, where the sums converge absolutely; the finite window $[-K, K]$ returns in clause (3).



**Theorem 31 (Bose-Einstein occupancy, with quantified window corrections).** Let the ladder carry the linear s-wave weight assignment (the convention T5's Premise (Q) adopts, a modelling input here as there; Fact \claimref{hawking.imported-s-wave-bosonic-sector}): level spacing $\epsilon$, sea at level $0$, I-state occupancies $n_k = (x^{-k} + 1)^{-1}$ with $x = e^{-\beta\epsilon} \in (0,1)$ the Boltzmann factor of the level spacing. Then:
\begin{enumerate}
\item \emph{(Detailed-balance identity.)} For every $k$ and $m \ge 1$, exactly,
\[
n_k - n_{k+m} \;=\; \bigl(x^{-m} - 1\bigr)\; n_{k+m}\,\bigl(1 - n_k\bigr).
\]
\item \emph{(The Planck factor, exactly, in the bilateral limit.)} Summing (1) over $k \in \Z$,
\[
\sum_{k \in \Z} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{x^{-m} - 1} \;=\; \frac{m}{e^{\beta\epsilon m} - 1}:
\]
the current two-point function $\langle a_m^\dagger a_m\rangle_I = \sum_k n_{k+m}(1 - n_k)$ (a Wick computation) is exactly $m$ times the Bose-Einstein value at $\TH$, with no vacuum correction in this normalisation. The factor $m$ is the free-boson normalisation: on the bilateral ladder the currents are used only inside expectations, and $\langle [a_m, a_m^\dagger]\rangle_I = \sum_k (n_k - n_{k+m}) = m$, the telescoped left side of (1), matching the finite-window scalar of Proposition \claimref{hawking.current-commutator-exactly-edge-split}; the unit-normalised boson is $\hat a_m = a_m/\sqrt{m}$, whose occupancy $\langle \hat a_m^\dagger \hat a_m\rangle_I = 1/(e^{\beta\epsilon m} - 1)$ is the $n_-$ of the lift.
\item \emph{(Window tails.)} For the window $[-K, K]$ with the sea at the centre, i.e.\ the sum of (2) restricted to $k \in [-K, K-m]$ (both mode indices inside the window), the bilateral sum exceeds the window sum by a positive amount bounded by $2m\,x^{K - m}/(1 - x)$: exponentially small in the distance from the sea to the edges, in units of the level spacing.
\end{enumerate}

*Proof.* (1) With $u := x^{-k}$ and $w := x^{-m}$ (the I-state occupancies of \claimref{hawking.i-state} on the linear s-wave weights of \claimref{hawking.imported-s-wave-bosonic-sector}): $n_k - n_{k+m} = \tfrac{1}{u+1} - \tfrac{1}{uw+1} = \tfrac{u(w-1)}{(u+1)(uw+1)}$, and $(w-1)\,n_{k+m}(1-n_k) = (w-1)\cdot\tfrac{1}{uw+1}\cdot\tfrac{u}{u+1}$: identical. The script checks it as an identity of rational functions in the formal variable $u$ at several rational $w$.
(2) The terms $n_{k+m}(1 - n_k)$ decay like $x^{|k|}$ in both directions, so all sums converge absolutely and may be regrouped. Fix a residue class $k = r + jm$, $j \in \Z$: the class sum of the left side of (1) is $\lim_{j_0 \to \infty}\sum_{j=-j_0}^{j_0}\bigl(n_{r+jm} - n_{r+(j+1)m}\bigr) = \lim_{j_0 \to \infty}\bigl(n_{r-j_0 m} - n_{r+(j_0+1)m}\bigr) = 1 - 0$, the interior terms cancelling in adjacent pairs; there are $m$ residue classes, and dividing by $(x^{-m}-1)$ via (1) gives the display. The Wick computation: in the gauge-invariant quasi-free state, $\langle \psi^\dagger_{l+m}\psi_l\,\psi^\dagger_k\psi_{k+m}\rangle$ has vanishing disconnected part for $m \ge 1$ (the two-point function is mode-diagonal) and connected part $\delta_{kl}\,n_{k+m}(1 - n_k)$.
(3) Bound each term two ways, both valid for every integer index: $n_{k+m}(1-n_k) \le n_{k+m} \le x^{k+m}$ and $n_{k+m}(1-n_k) \le 1 - n_k \le x^{-k}$, since $n_j \le x^j$ and $1 - n_j \le x^{-j}$ are each the statement $1 \le 1 + x^{\pm j}$. The terms missing from the window sum are those with $k > K - m$ or $k < -K$, all positive, so the difference is positive and at most
\[
\sum_{k > K-m} x^{k+m} + \sum_{k < -K} x^{-k} \;=\; \frac{2\,x^{K+1}}{1-x} \;\le\; \frac{2m\,x^{K-m}}{1-x}.
\]
The script verifies instances of the bound exactly, and checks that the window sums at $K = 30$ and $K = 40$ agree with the closed form to within the proven tails, all in exact rational arithmetic.


**Remark  (The $\ell_P^2/A$ correction, interpreted).** Propositions \claimref{hawking.current-commutator-exactly-edge-split} and \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections} together are the quantitative form of T5's note on the level of its assembly joint. The charge-zero Fock isomorphism is exact for the infinite chiral fermion; for the physical boundary mode space of $L \sim A/\ell_P^2$ modes, every deviation is edge-supported (Proposition \claimref{hawking.current-commutator-exactly-edge-split}), and thermal expectations of the deviations carry explicit tails (Proposition \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}(3)). The corrections therefore vanish as the area grows, at a rate set by the window geometry: the relative scale of generic finite-size effects is read dimensionally as $1/L = \ell_P^2/A$ (for the discretisation of mode sums and the Sugawara normalisation; proving that scaling per named observable is successor problem 4), while edge-clean bulk correlators at fixed $m$ are exponentially smaller, at the proven rates. The quantum-gravity corrections are area-suppressed and vanish where general relativity is well tested; any new physics in this derivation would appear in the $\ell_P^2/A$ correction, and that correction is a prediction of the derivation rather than a defect in it.

**Remark  (Point of contact: the Weinberg-Witten triage).** The bosonic sector's lift contains a graviton candidate (homogeneities $-6, +2$ in Assembly \claimref{hawking.helicity-lift-joints-itemised}), and a composite graviton must answer \cite{WeinbergWitten1980}: a theory with a Lorentz-covariant conserved stress tensor admits no massless spin-2 particle coupling to it. The evasion, recorded here as this paper's own claim and at Tier C: the theorem's hypotheses require the stress tensor and the spin-2 state to be defined on one and the same spacetime, and on the composite reading they are not; the covariant stress tensor of the boundary modes is defined in the two-dimensional reduced theory at the degenerate locus, the graviton candidate is a collective mode of the emergent four-dimensional description, and the hypotheses fail exactly where they fail for boundary gravitons in holography. The evidential triage, stated because the series states its own claims at their level: by \cite{Weinberg1964}, \emph{any} massless spin-2, composite or fundamental, couples universally to stress-energy, so the equivalence principle and the universal vertex are common ground and do not discriminate; what is distinctive to the composite reading is the ultraviolet behaviour and the $\ell_P^2/A$ correction of Remark \claimref{note.hawking.p-2-correction-interpreted}, and the discriminating experiments, if any, are at the scale of that correction. Below the Planck scale no available experiment discriminates the composite reading from the fundamental one, so the reading is at present untestable; this paper says so rather than presenting the absence of a refutation as support. The engineering no-go and its ontology-independence are assigned to the action paper T10 \cite{ButlerT10}.

## Scope, and successor problems



**setting  (What is proved, what is imported, what is modelling).** The abstract states each claim at one of three tiers: Tier A for what this paper proves, Tier B for what it assembles from results proved elsewhere or from named premises, and Tier C for an interpretation offered as such. The first paragraph below is the Tier A content, Proposition \claimref{hawking.homogeneity-ordering-shift} included, which the abstract meets as the lift's one proved joint; the second lists the imports that content rests on, certified by their source papers or the literature; the third is the assembly and modelling content, the assembly at Tier B and the modelling items stated as such, with the composite-graviton triage at Tier C. In the claim table of T17 \cite{ButlerT17} the paper as a whole is Tier B, because its physical conclusions pass through the assembly section, while its mathematical core is Tier A.

\emph{Proved in this paper, at the standard of \cite{ButlerT1}:} the single-mode modular structure (Proposition \claimref{hawking.modular-structure-completed-pair}); the Gibbs/KMS equivalence with uniqueness in finite dimensions and the restriction lemma (Lemmas \claimref{hawking.gibbs-states-are-kms-conversely-finite}, \claimref{hawking.kms-restricts-invariant-subalgebras}). Also proved here: the I-state theorem's window-exact existence (Theorem \claimref{hawking.i-state}(1), window case), the forced gauge invariance, and the derivation of the Fermi-Dirac symbol from the KMS identity, on the boundary modes and on the continuum core (Theorems \claimref{hawking.i-state}(2)--(3), \claimref{hawking.i-state-continuum}(2)--(3)); the homogeneity $-2s-2$ from the ordering shift (Proposition \claimref{hawking.homogeneity-ordering-shift}); the exact edge identity, the edge-clean exactness of the free-boson relation, and the cross-commutator support bound (Proposition \claimref{hawking.current-commutator-exactly-edge-split}); the detailed-balance identity, the exact bilateral Planck factor, and the window tail bounds (Proposition \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}, on the (Q)-convention ladder named in its statement).

\emph{Imported as Facts with provenance:} T5's modular descent under its premises (P) and (R), with the geometric normalisation (Fact \claimref{hawking.imported-modular-descent-premises-geometric-normalisation}); the tower's CAR limit (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}); the s-wave bosonisation results, their occupancy half under T5's premise (Q) (Fact \claimref{hawking.imported-s-wave-bosonic-sector}); the exterior exactness at $\Lambda = 0$ (Fact \claimref{hawking.imported-exterior-exactly-general-relativity}); the twistor storey and the ordering shift (Fact \claimref{hawking.imported-twistor-storey-ordering-shift}). From the literature: Araki's quasi-free calculus, the inductive-limit KMS result, the two-point reduction, and the ideal-Fermi-gas uniqueness (Facts \claimref{hawking.imported-quasi-free-states-car-algebra}, \claimref{hawking.imported-kms-passes-inductive-limits}, \claimref{hawking.imported-quasi-free-kms-reduces-two}, \claimref{hawking.imported-ideal-fermi-gas-uniqueness}); the Araki-Wyss representation (Fact \claimref{hawking.imported-thermal-representation}); the Penrose transform (Fact \claimref{hawking.imported-penrose-transform}); the soft-graviton universality \cite{Weinberg1964} used in Remark \claimref{note.hawking.point-contact-weinberg-witten-triage}.

\emph{Assembly and modelling, flagged at their level:} the helicity lift's joint J3 and the greybody interface premise (I) (the section ``The four-dimensional lift''); the identification of the physical mode set, and the linear s-wave weight convention of the bilateral ladder (Remark \claimref{note.hawking.which-dynamics-what-level}, Proposition \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}); the $\ell_P^2/A$ dimensional reading of generic finite-size corrections (Remark \claimref{note.hawking.p-2-correction-interpreted}); the composite-graviton reading and its triage (Remark \claimref{note.hawking.point-contact-weinberg-witten-triage}), which is Tier C and says so.

**setting  (Successor problems).** Six problems for the series' list of open directions.

\begin{enumerate}
\item \emph{State selection from geometry.} Formulate the geometric-modular-action axiom for a net of boundary-mode algebras over the horizon and derive the boost dynamics, the temperature entering through the net's geometric normalisation rather than as an algebra-intrinsic quantity, which T5's rate-rigidity theorem shows it cannot be \cite[Thm.~7.16]{ButlerT5}. Proposition \claimref{hawking.modular-structure-completed-pair}(5) fixes the single-atom orbits, and T5's factor-level analysis (its condition (G), rejected as over-determining) records what is already established.
\item \emph{The lift beyond assembly.} Derive joint J3, the partial-wave identification, from the emergent transverse geometry (the fuzzy sphere of the counting programme), converting the helicity lift (Assembly \claimref{hawking.helicity-lift-joints-itemised}) from assembly to theorem; shared with the entropy paper T8 \cite{ButlerT8} and the action paper T10 \cite{ButlerT10}.
\item \emph{The Kerr continuum.} Superradiant channels make the rotating analogue of Theorem \claimref{hawking.i-state-continuum} genuinely different (no global KMS state at fixed angular velocity for all modes); formulate the correct rotating statement.
\item \emph{The $\ell_P^2/A$ correction, per observable.} Refine Remark \claimref{note.hawking.p-2-correction-interpreted} into a table of leading finite-$L$ corrections for named observables (spectrum distortion, correlator deficits), with the $\ell_P^2/A$ scaling proved rather than dimensional.
\item \emph{The cosmological state.} Connect the equilibrium I-state to the non-equilibrium state of the descent.
\item \emph{Helicity counting per boundary mode.} Decide whether one boundary mode of the near-horizon theory carries one helicity channel of the lift or both helicities of a massless species. The two answers differ downstream by a factor of two in the capacity per boundary mode ($\ln 2$ against $2\ln 2$) and so in the entropy paper's calibration residue, $\kappa_c = 1/(4\ln 2)$ against $1/(8\ln 2)$ \cite[Prop.~4.12]{ButlerT8}. In this paper the question sits at joint J3 of Assembly \claimref{hawking.helicity-lift-joints-itemised}, the partial-wave identification of each $(\omega, \ell, m, s)$ channel with a two-dimensional mode, which is modelling; joints J1 and J2 place the two helicities at distinct homogeneities but do not say how many channels one boundary mode registers. T8 takes the one-helicity reading, at the tier of that joint; settling it is part of converting J3 to a theorem (problem 2).
\end{enumerate}

## Position in the series



**setting  (Position in the series).** This paper is T7 of the series. \emph{It relies on six predecessors:} the primer T0 \cite{ButlerT0} and the root paper T1 \cite{ButlerT1} for the completed-pair language and the transport principle; the tower paper T3 \cite{ButlerT3} for the CAR limit that makes the boundary modes an algebra (Fact \claimref{hawking.imported-algebra-boundary-modes-car-algebra}); the singularity paper T5 \cite{ButlerT5} for modular descent under its premises (P) and (R), the bosonisation bridge under (Q), and the surface gravity $\kappa = 1/4M$ (Facts \claimref{hawking.imported-modular-descent-premises-geometric-normalisation} and \claimref{hawking.imported-s-wave-bosonic-sector}); the interior paper T6 \cite{ButlerT6} for the exterior exactness that greybody inheritance rests on (Fact \claimref{hawking.imported-exterior-exactly-general-relativity}); and the twistor paper T9 \cite{ButlerT9} for the ordering shift from which Proposition \claimref{hawking.homogeneity-ordering-shift} is promoted.

\emph{Papers that rely on this one:} the entropy paper T8 \cite{ButlerT8} imports the single-mode modular structure, the quasi-free calculus, and the finite-window identities; the action paper T10 \cite{ButlerT10} imports the finite-window quantification of the current algebra; the standard-model paper T12 \cite{ButlerT12} imports the helicity identification of Proposition \claimref{hawking.homogeneity-ordering-shift}; and the capstone T17 \cite{ButlerT17} tabulates this paper's claims at their tiers.

## Machine verification



**setting  (Machine verification).** The computational identities asserted in this paper are verified by the script deposited with it, \texttt{verify\_T07.py} \cite{ButlerVerifyT7}. The script imports the series' shared exact-arithmetic library \texttt{GA.py}, runs entirely in exact arithmetic (rational numbers and rational functions in a formal Boltzmann variable, no floating point anywhere), and so certifies each check as an identity, or as an exactly evaluated inequality, rather than an approximation. Twenty-five checks pass. Not scripted, and stated as such where they occur: the imported Facts, certified by their source papers' scripts or by the literature; the continuum passage beyond its window content; the assembly joints of the section ``The four-dimensional lift''; the classical Penrose transform; and the geometric inputs $\kappa = 1/4M$ and $\TH = \kappa/2\pi$, proved and scripted in T5.

The coverage, section by section.

\begin{description}
\item[the section ``Setting and imports'', the single mode (Proposition \claimref{hawking.modular-structure-completed-pair}).] All five clauses in the basis-blade arithmetic over $\Cl(1,1)$: the null pair's squares and anticommutator, $\sigma = e_0e_1$ with $\sigma^2 = 1$, the one-sided weight relations, the finite conjugation at the rational rotor $R = \tfrac53 + \tfrac43\,\sigma$ (that is, $\cosh(\lambda/2) = \tfrac53$) with scale factors $\tfrac19$ and $9$, the projector identities, and the one-dimensionality of the bivector space; plus the Fock identity $\tfrac12\sigma = N - \tfrac12$.
\item[the section ``The state input: the I-state'', the state (Lemma \claimref{hawking.gibbs-states-are-kms-conversely-finite}, Theorem \claimref{hawking.i-state}).] The Gibbs KMS identity on all sixteen matrix-unit pairs of the mode algebra, as identities of rational functions in the formal Boltzmann factor; the uniqueness solve, performed symbolically, the KMS constraints on an arbitrary density matrix having a one-dimensional kernel spanned by the Gibbs matrix. Then the symbol itself: the Fermi-Dirac detailed-balance identity $n/(1-n) = e^{-\beta\omega}$; the Fermi-Dirac product state on a three-mode window confirmed equal to the Gibbs matrix of $H_F$, the two sides built independently, then confirmed KMS on all $4096$ matrix-unit pairs; and, on a two-mode window, the full KMS constraint system solved for an arbitrary density matrix against independently supplied dynamics, with one-dimensional kernel, vanishing pairing, and the Fermi-Dirac symbol.
\item[the section ``The mode continuum'', the continuum.] No separately computable identity: its exact content is the window case, scripted under Section 3, and its remaining steps are the imported calculus of Facts \claimref{hawking.imported-quasi-free-kms-reduces-two} and \claimref{hawking.imported-ideal-fermi-gas-uniqueness}, certified by their sources.
\item[the section ``The four-dimensional lift'', the lift (Proposition \claimref{hawking.homogeneity-ordering-shift}).] The operator identity $q(\id) = -\hbar(\Upsilon + 2)$ on all twistor monomials of degree at most three, and the homogeneity table $-2s-2 \mapsto (-4, 0, -6, +2)$ at $s = \pm 1, \pm 2$.
\item[the section ``The finite boundary mode space, and the $\ell_P^2/A$ correction'', the finite window (Propositions \claimref{hawking.current-commutator-exactly-edge-split} and \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}).] The edge identity $[a_m, a_m^\dagger] = B_m - T_m$ as an operator identity on all $256$ states of an eight-mode window for $m = 1, 2, 3$; the exact free-boson relation on every edge-clean state; the exact vanishing of $[a_m, a_{m'}]$ and the vanishing of the cross commutator on edge-clean states. Then the ladder: the detailed-balance identity of Proposition \claimref{hawking.bose-einstein-occupancy-quantified-window-corrections}(1) in the formal $x^{-k}$ at three values of $x^{-m}$, with the Bose-Einstein form $\bar n/(1 + \bar n) = e^{-\beta\omega}$ of the clause-(2) occupancy, at $\omega = \epsilon m$ on the ladder; the window sums' approach to the exact Planck factor from below, within the proven tail bound, as exact rational inequalities at two temperatures and three $m$; and the Wick formula checked against the direct density-matrix expectation on the full $256$-state window, the ladder in the paper's occupancy convention.
\end{description}

The script exits nonzero on any failure and prints one line per check, tagged by the statement it certifies.

## Results cited, not shown

**Fact (imported) 32 (The Clifford side of the ordering shift).** Let $(v, v^*)$ be a null pair of $V$ with $\ip{v}{v^*} = 1$ (an adjoined ladder pair), and let $E := v\wedge v^* \in \mathfrak{so}(2,4)$ be the grading element of the corresponding hyperbolic plane. In the Fock model, the spinor action of $E$ is
\[
\rho(E) \;=\; \tfrac12\,c(v)\,c(v^*) - \tfrac12 \;=\; N - \tfrac12 ,
\]
where $N$ is the occupation number operator of the mode created by $v$ (eigenvalue $1$ on states containing that mode, $0$ otherwise). The generator of the adjoined plane's boost is the mode's number operator shifted by one half.

*Provenance:* Transport Lab claim correspondence.clifford-side-ordering-shift, version 3 (T09 Prop 5.6).

**Fact (imported) 33 (The Fock model of the complexified ascended algebra).** Let $W \subset V_\C$ be a maximal totally isotropic subspace ($\dim_\C W = 3$) and $W'$ a complementary maximal isotropic subspace, dual to $W$ under the $\C$-bilinear form (such a pair exists, and any two such pairs are conjugate under $O(V_\C)$). On the exterior algebra $\Lambda^\bullet W$ ($\dim_\C = 2^3 = 8$) define
\[
c(w) := \sqrt2\; w \wedge (\cdot) \quad (w \in W),
\qquad
c(w') := \sqrt2\; \iota_{w'} \quad (w' \in W'),
\]
with $\iota$ contraction through the pairing. Then $c(u)^2 = Q(u)\,\id$ for every $u \in W \oplus W' = V_\C$, so $c$ extends to an algebra map $\Cl(V_\C) \to \End(\Lambda^\bullet W)$; this map is an isomorphism, and $\Lambda^\bullet W$ is the unique irreducible module of $\Cl(2,4)_\C$: the Dirac spinors of the completion. Vectors act oddly, so the even and odd halves
\[
\CS := \Lambda^{\mathrm{even}} W, \qquad \CSm := \Lambda^{\mathrm{odd}} W,
\]
each of complex dimension 4, are modules of the even subalgebra $\Cl^0(2,4)_\C \cong \End(\CS) \oplus \End(\CSm)$: the two chiralities, the conformal spinor space $\CS$ and its opposite $\CSm$ (twistor and dual twistor space).

*Provenance:* Transport Lab claim correspondence.fock-model-complexified-ascended-algebra, version 6 (T09 Thm 3.1).

**Fact (imported) 34 (The shared core, and the ordering dictionary).** \begin{enumerate}
\item The symmetrised quadratics of the palatial algebra close under commutator on a copy of $\mathfrak{gl}(4,\C) = \mathfrak{gl}(\CS)$, with $\CS$ the conformal spinor space (twistor space) (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}); the anti-Hermitian part with respect to the Hermitian form $\Sigma$ of Proposition \claimref{correspondence.reality-conjugation-twistor-form-factor} is $\mathfrak{u}(2,2)$, containing $\mathfrak{su}(2,2) \cong \mathfrak{so}(2,4)$.
\item The bivectors of $\Cl(2,4)_\C$ close under commutator on $\mathfrak{so}(2,4)_\C$ and act on $\CS$ as $\mathfrak{sl}(\CS)$ (Proposition \claimref{correspondence.spin-representation}).
\item Under the Klein identification the two copies coincide, compatibly with their actions: the assignment $\beta \mapsto q(\rho(\beta))/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{so}(2,4)_\C \to \mathcal{P}$, and the adjoint action of $q(\rho(\beta))/\hbar$ on the linear palatial generators $Z^\alpha$, $\bar Z_\beta$ is the spinor action $\rho(\beta)$ of the Clifford bivector, in the dual pair of slots of Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(1) ($-\rho(\beta)$ on the $Z$ slot, its transpose on the $\bar Z$ slot).
\item Both quantisations incur the same ordering shift of one half per dimension: on the palatial storey, symmetric ordering shifts the distinguished $\mathfrak{u}(1)$ generator by $-\tfrac{\hbar}{2}$ per complex dimension of $\CS$, totalling $-2\hbar$ (Lemma \claimref{correspondence.symmetrised-quadratics-palatial-algebra}(3)); on the Clifford storey, the boost generator of each adjoined plane is $N - \tfrac12$: minus one half per fermionic mode, the same sign (Proposition \claimref{correspondence.clifford-side-ordering-shift}).
\end{enumerate}

*Provenance:* Transport Lab claim correspondence.shared-core-ordering-dictionary, version 4 (T09 Thm 5.7).

**Fact (imported) 35 (Symmetrised quadratics of the palatial algebra).** For $M \in \mathfrak{gl}(4,\C)$ with entries $M^\beta{}_\alpha$ set
\[
q(M) \;:=\; \tfrac12 \sum_{\alpha,\beta} M^\beta{}_\alpha\,\bigl(Z^\alpha \bar Z_\beta + \bar Z_\beta Z^\alpha\bigr) \;\in\; \mathcal{P}.
\]
Then:
\begin{enumerate}
\item $[q(M), Z^\gamma] = -\hbar\,(MZ)^\gamma$ and $[q(M), \bar Z_\gamma] = +\hbar\,(M^{\mathsf T}\bar Z)_\gamma$: the adjoint action of $q(M)$ on the linear generators is the linear action of $M$ (in the dual pair of representations), times $\hbar$;
\item $[q(M), q(N)] = \hbar\, q([M,N])$: the map $M \mapsto q(M)/\hbar$ is an injective Lie algebra homomorphism $\mathfrak{gl}(4,\C) \to \mathcal{P}$;
\item $q(M) = \sum M^\beta{}_\alpha Z^\alpha \bar Z_\beta - \tfrac{\hbar}{2}\operatorname{tr} M$: the symmetric and normal orderings of a quadratic differ by the central element $\tfrac{\hbar}{2}\operatorname{tr}M$; for the distinguished generator $M = \mathrm{id}$ (the helicity/homogeneity direction) the shift is $-2\hbar$, that is $q(\mathrm{id}) = \sum_\alpha Z^\alpha\bar Z_\alpha - 2\hbar$: minus one half of $\hbar$ for each of the four complex dimensions of the conformal spinor space $\CS$ (twistor space).
\end{enumerate}

*Provenance:* Transport Lab claim correspondence.symmetrised-quadratics-palatial-algebra, version 5 (T09 Lem 5.5).

**Fact (imported) 36 (Covariant form of the vacuum equations).** Let $g$ be the derived metric of a gravitational field $(\hb, \Omega)$ on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) on its invertible region $M^\circ$, and let $I_g := (1, 0, 0) = \nInf$ be the pure-scale section of $\mathcal{T}$ in the scale $g$. For the tractor connection, which in Gauge Theory Gravity is the $\Cl(2,4)$ rotation-gauge field $D^{T}_{a} = a \cdot \nabla + \Omega_{T}(a)\times$, $\Omega_{T}(a) = \Omega(a) - \nInf \wedge \hb^{-1}(a) + \nO \wedge \Sch(\hb^{-1}(a))$, acting on tractors $\sigma\nInf + \mu + \rho\nO$ (Theorem \claimref{synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection}), with slots in the splitting of $g$,
\[
\nabla_a I_g = \bigl(0,\; -\Sch_{ab},\; 0\bigr), \qquad\text{that is}\qquad D^{T}_{a}\nInf = -\Sch\bigl(\hb^{-1}(a)\bigr),
\]
so $I_g$ is parallel if and only if $\Sch = 0$, if and only if $g$ is Ricci-flat, if and only if (Fact \claimref{interior.imported-equivalence-einstein-equations}) the GTG vacuum field equations hold. Moreover $Q(I_g) = 0$: the section is null. Hence the vacuum field equations on $M^\circ$ are exactly equivalent to the parallelism of the scale tractor $I_g$ attached to $g$: the ideal point of the fibre quadric that the physical scale distinguishes is covariantly constant. (Existence of \emph{some} parallel null tractor is the strictly weaker, conformally invariant statement that $[g]$ is almost Ricci-flat: it carries an almost-Einstein scale which is Ricci-flat away from that scale's zero set, and the zero set may be non-empty. A non-constant rescaling $e^{2\omega}g$ already keeps the parallel section while losing the field equations.) The statement is covariant under the gauge transformations of $\mathcal{T}$, whose structure algebra is $\mathfrak{so}(2,4)$ acting through the bivectors of $\Cl(2,4)$.

*Provenance:* Transport Lab claim interior.covariant-form-vacuum-equations, version 5 (T06 Thm 4.5).

**Fact (imported) 37 (Imported: equivalence with the Einstein equations).** On any region where $\hb$ is invertible, the GTG field equations for $(\hb, \Omega)$ are equivalent to the Einstein field equations for the metric $g(a,b) = \hb^{-1}(a)\cdot\hb^{-1}(b)$; in vacuum, to Ricci-flatness of $g$. \emph{Provenance:} Lasenby, Doran and Gull \cite[\S 4.3 and App.~C]{LDG1998}; textbook form \cite[Ch.~13-14]{DoranLasenby2003}.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 38 (The bosonisation bridge, s-wave sector).** Let $\{\psi_k, \psi^\dagger_k\}_{k \in \mathbb{Z}}$ be the boundary modes, as fermion operators on the filled-sea Fock space (the infinite filled-sea array whose algebraic model is the completed tower limit of \cite[Thm.~5.6]{ButlerT3}, cited for the structure; its provenance here is the s-wave aggregation declared above, not a tower, the mod-8 clock having stopped after one ascent), and define the currents $a_m := \sum_k :\psi^\dagger_k\,\psi_{k+m}:$ with $:\;:$ normal ordering at the sea level; with the sea filled below the level, $a_m$ annihilates the sea for $m > 0$ and $a_{-m} = a_m^{\dagger}$ creates particle-hole pairs. (The opposite index convention flips the sign of the central term; the verification script fixes the convention by computation.) Then:
\begin{enumerate}
\item (Current algebra.) $[a_m, a_n] = m\,\delta_{m+n,0}\,\id$ on the infinite array; on a finite window the commutator equals $m\,\delta_{m+n,0}\,\id$ plus an \emph{exactly identified} edge operator ($B_m - T_m - m$ in the proof's notation), supported on the bottom and top $m$ sites and vanishing on all bulk states: the number-conserving bilinears satisfy the canonical commutation relations of a free boson. A boson is a pair of the pair.
\item (KMS restriction.) Each bilinear $\psi^\dagger_k\psi_{k+m}$ carries a definite boost weight, fixed by the difference $\omega_{k+m} - \omega_k$ of its two modes' weights. Under (Q)'s weight clause, $\omega_k = \kappa k$, that difference is $\kappa m$ for every $k$, so each current $a_m$ is itself a weight vector and the current subalgebra is globally invariant under the modular flow of Theorem \claimref{singularity.modular-structure-completed-pair}; for weights that are not affine in $k$ the summands of $a_m$ rotate at different rates and the span of the currents need not be invariant, so this invariance uses (Q). Under (Q) the joint state is KMS for that flow, and a KMS state restricted to a flow-invariant subalgebra is KMS at the same temperature for the restricted flow. Without (Q) no joint KMS state is available: (R) is imposed on the marginals alone, and Theorem \claimref{singularity.exact-equilibrium-over-determines-boundary-modes} is the reason its joint form is rejected elsewhere in the chain.
\item (The Planck factor.) Under (Q), with the marginal occupancies $n_k = (e^{\beta\omega_k} + 1)^{-1} = (e^{\beta\kappa k} + 1)^{-1}$ at the premise's linear weights, the current occupancy is, exactly,
\[
\langle a_{-m} a_m \rangle \;=\; \sum_{k \in \mathbb{Z}} n_{k+m}\,(1 - n_k) \;=\; \frac{m}{e^{\beta\kappa m} - 1} \qquad (m > 0) ,
\]
with no vacuum piece in this convention ($a_m$ annihilates the sea): Bose-Einstein occupancy at exactly $\TH$. The Planck spectrum of the bosonic Hawking flux is derived, not conjectured, for the s-wave sector, in the equilibrium reading (Q) fixes; for a general member of the chain's state class the left side acquires the connected correlators (Q) sets to zero, and no exact spectrum is claimed.
\end{enumerate}
The single assembly-level ingredient in the section is the charge-zero Fock isomorphism (the charge-zero sector of the fermionic Fock space is canonically the bosonic Fock space, with fermions recovered as vertex operators), cited to \cite{PressleySegal1986} and used only for the completeness statement that the two descriptions are one algebra; parts (1)-(3) are proved outright.

*Provenance:* Transport Lab claim singularity.bosonisation-bridge-s-wave-sector, version 7 (T05 Thm 8.2).

**Fact (imported) 39 ($\kappa = 1/4M$, computed).** For the Schwarzschild gravitational field of the section ``The metric of the gauge field, and its static form'' (the stored field $\hb = 1 - \beta P$ on flat spacetime, Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}), the static Killing field $K = \hb^{-1}(e_t)$ has $Q(K) = f = 1 - 2M/r$, and the static observers, of velocity $v = K/\sqrt f$, have redshifted proper acceleration $\sqrt f\,\sqrt{-Q((v \cdot D)v)} = f'(r)/2$ at every $r > 2M$, so the surface gravity of the horizon locus $r = 2M$ is
\[
\kappa \;=\; \lim_{r \to 2M} \frac{f'(r)}{2} \;=\; \frac{1}{2}\cdot\frac{2M}{(2M)^2} \;=\; \frac{1}{4M} .
\]

*Provenance:* Transport Lab claim singularity.computed, version 4 (T05 Prop A.2).

**Fact (imported) 40 (The descended form is state independent).** Let $\varrho$ be the density matrix of \emph{any} state on the boundary mode space, and $\varrho_k$ its marginal at mode $k$. Then $E_k(\varrho_k)$ is diagonal in that mode's number basis, and therefore
\[
E_k(\varrho_k) \;=\; \frac{e^{-\beta_k \omega_k N_k}}{Z_k}
\]
for a unique $\beta_k \in [-\infty, +\infty]$, determined by $\beta_k\omega_k = \log\bigl(p_k/(1-p_k)\bigr)$ with $p_k$ the descended vacancy probability. (Stated for $\omega_k \neq 0$: at a zero-weight mode the right side is $\tfrac12\,\mathrm{id}$ for every $\beta_k$, so uniqueness always fails there, and existence fails unless $p_k = \tfrac12$.) The descended single-mode state is a Gibbs state of the boost generator $K_k$ whatever the ascended state was: no hypothesis on the state is used.

*Provenance:* Transport Lab claim singularity.descended-form-state-independent, version 4 (T05 Thm 7.6).

**Fact (imported) 41 (The Euclidean section, and its period).** Let $t_s = -i\tau$ in the static gauge of the Schwarzschild gravitational field on flat spacetime (the section ``The metric of the gauge field, and its static form''; Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}). The Wick-rotated field lives on the flat Euclidean background, and its derived metric is the Riemannian metric $f\,d\tau^{2} + f^{-1}dr^{2} + r^{2}d\Omega^{2}$ on $r > 2M$; let $\varrho(r) := \int_{2M}^{r} f^{-1/2}\,dr'$ be proper radial distance from the horizon locus. Then, with $F := \sqrt f$ regarded as a function of $\varrho$,
\[
f\,d\tau^{2} + f^{-1}dr^{2} \;=\; d\varrho^{2} + F(\varrho)^{2}\,d\tau^{2}, \qquad F(0) = 0, \qquad \frac{dF}{d\varrho}\Big|_{\varrho = 0} \;=\; \frac{f'(2M)}{2} \;=\; \kappa \;=\; \frac{1}{4M} ,
\]
so that near $\varrho = 0$ the $(\varrho, \tau)$ plane carries the metric $d\varrho^{2} + \kappa^{2}\varrho^{2}d\tau^{2} + O(\varrho^{4})\,d\tau^{2}$. If $\tau$ is periodic with period $p$, the section is a smooth Riemannian manifold at $\varrho = 0$ (the tip of the section, the two-sphere where the Euclidean Killing flow has its fixed points, the Euclidean counterpart of the bifurcation sphere) if and only if
\[
\kappa\,p \;=\; 2\pi, \qquad \text{i.e.} \qquad p \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M ;
\]
for any other period the origin of the $(\varrho, \tau)$ plane is a conical point of total angle $\kappa p$. The period of imaginary Killing time is therefore fixed by the gravitational field, at the horizon locus, and it is the conversion factor of Proposition \claimref{singularity.plane-rate} read in imaginary time. The regularity condition is local: it lives in a polar chart about the tip of the Wick-rotated flat background; the Lorentzian bifurcation surface itself lies beyond one flat chart and is not used.

*Provenance:* Transport Lab claim singularity.euclidean-section-period, version 5 (T05 Prop 7.18).

**Fact (imported) 42 (The matching: Steps 4b and 4c join by equation).** Realise the hyperbolic atom of Lemma \claimref{singularity.pseudo-inverse-identities-hyperbolic-atom} on the radial plane, $e_0 = \hat e_t$, $e_1 = \hat e_r$. Where this realisation lies must be stated, because it is available exactly where the ascent is not needed: at every $r > 0$ the physical radial plane has signature $(1,1)$ and carries a CAR pair inside $\Cl(1,3)$ with no ascent at all, but at $r = 0$ the radial plane itself degenerates, its radical the dying direction $k$ (corank one in the forced weighting, Remark \claimref{note.singularity.corank-limit-weighted-answer} and Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2); Proposition \claimref{singularity.degeneration-exactly}'s uniform rescaling degenerates the whole form), so no CAR pair supported on the radial plane survives there, even though the weighted module still contains hyperbolic planes (Fact \claimref{sheaf.schwarzschild-degeneration-boundary-tame}(2): $V_1$ carries $\mathrm{diag}(m^2, -1, -1)$). On $E$ the atom is carried by $\operatorname{span}(k, \nO/2\nu)$, one leg the dying direction itself and one adjoined (Fact \claimref{singularity.imported-one-sided-completion-singularity}, Remark \claimref{note.singularity.metric-level-parity-even-level}): the odd sector is not a pre-existing grading of $\Cl(1,3)$ precisely because one of its legs lies outside. Nor is the matching an identification of two coexisting copies, Fact \claimref{singularity.imported-one-sided-completion-singularity}'s pair existing exactly over $E$: the two constructions share the leg $k$. At every $r > 0$ the radial plane contains $k^{\sharp} = -\sqrt r\,\er$ (Proposition \claimref{singularity.transport-schwarzschild-fibre}(4)), the plane degenerates onto $\R k$ as $r \to 0$, and the completion re-attaches $\nO/2\nu$ to that same $k$. What is shared is the direction and the degeneration onto it, not a null leg of the atom: $k^{\sharp}$ is spacelike at every $r > 0$ while the atom's legs are null, and the $E$-atom's bivector $k \wedge \nO/2\nu$ is not $\sigma_r$. The identification of the modular bivector with the curvature-selected plane is therefore made at $r > 0$, where Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling} holds, and \emph{transported} to $E$ along the degeneration; that transport is the matching's residual step, stated as such rather than absorbed into the shared direction, and the two-level computations of Steps 4c through 6b concern the abstract atom, whichever realisation carries it. Then the modular bivector of Theorem \claimref{singularity.modular-structure-completed-pair},
\[
\sigma \;=\; v^*v - vv^* \;=\; e_0 e_1 ,
\]
spans the radial plane and satisfies the pair of equations
\[
S(\sigma) = -2\,\sigma, \qquad \sigma^2 = +1 ,
\]
and this pair characterises $\sigma$ up to sign among the unit frame bivectors: the eigenvalue equation confines $\sigma$ to $\{\sigma_r, I\sigma_r\}$ (Theorem \claimref{singularity.curvature-gauge-field-exact-shape-decoupling}), and the square excludes the dual, for which $(I\sigma_r)^2 = -1$. The bivector that generates Step 4c's modular flow, the phase flow $\operatorname{Ad}(e^{it\sigma/2})$, whose real rotor flow is $\exp(\lambda\sigma/2)$, is therefore the same object Step 4b's curvature distinguishes, identified by equation rather than by name; the residual sign is the orientation of the boost, the labelling of outgoing against ingoing, which is exactly the $\mathbb{Z}_2$ that Theorem \claimref{singularity.modular-structure-completed-pair}(2) attaches to the weights of $v$ and $v^*$. And by the localisation theorem \cite[Thm.~4.4, Cor.~4.5]{ButlerT4} the pair, hence the atom, hence $\sigma$, is at the degenerate radial direction, which is where Proposition \claimref{singularity.degeneration-exactly} located the division: the plane the curvature selects, the plane the completed pair lies in, and the plane through which division fails are one plane. One plane, not one locus: the curvature selects it at every $r > 0$, the calibration reads it at the horizon (Proposition \claimref{singularity.plane-rate}), the ladder inhabits it on $E$, and Proposition \claimref{singularity.why-calibration-cannot-be-internal} records that the calibration locus and the singular locus do not meet; what carries the identification across them is the frame-robustness of the plane (Remark \claimref{note.singularity.frame-made-explicit}) and the radius-independence of its selection, not a claim that the loci coincide.

*Provenance:* Transport Lab claim singularity.matching-steps-4b-4c-join-equation, version 5 (T05 Cor 6.4).

**Fact (imported) 43 (Modular descent).** Let the ascended algebra of the horizon pair carry any state that is (i) pure, (ii) invariant under the boost flow generated by $\sigma$, and (iii) entangling across the two ends of the pair (cyclic and separating for the one-sided subalgebra). Then the descended state, the partial trace over the partner, which for such a state coincides with the restriction under the pinching $E$ of Proposition \claimref{singularity.descent-what-it-erases} (Proposition \claimref{singularity.pinching-against-partial-trace-scope-coincidence}(i); the coincidence is exactly single-mode, Proposition \claimref{singularity.pinching-against-partial-trace-scope-coincidence}(ii)), is KMS for the phase flow $\operatorname{Ad}(e^{it\sigma/2})$ of $\sigma$ at some inverse temperature $\beta \in \R$ in rapidity, and the hypotheses leave $\beta$ free, its sign included: nothing in (i) to (iii) forces $\beta > 0$ (the descended form of Theorem \claimref{singularity.descended-form-state-independent} allows the closed range $[-\infty, +\infty]$, and hypothesis (iii) removes exactly the endpoints), and positivity arrives with (R). If the modular parameter is normalised to the geometric period, one modular period being one period $2\pi/\kappa$ of rapidity-time (the Bisognano-Wichmann normalisation, which the section ``What selects the state'' names as premise (R) and proves irreducible), then $\beta = 2\pi$ in rapidity and, by Proposition \claimref{singularity.plane-rate}, the physical temperature is
\[
T \;=\; \frac{\kappa}{2\pi} \;=\; \frac{1}{8\pi M} \;=\; \TH ,
\]
exactly the Hawking temperature. For the CAR pair, the reduced density matrix per mode of frequency $\omega$ is then the Fermi-Dirac matrix $\operatorname{diag}(1, e^{-\omega/T})/Z$ with occupancy $1/(e^{\omega/T} + 1)$. The hypotheses are sufficient, not necessary: a state violating (ii) or (iii) need not descend thermally, and the projection cannot make it do so, but some such states do (the proof exhibits one), and Theorem \claimref{singularity.descended-form-state-independent} explains why no hypothesis on the state can be necessary for the \emph{form}.

*Provenance:* Transport Lab claim singularity.modular-descent, version 5 (T05 Thm 7.3).

**Fact (imported) 44 (The rate, and the discharge of hypothesis (iii)).** Assume (P) and (R). Then at every mode $k$ the marginal is the Gibbs state of $K_k$ at the same inverse temperature,
\[
\beta_k \;=\; \beta \;=\; \frac{2\pi}{\kappa} \;=\; 8\pi M , \qquad T \;=\; \frac{\kappa}{2\pi} \;=\; \frac{1}{8\pi M} \;=\; \TH ,
\]
with occupancy $\omega(v_k^{*}v_k) = (e^{\beta\omega_k} + 1)^{-1} \in (0,1)$. In particular every marginal is faithful, hence cyclic and separating for its mode factor: hypothesis (iii) of Theorem \claimref{singularity.modular-descent} is a consequence of (R), not an assumption; and the temperature is the same at every mode without any condition on the joint state.

*Provenance:* Transport Lab claim singularity.rate-discharge-hypothesis-iii, version 4 (T05 Thm 7.20).

**Fact (imported) 45 (Rate rigidity: the temperature is not algebra intrinsic).** Let $\alpha_t = \operatorname{Ad}(e^{itK})$ be the boost flow of the single-mode algebra $\Aa$, let $\theta$ be a $*$-automorphism of $\Aa$, and let $\omega_\beta$ denote the $\beta$-KMS state of $\alpha$.
\begin{enumerate}
\item If $\theta$ commutes with the flow then it fixes every Gibbs state of $K$: $\omega_\beta \circ \theta = \omega_\beta$ for every $\beta$.
\item If $\theta$ reverses the flow, $\theta\circ\alpha_t = \alpha_{-t}\circ\theta$, then $\omega_\beta\circ\theta = \omega_{-\beta}$.
\item Under a constant reparametrisation of the flow, $\alpha_t \mapsto \alpha_{ct}$ with $c > 0$, the $\beta$-KMS state of $\alpha$ is the $(\beta/c)$-KMS state of the reparametrised flow: $\omega_\beta$ is unchanged and its inverse temperature is rescaled.
\item Hence no automorphism intertwining the flow carries $\omega_\beta$ to $\omega_{\beta'}$ for $|\beta'| \neq |\beta|$: $|\beta|$ is an invariant of the pair (state, parametrised flow), and the automorphism group acts on the line of KMS states with orbits $\{\beta, -\beta\}$, so that line carries no automorphism-theoretic structure beyond the orientation flip of (2). A condition that singles out one point of the line is therefore either a stipulation of the state itself or a reference to data outside the pair $(\Aa, \alpha)$; by (3), the value of $|\beta|$ is meaningful only relative to a parametrisation of the flow, and it is that parametrisation, the conversion of the flow parameter into geometric time, that the algebra does not supply.
\end{enumerate}

*Provenance:* Transport Lab claim singularity.rate-rigidity-temperature-not-algebra-intrinsic, version 4 (T05 Thm 7.16).

**Fact (imported) 46 (Exponentials of bivectors with scalar square).** Let $A \in \Cl^{2}(V, Q)$ with $A^{2} = \lambda \in \R$ (true for every simple bivector $A = a \wedge b$, and for every bivector when $n \le 3$). Then $A^{2k} = \lambda^{k}$, $A^{2k+1} = \lambda^{k} A$, and $e^{A} = \sum_k A^{k}/k!$ is
\begin{equation}
e^{A} =
\begin{cases}
\cos\theta + \dfrac{\sin\theta}{\theta} A, & \lambda = -\theta^{2} < 0,\\[6pt]
\cosh\theta + \dfrac{\sinh\theta}{\theta} A, & \lambda = \theta^{2} > 0,\\[6pt]
1 + A, & \lambda = 0 .
\end{cases}
\end{equation}
In each case $e^{A} (e^{A})^{\sim} = e^{A} e^{-A} = 1$. For orthogonal $a, b$ with $Q(a) \ne 0$, $e^{\phi\, \hat{a}\hat{b}}$ (unit $\hat{a}, \hat{b}$, or $\hat{b}$ null) is the product of two invertible vectors, hence a rotor (\claimref{obj.std-algebra.rotor}): a rotation when $(a \wedge b)^{2} < 0$, a boost when $> 0$, and a null rotation or translation when $= 0$.

*Provenance:* Transport Lab claim std-algebra.bivector-exponential, version 1.

**Fact (imported) 47 (The product of two vectors).** In $\Cl(V, Q)$, for all $u, v \in V$,
\begin{equation}
v^{2} = Q(v), \qquad u v + v u = 2 B(u, v).
\end{equation}
In particular $u v = B(u, v) + \tfrac12(u v - v u)$, the sum of a scalar and an antisymmetric part.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 48 (Null pairs satisfy the canonical anticommutation relations).** Let $v_1, \dots, v_k, w_1, \dots, w_k \in V$ be a \emph{Witt basis} of their span: $B(v_i, v_j) = B(w_i, w_j) = 0$ and $B(v_i, w_j) = \tfrac12 \delta_{ij}$. Then in $\Cl(V, Q)$
\begin{equation}
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij},
\end{equation}
the canonical anticommutation relations for $k$ modes (read $v_i$ as annihilators, $w_i$ as creators). The elements $N_i = w_i v_i$ are mutually commuting idempotents with $N_i + v_i w_i = 1$. In particular, for orthogonal hyperbolic planes $\operatorname{span}(e_i, e_{k+i})$ of $\R^{k,k}$, $v_i = \tfrac12(e_i + e_{k+i})$ and $w_i = \tfrac12(e_i - e_{k+i})$ form such a basis. The form need not be nondegenerate outside the span.

*Provenance:* Transport Lab claim std-algebra.witt-basis-car, version 1.

**Fact (imported) 49 (The algebraic limit, even charge).** Let $p - q$ be even. The algebraic direct limit of the tower $(T_k, \iota_k)$ is canonically isomorphic to
\[
\varinjlim T_k \;\cong\; \Cl(p,q) \otimes \Mat_{2^\infty}, \qquad \Mat_{2^\infty} := \varinjlim \Mat_{2^k}(\R) \ \ (m \mapsto \operatorname{diag}(m,m)),
\]
the ground algebra tensored with the algebraic $2^\infty$ matrix algebra. Equivalently, $\varinjlim T_k$ is the Clifford algebra of the infinite-dimensional quadratic space $\R^{p,q} \perp H_1 \perp H_2 \perp \cdots$.

*Provenance:* Transport Lab claim tower.algebraic-limit-even-charge, version 3 (T03 Thm 5.3).

**Fact (imported) 50 (The CAR limit, even charge).** Continue with $p - q$ even. Complexifying and completing in the unique C*-norm of the complexified limit (Lemma \claimref{tower.structure-tower-c-norms}): the result is
\[
\Cl(p,q)_\C \,\otimes\, \CAR,
\]
where $\CAR$ is the CAR algebra of countably many fermionic modes, the unique Glimm UHF algebra of type $2^\infty$; the mode operators are represented by the adjoined null vectors themselves via Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, with $w_j = v_j^*$ both for the intrinsic *-structure of Lemma \claimref{tower.structure-tower-c-norms} and for the Fock inner product. The completed tower is the ground algebra tensored with the algebra of a free fermionic quantum field: iterated transport is second quantisation, one mode per rung.

*Provenance:* Transport Lab claim tower.car-limit-even-charge, version 5 (T03 Thm 5.6).

**Fact (imported) 51 (The ladder pairs satisfy the CAR, as vectors).** In $T_k$, the adjoined null pairs satisfy, exactly and at the level of vectors,
\[
v_i v_j + v_j v_i = 0, \qquad w_i w_j + w_j w_i = 0, \qquad v_i w_j + w_j v_i = \delta_{ij}\,,
\]
for all $1 \leq i, j \leq k$: a system of $k$ fermionic modes, with no normal-ordering, no completion, and no representation chosen. Adding a rung adds one mode and touches none of the existing relations.

*Provenance:* Transport Lab claim tower.ladder-pairs-satisfy-car-vectors, version 4 (T03 Prop 4.1).

**Prediction 52 (The no-echo prediction, registered).** The framework's quantum structure lies at the stretched singularity, $r_c = (2M)^{1/3}$ in Planck units, by Postulate \claimref{singularity.c1-curvature-cutoff} (C1): deep inside the hole, at Planck curvature, and nowhere near the horizon, which remains exactly the smooth vacuum horizon of classical general relativity (the exterior dictionary is exact, \cite[Fact 2.1]{ButlerT6}). The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \emph{no} modification, and in particular no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\,M_\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\,M_\odot$): within the sensitivity band of existing detectors. A single statistically confirmed echo train would refute the framework's localisation of quantum structure. The prediction is stated so that it can fail.


