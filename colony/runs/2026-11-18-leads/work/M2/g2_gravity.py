"""Group 2: op.gravitational-field-at-null-momentum, op.einstein-from-the-field-theory."""
from oplib import *

FREE = 'synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints'
MAXW = 'synthesis.two-dimensional-lattice-maxwell-coulomb-slaved-field-fails-and-string-dressed-detection-commutes'
SIG = 'synthesis.with-a-coupled-device-the-slaved-field-failure-is-a-first-order-signal-and-a-survey-finds-no-stored-bound'
SLAVED = 'synthesis.field-slaved-to-an-operator-source-does-not-commute-at-spacelike-separation'
RATE = 'synthesis.gravitational-pair-production-from-the-operator-source-at-first-order'


def null_momentum(b):
    b = rep(b, '  status: open\n', '  status: reformulated\n')
    b = rep(b, "and Leon's decision of 18 November (record as open; no position changed)\"\n",
            "and Leon's decision of 18 November (record as open; no position changed); the three results on the "
            "field accepted later on 18 November (the free directions at null momentum, the lattice Maxwell model, "
            "the first-order signal) and Leon's decision of that day (the series requires no signal outside the "
            "light cone; how the requirement is met is this problem)\"\n")
    b = set_field(b, 'statement', 'why', [
        r"Restated 18 November, after Leon's decision of that day. The series requires that no signal pass "
        r"outside the light cone (conventions, section ``Gravity and the graviton'', the requirement of 18 "
        r"November 2026). In the stored lattice model a field with no variables of its own, slaved to the "
        r"matter's operator source, fails to commute with the source's later detection at spacelike separation ("
        + cr(SLAVED) + r"), and under the hypothesis that a classical device couples to such a field the failure "
        r"is a signal of first order (" + cr(SIG) + r"; its transfer to the gravitational field is argued). So, by "
        r"that decision, a gravitational field with no variables of its own is not the full account of the "
        r"field. The series holds no quantum of the gravitational gauge field and posits none. At first order the "
        r"field is fixed by its source at every non-null momentum; at a null momentum two directions, the "
        r"transverse trace-free ones, are not, and four of the ten first-order equations are constraints (" +
        cr(FREE) + r"). Open: how the requirement is met. Whether the two free directions carry states or "
        r"variables of their own is not decided, in either sense, and no other way of meeting the requirement is "
        r"stored. Say how the series' gravitational field meets the requirement, and restate the burst baseline "
        r"and the stored readings that name a graviton to match."])
    b = append_known(b,
        r"(18 November, second pass.) A decision and three results. The decision (Leon, 18 November): the series "
        r"requires no signal outside the light cone, so the slaved field is not the full account of the "
        r"gravitational field; how the requirement is met is this problem, and no quantum is posited. The field "
        r"at null momentum (" + cr(FREE) + r"): at every nonzero null momentum the kernel of the first-order "
        r"Einstein map is the displacements together with the two transverse trace-free maps (proved); the map is "
        r"symmetric for the stored pairing, so the first-order equation is solvable there exactly for sources with "
        r"no transverse trace-free part; the pole of the first-order curvature on the cone lies in those two "
        r"components only, and the stored bilinear restricted to the cone is a sum of two squares, one for each; "
        r"four of the ten equations carry no second derivative in the time of a frame, the constraints (all "
        r"proved); the pseudoscalar exchanges the curvatures of the two directions, so they are one mode over "
        r"$\mathrm{span}\{1, I_{4}\}$ per null momentum, as for the stored photon (computed). Nothing in it "
        r"decides whether the series gives those solutions any existence of their own. The lattice Maxwell model, "
        r"as restated after review (" + cr(MAXW) + r"): a lattice Maxwell field in two space dimensions with a "
        r"Gauss constraint and a scalar charge, exactly solvable, and not a model of spin two. With no variable "
        r"of its own the constraint fixes only the divergence of the field: the static slaved field, the Coulomb "
        r"one, fails to commute with the detection on $76$ of the $82$ links off the string (proved); a "
        r"string-shaped slaved field satisfies the constraint and commutes off the string at one time, but is not "
        r"a static solution (proved); with an exact cone the retarded slaved field fails at $878$ of $2750$ "
        r"spacelike events, every one in the forward cone of the source event and none spacelike to the source "
        r"(computed); and a slaved field obeying the field equation and fitted to one detection's time commutes "
        r"with that detection at all spacelike events and fails for a detection at another time (computed for two "
        r"detection times). With transverse variables and canonical commutators a "
        r"detection dressed by one Weyl operator commutes with the field exactly off the support of the dressing: "
        r"the string dressing gives commutation at all $2750$ spacelike events and the Coulomb dressing does not; "
        r"dressings by sums of such operators are not treated. In one space dimension there is no transverse part "
        r"and no failure outside the interval between the two sites. For the gravitational field the reading is "
        r"argued by analogy and settles nothing. The signal (" + cr(SIG) + r"): under its hypothesis (D), that a "
        r"classical device couples to the field by the model's own coupling with unitary evolution, the stored "
        r"commutator is a change of the detection probability of first order in the device's strength (proved); "
        r"its coefficient is nonzero at $172$ of the $502$ spacelike events of the stored grid, and at the $32$ of "
        r"them not later than the detection the device changes the detection probability (computed). "
        r"The slaved model with the device is unitary, so unitarity does not imply commutation (proved); with the "
        r"free part of the stored model the first-order term vanishes (proved). The device is a number, so no "
        r"floor on localisation hides the signal. Its gravitational size within the light-crossing time is at "
        r"most $\Phi_{w} = (Gm_{A}m_{B}/\hbar c)\,D\,|1/r_{1} - 1/r_{2}|$, half of that in the formulation that "
        r"does not count the pair's energy twice (argued, its numbers computed): about $1.3 \times 10^{-13}$ in "
        r"the proposed experiments, ten orders below the registered threshold, and of order one for a source of "
        r"about $190$ kg at one metre against a superposed mass of $10^{-14}$ kg. A survey of the stored locality "
        r"statements and of the cutoff and local-horizon premises, with its scope listed, found none that implies "
        r"commutation for the gravitational field, none that bounds the failure or makes it unobservable, and no "
        r"other condition in its place; that is the outcome of a survey, not a theorem about the store.")
    b = set_attack_item(b, 0,
        r"Answered (18 November; " + cr(SIG) + r"). The item asked whether any stored premise, or the unitarity "
        r"behind the registered prediction, implies that the gravitational field commutes with matter observables "
        r"at spacelike separation, and if not what the series puts in its place. No stored premise was found that "
        r"implies it (a survey with its scope listed, not a theorem about the store). Unitarity does not: the "
        r"slaved model with a coupled device is unitary (proved), and under the hypothesis (D) of that result the "
        r"failure is then a signal of first order. What the series puts in its place is decided (Leon, 18 "
        r"November; stated in the conventions): no signal outside the light cone. What remains is how that "
        r"requirement is met, the statement above.",
        expect_start='State the condition:')
    b = set_attack_item(b, 1,
        r"Answered (18 November; the same result). The item asked whether the cutoff premises (C1) and (C2), or "
        r"the finite count of boundary modes, supply a bound on localisation under which the model's failure "
        r"cannot be observed. No floor on localisation is relevant: the first-order signal needs no probe with a "
        r"wave packet, the device being a number, and a floor at the Planck length would change it only at the "
        r"relative order of that length over the separation of the paths; the floor of the working notes of 12 "
        r"October belongs to a different effect of second order, the reading of the which-path record by a probe. "
        r"No stored bound was found: the cutoff premises place modes on a surface that does not exist in the "
        r"configuration of the experiment (computed), clause (Loc) of the local-horizon premise is an entropy "
        r"density with no mode count, and the survey "
        r"found no stored statement on the localisation of a body or on a product of two masses. The signal's "
        r"size is set by $Gm_{A}m_{B}/\hbar c$: about $10^{-13}$ in the proposed experiments, and of order one "
        r"near $190$ kg at a metre against a superposed mass of $10^{-14}$ kg (argued, under (D)).",
        expect_start='The localisation floor:')
    b = set_attack_item(b, 2,
        r"Answered (18 November; " + cr(MAXW) + r", as restated after review). The item asked to repeat the "
        r"model with the constraint structure of the gauge field: an instantaneous part fixed by a constraint, "
        r"and dressed observables. Done in an exact lattice Maxwell model in two space dimensions with a scalar "
        r"charge; it has no spin two. With no variable of its own, the constraint does not fix the field: the "
        r"Coulomb slaved field fails at equal time, the retarded slaved field fails at spacelike events in the "
        r"source's forward cone, and a slaved field obeying the field equation that is fitted to one detection's "
        r"time commutes with that detection and fails for a detection at another time (computed). With transverse "
        r"variables, a detection dressed by one Weyl "
        r"operator along a string commutes with the field at every spacelike event. What remains: the same "
        r"question for the gravitational constraints, where the reading is argued by analogy only.",
        expect_start='Repeat the model with the constraint structure')
    b = set_attack_item(b, 3,
        r"Restated (18 November; " + cr(FREE) + r"). The count is made: two free directions at each null "
        r"momentum, the transverse trace-free ones, forming one mode over $\mathrm{span}\{1, I_{4}\}$, and four "
        r"constraint equations. If the two directions were given states in the way the photon is, the "
        r"construction would be that of the stored photon modes (" + cr('field-theory.fock-space-maxwell-modes') +
        r"), a canonical pair on polynomials and not an element of a floor of the tower (argued); whether they "
        r"are given states is not decided. The burst ratio is $D = (2 + g_{\mathrm{h}} + o)/(1 + g_{\mathrm{s}})$, "
        r"with $g_{\mathrm{h}}$ the hole's emission into the two directions and $g_{\mathrm{s}}$ that of the "
        r"standard expectation: $(2 + g + o)/(1 + g)$ if the two components emit as in standard physics, and "
        r"$(2 + o)/(1 + g)$ if they do not (computed from " + cr('synthesis.dimmed-burst-time-rescaled-copy') +
        r"). So the earlier wording of this item, ``restate the burst baseline with $g = 0$'', is corrected: "
        r"$D = 2 + o$ is the ratio to a baseline from which the term has also been removed, which is not the "
        r"standard expectation. The two options differ by $g/(1 + g)$, about $0.02$ at $g = 2/98$ (a hole "
        r"emitting only massless neutrinos, photons and the two components; the fraction is read from the "
        r"abstract of Page's 1976 paper), and the prediction's kill condition, an undimmed burst, does not "
        r"distinguish them. What remains: which option holds, which follows from how the requirement is met; "
        r"then the wording of the burst prediction and of the conventions.",
        expect_start='If a free part is admitted:')
    b = set_field(b, 'success', 'entities', [
        r"A stored statement of how the series' gravitational field meets the requirement of no signal outside "
        r"the light cone, derived or adopted as a premise with its grounds; with it the status of the two free "
        r"directions at null momentum, and the burst baseline and the conventions restated to match."])
    b = add_entities(b, [FREE, MAXW, SIG])
    return b


