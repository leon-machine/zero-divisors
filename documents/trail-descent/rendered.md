# Descent, parity and states

**Abstract.** Climbing the tower adds fermionic modes; descent is the way back down, from the enlarged algebra to what an observer can see. For a single mode it keeps the occupation data and erases the quantum coherence between empty and occupied.

That erasure is the same as averaging over fermion parity. Whatever the starting state, what survives can be read as a thermal state at one temperature.

For an entangled horizon pair, under a geometric premise fixing the period, the temperature is the Hawking temperature. The walk ends by asking what it costs to keep what the descent throws away, and finds that parity sets the price.

The walk first says what descent is, then shows how it makes states look thermal, and finally weighs the cost of undoing it. Each result appears after the ones it rests on.

## Descent, parity and states

This section follows a single fermionic mode down from the enlarged algebra and then asks what the journey lost.

Everything here concerns one fermionic mode, a slot that is either empty or occupied, built from a null pair $v$, $v^*$. With the projector $P = v^* v$, the descent keeps the diagonal of a two by two block and discards the rest: \[ E\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} a & 0 \\ 0 & d \end{pmatrix} \]

The entries $a$ and $d$ are the occupation data; $b$ and $c$ are the coherences that make the mode a quantum superposition. This is the basic operation the rest of the walk studies.

**Theorem 1 (The descent, and what it erases).** A single fermionic mode can be described by a two-by-two matrix. The descent keeps the two diagonal entries, which record whether the mode is empty or occupied, and discards the two off-diagonal entries, which record quantum coherence between those two possibilities.

*Rests on:* std-algebra.witt-basis-car, std-algebra.cl11-matrix

The erasure has a cleaner description in terms of symmetry. Averaging an observable with its parity-flipped version gives exactly the descent: \[ E(x) = \tfrac12\bigl(x + \sigma x \sigma\bigr) \]

So $E$ is the unique conditional expectation onto the parity-even observables, it kills the odd sector, and every parity-even state passes through it unchanged.

**Theorem 2 (The descent is the parity average).** The descent, which keeps a mode's occupation data and discards its coherences, is the same thing as averaging over fermion parity: take an observable and its parity-flipped version and average the two. This makes it the only consistent projection onto the parity-even observables, and it leaves every parity-even state unchanged.

*Rests on:* singularity.descent-what-it-erases

Once coherences are gone, a mode is left with just two probabilities. Any such pair can be written as a thermal (Gibbs) state, \[ E_k(\varrho_k) = \frac{e^{-\beta_k \omega_k N_k}}{Z_k} \] for a unique inverse temperature $\beta_k$, whatever state the mode started in, provided its weight $\omega_k$ is not zero.

So the thermal form after descent comes for free; the open question is which temperature.

**Theorem 3 (The descended form is state independent).** Once the descent has removed a mode's coherences, what remains is just the probability of the mode being empty or occupied. Any such pair of probabilities can be read as a thermal state at exactly one temperature, allowing the extreme cases at either end. This holds whatever state the system started in, provided the mode has nonzero weight.

*Rests on:* singularity.descent-parity-average

To fix the temperature one needs a clock, and the mode supplies its own. Its null pair combines into a single element \[ \sigma = v^* v - v v^* , \qquad \sigma^2 = 1 , \] which in the hyperbolic atom is the unit boost bivector $e_0 e_1$ of the plane.

The rotor flow of $\sigma$ scales $v$ and $v^*$ by opposite weights, as a boost does to outgoing and ingoing horizon modes, and its spectral projectors are exactly the occupation projectors the descent uses. So the clock is not a choice.

**Theorem 4 (Modular structure of the completed pair).** A pair of mutually adjoint elements that each square to zero, like the creation and annihilation operators of a fermion, combines into a single element that behaves as a boost, the geometric operation relating observers in relative motion. This one element plays three roles at once: it generates the boost, it counts whether the mode is occupied, and it produces the two projections later used to discard coherences. Among flows built from real rotations of this small two-dimensional algebra, the boost is the only one, up to its speed and direction.

