# One relation, read twice

**Abstract.** A Clifford algebra rests on one relation, which says how two vectors multiply when their order is swapped.

Written on an orthogonal basis it is a metric, the language of geometry; written on a Witt basis of paired null vectors it is the rule obeyed by fermions, the language of quantum theory. The geometric reading carries exactly one conversion constant, the speed of light.

Applied to the electron, the algebra ties the imaginary unit to the choice of rest frame. Granting stated premises, including that recording is irreversible and Hypothesis (S), measurement leaves every outcome in its own branch and nothing physically collapses. That stance predicts that no collapse signature will be found.

The walk starts with the two readings of the relation, follows the geometric reading to the speed of light, then the quantum reading through the electron's law to Schrödinger's equation, and ends with measurement and the prediction it makes.

## What we assume

**Postulate 1 (CPT covariance of the kinematic structures and of every action).** This is an assumption, partly checked: a particular symmetry that swaps matter with antimatter, reverses time and mirrors space is taken to leave every basic structure of the framework, and every one of its laws including the strengths of the forces, unchanged. Worked out exactly, the symmetry involves complex conjugation, the same kind of operation quantum field theory uses for this symmetry, rather than an ordinary linear swap. The series verifies the assumption for the geometric structures and for gravity, and assumes it for the imported description of the forces and of matter. It is the first premise behind the claim that the matter-antimatter orientation of the universe is a free choice rather than something the framework fixes.

**Postulate 2 (The flag as datum: the sign of the Witt flag is configuration data).** The framework's origin event makes one yes-or-no choice, which fixes both which of matter and antimatter is which and the direction of time. This assumption says where that choice lives: it is a fact about our particular universe, set when the universe began, not a built-in feature of the theory's laws or structure. A different universe obeying the same laws could have made the opposite choice. Several results, including the claim that the choice is a starting condition rather than a setting of the laws, rest on this assumption. It would be shown wrong if some part of the theory's fixed structure were found to prefer one answer.

**Postulate 3 (Recording is irreversible, stated so it can be refuted).** When an instrument records a measurement result, that record is assumed to be permanent: it cannot be undone. The series proves something similar for a more abstract process but not for real laboratory records, so this is stated openly as an assumption that could be refuted.

## One relation, read twice

These results take the defining relation of a Clifford algebra and ask what follows from reading it as geometry and as quantum theory.

The defining relation of a Clifford algebra is \[ \{e_{a}, e_{b}\} = 2g_{ab}\mathbf{1} \] which on an orthogonal basis displays a metric $g$, measuring lengths and angles.

On a Witt basis of paired null vectors the same relation reads $\{c(w_{i}), c(\bar{w}_{j})\} = \delta_{ij}$, exactly the canonical anticommutation relations of fermionic modes. So geometry and quantum structure are two charts on one algebra, at the level of structure rather than dynamics.

**Theorem 4 (The two presentations).** The basic rule of a Clifford algebra can be written in two ways. In one it describes distances and angles, the language of geometry and gravity; in the other it is exactly the rule obeyed by fermions, the language of quantum theory. The paper takes this to mean that geometry and quantum structure are two views of one object, though only at the level of structure, not of how things evolve.

*Rests on:* one-relation.imported-pure-spinors-incidence-chart, std-algebra.vector-squares, std-algebra.witt-basis-car

If geometry can be read as a system of fermion modes, one can count the modes.

There are two counts, a real capacity using real null vectors and a complex one allowing complex vectors, \[ r_{\R}(p,q) = \min(p,q), \qquad r_{\C}(p,q) = \lfloor d/2 \rfloor \] with $d = p + q$. For spacetime $(1,3)$ they are $1$ and $2$, and for the six-dimensional $(2,4)$ they are $2$ and $3$.

**Theorem 5 (The two capacities, and three consequences).** Reading spacetime geometry as a system of fermion modes, there are two ways to count the modes: using only real directions, or allowing complex ones. The two counts usually differ, and for ordinary spacetime they give one and two. Each step up the tower of extended spaces adds exactly one mode to both counts, and the complex count of the extended six-dimensional space is three.

