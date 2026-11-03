# The completion

**Abstract.** When division fails, the series does not give up: it moves to a larger setting in which the failing calculation works. This trail follows that move, the completion.

For a null vector the larger space must gain one new positive and one new negative direction, so the minimal completion is $\Cl(p,q) \to \Cl(p{+}1, q{+}1)$. There a single operation gives a reciprocal everywhere, agreeing with the usual one wherever that exists.

For an algebra split into two halves, adding one direction of either sign fuses the halves. Together these give the transport principle: three kinds of failure, each with a forced smallest repair.

The walk first repairs null vectors on the space of points, then degenerate geometries, then algebras split in two, and ends with the principle that gathers the repairs together.

## The completion

Each result here says how to enlarge a space or an algebra so that a failure of division is repaired, and how small that enlargement can be.

A null vector cannot be divided by, so the series instead represents each point of the geometry as a null vector in a larger space. The first question is how much larger that space must be.

The added part needs at least one direction of positive square and one of negative square, and one such pair, a hyperbolic plane, is enough: \[ \Cl(p,q) \;\longrightarrow\; \Cl(p{+}1, q{+}1) \] with signature increment $(+1,+1)$ in every signature.

**Theorem 1 (Minimality).** To make the reciprocal work everywhere, the series represents each point as a light-like direction in a larger space. This result asks how much larger that space has to be. The added part must contain at least one direction of positive square and one of negative square, so adding only space-like or only time-like directions never works, while one such pair is enough and is essentially unique.

*Rests on:* std-algebra.witt-decomposition, std-algebra.sylvester-inertia

With the larger space in hand, the reciprocal can be extended.

On the space of points a single sandwich by the new direction $e_+$, \[ \iota[N] = [\,e_+ N e_+\,] \] gives a reciprocal everywhere: on vectors with $Q(x) \neq 0$ it is the usual $x/Q(x)$, and it sends null vectors to points at infinity. It is also the only continuous rule that matches the usual reciprocal.

**Theorem 2 (Totality).** In a Clifford algebra with vectors of zero length, the reciprocal of a vector is undefined on exactly those vectors. After moving to the enlarged space of points, a single reflection-like operation gives a reciprocal everywhere: it agrees with the usual one on ordinary vectors and sends zero-length vectors to points at infinity. Those values are the limits one would expect, and no other continuous rule matches the usual reciprocal.

*Rests on:* transport.density, std-algebra.reflection

A calculation done in the larger space is only useful if its answer can be brought back.

The read-out map \[ \dsc\,[\, s\,\nO + x + t\,\nInf \,] = x/s \] does this for every point not at infinity, and on invertible vectors it returns the familiar reciprocal $x/Q(x)$. For null vectors the answer lies at infinity, and the read-out declines rather than inventing a value.

**Theorem 3 (Descent: the read-out map).** After computing in the enlarged space one needs a way back to the original one. The read-out map does this for every point not at infinity, and for ordinary invertible vectors it gives back the familiar reciprocal. For zero-length vectors the answer lies at infinity, and the read-out declines, because no point of the original space represents it.

*Rests on:* transport.totality

The same idea repairs geometries whose form is degenerate, with directions that pair to zero with everything.

Each degenerate direction needs exactly one new partner, so a radical of dimension $r$ gives \[ \Cl(p,q,r) \hookrightarrow \Cl(p{+}r, q{+}r) \] unique up to an isometry fixing the original space. Minimality here is among enlargements of the underlying space, not among all algebras.

**Theorem 4 (Minimal nondegenerate completion).** A geometric algebra built on a degenerate metric has directions that pair to zero with everything, and division fails along them. This result says how to enlarge the space so that the metric becomes nondegenerate: each degenerate direction needs exactly one new partner direction, and the enlarged metric gains one positive and one negative direction for each degenerate one. The smallest such enlargement is unique up to a symmetry that leaves the original space untouched. Minimality here is among enlargements of the underlying space, not among all algebras.

*Rests on:* conformal.blade-basis-persists-under-degeneracy, conformal.witt-extension-theorem, std-algebra.functoriality

The best-known example comes from engineering and computer graphics.

Projective geometric algebra, with one degenerate direction for the plane at infinity, completes uniquely to conformal geometric algebra: \[ \Cl(3,0,1) \;\longrightarrow\; \Cl(4,1) \] and in general $\Cl(n,0,1)$ completes to $\Cl(n{+}1,1)$. Two tools usually treated as separate design choices are thus one algebra and its repair.

