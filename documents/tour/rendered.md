# A tour of the Transport Papers

**Abstract.** A null vector, nonzero but with square zero, can never be divided by, even inside a larger algebra. With both space and time directions and at least three dimensions, no choice of partial inverses respects the symmetries, however the algebra is enlarged.

The fix is a larger space with one new positive and one new negative direction, $\Cl(p,q) \to \Cl(p{+}1, q{+}1)$. This becomes a recipe sorting every failure of division into three kinds, each with its own fix. Each step up the resulting tower adds exactly one fermionic mode.

At the centre of a non-rotating black hole the obstruction is the kind this repair supplies. Einstein's vacuum equations become one null tractor staying constant. The boundary modes carry a thermal state at the Hawking temperature, the only quasi-free state thermal for the boost clock.

On the matter side, the smallest massive twistor composite carries exactly the symmetry of the strong, weak and hypercharge forces. With an assumed hierarchical second correction, the neutrino masses add up to about 0.059 eV. Given stated symmetry assumptions, a mirror world copies the Standard Model.

This tour follows one idea from pure algebra all the way to particles, neutrinos and dark matter. It starts with a failure of division, because every later step is a response to that failure.

It then shows how enlarging the space repairs the failure, and applies the repair to geometry and gravity, then to black holes and heat, and last to matter. The assumptions that some results rest on are gathered first, under their own heading, so that what is proved stays separate from what is supposed.

## What we assume

**Postulate 1 (P1: the single frozen point).** This assumption says the origin of the universe happened once, in one way, for everything. Every hidden sector feels the same gravity, and every sector that can have a handedness received the same one. It is assumed, not derived.

**Postulate 2 (P2: indifference, scoped to sector labels).** This assumption says the birth of the universe treats alike only things that are genuinely alike. The only hidden sectors that count as alike are pairs related by a reflection, so only those pairs are forced to match. Which member of the matching pair we live in is simply a matter of where we stand. What must match are the sector's fixed labels, such as its stored charge, not how hot it is: the assumption leaves the temperature of the mirror sector open, and it takes the number of modes the birth deposits to be finite.

**Postulate 3 (H: the second stage is hierarchical).** This is an assumption, not a result: the lightest neutrino gets almost no mass, less than a hundredth of the next one. Other particle families show steep mass hierarchies of this kind, which makes the assumption plausible without proving it. With it, the framework's total neutrino mass becomes a sharp number rather than a lower limit.

**Postulate 4 (M: the framework realises the Majorana term, at a scale $M \gg v$).** Neutrinos could carry a special kind of mass that only electrically neutral particles can have. Nothing forbids it, but nothing in the framework yet shows that it forms or how big it is. The paper assumes that it does, at a very high scale, and leaves the explanation for later work.

**Postulate 5 (Tameness).** This is the standing assumption on how a geometry is allowed to degenerate. The places where it degenerates must form a smooth closed wall, exactly one direction must lose its length at each point of the wall, and these directions must vary smoothly along it. In addition, the length must vanish at a linear rate as the wall is reached, not to higher order.

## Zero divisors and obstructions

The series starts from a simple question: what happens when you try to divide by something that is not zero but whose square is zero?

In a space of mixed signature, $pq \neq 0$, like the spacetime of relativity, such vectors exist, and they form a cone much like a light cone.

The first result shows how firmly these vectors resist division.

A null $v \neq 0$ has no inverse on either side, in $\Cl(p,q)$ or in any larger algebra containing it.

**Theorem 6 (A null vector has no inverse).** A null vector is a nonzero direction whose square is zero. Such an element can never be divided by: if it had an inverse on either side, multiplying through would force the vector itself to be zero. The argument uses only the fact that its square is zero, so it still applies in any larger algebra of the same kind that contains the original one.

*Rests on:* std-algebra.vector-squares

With exact inverses ruled out, one might settle for partial ones.

A partial inverse $\sigma(v)$ satisfies \[ v\,\sigma(v)\,v = v \] but in mixed signature with $n \geq 3$ no choice of one for each null $v$ is equivariant, even under $\Spin^0(p,q)$, in any extension.

**Theorem 7 (No-go at the level of elements).** A light-like direction has no inverse, but it has many partial inverses. This theorem shows that there is no way to choose one for every light-like direction that respects the symmetries of the geometry, in any space with both space and time directions and at least three dimensions. Enlarging the algebra by any number of new directions does not help.

*Rests on:* transport.splitting-along-hyperbolic-plane, primer.commutation-rule, std-algebra.witt-decomposition

## Clifford algebra structure

A Clifford algebra is built from a space of directions together with a rule for multiplying them. Before trying to repair these algebras, it helps to know what they really are.

The classical answer is a short and complete list.

Each real Clifford algebra is a matrix algebra over $\R$, $\C$ or $\HH$, or a sum of two, according to the residue \[ d \equiv p - q \pmod 8 \] and it is simple except when $p - q \equiv 1 \pmod 4$.

**Theorem 8 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers (matrices) whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which of these appears depends only on p minus q, in a pattern that repeats every eight steps. Usually the algebra is a single indivisible block; it splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Rests on:* primer.classification-real-clifford-algebras

## The completion

Since division cannot be rescued inside the algebra, the series moves outside it, into a larger space. The question for this section is how much larger that space must be, and what to do once one is there.

The first answer concerns the reciprocal of a single vector.

The larger space needs one new direction of each sign, \[ \Cl(p,q) \;\longrightarrow\; \Cl(p{+}1, q{+}1) \] and this hyperbolic plane is enough and unique up to isometry.

**Theorem 9 (Minimality).** To make the reciprocal work everywhere, the series represents each point as a light-like direction in a larger space. This result asks how much larger that space has to be. The added part must contain at least one direction of positive square and one of negative square, so adding only space-like or only time-like directions never works, while one such pair is enough and is essentially unique.

*Rests on:* std-algebra.witt-decomposition, std-algebra.sylvester-inertia

A similar count applies when the geometry itself is degenerate.

A radical of dimension $r$ needs $r$ new partners, so $\Cl(p,q,r)$ embeds minimally in $\Cl(p{+}r, q{+}r)$.

**Theorem 10 (Minimal nondegenerate completion).** A geometric algebra built on a degenerate metric has directions that pair to zero with everything, and division fails along them. This result says how to enlarge the space so that the metric becomes nondegenerate: each degenerate direction needs exactly one new partner direction, and the enlarged metric gains one positive and one negative direction for each degenerate one. The smallest such enlargement is unique up to a symmetry that leaves the original space untouched. Minimality here is among enlargements of the underlying space, not among all algebras.

*Rests on:* conformal.blade-basis-persists-under-degeneracy, conformal.witt-extension-theorem, std-algebra.functoriality

These pieces now fit together into one working procedure.

The theorems distil into a six-step procedure, and every step names the theorem that licenses it.

