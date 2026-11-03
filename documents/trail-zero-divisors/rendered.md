# Zero divisors and obstructions

**Abstract.** Division is the operation this whole series turns on, and this trail follows where it breaks down.

A null vector, a nonzero vector $v$ whose square $v^{2}$ is zero, has no inverse, even inside a larger algebra. With a nondegenerate form, every failure of division is one of three kinds: a null vector, an algebra split into two halves, or a projection.

The projection kind repairs itself. The null kind cannot be repaired element by element while respecting the symmetries, however the algebra is enlarged. And every repair creates failures of its own.

The walk starts with the simplest element that cannot be divided by, maps where each kind of failure occurs, shows the list of kinds is complete, and ends with what can and cannot be repaired.

## Zero divisors and obstructions

These results ask when and why division fails in a Clifford algebra.

A null vector is a nonzero $v$ with $v^{2} = 0$.

If $v$ had an inverse $u$, then $v = v(vu) = v^{2} u = 0$, so no inverse exists on either side, in $\Cl(p,q)$ or in any larger associative algebra containing it. This is the first and simplest failure of division, and the rest of the walk grows from it.

**Theorem 1 (A null vector has no inverse).** A null vector is a nonzero direction whose square is zero. Such an element can never be divided by: if it had an inverse on either side, multiplying through would force the vector itself to be zero. The argument uses only the fact that its square is zero, so it still applies in any larger algebra of the same kind that contains the original one.

*Rests on:* std-algebra.vector-squares

Next comes the question of where such vectors exist.

They exist exactly when the signature is mixed, \[ pq \neq 0 \] that is, when there are both positive and negative directions, as in spacetime. They then form a cone of dimension $n - 1$, like a light cone, and every one of them is a two-sided zero divisor.

**Theorem 2 (Existence locus of type N).** In a space with both positive and negative directions, like the space-time of relativity, there are nonzero directions of zero length, called null directions. This result says they exist exactly when both kinds of direction are present, and that they then form a cone, much like a light cone. Each such direction multiplied by itself gives zero, so it can never be divided by, even in a larger algebra that contains the original one.

*Rests on:* transport.noinverse, std-algebra.orthogonal-anticommute

With one failure in view, it is natural to ask which algebras escape failure altogether.

Only three do: \[ \Cl(0,0) = \R, \quad \Cl(0,1) = \C, \quad \Cl(0,2) = \HH \] the reals, the complex numbers and the quaternions. Every other real Clifford algebra has nonzero elements whose product is zero.

**Theorem 3 (The exceptional division algebras).** In most Clifford algebras some nonzero elements multiply to zero, so division sometimes fails. This result lists the only exceptions: the real numbers, the complex numbers and the quaternions. Allowing pairs of these as well gives exactly the algebras in which no nonzero element has a power equal to zero.

*Rests on:* transport.classification-real-clifford-algebras, std-algebra.blade-basis

A second way for division to fail is for the whole algebra to come apart into two independent halves.

This happens exactly when $p - q \equiv 1 \pmod 4$, and the halves are picked out by the two central idempotents \[ \varepsilon_\pm = \tfrac12\,(1 \pm \omega) \] built from the pseudoscalar $\omega$, the product of all the basis vectors. They satisfy $\varepsilon_+ \varepsilon_- = 0$ and $\varepsilon_+ + \varepsilon_- = 1$, and the grade involution swaps them, but no inner automorphism can.

**Theorem 4 (Existence and classification of type C).** Some Clifford algebras secretly come in two independent halves, and the elements that pick out each half are called central idempotents. This result pins down exactly when that happens: precisely when the number of positive directions minus the number of negative ones leaves remainder 1 on division by four. In that case there are exactly two such elements, built from the product of all the basis directions. Reversing every direction swaps the two halves, but no conjugation by an element of the algebra itself can do so, since these elements commute with everything.

*Rests on:* transport.centre, transport.classification-real-clifford-algebras, transport.sign, std-algebra.involution-properties

The third kind, type P, is an idempotent that does not commute with everything, like a projection onto part of a space.

