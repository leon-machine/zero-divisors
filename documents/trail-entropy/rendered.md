# Entropy and information

**Abstract.** A black hole's entropy is proportional to its horizon area, and any theory of its quantum structure must say what that entropy counts and where its information goes. In this framework it counts fermionic modes gathering on the hole's inner surface, and the count matches the Bekenstein-Hawking value only over a span of about one natural time unit of the hole.

If that span is set by the modes' own clock, the theory predicts one boundary-mode fermion per Bekenstein-Mukhanov area quantum of horizon.

The trail then follows information: how fast it spreads, why the framework predicts no gravitational-wave echoes, and how, in a simple evaporation model, the radiation's entropy rises, levels off and falls back to zero.

The walk first counts the modes and tests the count against the area law, then turns to how information spreads and how it leaves in the radiation. Each result appears after the ones it rests on.

## What we assume

**Postulate 1 (Intrinsic clock (IC), flagged premise).** This is an assumption, not a result: the time over which a black hole's interior modes are counted is set by those modes' own internal clock rather than picked by hand. It is flagged openly so that its consequences can test it. If the numbers it leads to fail, the assumption fails with them. It is used only for non-rotating black holes in otherwise empty space: with a positive cosmological constant, the same reading of the clock gives the wrong entropy.

**Postulate 2 (C1: curvature cutoff).** This assumption says where the quantum degrees of freedom near a black hole's singularity live: on the surface inside the black hole where the gravitational field strength (curvature) reaches the Planck scale. That surface sits at a radius growing like the cube root of the mass. It is an assumption of the counting, not a derived result, and it is used only to calibrate the count on non-rotating black holes in otherwise empty space; on spinning black holes, or with a positive cosmological constant, read literally it gives the wrong entropy.

**Postulate 3 ((L$_E$): boundary-mode locality, as descent covariance on finite windows).** This assumption says that the quantum modes at a black hole's singularity evolve in a way that never disturbs what a measurement of their occupations would find: they change phases and build correlations, but never move particles between points or create them in pairs. Part of this is proved for the operators the framework supplies; ruling out any other operators is assumed. The assumption has a price: under it, information placed in one mode does not spread rapidly through the others in real time, so the fast scrambling often attributed to black holes holds here only as a statement about the modes' thermal clock, not about their actual evolution.

**Postulate 4 (The rate model's kinematic inputs: (L), (U), (C), (I)).** These are the basic assumptions of the framework's simple model of black-hole evaporation. Everything lives in two places, the black hole's interior modes and the radiation; the total state stays pure; the interior has a definite capacity that only shrinks once full; and each emitted quantum arrives entangled with a fresh partner inside. The freshness of each partner is assumed rather than derived.

## Entropy and information

This section moves from counting a black hole's modes to tracking the information they carry.

The starting point is a count of the fermionic modes that build up on the stretched singularity, the hole's inner surface, as Killing time runs on. Assuming the premises (C1) and (C2), with $\nu$ modes per Planck cell, the number gathered over a span $\Delta t$ is \[ N = 8\pi\,\nu\,M\,\Delta t\,/\,\lP^2 , \qquad \frac{dN}{dt} = \frac{\nu}{\TH} \] to leading order, so the accrual rate is set by the Hawking temperature.

The density factor $\nu$ is left open for now.

**Theorem 5 (The mode count).** Granting the singularity paper's two placement assumptions (the modes sit on the black hole's inner surface, a fixed number per smallest cell), modes accumulate there as time runs on. To leading order in the ratio of that surface's radius to the hole's size, the number gathered per unit time is proportional to the mass, or equivalently inversely proportional to the hole's Hawking temperature. The overall factor depends on how densely modes are packed, which is left open here.

*Rests on:* scrambling.slice-volume-exactly-per-unit-killing, singularity.stretched-singularity-count

A count of modes is a count of entropy, so it can be tested against the Bekenstein-Hawking area law. The count equals the entropy, coefficient included, exactly when the counting span is of order one Schwarzschild time: \[ N = \SBH = 4\pi M^2 \quad \text{if and only if} \quad \nu\,\Delta t = M/2 \]

Causality independently singles out a span of that order. Counting over the whole lifetime gives far too much, a tension the result records but does not resolve.

**Theorem 6 (The area-law test).** The framework counts quantum modes that accumulate at a black hole's inner surface over some span of time. The count matches the Bekenstein-Hawking entropy, numerical factor included, only if that span is about one natural time unit of the hole, which is also the span causality singles out. Counting over the hole's whole lifetime instead gives far too much, a puzzle shared with other interior-volume pictures and not resolved here.

*Rests on:* scrambling.mode-count, singularity.causal-epoch-computed-exactly