**Theorem 11 (The transport algorithm).** This is the series' recipe for what to do when division fails. Find where it fails, decide which of three kinds of failure it is, apply the matching fix (add a pair of dimensions, add one dimension, or do nothing), do the calculation in the enlarged setting, and bring the answer back, noting where it cannot come back. The recipe can be repeated, but its bookkeeping settles after at most one change.

*Rests on:* transport.classification-real-clifford-algebras, transport.cohomological-form-no-go, transport.descent-read-out-map, transport.door-one-way, transport.exhaustiveness-every-zero-divisor-annihilated-idempotent, transport.existence-classification-type-c, transport.existence-locus-type-n, transport.fusion-occurs-most-once, transport.minimality, transport.no-fourth-rule, transport.no-go-level-elements, transport.no-transport-terminates, transport.noinverse, transport.one-generator-minimal-minimal-completions-classified, transport.pinching-kernel, transport.representation-independent-minimality-completion, transport.rule-1-morita-trivial, transport.rule-2-ideal-fusion-sharp-form, transport.swap-rescale-normal-form, transport.totality, transport.type-p-self-repairing

## The tower and quantum capacity

Repeating the basic repair builds a tower of ever larger spaces.

Each step adds a null pair $v_i, w_i$, and these obey exactly the rules of fermionic modes, $v_i w_j + w_j v_i = \delta_{ij}$.

The next result counts how much of this quantum structure each floor can hold.

The number of modes realisable by vectors is the Witt index, \[ \min(p,q) \] and along the tower it is $\min(p,q) + k$, one more per rung.

**Theorem 12 (Witt index is quantum capacity).** Inside a Clifford algebra one can ask how many independent fermionic modes can be built directly from vectors. The answer is a classical number attached to the geometry, the Witt index: the largest number of independent zero-length directions that are all orthogonal to one another. For a space with p positive and q negative directions it is the smaller of p and q. Each step up the tower raises this number by exactly one, so each step adds precisely one mode of capacity and no more.

*Rests on:* tower.ladder-pairs-satisfy-car-vectors, std-algebra.vector-squares, std-algebra.witt-decomposition

## Degenerate metrics and walls

Real geometries can degenerate in some places and not in others, so the repair has to be made locally, along a wall.

The standing tameness assumption fixes what is allowed: a smooth closed wall, exactly one direction losing its length at each point, and that length vanishing at a linear rate.

With that assumption in place, the repair can be carried right up to the wall.

On the physical side the completed form is nondegenerate of signature $(p{+}1, q{+}1)$ at every point, including the wall, so every fibre is \[ \Cl(2,4) \cong \Mat_4(\HH) \] in the physical case.

**Theorem 13 (One-sided completion).** Assume a geometry degenerates along a wall in the tame way, with at least one positive direction on the physical side and with the dying direction's line consistently orientable along the wall. Then it can be repaired on that side by adding two extra dimensions and coupling them to the direction that is dying. This result shows that the coupling can be chosen so that the enlarged geometry is non-degenerate, with the same signature everywhere on the physical side, the wall itself included. The resulting family of algebras is then uniform: in the physical case every member is the algebra of four-by-four quaternion matrices.

*Rests on:* sheaf.determinant-identity-blow-up-expansion, sheaf.local-freeness-constant-rank, sheaf.wall-gram, sheaf.tameness

## The singularity

The centre of a black hole is the first physical place where the repair is put to work.

Approaching it, the gravitational field grows without bound, but once that growth is divided out the field settles to a limit that is degenerate.

The question is which kind of obstruction this degeneration turns out to be.

It is type N, a null direction without a partner, and type C cannot occur, because \[ p - q = -2 \equiv 6 \pmod 8 \] makes $\Cl(1,3) \cong \Mat_2(\HH)$ simple.

**Theorem 14 (Type N, and only type N).** At the centre of a non-rotating black hole one direction of the geometry collapses, and this result identifies which kind of algebraic obstruction that is in the series' classification. It is the kind caused by a direction with no partner to pair with. The other substantive kind, which would need the algebra to split into independent pieces, cannot occur for the algebra of spacetime, and a third kind is present but harmless. So the repair that applies is the one that supplies the missing partner by enlarging the algebra.

*Rests on:* sheaf.localised-transport, sheaf.one-sided-completion, sheaf.one-sided-completion-singularity, sheaf.schwarzschild-degeneration-boundary-tame, singularity.degeneration-exactly, tower.rigidity-clock-frozen, transport.existence-classification-type-c, transport.existence-locus-type-n, transport.type-p-self-repairing, primer.classification-real-clifford-algebras, std-algebra.sta-matrix

## Einstein's equations in the completion

To say anything about gravity itself, the series needs Einstein's equations in a form that lives naturally in the enlarged space.

The next result supplies such a form.

In Gauge Theory Gravity on flat spacetime, the vacuum field equations hold exactly when the null scale tractor $I_g = \nInf$ is parallel for the $\Cl(2,4)$ gauge field.

**Theorem 15 (Covariant form of the vacuum equations).** In the interior region, Einstein's equations for empty space can be recast as a single condition on the gravitational fields: a particular marker in the six-dimensional conformal extension of spacetime, attached to the physical scale, must stay constant as it is carried from point to point by a gauge field built from gravity. This result proves that the two formulations are exactly equivalent, and that the marker is a null (lightlike) object. It also notes that merely having some constant marker of this kind is a weaker condition that does not by itself give the field equations.

*Rests on:* interior.imported-equivalence-einstein-equations, interior.imported-tractor-connection, interior.metric-parallelism-trace-schouten-condition

## Descent, parity and states

After working upstairs one has to come back down, and any return journey must lose something. This section says what is lost and what the loss means.

The first result identifies the way down with a familiar operation.

Descent is the average over fermion parity, \[ E(x) \;=\; \tfrac12\bigl(x + \alpha(x)\bigr) \] whose kernel is exactly the adjoined ladder sector.

**Theorem 16 (The descent is the parity average).** The descent, which keeps a mode's occupation data and discards its coherences, is the same thing as averaging over fermion parity: take an observable and its parity-flipped version and average the two. This makes it the only consistent projection onto the parity-even observables, and it leaves every parity-even state unchanged.

*Rests on:* singularity.descent-what-it-erases

That leaves the question of where the missing partner of a mixed state comes from.

In the state's own representation the partner is the commutant, and for a Gibbs state the cyclic vector is the thermofield double.

**Theorem 17 (Purity is an output: the partner is the commutant).** Starting from a single quantum mode in a mixed state, there is a standard construction that builds a larger system in which that state is one half of a pure entangled state. This result shows that the partner needed for the pure state is not an extra ingredient: it emerges automatically as the mirror copy of the mode's own algebra, and the construction is unique up to changes made on the partner side alone. For a thermal state the resulting pure state is the familiar thermofield double.

