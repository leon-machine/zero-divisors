# Clifford algebra structure

**Abstract.** A Clifford algebra is built from a space of directions together with a rule for their lengths, and this trail is a primer on its structure. Products of basis directions form a basis of the whole algebra, even when the length rule is degenerate. Sandwiching by directions carries out every length-preserving symmetry, each one coming from exactly two such products that differ by sign. Every real Clifford algebra is a table of real, complex or quaternion numbers, or a pair of such tables, in a pattern that repeats every eight steps. The trail ends by showing that the position in that pattern belongs to the geometry, not to the bare algebra. These are the tools the other algebra trails rely on.

The walk starts with the multiplication table, moves through symmetries and the special product of all directions to the classification, and ends with matrix enlargements and what the geometry adds to the bare algebra.

## Clifford algebra structure

These results describe a Clifford algebra from the inside: its basis, its symmetries, its centre, and its place in a classification.

A Clifford algebra multiplies directions, and the first thing to know is what a basis of it looks like. The products of basis directions, called blades, form a basis of the algebra for any length rule, degenerate or not, and for any choice of basis directions, perpendicular or not. The multiplication table depends polynomially, and so smoothly, on the length rule.

**Theorem 1 (Blade basis, degenerate forms included).** A Clifford algebra is built from a space of directions together with a rule for multiplying lengths. This result says that the standard basis of the algebra, made from products of basis directions, still works when the rule is degenerate, so that some directions have zero length against everything, and even when the chosen directions are not perpendicular. The multiplication table depends polynomially, and so smoothly, on the rule.

*Rests on:* std-algebra.blade-basis

We turn to a further ingredient.

**Theorem 2 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers (matrices) whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which of these appears depends only on p minus q, in a pattern that repeats every eight steps. Usually the algebra is a single indivisible block; it splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Rests on:* primer.classification-real-clifford-algebras

In odd dimensions the split has a simple reason behind it. If the pseudoscalar squares to plus one, the algebra falls apart into two identical copies of its even part; if it squares to minus one, it behaves like the imaginary unit and the algebra is its even part with complex coefficients allowed. The even part is always a Clifford algebra of one dimension fewer.

**Theorem 3 (Doubling or complexification).** In an odd number of dimensions, the product of all the basis directions commutes with everything. If it squares to plus one, the algebra falls apart into two identical copies of its even part, the part built from products of an even number of directions. If it squares to minus one, it behaves like the imaginary unit and the algebra is that even part with complex coefficients allowed. The even part itself is always a Clifford algebra of one dimension fewer.

*Rests on:* odd-extensions.volume-element-odd-dimension, std-algebra.z2-grading, std-algebra.orthogonal-anticommute

Elements equal to their own square, called idempotents, act like projections, and they mark where division fails. In a nondegenerate real Clifford algebra, two idempotents are related by an internal change of viewpoint exactly when they project onto subspaces of the same size, in each block when the algebra splits. The ones that no such change can move are exactly the ones that commute with everything.

**Theorem 4 (Classification of idempotent orbits).** Idempotents are elements equal to their own square, like projections onto a subspace. This result sorts them in any nondegenerate real Clifford algebra: two are related by an internal change of viewpoint exactly when they project onto subspaces of the same size (in each of the two blocks, when the algebra splits into two). The ones that no such change can move at all are exactly the ones that commute with everything, and this is how the series separates two of its types of obstruction.

*Rests on:* transport.classification-real-clifford-algebras, transport.units-span

The classification describes algebras as matrices, so it helps to know what taking matrices does. Replacing an algebra by square matrices with entries in it changes its size but keeps its centre and its simplicity; matrices of matrices are just larger matrices, and the operation distributes over a sum of algebras.

**Theorem 5 (Matrix amplification: structural properties).** Replacing an algebra by square matrices whose entries come from that algebra changes its size but not its essential character. The centre stays the same, simplicity is kept, matrices of matrices are just larger matrices, and a direct sum of algebras splits into a direct sum of matrix algebras.

*Rests on:* std-algebra.morita-amplification

Since matrix enlargement keeps so much fixed, a bare algebra can hide where it came from. The position in the cycle of eight, the residue, is kept by every isomorphism that carries directions to directions, but not by bare algebra isomorphisms, under which some different residues coincide at equal dimension. For example, the algebra of our world and that of one of the series' candidate dark towers are the same bare algebra, and what tells them apart is which elements count as directions, which the metric fixes.

**Theorem 6 (The residue is a soldered invariant, not an algebraic one).** Each tower of possible matter is labelled by a number, its residue, which comes from how many directions are time-like and how many space-like. This result shows that the label only has meaning once the algebra is tied to the geometry of spacetime. As bare algebras, some different towers are exactly the same at the same dimension, for example our world's algebra and that of one dark tower. What tells them apart is which elements count as directions, and that is fixed by the metric.