*Rests on:* singularity.descent-what-it-erases, singularity.pseudo-inverse-identities-hyperbolic-atom, std-algebra.bivector-exponential

A mode at a horizon comes with a partner on the other side, and the joint state of the two matters. If that joint state is unchanged by the boost, apart from a phase, and genuinely entangled, it must have the form \[ \Omega = \cos\theta\,|00\rangle + \sin\theta\,|11\rangle \] with both coefficients nonzero.

The entanglement pairs empty with empty and occupied with occupied, and only the balance $\theta$ between the two terms is left free.

**Theorem 5 (Schmidt forcing, proved outright).** Take one mode together with its partner. If their joint state is unchanged by the boost, apart from an overall phase, and is genuinely entangled, then there is no freedom in which basis the entanglement uses: it must pair empty with empty and occupied with occupied. Only the balance between those two terms is left free.

With the shape of the pair's state fixed, descent to one side can be computed. A pure, boost-invariant, entangled pair state descends to a state that is KMS (thermal) for the flow $\operatorname{Ad}(e^{it\sigma/2})$ at some inverse temperature $\beta$, but these conditions alone leave $\beta$ free, its sign included.

Adding the geometric normalisation (R), which ties the state's intrinsic time to the horizon's period, gives exactly the Hawking temperature with Fermi-Dirac occupation. The conditions are sufficient, not necessary.

**Theorem 6 (Modular descent).** Suppose the quantum state of a horizon mode and its partner is pure, unchanged by the boost, and genuinely entangled across the pair. Then what is seen on one side is thermal, although these conditions alone do not fix the temperature, not even its sign. Adding the premise that ties the state's intrinsic time to the geometric period of the horizon gives exactly the Hawking temperature, with a Fermi-Dirac occupation for each mode. The conditions are enough for this conclusion but are not required for it.

*Rests on:* angle.imported-theorems-deliver-their-hypotheses

The walk now turns from what descent produces to what it destroys. Written with the parity monomials $\G^{\kappa}$ of the modes, the descent on the even sector of $\nu$ modes is \[ \EN(\rho) = 2^{1-\nu}\sum_{\kappa_{\nu} = 0}\G^{\kappa}\rho\,\G^{\kappa} \] half the flips it needs in general.

On a single mode it changes nothing. For a pair it sends $c\ket{00} + s\ket{11}$ to $\operatorname{diag}(c^{2}, s^{2})$, erasing precisely the coherence that makes the pair entangled.

**Theorem 7 (Kraus form of the descent on even states).** The descent can be written as an average of a state over a set of parity flips. On states of even fermion parity, half of those flips are redundant, so only half as many are needed. For a single mode nothing changes, and for a pair the descent erases precisely the coherence that makes the pair entangled.

*Rests on:* descent-lift.imported-descent-modes-univalence-supplied-class, descent-lift.imported-stinespring-kraus-choi

If descent erases entanglement, one can ask what it would cost to keep it in an extra record instead, a so-called lift. An even lift needs $2^{\nu-1}$ orthonormal even record states, and the even sector of $k$ rungs has dimension $2^{k-1}$, so for $\nu \geq 2$ the record needs $k \geq \nu$ rungs: one rung of the tower per mode.

Such a lift exists with $\nu$ rungs, on a record prepared in a paired state. Preparing that state from an empty record, though, needs dynamics that changes particle number.

**Theorem 8 (The lift costs one rung per mode, and needs a pairing).** The descent throws away part of the information in a set of two or more fermionic modes, and one can ask what it costs to keep that information in an extra record instead. Because physical states must have even fermion parity, the record needs one extra mode for every mode of the system, one more in total than a parity-blind count would give. An explicit way to do it exists: prepare the record in a paired state and apply a coupling the framework already supplies. Starting from an empty record, however, preparing that paired state needs a process that changes the particle number, which no number-conserving dynamics can provide.

