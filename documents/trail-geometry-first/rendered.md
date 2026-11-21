# Geometry first: from the bit to the numbers

**Abstract.** Most accounts of geometric algebra start from the real numbers and put geometry on top. This trail goes the other way: it starts from a single distinction, something or nothing, and asks how much of the algebra and how many of the numbers follow from it.

From that distinction, an order that matters by one extra bit, and whole-number counting, the algebra of directions appears with its one rule, a direction times itself gives its squared length, as a consequence. Division then brings in the fractions, completion the real numbers, and the complex numbers and quaternions turn up as members of the family. The walk ends with the switch: setting and clearing a bit are exactly the rules of one particle of matter.

Each step adds one assumption or one consequence, in the order the note Geometry First (T0a) builds them.

The assumptions are choices about mathematics, not claims about nature, and the trail names each one where it enters.

## What we assume

**Postulate 1 (Premise (F4): the coefficients are completed to a complete ordered field).** This is a starting assumption of the mathematics underneath the series, not a statement about the physical world: the numbers used as coefficients are taken to be the real numbers, the number line with no gaps. Everything built before it uses only whole numbers and fractions. Fractions together with square roots of positive numbers are enough to rescale every direction until its square is plus one, minus one or zero, so the gap-free line is needed only where limits are taken, for example to define the number $\pi$ or a smooth rotation by any angle.

**Postulate 2 (Premise (F2): minimal non-commutativity).** This assumption, again a choice about mathematics rather than a claim about nature, lets the order of two different distinctions matter, but only by the smallest possible amount: swapping them flips one extra on-off bit. That one bit is where the minus sign comes from (read later, in the series, as the sign behind rotation), and with it the possibility of different kinds of directions, some squaring to plus one and some to minus one. Which directions are of which kind is left open.

**Postulate 3 (Premise (F3): superposition over the integers).** The third starting assumption, like the first two a choice about mathematics and not a claim about nature, is that the on-off patterns can be added together and counted with whole numbers, with the special swap bit counting as minus one. Nothing beyond whole numbers is assumed: fractions come later from division, and the continuum of real numbers needs a separate assumption. With this step the whole-number form of the algebra of directions used throughout the series appears.

**Postulate 4 (Premise (F1): the bit).** This is the starting assumption of the whole construction, and it is a choice about mathematics, not a claim about nature: the simplest possible difference, something versus nothing, where doing the same thing twice undoes it. Many such differences, independent of one another, give a collection of on-off patterns. These patterns already have the shape of the algebra of directions used throughout the series, but none of its geometry yet: no sign, no order and no lengths.

## Clifford algebra structure

The steps below build the algebra of directions from below: first its shape, then its numbers, then what a single bit does.

Take a handful of independent distinctions, each either made or not. Let the order in which two of them are made matter, but only by the smallest amount: one extra bit that flips when they are swapped.

That bit has to behave like a minus sign, and once the patterns can be added with whole numbers the algebra of directions appears, with \[ v^{2} = Q(v) \] for every direction $v$ as a theorem rather than a rule. Which version of the algebra one gets is decided by a yes-or-no table of the signs.

**Theorem 5 (The group of signed directions and its integer Clifford algebra).** Start with a handful of independent yes-or-no distinctions and allow them to depend on the order in which they are made, by the smallest possible amount: one extra bit that flips when two distinctions are swapped. That bit has to behave like a minus sign, and every combination of distinctions then squares to plus or minus one. Allowing whole-number combinations of these distinctions produces, with no further assumption, the whole-number form of the algebra of directions used throughout the series, which becomes that algebra once the coefficients are extended, with the rule that a direction times itself gives its squared length coming out as a consequence rather than being assumed. Which version of the algebra one gets is decided entirely by a yes-or-no table of the signs.

So far only whole numbers have been used. A direction $v$ with $Q(v) \neq 0$ can be undone exactly when $Q(v)$ can be divided by, \[ v^{-1} = v / Q(v), \] and asking that every such direction be undone forces in every fraction.

Division does not remove everything: in the algebras with both kinds of direction, light-like directions that square to zero survive it.

