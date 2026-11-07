---
id: synthesis.kernel-bivector-is-the-unit-of-hermitian-boson-fields-on-the-tower
kind: claim
version: 1
title: 'The kernel bivector is the even unit of Hermitian boson fields on the tower'
status: proved
region: synthesis
subject: quantum-fields
tags: [bosonisation, car-algebra, pseudoscalar-and-centre, grading-and-parity]
proposed_by:
  kind: ai
  session: 2026-11-07-boson-items
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: run 2026-11-07-boson-items
review: draft
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.volume-elements-planes@5
  - tower.commuting-copies@5
  - synthesis.plane-commutant-even-ground@3
  - tower.structure-tower-c-norms@10
  - tower.ladder-pairs-satisfy-car-vectors@4
  - std-algebra.orthogonal-anticommute@1
  - std-algebra.pseudoscalar-commutation@1
  - std-algebra.bivector-exponential@4
  - synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom@1
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum@1
  - synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes@1
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_hyperbolic_tower_has_no_unit
- kind: check
  ref: check.py::check_kernel_bivector_commutes_with_transport_and_is_antihermitian
- kind: check
  ref: check.py::check_commutant_of_transport_is_a_quaternion_algebra
- kind: check
  ref: check.py::check_level_pseudoscalar_is_J_on_each_parity_sector
- kind: check
  ref: check.py::check_hermitian_pair_with_unit_J
- kind: check
  ref: check.py::check_density_modes_with_unit_J
- kind: check
  ref: check.py::check_sign_of_J_and_the_phase_circle
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum
  - synthesis.n-plus-null-ground-state
