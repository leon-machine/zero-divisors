# One Complex Unit: The Field Theory of the Transport Series, from the CAR Limit to the Photon (regenerated from the store)

**Abstract.** The tower of the series has the canonical anticommutation relations as its limit; this note asks whether that limit reaches a quantum field theory. It does, in one way. The palatial storey supplies a positive-energy one-particle space, the Penrose transform supplies the mode functions, and the tower's anticommutation relations are the second quantisation over that space. In real geometric algebra the construction needs one operator imaginary unit, and the pseudoscalar $I_4$ serves: it is Lorentz-invariant, and with it positive frequency is positive helicity for every massless field. A massive fermion is then two right-handed fields joined by the epsilon pairing; tower contact interactions give the textbook scattering laws; a tower pairing interaction condenses into a fermion mass; gauge bosons are adjoined as a bosonic Fock space; and the coupled system gives one-photon exchange exactly, for distinguishable and identical fermions. Pointed at the series' gravity prediction, the field theory is consistent with its matter premises and leaves the registered phase unchanged. Pointed at the Standard-Model paper, the assignments survive, and the paper's undetermined orientation is relocated into the relative sign of the twistor's complex unit and the field's. Almost every result is standard physics in the series' algebra; the series' own content is where the one-particle structure comes from, why the commutation relations must be adjoined, and what one complex unit fixes. Exact-arithmetic checks accompany every claim.

## Introduction



**setting  (Introduction).** The relation of T16, $\{e_a, e_b\} = 2g_{ab}$, has two readings: a metric one in an orthogonal basis and the canonical anticommutation relations (CAR) in a Witt basis. The tower of T03 iterates the ascent and has the CAR algebra as its limit. That limit is many-fermion quantum mechanics. Whether it reaches a quantum field theory, with fields on spacetime that are local, covariant and of positive energy, is a different question, and the claim that general relativity and quantum theory are two faces of one object covers field theory only if the answer is yes.

This note collects the answer, built in eight exact-arithmetic runs on 15 and 16 October 2026, each with a preregistration, an independent adversarial review and its corrections. The answer is yes, in one way. The note is a consolidation: each result is stated at its level and cited to the run and check that establish it, and the runs' findings files carry the detail.

The plan. the section ``Setting and imports'' fixes the setting and the imports. the section ``Attaching the modes to spacetime'' attaches the modes to spacetime. the section ``The imaginary units in real geometric algebra'' identifies the imaginary units in real geometric algebra. the section ``Second quantisation in one algebra'' second-quantises multivector-valued fields in one algebra with $i = I_4$. the section ``Mass and contact interactions'' treats mass and contact interactions, the section ``Bosons'' the bosons, and the section ``The photon's Fock space and the coupled system'' the photon's Fock space and the coupled system. the section ``Gravity's source: the registered prediction'' and the section ``The Standard-Model paper's chirality'' point the result at two of the series' own claims: the registered gravity prediction and the Standard-Model paper's chirality. the section ``The ledger'' states what is the series' own, what is imported, and what is open.

**setting  (Prior art).** Second quantisation, Coulomb-gauge quantum electrodynamics and old-fashioned perturbation theory are textbook (Sakurai; Weinberg, \emph{The Quantum Theory of Fields}, vol.~I). The spacetime algebra, its plane waves, its chirality and its photon polarisations are Hestenes' and Doran and Lasenby's; the geometric-algebra treatment of twistors with the conformal pseudoscalar as imaginary unit is Arcaute, Lasenby and Doran's. Two-component spinor technique is Dreiner, Haber and Martin's. The Nambu-Jona-Lasinio mechanism, Weinberg and Witten's theorem, Bjorken's composite photon and Anderson's quasi-spin are standard and credited where used. What the note claims for the series is the placement of these structures in the series' own algebra and storeys, and the consequences of using a single complex unit for all of them.

## Setting and imports



**setting  (Setting and imports).** The ground is $\Cl(1,3)$ with signature $(+,-,-,-)$ and pseudoscalar $I_4 = \gamma_0\gamma_1\gamma_2\gamma_3$, $I_4^2 = -1$. Tower planes $(e_j, f_j)$ with $e_j^2 = 1$, $f_j^2 = -1$ are adjoined after the ground; $v_j = (e_j + f_j)/2$ creates and $w_j = (e_j - f_j)/2$ annihilates. T03's adjoint $*$ is the antiautomorphism with $x^* = x$ on generators of square $+1$ and $x^* = -x$ on generators of square $-1$; so $I_4^* = -I_4$ and $w_j^* = v_j$. Hestenes' unit $\IS = \gamma_2\gamma_1$ acts on the right. The chirality projectors on even elements are $\chi_\pm(\phi) = (\phi \mp I_4\phi\IS)/2$, so that $I_4\phi = \phi\IS$ on $\chi_+$.



**Theorem 1 (Imported: the tower and its limit).** The planes generate the CAR, $\{v_j, w_k\} = \delta_{jk}$, $v_j^2 = w_j^2 = 0$, and the tower's limit is the CAR algebra. \emph{Provenance:} T03, Thm.~thm:carlimit.

*Proof.* Restated from \claimref{tower.car-limit-even-charge} (T03, Thm.~thm:carlimit), where it is proved.




**Theorem 2 (Imported: the statistics no-go and the palatial algebra).** The palatial algebra $[Z^\alpha, \bar Z_\beta] = \hbar\,\delta^\alpha_\beta$ has no nonzero finite-dimensional representation and no embedding into any finite-dimensional algebra. It is realised on polynomials by $\bar Z_\beta = -\hbar\,\partial/\partial Z^\beta$. \emph{Provenance:} T09, Prop.~prop:statistics and Lemma lem:weyl. For the bounded CAR algebra the corresponding statement is the Wielandt-Wintner theorem: no bounded operators satisfy $[a, a^*] = 1$.

*Proof.* Restated from \claimref{correspondence.statistics-no-go} (T09, Prop.~prop:statistics) and \claimref{correspondence.symmetrised-quadratics-palatial-algebra} (T09, Lemma lem:weyl, whose proof uses the polynomial realisation), where they are proved. The closing sentence is the Wielandt-Wintner theorem, which the source cites from the literature.