*Rests on:* descent-lift.imported-stinespring-kraus-choi, descent-lift.imported-fermionic-operations-are-even-reduced

The count of one rung per mode looks generous for a pair, so the next result asks where the extra rung comes from. For an entangled pair, two one-rung recipes exist as maps: Stinespring's minimal dilation and the occupation copy.

Both are odd, so neither is an operation the univalence rule allows, and nothing else stands in the way. Parity alone forces the second rung.

**Theorem 9 (Parity alone forces the second rung).** For an entangled pair of modes, a single extra record mode would be enough to store what the descent discards if parity did not matter. Both natural one-mode recipes work as maps, but both break the rule that fermion parity is conserved. Restoring parity is the only thing the second record mode is needed for.

*Rests on:* descent-lift.lift-costs-one-rung-per-mode

A worked example shows the lift in action. For the series' sample pair, with $(c, s) = (\tfrac45, \tfrac35)$, the two-rung lift is the pure, even four-mode state \[ c\,\ket{00} \otimes (\ket{00} + \ket{11}) + s\,\ket{11} \otimes (\ket{00} - \ket{11}) \] up to normalisation.

The pair's marginal is $\operatorname{diag}(\tfrac{16}{25}, \tfrac{9}{25})$, exactly the classical shared bit the descent leaves. The entanglement has not gone: it now sits between pair and record, with the same Schmidt coefficients.

**Theorem 10 (The classical shared bit is the reduced view of a pure four-mode state).** Take the series' sample entangled pair of modes, with amplitudes four fifths and three fifths. When the descent turns it into a classical shared bit, the lost coherence can be kept, using the two-rung lift, by a record made of two extra modes. The pair and record together are then in a single pure state, and the classical bit is simply what the pair looks like when the record is ignored. The entanglement that was between the two modes is now between the pair and the record, with the same strengths.

*Rests on:* descent-lift.lift-costs-one-rung-per-mode

## Results cited, not shown

**Fact (imported) 11 (Imported: the theorems that deliver $2\pi$, and their hypotheses).** These are the standard theorems of quantum field theory that produce the factor $2\pi$ behind the Unruh and Hawking temperatures. They say that when energy is positive and the theory respects relativity and locality, the natural internal clock of the region on one side of a horizon is the horizon's boost, running at a fixed rate. The entry records their hypotheses, since those are what any attempt to use them must supply.

*Provenance:* J. J. Bisognano and E. H. Wichmann, On the duality condition for a Hermitian scalar field, J. Math. Phys. 16 (1975), 985--1007.; J. J. Bisognano and E. H. Wichmann, On the duality condition for quantum fields, J. Math. Phys. 17 (1976), 303--321.; H.-J. Borchers, The CPT-theorem in two-dimensional theories of local observables, Commun. Math. Phys. 143 (1992), 315--332.; P. D. Hislop and R. Longo, Modular structure of the local algebras associated with the free massless scalar field theory, Commun. Math. Phys. 84 (1982), 71--85.; R. Brunetti, D. Guido and R. Longo, Modular structure and duality in conformal quantum field theory, Commun. Math. Phys. 156 (1993), 201--219.; G. L. Sewell, Quantum fields on manifolds: PCT and gravitationally induced thermal states, Ann. Phys. 141 (1982), 201--224.; B. S. Kay and R. M. Wald, Theorems on the uniqueness and thermal properties of stationary, nonsingular, quasifree states on spacetimes with a bifurcate Killing horizon, Phys. Rep. 207 (1991), 49--136.; W. G. Unruh, Notes on black-hole evaporation, Phys. Rev. D 14 (1976), 870--892..

**Fact (imported) 12 (Imported: the descent on modes, univalence, and the supplied class).** This entry gathers background results from the earlier black-hole singularity work. Erasing a mode's ladder is the same as averaging over its parity; by the univalence premise (P), physical states are restricted to even fermion parity; and, under the boundary-mode locality premise, the dynamics the framework supplies never creates or destroys pairs of particles, the exclusion of such pairing terms being itself a premise. It also fixes the example used throughout: an entangled pair whose single-mode views are thermal, at amplitudes four fifths and three fifths.

