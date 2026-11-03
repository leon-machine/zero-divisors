# The algebra core

**Abstract.** Every result in the Transport Papers is stated in one algebra: the geometric algebra of a space of directions with a rule for their square lengths. This trail walks through its core, from that one rule to rotors, the classification of the real algebras, and the fermion Fock space.

Products of basis directions form a basis of the whole algebra, even when some directions have zero length. Sandwiching between directions carries out every reflection and rotation, and each rotation comes from exactly two rotors, $R$ and $-R$.

Pairs of light-like directions behave exactly like fermion creation and annihilation operators.

The walk starts with the defining rule, builds up grades and symmetries, and ends where the algebra meets quantum theory.

## Clifford algebras and quadratic forms

These results build the geometric algebra from one rule and show what it contains.

The algebra has a single defining rule: a vector $v$ multiplied by itself gives its square length $Q(v)$, a plain number.

Applying that rule to a sum of two vectors $u$ and $v$ gives \[ uv + vu = 2B(u, v), \] where $B$ is the dot product that $Q$ defines. So the product $uv$ is the scalar $B(u, v)$ plus a part that changes sign when the order is swapped.

**Theorem 1 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Rests on:* std-algebra.polarisation

Reordering costs only a sign and a scalar, and a repeated vector collapses to a number, so every product reduces to products $e_I$ of distinct basis vectors in increasing order.

In $n$ dimensions these blades, from $1$ up to the full volume, form a basis, so \[ \dim \Cl(V, Q) = 2^{n} \] This holds when some directions have zero length, which matters because the series works in exactly such degenerate spaces.

**Theorem 2 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Rests on:* std-algebra.existence-uniqueness, std-algebra.vector-squares

Each blade has a grade $k$, the number of vectors in it, so every element splits into scalars, vectors, bivectors and so on.

Three ways of flipping an element act on grade $k$ by a sign: the grade involution, reversion (writing every product backwards) and their composite. Reversion, written with a tilde, acts by \[ \tilde{x} = (-1)^{k(k-1)/2} x \] on grade $k$, and it is the one that undoes rotations later in the walk.

**Theorem 3 (The three involutions on each grade).** The three basic ways of "flipping" an element each multiply every grade by plus or minus one, according to a simple pattern in the grade. Reversion, for example, leaves numbers and arrows alone and changes the sign of planes and volumes.

*Rests on:* std-algebra.functoriality, std-algebra.existence-uniqueness, std-algebra.grade-decomposition

The elements that commute with everything form the centre of the algebra.

With $n$ even only the scalars are central. With $n$ odd the pseudoscalar $\omega = e_1 e_2 \cdots e_n$, the product of all the basis vectors, is central too.

Whether the pseudoscalar squares to plus or minus one decides much of the algebra's shape, as the classification below shows.

**Theorem 4 (The centre).** The centre of an algebra is the set of its elements that commute with everything in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

A vector $u$ with $Q(u) \ne 0$ can be divided by. Sandwiching another vector $x$ between it and its inverse gives \[ x \mapsto -u x u^{-1}, \] the reflection in the mirror perpendicular to $u$.

So the algebra does geometry directly: a mirror is just a vector.

**Theorem 5 (Reflection in a non-null vector).** Multiplying an arrow on both sides by a fixed arrow, with a sign, gives its mirror image in the plane perpendicular to the fixed arrow. This works for any fixed arrow that does not have zero length. Mirrors are the building blocks of all rotations.

*Rests on:* std-algebra.inverse-of-vector, std-algebra.vector-squares, std-algebra.orthogonal-anticommute

Two reflections in a row give a rotation, or a boost in spacetime, and the product of the two vectors is a rotor $R$. A rotor acts on vectors by \[ x \mapsto R x \tilde{R} \]

In a nondegenerate space every such rotation arises this way, and exactly two rotors, $R$ and $-R$, give the same one. This doubling is where spinors come from.

