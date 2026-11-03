# The singularity

**Abstract.** This trail goes to the centre of a non-rotating black hole and asks exactly what fails there. The gauge field describing the black hole is the identity plus a shear $P$ with $P^2 = 0$, so it can be inverted at every radius, the event horizon included.

All of the blow-up lives instead in the connection and the curvature. A curvature invariant that no gauge choice can alter grows without bound at the centre, so the breakdown is real rather than an artefact.

Once the growth is divided out, the field settles to a degenerate limit with a null direction that has no partner: an obstruction of type N. Adding a hyperbolic plane, coupled to the lost direction only inside the horizon, repairs the geometry everywhere, the centre included.

The walk follows the order of the argument: first the gauge field and its connection, then where the divergence sits and why it cannot be removed, then the exact shape of the degeneration and what the series makes of it.

## The singularity

Each step below narrows down where, and in what sense, the black-hole solution breaks at its centre.

We start with the gravitational field itself, which in Gauge Theory Gravity is a linear map $\hb$ acting on the directions of flat spacetime.

In the Painlev\'e-Gullstrand gauge it is $\hb = 1 - \beta P$ with $P^2 = 0$ exactly, so its inverse is \[ \hb^{-1} = 1 + \beta P \] at every $r > 0$. At the horizon, $\beta = 1$, division does not fail: the horizon is algebraically unremarkable.

**Theorem 1 (The unipotent ray).** In this formulation of gravity, the field describing a non-rotating black hole is the identity plus a shear whose square is zero. That makes it reversible at every radius, with an explicit formula for the inverse. In particular nothing goes wrong algebraically at the event horizon.

The field $\hb$ is only half of the description; the other half is the rotation-gauge field $\Omega$, which records how local frames boost and rotate from point to point.

Here it is a multiple of the single radial boost bivector $\sigma_r$: \[ \Omega(\partial_t) = \frac{M}{r^2}\,\sigma_r, \qquad \Omega(\partial_r) = \sqrt{\frac{M}{2r^3}}\;\sigma_r \] Along time it is Newton's field strength, while along the radius it grows without bound towards the centre.

**Theorem 2 (The connection bivector, computed).** In the gauge-theory description of gravity, the connection records how local frames boost and rotate from point to point. For a non-rotating black hole in this gauge it can be written down exactly. Along the time direction it equals Newton's gravitational field strength, mass over radius squared, at every radius; along the radial direction it grows without bound towards the centre, at the square root of the rate at which the field strength grows.

Putting the two halves together locates the trouble.

The pair solves the vacuum equations at every $r > 0$ with $\det \hb = 1$ throughout, so the divergence lives in $\Omega$ and in the curvature, not in $\hb$. Reading this as a statement about Einstein's theory uses the imported equivalence of the two, wherever $\hb$ is invertible.

**Theorem 3 (The solution, and where the divergence lies).** The gravitational field of a non-rotating black hole is written here in a gauge-theory language with two ingredients: a field describing how lengths are stretched, and a connection describing how directions turn. The first ingredient stays well behaved at every distance from the centre and never squeezes or expands volume. All of the blow-up as the centre is approached lives in the connection, in the curvature built from it, and in the ordinary metric components.

*Rests on:* singularity.connection-bivector-computed, singularity.imported-equivalence-einstein-equations

Since the curvature carries the divergence, it is worth seeing its form exactly.

Acting on bivectors $B$, the field strength is a fixed shape times one scalar, \[ \mathcal{R}(B) = -\frac{M}{r^3}\,S(B), \qquad S = 1 - 3\Pi \] where $\Pi$ projects onto the radial plane and its dual. The shape $S$, with spectrum $(-2,-2,1,1,1,1)$, never changes; only $M/r^3$ grows.

**Theorem 4 (The curvature of the gauge field: exact shape decoupling).** The tidal curvature of a non-rotating black hole splits exactly into a fixed geometric shape times a single number. The shape singles out the radial direction and is the same at every radius; only the strength, mass divided by radius cubed, changes. So the whole approach to the central singularity is governed by that one scalar.

*Rests on:* pairing.imported-weyl-scalars-petrov-type-schwarzschild

A blow-up seen in one gauge might still be an artefact of that gauge.

This step closes the loophole with the curvature scalar \[ K = R_{abcd}R^{abcd} = \frac{48\,M^2}{r^6} \] which every gauge transformation leaves unchanged and which diverges as $r \to 0$. The division-by-zero locus is therefore a property of the solution, not of its presentation.

**Theorem 5 (Non-removability: the invariant argument).** At the centre of a non-rotating black hole, a measure of curvature that does not depend on how the description is set up grows without bound. Because every change of description allowed in the theory leaves this quantity unchanged, no choice of description can make the blow-up disappear. The breakdown at the centre is therefore a feature of the solution itself rather than an artefact of how it is written down.

*Rests on:* singularity.solution-where-divergence-lies

Knowing that something genuinely fails, the next question is what shape the failure takes.

Divided by its growth, the field tends to a rank-one limit, $\beta^{-1}\hb \to -P$, and the metric to \[ \hat g(a,b) = -(a\cdot\et)(b\cdot\et) \] a form of signature $(0,1,3)$ that sees only the time direction. The radial direction $\er$ joins its radical only in the limit, never at any finite radius.