**Theorem 3 (Imported: one datum for the massive law).** The massive Dirac law in the spacetime algebra needs one geometric datum beyond the field, and the pseudoscalar cannot serve as it. \emph{Provenance:} T16, Lemma lem:onedatum.

*Proof.* Restated from \claimref{one-relation.one-datum-not-two-imaginary-unit} (T16, Lemma lem:onedatum), where it is proved.




**Fact (imported) 4 (Imported: standard field theory).** The Jost-point form of the spin-statistics theorem (Streater and Wightman, ch.~4), whose complex Lorentz path reads in geometric algebra as the rotation of one chirality through $2\pi$, $(1-\Pi) + \Pi\exp(\theta\gamma_1\gamma_2)$ with $\Pi = (1 - E)/2$, ending at conjugation by $E$, the total inversion $x \mapsto -x$ on the conformal model; the Penrose transform, whose kernels the spacetime algebra writes as $x\psi_0\gamma_0/Q(x)^2$ (spin $\tfrac12$), $xBx/Q(x)^3$ (Maxwell) and $1/Q(x)$ (scalar), and its $H^1$ isomorphism with cohomology on regions of the projective spinor space $\PCS$ (projective twistor space); the Weinberg-Witten theorem (massless particles of spin greater than one half carry no charge under a conserved Lorentz-covariant current); the random-phase Goldstone pole of the Nambu-Jona-Lasinio model; the Coulomb-gauge Hamiltonian of quantum electrodynamics; the Adler-Bell-Jackiw anomaly.

*Provenance:* R. F. Streater and A. S. Wightman, PCT, Spin and Statistics, and All That, ch. 4 (the Jost-point form of the spin-statistics theorem; named in the source); The Penrose transform and its H^1 isomorphism (Penrose; named in the source); S. Weinberg and E. Witten, the Weinberg-Witten theorem (named in the source); The random-phase Goldstone pole of the Nambu-Jona-Lasinio model (named in the source); The Coulomb-gauge Hamiltonian of quantum electrodynamics (Sakurai; Weinberg, The Quantum Theory of Fields, vol. I; named in the source); The Adler-Bell-Jackiw anomaly (named in the source).

## Attaching the modes to spacetime





**Theorem 5 (The ground does not attach the modes).** Over the conformal ground every even ground element commutes with every mode operator of every higher plane. In particular the conformal bivectors, the chart translations and the Lorentz rotors act trivially on the modes, so a field $\psi(x) = \sum_j u_j(x)a_j$ on which the ground's translations act covariantly has constant mode functions. The obstruction is finite-dimensionality: a noncompact group has no nontrivial unitary representation on a finite floor.

*Proof.* Proof by exact computation: run \texttt{qft\_2026-10-15}, checks A1.1 to A1.8 and A2; the finite-dimensionality obstruction is the corrected form of A2 after review. The first clause is also a consequence of the tower's structure: $\Omega_{k} = \omega_{1}\cdots\omega_{k}$ squares to one and commutes with every ground generator (Lemma \claimref{tower.volume-elements-planes}), so an even product of ground generators equals the same product of the twisted generators $x\,\Omega_{k}$ and lies in the subalgebra $A_{k}$, which commutes elementwise with the subalgebra $B_{k}$ generated by the planes (Theorem \claimref{tower.commuting-copies}); every mode operator lies in $B_{k}$.




**Theorem 6 (The attachment through conformal spinors).** The attachment available to the series is the one through the conformal spinor space $\CS$ (the twistor attachment): the palatial storey supplies a positive-energy one-particle space with a conformal-group action, the Penrose transform supplies the mode functions, and the tower's CAR is the second quantisation over that space. In the oscillator model the helicity-$s$ module has energies $|s| + 1 + n$ with multiplicity $(n+1)(n + 2|s| + 1)$; the conformal energy is the palatial quadratic of the reversion form $h$ on $\CS$ (the twistor form); the sixteen generators of $\mathfrak{u}(2,2)$, the algebra preserving $h$, preserve each positive-energy, fixed-helicity module. On this attachment the tower's floors are energy cut-offs, not regions of spacetime. Spin-statistics constrains it: a CAR lift is local exactly when $2s$ is odd, and the series' fermion assignments pass.

*Proof.* Proof by exact computation for the oscillator statements (\texttt{qft\_2026-10-15}, A5.1 to A5.5, B2.1); the parity of the two-point kernel (A4.4 to A4.6); the Jost framing and the Penrose isomorphism imported (Fact \claimref{field-theory.imported-standard-field-theory}). The second-quantisation clause rests on \claimref{field-theory.imported-tower-limit}, which supplies the tower's CAR and its limit, the CAR algebra, and the oscillator model on \claimref{field-theory.imported-statistics-no-go-palatial-algebra}, which supplies the palatial algebra and its realisation on polynomials.




**Theorem 7 (The boost on the modes).** On a plane's mode operators the real-rapidity rotor acts by scaling, preserves the CAR, and is not a $*$-map; uniformly over many planes it has no bounded extension to the CAR algebra. The imaginary-rapidity rotor is unitary and acts by phases. So on the modes the series' geometric boost is the imaginary-time (KMS-strip) map, and the unitary real-time flow is the rotor at imaginary rapidity.

*Proof.* Proof by exact computation: \texttt{qft\_2026-10-15}, B1.0 to B1.8. The computation rests on \claimref{field-theory.imported-tower-limit}, which supplies the CAR of the plane mode operators and the CAR algebra as the tower's limit. The reading of T05's premise (R) that follows is flagged in that run as assembly-level and a decision for the author.




**Theorem 8 (The path integral is inside the tower).** Grassmann variables are further rungs. The Grassmann path integral at slicing $M$ gives $\operatorname{Tr}(1 - \delta H)^M$ exactly, and $\operatorname{Tr}\exp(-\beta H)$ and the Fermi-Dirac occupation in the limit; its two-point function is antiperiodic for the trace and periodic for the supertrace at every slicing. The period itself is imported.

*Proof.* Proof by exact computation: \texttt{qft\_2026-10-15}, D1 to D4; D5 assembly. Reading the Grassmann variables as further rungs rests on Fact \claimref{field-theory.imported-tower-limit}: the adjoined null vectors square to zero and anticommute, as Grassmann generators must.


## The imaginary units in real geometric algebra