The test still leaves two unknowns, how long to count for and how densely the modes are packed. Assuming the intrinsic-clock premise (IC), read as a calibration on the Schwarzschild family, the counting span is the modular period: \[ \Delta t = \beta = \frac{2\pi}{\kappa} = 8\pi M \]

That leaves a single number, the density $\nu$, which the theory must reproduce or the premise fails.

**Theorem 7 (The epoch is the modular period; two unknowns become one).** The entropy count needed two unknown inputs: how long to count for, and how densely modes are packed. Assuming the counting time is set by the modes' own clock, it must be one thermal cycle of the black hole. That leaves a single number, the packing density, which the theory must reproduce or else the assumption fails.

*Rests on:* scrambling.area-law-test, scrambling.clock-inventory-boundary-modes, singularity.euclidean-rotor-where-it-lies, scrambling.intrinsic-clock-ic-flagged-premise

Fixing the clock turns the area law into a definite prediction. Counting a fermionic mode as carrying at most $\ln 2$ nats, the density must be \[ \nu = \frac{1}{16\pi\ln 2} \] one boundary-mode fermion per $4\ln 2$ Planck cells of horizon area, one per Bekenstein-Mukhanov area quantum, per modular period.

The test is internal: if the theory's own calculation of this density gave a different value, the intrinsic-clock premise would be refuted.

**Prediction 8 (One boundary mode per Bekenstein-Mukhanov area quantum).** The framework predicts how densely a black hole's horizon modes record information: one elementary fermionic mode for about every three Planck-sized patches of horizon area (exactly $4\ln 2 \approx 2.77$ of them, the area quantum Bekenstein and Mukhanov proposed), per cycle of the hole's natural clock. Each such mode can hold one bit. Given the premise that this clock sets the counting epoch, this is the counting that reproduces the Bekenstein-Hawking entropy. The test is internal to the theory: if its own calculation of this density gave a different number, a key assumption about the clock would be refuted.

With the modes counted, the next question is how quickly information spreads among them. The modes' only clock is the boost at rate $\kappa$, which stretches operator amplitudes as $e^{\kappa t}$, so a disturbance on one mode spans all $N$ modes after the fast-scrambling time \[ t_* = \kappa^{-1}\ln N = \frac{\beta}{2\pi}\,\ln S \]

The rate meets the known upper bound on chaos, though this is shown only for a simple free-fermion model of the dynamics.

**Theorem 9 (The spreading law, and the chaos bound met, not saturated).** A disturbance entering the black hole's interior modes spreads through them exponentially fast, because the modes' only clock is a stretching motion. Assuming a generic coupling between the modes, it reaches every mode after a time that grows with the logarithm of the entropy, the fast-scrambling time. Under the series' premise that the modes on each light ray are in their lowest-energy state, the spreading rate equals the rate named by a known general bound on chaos, but the dynamics is not chaotic: disturbances spread without growing in real time, so the bound is met rather than saturated.

*Rests on:* scrambling.area-law-test, scrambling.clock-inventory-boundary-modes, scrambling.imported-modes-modular-inventory, scrambling.mode-count

Where the quantum structure sits also has an observable consequence. By premise (C1) it lies at the stretched singularity, deep inside the hole at Planck curvature, while the horizon stays the smooth vacuum horizon of general relativity.

So merging black holes should ring exactly as general relativity says, with no echo train at the delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ that near-horizon structure would produce. One statistically confirmed echo train would refute it.

**Prediction 10 (The no-echo prediction, registered).** If quantum effects altered a black hole's surface, merging black holes would ring with faint repeated echoes a fraction of a second after the main signal. This framework puts its quantum structure deep inside the hole instead, so it predicts no echoes: the ringing should be exactly as general relativity says. A single confirmed echo would refute it.

The remaining steps ask what the radiation carries, and they need an exact way to measure lost information. Descent keeps only the diagonal blocks of a state $\rho$, and the entropy it adds is a relative entropy: \[ S\bigl(E(\rho)\bigr) - S(\rho) = \rel{\rho}{E(\rho)} \geq 0 \]

The gain is zero only when there was nothing to discard, that is when $\rho = E(\rho)$.

**Theorem 11 (The deficit theorem: the cost of descent, exactly).** Descent here means discarding the parts of a quantum state that link different sectors, keeping only the blocks along the diagonal. The theorem says the entropy gained by doing so equals a standard measure of how distinguishable the original state is from its descended version. The gain is never negative, and it is zero only when there was nothing to discard.

The walk now enters the framework's simple rate model of evaporation, built on the postulates in what we assume. Each emitted quantum is entangled with a partner kept in a window inside, and partners are pushed out, or evicted, as the hole shrinks.