Such elements are almost everywhere: for an orthogonal pair $a, b$ with $a^{2} b^{2} = -1$, the bivector $u = ab$ squares to one and gives \[ \tfrac12(1 + u) \] a non-central idempotent. Only five small algebras, built from the reals, the complex numbers and the quaternions, lack them.

**Theorem 5 (Existence locus of type P).** An element that equals its own square but does not commute with everything is a type-P obstruction. Such elements exist in every real Clifford algebra except five small ones built from the real numbers, the complex numbers and the quaternions. A simple recipe produces one from a space-like and a time-like direction at right angles.

*Rests on:* transport.classification-real-clifford-algebras, transport.exceptional-division-algebras, std-algebra.orthogonal-anticommute

With three kinds named, the question is whether there are any others.

The key step is that each element $a$ of a nondegenerate Clifford algebra has a partial inverse $x$ with $axa = a$. For a zero divisor this produces idempotents $e = xa$ and $f = ax$ with \[ a(1 - e) = 0, \qquad (1 - f)a = 0 \] which pin down where the failure sits.

**Theorem 6 (Regularity localises zero divisors at idempotents).** In the algebras of the series every element has a weak kind of inverse that undoes it partway. Applying that weak inverse to an element that cannot be divided by produces elements equal to their own squares, which pin down exactly where the failure sits. This is the step that turns every failure of division into a statement about such elements.

*Rests on:* transport.classification-real-clifford-algebras

That step turns every failure of division into a statement about idempotents.

From there, whenever the form is nondegenerate, every zero divisor traces back to one of the three kinds already named, so the list is complete. The central kind can occur only when $p - q \equiv 1 \pmod 4$; otherwise every annihilating idempotent is non-central.

**Theorem 7 (Exhaustiveness: every zero divisor is annihilated by an idempotent).** Whenever division fails in a Clifford algebra with a nondegenerate notion of length, the failure can be traced to an element that equals its own square. This shows that the three kinds of failure already named cover every case. Which kinds occur depends only on the numbers of space and time directions.

*Rests on:* transport.classification-real-clifford-algebras, transport.existence-classification-type-c, transport.existence-locus-type-n, transport.regularity-localises-zero-divisors-idempotents

Once the kinds are known, one can ask which of them can be repaired.

The projection kind repairs itself: each idempotent is its own partial inverse, \[ e\,e\,e = e \] so the assignment $\sigma(e) = e$ satisfies the required identities and respects every symmetry. Nothing needs to be added to the algebra.

**Theorem 8 (Type P is self-repairing).** Some zero divisors are projection-like elements, ones that equal their own square. For these, the repair being sought is already available: each such element can serve as its own partner and satisfies the required identities. Because the rule is simply to take the element itself, it automatically respects every symmetry, so nothing needs to be added to the algebra.

The null kind is the opposite case.

A null vector $v$ has many partial inverses $\sigma(v)$ with \[ v\,\sigma(v)\,v = v \] but in mixed signature with $n \geq 3$ there is no way to choose one for each null $v$ that is equivariant, even under $\Spin^0(p,q)$. Enlarging the algebra by any number of new directions does not help.

Any repair of this kind must therefore work differently, and the completion trail takes that up.

**Theorem 9 (No-go at the level of elements).** A light-like direction has no inverse, but it has many partial inverses. This theorem shows that there is no way to choose one for every light-like direction that respects the symmetries of the geometry, in any space with both space and time directions and at least three dimensions. Enlarging the algebra by any number of new directions does not help.

*Rests on:* transport.splitting-along-hyperbolic-plane, primer.commutation-rule, std-algebra.witt-decomposition

A last question is whether repairing ever finishes.

It does not: a completion by the first rule has mixed signature and so new null vectors, and one by the second is a matrix algebra $\Mat_2(\Cl^0(p,q))$ with new projections. So the process never ends in an algebra free of zero divisors.

**Theorem 10 (No transport terminates).** Each repair in the transport programme enlarges the algebra to fix a failure of division. This result shows that the enlarged algebra always has failures of its own: one repair adds new light-like directions, the other produces projections and elements that square to zero. So the process never ends in an algebra where every nonzero element can be divided by.

