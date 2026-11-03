# The origin of mass

**Abstract.** Where does mass come from in this framework? The completion has one built-in scale, the frozen point set by the cosmological constant, and mass is read as how strongly a particle grips it.

Two massless conformal spinors (twistors) make a massive composite whose mass measures how far apart their light-like directions point, and the trail shows the two readings agree exactly. A second reading turns mass into one number a field carries, its conformal weight.

The trail then meets the subject's main refutation: tying every mass to the cosmological scale restates the hierarchy rather than explaining it. It closes on a clear record of which routes to the absolute mass scale fail.

The walk first fixes the one scale the framework has, then builds mass from conformal spinors and from weights, joins the two, and ends with what the mechanism does not explain.

Results a step rests on but that are not on the trail are listed at the end.

## Dark energy and the frozen point

Mass needs a scale to be measured against, so the walk begins with the frozen point of the dark-energy subject.

On flat spacetime, de Sitter space is the gravitational field $\hb = \sigma$, a pure dilation by the function $\sigma = 1 - \Lambda Q(x)/12$.

Its frozen point is the unique constant vector \[ I_\Lambda = n_\infty + \frac{\Lambda}{6}\,n_0 \] of squared norm $\Lambda/3$, with $n_0$ and $n_\infty$ the two null directions the completion adds. With the cosmological constant switched off it is the point at infinity $n_\infty$.

**Theorem 1 (The de Sitter scale and its frozen point).** De Sitter space, the universe with only a positive cosmological constant, needs no curved background: on ordinary flat spacetime it is a gravitational field that rescales every length by one simple function of position. This lemma finds the frozen point of that field and shows that it is a single fixed vector of the larger conformal space. When the cosmological constant is switched off, that vector becomes the familiar point at infinity of flat space's conformal model.

*Rests on:* mass.imported-flat-model-twistor-chart-infinity, mass.imported-frozen-point-tractor-connection, mass.imported-thomas-operator

## The origin of mass

With the scale in hand, these results build mass from conformal spinors and from conformal weights, and test what the construction explains.

Before using the frozen point, recall how two conformal spinors make mass. A single conformal spinor carries null momentum and is massless.

Two of them with spinor parts $\pi^{1}$ and $\pi^{2}$ have \[ m^{2} = 2\,\bigl|\br{\pi^{1}\pi^{2}}\bigr|^{2}, \] the squared symplectic area between the two spinor parts. Aligned spinors give a massless composite, and mass grows with the misalignment.

**Theorem 2 (Mass as symplectic area: the two-spinor formula).** A single spinor of the conformal geometry describes a massless particle travelling at light speed. Two of them together can describe a massive particle, and its mass depends only on how far apart their two light-like directions point. When they line up the composite stays massless; the more they disagree, the heavier it is.

To read mass off the frozen point we need to know which symmetries it breaks.

For a non-null $I$ the stabiliser in $\mathfrak{sl}(\CS)$ is $10$-dimensional, and the five generators $A(e_{a}\wedge I)$ span its $5$-dimensional complement. For the frozen point with $\Lambda > 0$ these five are the de Sitter translations.

**Theorem 3 (The five broken generators).** The cosmological scale picks out a direction that breaks the conformal symmetry of spacetime down to de Sitter symmetry. Of the fifteen conformal symmetries ten survive and five are broken. This result identifies the five broken ones exactly: they are the de Sitter translations, the symmetries whose charges make up a composite's momentum.

*Rests on:* mass.de-sitter-scale-frozen-point, mass.imported-flat-model-twistor-chart-infinity, mass.imported-frozen-point-tractor-connection

There are now two readings of mass: the grip on the frozen point and the misalignment of two conformal spinors.

This result joins them exactly: \[ m^{2} = 2\,|B_{\Lambda}|^{2} + \frac{\Lambda}{3}\,C, \] where $B_{\Lambda} = \br{\pi^{1}\pi^{2}} + \tfrac{\Lambda}{6}[\omega^{1}\omega^{2}]$ is the deformed bracket and $C$ depends on how the constituents overlap. At $\Lambda = 0$ the two-spinor formula returns.

**Theorem 4 (The exact join).** The framework reads mass in two ways: from how a composite grips the one built-in cosmological scale, and from how misaligned its two constituents are. This theorem joins the two readings exactly. The mass squared is twice the squared size of a slightly deformed misalignment, plus a tiny correction, proportional to the cosmological constant, that depends on how the constituents overlap. Without a cosmological constant the familiar two-constituent area formula returns.

*Rests on:* correspondence.incidence-relation-chart, mass.chart-form-spin-isomorphism, mass.de-sitter-scale-frozen-point, mass.imported-flat-model-twistor-chart-infinity, mass.mass-symplectic-area-two-twistor-formula

A different route to mass goes through fields rather than particles.

A density $\sigma$ of conformal weight $w$ coupled to the frozen point by $I \cdot D\sigma = 0$ obeys the Klein-Gordon equation, in four dimensions with \[ m^{2} = -\,w(w+3)\,H^{2} \] Every mass is then $\sqrt{\Lambda}$ times a factor fixed by the weight.