*Provenance:* Transport Lab claim descent-lift.imported-descent-modes-univalence-supplied-class, version 8 (T05-descent-lift Fact 1.2).

**Fact (imported) 13 (Imported: fermionic operations are even, and reduced states are restrictions).** For fermions, the operations one can actually perform must preserve whether the particle number is even or odd. Looking at part of a fermionic system means restricting attention to the operators on that part, and when the rest has even parity this matches the usual recipe of tracing it out. Two independent subsystems can always be combined when one of them has even parity.

*Provenance:* S. B. Bravyi, A. Yu. Kitaev, Fermionic quantum computation, Ann. Phys. 298 (2002) 210--226.; H. Araki, H. Moriya, Joint extension of states of subsystems for a CAR system, Commun. Math. Phys. 237 (2003) 105--122., Thm.~1; G. C. Wick, A. S. Wightman, E. P. Wigner, The intrinsic parity of elementary particles, Phys. Rev. 88 (1952) 101--105..

**Fact (imported) 14 (Imported: Stinespring, Kraus, Choi).** Any physically allowed quantum process can be viewed as a reversible interaction with an environment that is afterwards ignored. The smallest environment that does the job is fixed by a single matrix built from the process, and every other way of doing it is that smallest one with extra room added. These are the classical theorems of Stinespring, Kraus and Choi.

*Provenance:* W. F. Stinespring, Positive functions on $C^*$-algebras, Proc. Amer. Math. Soc. 6 (1955) 211--216.; K. Kraus, States, Effects, and Operations: Fundamental Notions of Quantum Theory, Lecture Notes in Physics 190, Springer (1983).; M.-D. Choi, Completely positive linear maps on complex matrices, Linear Algebra Appl. 10 (1975) 285--290..

**Fact (imported) 15 (Pseudo-inverse identities, and the hyperbolic atom).** Two elements that each square to zero can still act as partial inverses of one another: multiplying one by the other and then by the first again returns the first. Neither has a true inverse. Such a pair already lives in the algebra of a single plane with one space-like and one time-like direction, called the hyperbolic atom, which is the one building block of transport that, at the level of elements, needs no ascent of its own.

*Provenance:* Transport Lab claim singularity.pseudo-inverse-identities-hyperbolic-atom, version 4 (T05 Lem 4.1).

**Fact (imported) 16 (Exponentials of bivectors with scalar square).** Turning by an angle in a plane is the exponential of the plane piece times the angle, just as $e^{i\theta}$ turns by $\theta$ in the complex plane. Planes whose square is positive give boosts instead of rotations, and planes containing a zero-length direction give the simplest motions of all, written exactly as one plus the plane piece.

*Provenance:* Transport Lab claim std-algebra.bivector-exponential, version 1.

**Fact (imported) 17 (Cl(1,1) and Cl(2,0) are the real 2x2 matrices).** The algebra of one space and one time direction is exactly the familiar algebra of two-by-two real matrices. The light-like directions become the matrices that move one coordinate into the other.

*Provenance:* Transport Lab claim std-algebra.cl11-matrix, version 1.

**Fact (imported) 18 (Null pairs satisfy the canonical anticommutation relations).** Inside a Clifford algebra, a direction of space paired with a direction of time produces two zero-length arrows that obey exactly the rules for creating and destroying a fermion. With several such pairs you get several independent fermion modes, without building any Hilbert space first.

*Provenance:* Transport Lab claim std-algebra.witt-basis-car, version 1.

Descent is parity averaging, it makes every mode look thermal, and for a pure, boost-invariant, entangled horizon pair the temperature is Hawking's once premise (R) fixes the period.

For two or more modes, undoing it costs one rung per mode, a price set by the univalence rule that physical states have even fermion parity. Those two conditions, univalence and the geometric normalisation, are the ones this trail leans on, and both appear as stated conditions in the results rather than as separate assumptions.
