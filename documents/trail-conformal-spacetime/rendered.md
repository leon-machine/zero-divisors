# Spacetime in the conformal completion

**Abstract.** In the conformal completion, two extra directions are added to the algebra of spacetime, and every point becomes a null vector, one whose square is zero. This trail shows that the same algebra already contains the conformal spinor space, which Penrose called twistor space.

The null directions of the completion match the lines of the projective spinor space, the classical Klein correspondence obtained here from the algebra. Penrose's incidence relation, the rule tying points to spinors, turns out to be the completion's own coordinate chart.

Conformal spinors are vacuum states of fermionic ladder pairs, not the operators that act on them. The walk ends with Einstein's vacuum equations read in three equivalent languages.

The walk starts from points as null vectors, builds the space the completed algebra acts on, and then reads the spinor dictionary off it one step at a time. Results a step rests on but that are not on the trail are listed at the end.

## Spacetime in the conformal completion

These results place spacetime, its light cones and its conformal spinors inside a single algebra.

The completion adds a null pair $\nO$ and $\nInf$, the origin and the point at infinity, to the directions of spacetime. A point $x$ is then represented by the null vector \[ X(x) = \nO + x + \tfrac12 Q(x)\,\nInf \]

The product of two such vectors is $X(x)\cdot X(y) = -\tfrac12 Q(x - y)$, so separations are read off the algebra directly. The rotors $R_u = 1 + vu$ that fix a null vector $v$ add like vectors.

**Theorem 1 (Imported: the conformal model and the null rotations).** Adding two extra directions to the algebra of space lets every point be written as a null vector, one whose square is zero, and the squared distance between two points can then be read off from a simple product of their vectors. In the same setting, each null direction has a family of rotations that leave it fixed, and these rotations combine exactly like ordinary addition of vectors. Both facts are carried over from earlier work in the series.

*Rests on:* transport.group-null-rotations, transport.totality

To compute with the completed algebra we need a concrete space for it to act on.

Pick a maximal set $W$ of mutually null complex directions, with $\dim_\C W = 3$, and let vectors act on the exterior algebra $\Lambda^\bullet W$ by wedging and contracting: \[ c(w) = \sqrt2\; w \wedge (\cdot), \qquad c(w') = \sqrt2\; \iota_{w'} \] This is the only irreducible module of the complexified algebra, the Fock model.

Vectors act oddly, so the module splits into even and odd halves of complex dimension four, the two chiralities $\CS$ and $\CSm$.

**Theorem 2 (The Fock model of the complexified ascended algebra).** The completed algebra of six directions can be represented concretely. Pick three complex directions that are mutually lightlike, and let the algebra act on all combinations of them by adding or removing a direction, much as one creates and destroys particles. This gives an eight-dimensional space on which the algebra acts faithfully and irreducibly, the only such space up to equivalence, and it splits into two four-dimensional halves, the two chiralities.

*Rests on:* std-algebra.existence-uniqueness, std-algebra.complex-clifford-algebra

With the conformal spinor space in hand, the next question is how the symmetries of spacetime act on it.

The bivectors close under commutators and act on $\CS$ by an isomorphism \[ \rho : \mathfrak{so}(2,4)_\C \to \mathfrak{sl}(\CS) \] So the spin group acts as all of $SL(\CS)$, and any nonzero conformal spinor can be moved to any other.

**Theorem 3 (The spin representation is $\mathfrak{sl}(\CS)$).** The conformal symmetries of spacetime, extended to complex numbers, can be realised inside the completed Clifford algebra. Acting on the four-dimensional spinor space of the conformal algebra they give exactly the trace-free linear transformations of that space, no more and no fewer. At the level of groups every volume-preserving linear map of that space is achieved, so any nonzero spinor in it can be moved to any other.

*Rests on:* std-algebra.vector-squares, std-algebra.complex-clifford-algebra

Now the two pictures can be matched.

The complexified vectors are exactly the bivectors of the spinor space, \[ V_\C \cong \Lambda^{2}\CS \] with the quadratic form becoming the wedge square of a bivector. A vector is null exactly when its bivector is simple, that is, when it is a line of the projective spinor space $\PCS$. This is the Klein correspondence, obtained from the completion rather than assumed.

**Theorem 4 (The spinor identification).** This result matches the six complex directions of the completed spacetime algebra with the six independent plane elements that can be formed inside the four-dimensional conformal spinor space. Under the match, the lightlike directions are exactly those plane elements that are single planes rather than sums of planes, and in projective terms these are lines of that spinor space. So the lightlike directions of the completion, taken up to sign, are lines in the projective spinor space: the Klein correspondence, obtained from the completion.