**Theorem 5 (The principal case).** Engineers and graphics programmers use two geometric algebras: projective geometric algebra, which has one degenerate direction standing for the plane at infinity, and conformal geometric algebra, which has two extra directions. They are usually treated as separate design choices. This result shows that the conformal algebra is the unique smallest nondegenerate enlargement of the projective one, in any number of dimensions, in the sense of enlarging the underlying space.

*Rests on:* conformal.minimal-nondegenerate-completion

Back with the null repair, it helps to know what the enlarged algebra actually is.

Adding one hyperbolic plane, the step called Rule 1, gives two-by-two matrices over the original algebra, \[ \Cl(p{+}1, q{+}1) \;\cong\; \Mat_2\bigl(\Cl(p,q)\bigr) \] with the new null pair $f, f^*$ as the off-diagonal entries. So the step leaves the clock residue $d = p - q \pmod 8$ unchanged.

**Theorem 6 (Rule 1 is Morita-trivial).** The basic transport step adds one new pair of null directions to an algebra. The enlarged algebra turns out to be the algebra of two-by-two matrices with entries in the original one, with the new null pair playing the role of the off-diagonal entries. So the step leaves the essential type of the algebra unchanged, although whether certain other kinds of obstruction are present can change.

*Rests on:* transport.matrix-units-peirce-isomorphism, std-algebra.involution-properties, std-algebra.morita-amplification

The second kind of failure, an algebra split into two halves, needs a different repair.

When $p - q \equiv 1 \pmod 4$, adding one new direction of either sign fuses the halves: \[ \Cl(p{+}1,q) \;\cong\; \Cl(p,q{+}1) \;\cong\; \Mat_2\bigl(\Cl^0(p,q)\bigr) \] matrices over the even part. The fused algebra is simple, with centre $\R$, so it has no split of its own.

**Theorem 7 (Rule 2: ideal fusion, sharp form).** Some Clifford algebras split into two independent halves. Adding one new direction, of either sign, fuses the halves into a single algebra of two-by-two matrices whose entries come from the algebra's even part. The fused algebra has no split of its own, and the two choices of sign give the same algebra.

*Rests on:* transport.ascent-renders-grade-involution-inner, transport.centre, transport.classification-real-clifford-algebras, transport.corner-even-subalgebra, transport.matrix-units-peirce-isomorphism, std-algebra.morita-amplification

Is a single direction really the least one can add?

Yes: adding nothing leaves the algebra split, and adding a null direction only thickens it, by an ideal $J$ with $J^2 = 0$. One direction of nonzero square is the smallest repair that joins the halves, and both signs give the same algebra.

**Theorem 8 (One generator is minimal; the minimal completions classified).** When a Clifford algebra splits into two halves, one can try to repair it by adding directions. Adding nothing leaves it split; adding one direction of zero length only thickens the algebra without joining the halves; adding one direction of nonzero length joins them; adding more is larger than needed. The two possible single directions, of positive or negative square, give the same algebra, so the repair is unique and cannot tell which sign was used.

*Rests on:* transport.decomposition-commutation, transport.existence-classification-type-c, transport.rule-2-ideal-fusion-sharp-form, std-algebra.blade-basis, std-algebra.sylvester-inertia

Repairs can be repeated, so it matters how often each is needed.

Every algebra sits on a clock, its residue $d \bmod 8$: Rule 1 never moves the hand, and Rule 2 is used only at residues $1$ and $5$ and lands in $\{0, 2\}$ or $\{4, 6\}$. So fusion happens at most once, and the algebra of spacetime starts at a residue that never needs it.

**Theorem 9 (Fusion occurs at most once).** Each Clifford algebra sits at one of eight positions on a clock. One repair rule never moves the hand; the other moves it by one step, is only used at the two positions where the algebra is split, and always lands where no split occurs. So the second rule can be used at most once, after which nothing structural changes. The algebra of spacetime starts at a position that never needs the second rule.

*Rests on:* transport.classification-real-clifford-algebras, transport.existence-classification-type-c, transport.rule-1-morita-trivial

Everything now fits into one statement.

Division in a nondegenerate real Clifford algebra fails in exactly three ways, and each carries a forced minimal repair: complete the space, complete the algebra, or do nothing. For a null vector the element itself cannot be repaired; the repair acts on the space of points, with increment $(+1,+1)$.

**Theorem 10 (Transport principle).** Division can go wrong in a Clifford algebra in exactly three ways. For a light-like direction the element itself cannot be fixed, but adding one extra pair of dimensions repairs the space of points; for an algebra split into two halves, adding one dimension fuses them; for an ordinary projection, nothing needs fixing. Each repair is the smallest possible, and the list is complete.