Under (L), (U), (C), (I) and boundary-mode locality (L$_E$), the window state is always a product of thermal pieces, so the radiation's entropy is \[ S_R(t) = S_L(t) = \sum_{k \in W(t)} h_k \] the sum over the partners $k$ still in the window $W(t)$.

**Theorem 12 (Eviction: the window is a thermal product, and the radiation entropy is its content).** In the framework's rate model, on its stated postulates (two sectors, global purity, a fixed window capacity, fresh thermal injection and boundary-mode locality), with internal dynamics that only changes phases and emitted quanta that never return, a black hole emits quanta that are each entangled with a partner mode kept inside, and partners are later pushed out as the hole shrinks. This result shows the inside state is always a simple product of thermal pieces, so the radiation's entropy is just the sum of the entropies of the partners still inside. That gives a rising branch, a ceiling set by the shrinking capacity, and zero entropy at the end.

*Rests on:* singularity.no-attic-derived-model, singularity.rate-models-kinematic-inputs-l-u, singularity.l-boundary-mode-locality

This is where the Page curve, the expected rise and fall of the radiation's entropy, comes in. From the same inputs, with no appeal to typicality, \[ S_R(t) \leq \min\bigl(\Sth(t),\, C(t)\bigr) \] so the radiation's entropy never exceeds its thermal value or the window's capacity, and it returns to zero at complete evaporation.

Locality (L$_E$) cannot be dropped: a small explicit example with a window rotation that is not number diagonal makes $S_R$ exceed $\Sth$.

**Theorem 13 (The envelope and the endpoint, and why boundary-mode locality is needed for them).** In the framework's model of black-hole evaporation, which assumes two sectors, overall purity, a window of the stated size and fresh thermal pairs injected at each step (the rate model's inputs (L), (U), (C), (I)), the entropy of the emitted radiation never exceeds either its thermal value or the black hole's remaining capacity, and it returns to zero once the hole has fully evaporated. This needs no assumption that the state is typical. It does need the assumption that the internal dynamics never shifts occupation numbers (boundary-mode locality, (L$_E$)): a small explicit example shows that without it the bound fails.

*Rests on:* singularity.eviction-window-thermal-product-radiation-entropy, singularity.rate-models-kinematic-inputs-l-u, singularity.l-boundary-mode-locality

The last step asks how the information gets out. At an emission event the block $A$ added to the radiation, the new quantum with the evicted qubits, satisfies \[ S(\rho_A) = h_k + \sum_{j\ \mathrm{evicted}} h_j , \qquad I(A{:}R_{<}) = 2\sum_{j\ \mathrm{evicted}} h_j \]

The new quantum carries nothing about the earlier radiation, while each evicted qubit arrives as correlated with it as a qubit can be. So in the model information returns by eviction, at the rate the capacity shrinks.

**Theorem 14 (What an event returns to the radiation).** Under the hypotheses of the evaporation model's eviction theorem, each time the model black hole emits, it releases a new quantum and may push out some interior partners. The new quantum carries no information about the earlier radiation, but each pushed-out partner is as correlated with the earlier radiation as it can be. So information comes back by eviction, at the rate the capacity shrinks, matching the known mirror-like behaviour of black holes rather than arising from scrambling.

*Rests on:* singularity.eviction-window-thermal-product-radiation-entropy, singularity.purity-correlation-transfer-recovery

## Results cited, not shown

**Fact (imported) 15 (Imported: equivalence with the Einstein equations).** Gauge theory gravity rewrites general relativity in the language of geometric algebra. This imported result says that, wherever its basic field can be inverted, its equations say exactly the same as Einstein's equations for the corresponding metric. In empty space this means the metric has vanishing Ricci curvature.

*Provenance:* A. Lasenby, C. Doran and S. Gull, Gravity, gauge theories and geometric algebra, Phil. Trans. R. Soc. Lond. A 356 (1998), 487--582., \S 4 (\S 4.3, covariant forms of the field equations), App.~C; C. Doran and A. Lasenby, Geometric Algebra for Physicists, Cambridge University Press (2003)., Ch.~13-14.

**Fact (imported) 16 (The clock inventory of the boundary modes).** The black hole's boundary modes can evolve internally in many ways, but only some of these behave like clocks ticking at a steady rate. Every such clock, however it is built from the modes, runs at one and the same rate, set by the surface gravity of the horizon. So all of them share a single period, the black hole's natural thermal cycle.

*Provenance:* Transport Lab claim scrambling.clock-inventory-boundary-modes, version 5 (T08 Lem 4.2).