**Theorem 6 (Division in the integer Clifford algebra gives the rationals).** In the algebra built from whole-number combinations of directions, an arrow multiplied by itself gives a whole number. Undoing that multiplication means dividing by the number, and asking that every arrow which can be undone actually be undone forces in every fraction: dividing by an arrow three times as long as a unit arrow already produces one third. So the fractions are what division makes of the whole numbers. Division does not get rid of everything, though: in some of these algebras light-like arrows, which square to zero, survive it, and in all but three of them so do other elements whose product is zero.

The next step is the one assumption that is not algebraic: the number line is taken to have no gaps.

With it, every way of measuring lengths and times can be rescaled until each basic direction counts as plus one, minus one or zero, and how many of each there are does not depend on the directions chosen. With fractions alone this fails, which is why the step is needed.

**Theorem 7 (Completion recovers the real Clifford algebras; Sylvester's law of inertia in GA).** If the number line is taken to have no gaps, every way of measuring lengths and times in a flat space can be rescaled until each basic direction counts as plus one, minus one or zero, and how many of each there are does not depend on the directions chosen. This holds as soon as positive numbers have square roots, which needs much less than the full number line. With fractions alone it fails: a direction whose square is $2$ cannot be rescaled to square $1$, and some planes then behave differently, for example having no elements that multiply to zero. Under that assumption, all the algebras the store uses are the ones built earlier from whole numbers and fractions, extended to real coefficients.

*Rests on:* std-algebra.polarisation, std-algebra.orthogonal-anticommute, std-algebra.blade-basis, std-algebra.functoriality, std-algebra.existence-uniqueness, conformal.minimal-nondegenerate-completion

With the real numbers in hand, the familiar number systems can be looked for inside the algebra.

The only finite number systems in which one can always divide are the real numbers, the complex numbers and the quaternions, and all three are algebras of directions: one direction squaring to minus one gives the complex numbers, two give the quaternions. They are members of the family the bit produces, not extra ingredients.

**Theorem 8 (Frobenius in GA; every finite-dimensional associative real algebra in a corner of Cl(k,k)).** If the number line has no gaps, then the only finite-dimensional number systems in which one can always divide, and in which multiplication is associative though not necessarily commutative, are the real numbers, the complex numbers and the quaternions. All three are algebras of directions: the complex numbers come from one direction whose square is minus one, the quaternions from two. The proof finds the quaternions as the most such directions can give, because a third direction is forced to be the product of the first two. Every other finite associative number system, including split-complex and dual numbers and all matrices, sits inside one of these algebras of directions, though the same could be said of matrices.

*Rests on:* std-algebra.complex-numbers, std-algebra.quaternions, std-algebra.orthogonal-anticommute, std-algebra.blade-basis, transport.exceptional-division-algebras, std-algebra.witt-basis-car, std-algebra.fock-representation, std-algebra.matrix-units

The last two steps ask what a single bit can do.

Setting a bit and clearing it, with the facts that setting twice is useless and that the bit is always either set or clear, are exactly the rules of one particle of matter. Adding and subtracting the two operations gives one direction that squares to plus one and one that squares to minus one, the pair the series adds at each step, with whole numbers only.

**Theorem 9 (Set and clear of a bit generate the hyperbolic plane).** Think of a light switch with two operations: switch on and switch off. Switching on something that is already on does nothing useful, and at any moment the light is either on or off. Written as algebra, those two facts are exactly the rules physicists use for a single particle of matter. From the two operations alone, by adding and subtracting them, one gets two directions, one that squares to plus one and one that squares to minus one, which is the pair of directions the series adds at each step. No halves are needed along the way.

The other order of construction does not give the same thing.

The algebra of directions built with whole numbers can flip a two-state system, but it contains no operation that sets or clears it; those need halves. Starting from the switch gives them at once.

**Theorem 10 (The integer Clifford algebras contain no idempotent and no switch).** Build the algebra of directions using whole numbers only. It can flip a two-state system from one state to the other, but it contains no operation that asks ``is it on?'' and no operation that switches on or switches off. Those appear only once halves are allowed. Starting instead from the switch gives them straight away, with whole numbers.

## Results cited, not shown

**Fact (imported) 11 (Minimal nondegenerate completion).** A geometric algebra built on a degenerate metric has directions that pair to zero with everything, and division fails along them. This result says how to enlarge the space so that the metric becomes nondegenerate: each degenerate direction needs exactly one new partner direction, and the enlarged metric gains one positive and one negative direction for each degenerate one. The smallest such enlargement is unique up to a symmetry that leaves the original space untouched. Minimality here is among enlargements of the underlying space, not among all algebras.

*Provenance:* Physics Graph result conformal.minimal-nondegenerate-completion, version 6 (T02 Thm 2.3).

**Fact (imported) 12 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Provenance:* Physics Graph result std-algebra.blade-basis, version 1.

**Fact (imported) 13 (The complex numbers inside Clifford algebras).** The imaginary unit of the complex numbers is the oriented unit square of a plane. Multiplying an arrow in the plane by it turns the arrow through a right angle, and complex numbers are numbers plus multiples of that square.

*Provenance:* Physics Graph result std-algebra.complex-numbers, version 3.

**Fact (imported) 14 (The Clifford algebra exists and is unique).** The rule "an arrow squared is a number" can always be realised by an actual algebra, and in essentially one way only. One explicit construction lets arrows act on oriented areas and volumes by adding a direction or removing one.

*Provenance:* Physics Graph result std-algebra.existence-uniqueness, version 1.

**Fact (imported) 15 (The Fock representation, and the Fock space as a minimal left ideal).** The state space of $k$ fermion modes, with its creation and annihilation operators, already sits inside the Clifford algebra of $k$ space and $k$ time directions. The "empty" state is an element of the algebra, and the other states are obtained by multiplying it by the creation arrows.

*Provenance:* Physics Graph result std-algebra.fock-representation, version 1.

**Fact (imported) 16 (Isometries extend to algebra homomorphisms).** If a map of arrows preserves square lengths, it automatically extends to a map of the whole algebra that respects multiplication. Symmetries of space therefore act on everything built from arrows.

*Provenance:* Physics Graph result std-algebra.functoriality, version 1.

**Fact (imported) 17 (Matrix units give a matrix algebra over the corner).** If an algebra contains elements that behave exactly like the basic building blocks of matrices, then the algebra is a matrix algebra: every element can be written as a square array of entries from a smaller algebra. The plane with one space and one time direction gives the simplest example, ordinary $2 \times 2$ matrices.

*Provenance:* Physics Graph result std-algebra.matrix-units, version 1.

**Fact (imported) 18 (Orthogonal vectors anticommute).** Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

*Provenance:* Physics Graph result std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 19 (Polarisation).** Knowing the square length of every arrow is the same as knowing the "dot product" of every pair of arrows. Each can be recovered from the other by a short formula.

*Provenance:* Physics Graph result std-algebra.polarisation, version 2.

**Fact (imported) 20 (The quaternions inside Clifford algebras).** Hamilton's quaternions, invented to describe rotations, are the oriented unit planes of ordinary space together with the ordinary numbers. Their strange multiplication rules are the geometric product of planes.

*Provenance:* Physics Graph result std-algebra.quaternions, version 1.

**Fact (imported) 21 (Null pairs satisfy the canonical anticommutation relations).** Inside a Clifford algebra, a direction of space paired with a direction of time produces two zero-length arrows that obey exactly the rules for creating and destroying a fermion. With several such pairs you get several independent fermion modes, without building any Hilbert space first.

*Provenance:* Physics Graph result std-algebra.witt-basis-car, version 1.

**Fact (imported) 22 (The exceptional division algebras).** In most Clifford algebras some nonzero elements multiply to zero, so division sometimes fails. This result lists the only exceptions: the real numbers, the complex numbers and the quaternions. Allowing pairs of these as well gives exactly the algebras in which no nonzero element has a power equal to zero.

*Provenance:* Physics Graph result transport.exceptional-division-algebras, version 3 (T01 Prop 3.2).

Along the trail, the algebra of directions and its numbers were built from one distinction, an order that matters by one bit, whole-number counting, division and completion. The switch shows the two orders of construction meet in one particle of matter.

The trail rests on four premises of the foundation, the bit, minimal non-commutativity, whole-number superposition and completion, together with the demand that directions be undone. None is a claim about the physical world; that this is the algebra of physics is argued in T0a, not proved.