**Theorem 9 (Where each imaginary unit lives).** \begin{enumerate}
\item The centre of $\Cl^+(1,3)$ is $\mathrm{span}\{1, I_4\}$, and the centre of $\Cl^+(2,4)$ is $\mathrm{span}\{1, I_6\}$ with $I_6 = I_4E$, where $E = e_+e_-$ is the bivector of the ascended plane, $E^2 = 1$, $[I_4, E] = 0$.
\item The conformal spinor space (twistor space) $\CS$ is the minimal left ideal $\Cl^+(2,4)P$; the commutant of the action of $\Cl^+(2,4)$ on $\CS$ is $\mathrm{span}\{1, I_6\}$, so the complex unit of $\CS$ is $\pm I_6$.
\item At a point, $\CS$ splits as $L_0 \oplus L_\infty$, the $E = \pm 1$ eigenspaces, both Lorentz-invariant, and $I_6 = +I_4$ on $L_0$ and $-I_4$ on $L_\infty$: the two chiral doublets.
\item For massless fields the field's complex structure is the pseudoscalar: $\pm I_4$ by helicity sector for Maxwell, and on the chiral subspaces of the Weyl field $I_4$ agrees with Hestenes' right $\IS$ up to the chirality sign. A mass term anticommutes with $I_4$.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{twistor\_ga\_2026-10-16}, E1.1 to E1.7 and E3.1, E3.2. Prior art: (1) to (3) are in Arcaute, Lasenby and Doran; (4) is standard spacetime algebra.


## Second quantisation in one algebra





**Definition 10 (The single-algebra field).** Values are even and chiral elements of the ground; modes are tower planes; the operator imaginary unit is $i = I_4$, which commutes with every mode; physical numbers are read by the projection $\proj$ onto $\mathrm{span}\{1, I_4\}$. The pairing of values is $\ip{\phi}{u} = \alpha(\phi, u) + I_4\,\alpha(\phi\IS, u)$ with $\alpha(\phi, u) = \langle \phi^*u\rangle_0$.



**Theorem 11 (Second quantisation).** With Definition \claimref{obj.field-theory.single-algebra-field}:
\begin{enumerate}
\item $\Lambda(k) = k\gamma_0/(2k_0)$ is the orthogonal projector onto $\ker k$.
\item The field's anticommutator has no tower part and equals $\ip{\phi_1}{\sum_j 2\alpha_j\cos(k_j\cdot\xi)\Lambda(k_j)\chi\,\phi_2}$; in the continuum it is $\chi(\nabla D)\gamma_0$ with $D$ the Pauli-Jordan function, so the field is local.
\item The span$\{1, I_4\}$ part of $\Psi^*M\Psi$ is the second-quantised $d\Gamma(M)$ on particle modes; antiparticle terms need normal ordering.
\item With $i = I_4$ a field carrying both chiralities gives the right-handed part complex-linearly and the left-handed part conjugated. With Hestenes' $i = \IS$ the same field quantises as a whole Dirac field, at the cost of a frame-dependent unit. The split is forced by the choice $i = I_4$, not by the algebra.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{ga\_second\_quantisation\_2026-10-16}, Q1 to Q7 (Q4 at assembly level with one import; Q6 corrected after review). The anticommutator computation rests on \claimref{field-theory.imported-tower-limit}, which supplies the CAR of the tower planes that carry the field's modes.


**Remark  (The choice of unit).** The author adopted $i = I_4$ for the series' field theory on 16 October 2026. The reasons are Lorentz invariance and centrality; the cost is that every field is read in one chirality. Proposition \claimref{field-theory.mass} shows the cost is the standard two-component one.

## Mass and contact interactions





**Theorem 12 (Mass with $i = I_4$).** For the four even right factors $N \in \{\gamma_0\gamma_1, \gamma_0\gamma_2, \gamma_1\gamma_3, \gamma_2\gamma_3\}$ that anticommute with $\IS$, $B_N(\psi, \phi) = \proj(\tilde\psi\phi N)$ is a nonzero, antisymmetric, nondegenerate, Lorentz-invariant, $I_4$-bilinear pairing on $\chi_+$: the epsilon pairing $\lambda^{\mathsf T}\epsilon\lambda$, of charge two under the common phase. A massive Dirac plane wave splits as $\chi + \psi_-$ with $\eta = \psi_-N \in \chi_+$; $\chi$ and $\eta$ have opposite $I_4$-charges, the Dirac equation is the coupled pair, and the mass density is $2B(\chi, \eta)$. The common $I_4$ phase is axial and the mass breaks it. Fact \claimref{field-theory.imported-one-datum-massive-law} stands: $I_4$ is the field algebra's unit, not the massive law's complex structure.

*Proof.* Proof by exact computation: \texttt{ga\_interactions\_2026-10-16}, M1, M2 (the reading corrected after review). The closing clause rests on \claimref{field-theory.imported-one-datum-massive-law}, which supplies that the massive Dirac law needs one geometric datum beyond the field and that the pseudoscalar cannot serve as it.




**Theorem 13 (Contact interactions in the tower).** For two right-handed species the current-current density $H = g J_A\cdot J_B$, built in the single algebra on four particle modes, is self-adjoint, commutes with both charges, and has tower grade four. Its tower matrix element is $\langle A3, B4|H|A1, B2\rangle = g J_A(3,1)\cdot J_B(4,2)$, with $|M|^2/(g^2 s^2) = 1/4$ for spinors normalised to $J^{\mu}(f, f) = k^{\mu}$ (in general $|M|^2/(g^2 c_1c_2c_3c_4\,s^2) = 1/4$ with $J(f_i, f_i) = c_i k_i$) at every configuration tested, in centre-of-mass and boosted frames; with the second species as antiparticles the crossed amplitude gives $|M|^2/(g^2 u^2) = 1/4$ under the same normalisation.

*Proof.* Proof by exact computation: \texttt{ga\_interactions\_2026-10-16}, C1 to C3b.




**Theorem 14 (No canonical commutation relations in the tower).** No floor contains a pair with $[a, a^*] = 1$, and no bounded element of the CAR limit satisfies it. Bosons made of fermions are not excluded by this.

*Proof.* Finite statement proved (\texttt{ga\_interactions\_2026-10-16}, B1, the trace argument of Fact \claimref{field-theory.imported-statistics-no-go-palatial-algebra}); the bounded statement imported (Wielandt-Wintner). The original wording, ``no bosons'', was refuted on review.