*Rests on:* one-relation.imported-witts-extension-theorem, one-relation.two-presentations, tower.witt-index-quantum-capacity, std-algebra.vector-squares, std-algebra.witt-decomposition

The geometric reading carries something the quantum reading does not see.

Time and space are measured in independent units, so a quadratic form on events needs a conversion constant $c$, \[ Q = c^{2}t^{2} - |\mathbf{x}|^{2} \] in the Lorentzian case, and the null cone is the invariant ratio it fixes. Such a finite ratio exists only when the signature is mixed, $pq \neq 0$. This places the constant without deriving its value.

**Theorem 6 (The third constant is the conversion constant between the charts).** The speed of light can be seen as a conversion factor between units of time and units of length. This result shows such a factor exists only when spacetime mixes time-like and space-like directions, that there is only one such number, and that it is invisible in the quantum description and appears only on passing to the geometric one. It also places the three fundamental constants at three different levels of structure, without deriving any of their values.

*Rests on:* one-relation.imported-null-cone-determines-form-zeemans, one-relation.imported-witts-extension-theorem, std-algebra.bivector-exponential

The quantum reading now turns to the electron, whose relativistic law is first order.

A law $\nabla\psi = m\,\psi\,C$ with a constant factor $C$, applied twice, gives the Klein-Gordon equation \[ \nabla^{2}\psi = -m^{2}\psi \] exactly when $C^{2} = -1$. With $C^{2} = +1$ the sign is tachyonic, and a non-scalar square gives no scalar equation at all.

**Theorem 7 (The form of the law is forced by its square).** A first-order wave equation of this type, applied twice, should give the familiar relativistic relation between energy, momentum and mass. Whether it does depends only on the square of one constant factor in the law. That square must be minus one; any other choice gives faster-than-light behaviour or no sensible equation at all.

That condition can be solved completely.

The odd square roots of minus one in $\Cl(1,3)$ are \[ C = (\cos t + \sin t\, I)\,u \] with $u$ a unit spacelike vector and $I$ the pseudoscalar. A constant rotor moves $u$ and the chiral phase removes $t$, so for a single free fermion with minimal electromagnetic coupling every allowed law is the Dirac-Hestenes equation up to a constant field redefinition.

**Theorem 8 (Odd square roots of $-1$, and the chiral phase).** An earlier result says the constant factor in the electron's law must square to minus one. This one lists every allowed factor and shows that, for a single free electron, they all give the same equation seen in a rotated frame or with a harmless constant phase. Once other interactions are included, that phase is no longer harmless.

*Rests on:* std-algebra.pseudoscalar-commutation, primer.sign, std-algebra.vector-squares

Quantum mechanics needs an imaginary unit and slow-motion physics needs a rest frame, and these look like two separate choices.

With the law aligned to $C = Iu$, the admissible imaginary units $J$ correspond one to one with the unit timelike vectors orthogonal to $u$, through \[ \gamma_{0} = CJ \] so picking one picks the other. The imaginary unit is not an extra ingredient put in by hand.

**Theorem 9 (One datum, not two: the imaginary unit is the rest frame read through the law).** Quantum mechanics uses an imaginary unit, and nonrelativistic physics uses a rest frame. In this algebraic form of the electron's equation, once the law is fixed, picking one automatically picks the other. So the imaginary unit is not an extra ingredient that has to be put in by hand.

*Rests on:* one-relation.odd-square-roots-chiral-phase, std-algebra.duality

With the law and its imaginary unit in place, the slow-motion limit can be taken.

The operator is the vector derivative $\nabla = \gamma^{\mu}\partial_{\mu}$, forced, and the law is the Dirac-Hestenes equation \[ \nabla\psi\, I\sigma_{3} = m\,\psi\gamma_{0} \] whose slow limit is Schrödinger's equation, at a structural level and for a single free fermion.

The orientation of time comes from an earlier argument that assumes Hypothesis (S), and the rest frame itself is supplied by the laboratory, not derived.

