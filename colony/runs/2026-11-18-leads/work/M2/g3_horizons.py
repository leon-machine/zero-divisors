"""Group 3: op.which-capacity, op.helicity-per-boundary-mode."""
from oplib import *

BH = 'synthesis.tube-point-clause-on-black-hole-fields-empty-for-the-horizon-flow-and-reading-dependent'
CLAUSE = 'synthesis.tube-point-clause-invariant-under-boost-commuting-symmetries'
ZER = 'synthesis.even-parity-gravity-channels-zerilli-equation-equivalent-to-the-vacuum-equations'
ODD = 'synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional'
LOW = 'synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional'
J3 = 'hawking.joint-j3-s-wave-reduction'


def capacity(b):
    b = rep(b, "decided for one-horizon fields under the costed tube-point clause adopted by Leon's decision of 31 "
               "October\"\n",
            "decided for one-horizon fields under the costed tube-point clause adopted by Leon's decision of 31 "
            "October; the black-hole tube-point result and Leon's decision of 18 November (the clause restated: "
            "the rotations commuting with the wedge's boost, the boost being the horizon's Killing flow; silent on "
            "black-hole fields)\"\n")
    b = set_field(b, 'statement', 'why', [
        r"Restated 18 November, after the black-hole result and Leon's decision of that day. A wedge's boost-KMS "
        r"data together with the ascent pair fix the compatible tube point up to one scale $\rho$, and the "
        r"capacity a state reads is the same at every tube point. The adopted costed clause, as restated, asks "
        r"that a state's tube point be invariant under the rotations commuting with its wedge's boost, the boost "
        r"being a positive multiple of the horizon's Killing flow. In the de Sitter field it gives "
        r"$\rho^{2} = 12/\Lambda$, and that result stands on this reading. For $\Lambda \le 0$ no tube point is "
        r"fixed and $\rho$ stays free, as before. On the Schwarzschild exterior and on the static region of "
        r"Schwarzschild-de Sitter no observer meets the condition: the clause is silent there and $\rho$ stays "
        r"free. So the two cases that were open, fields "
        r"with more than one horizon and the Schwarzschild field, are answered under the present premises: "
        r"$\rho$ is a free datum there, and the choice between a tube point per observer and per horizon is not "
        r"reached. What is left: whether a further premise is to fix $\rho$ on those fields. The candidates that "
        r"coincide with the clause in the de Sitter field, the largest normalised norm of the boost generator and "
        r"free fall, are one condition on these fields; they select no observer on Schwarzschild and one radius, "
        r"$r_{0}^{3} = 3M/\Lambda$, in Schwarzschild-de Sitter, with one scale per horizon. They are not "
        r"adopted."])
    b = append_known(b,
        r"(18 November.) The black-hole fields (" + cr(BH) + r", proved). The boost itself fixes no compatible "
        r"tube point in any field, so the condition is read for the rotations among the symmetries commuting with "
        r"the boost. Every $\so(3)$ of bivectors commuting with the boost is the transverse rotation algebra of "
        r"one de Sitter tractor, and a compatible tube point is fixed by it exactly when its observer is a fixed "
        r"point of those rotations. In a gauge in which the wedge's boost generates a positive multiple of the "
        r"horizon's Killing flow and the rotations act by bivectors, a region whose rotation orbits are "
        r"two-spheres has no such observer: on the Schwarzschild exterior, and on the static region of "
        r"Schwarzschild-de Sitter for either horizon, the condition is met by no observer. The clause as first "
        r"worded asked only that the boost generate a symmetry. In a gauge twisted by a rotation about one axis "
        r"that grows with the rapidity the boost generates the horizon's flow plus a rotation, and the observers "
        r"on the axis meet the condition at every scale, in these fields (given that they have no symmetries "
        r"beyond the horizon's flow and the rotations, which is cited from memory) and in the de Sitter field "
        r"too; so the outcome depended on a reading that the wording did not fix. Under a third reading, in which "
        r"only "
        r"symmetries acting by bivectors count, the condition can be made empty (argued, not computed). The norm "
        r"and free-fall candidates are one condition, a stationary lapse, $f' = 0$: it has no solution on "
        r"Schwarzschild, where the normalised norm increases to its supremum $1/\kappa$ and attains it at no "
        r"radius (the store had argued this without computing it); in Schwarzschild-de Sitter it holds at one "
        r"radius $r_{0} = (3M/\Lambda)^{1/3}$, the same for both horizons, where the two horizons give scales in "
        r"the ratio $\kappa_{b}/\kappa_{c}$ ($\tfrac85$ in the stored sample), neither equal to the inverse "
        r"surface gravity. Leon's decision of 18 November: the clause is restated to the first reading, "
        r"invariance under the rotations commuting with the wedge's boost, the boost being a positive multiple of "
        r"the horizon's Killing flow (" + cr(CLAUSE) + r", as restated); the de Sitter result stands on that "
        r"reading; on the Schwarzschild exterior and on the static region of Schwarzschild-de Sitter no observer "
        r"meets the condition, the clause is silent there, and $\rho$ stays free. The sentences above that the "
        r"clause decides fields with one horizon are superseded: Schwarzschild is a field with one horizon that "
        r"the clause does not decide.")
    b = set_attack_item(b, 0,
        r"Answered (18 November; " + cr(BH) + r", clause (vi), with Leon's decision of that day). The item "
        r"asked to compute, in Schwarzschild-de Sitter, the tube points the clause fixes for each horizon's "
        r"wedge, and to decide between assigning the observer's tube point per observer and per horizon, or to "
        r"show that the premises leave the choice free. Under the clause as restated no observer of the static "
        r"region has a tube point fixed by the rotations, for either horizon: the clause is silent, $\rho$ stays "
        r"free, and the choice between per observer and per horizon is not reached. What remains: the norm and "
        r"free-fall candidates select the one radius $r_{0}^{3} = 3M/\Lambda$, the same for both horizons, with "
        r"one scale per horizon in the ratio of the surface gravities (a foot per observer and a scale per "
        r"horizon); by the Tolman relation, cited from memory, that observer is also the coldest for each "
        r"horizon. They are not adopted, and adopting them would be a further premise.",
        expect_start='Two horizons:')
    b = set_attack_item(b, 1,
        r"Answered (18 November; the same result, clause (v)). The item asked to compute the compatible tube "
        r"points fixed by the Schwarzschild field's symmetries commuting with the horizon's boost (time "
        r"translation and rotations) in a gauge adapted to the tube-point machinery, and to test whether a finite "
        r"$\rho$ is selected. In every gauge adapted to the horizon's flow no observer of the exterior has a tube "
        r"point fixed by the rotations, and neither the clause nor the norm and free-fall candidates select a "
        r"finite scale: each is met only in the limit $r \to \infty$. Under the clause as restated $\rho$ is free "
        r"on the Schwarzschild exterior.",
        expect_start='Schwarzschild: compute')
    b = set_field(b, 'success', 'entities', [
        r"Restated 18 November. Under the present premises $\rho$ is a free datum of the state on the "
        r"Schwarzschild exterior and on the static region of Schwarzschild-de Sitter, which is one of the three "
        r"outcomes first asked for. What would close the problem: a decision, with its grounds, on whether a "
        r"further premise fixes the tube point on black-hole fields (the norm and free-fall rule is the stored "
        r"candidate), or a derivation of such a rule; and the compatibility condition derived as a property of "
        r"the continuum I-state."])
    b = add_entities(b, [BH])
    return b