*Rests on:* transport.cohomological-form-no-go, transport.embedding-independent-minimality-fusion, transport.exhaustiveness-every-zero-divisor-annihilated-idempotent, transport.minimality, transport.no-fourth-rule, transport.no-go-level-elements, transport.one-generator-minimal-minimal-completions-classified, transport.representation-independent-minimality-completion, transport.rule-2-ideal-fusion-sharp-form, transport.totality, transport.type-p-self-repairing

## Results cited, not shown

**Fact (imported) 11 (The blade basis persists under degeneracy).** A Clifford algebra is built from a space of directions together with a rule for multiplying them. This fact says that the products of distinct basis directions always form a basis for the whole algebra, so an algebra built on m directions has size two to the power m. That stays true even when the multiplication rule is degenerate, with some directions of zero length against every direction.

*Provenance:* Transport Lab claim conformal.blade-basis-persists-under-degeneracy, version 4 (T02 Fact 2.1).

**Fact (imported) 12 (The Witt extension theorem).** Suppose two spaces carry equivalent nondegenerate notions of length and angle. Then any length-preserving match between a part of one and a part of the other can be extended to a length-preserving match of the whole spaces. This works even when the parts themselves are degenerate. It is a standard theorem about quadratic forms.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, Thm.~4.7.

**Fact (imported) 13 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Provenance:* Transport Lab claim std-algebra.blade-basis, version 1.

**Fact (imported) 14 (Isometries extend to algebra homomorphisms).** If a map of arrows preserves square lengths, it automatically extends to a map of the whole algebra that respects multiplication. Symmetries of space therefore act on everything built from arrows.

*Provenance:* Transport Lab claim std-algebra.functoriality, version 1.

**Fact (imported) 15 (The three involutions on each grade).** The three basic ways of "flipping" an element each multiply every grade by plus or minus one, according to a simple pattern in the grade. Reversion, for example, leaves numbers and arrows alone and changes the sign of planes and volumes.

*Provenance:* Transport Lab claim std-algebra.involution-properties, version 1.

**Fact (imported) 16 (An algebra and its matrix amplification).** Taking square arrays of elements of an algebra gives a bigger algebra with the same essential structure: the same central elements, the same ways of being cut down, and the same ways of acting on things.

*Provenance:* Transport Lab claim std-algebra.morita-amplification, version 1.

**Fact (imported) 17 (Reflection in a non-null vector).** Multiplying an arrow on both sides by a fixed arrow, with a sign, gives its mirror image in the plane perpendicular to the fixed arrow. This works for any fixed arrow that does not have zero length. Mirrors are the building blocks of all rotations.

*Provenance:* Transport Lab claim std-algebra.reflection, version 1.

**Fact (imported) 18 (Orthogonal bases and the law of inertia).** However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 19 (Hyperbolic pairs and the Witt decomposition).** Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 20 (The ascent renders the grade involution inner).** Some Clifford algebras split into two independent halves, and the symmetry that swaps the halves cannot be produced from inside the algebra. Adding one new direction changes that: conjugating by the new direction performs the swap. Once the swap is available inside the algebra, the two halves can no longer be kept apart, and they merge into one.

*Provenance:* Transport Lab claim transport.ascent-renders-grade-involution-inner, version 3 (T01 Prop 5.2).

**Fact (imported) 21 (The centre).** The centre of an algebra is the set of its elements that commute with everything else in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

*Provenance:* Transport Lab claim transport.centre, version 4 (T01 Lem 2.6).

**Fact (imported) 22 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers (matrices) whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which of these appears depends only on p minus q, in a pattern that repeats every eight steps. Usually the algebra is a single indivisible block; it splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Provenance:* M. F. Atiyah, R. Bott and A. Shapiro, Clifford modules (1964); I. R. Porteous, Clifford Algebras and the Classical Groups (1995); P. Lounesto, Clifford Algebras and Spinors (2001).

**Fact (imported) 23 (Cohomological form of the no-go).** Earlier results show that the symmetries fixing a light-like direction slide every candidate partial inverse along by a definite amount. This theorem packages that sliding as a single algebraic invariant, which vanishes only in the smallest case of one space and one time direction. Because the invariant is built inside the original algebra, enlarging the algebra or the symmetry group cannot remove it.

*Provenance:* Transport Lab claim transport.cohomological-form-no-go, version 4 (T01 Thm 4.8).

**Fact (imported) 24 (The corner is the even subalgebra).** When an algebra splits into two blocks, each block can be compared with the algebra's even part, built from products of an even number of directions. This result shows each block is an exact copy of that even part. It also shows that enlarging the algebra by one extra direction and then cutting back down to the block returns the same block.

*Provenance:* Transport Lab claim transport.corner-even-subalgebra, version 4 (T01 Lem 5.3).