*Rests on:* dark-matter.type-residue-what-each-tower-can, std-algebra.sylvester-inertia, primer.classification-real-clifford-algebras

## Clifford algebras and quadratic forms

This section gathers the results on Clifford algebras and quadratic forms.

We turn to a further ingredient.

**Theorem 7 (The commutation rule).** In a Clifford algebra two perpendicular directions anticommute: swapping their order flips the sign. This rule extends that to anything built from directions perpendicular to a given one. Moving the given direction past such an element flips the sign of its odd part and leaves its even part alone.

That sign rule is what makes reflections work. Sandwiching by a single direction reflects in the mirror perpendicular to it, with a sign twist for products of an odd number of directions, and each length-preserving symmetry arises from exactly two such products, differing by sign.

**Theorem 8 (The twisted adjoint action).** Every symmetry of a geometry that preserves lengths can be built from mirror reflections. In a Clifford algebra each reflection is carried out by sandwiching with a single direction, and a product of directions carries out the combined symmetry. This result sets up the sandwich carefully, with a sign twist for products of an odd number of directions, and shows that each length-preserving symmetry comes from exactly two such products, differing by sign.

One product of directions is special: the product of all the basis directions, called the pseudoscalar. Its square is always plus one or minus one: plus one exactly when the number of positive directions minus the number of negative ones leaves remainder zero or one on division by four, and minus one otherwise.

**Theorem 9 (The sign of $\omega^2$).** Multiplying all the basis directions of a Clifford algebra together gives a special element called the pseudoscalar. Its square is always plus one or minus one, and this result says which. The answer depends only on the number of positive directions minus the number of negative ones: plus one when that difference leaves remainder 0 or 1 on division by four, and minus one otherwise.

The pseudoscalar also decides which elements commute with everything, the centre of the algebra. With an even number of dimensions only the ordinary numbers do; with an odd number the pseudoscalar does too, so the centre becomes two-dimensional.

**Theorem 10 (The centre).** The centre of an algebra is the set of its elements that commute with everything in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

## Results cited, not shown

**Fact (imported) 11 (Type by residue, and what each tower can carry intrinsically).** Each tower's basic algebra decides what kind of numbers its matter states naturally use: real numbers, complex numbers or quaternions. That choice depends only on the tower's label, and it fixes which continuous symmetries a tower carries before any further structure is added. For the representatives the paper uses, and in its labelling convention (the opposite convention swaps the two members of each mirror pair), the mirror tower comes out with real spinors and no built-in continuous charge, two of the odd towers with exactly one built-in charge each, and our own world with quaternionic spinors.

*Provenance:* Transport Lab claim dark-matter.type-residue-what-each-tower-can, version 5 (T14 Thm 3.4).

**Fact (imported) 12 (The volume element in odd dimension).** Multiply all the basis directions of an odd-dimensional Clifford algebra together and the result commutes with everything in the algebra. Its square is either plus one or minus one, and this lemma gives a simple formula for which. In five dimensions it is plus one exactly when the number of negative directions is even.

*Provenance:* Transport Lab claim odd-extensions.volume-element-odd-dimension, version 3 (T14a Lem 2.2).

**Fact (imported) 13 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which one appears depends only on p minus q, in a pattern that repeats every eight steps. The algebra splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Provenance:* Transport Lab claim primer.classification-real-clifford-algebras, version 3 (T00 Thm 9.3).

**Fact (imported) 14 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Provenance:* Transport Lab claim std-algebra.blade-basis, version 1.

**Fact (imported) 15 (An algebra and its matrix amplification).** Taking square arrays of elements of an algebra gives a bigger algebra with the same essential structure: the same central elements, the same ways of being cut down, and the same ways of acting on things.

*Provenance:* Transport Lab claim std-algebra.morita-amplification, version 1.

**Fact (imported) 16 (Orthogonal vectors anticommute).** Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 17 (Orthogonal bases and the law of inertia).** However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 18 (The even subalgebra and the Z2 grading).** Parity multiplies like signs: even with even or odd with odd gives even, mixed gives odd. A product of a $j$-grade and a $k$-grade element can only have grades between their difference and their sum, in steps of two.

*Provenance:* Transport Lab claim std-algebra.z2-grading, version 1.

**Fact (imported) 19 (Units span).** In any finite-dimensional algebra over the real numbers, even an element that cannot be divided by is the sum of two elements that can. The trick is to subtract a suitable multiple of 1, which leaves something invertible for all but finitely many choices.

*Provenance:* Transport Lab claim transport.units-span, version 2 (T01 Lem 6.3).

The structure of a real Clifford algebra is fixed by its numbers of positive and negative directions, in a pattern that repeats every eight steps. Yet the position in that pattern lives in the geometry, since bare algebra isomorphisms can forget it. This trail rests on no postulate: each step is proved here or cited from results proved elsewhere and from the classical literature.