## Bosons





**Theorem 15 (Composite scalars, at mean-field level).** \begin{enumerate}
\item The two-mode block $H = K(n_a + n_c) + \mu w_aw_c + \mu^*v_cv_a$, $\mu \in \mathrm{span}\{1, I_4\}$, is self-adjoint, with $\operatorname{ad}_H^2 = K^2 + |\mu|^2$ on all four mode operators and block spectrum $\{K - E, K, K, K + E\}$, $E = \sqrt{K^2 + |\mu|^2}$; with $\mu = mB$ the dispersion is $E^2 = K^2 + m^2$.
\item The tower element $H_4 = \sum_b K(n_a + n_c) - GP^*P$, $P = \sum_b w_aw_c$, is self-adjoint, conserves the axial number, and has exact pair states of energy $2Kn - Gn(n_b - n + 1)$; pairs enter the ground state exactly when $G > 2K/n_b$, the threshold of the mean-field energy.
\item In the block ground state $\langle w_aw_c\rangle = -\mu^*/(2E)$, so the gap equation holds: the fermion mass is $G$ times the pair condensate.
\item The axial phase is an inner unitary of the tower, $U H(\mu) U^* = H(\mu e^{-2\theta I_4})$: the mean-field energy has an exactly flat phase direction.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{ga\_bosons\_2026-10-16}, S1.1 to S3 and S2.5. Mean field only; the massless pole is the imported random-phase result; at finite size the exact ground state has $\langle P\rangle = 0$; the order parameter is a Lorentz scalar but a single shell is frame-dependent; the axial $U(1)$ is anomalous, so with colour the scalar is massive.




**Theorem 16 (Composite gauge bosons: what is excluded).** The GA current transforms as a vector, $J(Sf, Sg) = SJ(f,g)\tilde S$, for every element $S$ of definite parity; so a nonzero vector condensate breaks Lorentz invariance, and a massless composite photon as a Goldstone mode of one (Bjorken) conflicts with the exact Lorentz invariance of the series' exterior. Massless composites charged under a covariant current of the fermions are excluded by Weinberg and Witten. Massive composite vectors and gauge bosons of an emergent gauge symmetry are not addressed. The elementary route was taken because the author chose it, not because it is forced.

*Proof.* \texttt{ga\_bosons\_2026-10-16}, V2 (near-immediate) and V1 (imported, the Weinberg-Witten theorem of \claimref{field-theory.imported-standard-field-theory}). The preregistered verdict ``the composite route fails'' was narrowed to this statement on review.




**Theorem 17 (The elementary photon in GA).** With $i = I_4$ and complex coefficients on the left:
\begin{enumerate}
\item the polarisation $\epsilon_h = t_1 - hI_4t_2$ satisfies $B_q\cdot\epsilon_h = hI_4\epsilon_h$ for the rotation bivector $B_q$ about $q$, on and off the coordinate axes;
\item the geometric product of complex vectors is sesquilinear, $\proj(J\epsilon) = J\cdot\bar\epsilon$, because $I_4$ anticommutes with vectors;
\item the helicity sum $\tfrac12\sum_h\proj(J_A\epsilon_h)\proj(J_B\epsilon_{-h})$ is the transverse product $J_A^\perp\cdot J_B^\perp$;
\item Coulomb-gauge exchange (two time orderings and the instantaneous Coulomb term) equals the covariant $-e^2J_A\cdot J_B/t$, by current conservation;
\item massive vector exchange reduces to the contact term of Proposition \claimref{field-theory.contact-interactions-tower} with $G = e^2/M^2$.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{ga\_bosons\_2026-10-16}, E0 to E4. (4) is arithmetic conditional on current conservation (E1); the GA content is E1 and E2. Clause (4) rests on \claimref{field-theory.imported-standard-field-theory}, which supplies the Coulomb-gauge Hamiltonian, and clause (5) on \claimref{field-theory.contact-interactions-tower}, which supplies the contact term the massive exchange reduces to.


## The photon's Fock space and the coupled system