extraction:
  note: >-
    Answers the remark closing clause (vii) of
    synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum: a Weyl form with
    self-adjoint boson fields needs a central unit, which a block's even algebra lacks. Stored already and
    cited, not refiled: for N = 1 the centraliser of the radial atom in Cl(1,3) is the quaternion algebra
    span{1, J, e_0e_1e_2, e_0e_1e_3} with even unit +-J, J* = -J, J sigma = +I_4 and I_4 P_+- = +-J P_+-
    (synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom (i), (iii)); the commutant of the
    planes on a floor is the twisted copy of the ground algebra (tower.commuting-copies), here read with
    ground Cl(0,2); in the limit only the even ground algebra survives, and for n even the centre of the even
    ground algebra is span{1, omega} with omega^2 = (-1)^{r/2} (synthesis.plane-commutant-even-ground (i),
    (ii)), whose r = 0 case is the central part of (i) here; the edge operator, the hopping ladder and the
    block commutators (fluctuation-forms (ii), (iii), (v)). New to the store (not new mathematics): (i), (iii),
    (iv) and the Lemma of (v) are standard Clifford and CCR algebra (the centre of the even subalgebra of an
    even-dimensional Clifford algebra; Mat_{2^N}(H) = Cl(0,2) (x) Mat_{2^N}(R) has commutant H of the factor
    Mat_{2^N}(R); a complex structure commuting with a family of canonical pairs), new to the store only in
    this tower reading. In that sense: (i) the commutant of the even part in
    the whole of Cl(N, N) has no odd part, for every N, so no unit at all; (ii)-(iii) for every N, with the
    radial plane counted among the transport planes, the commutant of transport in Cl(N, N+2) is the
    quaternion algebra span{1, J, Gamma e_2, Gamma e_3} with unique even unit +-J, and the contrast that with
    the radial plane in the ground the even commutant is Cl^+(1,3), where I_4 and J (and others) both serve;
    (iv) I_n = J Gamma on every level; (v) the Hermitian fields phi = X + X*, pi = J(X* - X) with
    [phi, pi] = 2 J [X, X*], the collective and density instances, and the lemma giving the Hermitian
    canonical relations with any unit u (u^2 = -1, u* = -u) commuting with a family of canonical pairs;
    (vi) the reflection automorphism that fixes transport and reverses J, and the phase circle e^{theta J Q/2},
    which is the case s = (1/2, -1/2, 1/2, ...) of the diagonal mode rotation U_s of
    synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes (i) (stored with this one and used for the
    product formula, unitarity and the action on modes, not re-derived here).
    The identification in (vi) of the sign of J with the orientation datum of Premise (N+) is argued (it
    goes through J = I_4 sigma and the datum as stated in synthesis.n-plus-null-ground-state, which is cited
    and not used, so that this result does not rest on (N+)). No imported Fact is a premise and no
    imaginary unit is used: every unit is J, I_4 or I_n, never identified. Prior art, orientation only,
    cited from memory: writing canonical commutation relations of self-adjoint fields needs a complex
    structure commuting with the field algebra (Segal's quantisation of a symplectic space with a compatible
    complex structure). Ledger: transport-absent as derived (finite Clifford algebra of a tower level;
    "transport" here names the tower's hyperbolic planes, not a transport completion).
---

## formal
Let $N \ge 1$ and let $L_{N} = \Cl(N, N{+}2)$ be the tower level with orthogonal generators $e_{0}, e_{1}, e_{2}, e_{3}$ ($Q = +1, -1, -1, -1$) and the tower planes $(e_{j}', f_{j}')$, $Q(e_{j}') = 1$, $Q(f_{j}') = -1$, $j = 1, \dots, N - 1$ (floor $N - 1$ of the tower on $\Cl(1,3)$, Theorem \claimref{tower.commuting-copies}), read through the Witt decomposition of its vector space: the anisotropic kernel $\mathrm{span}\{e_{2}, e_{3}\}$, of signature $(0,2)$, orthogonal to $N$ hyperbolic (transport) planes, the radial plane $(e_{0}, e_{1})$ (mode $0$) and the tower planes (modes $1, \dots, N - 1$). $B_{N}$ is the subalgebra generated by the $2N$ plane generators. For a plane $(e, f)$, $v = \tfrac12(e + f) = a^{*}$, $w = \tfrac12(e - f) = a$, $n = vw$, $\omega = ef$; $\Gamma = \prod_{\text{planes}}\omega$; $J = e_{2}e_{3}$; $\sigma = e_{0}e_{1}$; $I_{4} = e_{0}e_{1}e_{2}e_{3}$; $I_{n}$ is the product of all $2N + 2$ generators in the order listed; $*$ is the frame adjoint of Theorem \claimref{tower.structure-tower-c-norms} on the real level (the antiautomorphism fixing the generators of square $+1$ and negating those of square $-1$).
\begin{enumerate}
\item[(i)] \emph{(No unit in the hyperbolic tower.)} In $\Cl(N,N)$, generated by $N$ hyperbolic planes alone, the commutant of the even subalgebra is $\mathrm{span}\{1, \Gamma\}$, $\Gamma^{2} = +1$, and $(\alpha + \beta\Gamma)^{2} = \alpha^{2} + \beta^{2} + 2\alpha\beta\Gamma$: no element that commutes with every even element squares to $-1$. Inside the transport algebra, self-adjoint boson fields (even elements) have no unit that commutes with all bosonic elements.
\item[(ii)] \emph{(The kernel bivector.)} In $L_{N}$, $J^{2} = -1$, $J^{*} = -J$, and $J$ commutes with every plane generator, hence with all of $B_{N}$ (every mode $v_{j}, w_{j}$ and every pair); $J = I_{4}\sigma$.
\item[(iii)] \emph{(The commutant of transport is a quaternion algebra.)} The commutant of $B_{N}$ in $L_{N}$ is $\mathrm{span}\{1, J, \Gamma e_{2}, \Gamma e_{3}\}$, with $(\Gamma e_{2})^{2} = (\Gamma e_{3})^{2} = -1$ and $(\Gamma e_{2})(\Gamma e_{3}) = J = -(\Gamma e_{3})(\Gamma e_{2})$: a quaternion algebra, the twisted copy of the ground $\Cl(0,2)$. Its even part is $\mathrm{span}\{1, J\}$, and $\pm J$ are its only even elements of square $-1$; they are also its only units fixed by the rotors $e^{\varphi J}$ of the kernel plane, which turn $(\Gamma e_{2}, \Gamma e_{3})$ through $2\varphi$. In the tower's limit only $\mathrm{span}\{1, J\}$ commutes with every plane (Theorem \claimref{synthesis.plane-commutant-even-ground}(i) with ground signature $(0,2)$). The uniqueness needs the radial plane among the transport planes: if $(e_{0}, e_{1})$ is counted in the ground $\Cl(1,3)$ and only the tower planes as transport ($N \ge 2$), the even part of their commutant is $\Cl^{+}(1,3)$ (of dimension $8$), which contains $I_{4}$, $J$, $e_{1}e_{2}$ and $e_{1}e_{3}$, all of square $-1$; then $J$ and $I_{4} = J\sigma$ both commute with transport.
\item[(iv)] \emph{(The level pseudoscalar.)} $I_{n} = J\Gamma$, $I_{n}^{2} = -1$, $I_{n}^{*} = -I_{n}$; $\Gamma^{*} = \Gamma = \prod_{j}(1 - 2n_{j})$, the fermion parity, which anticommutes with every $v_{j}, w_{j}$ and commutes with every product of two. Hence $I_{n}\tfrac12(1 \pm \Gamma) = \pm J\tfrac12(1 \pm \Gamma)$: $I_{n} = J$ on even and $-J$ on odd fermion number. $\operatorname{Ad}(I_{n})$ is the grade involution of $L_{N}$, which on $B_{N}$ is $\operatorname{Ad}(\Gamma)$. $I_{n}$ and $J$ are not identified.
\item[(v)] \emph{(Hermitian boson fields with unit $J$.)} For every $X \in B_{N}$, $\phi_{X} = X + X^{*}$ and $\pi_{X} = J(X^{*} - X)$ are self-adjoint and $[\phi_{X}, \pi_{X}] = 2J[X, X^{*}]$; for $X, Y \in B_{N}$ with $[X, Y] = 0$, $[\phi_{X}, \pi_{Y}] = J([X, Y^{*}] + [Y, X^{*}])$ and $[\phi_{X}, \phi_{Y}] = [\pi_{X}, \pi_{Y}] = [X, Y^{*}] - [Y, X^{*}]$.
\begin{itemize}
\item \emph{Collective pairs.} For $N = 2M$ and $S = \sum_{k=0}^{M-1}v_{2k}w_{2k+1}$, $\phi = \phi_{S}$, $\pi = \pi_{S}$: $[\phi, \pi] = 2J\sum_{k}(n_{2k} - n_{2k+1})$ exactly. With $P_{\mathrm{pol}} = \prod_{k}n_{2k}(1 - n_{2k+1})$, $SP_{\mathrm{pol}} = 0$, $X_{j} = (S^{*})^{j}P_{\mathrm{pol}}$ is nonzero for $j \le M$ and zero for $j = M + 1$, and $[\phi, \pi]X_{j} = 2(M - 2j)JX_{j}$; so $\Phi = \phi/\sqrt{2M}$, $\Pi = \pi/\sqrt{2M}$ satisfy $[\Phi, \Pi]X_{j} = (1 - 2j/M)JX_{j}$: the Hermitian canonical relation $[\Phi, \Pi] = J$ holds exactly on the polarised element and, at fixed $j$, as $M \to \infty$.
\item \emph{Density modes.} On a window of the $N$ modes, $\rho_{q} = \sum_{k=0}^{N-1-q}v_{k}w_{k+q}$ ($1 \le q \le N - 1$) satisfy $[\rho_{q}, \rho_{q'}] = 0$ and $[\phi_{\rho_{q}}, \pi_{\rho_{q}}] = 2J(\sum_{k<q}n_{k} - \sum_{k \ge N-q}n_{k})$; for $2q \le N$ and $E_{q} = \prod_{k<q}n_{k}\prod_{k \ge N-q}(1 - n_{k})$ (the filled sea's edge-clean projector), $[\phi_{\rho_{q}}, \pi_{\rho_{q}}]\psi = 2qJ\psi$ whenever $E_{q}\psi = \psi$.
\item \emph{Lemma.} In any real $*$-algebra, let $u^{2} = -1$, $u^{*} = -u$, and let $u$ commute with a family $X_{q}$ with $[X_{q}, X_{q'}] = 0$ and $[X_{q}, X_{q'}^{*}] = c_{q}\delta_{qq'}$, $c_{q} > 0$ real. Then $\Phi_{q} = (X_{q} + X_{q}^{*})/\sqrt{2c_{q}}$ and $\Pi_{q} = u(X_{q}^{*} - X_{q})/\sqrt{2c_{q}}$ are self-adjoint and $[\Phi_{q}, \Pi_{q'}] = u\,\delta_{qq'}$, $[\Phi_{q}, \Phi_{q'}] = [\Pi_{q}, \Pi_{q'}] = 0$. The canonical relations of Theorem \claimref{synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum}(vi) on its domain $\mathcal{D}$ have this form with $X_{q} = \rho_{q}$, $c_{q} = q$, for any unit $u$ of that representation commuting with the band modes; such a $u$ is not exhibited here (the one-particle unit there is $I_{4}$ on $\mathfrak{h}$, not an element of the CAR algebra).
\end{itemize}
\item[(vi)] \emph{(The sign of $J$ and the phase circle.)} The map $\alpha$ with $e_{3} \mapsto -e_{3}$ and every other generator fixed extends to a $*$-automorphism of $L_{N}$; it fixes $B_{N}$ pointwise and $\sigma$, and sends $J \mapsto -J$, $I_{4} \mapsto -I_{4}$, $I_{n} \mapsto -I_{n}$, $(\phi_{X}, \pi_{X}) \mapsto (\phi_{X}, -\pi_{X})$. So nothing in the transport algebra fixes the sign of $J$; given $\sigma$, it is the orientation of $I_{4}$ ($J = I_{4}\sigma$). With $Q = \sum_{k}(n_{2k} - n_{2k+1})$ and $U_{\theta} = e^{\theta JQ/2} = \prod_{k}(1 - n_{2k} + n_{2k}e^{\theta J/2})(1 - n_{2k+1} + n_{2k+1}e^{-\theta J/2})$, the diagonal mode rotation with weights $s_{2k} = \tfrac12$, $s_{2k+1} = -\tfrac12$ of \claimref{synthesis.ladder-bosons-inherit-spin-statistics-from-the-single-modes}(i), which gives the product form, unitarity and the action on the modes, $U_{\theta}$ is unitary, $U_{\theta}SU_{\theta}^{*} = e^{\theta J}S$, and $(\phi, \pi) \mapsto (\phi\cos\theta - \pi\sin\theta, \phi\sin\theta + \pi\cos\theta)$, which keeps $[\phi, \pi]$. The phase $e^{\theta J} = \cos\theta + J\sin\theta$ has period $2\pi$; it is the rotor of the kernel plane, $\operatorname{Ad}(e^{\theta J})$ turns $e_{2}, e_{3}$ through $2\theta$ and fixes $B_{N}$ pointwise, and $e^{\pi J} = -1$ is the rotor of the turn by $2\pi$.
\end{enumerate}
Clauses (i) to (vi) are proved. \emph{Reading (argued).} The orientation of $I_{4}$ relative to time is the datum that Premise (N$_{+}$) assumes (\claimref{synthesis.n-plus-null-ground-state}); by (vi), with $\sigma$ fixed, it is the sign of $J$, which now orients both the fermion phase flow $v \mapsto e^{-Jt}v$ of \claimref{synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom}(iv) and the boson relation $[\Phi, \Pi] = +J$ of (v): reversing it reverses both together.

## technical
A boson field written as a self-adjoint pair needs a unit: something that squares to $-1$, is anti-self-adjoint, and commutes with the fields. The tower's hyperbolic planes alone do not supply one. In $\Cl(N,N)$ the elements commuting with every even element are $\alpha + \beta\Gamma$, with $\Gamma$ the product of the plane volume elements, and these square to $\alpha^{2} + \beta^{2} + 2\alpha\beta\Gamma$, never $-1$. A tower level over spacetime is $\Cl(N, N{+}2)$, whose vector space is $N$ hyperbolic planes, the radial plane among them, plus a two-dimensional kernel of square $-1$. The kernel bivector $J = e_{2}e_{3}$ squares to $-1$, is anti-self-adjoint, and commutes with every mode operator. The whole commutant of the transport algebra is a quaternion algebra $\mathrm{span}\{1, J, \Gamma e_{2}, \Gamma e_{3}\}$, and $\pm J$ is its only even unit, the one the kernel rotations fix, and the only one surviving in the tower's limit. The level pseudoscalar is $I_{n} = J\Gamma$, which equals $J$ on even and $-J$ on odd fermion number; the two are not identified. With $J$, any transport element $X$ gives the self-adjoint fields $\phi = X + X^{*}$ and $\pi = J(X^{*} - X)$, and $[\phi, \pi] = 2J[X, X^{*}]$. For the collective hopping pair $S$ of $M$ blocks this is $2J$ times the edge count $\sum(n_{2k} - n_{2k+1})$, so the normalised fields satisfy $[\Phi, \Pi] = (1 - 2j/M)J$ on the $j$-th rung of the polarised ladder; for density modes of a window it is $2qJ$ on the filled sea's edge-clean projector. A lemma gives the full Hermitian canonical relations for any family of commuting canonical pairs and any commuting unit. Uniqueness of $J$ depends on counting the radial plane as a transport plane: with the radial plane in the ground, the even commutant of the tower planes is the even spacetime algebra, where $I_{4}$ (the field theory's unit) and $J$ both serve. Finally, reflecting $e_{3}$ is an automorphism that fixes every transport element and reverses $J$ and $I_{4}$ together, so the sign of $J$ is not fixed by the fermions; given the radial plane's orientation it is the orientation of $I_{4}$, which we read (argued, not proved) as the datum Premise (N$_{+}$) assumes. The boson phase circle is $e^{\theta J}$, implemented inside the level by $e^{\theta JQ/2}$; it is the kernel plane's rotor, and its value $-1$ at $\theta = \pi$ is the rotor of a full turn.

## lay
Quantum fields that describe bosons, the particles that can share a state, are usually written as pairs of real quantities whose commutator is the imaginary unit. The graph builds everything from fermions living in a tower of planes, so it has to find that unit inside its own algebra. The planes alone have none: nothing that commutes with all their pairs squares to minus one. The extra two directions of spacetime that are not part of any plane, the two directions along a horizon's sphere, supply one: the product of those two directions squares to minus one and commutes with every fermion operation. Counting the time-radial plane among the planes, it is the only such element of the right type (if that plane is left out, the field theory's own unit also works), it is what survives at the top of the tower, and with it the collective pairs of fermions give boson fields with the standard commutator, exactly in the states where the bosons were already known to appear. Its sign is a free choice that nothing among the fermions fixes, and it can be read, as an argument rather than a proof, as the same choice that the series' premise about horizons makes when it fixes the direction of time relative to the imaginary unit.

## one-liner
In the tower level $\Cl(N, N{+}2)$ the commutant of the $N$ hyperbolic planes (the radial plane $(e_{0}, e_{1})$ counted as mode $0$; with it in the ground, $I_{4}$ also serves) is the quaternion algebra $\mathrm{span}\{1, J, \Gamma e_{2}, \Gamma e_{3}\}$ with unique even unit $\pm J = \pm e_{2}e_{3}$ (the planes alone have none), $I_{n} = J\Gamma$, and $\phi = X + X^{*}$, $\pi = J(X^{*} - X)$ are self-adjoint with $[\phi, \pi] = 2J[X, X^{*}]$, giving $2J\sum_{k}(n_{2k} - n_{2k+1})$ for collective pairs; the sign of $J$ is fixed by nothing in transport.
