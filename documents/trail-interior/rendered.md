# Inside the black hole

**Abstract.** This trail goes inside a black hole, where the fall towards the centre becomes a passage of time. Near the centre of a non-rotating black hole the geometry is of Kasner form: one direction stretches while the other two shrink, each as a fixed power of proper time.

After rescaling by the natural clock, the rotation-gauge field settles to three pure boosts with the Kasner weights, which generate exactly the Lorentz algebra $\mathfrak{so}(1,3)$. A cosmological constant leaves that limit unchanged.

For a rotating black hole the series' rule, that trouble arises where a quantity cannot be inverted, picks out exactly the singular ring. The walk ends at the unstable inner horizon and at an open conjecture about the ring.

The walk starts with the non-rotating black hole, building from its Kasner form to the limit at the singularity, and then turns to the rotating black hole.

## Inside the black hole

Each step looks a little closer at the region inside the horizon, first without rotation and then with it.

We begin with the shape of the geometry inside the horizon, where the radius $r$ runs like a clock.

In proper time $\tau$, with the singularity at $\tau = 0$, the derived metric is synchronous and diagonal, and to leading order its scale factors obey \[ \sqrt{A} \propto \tau^{-1/3}, \qquad r \propto \tau^{2/3} \] These are the Kasner exponents $(-\tfrac13, \tfrac23, \tfrac23)$: one direction stretches while two shrink.

**Theorem 1 (Kasner form of the interior).** Inside a non-rotating black hole the roles of space and time swap, and the fall towards the centre becomes a passage of time. In the right time variable the gravitational field near the centre looks like a Kasner universe: one direction stretches while the other two shrink, each, to leading order, as a fixed power of time. This result gives those powers, minus one third and two thirds twice, together with the first corrections.

*Rests on:* interior.imported-schwarzschild-curvature-spectrum

An observer falling towards the centre can carry a frame of reference directions along.

The adapted frame is exactly parallel along the free-fall worldlines, at every $\tau > 0$, so carrying it into the singularity is not an asymptotic question. The expansion rates reach the Kasner exponents at the single rate $O(\tau^{2/3})$, without oscillation.

**Theorem 2 (Exact parallelism, and the convergence rate).** Inside a non-rotating black hole, an observer falling towards the centre can carry a set of reference directions along. This result shows that a natural choice of such directions is carried along perfectly, with no drift at all, right up to the singularity. It also gives the exact rate at which the stretching and squeezing of space approach the idealised Kasner pattern, and shows that the approach is smooth, without oscillation.

*Rests on:* interior.kasner-form-interior

With a parallel frame in hand, the rotation-gauge field can be written down exactly.

On each unit tangential direction the field $\Omega$ is a pure boost $B_i = e_0 \wedge e_i$ at the expansion rate $\sigma_i$, plus one rotation from the round spheres: \[ \Omega(e_1) = -\sigma_1 B_1, \qquad \Omega(e_3) = -\sigma_3 B_3 + \frac{\cot\theta}{r}\,R_{23} \] Along the direction of fall it vanishes, $\Omega(e_0) = 0$.

**Theorem 3 (The interior connection, exactly).** This result writes down exactly how directions twist into one another as one moves about inside a non-rotating black hole. Along each direction the effect is a pure stretching, except for one extra rotation term that reflects the curvature of the spheres of fixed radius. That rotation term grows like one over the radius.

*Rests on:* interior.exact-parallelism-convergence-rate

This is the central result about the approach to the singularity.

After Hubble normalisation, rescaling by the natural clock, the connection tends to \[ -\sum_i p_i\, B_i \otimes \hat\theta^i \] three pure boosts weighted by the Kasner exponents $p_i$, for Schwarzschild and every admissible metric. The scale tractor extends as a parallel section, and the boundary holonomy algebra is exactly $\Lambda^2 W \cong \mathfrak{so}(1,3)$.

**Theorem 4 (Weighted limit theorem).** This is the central result about the approach to the singularity of a non-rotating black hole, and of a wider class of similar singularities. After rescaling by the natural clock, the rules for carrying directions settle to a clean limit at the singularity: three pure stretchings with the Kasner weights, and nothing else. These generate exactly the algebra of Lorentz transformations, while the parts of the larger symmetry that caused obstructions elsewhere in the series receive nothing.