*Rests on:* singularity.modular-theory-matrix-factor-proved-outright

## Temperature and Hawking radiation

The series next asks whether the modes it finds at the black-hole boundary can be hot, in the sense that Hawking described.

The thermal case of that construction now meets the black hole directly.

At inverse temperature \[ \beta = 1/\TH = 2\pi/\kappa \] the boundary modes have a state thermal for the boost clock, and within the quasi-free class it is unique, its two-point data forced.

**Theorem 18 (The I-state).** The boundary modes in this black-hole setting can be placed in a thermal state at the Hawking temperature, each mode filled according to the Fermi-Dirac rule. This result shows that this state exists and is thermal in the precise algebraic sense, both on every finite set of modes and on the whole system. It also shows that among the simple Gaussian (quasi-free) states it is the only one that is thermal for the geometry's boost time evolution, which turns the phase of each mode at its own frequency, so its occupation numbers are derived rather than chosen.

*Rests on:* hawking.gibbs-states-are-kms-conversely-finite, hawking.imported-kms-passes-inductive-limits, hawking.imported-quasi-free-states-car-algebra

## Dark energy and the frozen point

The cosmological constant enters through the frozen point, a fixed direction in an enlarged conformal space whose length the constant sets. One of the earlier results used here rests on an assumed principle rather than a proof.

From heat the tour turns to gravity on the largest scale.

Where $\Lambda \neq 0$, the frozen point supplies the Stelle-West vector, so gravity's action makes sense where the metric degenerates.

**Theorem 19 (The frozen point makes the Stelle-West vector).** The frozen point is a fixed direction in the larger conformal space whose length encodes the cosmological constant. On the region where Einstein's equations hold with a nonzero cosmological constant, this result shows that the frozen point, together with one canonical geometric object, produces exactly the extra vector that a known reformulation of gravity, due to MacDowell and Mansouri and to Stelle and West, requires. Gravity's action can then be written as the square of the curvature as seen from the point at infinity, with no inverse metric anywhere, so it is defined wherever the connection stays regular. At the black hole's wall, where the connection is singular, its value diverges but its field equations still reach the wall; and the curvature-squared form itself exists only while the cosmological constant is nonzero.

*Rests on:* dark-energy.imported-frozen-point-geometry, dark-energy.imported-macdowell-mansouri-theorem-stelle-west, dark-energy.imported-walls-sphere-theorem, dark-energy.stelle-west-vector-frozen-point

## The origin of mass

The tour now turns from gravity to matter, using twistors, in which a single twistor describes a massless particle travelling at light speed.

The first question about matter is where its mass comes from.

A single conformal spinor carries the null momentum \[ p_{AA'} = \pi_{A}\bar\pi_{A'} \] and is massless, so mass first appears for a system of two.

**Theorem 20 (Mass as symplectic area: the two-spinor formula).** A single spinor of the conformal geometry describes a massless particle travelling at light speed. Two of them together can describe a massive particle, and its mass depends only on how far apart their two light-like directions point. When they line up the composite stays massless; the more they disagree, the heavier it is.

## The Standard Model

Next the tour asks which forces such a massive composite would feel.

Looking inside the smallest massive composite answers that question.

Two conformal spinors of three pairs each have automorphisms $(U(2) \times U(3))/U(1)$, with Lie algebra \[ \su(2) \oplus \su(3) \oplus \uu(1) \] the Standard Model's exactly.

**Theorem 21 (The gauge algebra of the minimal massive composite).** A composite of basic spinor states of the conformal algebra has a two-level internal structure: which spinor state, and which of its three internal pairs. The rotations that respect both levels form a symmetry algebra. For the smallest composite that can have mass, two spinor states of three pairs each, that algebra is exactly the one behind the strong, weak and hypercharge forces; for three spinor states it is too large.

*Rests on:* mass.mass-symplectic-area-two-twistor-formula

## Families of quarks and leptons

The next question is why matter might repeat itself in families.

Here Hypothesis (S), an assumption about how the slots of a composite behave, is needed, and several of the framework's particle-physics results hold only if it does. In particular, everything said about charged leptons depends on it.

Allowing a composite more than two twistors leads to a simple count of choices.

The faces, three of them under the three-spinor bound, carry identical content, because the permutations $S_{3}$ of the slots carry each face's copy onto every other.

**Theorem 22 (Three identical families, mixing by shared slots).** If the largest allowed composite is made of three conformal spinors and a massive particle uses two of them, there are three ways to choose the pair. Each choice carries an exact copy of the same set of particles, because relabelling the spinors maps one copy onto another; the copies include the lepton doublet if the slots behave like the pairs (Hypothesis (S)). Any two choices share exactly one spinor, which hints at why quark families mix the way they do, though that hint and the matching of choices to real families are not proved.

*Rests on:* families.imported-one-derived-generation-hypothesis-s, families.imported-face-valued-bracket-quantum-numbers, standard-model.hyp-s-slot-statistics

## Neutrino masses

Neutrinos are where the framework comes closest to numbers that experiments can check.

The account assumes that neutrinos carry a Majorana mass at a very high scale, which nothing in the framework yet shows forming. The family picture it builds on is itself still a conjecture.

Treating the families even-handedly has a sharp consequence for neutrino masses.

The Dirac mass matrix is democratic, $\mD = d\,\J$, with the single eigenvalue $m_{D} = 3d$, so the seesaw gives the normal ordering.

**Theorem 23 (The rank-one seesaw: ordering, sum, and the double-beta values).** Assuming the framework supplies the heavy neutrino's Majorana mass at a scale far above the electroweak one (Premise (M)), and because the framework's neutrino couplings treat the three families identically at first approximation (a structural-level reading), only one light neutrino gets a mass, through the seesaw. Provided the corrections that break that symmetry are small, that fixes the mass ordering as normal; if the second stage of those corrections is also hierarchical (Premise (H)), the total mass sits at the smallest value oscillation experiments allow, about 0.059 eV, and otherwise that value is only a lower bound. Under the same premises neutrinoless double-beta decay occurs, at rates too small for the next generation of experiments to see: a conditional absence.

*Rests on:* neutrino.imported-indifference-faces-democratic-alignment-rank, neutrino.invariant-symmetric-matrices, neutrino.seesaw-what-gauge-invariance-proves-what, neutrino.h-second-stage-hierarchical, neutrino.m-framework-realises-majorana-term-scale

## Dark matter and the dark towers

The account of matter ends with matter we cannot see. The answer rests on postulates, not proofs, about how the origin of the universe treats its hidden sectors.

Swapping the roles of time and space gives a second world to set beside our own.

Every input of the Standard Model chain is invariant under the reversal \[ (p,q) \mapsto (q,p) \] which carries $(1,3)$ to the mirror's $(3,1)$, so the mirror has the same gauge algebra and the same generation.