*Rests on:* correspondence.chevalley-pairing, correspondence.fock-model-complexified-ascended-algebra, correspondence.imported-forced-completion-fibre-quadric, std-algebra.vector-squares, std-algebra.inverse-of-vector

Since points are null vectors and null vectors are lines, each point of spacetime should be a line of spinors.

For a linear map $A$ between the two planes $\Spi$ and $\Som$ of the splitting, the bivector of its graph line expands as \[ P(A) = N_0 + \varphi(A) + (\det A)\, N_\infty \] Term by term this is the completion's point $X(m(A))$, with the determinant as its quadratic term, so the incidence relation is the completion's chart.

**Theorem 5 (The incidence relation is the chart).** Penrose described a spacetime point by a line in a three-dimensional complex projective space, through his incidence relation. This theorem shows that, written out term by term, the coordinates of that line are exactly the null vector by which the completed algebra represents the point, so the incidence relation is the completion's coordinate chart. The quadratic term of the chart is a determinant, the lines meeting a fixed line at infinity are the points at infinity, and the symmetries fixing that line are those of flat spacetime.

*Rests on:* correspondence.chiral-planes-summand-spaces, correspondence.imported-stabilisers-flat-model, correspondence.skew-lines-splittings-hyperbolic-planes-one, correspondence.spinor-identification

So far everything is complex, but the spacetime we live in is real.

The completion supplies its own antilinear conjugation, unique up to scale, and from it a Hermitian form on $\CS$ of signature $(2,2)$. Real points are the null lines of that form skew to the infinity line, with incidence relation \[ \omega = I_6\, \hat x\, \pi \] for Hermitian $\hat x$, so the factor in front is the conformal pseudoscalar $I_6$, not a bare imaginary unit.

**Theorem 6 (Reality: the conjugation, the invariant Hermitian form, and the factor $I_6$).** The spinor space of the conformal algebra, as built here, is a complex space, and real spacetime has to be recovered from it by a reality condition. This result builds that condition from the completion itself: a conjugation operation and, from it, a Hermitian form on the spinor space with two positive and two negative directions. Real spacetime points are exactly the lines of spinors on which this form vanishes, and the complex unit in Penrose's incidence relation, here the conformal pseudoscalar, is forced by this reality condition.

*Rests on:* correspondence.chevalley-pairing, correspondence.incidence-relation-chart, correspondence.fock-model-complexified-ascended-algebra, std-algebra.inverse-of-vector, std-algebra.reflection

Having placed conformal spinors in the algebra, we can ask what kind of object they are there.

Each nonzero spinor $u$ has an annihilator \[ W_u = \{ v \in V_\C : c(v)u = 0 \} \] which is a maximal null subspace, so every conformal spinor is pure. The spinor is the Fock vacuum of the three ladder pairs built on $W_u$, and every other state is reached from it by those pair operators.

Conformal spinors are therefore states that operators act on, not the operators themselves.

**Theorem 7 (Conformal spinors are the states of three ladder pairs).** The four-component spinors of the conformal algebra are the objects Penrose built his theory on. This result shows that, inside the completed algebra of the series, each such spinor is the empty state (the vacuum) of a system of three fermionic ladder pairs that the spinor itself singles out. Every other state of the module is reached from it by those ladder operators, so these spinors are the states the operators act on, not the operators themselves.

*Rests on:* correspondence.fock-model-complexified-ascended-algebra, correspondence.imported-ladder-pairs-fock-modules-over, correspondence.spin-representation, std-algebra.vector-squares, std-algebra.blade-basis

Putting the last two steps together gives a new picture of spacetime itself.

Every point is null, so its vector acts on the Fock module as a nilpotent: \[ c(X(x))^{2} = Q(X(x)) = 0 \] Its kernel is a line of vacua, and two points are null-separated exactly when their lines share a vacuum.

**Theorem 8 (Spacetime as the manifold of vacuum lines).** In this picture every point of spacetime is a light-like vector, so in the algebra each point behaves like a zero divisor. Each point also carries a whole line of possible vacuum states, and two points are light-like separated exactly when their lines share a vacuum. The result then reads gravity as how these vacua change from point to point and quantum mechanics as the excitations above a chosen vacuum, with singularities where the family of vacua breaks down.