**Theorem 5 (The mass-weight dictionary).** The framework has exactly one built-in scale, set by the cosmological constant. This theorem shows that a field coupled to that scale in the natural way behaves as a particle with a definite mass, fixed by a single number the field carries, its conformal weight. In that sense every mass is the cosmological scale multiplied by a number determined by the weight.

*Rests on:* mass.imported-frozen-point-tractor-connection, mass.imported-thomas-operator

The next step maps out which masses this rule allows.

Real weights give $0 \le m \le 3H/2$, exactly for $w$ in $[-3, 0]$. Anything heavier needs the complex weight $w = -\tfrac32 \pm i\nu$, the principal series, and the two regimes match the two standard series of de Sitter representations.

**Theorem 6 (The weight polynomial and the two series).** The framework's mass rule turns one number, the weight, into a mass. This result maps out what the rule allows. Real weights only give masses up to a tiny threshold set by the expansion rate of the universe; anything heavier needs a complex weight, with a fixed real part and an imaginary part that carries the mass. These two regimes match the two standard families of particles in de Sitter space.

*Rests on:* mass.imported-unitary-representations-de-sitter-group

Combining the weight rule with the exact join assigns every two-spinor composite a weight.

For $\Lambda > 0$ a composite heavier than $3H/2$ has \[ w = -\frac32 \pm i\nu, \] the same real part for every such particle. Its mass lies in the imaginary part, which at leading order is $\sqrt{2}\,|B_{\Lambda}|/H$, an enormous number for every known particle.

**Theorem 7 (The weight of a composite).** With a positive cosmological constant, each composite particle can be given a weight: the number that would produce its mass under the framework's mass rule. For anything heavier than a tiny threshold set by the expansion of the universe, that weight is complex. Its real part is the same for every such particle, and its imaginary part is essentially the mass measured in cosmological units, an enormous number for every known particle.

*Rests on:* mass.exact-join, mass.weight-polynomial-two-series

The size of a mass is one question; which field carries the mass term is another.

Under the two-spinor $U(2)$ the mass bracket transforms by the determinant, \[ \br{\pi^{1}\pi^{2}} \mapsto \det(U)\,\br{\pi^{1}\pi^{2}}, \] so it is an $SU(2)$ singlet of hypercharge $+1$. It carries the quantum numbers of $e^{c}$, not of a weak doublet such as the Higgs.

**Theorem 8 (The mass bracket is a charged singlet).** For two conformal spinors, the series' mass is the size of a single complex number, the mass bracket. This result works out how that number changes under the internal symmetries of a system of two conformal spinors. It is unchanged by the $SU(2)$ part and only picks up a phase from the $U(1)$ part, so, with the paper's global form and hypercharge, it carries the charges of the conjugate electron field $e^{c}$, a weak singlet of hypercharge $+1$, rather than those of a weak doublet such as the Higgs.

*Rests on:* mass.mass-symplectic-area-two-twistor-formula, standard-model.global-form-quotient-determined, standard-model.imported-pair-systems-two-chirality-halves

It was natural to hope that tying every mass to the one cosmological scale would explain why particles weigh what they do.

The programme records that hope as refuted: coupling to the frozen point restates the hierarchy as the size of the imaginary weights in Hubble units. The old puzzle returns in a new form.

**Refutation 9 (The mass dictionary, coupling to the frozen point, explains the observed masses).** It was natural to hope that tying every field to the single cosmological scale would explain why particles have the masses they do. It does not: that scale is so small that ordinary particles need enormous weights, so the old puzzle of why matter is so heavy compared with it simply comes back in a new form.

The remaining question is whether anything else in the framework fixes the size of those weights.

Every structural route tried, including the pion-scale $N^{2/3}$ scaling, fails, so the absolute mass hierarchy stays one unexplained number. It is recorded as a clean negative result, at the level of a conjecture rather than a theorem.

**Conjecture 10 (The absolute scale: a clean negative result).** In this framework a particle's mass is coded by a number, its weight, measured against the tiny scale set by the cosmological constant. For ordinary particles that number is enormous, around $10^{38}$ for the electron, and nothing in the framework yet explains why. Several natural attempts were tried and all fail, one of them because it only rediscovers a coincidence first noticed in 1967. What remains is a clear record of which routes do not work.

## Results cited, not shown

**Fact (imported) 11 (The incidence relation is the chart).** Penrose described a spacetime point by a line in a three-dimensional complex projective space, through his incidence relation. This theorem shows that, written out term by term, the coordinates of that line are exactly the null vector by which the completed algebra represents the point, so the incidence relation is the completion's coordinate chart. The quadratic term of the chart is a determinant, the lines meeting a fixed line at infinity are the points at infinity, and the symmetries fixing that line are those of flat spacetime.

*Provenance:* Transport Lab claim correspondence.incidence-relation-chart, version 4 (T09 Thm 4.2).