**Theorem 24 (The mirror tower is a copy of this one).** Swapping which directions count as time and which as space turns our world into a mirror world, and this result shows that every ingredient used to derive our particle physics survives the swap. So the mirror world has its own copy of the Standard Model as the series derives it (under Hypothesis (S)), with mirror photons and mirror neutrinos. If the two worlds share one cutoff scale (a common ceiling), then under the framework's premises of a single frozen point (P1) and indifference (P2), which fix a common coupling there and an equal matter excess, it also has the same particle masses and the same matter excess, so its matter equals our ordinary matter to within half a percent, the gap coming from the two worlds' nuclear histories. A later note (T14c) shows that the same indifference principle, applied as widely, would also make the mirror world as hot as ours, which observations rule out, so the cold mirror world the series relies on is an unstated exception to that principle.

*Rests on:* dark-matter.imported-inputs-standard-model-chain, dark-matter.type-residue-what-each-tower-can, dark-matter.p1-single-frozen-point, dark-matter.p2-indifference

## One relation, read twice

The tour closes by stepping back to the single rule behind everything.

That rule, $\{e_{a}, e_{b}\} = 2g_{ab}\mathbf{1}$, can be read as geometry or as the rule obeyed by fermions, though only at the level of structure.

A last result counts the quantum structure in two ways.

The real and complex capacities are \[ r_{\R}(p,q) = \min(p,q), \qquad r_{\C}(p,q) = \lfloor d/2 \rfloor \] and for spacetime $(1,3)$ they are $1$ and $2$.

**Theorem 25 (The two capacities, and three consequences).** Reading spacetime geometry as a system of fermion modes, there are two ways to count the modes: using only real directions, or allowing complex ones. The two counts usually differ, and for ordinary spacetime they give one and two. Each step up the tower of extended spaces adds exactly one mode to both counts, and the complex count of the extended six-dimensional space is three.

*Rests on:* one-relation.imported-witts-extension-theorem, one-relation.two-presentations, tower.witt-index-quantum-capacity, std-algebra.vector-squares, std-algebra.witt-decomposition

## Results cited, not shown

**Fact (imported) 26 (The blade basis persists under degeneracy).** A Clifford algebra is built from a space of directions together with a rule for multiplying them. This fact says that the products of distinct basis directions always form a basis for the whole algebra, so an algebra built on m directions has size two to the power m. That stays true even when the multiplication rule is degenerate, with some directions of zero length against every direction.

*Provenance:* Transport Lab claim conformal.blade-basis-persists-under-degeneracy, version 4 (T02 Fact 2.1).

**Fact (imported) 27 (The Witt extension theorem).** Suppose two spaces carry equivalent nondegenerate notions of length and angle. Then any length-preserving match between a part of one and a part of the other can be extended to a length-preserving match of the whole spaces. This works even when the parts themselves are degenerate. It is a standard theorem about quadratic forms.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, Thm.~4.7.

**Fact (imported) 28 (Imported: the frozen point and its geometry).** This fact collects earlier results about the frozen point, a fixed direction in the six-dimensional conformal model attached to flat spacetime. Einstein's vacuum equations amount to this direction staying constant as the gravitational gauge fields carry it from place to place, and its length is set by the cosmological constant. The symmetries that leave it alone form the de Sitter group, or the anti-de Sitter group when the cosmological constant is negative. The fact also writes down the gauge field that says what constant means here.

*Provenance:* Transport Lab claim dark-energy.imported-frozen-point-geometry, version 6 (T10 Fact 2.1).

**Fact (imported) 29 (Imported: the MacDowell-Mansouri theorem, Stelle-West form).** MacDowell and Mansouri, and later Stelle and West, showed that gravity with a cosmological constant can be written as a theory of a larger symmetry group, the de Sitter group, broken by a vector of fixed length. On flat spacetime this means adding one extra direction to the algebra in which the gravitational fields take their values. The action is then the square of a field strength, and it splits into a topological piece, the usual Einstein term and the cosmological term. Its equations are the Einstein equations with that cosmological constant.

*Provenance:* S. W. MacDowell and F. Mansouri, Unified geometric theory of gravity and supergravity, Phys. Rev. Lett. 38 (1977), 739--742.; K. S. Stelle and P. C. West, Spontaneously broken de Sitter symmetry and the gravitational holonomy group, Phys. Rev. D 21 (1980), 1466--1488.; D. K. Wise, MacDowell-Mansouri gravity and Cartan geometry, Class. Quantum Grav. 27 (2010), 155010..

**Fact (imported) 30 (Imported: walls, and the sphere theorem).** Where geometry degenerates in the mildest, tame way, along a wall where one direction stops being measurable, the algebraic description of geometry does not break but carries on through the wall. The metric blows up there in a controlled way, and the completion adds exactly one partner to the dying direction. A further imported result, which rests on an assumed principle (the Indifference principle) rather than a proof, says that the sphere of directions around the wall is built from pairings of the wall's boundary modes.

*Provenance:* Transport Lab claim dark-energy.imported-walls-sphere-theorem, version 6 (T10 Fact 2.4).

**Fact (imported) 31 (The Stelle-West vector of the frozen point).** Starting from the frozen point and one canonical fixed direction of the six-dimensional conformal model, this lemma builds a vector perpendicular to the frozen point whose length is set by the cosmological constant. Its rate of change is exactly the frame that links the conformal model to the physical directions of the gravitational field on flat spacetime. It is the vector that the Stelle-West form of gravity needs, and the lemma records its basic algebra.

*Provenance:* Transport Lab claim dark-energy.stelle-west-vector-frozen-point, version 5 (T10 Lem 2.5).

**Fact (imported) 32 (Imported: the inputs of the Standard-Model chain).** The Standard-Model results of the series come from a chain of derivations. This entry lists every ingredient that chain uses, from the six-dimensional conformal geometry and its spinors to the mass formula, a counting rule for hypercharge, one structural hypothesis about the slots of the composite's spinor states (Hypothesis (S)) and a few textbook results. The point is that nothing else goes in, so later work can ask which ingredients survive in other settings. That the list is complete is a reading, carried as an assumption.

*Provenance:* Transport Lab claim dark-matter.imported-inputs-standard-model-chain, version 6 (T14 Fact 4.2).

**Fact (imported) 33 (Type by residue, and what each tower can carry intrinsically).** Each tower's basic algebra decides what kind of numbers its matter states naturally use: real numbers, complex numbers or quaternions. That choice depends only on the tower's label, and it fixes which continuous symmetries a tower carries before any further structure is added. For the representatives the paper uses, and in its labelling convention (the opposite convention swaps the two members of each mirror pair), the mirror tower comes out with real spinors and no built-in continuous charge, two of the odd towers with exactly one built-in charge each, and our own world with quaternionic spinors.