*Rests on:* one-relation.imported-pure-spinors-incidence-chart, one-relation.imported-witts-extension-theorem, one-relation.two-presentations, sheaf.localised-transport, sheaf.one-sided-completion, sheaf.one-sided-completion-singularity, std-algebra.inverse-of-vector

For the vacua to vary from point to point we need a rule for carrying spinors along.

Assuming the conformal manifold is spin, the spinor connection induced from the tractor gauge field has exactly the form of Penrose's local transport of four-component spinors. The two agree once one imported sign and normalisation convention for the Schouten term is matched.

**Theorem 9 (The conformal spinor connection is Penrose's local twistor transport).** Two older formalisms describe the geometry of conformal spacetime: tractors, a six-component bundle with its own connection, and Penrose's four-component bundle with its own transport rule. Assuming the conformal spacetime is spin, so that the tractor bundle has spinors (locally they always exist), this result shows that those spinors, built from the completion's Fock model, carry a connection with exactly the shape of Penrose's transport rule. The two agree completely once one sign and normalisation convention for the curvature term is matched, and that convention is the only thing imported.

*Rests on:* correspondence.imported-tractor-connection-local-twistor-transport-external

With transport in place, Einstein's equations can be stated in any of the three languages met so far.

On the region where the gravitational field $(\hb, \Omega)$ on flat spacetime is invertible, the vacuum and Einstein equations say that the infinity bivector \[ I_{\alpha\beta} = \Psi(I_g) \in \Lambda^{2}\CS \] is covariantly constant. It is simple, a genuine line of $\PCS$, exactly when the cosmological constant vanishes, by the same rule that matched null vectors with lines.

**Theorem 10 (One statement in three languages).** In this series gravity is a pair of fields on flat spacetime, and Einstein's vacuum equations can be phrased as the statement that one vector of the six-dimensional conformal model, the scale tractor, is constant as those fields carry it around. Translating that object into the spinors of the conformal algebra gives a bivector of that spinor space, the infinity bivector. This result shows that the three formulations say the same thing, and that the familiar fact that this bivector is a genuine line exactly when the cosmological constant vanishes is the same rule that matches lightlike vectors with lines.

*Rests on:* correspondence.imported-vacuum-equations-scale-tractor, correspondence.spinor-identification

## Results cited, not shown

**Fact (imported) 11 (The Chevalley pairing).** The spinor space of the completion carries a natural way, due to Chevalley, of pairing two spinors to give a number. This result fixes all its signs: it pairs the two chirality halves with each other, it changes sign when the two inputs are swapped, and it is compatible with the action of vectors and of the infinitesimal symmetries.

*Provenance:* Transport Lab claim correspondence.chevalley-pairing, version 4 (T09 Lem 3.3).

**Fact (imported) 12 (The chiral planes, and the summand spaces).** The Lorentz symmetry of spacetime, once complex numbers are allowed, splits into two independent halves. This result shows that the two planes into which the spinor space of the conformal algebra splits are exactly the basic two-component objects of these halves, one plane for each, and that together they rebuild the spacetime directions. It also shows that there is essentially only one symmetric way to combine a spacetime direction with one plane so as to land in the other.

*Provenance:* Transport Lab claim correspondence.chiral-planes-summand-spaces, version 5 (T09 Lem 4.4).

**Fact (imported) 13 (Imported: the forced completion and its fibre quadric).** In the algebra of spacetime some elements cannot be divided by, and nothing done inside the algebra fixes this. The smallest enlargement that does fix it adds two dimensions, one space-like and one time-like, and this enlargement is unique. The repaired divisions live on the set of light-like directions of the resulting six-dimensional space.

*Provenance:* Transport Lab claim correspondence.imported-forced-completion-fibre-quadric, version 6 (T09 Fact 2.1).

**Fact (imported) 14 (Imported: ladder pairs and Fock modules over the reals).** Two directions in this kind of algebra, one squaring to plus one and one to minus one, can be recombined into two elements of zero length that behave exactly like the operators that create and destroy a single fermion. Several such pairs together act on a space of states built by filling or emptying each mode, the usual Fock space of fermions. This is an imported result over the real numbers; the complex version is treated separately.

*Provenance:* cite[ S7] ButlerT1 ;  cite[ S 4] ButlerT3.

**Fact (imported) 15 (Imported: stabilisers in the flat model).** In the completed algebra, the symmetries that fix one special lightlike direction, the point at infinity, are exactly the symmetries of flat spacetime: rotations, boosts and translations. Allowing that direction to be rescaled adds one more symmetry, overall scaling. The translations are the same special transformations that appear in the series' earlier no-go theorem.

*Provenance:* Transport Lab claim correspondence.imported-stabilisers-flat-model, version 3 (T09 Fact 4.3).

**Fact (imported) 16 (Imported: the tractor connection, and the conformal spinor connection (local twistor transport), external ingredients).** A list of the published works from which the series takes its two standard connection formulas for conformal geometry. Nothing new is claimed here; the entry records where the borrowed results come from.

*Provenance:* R. Penrose and W. Rindler, Spinors and Space-Time, Vols. 1--2, Cambridge University Press (1984, 1986)., Vol.~2, Ch.~6; T. N. Bailey, M. G. Eastwood and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.; S. N. Curry and A. R. Gover, An introduction to conformal geometry and tractor calculus, with a view towards analysis on manifolds, in Asymptotic Analysis in General Relativity, London Mathematical Society Lecture Note Series 443, Cambridge University Press (2018), 86--170.; R. Penrose and M. A. H. MacCallum, Twistor theory: an approach to the quantisation of fields and space-time, Phys. Rep. 6 (1973), 241--316.; K. Dighton, An introduction to the theory of local twistors, Int. J. Theor. Phys. 11 (1974), 31--43..

**Fact (imported) 17 (Imported: the vacuum equations and the scale tractor).** Einstein's vacuum equations can be rewritten as the statement that one vector of the six-dimensional conformal model, attached to the choice of scale, does not change as the gravitational gauge fields carry it across flat spacetime. With a cosmological constant the same holds, and the squared length of that vector is a third of the constant. This entry restates both results from earlier in the series.

*Provenance:* Transport Lab claim correspondence.imported-vacuum-equations-scale-tractor, version 6 (T09 Fact 4.7).

**Fact (imported) 18 (Skew lines, splittings, hyperbolic planes: one datum).** Three different-looking pieces of structure turn out to be the same thing: a pair of non-intersecting lines in the projective spinor space, a splitting of the conformal spinor space into two planes, and a pair of lightlike directions of the kind the completion adds. Given any one, the other two follow. The four remaining directions, which mix the two planes, are exactly the directions perpendicular to the added pair.

*Provenance:* Transport Lab claim correspondence.skew-lines-splittings-hyperbolic-planes-one, version 4 (T09 Prop 4.1).

**Fact (imported) 19 (Imported: pure spinors and the incidence chart).** This collects earlier results that the one-relation paper needs. In six complex dimensions every four-component spinor of the conformal algebra is the vacuum of its own small system of fermionic operators, a coincidence special to this dimension. Each point of spacetime corresponds to a line of such spinors, and the standard way of placing spacetime points into the six-dimensional space makes every point a light-like vector.

*Provenance:* Transport Lab claim one-relation.imported-pure-spinors-incidence-chart, version 5 (T16 Fact 2.3).

**Fact (imported) 20 (Imported: Witt's extension theorem).** Witt's theorem concerns a space with a fixed rule for measuring lengths. It says that any length-preserving match between two pieces of the space extends to a length-preserving symmetry of the whole space, so pieces that look alike from the inside are also indistinguishable from the outside. It is a classical result from the 1930s.

*Provenance:* E. Witt, Theorie der quadratischen Formen in beliebigen K"orpern, J. Reine Angew. Math. 176 (1937) 31--44.; T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, \S4.

**Fact (imported) 21 (The two presentations).** The basic rule of a Clifford algebra can be written in two ways. In one it describes distances and angles, the language of geometry and gravity; in the other it is exactly the rule obeyed by fermions, the language of quantum theory. The paper takes this to mean that geometry and quantum structure are two views of one object, though only at the level of structure, not of how things evolve.

*Provenance:* Transport Lab claim one-relation.two-presentations, version 4 (T16 Prop 3.1).

**Fact (imported) 22 (Localised transport).** When the degenerate algebra is placed inside the larger completed algebra, it sits there unchanged. What changes is its surroundings: on the wall, a direction of zero length that was a dead end in the small algebra finds a partner in the large one, and together they behave like the creation and annihilation operators of a single fermion. This pairing happens only on the wall, so the fermion-like structure lives exactly where the geometry is singular.

*Provenance:* Transport Lab claim sheaf.localised-transport, version 5 (T04 Cor 4.5).

**Fact (imported) 23 (One-sided completion).** Assume a geometry degenerates along a wall in the tame way, with at least one positive direction on the physical side and with the dying direction's line consistently orientable along the wall. Then it can be repaired on that side by adding two extra dimensions and coupling them to the direction that is dying. This result shows that the coupling can be chosen so that the enlarged geometry is non-degenerate, with the same signature everywhere on the physical side, the wall itself included. The resulting family of algebras is then uniform: in the physical case every member is the algebra of four-by-four quaternion matrices.

*Provenance:* Transport Lab claim sheaf.one-sided-completion, version 4 (T04 Thm 4.4).

**Fact (imported) 24 (One-sided completion at the singularity).** The completion that repairs a degenerating geometry can be carried out at the central singularity of a Schwarzschild black hole, once that singularity has been opened up into a boundary. Coupling two extra dimensions to the dying direction, with the sign of the coupling chosen to suit the black-hole interior and the coupling switched on only inside the horizon, gives a geometry that is non-degenerate everywhere, and no new degeneracy appears anywhere else. The fermion-like pairing then lives exactly on the opened-up singularity, which has the shape of a line times a sphere.

*Provenance:* Transport Lab claim sheaf.one-sided-completion-singularity, version 4 (T04 Thm 8.12).

**Fact (imported) 25 (The blade basis, degenerate forms included).** Every element of the algebra is a combination of products of distinct basis arrows, and no such product can be written in terms of the others. In $n$ dimensions there are $2^{n}$ of them: the number, the arrows, the planes, the volumes and so on. This stays true even when some directions have zero length.

*Provenance:* Transport Lab claim std-algebra.blade-basis, version 1.

**Fact (imported) 26 (The complex Clifford algebra, its classification modulo 2, its Fock model and its pairing).** Allowing complex coefficients erases the difference between space-like and time-like directions, so the algebra depends only on the number of dimensions: a single complex matrix algebra in even dimension and a pair of them in odd dimension. In even dimension the matrix algebra is the algebra of creation and annihilation operators of fermion modes, and the states carry a pairing that every rotation respects.

*Provenance:* Transport Lab claim std-algebra.complex-clifford-algebra, version 1.

**Fact (imported) 27 (The Clifford algebra exists and is unique).** The rule "an arrow squared is a number" can always be realised by an actual algebra, and in essentially one way only. One explicit construction lets arrows act on oriented areas and volumes by adding a direction or removing one.

*Provenance:* Transport Lab claim std-algebra.existence-uniqueness, version 1.

**Fact (imported) 28 (Which vectors and versors are invertible).** An arrow can be "divided by" exactly when its square length is not zero. Arrows of zero length, like light rays, cannot be inverted: multiplying such an arrow by itself gives zero. Products of invertible arrows are always invertible, and their inverse is found by writing the product backwards and dividing by a number.

*Provenance:* Transport Lab claim std-algebra.inverse-of-vector, version 1.

**Fact (imported) 29 (Reflection in a non-null vector).** Multiplying an arrow on both sides by a fixed arrow, with a sign, gives its mirror image in the plane perpendicular to the fixed arrow. This works for any fixed arrow that does not have zero length. Mirrors are the building blocks of all rotations.

*Provenance:* Transport Lab claim std-algebra.reflection, version 1.

**Fact (imported) 30 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 31 (The group of null rotations).** Among the symmetries of a space with both space and time directions, some leave a chosen light-like direction exactly in place while shearing other directions along it. These null rotations combine just as vectors add in the directions perpendicular to the light ray and its partner. Ordinary rotations of those perpendicular directions act on the null rotations in the expected way.

*Provenance:* Transport Lab claim transport.group-null-rotations, version 4 (T01 Lem 4.6).

**Fact (imported) 32 (Totality).** In a Clifford algebra with vectors of zero length, the reciprocal of a vector is undefined on exactly those vectors. After moving to the enlarged space of points, a single reflection-like operation gives a reciprocal everywhere: it agrees with the usual one on ordinary vectors and sends zero-length vectors to points at infinity. Those values are the limits one would expect, and no other continuous rule matches the usual reciprocal.

*Provenance:* Transport Lab claim transport.totality, version 3 (T01 Thm 4.10).

Starting from points as null vectors, the trail has recovered the conformal spinor space, the Klein correspondence, the incidence relation, the reality condition and local spinor transport, all from the completion itself.

No postulate is needed on this stretch; the one standing condition is that the conformal manifold be spin, which the transport step assumes. The vacuum-line picture of spacetime that emerges is the ground the later subjects build on.