**Fact (imported) 12 (The chart form of the spin isomorphism).** The conformal symmetries of spacetime can be written either as rotations of a six-dimensional space or as four-by-four matrices acting on the four-component spinors of the conformal algebra. This lemma writes that translation out explicitly in the chart used for spacetime points. Dilations become a diagonal matrix, translations an upper corner block, and special conformal transformations a lower corner block.

*Provenance:* Transport Lab claim mass.chart-form-spin-isomorphism, version 5 (T11 Lem 5.3).

**Fact (imported) 13 (Imported: the flat model, the conformal spinor chart, and the infinity bivector).** This gathers in one place the flat-space set-up that the mass paper builds on. A point of flat spacetime is represented by a light-like vector in a six-dimensional space, and that space can be rebuilt from pairs of four-component spinors of the conformal algebra. In this picture the conformal symmetries act on those spinors as matrices, and the bivector at infinity that records the choice of scale is, when the cosmological constant vanishes, a fixed line in the projective spinor space.

*Provenance:* Transport Lab claim mass.imported-flat-model-twistor-chart-infinity, version 7 (T11 Fact 2.3).

**Fact (imported) 14 (Imported: the frozen point and the tractor connection).** In the series' language, a gravitational field on flat spacetime that describes empty space with a cosmological constant carries one distinguished vector of the six-dimensional conformal model, the frozen point, which stays fixed as the gravitational gauge fields carry it around. Its squared length is a third of the cosmological constant. When the constant is positive, the symmetries fixing the frozen point are those of de Sitter space. These facts are restated from earlier in the series.

*Provenance:* Transport Lab claim mass.imported-frozen-point-tractor-connection, version 6 (T11 Fact 2.1).

**Fact (imported) 15 (Imported: the Thomas operator).** The Thomas operator is a standard tool of conformal geometry that turns a scale-dependent quantity into an object that does not depend on the choice of scale. Applied to a choice of scale itself, it produces the scale tractor, and an Einstein scale gives the frozen point. This classical construction is imported in the sign convention the series uses.

*Provenance:* T. Y. Thomas, On conformal geometry, Proc. Natl. Acad. Sci. USA 12 (1926), 352--359.; T. N. Bailey, M. G. Eastwood, and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.; A. R. Gover, Almost Einstein and Poincar'e-Einstein manifolds in Riemannian signature, J. Geom. Phys. 60 (2010), 182--204..

**Fact (imported) 16 (Imported: the unitary representations of the de Sitter group).** Quantum particles in a universe with a positive cosmological constant are classified by the symmetry group of de Sitter space. For scalar particles this classical result sorts the allowed masses into families: heavy particles above a threshold set by the expansion rate, light ones below it, and the massless case. None of the families used here allows a negative mass squared.

*Provenance:* J. Dixmier, Repr'esentations int'egrables du groupe de De Sitter, Bull. Soc. Math. France 89 (1961), 9--41., \S\S3--4; A. Higuchi, Symmetric tensor spherical harmonics on the $N$-sphere and their application to the de Sitter group $SO(N,1)$, J. Math. Phys. 28 (1987), 1553--1566..

**Fact (imported) 17 (The global form: the quotient determined).** The symmetries of the smallest composite that can carry mass have the algebra of the Standard Model forces. This result pins down the group itself, not only its algebra: it is the most economical of the possible global forms, the one in which a six-element subgroup is divided out. That choice restricts which combinations of colour, weak charge and hypercharge any particle can carry, and it is the form that grand unification requires. A free particle with no colour and a fractional electric charge would contradict the identification.

*Provenance:* Transport Lab claim standard-model.global-form-quotient-determined, version 3 (T12 Thm 4.2).

**Fact (imported) 18 (Imported: the pair systems and the two chirality halves).** This restates earlier results of the series for the Standard Model paper. The completed algebra acts on an eight-dimensional space that splits into two halves of opposite chirality, four dimensions each (the chirality of the completed algebra, not the left and right handedness of spacetime spinors at a point). Every nonzero spinor in the first half is the empty state of its own three fermionic ladder pairs, and all other states are reached from it by those operators.

*Provenance:* Transport Lab claim standard-model.imported-pair-systems-two-chirality-halves, version 5 (T12 Fact 2.2).

**Prediction 19 (No fractionally charged colour singlet).** The series derives not only the Standard Model's symmetries but the precise way they fit together, and that restricts the charges particles can have. In particular, a particle that feels no strong force must have a whole-number electric charge. Finding even one such particle with a fractional charge would refute this part of the framework; searches so far have found none.

The trail has shown two readings of mass, the grip on the frozen point and the misalignment of two conformal spinors, joined exactly, with the conformal weight as a third language for the same quantity.

No postulate is needed on this stretch, and the charge assignment of the mass bracket rests on the series' derived global form and hypercharge. What the mechanism does not do is explain the observed masses: it restates the hierarchy as the size of the weights, which remains open.