OLD_ITEM = ('    - "The trace-free channel: derive from the series\' field theory that the trace-free stress is a '
            'source, that is, that the gravitational field is varied off the Weyl-flat class, or show that clause '
            'independent of the series\' premises."\n')


def einstein(b):
    b = rep(b, "and Leon's decisions of 2 November (the clause recorded as: the trace-free stress is a source)\"\n",
            "and Leon's decisions of 2 November (the clause recorded as: the trace-free stress is a source); the "
            "null-momentum result accepted 18 November (which stored results test the trace-free channel)\"\n")
    new = '    - >-\n' + wrap(
        r"The trace-free channel: derive from the series' field theory that the trace-free stress is a source, "
        r"that is, that the gravitational field is varied off the Weyl-flat class, or show that clause "
        r"independent of the series' premises. Narrowed (18 November; " + cr(FREE) + r", clause (vii)): the "
        r"operator source of the stored rate result (" + cr(RATE) + r", hypothesis (OS)) takes the whole stress "
        r"map as source, so it assumes the clause at the level of operators and does not derive it. Among the "
        r"stored results the static coupling and the registered entangling phase do not test the clause: for two "
        r"bodies at rest the stored bilinear splits as $\tfrac23 - \tfrac16$ between its trace-free and trace "
        r"parts and equals the trace-only bilinear normalised to Newton's law (proved). The production rate does "
        r"test it: with a trace-only source a copy of the Standard Model's content would be produced at "
        r"$15360/1519247$, about one percent, of the stored rate, and massless vectors not at all (computed, "
        r"given (OS)). Neither a derivation of the clause nor its independence is obtained.", 6) + '\n'
    b = rep(b, OLD_ITEM, new)
    b = add_entities(b, [FREE])
    return b


if __name__ == '__main__':
    apply([('op.gravitational-field-at-null-momentum', null_momentum),
           ('op.einstein-from-the-field-theory', einstein)])