def helicity(b):
    b = rep(b, "the spin-2 horizon-channel result and Leon's decisions of 9 November (second pass)\"\n",
            "the spin-2 horizon-channel result and Leon's decisions of 9 November (second pass); the even-parity "
            "spin-2 result accepted 18 November\"\n")
    b = rep(b,
            "    What is open is joint J3: convert the helicity lift from an assembly to a\n"
            "    theorem by proving the identification of each $(\\omega, \\ell, m, s)$\n"
            "    channel with a two-dimensional mode, at the horizon.\n",
            wrap(
                r"What is open is joint J3: convert the helicity lift from an assembly to a theorem. Its "
                r"channel-reduction part, the identification of each $(\omega, \ell, m, s)$ channel with a "
                r"two-dimensional mode at the horizon, is derived for spins $0$, $\tfrac12$ and $1$ and, since 18 "
                r"November, for both parities of spin $2$ on oscillating channels with $\ell \ge 2$, in the "
                r"static frame and given facts of harmonic analysis that are cited from memory. What remains of "
                r"J3: the current-boson identification and the partial-wave lift, which stay premise, and those "
                r"cited facts.", 4) + '\n')
    b = append_known(b,
        r"(18 November.) Spin $2$, even parity, is proved in both directions (" + cr(ZER) + r"). The first-order "
        r"Ricci vectors of the even-parity field in the Regge-Wheeler gauge are computed in closed form as "
        r"identities in the radius and the polar angle together, for an arbitrary angular function; the same "
        r"computation makes the stored odd-parity closed forms identities in both variables, so the degree bound "
        r"argued there is no longer needed. From any function $\Phi$ a field is written down whose vacuum "
        r"equations are explicit differential operators applied to the Zerilli operator on $\Phi$, with "
        r"Zerilli-Moncrief function $(\lambda + 1)\Phi$: every solution of the Zerilli equation is the master "
        r"function of a vacuum solution, with no condition on its time dependence. That is the cited fact (C3) "
        r"of " + cr(ODD) + r", now proved. On a channel with $\partial_{t}^{2} = -\omega^{2}$, $\omega^{2} \ne 0$, "
        r"the vacuum equations amount to a first-order system and one algebraic relation, they imply the Zerilli "
        r"equation identically, and the field is the one rebuilt from its own master function; so the master "
        r"function is a bijection between the even-parity vacuum solutions of the channel in the Regge-Wheeler "
        r"gauge and the solutions of the Zerilli equation in the channel. Hence each even-parity channel with "
        r"$\ell \ge 2$ and real nonzero frequency is a two-dimensional mode at the horizon in the static frame, "
        r"as the odd-parity ones are, given the cited facts (C1) (completeness of the tensor harmonics, and that "
        r"the axisymmetric representative suffices) and (C2) (reachability of the Regge-Wheeler gauge), which "
        r"stay cited from memory. The sample-point clause (3) of the stored result is superseded on oscillating "
        r"channels only: off them the implication from the vacuum equations to the Zerilli equation stays as "
        r"stored, computed at sample points. With this the channel-reduction clause of J3 (" + cr(J3) + r") is no "
        r"longer needed for the even-parity channels of spin $2$ on oscillating channels, once (C1) and (C2) are "
        r"granted; the current-boson identification and the partial-wave lift are not derived and stay premise. "
        r"Not attempted: $\ell = 0, 1$, charts regular across the horizon, and the identification of the partial "
        r"waves from the fuzzy sphere.")
    b = set_attack_item(b, 0,
        r"Spin $2$, what remains (restated 18 November; the even-parity reduction is proved in both directions, "
        + cr(ZER) + r", the odd-parity reduction is derived, " + cr(ODD) + r", and the reductions for spins $0$, "
        r"$\tfrac12$ and $1$, " + cr(LOW) + r"). Done since the restatement of 9 November: the even-parity "
        r"converse, that every solution of the Zerilli equation in an oscillating channel is the master function "
        r"of a vacuum solution, with the implication from the vacuum equations proved identically on oscillating "
        r"channels; and the degree bound of the odd-parity identity, which is no longer needed. What remains: "
        r"the harmonic-analysis inputs cited from memory, to be derived or imported as Facts ((C1) completeness "
        r"of tensor harmonics and (C2) reachability of the Regge-Wheeler gauge for spin $2$; completeness of "
        r"spherical and spinor harmonics and the exact/co-exact split of one-forms on $S^{2}$ for the lower "
        r"spins); the implication from the vacuum equations to the Zerilli equation off oscillating channels, "
        r"which stays at sample points; the cases $\ell = 0, 1$ (changes of mass, spin and gauge); and the "
        r"statement in charts regular across the horizon. The current-boson identification and the partial-wave "
        r"lift stay premise.",
        expect_start='Spin $2$, what remains (restated 9 November, second pass;')
    b = add_entities(b, [ZER])
    return b


if __name__ == '__main__':
    apply([('op.which-capacity', capacity), ('op.helicity-per-boundary-mode', helicity)])