**Theorem 6 (Spin double-covers the special orthogonal group).** Every rotation, and every Lorentz boost, is produced by a rotor, and by exactly two of them, which differ by a sign. This two-to-one relation is the origin of spin one-half: a full turn of space changes the sign of the rotor.

*Rests on:* primer.twisted-adjoint-action, primer.centre, std-algebra.cartan-dieudonne, std-algebra.reflection, std-algebra.inverse-of-vector, std-algebra.orthogonal-anticommute, std-algebra.z2-grading

Light-like vectors, nonzero vectors with $Q(u) = 0$, cannot be divided by, but they come in pairs.

A light-like vector $u$ and a partner $w$ span a hyperbolic plane, and the space splits into as many such planes as possible: \[ V = H_1 \perp \dots \perp H_m \perp A \perp \operatorname{rad} V, \] with $m = \min(p, q)$ and $A$ free of light-like vectors.

The number of these planes is the Witt index, which later in the lab counts quantum capacity.

**Theorem 7 (Hyperbolic pairs and the Witt decomposition).** Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

*Rests on:* std-algebra.sylvester-inertia, std-algebra.polarisation, std-algebra.vector-squares

Adding one hyperbolic plane doubles the matrix size: \[ \Cl(p{+}1, q{+}1) \cong \Mat_2(\Cl(p,q)) \]

Adding eight positive or eight negative directions gives sixteen-by-sixteen matrices over the old algebra. So every real geometric algebra is a matrix algebra over $\R$, $\C$ or $\HH$, or a sum of two such, fixed by $n = p + q$ and by $p - q$ modulo $8$.

**Theorem 8 (Periodicity and the table of real Clifford algebras).** The algebras of all the different spaces fall into a repeating pattern of eight. Each is a table of real, complex or quaternion numbers, sometimes two such tables side by side, and which kind depends only on the difference between the number of space-like and time-like directions, counted round a clock of eight hours.

*Rests on:* std-algebra.tensor-rules, std-algebra.cl11-matrix, std-algebra.blade-basis

Return now to the light-like pairs of a hyperbolic plane.

Chosen as a Witt basis $v_i$, $w_i$, with $B(v_i, w_j) = \tfrac12 \delta_{ij}$, they satisfy \[ v_i w_j + w_j v_i = \delta_{ij}, \] and the $v_i$ anticommute among themselves, as do the $w_i$. These are the canonical anticommutation relations, with $v_i$ annihilating and $w_i$ creating a fermion.

One rule about square lengths therefore already contains the algebra of fermions.

**Theorem 9 (Null pairs satisfy the canonical anticommutation relations).** Inside a Clifford algebra, a direction of space paired with a direction of time produces two zero-length arrows that obey exactly the rules for creating and destroying a fermion. With several such pairs you get several independent fermion modes, without building any Hilbert space first.

*Rests on:* std-algebra.vector-squares

Let the $w_i$ act by adding a direction and the $v_i$ by removing one. This writes the whole algebra as matrices on all combinations of the $w_i$: \[ \Cl(V, Q) \cong \End(\Lambda W) \]

That space is the fermion Fock space, and it sits inside the algebra as the left ideal generated by the vacuum idempotent $f$, so states and operators live in one algebra.

**Theorem 10 (The Fock representation, and the Fock space as a minimal left ideal).** The state space of $k$ fermion modes, with its creation and annihilation operators, already sits inside the Clifford algebra of $k$ space and $k$ time directions. The "empty" state is an element of the algebra, and the other states are obtained by multiplying it by the creation arrows.

*Rests on:* std-algebra.witt-basis-car, std-algebra.existence-uniqueness, std-algebra.blade-basis

## Results cited, not shown