**Theorem 6 (The degeneration, exactly).** Approaching the centre of a black hole the gravitational field grows without bound, but once that overall growth is divided out the field settles to a definite limit. The limit is degenerate: it registers only the time direction and is blind to the other three. The radial direction, along which the light cones fold, becomes one of these blind directions only in the limit, not at any finite distance from the centre.

The same collapse shows up in the light cones.

The two radial null directions are $\et + (-\beta \pm 1)\er$, and as $r \to 0$ both tip inward and merge onto the single direction $\er$, while $g(\et,\et)$ diverges. No gauge choice removes this degeneration through a null kernel direction.

**Theorem 7 (The cones fold).** Light cones record the directions in which light can travel at each point. Following the two radial light directions inward towards the centre of a black hole, both swing round to point inward and, in the limit at the centre, merge into a single direction. At the same time the time part of the metric grows without bound, so the classical field cannot be rescaled to stay finite and well behaved there, and the failure cannot be removed by a change of gauge.

*Rests on:* singularity.degeneration-exactly, singularity.non-removability-invariant-argument, std-algebra.orthogonal-anticommute

The series classifies the ways in which division can fail, and this step places the black-hole centre in that classification.

The obstruction is of type N, a null direction with no metric partner. Type C cannot occur, because $\Cl(1,3) \cong \Mat_2(\HH)$ is central simple, and type P is present but imposes no transport.

That diagnosis decides the repair: supply the missing partner by the Witt completion.

**Theorem 8 (Type N, and only type N).** At the centre of a non-rotating black hole one direction of the geometry collapses, and this result identifies which kind of algebraic obstruction that is in the series' classification. It is the kind caused by a direction with no partner to pair with. The other substantive kind, which would need the algebra to split into independent pieces, cannot occur for the algebra of spacetime, and a third kind is present but harmless. So the repair that applies is the one that supplies the missing partner by enlarging the algebra.

*Rests on:* sheaf.localised-transport, sheaf.one-sided-completion, sheaf.one-sided-completion-singularity, sheaf.schwarzschild-degeneration-boundary-tame, singularity.degeneration-exactly, tower.rigidity-clock-frozen, transport.existence-classification-type-c, transport.existence-locus-type-n, transport.type-p-self-repairing, primer.classification-real-clifford-algebras, std-algebra.sta-matrix

The repair is carried over from the series' general treatment of degenerating geometries.

A hyperbolic plane $(\nO, \nInf)$ is adjoined and coupled to the dying direction, with $\mu\nu < 0$ and a bump inside the horizon, and the ambient form then has constant signature $(2,4)$ everywhere, the singularity included. The ladder pair that partners the lost direction exists exactly over the singularity, and no shadow wall forms anywhere.

**Theorem 9 (Imported: one-sided completion at the singularity).** The centre of a non-rotating black hole is where the geometry loses a direction. This result, carried over from the sheaf paper, adds two extra directions and couples them to the lost one, with couplings of opposite sign switched on only inside the horizon, so that the enlarged geometry is non-degenerate everywhere, the centre included. The new partner for the lost direction exists exactly at the centre, and the repair creates no new defect anywhere else.

*Rests on:* sheaf.one-sided-completion-singularity, sheaf.schwarzschild-degeneration-boundary-tame

## Results cited, not shown

**Fact (imported) 10 (Imported: the Weyl scalars, and the Petrov type of Schwarzschild).** The part of the gravitational field strength that describes tidal forces and gravitational waves can be summarised by five complex numbers relative to a frame of light-like directions. Black holes like Schwarzschild are especially simple: in the natural frame only one of the five is nonzero, and the radial light rays are the field strength's special directions. This standard result is imported.

*Provenance:* R. Penrose, W. Rindler, Spinors and Space-Time, Vol. 2: Spinor and Twistor Methods in Space-Time Geometry, Cambridge University Press (1986)., Ch.~8; E. Newman, R. Penrose, An approach to gravitational radiation by a method of spin coefficients, J. Math. Phys. 3 (1962) 566--578..

**Fact (imported) 11 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which one appears depends only on p minus q, in a pattern that repeats every eight steps. The algebra splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Provenance:* Transport Lab claim primer.classification-real-clifford-algebras, version 3 (T00 Thm 9.3).

**Fact (imported) 12 (Localised transport).** When the degenerate algebra is placed inside the larger completed algebra, it sits there unchanged. What changes is its surroundings: on the wall, a direction of zero length that was a dead end in the small algebra finds a partner in the large one, and together they behave like the creation and annihilation operators of a single fermion. This pairing happens only on the wall, so the fermion-like structure lives exactly where the geometry is singular.

*Provenance:* Transport Lab claim sheaf.localised-transport, version 5 (T04 Cor 4.5).