*Provenance:* Transport Lab claim dark-matter.type-residue-what-each-tower-can, version 5 (T14 Thm 3.4).

**Fact (imported) 34 (Imported: the face-valued bracket and its quantum numbers).** In this framework a particle with mass is built from two conformal spinors, and its mass in flat space is carried by one complex number, the bracket. This result records how that number behaves under the framework's internal symmetries: it has the charges of $e^{c}$, the conjugate of the right-handed electron, with hypercharge $+1$, not those of the Higgs doublet of the Standard Model. Whether it nonetheless plays a role like the Higgs field is left open, and that reading is held at observation level only.

*Provenance:* Transport Lab claim families.imported-face-valued-bracket-quantum-numbers, version 5 (T13 Fact 2.1).

**Fact (imported) 35 (Imported: one derived generation, and Hypothesis (S)).** The families paper imports what the series has derived about one generation of matter. The quark doublet and the charges of single free spinor states come out with no extra assumption; the lepton doublet appears only if one adopts a stated hypothesis about how the slots those states occupy behave. With that hypothesis, and given the generation's particle content listed with one handedness, at most one extra neutral singlet and the quark doublet's charge as the unit, requiring the theory to be free of quantum anomalies fixes all the hypercharges of the generation, up to which of the two antiquark singlets takes which value. The hypothesis is not proved, and everything that paper says about charged leptons depends on it.

*Provenance:* Transport Lab claim families.imported-one-derived-generation-hypothesis-s, version 6 (T13 Fact 2.3).

**Fact (imported) 36 (Gibbs states are KMS, and conversely, in finite dimensions).** In a finite quantum system, the thermal (Gibbs) state at a given temperature satisfies a standard algebraic test of thermal equilibrium, the KMS condition. This result also proves the converse: in finite dimensions the Gibbs state is the only state that passes the test, even when some energy levels coincide.

*Provenance:* Transport Lab claim hawking.gibbs-states-are-kms-conversely-finite, version 2 (T07 Lem 3.1).

**Fact (imported) 37 (Imported: KMS passes to inductive limits).** Thermal equilibrium, in its precise algebraic form, can be checked piece by piece. If a large system is the limit of an increasing chain of smaller subsystems, each preserved by the time evolution, and a state is in equilibrium on every one of them, then it is in equilibrium on the whole system. This is a known result taken from the literature.

*Provenance:* O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., Prop.~5.3.25.

**Fact (imported) 38 (Imported: quasi-free states of the CAR algebra).** For fermions there is a class of especially simple states, called quasi-free, in which every correlation is fixed by the two-point correlations alone. This imported result says that each admissible choice of occupation data gives exactly one such state that is invariant under phase rotations, and that a quasi-free state is invariant in this way exactly when a certain pairing term vanishes. On finitely many modes with no mixing these states simply occupy each mode independently.

*Provenance:* H. Araki, On quasifree states of CAR and Bogoliubov automorphisms, Publ. RIMS Kyoto Univ. 6 (1971), 385--442.; O. Bratteli and D. W. Robinson, Operator Algebras and Quantum Statistical Mechanics 2, 2nd ed., Springer, Berlin (1997)., \S 5.2.

**Fact (imported) 39 (Imported: equivalence with the Einstein equations).** Gauge theory gravity rewrites general relativity in the language of geometric algebra. This imported result says that, wherever its basic field can be inverted, its equations say exactly the same as Einstein's equations for the corresponding metric. In empty space this means the metric has vanishing Ricci curvature.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 40 (Imported: the tractor connection).** Gravity here is a pair of fields on flat spacetime, and what it determines, once lengths are allowed to be rescaled freely, is a conformal geometry. To it one can attach a larger bundle called the tractor bundle, whose fibres are the six-dimensional vectors of the series' conformal model, with a natural way of differentiating its sections. This imported result gives that derivative explicitly once a particular scale is chosen, in terms of the Schouten tensor, a rearranged form of the field strength. The derivative depends only on the conformal geometry and respects the bundle's own metric.

*Provenance:* T. N. Bailey, M. G. Eastwood and A. R. Gover, Thomas's structure bundle for conformal, projective and related structures, Rocky Mountain J. Math. 24 (1994), 1191--1217.; S. N. Curry and A. R. Gover, An introduction to conformal geometry and tractor calculus, with a view towards analysis on manifolds, in Asymptotic Analysis in General Relativity, London Mathematical Society Lecture Note Series 443, Cambridge University Press (2018), 86--170., \S 5.

**Fact (imported) 41 (Metric parallelism, and the trace of the Schouten condition).** This lemma records two elementary facts behind the tractor form of the gravitational field equations. First, the natural derivative on the tractor bundle, which on flat spacetime is a field of rotations of the six-dimensional conformal model, respects that model's own notion of length. Second, if the Schouten tensor, a rearranged form of the gravitational field strength, is a multiple of the metric then the field is Einstein, and the Schouten tensor vanishes exactly when the Ricci curvature does.

*Provenance:* Transport Lab claim interior.metric-parallelism-trace-schouten-condition, version 6 (T06 Lem 4.2).

**Fact (imported) 42 (Imported: indifference, the faces, the democratic alignment, and the rank-one texture).** The framework adopts a rule, as a premise rather than a theorem, that it may not build in distinctions that nothing explains. Applied to three families pictured as three equivalent pairs inside a three-part object, the rule says the vacuum must at first treat all three alike. If the leading masses come from squaring that evenly weighted direction, one family is heavy and two are massless at first order, with smaller effects later separating the light ones. Each step holds only at the level the earlier work stated, and the family picture itself is still a conjecture.

*Provenance:* Transport Lab claim neutrino.imported-indifference-faces-democratic-alignment-rank, version 6 (T15 Fact 2.3).

**Fact (imported) 43 ($S_{3}$-invariant symmetric matrices).** If a three-by-three table of numbers must look the same however the three families are relabelled, it can contain only two independent numbers. That fixes its behaviour completely: one special direction in which all three families are equal, and a plane of directions all treated alike. Inverting such a table is then simple.

*Provenance:* Transport Lab claim neutrino.invariant-symmetric-matrices, version 2 (T15 Lem 4.3).

**Fact (imported) 44 (The seesaw: what gauge invariance proves, and what is assumed).** The paper first rules out one idea: the cosmological constant's tiny effect on the framework's mass formula is far too weak to give neutrinos their mass. It then recalls that gauge symmetry allows exactly one fermion mass that needs no Higgs field, a Majorana mass for the right-handed neutrino. Assuming, as Premise (M), that the framework realises that mass and makes it large, the familiar seesaw follows at leading order: the light neutrino mass is the square of an ordinary mass divided by the huge one.

*Provenance:* Transport Lab claim neutrino.seesaw-what-gauge-invariance-proves-what, version 4 (T15 Prop 4.1).