*Rests on:* interior.boosts-generate-exactly-levi-factor, interior.covariant-form-vacuum-equations, interior.exact-parallelism-convergence-rate, interior.interior-connection-exactly, interior.kasner-form-interior, interior.metric-parallelism-trace-schouten-condition, interior.non-null-stabilisers-section-they-act, interior.scale-tractor-leaves-cone, interior.stabilisers-flat-model

A natural worry is whether that limit survives a cosmological constant.

It does: near the centre the corrections are of order $\Lambda\tau^2$, below the $O(\tau^{2/3})$ recovery rate, so the exponents, data and rate are unchanged. For $\Lambda > 0$ the limit algebra lies in the reductive stabiliser $\mathfrak{so}(1,4)$, a simplification rather than a complication.

**Theorem 5 (Schwarzschild-de Sitter weighted limit).** A cosmological constant, the ingredient behind the accelerating expansion of the universe, changes a black hole's gravitational field only very slightly near its centre. This result shows that the limiting behaviour at the singularity is the same as without it, with the same powers and the same rates. The one change is algebraic, and it makes the picture simpler rather than more complicated.

*Rests on:* interior.boosts-generate-exactly-levi-factor, interior.exact-parallelism-convergence-rate, interior.kasner-form-interior, interior.non-null-stabilisers-section-they-act, interior.scale-tractor-leaves-cone, interior.weighted-limit-theorem

The walk now turns to rotating black holes.

In the commuting subalgebra $\R \oplus \R I$, with $I$ the pseudoscalar and $I^2 = -1$, the Kerr curvature is the Schwarzschild shape operator times the scale \[ \mathfrak{M} = -M\,(r - Ia\cos\theta)^{-3} \] Its base fails to be invertible exactly on the ring $r = 0$, $\theta = \pi/2$, which is where the black hole is singular.

**Theorem 6 (Complex factorisation and the location of the ring).** The curvature of a rotating black hole can be written as the curvature of a non-rotating one, with the radius replaced by a complex number built from the radius and the angle. The series' rule is that trouble arises where a quantity cannot be inverted. Applied to this complex number, the rule picks out exactly the ring where a rotating black hole is singular, and says that the disc spanning the ring is regular.

*Rests on:* interior.exact-scale-decoupling, interior.imported-kerr-curvature

That scalar-plus-pseudoscalar scale turns out to be a well-known object.

It is the inverse cube of the Walker-Penrose Killing-spinor scalar, \[ \mathfrak M = -M\,\chi^{-3}, \qquad \chi = r - Ia\cos\theta \] So going once around the ring, the curvature's duality phase turns $-3$ times as far as the spinor's.

**Theorem 7 (The complex scale is the inverse cube of the Killing spinor).** A previous result produced a complex number that controls the curvature of a rotating black hole. This result shows that the number is, up to a cube and a constant, a well-known object: the Killing spinor behind Carter's hidden conserved quantity for orbits around a rotating black hole. Going once around the singular ring, the curvature's phase therefore turns three times as often as the spinor's, in the opposite sense.

*Rests on:* interior.complex-factorisation-location-ring, interior.imported-kerr-curvature, interior.imported-walker-penrose-killing-spinor

A rotating black hole also has an inner horizon, which established results show to be unstable: infalling radiation makes the curvature grow without limit there while the geometry stays continuous.

Read in the series' language, this is a type-N degeneration, the same class as at the centre of a non-rotating black hole, realised on a null hypersurface. Survival is ordered by derivative level: point-level structure extends, connection-level structure generically fails, proved in spherical symmetry and expected for Kerr.

**Theorem 8 (The filtration at the Cauchy horizon, read from the literature).** The inner horizon of a rotating black hole is known to be unstable: perturbations make the strength of the gravitational field blow up there, although the field itself stays continuous. This result translates those established findings into the series' language. It finds the same kind of breakdown as at the centre of a non-rotating black hole, one that generically hits the rules for comparing directions but not the field itself (proved in the spherically symmetric case and expected for rotating holes), and it places the divergence where the framework expects it.