**Theorem 10 (Schrödinger as the slow shadow).** The everyday equation of quantum mechanics, Schr\"odinger's, is shown to be the slow-motion limit of the relativistic electron equation, which is itself built from the basic algebra of spacetime. The paper tracks where each ingredient comes from, at a structural level: the mass from an earlier mechanism, at the observation level that mechanism's reading holds; the orientation half of the direction of time from an earlier argument that holds if the slots behave like the pairs (Hypothesis (S)); and the imaginary unit from the choice of rest frame. Only the first-order form of the law and the standard slow-motion expansion are imported, for a single free fermion. The rest frame itself is supplied by the laboratory, not derived.

*Rests on:* one-relation.arrow-frequency-are-one-bit-level, one-relation.form-law-forced-square, one-relation.imported-flag-arrow-superselection, one-relation.imported-condensate-derived-content, one-relation.odd-square-roots-chiral-phase, one-relation.one-datum-not-two-imaginary-unit, one-relation.vector-derivative-covariant-first-order-operator, standard-model.hyp-s-slot-statistics, std-algebra.vector-squares

Quantum mechanics also needs a rule for chances, Born's rule.

The unique conserved density is the time component of the current \[ J = \psi\gamma_{0}\tilde{\psi} \] and under the indifference premise, that nothing may prefer one of several equivalent outcomes, it is the only consistent assignment of weights. The result is conditional on that premise, and the density is relative to the laboratory's rest frame.