**Fact (imported) 25 (Decomposition and commutation).** Adding one new direction to a Clifford algebra doubles its size: every element becomes an old element plus an old element times the new direction. Moving the new direction past an old element flips the sign of that element's odd parts. If the new direction has nonzero square, one can divide by it.

*Provenance:* Transport Lab claim transport.decomposition-commutation, version 3 (T01 Lem 5.1).

**Fact (imported) 26 (Density).** The repair represents each point of the original space as a light-like ray in a bigger space, and the bigger space also contains extra points at infinity. This result says that the ordinary, invertible points come arbitrarily close to every point of the bigger space, the points at infinity included. Nothing in the enlarged space is cut off from the ordinary points.

*Provenance:* Transport Lab claim transport.density, version 3 (T01 Lem 4.9).

**Fact (imported) 27 (Embedding-independent minimality of the fusion).** When a Clifford algebra splits into two halves, the series repairs it by adding one direction, which fuses the halves into a single indivisible algebra twice the size. This result shows that no cleverer choice does better: any indivisible algebra containing the split one is at least twice its size. The fused algebra is, up to relabelling, the only one that achieves this.

*Provenance:* Transport Lab claim transport.embedding-independent-minimality-fusion, version 4 (T01 Thm 5.11).

**Fact (imported) 28 (Exhaustiveness: every zero divisor is annihilated by an idempotent).** Whenever division fails in a Clifford algebra with a nondegenerate notion of length, the failure can be traced to an element that equals its own square. This shows that the three kinds of failure already named cover every case. Which kinds occur depends only on the numbers of space and time directions.

*Provenance:* Transport Lab claim transport.exhaustiveness-every-zero-divisor-annihilated-idempotent, version 3 (T01 Thm 3.9).

**Fact (imported) 29 (Existence and classification of type C).** Some Clifford algebras secretly come in two independent halves, and the elements that pick out each half are called central idempotents. This result pins down exactly when that happens: precisely when the number of positive directions minus the number of negative ones leaves remainder 1 on division by four. In that case there are exactly two such elements, built from the product of all the basis directions. Reversing every direction swaps the two halves, but no conjugation by an element of the algebra itself can do so, since these elements commute with everything.

*Provenance:* Transport Lab claim transport.existence-classification-type-c, version 4 (T01 Thm 3.6).

**Fact (imported) 30 (Matrix units, and the Peirce isomorphism).** Inside the enlarged algebra, the two projectors that used to split the original algebra, together with the new direction, behave exactly like the four basic entries of a two-by-two matrix. It follows that the enlarged algebra is the same thing as two-by-two matrices whose entries come from one corner of it.

*Provenance:* Transport Lab claim transport.matrix-units-peirce-isomorphism, version 3 (T01 Lem 5.4).

**Fact (imported) 31 (No fourth rule).** Division can fail in a nondegenerate real Clifford algebra in exactly three ways, and each has its own prescribed fix: add a pair of dimensions, add one dimension, or do nothing. Since every failure of division is one of the three, the list of fixes is complete.

*Provenance:* Transport Lab claim transport.no-fourth-rule, version 4 (T01 Cor 6.7).

**Fact (imported) 32 (No-go at the level of elements).** A light-like direction has no inverse, but it has many partial inverses. This theorem shows that there is no way to choose one for every light-like direction that respects the symmetries of the geometry, in any space with both space and time directions and at least three dimensions. Enlarging the algebra by any number of new directions does not help.

*Provenance:* Transport Lab claim transport.no-go-level-elements, version 4 (T01 Thm 4.2).

**Fact (imported) 33 (Representation-independent minimality of the completion).** One might hope to repair a geometry inside some smaller algebra by placing the original algebra in it in an unusual way. This result rules that out. What the repair needs is room for the points of the geometry together with their separations, and that requires at least one extra positive and one extra negative direction, whatever the embedding.

*Provenance:* Transport Lab claim transport.representation-independent-minimality-completion, version 4 (T01 Thm 4.19).

**Fact (imported) 34 (Type P is self-repairing).** Some zero divisors are projection-like elements, ones that equal their own square. For these, the repair being sought is already available: each such element can serve as its own partner and satisfies the required identities. Because the rule is simply to take the element itself, it automatically respects every symmetry, so nothing needs to be added to the algebra.

*Provenance:* Transport Lab claim transport.type-p-self-repairing, version 2 (T01 Prop 6.1).

The completion turns each of the three failures of division into a forced smallest repair.

A calculation done in the enlarged setting can be read back everywhere except at the points at infinity. This trail rests on no postulate: each step is proved here or cited from proved or classical results, such as the classification of real Clifford algebras and Witt's extension theorem.