*Rests on:* interior.imported-mass-inflation-stability, interior.stabilisers-flat-model, singularity.type-n-only-type-n

The walk ends with an open problem rather than a result.

Since the curvature's phase winds around the ring, the conjecture is that the completion's exceptional structure over the ring is a duality-monodromy fibration, whose structure group contains the duality circle. The winding number three of the Kerr scale would be an invariant of that fibration; it is posed, not proved.

**Conjecture 9 (Duality-monodromy fibration over the ring).** Going once around the ring singularity of a rotating black hole, the complex phase of the curvature turns three times. The conjecture is that this twisting is the visible trace of a larger geometric structure attached to the ring, a bundle whose twisting links the different sheets of the black hole's extended spacetime. It is posed as an open problem, not proved.

## Results cited, not shown

**Fact (imported) 10 (The boosts generate exactly the Levi factor).** Among the symmetries of the series' six-dimensional ambient space, take the three boosts, the transformations that change velocity along each spatial axis. Repeatedly combining them produces exactly the six Lorentz transformations of ordinary spacetime and nothing else. In particular, boosts alone never generate a translation or a rescaling.

*Provenance:* Transport Lab claim interior.boosts-generate-exactly-levi-factor, version 4 (T06 Lem 5.4).

**Fact (imported) 11 (Covariant form of the vacuum equations).** In the interior region, Einstein's equations for empty space can be recast as a single condition on the gravitational fields: a particular marker in the six-dimensional conformal extension of spacetime, attached to the physical scale, must stay constant as it is carried from point to point by a gauge field built from gravity. This result proves that the two formulations are exactly equivalent, and that the marker is a null (lightlike) object. It also notes that merely having some constant marker of this kind is a weaker condition that does not by itself give the field equations.

*Provenance:* Transport Lab claim interior.covariant-form-vacuum-equations, version 5 (T06 Thm 4.5).

**Fact (imported) 12 (Exact scale decoupling).** Near a Schwarzschild black hole the tidal curvature has a fixed pattern: stretching in one pair of directions and squeezing in the others, in a two-to-one ratio. This result shows the pattern is exactly the same at every radius, all the way in towards the singularity. Only its overall strength, which grows like the inverse cube of the radius, changes.

*Provenance:* Transport Lab claim interior.exact-scale-decoupling, version 4 (T06 Prop 3.3).

**Fact (imported) 13 (Imported: the Kerr curvature).** This is the standard description of the strength of the gravitational field around a rotating black hole, the quantity that plays the part of spacetime curvature, written in the language of geometric algebra on a flat background. The strength of the curvature is controlled by a single complex number built from the radius and the angle from the rotation axis. The result is taken from the literature.

*Provenance:* C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~14; B. Carter, Global structure of the Kerr family of gravitational fields, Phys. Rev. 174 (1968), 1559--1571..

**Fact (imported) 14 (Imported: mass inflation and $C^0$ stability).** The inner horizon of a charged or rotating black hole is unstable. Radiation falling in piles up there and the strength of the gravitational field grows without limit, yet the field itself remains continuous and an infalling object is stretched only by a finite amount. These are established results of mathematical relativity taken from the literature; for rotating black holes part of the picture is still conjectural.

*Provenance:* E. Poisson and W. Israel, Internal structure of black holes, Phys. Rev. D 41 (1990), 1796--1809.; M. Dafermos and J. Luk, The interior of dynamical vacuum black holes I: the $C^0$-stability of the Kerr Cauchy horizon, preprint, arXiv:1710.01722 (2017).; J. Luk and S.-J. Oh, Strong cosmic censorship in spherical symmetry for two-ended asymptotically flat initial data I. The interior of the black hole region, Ann. of Math. (2) 190 (2019), 1--111.; J. Luk and S.-J. Oh, Strong cosmic censorship in spherical symmetry for two-ended asymptotically flat initial data II. The exterior of the black hole region, Ann. PDE 5 (2019), Art. 6.; A. Ori, Inner structure of a charged black hole: an exact mass-inflation solution, Phys. Rev. Lett. 67 (1991), 789--792..