**Theorem 11 (The measure from indifference: Born's rule located).** Born's rule says the chance of a quantum outcome is the squared size of its part of the wave. Here the relevant density is fixed as the unique conserved, positive one, measured in the laboratory's rest frame. Then the series' indifference premise, a declared starting point and not a theorem, that nothing may prefer one of several equivalent outcomes, forces equal chances for equal parts and builds up to the squared-size rule. One assumption remains, that chances exist and add up, and the paper names it as what is still postulated, so the result is conditional on both.

*Rests on:* one-relation.dirac-current-conserved-density, one-relation.imported-indifference-instrument

The same premises bear on what happens in a measurement.

Granting indifference, that branches cannot see one another, and that recording is irreversible, with Hypothesis (S) behind the count, every outcome happens in its own branch and nothing physically collapses. Picking one outcome would be an uncaused preference.

Why this branch is the one experienced is left open.

**Theorem 12 (The record chain votes: measurement without collapse).** When a measurement is made, the framework, granting its stated premises (that an unexplained preference is forbidden, that recording is irreversible, and, behind its count of free numbers, Hypothesis (S) on the slots' statistics), says every possible outcome happens, each in its own branch that cannot see the others, rather than one outcome being picked by a physical collapse. It argues this in two ways: picking one outcome would be an unexplained preference, and collapse would need an endless supply of new random choices the framework does not have. The parallel with the cosmic case holds only in the limit of ideal recording, since laboratory decoherence is approximate, and the account leaves open why this branch is the one experienced. This is a testable, conditional bet: any confirmed sign of real wavefunction collapse would refute it.

*Rests on:* one-relation.imported-flag-arrow-superselection, one-relation.imported-indifference-instrument, one-relation.measure-indifference-borns-rule-located, standard-model.trichotomy-what-kind-number, dark-matter.asymmetry-arrow-counted-fifteenth-refutation, dark-matter.orientation-arrow-seventeenth-refutation, standard-model.hyp-s-slot-statistics, one-relation.recording-irreversible-stated-so-it-can, dark-matter.premise-cpt-covariance, dark-matter.premise-flag-as-datum

A stance on measurement is worth most if it can fail.

The framework predicts no objective-collapse signature: no spontaneous-localisation noise and no gravitationally induced collapse. A single confirmed detection would refute the prediction together with the argument behind it.

**Prediction 13 (No objective-collapse signature).** Some proposed theories say quantum superpositions collapse on their own, perhaps because of gravity, and these would leave tiny detectable traces such as extra random noise. This framework predicts that no such traces exist at any level of sensitivity. The prediction rests on the framework's account of measurement, under that account's premises. Experiments so far have found none, and a single confirmed detection would refute the prediction together with the argument behind it.

## Results cited, not shown

**Fact (imported) 14 (The asymmetry: the arrow counted, and the fifteenth refutation).** In this framework the excess of matter over antimatter is not produced by any process after the start. On a stance the paper flags, and which any calculation inside the framework that produced the excess would refute, it is part of the initial conditions the descent sets. A well-known alternative source, a constant angle in the strong force, is ruled out for our world by measurements of the neutron, although an angle that changed over time is not ruled out. The excess can only live in our world and its mirror twin; that it has the same size in every such world is assumed (the democracy premise P4, a theorem for the mirror), and its size is left as an unexplained input.

*Provenance:* Transport Lab claim dark-matter.asymmetry-arrow-counted-fifteenth-refutation, version 5 (T14 Prop 5.1).

**Fact (imported) 15 (The orientation is the arrow: the seventeenth refutation).** Our universe is made of matter rather than antimatter, and in this framework a single yes-or-no choice decides which is which. Assuming that the matter-antimatter symmetry (CPT) respects every structure of the theory, its laws included (checked for the core structures, assumed for the imported forces and later additions), that the slots behave like the pairs (Hypothesis (S)), and that the choice belongs to each possible universe rather than to the theory's fixed structure (all three stated as assumptions), this result shows that none of the framework's laws can make that choice: the symmetry turns any possible universe into another possible universe of the same theory with the choice reversed. So the choice differs between solutions of one and the same theory, which makes it a starting condition rather than a setting of the laws, and it is the same choice that sets the direction of time.

*Provenance:* Transport Lab claim dark-matter.orientation-arrow-seventeenth-refutation, version 9 (T14 Prop 5.2).

**Fact (imported) 16 (The arrow and the frequency are one bit, at $\Cl(1,3)$ level).** In the relativistic electron equation, the sign that separates particles from antiparticles and the direction in which a laboratory's time runs look like two separate choices. Once the form of the law is fixed, flipping one forces the other to flip, so they are a single yes-or-no choice. This does not explain where that choice comes from, which still rests on Hypothesis (S); it only shows that its two readings always agree.

*Provenance:* Transport Lab claim one-relation.arrow-frequency-are-one-bit-level, version 4 (T16 Cor 5.7).

**Fact (imported) 17 (The Dirac current is the conserved density).** The Dirac equation describes the electron relativistically. Among all the simple candidate currents one can build from its solutions, only one is conserved for every solution, the standard Dirac current. Its time component, the density, is always positive and is zero only when there is no wave at all.

*Provenance:* Transport Lab claim one-relation.dirac-current-conserved-density, version 2 (T16 Lem 6.1).

**Fact (imported) 18 (Imported: the condensate and the derived content).** This collects earlier results on how mass arises, each at the strength it was established. The size of the mass-carrying bracket is fixed exactly, but whether a condensate actually forms is only a reading that rests on an assumption. The vacuum's alignment is democratic only under a reading that rests on the indifference premise. On an empty background obeying Einstein's equations, and at the level of the Klein-Gordon equation, mass is how a composite grips the cosmological scale, and the forces come from a connection the framework forces rather than chooses, though how matter couples to it is again a reading.

*Provenance:* Transport Lab claim one-relation.imported-condensate-derived-content, version 3 (T16 Fact 2.6).

**Fact (imported) 19 (Imported: the flag, the arrow, and superselection).** The step down from the enlarged algebra to ordinary physics involves one binary choice, an orientation. That single bit is at once the direction of time's arrow and the distinction between matter and antimatter. Under three stated premises, a matter-antimatter (CPT) symmetry of the structures and laws, Hypothesis (S) that the composite's slots behave as fermions, and the assumption that the choice belongs to each universe rather than to the theory's fixed structure, it must be supplied as initial data rather than derived, and, as a declared stance, the framework takes its matter asymmetry as given rather than explaining it. A separate exact rule keeps different sectors invisible to one another rather than forbidden.

*Provenance:* Transport Lab claim one-relation.imported-flag-arrow-superselection, version 7 (T16 Fact 2.5).

**Fact (imported) 20 (Imported: the indifference instrument).** The series assumes that nature does not make arbitrary choices: if nothing in the theory tells two things apart, the theory may not treat them differently. In use, this means giving equal weight to things related by an exact symmetry, while never forcing genuinely different things to match. Numbers the theory leaves free are treated as facts to be measured rather than averaged away (a reading held at observation level), and the question of why we find ourselves in our sector rather than its mirror is treated as a matter of where we stand rather than of dynamics. All of this is an assumption of the programme, not a result.

*Provenance:* Transport Lab claim one-relation.imported-indifference-instrument, version 4 (T16 Fact 2.7).

**Fact (imported) 21 (Imported: the null cone determines the form, and Zeeman's theorem).** Knowing which directions are light-like fixes the spacetime metric up to an overall scale. In three or more dimensions Zeeman showed more: any map of flat spacetime that preserves which events can influence which is built from rotations, boosts, shifts and rescalings. In two dimensions this fails, since each light direction can be stretched independently.

*Provenance:* Transport Lab claim one-relation.imported-null-cone-determines-form-zeemans, version 3 (T16 Fact 2.9).

**Fact (imported) 22 (Imported: pure spinors and the incidence chart).** This collects earlier results that the one-relation paper needs. In six complex dimensions every four-component spinor of the conformal algebra is the vacuum of its own small system of fermionic operators, a coincidence special to this dimension. Each point of spacetime corresponds to a line of such spinors, and the standard way of placing spacetime points into the six-dimensional space makes every point a light-like vector.

*Provenance:* Transport Lab claim one-relation.imported-pure-spinors-incidence-chart, version 5 (T16 Fact 2.3).

**Fact (imported) 23 (Imported: Witt's extension theorem).** Witt's theorem concerns a space with a fixed rule for measuring lengths. It says that any length-preserving match between two pieces of the space extends to a length-preserving symmetry of the whole space, so pieces that look alike from the inside are also indistinguishable from the outside. It is a classical result from the 1930s.

*Provenance:* E. Witt, Theorie der quadratischen Formen in beliebigen K"orpern, J. Reine Angew. Math. 176 (1937) 31--44.; T. Y. Lam, Introduction to Quadratic Forms over Fields, Graduate Studies in Mathematics 67, American Mathematical Society (2005)., Ch.~I, \S4.

**Fact (imported) 24 (The vector derivative is the covariant first-order operator).** Relativity requires a law to look the same to all observers. Among the simplest kinds of first-order derivative operator in the spacetime algebra, only one meets that requirement, up to a constant multiple: the vector derivative. So, within that class, the operator in the electron's equation is not a free choice.

*Provenance:* Transport Lab claim one-relation.vector-derivative-covariant-first-order-operator, version 4 (T16 Lem 5.1).

**Fact (imported) 25 (The sign of $\omega^2$).** Multiplying all the basis directions of a Clifford algebra together gives a special element called the pseudoscalar. Its square is always plus one or minus one, and this result says which. The answer depends only on the number of positive directions minus the number of negative ones: plus one when that difference leaves remainder 0 or 1 on division by four, and minus one otherwise.

*Provenance:* Transport Lab claim primer.sign, version 2 (T00 Lem 9.5).

**Fact (imported) 26 (Hypothesis (S): slot statistics, derived from the slot-module hypothesis).** The framework's account of quarks and leptons rested on an assumption, called (S), that two particular ingredients of each particle behave like fermions, the kind of particle that obeys the exclusion principle. It is now a consequence of a weaker assumption: that a particle's states are built from one empty state by adding quanta of a single two-state kind, and that handedness splits them into particles and their mirror-image antiparticles in a way that respects the intermediate Pati-Salam symmetry the framework uses. Under that assumption, with the standard requirement that the theory be free of anomalies, the ingredients must be fermions, and the possible states of a particle form exactly the standard quantum state space of five fermionic modes, with the right handedness for the particles of the Standard Model.

*Provenance:* Transport Lab claim standard-model.hyp-s-slot-statistics, version 9 (T12 Hypothesis (S)).

**Fact (imported) 27 (The trichotomy: what kind of number $N$ is).** The framework's one large number, $N$, could in principle be fixed by the structure of the theory, by its equations, or by the starting conditions of the universe. This result proves that rescaling it changes nothing else the theory derives, reads that, at observation level, as showing that the structure alone cannot fix it, and imports the fact that no equation governs it. With the action as currently written $N$ turns out to be a fixed parameter of the laws; it would count as a starting condition only if the theory were modified in a specific way that the series leaves as an open choice.

*Provenance:* Transport Lab claim standard-model.trichotomy-what-kind-number, version 10 (T12 Prop 7.6).

**Fact (imported) 28 (Exponentials of bivectors with scalar square).** Turning by an angle in a plane is the exponential of the plane piece times the angle, just as $e^{i\theta}$ turns by $\theta$ in the complex plane. Planes whose square is positive give boosts instead of rotations, and planes containing a zero-length direction give the simplest motions of all, written exactly as one plus the plane piece.

*Provenance:* Transport Lab claim std-algebra.bivector-exponential, version 1.

**Fact (imported) 29 (Duality).** Multiplying by the unit volume trades an element for its complement: a plane in three dimensions for the line perpendicular to it. Under this exchange, adding a direction and removing one swap roles.

*Provenance:* Transport Lab claim std-algebra.duality, version 1.

**Fact (imported) 30 (How the pseudoscalar commutes).** The unit volume element commutes with everything in odd dimensions, and flips the sign of arrows in even dimensions. If the space has a direction of zero length, the volume element squares to zero.

*Provenance:* Transport Lab claim std-algebra.pseudoscalar-commutation, version 1.

**Fact (imported) 31 (The product of two vectors).** Multiplying two arrows gives a number plus something new. The number is their ordinary dot product. The new part changes sign when the order is swapped, and turns out to be the oriented plane the two arrows span.

*Provenance:* Transport Lab claim std-algebra.vector-squares, version 1.

**Fact (imported) 32 (Null pairs satisfy the canonical anticommutation relations).** Inside a Clifford algebra, a direction of space paired with a direction of time produces two zero-length arrows that obey exactly the rules for creating and destroying a fermion. With several such pairs you get several independent fermion modes, without building any Hilbert space first.

*Provenance:* Transport Lab claim std-algebra.witt-basis-car, version 1.

**Fact (imported) 33 (Hyperbolic pairs and the Witt decomposition).** Any space with both space-like and time-like directions can be cut into perpendicular copies of the simplest space-time plane, plus a leftover piece that is purely space-like or purely time-like, plus the directions the length rule cannot see. The number of space-time planes, the smaller of the two counts, is the largest number of independent mutually perpendicular light-like directions the space can hold.

*Provenance:* Transport Lab claim std-algebra.witt-decomposition, version 1.

**Fact (imported) 34 (Witt index is quantum capacity).** Inside a Clifford algebra one can ask how many independent fermionic modes can be built directly from vectors. The answer is a classical number attached to the geometry, the Witt index: the largest number of independent zero-length directions that are all orthogonal to one another. For a space with p positive and q negative directions it is the smaller of p and q. Each step up the tower raises this number by exactly one, so each step adds precisely one mode of capacity and no more.

*Provenance:* Transport Lab claim tower.witt-index-quantum-capacity, version 4 (T03 Thm 4.3).

One relation, read twice, gives both the geometry of spacetime and the fermion structure of quantum theory.

The steps on measurement rest on the postulates set out under what we assume, that laboratory records are never unwritten and Hypothesis (S) on slot statistics, together with the indifference premise. A single confirmed collapse signature would refute the prediction together with the argument behind it.