**Fact (imported) 17 (Imported: the mode's modular inventory).** Each boundary mode carries a built-in clock: one element that generates boosts, counts whether the mode is occupied, and supplies the projections used to discard coherence. The algebra fixes the shape of this clock's motion but not its rate; the black hole's geometry sets the rate through its surface gravity. Continuing the clock to imaginary time gives a cycle of period $2\pi$, but that cycle lies outside the real algebra, so it is not a genuine motion of the modes.

*Provenance:* Transport Lab claim scrambling.imported-modes-modular-inventory, version 3 (T08 Fact 2.2).

**Fact (imported) 18 (The integer-holographic form, and the identification of the $16\pi$).** Once the counting time is fixed at one thermal cycle, and in a bookkeeping convention that credits each mode with one unit of entropy, the predicted packing density of modes holds exactly when a whole-number rule does: one elementary mode per four Planck-sized patches of horizon, per thermal cycle. In that convention, counting one mode per tiny cell of interior volume instead gives too many by a factor of $16\pi$, the same number that appears in the area of the horizon.

*Provenance:* Transport Lab claim scrambling.integer-holographic-form-identification, version 2 (T08 Cor 4.4).

**Fact (imported) 19 (The residue in each convention).** The number of boundary modes per unit of horizon area can be quoted in two bookkeeping conventions, which differ by a factor of $\ln 2$. Only one of them counts entropy properly, because a single fermionic mode can hold at most $\ln 2$ units of entropy. In that convention the rule is one mode per Bekenstein-Mukhanov quantum of horizon area per thermal cycle.

*Provenance:* Transport Lab claim scrambling.residue-each-convention, version 4 (T08 Prop 4.12).

**Fact (imported) 20 (The slice volume is exactly $8\pi M$ per unit Killing time, at leading order in $r_c/2M$).** Inside a black hole one can look at the surface of fixed radius near the centre where the curvature reaches the Planck scale. This result computes how much volume that surface gains per unit of the black hole's outside time. At leading order the answer is exactly eight pi times the mass, so it grows in direct proportion to the mass.

*Provenance:* Transport Lab claim scrambling.slice-volume-exactly-per-unit-killing, version 4 (T08 Prop 3.3).

**Fact (imported) 21 (The causal epoch, computed exactly).** An observer falling into a black hole from rest far away crosses the horizon and then reaches the singularity. This result computes exactly how much of the outside clock time that journey spans. The answer is about the black hole's mass in natural units, with a mild logarithmic dependence on exactly where the horizon crossing is taken to be.

*Provenance:* Transport Lab claim singularity.causal-epoch-computed-exactly, version 4 (T05 Lem 10.4).

**Fact (imported) 22 (The Euclidean rotor, and where it lies).** Thermal effects near a black hole are often explained by turning time into an angle, so that the horizon's boost becomes a rotation. This result locates that rotation precisely. It is not any real rotation available in the ordinary algebra of spacetime directions, and in particular not the rotation along the sphere that the curvature also picks out; it lives only in the complexified algebra of the radial plane, where one full turn flips the sign of every spinor.

*Provenance:* Transport Lab claim singularity.euclidean-rotor-where-it-lies, version 4 (T05 Prop 7.21).

**Fact (imported) 23 (No attic, derived in the model).** An attic would be a hidden third place, besides the black hole's interior modes and its radiation, where information could end up. In the framework's model, granting its rate-model inputs (L), (U) and (C), the bookkeeping has only those two places, so information leaving the interior must go into the radiation. Whether real black holes have no such third place is still an assumption, now stated openly.

*Provenance:* Transport Lab claim singularity.no-attic-derived-model, version 6 (T05 Prop 11.4).

**Fact (imported) 24 (Purity, correlation transfer, and recovery).** In the smallest scrambled version of the model, the radiation ends up in a pure state, so nothing is lost. Scrambling weakens the correlation within an emitted pair, but the missing correlation reappears in a three-quantum correlation. Measuring those correlations reveals which scrambling was applied, even though each quantum on its own looks thermal.

*Provenance:* Transport Lab claim singularity.purity-correlation-transfer-recovery, version 3 (T05 Prop 12.3).

**Fact (imported) 25 (The stretched singularity, and the count).** Assume premise (C1), that the quantum modes are counted on a surface inside the black hole where curvature reaches the Planck scale, and premise (C2), that they are packed at a fixed number per Planck-sized cell. For a large black hole the volume of that surface grows with outside clock time at a rate proportional to the mass, at leading order, a coincidence special to this choice of surface. As a result, the surface gains modes at a steady rate set by the black hole's Hawking temperature.

*Provenance:* Transport Lab claim singularity.stretched-singularity-count, version 7 (T05 Prop 10.6).

The trail ties black-hole entropy to a count of fermionic modes, turns the area law into a prediction for their density, and shows a model in which information returns to the radiation by eviction.

The count rests on (C1) and (C2), the prediction on the intrinsic-clock premise (IC), and the evaporation results on the rate model's inputs (L), (U), (C), (I) together with boundary-mode locality (L$_E$).