**Fact (imported) 15 (Imported: the Schwarzschild curvature spectrum).** The tidal part of the gravitational field strength around a non-rotating black hole has a simple form: one pair of planes feels a stretching or squeezing of one strength, and the four remaining mixed planes feel half that strength with the opposite sign. This standard result is restated from earlier work in the series.

*Provenance:* Transport Lab claim interior.imported-schwarzschild-curvature-spectrum, version 6 (T06 Fact 2.2).

**Fact (imported) 16 (Imported: the Walker-Penrose Killing spinor).** Rotating black holes have a hidden symmetry, which gives orbits an extra conserved quantity discovered by Carter. That symmetry comes from a special spinor field, whose basic invariant is a simple complex combination of the radius and the angle. This is a classical result taken from the literature.

*Provenance:* M. Walker and R. Penrose, On quadratic first integrals of the geodesic equations for type $22$ spacetimes, Commun. Math. Phys. 18 (1970), 265--274.; B. Carter, Global structure of the Kerr family of gravitational fields, Phys. Rev. 174 (1968), 1559--1571..

**Fact (imported) 17 (Metric parallelism, and the trace of the Schouten condition).** This lemma records two elementary facts behind the tractor form of the gravitational field equations. First, the natural derivative on the tractor bundle, which on flat spacetime is a field of rotations of the six-dimensional conformal model, respects that model's own notion of length. Second, if the Schouten tensor, a rearranged form of the gravitational field strength, is a multiple of the metric then the field is Einstein, and the Schouten tensor vanishes exactly when the Ricci curvature does.

*Provenance:* Transport Lab claim interior.metric-parallelism-trace-schouten-condition, version 6 (T06 Lem 4.2).

**Fact (imported) 18 (Non-null stabilisers, and the section they act on).** In the series' six-dimensional ambient space, pick a direction whose squared length is not zero. The symmetries that leave it fixed are those of de Sitter space if the squared length is positive, or of anti-de Sitter space if it is negative. A natural slice of the space of points is then exactly that de Sitter or anti-de Sitter spacetime, and its boundary at infinity is spacelike or timelike accordingly.

*Provenance:* Transport Lab claim interior.non-null-stabilisers-section-they-act, version 4 (T06 Prop 4.4).

**Fact (imported) 19 ($\Lambda \neq 0$: the scale tractor leaves the cone).** Einstein's equations with a cosmological constant can be written as the statement that one vector of the six-dimensional conformal model, the scale tractor, is unchanged as the gravitational gauge fields carry it from point to point. Its squared length turns out to be the cosmological constant divided by three. With no cosmological constant it has zero length, and any nonzero cosmological constant moves it off the cone of zero-length directions.

*Provenance:* Transport Lab claim interior.scale-tractor-leaves-cone, version 7 (T06 Thm 4.7).

**Fact (imported) 20 (Stabilisers in the flat model).** In the flat model of the series' six-dimensional ambient space, the point at infinity is a direction of zero length. The symmetries that fix it are exactly those of flat spacetime, Lorentz transformations and translations, ten in all, with one extra rescaling if only its direction must be kept. The translations act as shears that tilt everything towards the point at infinity, and they are the same shears that block the naive way of dividing by zero.

*Provenance:* Transport Lab claim interior.stabilisers-flat-model, version 5 (T06 Prop 4.3).

**Fact (imported) 21 (Type N, and only type N).** At the centre of a non-rotating black hole one direction of the geometry collapses, and this result identifies which kind of algebraic obstruction that is in the series' classification. It is the kind caused by a direction with no partner to pair with. The other substantive kind, which would need the algebra to split into independent pieces, cannot occur for the algebra of spacetime, and a third kind is present but harmless. So the repair that applies is the one that supplies the missing partner by enlarging the algebra.

*Provenance:* Transport Lab claim singularity.type-n-only-type-n, version 5 (T05 Prop 3.1).

The thread runs from the Kasner form of the non-rotating interior, through a parallel frame and an exact connection, to the limit at the singularity, and then carries the same invertibility rule into the rotating case.

No postulate of the series enters this walk; its rotating part rests on imported results, namely the Kerr curvature, its Killing spinor and the instability of its inner horizon. The inner-horizon step inherits the parts of that literature that are still conjectural for rotating black holes.