**Fact (imported) 45 (Imported: Witt's extension theorem).** Witt's theorem concerns a space with a fixed rule for measuring lengths. It says that any length-preserving match between two pieces of the space extends to a length-preserving symmetry of the whole space, so pieces that look alike from the inside are also indistinguishable from the outside. It is a classical result from the 1930s.

*Provenance:* E. Witt, Theorie der quadratischen Formen in beliebigen K"orpern, J. Reine Angew. Math. 176 (1937) 31--44.; T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, \S4.

**Fact (imported) 46 (The two presentations).** The basic rule of a Clifford algebra can be written in two ways. In one it describes distances and angles, the language of geometry and gravity; in the other it is exactly the rule obeyed by fermions, the language of quantum theory. The paper takes this to mean that geometry and quantum structure are two views of one object, though only at the level of structure, not of how things evolve.

*Provenance:* Transport Lab claim one-relation.two-presentations, version 4 (T16 Prop 3.1).

**Fact (imported) 47 (Classification of the real Clifford algebras).** Clifford algebras built from a space with p positive and q negative directions turn out to be familiar objects in disguise: square tables of numbers whose entries are real numbers, complex numbers or quaternions, or a pair of such tables side by side. Which one appears depends only on p minus q, in a pattern that repeats every eight steps. The algebra splits into two identical pieces exactly when p minus q leaves remainder 1 on division by four.

*Provenance:* Transport Lab claim primer.classification-real-clifford-algebras, version 3 (T00 Thm 9.3).

**Fact (imported) 48 (The commutation rule).** In a Clifford algebra two perpendicular directions anticommute: swapping their order flips the sign. This rule extends that to anything built from directions perpendicular to a given one. Moving the given direction past such an element flips the sign of its odd part and leaves its even part alone.

*Provenance:* Transport Lab claim primer.commutation-rule, version 2 (T00 Lem 9.1).

**Fact (imported) 49 (The determinant identity, and the blow-up expansion).** The enlarged geometry built around a degenerating wall has a determinant that factorises exactly into the original determinant times a simple correction factor. The correction involves a quantity that blows up as the wall is approached, like one over the vanishing eigenvalue, with opposite signs on the two sides. Knowing exactly how it blows up is what lets one control where the enlarged geometry stays non-degenerate.

*Provenance:* Transport Lab claim sheaf.determinant-identity-blow-up-expansion, version 3 (T04 Lem 4.3).

**Fact (imported) 50 (Local freeness at constant rank).** Gluing together the Clifford algebras at all points of a space gives a smoothly varying family of algebras. This result shows that the family has the same size everywhere, even where the geometry degenerates. So degeneration cannot be detected by counting dimensions; it has to show up in the structure of the algebra instead.

*Provenance:* Transport Lab claim sheaf.local-freeness-constant-rank, version 2 (T04 Prop 2.8).

**Fact (imported) 51 (Localised transport).** When the degenerate algebra is placed inside the larger completed algebra, it sits there unchanged. What changes is its surroundings: on the wall, a direction of zero length that was a dead end in the small algebra finds a partner in the large one, and together they behave like the creation and annihilation operators of a single fermion. This pairing happens only on the wall, so the fermion-like structure lives exactly where the geometry is singular.

*Provenance:* Transport Lab claim sheaf.localised-transport, version 5 (T04 Cor 4.5).

**Fact (imported) 52 (One-sided completion at the singularity).** The completion that repairs a degenerating geometry can be carried out at the central singularity of a Schwarzschild black hole, once that singularity has been opened up into a boundary. Coupling two extra dimensions to the dying direction, with the sign of the coupling chosen to suit the black-hole interior and the coupling switched on only inside the horizon, gives a geometry that is non-degenerate everywhere, and no new degeneracy appears anywhere else. The fermion-like pairing then lives exactly on the opened-up singularity, which has the shape of a line times a sphere.

*Provenance:* Transport Lab claim sheaf.one-sided-completion-singularity, version 4 (T04 Thm 8.12).

**Fact (imported) 53 (The Schwarzschild degeneration is boundary-tame in $\shW$).** At the centre of a Schwarzschild black hole the gravitational field is singular. Once the singularity is opened up into a boundary and suitably rescaled directions are used, the field's measure of lengths extends smoothly to that boundary and degenerates there in the mildest possible way: exactly one direction loses its length, and it does so at a linear rate. That dying direction is the same in two standard coordinate systems, and it is perpendicular to the slices traced out by observers falling freely inward.

*Provenance:* Transport Lab claim sheaf.schwarzschild-degeneration-boundary-tame, version 6 (T04 Thm 8.7).

**Fact (imported) 54 (The wall Gram).** On the wall, the enlarged geometry splits into two independent pieces: the ordinary directions that survive the degeneration, and a three-dimensional block made of the dying direction and the two added ones. A direct calculation shows that this block is never degenerate, whatever non-zero coupling strengths are used. The sign of the product of the two coupling constants decides how many directions of each sign the repaired geometry has.

*Provenance:* Transport Lab claim sheaf.wall-gram, version 3 (T04 Lem 4.2).

**Fact (imported) 55 (The degeneration, exactly).** Approaching the centre of a black hole the gravitational field grows without bound, but once that overall growth is divided out the field settles to a definite limit. The limit is degenerate: it registers only the time direction and is blind to the other three. The radial direction, along which the light cones fold, becomes one of these blind directions only in the limit, not at any finite distance from the centre.

*Provenance:* Transport Lab claim singularity.degeneration-exactly, version 2 (T05 Prop 2.6).

**Fact (imported) 56 (The descent, and what it erases).** A single fermionic mode can be described by a two-by-two matrix. The descent keeps the two diagonal entries, which record whether the mode is empty or occupied, and discards the two off-diagonal entries, which record quantum coherence between those two possibilities.

*Provenance:* Transport Lab claim singularity.descent-what-it-erases, version 5 (T05 Prop 5.5).

**Fact (imported) 57 (Modular theory of a matrix factor, proved outright).** Tomita-Takesaki theory attaches to a quantum state a natural time evolution, called the modular flow. For two finite quantum systems in an entangled state, this lemma works out every ingredient of that theory by hand. The modular flow turns out to be the evolution generated by the reduced density matrix of one side, and the state satisfies the equilibrium (KMS) condition with respect to it.

*Provenance:* Transport Lab claim singularity.modular-theory-matrix-factor-proved-outright, version 4 (T05 Lem 7.1).

**Fact (imported) 58 (Hypothesis (S): slot statistics, derived from the slot-module hypothesis).** The framework's account of quarks and leptons rested on an assumption, called (S), that two particular ingredients of each particle behave like fermions, the kind of particle that obeys the exclusion principle. It is now a consequence of a weaker assumption: that a particle's states are built from one empty state by adding quanta of a single two-state kind, and that handedness splits them into particles and their mirror-image antiparticles in a way that respects the intermediate Pati-Salam symmetry the framework uses. Under that assumption, with the standard requirement that the theory be free of anomalies, the ingredients must be fermions, and the possible states of a particle form exactly the standard quantum state space of five fermionic modes, with the right handedness for the particles of the Standard Model.

*Provenance:* Transport Lab claim standard-model.hyp-s-slot-statistics, version 9 (T12 Hypothesis (S)).

**Fact (imported) 59 (Isometries extend to algebra homomorphisms).** If a map of arrows preserves square lengths, it automatically extends to a map of the whole algebra that respects multiplication. Symmetries of space therefore act on everything built from arrows.

*Provenance:* Transport Lab claim std-algebra.functoriality, version 1.

**Fact (imported) 60 (The spacetime algebra as a matrix algebra, and the spacetime split).** The algebra of spacetime arrows can be written with $2 \times 2$ arrays of quaternions, or, after allowing complex numbers, with the $4 \times 4$ Dirac matrices of relativistic quantum mechanics. Its even part is exactly the algebra of an observer's ordinary three-dimensional space.

*Provenance:* Transport Lab claim std-algebra.sta-matrix, version 1.

**Fact (imported) 61 (Orthogonal bases and the law of inertia).** However you choose perpendicular unit directions in a space, you always find the same number of "space-like", "time-like" and "zero" directions. These three counts are the space's signature, and they are all there is to know about it.

*Provenance:* T. Y. Lam, Introduction to Quadratic Forms over Fields, AMS (2005)., the diagonalisation of forms and Sylvester's law of inertia (real case).

**Fact (imported) 62 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 63 (Hyperbolic pairs and the Witt decomposition).** Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 64 (The ladder pairs satisfy the CAR, as vectors).** Each step up the tower adds a new pair of special zero-length directions to the space. Taken together, these pairs obey exactly the algebraic rules that quantum theory uses for fermionic modes, the kind of states occupied by particles such as electrons, with one mode per step. The rules hold for the directions themselves, so nothing has to be added or chosen to make them work, and a new step never disturbs the modes already present.

*Provenance:* Transport Lab claim tower.ladder-pairs-satisfy-car-vectors, version 4 (T03 Prop 4.1).

**Fact (imported) 65 (Rigidity; the clock is frozen).** Building the tower by adding pairs of opposite-signed directions never changes the essential type of the algebra. Every floor has the same underlying number system, the same centre and the same kinds of obstruction as the ground floor. For the spacetime algebra, every floor is a matrix algebra over the quaternions, so the eight-step Bott clock does not advance along the tower: it stays where it starts.

*Provenance:* Transport Lab claim tower.rigidity-clock-frozen, version 5 (T03 Thm 3.6).

**Fact (imported) 66 (Cohomological form of the no-go).** Earlier results show that the symmetries fixing a light-like direction slide every candidate partial inverse along by a definite amount. This theorem packages that sliding as a single algebraic invariant, which vanishes only in the smallest case of one space and one time direction. Because the invariant is built inside the original algebra, enlarging the algebra or the symmetry group cannot remove it.

*Provenance:* Transport Lab claim transport.cohomological-form-no-go, version 4 (T01 Thm 4.8).

**Fact (imported) 67 (Descent: the read-out map).** After computing in the enlarged space one needs a way back to the original one. The read-out map does this for every point not at infinity, and for ordinary invertible vectors it gives back the familiar reciprocal. For zero-length vectors the answer lies at infinity, and the read-out declines, because no point of the original space represents it.

*Provenance:* Transport Lab claim transport.descent-read-out-map, version 2 (T01 Lem 4.23).

**Fact (imported) 68 (The door is one-way).** The series repairs an algebra by moving up to a larger one. Starting from a nondegenerate algebra, this result shows that there is no way back down that respects multiplication: no structure-preserving map from either larger algebra (the second kind exists only when the signature meets a congruence condition) to the original one exists. Any return journey must lose something, and the natural way back loses the part the climb added.

*Provenance:* Transport Lab claim transport.door-one-way, version 5 (T01 Thm 7.6).

**Fact (imported) 69 (Exhaustiveness: every zero divisor is annihilated by an idempotent).** Whenever division fails in a Clifford algebra with a nondegenerate notion of length, the failure can be traced to an element that equals its own square. This shows that the three kinds of failure already named cover every case. Which kinds occur depends only on the numbers of space and time directions.

*Provenance:* Transport Lab claim transport.exhaustiveness-every-zero-divisor-annihilated-idempotent, version 3 (T01 Thm 3.9).

**Fact (imported) 70 (Existence and classification of type C).** Some Clifford algebras secretly come in two independent halves, and the elements that pick out each half are called central idempotents. This result pins down exactly when that happens: precisely when the number of positive directions minus the number of negative ones leaves remainder 1 on division by four. In that case there are exactly two such elements, built from the product of all the basis directions. Reversing every direction swaps the two halves, but no conjugation by an element of the algebra itself can do so, since these elements commute with everything.

*Provenance:* Transport Lab claim transport.existence-classification-type-c, version 4 (T01 Thm 3.6).

**Fact (imported) 71 (Existence locus of type N).** In a space with both positive and negative directions, like the space-time of relativity, there are nonzero directions of zero length, called null directions. This result says they exist exactly when both kinds of direction are present, and that they then form a cone, much like a light cone. Each such direction multiplied by itself gives zero, so it can never be divided by, even in a larger algebra that contains the original one.

*Provenance:* Transport Lab claim transport.existence-locus-type-n, version 5 (T01 Prop 3.3).

**Fact (imported) 72 (Fusion occurs at most once).** Each Clifford algebra sits at one of eight positions on a clock. One repair rule never moves the hand; the other moves it by one step, is only used at the two positions where the algebra is split, and always lands where no split occurs. So the second rule can be used at most once, after which nothing structural changes. The algebra of spacetime starts at a position that never needs the second rule.

*Provenance:* Transport Lab claim transport.fusion-occurs-most-once, version 5 (T01 Prop 7.4).

**Fact (imported) 73 (No fourth rule).** Division can fail in a nondegenerate real Clifford algebra in exactly three ways, and each has its own prescribed fix: add a pair of dimensions, add one dimension, or do nothing. Since every failure of division is one of the three, the list of fixes is complete.

*Provenance:* Transport Lab claim transport.no-fourth-rule, version 4 (T01 Cor 6.7).

**Fact (imported) 74 (No transport terminates).** Each repair in the transport programme enlarges the algebra to fix a failure of division. This result shows that the enlarged algebra always has failures of its own: one repair adds new light-like directions, the other produces projections and elements that square to zero. So the process never ends in an algebra where every nonzero element can be divided by.

*Provenance:* Transport Lab claim transport.no-transport-terminates, version 4 (T01 Prop 7.8).

**Fact (imported) 75 (One generator is minimal; the minimal completions classified).** When a Clifford algebra splits into two halves, one can try to repair it by adding directions. Adding nothing leaves it split; adding one direction of zero length only thickens the algebra without joining the halves; adding one direction of nonzero length joins them; adding more is larger than needed. The two possible single directions, of positive or negative square, give the same algebra, so the repair is unique and cannot tell which sign was used.

*Provenance:* Transport Lab claim transport.one-generator-minimal-minimal-completions-classified, version 5 (T01 Thm 5.7).

**Fact (imported) 76 (The pinching, and its kernel).** After moving up to the completed algebra there is a canonical way to come back down: keep the blocks that commute with a chosen projector and discard the rest. What is discarded is exactly the new ladder pair that the completion added, and every element of the original algebra comes back unchanged under the natural identification of the corner (under the other standard identification it comes back as its grade involution, still faithfully). Coming back down does not respect multiplication in general, and the result gives the exact correction term.

*Provenance:* Transport Lab claim transport.pinching-kernel, version 3 (T01 Prop 7.5).

**Fact (imported) 77 (Representation-independent minimality of the completion).** One might hope to repair a geometry inside some smaller algebra by placing the original algebra in it in an unusual way. This result rules that out. What the repair needs is room for the points of the geometry together with their separations, and that requires at least one extra positive and one extra negative direction, whatever the embedding.

*Provenance:* Transport Lab claim transport.representation-independent-minimality-completion, version 4 (T01 Thm 4.19).

**Fact (imported) 78 (Rule 1 is Morita-trivial).** The basic transport step adds one new pair of null directions to an algebra. The enlarged algebra turns out to be the algebra of two-by-two matrices with entries in the original one, with the new null pair playing the role of the off-diagonal entries. So the step leaves the essential type of the algebra unchanged, although whether certain other kinds of obstruction are present can change.

*Provenance:* Transport Lab claim transport.rule-1-morita-trivial, version 5 (T01 Thm 7.1).

**Fact (imported) 79 (Rule 2: ideal fusion, sharp form).** Some Clifford algebras split into two independent halves. Adding one new direction, of either sign, fuses the halves into a single algebra of two-by-two matrices whose entries come from the algebra's even part. The fused algebra has no split of its own, and the two choices of sign give the same algebra.

*Provenance:* Transport Lab claim transport.rule-2-ideal-fusion-sharp-form, version 4 (T01 Thm 5.5).

**Fact (imported) 80 (Splitting along a hyperbolic plane).** When a space contains a light-like direction paired with a partner, the algebra of the whole space splits into four slots built from that pair, each filled by an element of the algebra of the remaining directions. The split is unique, which makes it a reliable bookkeeping device. Multiplying by the light-like direction never sends a nonzero element of the remaining algebra to zero.

*Provenance:* Transport Lab claim transport.splitting-along-hyperbolic-plane, version 3 (T01 Lem 2.4).

**Fact (imported) 81 (Swap-and-rescale normal form).** Points of the enlarged space can be written as a triple: a number, an ordinary vector, and a second number. In these terms, taking the reciprocal just swaps the two numbers, with a factor of two, a simple operation that always works. Dividing out the first number gives back the usual answer; when that number is zero, the answer is one of three kinds of point at infinity.

*Provenance:* Transport Lab claim transport.swap-rescale-normal-form, version 4 (T01 Prop 4.21).

**Fact (imported) 82 (Totality).** In a Clifford algebra with vectors of zero length, the reciprocal of a vector is undefined on exactly those vectors. After moving to the enlarged space of points, a single reflection-like operation gives a reciprocal everywhere: it agrees with the usual one on ordinary vectors and sends zero-length vectors to points at infinity. Those values are the limits one would expect, and no other continuous rule matches the usual reciprocal.

*Provenance:* Transport Lab claim transport.totality, version 3 (T01 Thm 4.10).

**Fact (imported) 83 (Type P is self-repairing).** Some zero divisors are projection-like elements, ones that equal their own square. For these, the repair being sought is already available: each such element can serve as its own partner and satisfies the required identities. Because the rule is simply to take the element itself, it automatically respects every symmetry, so nothing needs to be added to the algebra.

*Provenance:* Transport Lab claim transport.type-p-self-repairing, version 2 (T01 Prop 6.1).

**Prediction 84 (Neutrino mass sum at the oscillation floor).** If the second stage of the framework's family symmetry breaking is hierarchical (Premise (H)), the framework predicts that the three neutrino masses add up to the smallest total that oscillation experiments allow, about 0.059 eV, with the normal ordering. Cosmological surveys are now close to this value, so it is a near-term test.

**Prediction 85 (No neutrinoless double-beta signal at next-generation sensitivity).** Neutrinoless double-beta decay is a rare nuclear process that would show neutrinos are their own antiparticles. Assuming the framework's premise (H), that the lightest neutrino is nearly massless, the effective mass that sets the rate comes out at a few thousandths of an electronvolt, between about $1.3$ and $3.9$ meV, with the sharper windows $1.3$ to $1.7$ or $3.5$ to $3.9$ meV if the breaking is also assumed real. That is too small for the next generation of experiments to detect, so a clear signal there would count against the framework. The absence is conditional: it rests on premise (H).

**Prediction 86 (The no-echo prediction, registered).** If quantum effects altered a black hole's surface, merging black holes would ring with faint repeated echoes a fraction of a second after the main signal. This framework puts its quantum structure deep inside the hole instead, so it predicts no echoes: the ringing should be exactly as general relativity says. A single confirmed echo would refute it.

The thread of the tour is one move, made again and again. Division fails along null directions, so the space is enlarged by a pair of new directions, one of each sign. The work is done in the larger setting and the answer is brought back, noting where it cannot come back.

At the centre of a non-rotating black hole that move supplies the missing partner. Its boundary modes then carry a thermal state at the Hawking temperature whose occupation numbers are derived rather than chosen. On the matter side, the same algebra yields the symmetry of the strong, weak and hypercharge forces.

Not all of this is proved from nothing, and the assumptions are part of the picture. The repair along a wall assumes the degeneration is tame. The family results assume Hypothesis (S) about slot statistics.

The neutrino results assume that the framework realises a heavy Majorana mass, which is left for later work. The sharp total neutrino mass further assumes that the lightest neutrino gets almost no mass.

The mirror world assumes a single shared origin for every hidden sector. It also assumes that only sectors related by a reflection are forced to match. That the matter excess is imprinted equally in the two mirror sectors is proved for the mirror copy, not assumed.

Under these assumptions the framework makes claims that can fail. It predicts that the three neutrino masses add up to about 0.059 eV, with the normal ordering. It expects no neutrinoless double-beta signal at next-generation sensitivity, so a clear signal would count against it. It predicts no echoes after black holes merge, and a single confirmed echo would refute it.