**Fact (imported) 13 (One-sided completion).** Assume a geometry degenerates along a wall in the tame way, with at least one positive direction on the physical side and with the dying direction's line consistently orientable along the wall. Then it can be repaired on that side by adding two extra dimensions and coupling them to the direction that is dying. This result shows that the coupling can be chosen so that the enlarged geometry is non-degenerate, with the same signature everywhere on the physical side, the wall itself included. The resulting family of algebras is then uniform: in the physical case every member is the algebra of four-by-four quaternion matrices.

*Provenance:* Transport Lab claim sheaf.one-sided-completion, version 4 (T04 Thm 4.4).

**Fact (imported) 14 (One-sided completion at the singularity).** The completion that repairs a degenerating geometry can be carried out at the central singularity of a Schwarzschild black hole, once that singularity has been opened up into a boundary. Coupling two extra dimensions to the dying direction, with the sign of the coupling chosen to suit the black-hole interior and the coupling switched on only inside the horizon, gives a geometry that is non-degenerate everywhere, and no new degeneracy appears anywhere else. The fermion-like pairing then lives exactly on the opened-up singularity, which has the shape of a line times a sphere.

*Provenance:* Transport Lab claim sheaf.one-sided-completion-singularity, version 4 (T04 Thm 8.12).

**Fact (imported) 15 (The Schwarzschild degeneration is boundary-tame in $\shW$).** At the centre of a Schwarzschild black hole the gravitational field is singular. Once the singularity is opened up into a boundary and suitably rescaled directions are used, the field's measure of lengths extends smoothly to that boundary and degenerates there in the mildest possible way: exactly one direction loses its length, and it does so at a linear rate. That dying direction is the same in two standard coordinate systems, and it is perpendicular to the slices traced out by observers falling freely inward.

*Provenance:* Transport Lab claim sheaf.schwarzschild-degeneration-boundary-tame, version 6 (T04 Thm 8.7).

**Fact (imported) 16 (Imported: equivalence with the Einstein equations).** Gravity can be described either as the curvature of spacetime, as in Einstein's theory, or as a gauge theory on flat spacetime written in geometric algebra. This imported result says that wherever the gauge field is invertible the two descriptions have equivalent field equations and the same curvature. Curvature calculations can therefore be done in either language and combined.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 17 (Orthogonal vectors anticommute).** Perpendicular arrows anticommute: swapping their order flips the sign. That single fact, plus the squares of the basis arrows, gives the whole multiplication table.

*Provenance:* Transport Lab claim std-algebra.orthogonal-anticommute, version 1.

**Fact (imported) 18 (The spacetime algebra as a matrix algebra, and the spacetime split).** The algebra of spacetime arrows can be written with $2 \times 2$ arrays of quaternions, or, after allowing complex numbers, with the $4 \times 4$ Dirac matrices of relativistic quantum mechanics. Its even part is exactly the algebra of an observer's ordinary three-dimensional space.

*Provenance:* Transport Lab claim std-algebra.sta-matrix, version 1.

**Fact (imported) 19 (Rigidity; the clock is frozen).** Building the tower by adding pairs of opposite-signed directions never changes the essential type of the algebra. Every floor has the same underlying number system, the same centre and the same kinds of obstruction as the ground floor. For the spacetime algebra, every floor is a matrix algebra over the quaternions, so the eight-step Bott clock does not advance along the tower: it stays where it starts.

*Provenance:* Transport Lab claim tower.rigidity-clock-frozen, version 5 (T03 Thm 3.6).

**Fact (imported) 20 (Existence and classification of type C).** Some Clifford algebras secretly come in two independent halves, and the elements that pick out each half are called central idempotents. This result pins down exactly when that happens: precisely when the number of positive directions minus the number of negative ones leaves remainder 1 on division by four. In that case there are exactly two such elements, built from the product of all the basis directions. Reversing every direction swaps the two halves, but no conjugation by an element of the algebra itself can do so, since these elements commute with everything.

*Provenance:* Transport Lab claim transport.existence-classification-type-c, version 4 (T01 Thm 3.6).

**Fact (imported) 21 (Existence locus of type N).** In a space with both positive and negative directions, like the space-time of relativity, there are nonzero directions of zero length, called null directions. This result says they exist exactly when both kinds of direction are present, and that they then form a cone, much like a light cone. Each such direction multiplied by itself gives zero, so it can never be divided by, even in a larger algebra that contains the original one.

*Provenance:* Transport Lab claim transport.existence-locus-type-n, version 5 (T01 Prop 3.3).

**Fact (imported) 22 (Type P is self-repairing).** Some zero divisors are projection-like elements, ones that equal their own square. For these, the repair being sought is already available: each such element can serve as its own partner and satisfies the required identities. Because the rule is simply to take the element itself, it automatically respects every symmetry, so nothing needs to be added to the algebra.

*Provenance:* Transport Lab claim transport.type-p-self-repairing, version 2 (T01 Prop 6.1).

The thread runs from a field that inverts everywhere away from the centre, through a divergence no gauge choice removes, to a degenerate limit with one partnerless null direction and the completion that supplies its partner.

This walk adds no postulate of its own; it rests on imported results, above all the equivalence of Gauge Theory Gravity with Einstein's equations wherever $\hb$ is invertible. The repair uses the general completion only after the black-hole degeneration has been shown to be of the tame kind the completion requires.