**Theorem 18 (The Fock space and the Maxwell modes).** \begin{enumerate}
\item On polynomials with $\mathrm{span}\{1, I_4\}$ coefficients, $a_m = \partial/\partial z_m$ and $a_m^* = z_m$ satisfy the CCR exactly, and $a_m^*$ is the adjoint of $a_m$ for $\ip{z^n}{z^{n'}} = n!\,\delta$. This is the representation of Fact \claimref{field-theory.imported-statistics-no-go-palatial-algebra}, with variables indexed by photon modes; the relation to the palatial algebra itself is an analogy, not a construction.
\item For null $k$ the bivectors $f$ with $kf = 0$ form a real two-dimensional, $I_4$-stable space: one $I_4$-complex mode per momentum.
\item The positive-frequency mode $f\exp(-I_4k\cdot x)$ has helicity $+1$. Every massless even spinor, of either chirality, has the left-$I_4$ rotation phase of helicity $+\tfrac12$. So with $i = I_4$, positive frequency is positive helicity for every massless even field.
\item With $i = I_4$ the field operator is the Riemann-Silberstein form $F = \sum N\,2X\,[\exp(-I_4k\cdot x)\,a_+ + \exp(+I_4k\cdot x)\,a_-^*]$: helicity $+1$ annihilated, helicity $-1$ created.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{ga\_photon\_fock\_2026-10-16}, F1.1, F1.2, M1 to M3.2. The registered prediction that photon and fermion helicities agree in sign (M2c) holds and is structural (M2e).




**Theorem 19 (The coupled system at tree level).** On the coupled state space (tower element times polynomial), $H_{\mathrm{int}} = e\sum J^\mu A_\mu$ is self-adjoint and conserves the fermion charges. The second-order amplitude $H_{\mathrm{int}}(E_i - H_0)^{-1}H_{\mathrm{int}} + H_C$, with $H_0$ applied as an operator, equals $-e^2J_A(3,1)\cdot J_B(4,2)/t$ for distinguishable fermions and $-e^2(J_{31}\cdot J_{42}/t - J_{41}\cdot J_{32}/u)$ for identical ones, exactly. Dropping the Coulomb term, one helicity, or the fermionic ordering gives a different amplitude.

*Proof.* Proof by exact computation: \texttt{ga\_photon\_fock\_2026-10-16}, C1 to C4c. The computation rests on \claimref{field-theory.fock-space-maxwell-modes}, which supplies the polynomial Fock space of the photon modes and the field operator, and on \claimref{field-theory.imported-standard-field-theory}, which supplies the Coulomb-gauge Hamiltonian and so the term $H_C$. The coupling does not test $i = I_4$ as such, since $I_4$ commutes with every tower operator.




**Theorem 20 (How close the tower comes to the CCR).** For $n$ tower pairs, $B = \sum_jw_{c_j}w_{d_j}$ gives $[B, B^*] = n - (N_c + N_d)$; with $K_3 = (N_c + N_d - n)/2$ the triple $(B^*, B, K_3)$ is an $\mathfrak{su}(2)$ quasi-spin, the ladder has $n + 1$ states, and $[b, b^*] = 1 - 2k/n$ on $k$-pair states for $b = B/\sqrt{n}$. The CCR is the Inonu-Wigner contraction $n \to \infty$; the operator limit holds only on states of bounded boson number.

*Proof.* Proof by exact computation: \texttt{ga\_photon\_fock\_2026-10-16}, T1 to T3. The computation rests on Fact \claimref{field-theory.imported-tower-limit}, which supplies the CAR of the tower pairs from which $[B, B^{*}]$ and the quasi-spin relations are evaluated, and the CAR algebra in which the contraction $n \to \infty$ is taken.


## Gravity's source: the registered prediction



**setting  (Gravity's source: the registered prediction).** The series registers that gravity entangles two masses, each held in a superposition of two places, by the standard phase $\Phi = (Gm_Am_B/\hbar)\int(1/r_{11} + 1/r_{22} - 1/r_{12} - 1/r_{21})\,dt$, under the element reading, in which the geometry's coefficients lie in a commuting algebra of the matter's number operators. The masses are the field theory's fermions; gravity is not quantised here.



**Theorem 21 (Conserved numbers in a mass block).** On the mass block of Proposition \claimref{field-theory.composite-scalars-mean-field-level}(1) the quasi-particle annihilators $\gamma_a = \alpha w_a + \beta v_c$, $\gamma_c = \alpha'w_c + \beta'v_a$ satisfy $[H, \gamma] = -E\gamma$, and $H = E(N_a + N_c) + (K - E)$ exactly, with $N = \gamma^*\gamma/\{\gamma, \gamma^*\}$. A single rung number does not commute with $H$ when $\mu \neq 0$, and the massive vacuum has $\langle n_a\rangle = (E - K)/(2E)$. The charge $Q = n_a - n_c$ lies in the rung algebra, commutes with $H$, equals $N_a - N_c$ and vanishes on the massive vacuum; one massive quantum is the rung state $v_aP_0$ itself.

*Proof.* Proof by exact computation: \texttt{ga\_gravity\_source\_2026-10-16}, G2, G3, G3b. The computation rests on \claimref{field-theory.composite-scalars-mean-field-level}, which supplies the two-mode block $H$, its self-adjointness and the energy $E = \sqrt{K^2 + |\mu|^2}$.




**Theorem 22 (The operator Newtonian coupling).** With $H_N = -G\sum_{i<j}M_iM_jN_iN_j/r_{ij}$ built from commuting conserved numbers (rung numbers of massless modes, quasi-particle numbers or block charges of massive ones), the branch states are eigenstates and the relative phase $\arg(c_{11}c_{22}/(c_{12}c_{21}))$ under $\exp(-I_4Ht)$ is $+\Phi$, the registered phase with its sign. The operator source gives no interaction between a body's own branches, unlike the mean-field (Schr\"odinger-Newton) source, which entangles nothing. For rigid composite bodies the phase is that of the total mass plus a correction of relative order $(a/R)^2$.

*Proof.* \texttt{ga\_gravity\_source\_2026-10-16}, G4 to G6. The coupling commutes with the numbers by construction, these being the conserved numbers of \claimref{field-theory.conserved-numbers-mass-block}, the masses are inserted, and the composite statement is the Newtonian multipole expansion with additivity and rigidity assumed; the static weak-field limit of the minimal coupling is imported.


**Remark  (What this does to the registration).** Nothing. The registered phase and its wording stand: ``the commuting algebra of the rungs' number operators'' is right when read as the conserved ones, which the block charge supplies inside the rung algebra. A first version of the run proposed changing the wording to quasi-particle numbers; review showed the charge serves equally, and the proposal was withdrawn.

## The Standard-Model paper's chirality





**Theorem 23 (The Standard-Model assignments survive).** T12's content, hypercharges and anomaly cancellation do not involve the complex unit: its listing and its conjugate differ by the outer automorphism $Y \mapsto -Y$, $3 \leftrightarrow \bar 3$, and both are anomaly-free. Of the 64 conjugation patterns of one generation exactly four are anomaly-free, so every multiplet except the self-conjugate $\nu^c$ must enter with the same status relative to $I_4$.

*Proof.* Arithmetic and standard representation theory, computed in run \texttt{ga\_sm\_chirality\_2026-10-16}, checks C3 and C4. The computation rests on \claimref{standard-model.quarks-leptons-two-level-fermion-content} and \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}, which supply the listing of one generation and its hypercharges, and on \claimref{standard-model.imported-anomaly-coefficients}, which supplies the four anomaly-cancellation conditions applied to each of the 64 conjugation patterns.




**Theorem 24 (The orientation is relocated).** \begin{enumerate}
\item Left multiplication by $e_+$ maps the even half $T$ of the conformal spinor module of $\Cl(2,4)$ (the twistor module) onto the odd half $T'$, commutes with $I_4$ and with Lorentz rotors, and swaps the $E$-doublets: $i = I_4$ and Lorentz symmetry alone do not tell $T$ from $T'$.
\item The conformal spinors' unit that commutes with Clifford multiplication is right multiplication by $I_6$, $J$; with $J$ the two halves are inequivalent (conformal spinors and their duals, the twistors and dual twistors), and on the momentum doublet $\ker n_0$, the $E = +1$ doublet of both halves, $J = +I_4$ in $T$ and $J = -I_4$ in $T'$.
\item The commutant fixes the conformal spinors' unit only up to sign. So with the field's unit $I_4$, which half's momentum spinors are complex-linear is the relative sign of the two units.
\end{enumerate}

*Proof.* Proof by exact computation: \texttt{ga\_sm\_chirality\_2026-10-16}, C6a to C6e. The computation rests on \claimref{field-theory.where-each-lives}, which supplies the central unit $I_6 = I_4E$, the commutant $\mathrm{span}\{1, I_6\}$ of the conformal spinor module, and the splitting at a point into the $E = \pm 1$ doublets with $I_6 = \pm I_4$.


**Remark  (How the unit choice moves the orientation bit).** T12's orientation bit, which the dark-matter paper shows the descent cannot derive, is not removed by $i = I_4$; it moves into the relative sign of the conformal spinors' unit ($\pm I_6$, the twistor's unit) and the field's. If the series fixes that sign, and if the label copy's parity is identified with the conformal spinors' (the twistor's; the theorem T12 calls the same missing theorem as Hypothesis (S)), the orientation is fixed, through T12's Fact on the charge and helicity read on the conformal spinor space (twistor charge and helicity), whose conventions were not checked here. Its physical content would be at most the sign of CP violation.

## The ledger



**setting  (What is the series' own).** Three things. (i) Where the field theory's one-particle structure comes from: the palatial storey, not the tower (Proposition \claimref{field-theory.twistor-attachment}); the tower supplies the CAR and nothing about spacetime (Proposition \claimref{field-theory.ground-does-not-attach-modes}). (ii) Why the canonical commutation relations must be adjoined: the tower's own bosons are $\mathfrak{su}(2)$ quasi-spins (Proposition \claimref{field-theory.how-close-tower-comes-ccr}), the field-theory form of T09's statistics no-go. (iii) What one complex unit fixes: with $i = I_4$, positive frequency is positive helicity for every massless field, so the opposite helicities and chiralities enter conjugated in one stroke (Propositions \claimref{field-theory.second-quantisation}(4), \claimref{field-theory.fock-space-maxwell-modes}(3)). The dictionary of Proposition \claimref{field-theory.boost-modes}, the boost on the modes as the KMS-strip map, is transport-convenient: its mathematics is that of any hyperbolic plane, its use the series'.

**setting  (What is standard).** Everything else: two-component mass, Fermi contact scattering, the Nambu-Jona-Lasinio condensate, Coulomb-gauge exchange and the quasi-spin are textbook results reproduced in the series' algebra. None of the runs produced a transport-essential result. The gravity run left the registered prediction unchanged and found its matter premises consistent with the field theory; the Standard-Model run found T12's assignments independent of the unit and relocated, but did not remove, its orientation bit.

**setting  (Decisions taken).** The author chose $i = I_4$ (16 October), composite bosons first and elementary bosons on their failure, then the elementary photon, and then to point the field theory at the gravity prediction and at T12.

**setting  (Open).** (1) Pair creation, antiparticle modes and Compton scattering in the coupled system. (2) Gauge invariance beyond current conservation, and Lorentz covariance of the Coulomb-gauge construction beyond tree level. (3) Loops and renormalisation. (4) Non-abelian gauge fields, which bring the axial anomaly into play. (5) The composite scalar beyond mean field: the Goldstone pole, a covariant regularisation, the sigma mode, and whether the contact term of Proposition \claimref{field-theory.contact-interactions-tower} has an attractive scalar channel. (6) The map from the palatial ladder module's conformal-energy basis to the plane-wave Fock space, which would turn the analogy of Proposition \claimref{field-theory.fock-space-maxwell-modes}(1) into a construction. (7) The terminology conflict recorded in the first run: T03 calls the tower second quantisation and T09 calls the palatial storey second quantisation; on the attachment found here the palatial storey supplies the one-particle space and the tower's CAR over it is second quantisation, which is T03's usage. (8) Whether the Higgs is composite, which the tower supports at mean-field level, or elementary: a modelling decision. (9) The relative sign of the twistor's complex unit and the field's, which now carries T12's orientation, and a check of the conventions of T12's Fact on twistor charge and helicity against T09 and T07. (10) For the gravity prediction: retardation and the radiative sector, non-rigid bodies, and the shared spinor factor of two masses in one tower.

## Machine verification



**setting  (Machine verification).** Every proposition above is established by exact computation in real geometric algebra, with the series' shared library \texttt{GA.py} (Fraction coefficients; Gaussian rationals only for bookkeeping); no floating point is used. The derivation scripts and their independent review scripts are:

\begin{tabularx}{\textwidth}{@{}lXrr@{}}
\toprule
Run & Derivation script & Checks & Review checks\\
\midrule
\texttt{qft\_2026-10-15} & \texttt{verify\_QFT.py} & 80 & 64\\
\texttt{twistor\_ga\_2026-10-16} & \texttt{verify\_TWGA.py} & 55 & 50\\
\texttt{ga\_second\_quantisation\_2026-10-16} & \texttt{verify\_GA2Q.py} & 19 & 25\\
\texttt{ga\_interactions\_2026-10-16} & \texttt{verify\_INT.py} & 20 & 31\\
\texttt{ga\_bosons\_2026-10-16} & \texttt{verify\_BOS.py} & 23 & 30\\
\texttt{ga\_photon\_fock\_2026-10-16} & \texttt{verify\_PHO.py} & 22 & 41\\
\texttt{ga\_gravity\_source\_2026-10-16} & \texttt{verify\_GRV.py} & 12 & 12\\
\texttt{ga\_sm\_chirality\_2026-10-16} & \texttt{verify\_SMC.py} & 12 & 15\\
\midrule
Total & & 243 & 268\\
\bottomrule
\end{tabularx}

The consolidated runner \texttt{verify\_FT.py} runs the eight derivation scripts from their folders and reports each count; all pass. Each run's findings file lists the checks by class (proof-carrying, near-immediate, controls, imports), records the review's findings and the corrections applied, and states what the checks do not show. All counts above are from runs in exact arithmetic on 15 and 16 October 2026.

## Results cited, not shown

**Fact (imported) 25 (The statistics no-go).** The palatial algebra admits no nonzero finite-dimensional representation, and no embedding of unital algebras into any finite-dimensional algebra; in particular none into $\Cl(2,4)$ or $\Cl(2,4)_\C$, of dimension $64$.

*Provenance:* Transport Lab claim correspondence.statistics-no-go, version 2 (T09 Prop 5.1).

**Fact (imported) 26 (Symmetrised quadratics of the palatial algebra).** For $M \in \mathfrak{gl}(4,\C)$ with entries $M^\beta{}_\alpha$ set
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

**Fact (imported) 27 (One datum, not two: the imaginary unit is the rest frame read through the law).** Align the representative so that $C = Iu$. The complex structures the descent of step (4) needs are the constant even $J$ with $J^{2} = -1$ commuting with $C$, so that the plane-wave factor $\exp(-Jp \cdot x)$ passes through $C$. The commutant of $C$ in $\Cl^{+}(1,3)$ is four-dimensional, spanned by $1$ and the three bivectors of the $3$-space orthogonal to $u$ (for $u = \gamma_{3}$: $1, \gamma_{0}\gamma_{1}, \gamma_{0}\gamma_{2}, \gamma_{1}\gamma_{2}$); the pseudoscalar, though even and a square root of $-1$, anticommutes with $C$ and is excluded. On the commutant $J^{2} = -1$ iff the scalar part vanishes and the bivector part has unit timelike-signature norm, a two-sheeted hyperboloid. The map $J \mapsto \gamma_{0} := CJ$ is a bijection from that hyperboloid onto the unit timelike vectors orthogonal to $u$, with inverse $J = C^{-1}\gamma_{0}$. So, given the law, choosing the imaginary unit and choosing the rest frame are one choice, not two. The joint commutant of $(C, J)$ in $\Cl^{+}(1,3)$ is $\mathrm{span}\{1, J\}$, whose rotors form the $U(1)$ of rotations in the spin plane, Hestenes' electromagnetic phase, which minimal coupling already uses. Any laboratory frame can be aligned: if the laboratory's $\gamma_{0}$ is not orthogonal to the representative's $u$, a rotor of the freedom of Lemma \claimref{one-relation.odd-square-roots-chiral-phase} realigns $u$, and that freedom is used up there, once, and is not to be counted again as the empty freedom of step (3).

*Provenance:* Transport Lab claim one-relation.one-datum-not-two-imaginary-unit, version 3 (T16 Lem 5.6).

**Fact (imported) 28 (Hypercharge from the global form, pair counting, and consistency).** With $Y$ the hypercharge defined before Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}, and with Hypothesis (S) wherever a doublet at the level of one conformal spinor (a twistor-level doublet) enters:
\begin{enumerate}
\item (Under (S).) The one-handed listing keeps the states of even total mode number and conjugates the odd ones, or the reverse; the choice is the particle-antiparticle orientation. Write $(j, k)$ for the component of the five-mode state space with $j$ slot modes and $k$ pair modes occupied (mode counts, not the pair of representation dimensions used elsewhere in this paper, for which see the caption of a figure of the original). In the listing that keeps the quark doublet, the component $(1,1)$, as a particle, the lepton doublet is the full conformal spinor, the component $(1,3)$, $Y_{L} = -1/2$, and the empty conformal spinor, the component $(1,0)$, appears only as its conjugate (here both phrases name doublet components of the one-slot listing; the neutrino paper uses ``empty'' and ``filled conformal spinor'' for the grade-zero and grade-three singlets of the single-spinor sector, different objects, Proposition \claimref{neutrino.empty-twistor}). The $[SU(2)]^{2}U(1)$ anomaly coefficient of the two doublets, $3Y_{Q} + Y_{L}$ with the three the colour multiplicity, is then the identity $3 \cdot \tfrac16 - \tfrac12 = 0$; it would equal $1$ if the empty conformal spinor were listed as the particle instead, so the anomaly confirms the orientation the listing fixed. Pair counting fixes $|Y_{L}/Y_{Q}| = 3$; the parity fixes the sign.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, like Proposition \claimref{standard-model.quarks-leptons-two-level-fermion-content}(3).) Listed by the handedness of (1), the sector of a single conformal spinor gives the singlet spectrum. Here $\CS = \Lambda^{\mathrm{even}}W$, the conformal spinor space, and $\CSm{} = \Lambda^{\mathrm{odd}}W$ are the two chirality halves (Fact \claimref{standard-model.imported-pair-systems-two-chirality-halves}), and the listing keeping the even grades and conjugating the odd ones gives
\[
(1)_{0} \;\oplus\; (\bar{3})_{-2/3} \;\oplus\; (\bar{3})_{+1/3} \;\oplus\; (1)_{+1},
\]
that is $\nu^{c}$, $u^{c}$, $d^{c}$, $e^{c}$ with hypercharges $0, -\tfrac23, +\tfrac13, +1$: the observed singlet spectrum, with the fourth singlet at hypercharge zero. (The listing by the opposite handedness is the conjugate of this one, the same spectrum in the opposite convention.) Under (S) the grade-$k$ states of a single conformal spinor are the $(0, k)$ components, the states with no slot mode and $k$ pair modes occupied (their content $\Lambda^{k}\C^{3}$ and weight $-2k$ match, and irreducibles are determined by content and weight), so their parity is the total parity and this listing is the same listing as in (1).
\item (Consistency, and uniqueness given the content; under (S) for the doublets.) With the content of (1) and (2), all four anomaly conditions of Fact \claimref{standard-model.imported-anomaly-coefficients} hold. Conversely, for the field content $Q = (2,3)$, $L = (2,1)$, $u^{c} = (1,\bar{3})$, $d^{c} = (1,\bar{3})$, $e^{c} = (1,1)$, all listed in one handedness, together with a fourth singlet of hypercharge zero or no fourth singlet, and $Y_{Q} = 1/6$ as the normalisation, the four conditions determine $Y_{L}$, $Y(e^{c})$ and $\{Y(u^{c}), Y(d^{c})\}$ uniquely, and the solution is the spectrum of (1) and (2). Both hypotheses are necessary: with a fourth singlet of unconstrained hypercharge the conditions admit a one-parameter family, and if the doublets were listed in the opposite handedness from the singlets the $[SU(3)]^{2}U(1)$ and cubic sums would be $-\tfrac23$ and $+\tfrac49$ rather than zero.
\end{enumerate}

*Provenance:* Transport Lab claim standard-model.hypercharge-global-form-pair-counting-consistency, version 5 (T12 Thm 5.5).

**Fact (imported) 29 (Imported: the anomaly coefficients).** For a gauge group with a $U(1)$ factor acting on left-handed Weyl fermions, with the $U(1)$ charges $Y$, the four anomaly-cancellation conditions are: $[SU(3)]^{2}U(1)$, the sum of $Y$ over the colour triplets and antitriplets (each weighted by its $SU(2)$ multiplicity) vanishes; $[SU(2)]^{2}U(1)$, the sum of $Y$ over the weak doublets (each weighted by its colour multiplicity) vanishes; $U(1)^{3}$, the sum of $Y^{3}$ over all Weyl fermions vanishes; and mixed gravitational, the sum of $Y$ over all Weyl fermions vanishes. A right-handed Weyl fermion of charge $Y$ enters the conditions as a left-handed one of charge $-Y$ in the conjugate representation. The four conditions are necessary for the consistency of the gauge theory, and a failure of any of them is not lifted by spontaneous breaking: an anomalous $U(1)$ cannot be gauged whether or not it is broken. \emph{Provenance:} \cite[\S 22.4]{WeinbergQFT2}.

*Provenance:* S. Weinberg, The Quantum Theory of Fields, Vol. 2: Modern Applications, Cambridge University Press (1996)., \S 22.4.

**Fact (imported) 30 (Quarks and leptons: the two-level fermion content).** Under $S(U(2) \times U(3))$, with $Y$ the hypercharge just defined:
\begin{enumerate}
\item (Unconditional.) The pair-level generators, the cells of the tensor state space, transform as $(2, 3)$ with abelian weight $q = 1$, so $Y = 1/6$: the quark doublet's representation. A single pair has one unit of hypercharge.
\item (Under Hypothesis (S).) The states with one slot mode occupied and the pair modes in an $SU(3)$-invariant configuration are $\C^{2} \otimes \Lambda^{0}W$, weight $3$ ($Y = +1/2$, total mode number one, odd), and $\C^{2} \otimes \Lambda^{3}W$, weight $-3$ ($Y = -1/2$, total mode number four, even); both transform as $(2, 1)$. Without (S) neither exists in the state space, whose only row-filling states form the quadruplet $(4,1)$ of weight $+3$.
\item (Unconditional as a computation on the Fock space of a single conformal spinor, with the pair-slot factor acting alone; that Fock space is not a subspace of the tensor state space, and under (S) it is the row $j = 0$.) In the sector of a single conformal spinor (the single-twistor sector) $\Lambda^{\bullet}W = \Lambda^{\bullet}\C^{3}$, the grade-$k$ states transform as $\Lambda^{k}\C^{3}$, that is as $1, 3, \bar{3}, 1$ for $k = 0, 1, 2, 3$, with weight $q = -2k$: $Y = 0, -1/3, -2/3, -1$.
\end{enumerate}
In particular, under (S), the fermion content of the composite at the particle handedness (Theorem \claimref{standard-model.hypercharge-global-form-pair-counting-consistency}) is
\begin{equation}
(2,3)_{1/6} \oplus (2,1)_{-1/2},
\end{equation}
quark doublet plus lepton doublet, with colour neutrality of the lepton the statement that a state with its pair modes full is an $SU(3)$ singlet: a lepton is a complete conformal spinor, one slot with the pair system full, while a quark is one slot with one pair.

*Provenance:* Transport Lab claim standard-model.quarks-leptons-two-level-fermion-content, version 5 (T12 Prop 5.3).

**Fact (imported) 31 (The CAR limit, even charge).** Continue with $p - q$ even. Complexifying and completing in the unique C*-norm of the complexified limit (Lemma \claimref{tower.structure-tower-c-norms}): the result is
\[
\Cl(p,q)_\C \,\otimes\, \CAR,
\]
where $\CAR$ is the CAR algebra of countably many fermionic modes, the unique Glimm UHF algebra of type $2^\infty$; the mode operators are represented by the adjoined null vectors themselves via Proposition \claimref{tower.ladder-pairs-satisfy-car-vectors}, with $w_j = v_j^*$ both for the intrinsic *-structure of Lemma \claimref{tower.structure-tower-c-norms} and for the Fock inner product. The completed tower is the ground algebra tensored with the algebra of a free fermionic quantum field: iterated transport is second quantisation, one mode per rung.

*Provenance:* Transport Lab claim tower.car-limit-even-charge, version 5 (T03 Thm 5.6).

**Fact (imported) 32 (Commuting copies).** Inside $T_k$, let $B_k$ be the subalgebra generated by the $2k$ plane generators $e_1, f_1, \dots, e_k, f_k$, and let $A_k$ be the subalgebra generated by the twisted base generators $x^{(k)} := x\,\omega_1 \omega_2 \cdots \omega_k$ for $x$ among the ground generators. Then: $B_k \cong \Cl(k,k) \cong \Mat_{2^k}(\R)$; $A_k \cong \Cl(p,q)$ via $x \mapsto x^{(k)}$ (the twisted generators satisfy the ground Clifford relations); $A_k$ and $B_k$ commute elementwise; and multiplication $A_k \otimes B_k \to T_k$ is an isomorphism of algebras,
\[
\Cl(p{+}k, q{+}k) \;\cong\; \Cl(p,q) \otimes \Mat_{2^k}(\R) \;=\; \Mat_{2^k}(\Cl(p,q)).
\]
The isomorphism is canonical given the ordered planes, and compatible with the tower embeddings up to the twist tracked in the section ``The CAR limit''.

*Provenance:* Transport Lab claim tower.commuting-copies, version 5 (T03 Thm 3.2).

**Fact (imported) 33 (Volume elements of the planes).** Let $\omega_j = e_j f_j$. Then $\omega_j^2 = 1$; $\omega_j$ anticommutes with $e_j$ and $f_j$; $\omega_j$ commutes with $e_i, f_i$ for $i \neq j$ and with every ground generator; and the $\omega_j$ commute pairwise. Hence $\Omega_k := \omega_1 \cdots \omega_k$ satisfies $\Omega_k^2 = 1$, commutes with all ground generators, and anticommutes with each $e_j, f_j$, $j \leq k$.

*Provenance:* Transport Lab claim tower.volume-elements-planes, version 5 (T03 Lem 3.1).

**Refutation 34 (The raw representation content matches the fermion table entry by entry).** Refuted. The corrected statement: The disagreements are composites; generators, not states, are the content, and the lepton lies one level higher, under the declared hypothesis of slot statistics.