*Rests on:* transport.existence-locus-type-n, transport.matrix-units-peirce-isomorphism, transport.rule-2-ideal-fusion-sharp-form

## Results cited, not shown

**Fact (imported) 11 (The commutation rule).** In a Clifford algebra two perpendicular directions anticommute: swapping their order flips the sign. This rule extends that to anything built from directions perpendicular to a given one. Moving the given direction past such an element flips the sign of its odd part and leaves its even part alone.

*Provenance:* Transport Lab claim primer.commutation-rule, version 2 (T00 Lem 9.1).

**Fact (imported) 12 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Provenance:* Transport Lab claim std-algebra.blade-basis, version 1.

**Fact (imported) 13 (The three involutions on each grade).** The three basic ways of "flipping" an element each multiply every grade by plus or minus one, according to a simple pattern in the grade. Reversion, for example, leaves numbers and arrows alone and changes the sign of planes and volumes.

*Provenance:* Transport Lab claim std-algebra.involution-properties, version 1.

**Fact (imported) 14 (Orthogonal vectors anticommute).** Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 15 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 16 (Hyperbolic pairs and the Witt decomposition).** Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 17 (The centre).** The centre of an algebra is the set of its elements that commute with everything else in it. For the Clifford algebra of a space with an even number of dimensions, only the ordinary numbers do this. With an odd number of dimensions there is one more such element, the product of all the basis directions, so the centre becomes two-dimensional.

*Provenance:* Transport Lab claim transport.centre, version 4 (T01 Lem 2.6).

**Fact (imported) 18 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers (matrices) whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which of these appears depends only on p minus q, in a pattern that repeats every eight steps. Usually the algebra is a single indivisible block; it splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Provenance:* M. F. Atiyah, R. Bott and A. Shapiro, Clifford modules (1964); I. R. Porteous, Clifford Algebras and the Classical Groups (1995); P. Lounesto, Clifford Algebras and Spinors (2001).

**Fact (imported) 19 (Matrix units, and the Peirce isomorphism).** Inside the enlarged algebra, the two projectors that used to split the original algebra, together with the new direction, behave exactly like the four basic entries of a two-by-two matrix. It follows that the enlarged algebra is the same thing as two-by-two matrices whose entries come from one corner of it.

*Provenance:* Transport Lab claim transport.matrix-units-peirce-isomorphism, version 3 (T01 Lem 5.4).

**Fact (imported) 20 (Rule 2: ideal fusion, sharp form).** Some Clifford algebras split into two independent halves. Adding one new direction, of either sign, fuses the halves into a single algebra of two-by-two matrices whose entries come from the algebra's even part. The fused algebra has no split of its own, and the two choices of sign give the same algebra.

*Provenance:* Transport Lab claim transport.rule-2-ideal-fusion-sharp-form, version 4 (T01 Thm 5.5).

**Fact (imported) 21 (The sign of $\omega^2$).** Multiplying all the basis directions of a Clifford algebra together gives a special element called the pseudoscalar. Its square is always plus one or minus one, and this result says which. The answer depends only on the number of positive directions minus the number of negative ones: the square is plus one when that difference leaves remainder 0 or 1 on division by four, and minus one otherwise.

*Provenance:* Transport Lab claim transport.sign, version 3 (T01 Lem 2.7).

**Fact (imported) 22 (Splitting along a hyperbolic plane).** When a space contains a light-like direction paired with a partner, the algebra of the whole space splits into four slots built from that pair, each filled by an element of the algebra of the remaining directions. The split is unique, which makes it a reliable bookkeeping device. Multiplying by the light-like direction never sends a nonzero element of the remaining algebra to zero.

*Provenance:* Transport Lab claim transport.splitting-along-hyperbolic-plane, version 3 (T01 Lem 2.4).

Division fails in exactly three ways in a Clifford algebra with a nondegenerate form, and the list is complete.

No repair ends in an algebra free of failures, so obstructions are something to move and manage rather than abolish. This trail rests on no postulate: each step is proved here or cited from results proved elsewhere, including the classical classification of real Clifford algebras.