**Fact (imported) 11 (The twisted adjoint action).** Every symmetry of a geometry that preserves lengths can be built from mirror reflections. In a Clifford algebra each reflection is carried out by sandwiching with a single direction, and a product of directions carries out the combined symmetry. This result sets up the sandwich carefully, with a sign twist for products of an odd number of directions, and shows that each length-preserving symmetry comes from exactly two such products, differing by sign.

*Provenance:* Transport Lab claim primer.twisted-adjoint-action, version 3 (T00 Lem 9.2).

**Fact (imported) 12 (The Cartan-Dieudonne theorem).** Every rigid symmetry of a nondegenerate space, including rotations and Lorentz boosts, is a sequence of mirror reflections, never more than the number of dimensions. This is why products of arrows can describe all of them.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the Cartan-Dieudonne theorem; I. R. Porteous, Clifford Algebras and the Classical Groups, Cambridge University Press (1995)., orthogonal groups generated by reflections.

**Fact (imported) 13 (Cl(1,1) and Cl(2,0) are the real 2x2 matrices).** The algebra of one space and one time direction is exactly the familiar algebra of two-by-two real matrices. The light-like directions become the matrices that move one coordinate into the other.

*Provenance:* Transport Lab claim std-algebra.cl11-matrix, version 1.

**Fact (imported) 14 (The Clifford algebra exists and is unique).** The rule "an arrow squared is a number" can always be realised by an actual algebra, and in essentially one way only. One explicit construction lets arrows act on oriented areas and volumes by adding a direction or removing one.

*Provenance:* Transport Lab claim std-algebra.existence-uniqueness, version 1.

**Fact (imported) 15 (Isometries extend to algebra homomorphisms).** If a map of arrows preserves square lengths, it automatically extends to a map of the whole algebra that respects multiplication. Symmetries of space therefore act on everything built from arrows.

*Provenance:* Transport Lab claim std-algebra.functoriality, version 1.

**Fact (imported) 16 (The grade decomposition).** In $n$ dimensions there is one number direction, $n$ arrow directions, $n(n-1)/2$ plane directions and so on, and every element splits uniquely into these parts. The split does not depend on which perpendicular axes are chosen.

*Provenance:* Transport Lab claim std-algebra.grade-decomposition, version 1.

**Fact (imported) 17 (Which vectors and versors are invertible).** An arrow can be "divided by" exactly when its square length is not zero. Arrows of zero length, like light rays, cannot be inverted: multiplying such an arrow by itself gives zero. Products of invertible arrows are always invertible, and their inverse is found by writing the product backwards and dividing by a number.

*Provenance:* Transport Lab claim std-algebra.inverse-of-vector, version 1.

**Fact (imported) 18 (Orthogonal vectors anticommute).** Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 19 (Polarisation).** Knowing the square length of every arrow is the same as knowing the "dot product" of every pair of arrows. Each can be recovered from the other by a short formula.

*Provenance:* Transport Lab claim std-algebra.polarisation, version 1.

**Fact (imported) 20 (Orthogonal bases and the law of inertia).** However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 21 (The tensor product rules).** Adding two extra directions to a space has a predictable effect on its algebra: the new algebra is the old one combined with a small two-dimensional algebra, at the cost of possibly swapping which directions count as space-like and which as time-like. Repeating this explains why the algebras repeat with period eight.

*Provenance:* Transport Lab claim std-algebra.tensor-rules, version 1.

**Fact (imported) 22 (The even subalgebra and the Z2 grading).** Parity multiplies like signs: even with even or odd with odd gives even, mixed gives odd. A product of a $j$-grade and a $k$-grade element can only have grades between their difference and their sum, in steps of two.

*Provenance:* Transport Lab claim std-algebra.z2-grading, version 1.

From the single rule $v^{2} = Q(v)$ the walk has reached rotors, the classification of every real geometric algebra, and the fermion Fock space.

The trail rests on no postulate. Each step is proved in the lab and checked by machine, citing the classical law of inertia and the theorem that every isometry is a product of reflections.
