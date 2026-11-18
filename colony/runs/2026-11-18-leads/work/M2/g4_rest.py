"""Group 4: op.positivity-of-values, op.curvature-coupling-across-subjects,
op.graviton-rate-as-classical-field-process, op.island-dictionary, op.order-four-anomaly-and-sixteen."""
from oplib import *

ADD = 'synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear'
PELL = 'synthesis.pell-values-are-the-running-maxima-of-the-pure-state-chsh-values-over-the-rationals'
TWOVAL = 'synthesis.no-two-valued-weights-on-the-atoms-of-two-modes-the-even-subalgebra-admits-them'
LOCAL = 'synthesis.local-weights-give-the-chsh-bound-and-do-not-fix-positivity-of-values'
HEAT = 'synthesis.heating-coefficients-across-curvature-couplings-and-on-the-chains-bath'
PS = 'synthesis.seeding-remainder-excludes-perturbative-pati-salam'
ROT = 'synthesis.rotation-weights-of-pair-sources-fix-the-channel-weights-and-give-no-trace-at-nonzero-weight'
FREE = 'synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints'
RET = 'scrambling.return-delay-scrambling-log-recovered'
SPREAD = 'scrambling.spreading-law-chaos-bound-saturated'


def positivity(b):
    b = rep(b, "(the stored Born account rests on (P) and sharpness in place of the imported envariance argument)\"\n",
            "(the stored Born account rests on (P) and sharpness in place of the imported envariance argument); "
            "the additive-weights and running-maxima results accepted 18 November\"\n")
    b = append_known(b,
        r"(18 November.) Two items are settled. Additive weights (" + cr(ADD) + r"; proved, with four finite "
        r"exact computations carried by its check): on the algebra of two modes over $\Q$ every function on the "
        r"self-adjoint idempotents that adds on orthogonal pairs, with values in any rational vector space and "
        r"with no sign, normalisation or continuity condition, is the restriction of a linear functional. So the "
        r"question of Gleason type is answered positively and in a stronger form: linearity does not need the "
        r"sign condition. With non-negativity and normalisation the weights are exactly the restrictions of the "
        r"states of (P) to the projectors, so of what (P) asserts about projectors only the sign is not implied "
        r"by additivity. (P) also gives values to elements whose spectral projectors are not rational, the CHSH "
        r"element among them, and that those values are the linear extension remains part of (P). The stored "
        r"functional of value $4$ restricts to an additive weight and takes the value $-\tfrac14$ on one atom. On "
        r"the atoms of rational unit vectors alone the statement fails (a parity weight, proved there; a "
        r"two-valued one is prior art). No premise about values is used, nothing in it derives (P), and more than "
        r"two modes are not treated. Prior art, read through abstracts and a summary only and to be confirmed "
        r"from the papers: Mushtari (2001) poses the question for non-negative measures on the rational "
        r"orthogonal projections of $\Q^{n}$ as open (his Problem G) and gives a two-valued measure on the unit "
        r"atoms of $\Q^{4}$; Mushtari (1995, 1998) proves the trace form for signed measures on all rational "
        r"idempotents, a larger domain from which the statement does not follow. Running maxima (" + cr(PELL) +
        r"; proved): for every $D \ge 1$ the largest pure-state value of denominator at most $D$ is the Pell "
        r"value whose denominator is the largest Pell denominator not above $D$, attained only there, so the "
        r"running maxima of the pure-state values are exactly $2, \tfrac{14}{5}, \tfrac{82}{29}, "
        r"\tfrac{478}{169}, \tfrac{2786}{985}, \dots$ for every denominator. This is a statement about pure "
        r"states at the stored settings; among all state values the Pell values are not the running maxima "
        r"(stored). The sentence above that linearity is undecided is superseded.",
        nextkey='attack')
    b = set_attack_item(b, 4,
        r"Done (18 November; " + cr(ADD) + r"): yes, and without the sign condition. Every weight on the "
        r"projectors with rational coefficients of two modes that adds on orthogonal projectors is the "
        r"restriction of a linear functional; with non-negativity and normalisation it is the restriction of "
        r"exactly one state of (P). The item as posed: decide whether non-negative additive weights on the "
        r"projectors with rational coefficients of two modes (size four over $\Q$) are restrictions of linear "
        r"functionals, a statement of Gleason type; two-valued weights are excluded there (" + cr(TWOVAL) +
        r"). Not done: more than two modes; other ordered fields.",
        expect_start='Decide whether non-negative additive weights')
    b = set_attack_item(b, 5,
        r"Done (18 November; " + cr(PELL) + r"): the Pell values are the running maxima of the pure-state values "
        r"for every denominator (proved). The item as posed: decide whether the pure-state values of the sector "
        r"that meet the denominator law with equality are the running maxima among pure-state values for every "
        r"denominator; this had been computed for denominators up to $400$ in the stored check and below $1200$ "
        r"in a separate computation.",
        expect_start='Decide whether the pure-state values')
    b = add_attack_item(b,
        r"New (18 November). Which projectors can label a record: every projector with rational coefficients "
        r"that is self-adjoint for the split, or only products of local outcomes? On the first reading, with "
        r"weights that are non-negative, do not depend on the context and add on orthogonal projectors, the "
        r"weights on two modes are the restriction of one state of (P), by the result on additive weights, and "
        r"what (P) still assumes there is the value of elements whose spectral projectors are not rational. On "
        r"the second, (P) is not fixed by such weights on two modes, by the stored one-parameter family (" +
        cr(LOCAL) + r"). The choice is a reading of the residual postulate and is Leon's; it is tied to the "
        r"parity item above, since the theorem uses projectors that are odd under the total parity (argued). "
        r"With it: more than two modes, where a first step is to show that any two rational vectors of "
        r"$\Q^{2^{\ell}}$ lie in a four-dimensional rational subspace similar to the standard one, which needs "
        r"an imported fact on the representation of positive rationals by positive definite rational forms of "
        r"dimension at least four (named as the candidate, not checked); and the prior art, to be read before "
        r"the result is described as new: Mushtari, Lobachevskii J. Math. 9 (2001) 47, so far read through a "
        r"summary only.")
    b = add_entities(b, [ADD, PELL])
    return b


def curvature(b):
    b = rep(b, "the tree-level value 0 as the stored reading for the rung doublets)\"\n",
            "the tree-level value 0 as the stored reading for the rung doublets); the heating-coefficients result "
            "accepted 18 November\"\n")
    b = append_known(b,
        r"(18 November.) The heating of the dark towers (" + cr(HEAT) + r"). The scalar channels of the stored "
        r"production rate carry $\tau = (1 - 6\xi_{R})^{2}$, and the couplings enter a summed coefficient only "
        r"through the product of the trace sums of the bath and of the produced content (proved); vectors and "
        r"fermions are blind to them. The heating does not constrain the open datum (computed). For the Standard "
        r"Model's bath and a copy of its content the two stored readings, $0$ and $\tfrac16$, differ by $0.11$ "
        r"percent in the coefficient and move no stated figure. The tilt window's coupling on every doublet "
        r"would raise the coefficient about sixfold and leave the four-content clause of the stored Pati-Salam "
        r"exclusion (" + cr(PS) + r") undecided, the crossing of its threshold lying inside the window while at "
        r"central inputs the threshold is not reached; that case is the one-field reading, which the result of "
        r"10 November excludes on other grounds. On the bath of the stored chain between the intermediate and "
        r"unification scales ($188$ real scalars, $48$ Weyl fields and $21$ vectors under Hypothesis (S)) the "
        r"bath enters twice, in the coefficient and in the threshold through the expansion rate and the entropy, "
        r"and the margins of the stored exclusion rise, from above $2.2$ and $1.5$ to about $2.83$ and $1.96$. So "
        r"the stored exclusion, computed with the Standard Model's bath, is conservative on its own chain, and "
        r"the curvature couplings of the chain's scalars do not decide it at either stored assignment, $0$ or "
        r"$\tfrac16$, even for four copies of the chain's own content, a case constructed in that result. Not "
        r"treated: the tilt window's coupling on the chain's scalars. The chain's scalars above the intermediate "
        r"scale have no stored coupling.")
    b = add_entities(b, [HEAT])
    return b


def graviton_rate(b):
    b = rep(b, "the search of the store for the word made the same day\"\n",
            "the search of the store for the word made the same day; the operator-source rate result of 18 "
            "November 2026 and, accepted later that day, the rotation-weights result (no trace part of the "
            "fermion channel from the stored trace statement)\"\n")
    b = append_known(b,
        r"(18 November, second pass.) The trace part of the fermion channel at the next order (" + cr(ROT) +
        r"). The tree-level source of a particle and antiparticle of one chiral fermion has rotation weight one "
        r"about the pair's axis, and a source of nonzero weight has no trace (proved; the rule is elementary and "
        r"all its content is the hypothesis on the weight). A term of the field equation built from the scalar "
        r"curvature changes only the product of two traces (proved), and the stored trace-anomaly statement takes "
        r"that form at first order (argued). So the part of the next-order correction that comes from the stored "
        r"trace statement gives the fermion channel, and the vector channel, no trace part; its first effect is "
        r"on the trace term of scalars to scalars, at relative order $s/\bar{M}_{P}^{2}$, which is third order in "
        r"$G$ in the rate ($G^{3}T^{10}$), an order that no stored result uses (argued). The fermion coefficient "
        r"is not "
        r"thereby unchanged at that order: the trace-free part of the vacuum's response rescales every spin-two "
        r"weight by one common factor and is not computed. That the two-quantum element of the stress of an "
        r"interacting theory keeps weight one is argued from the helicity of the state, not proved. The same "
        r"decomposition gives the nine channel weights $(\pi/180)(c_{i}c_{j} + 5\tau_{i}\tau_{j})$ from one norm "
        r"and one trace per source, with no angular integration, in agreement with the stored weights (proved). "
        r"The burst baseline: the ratio under each option is computed (" + cr(FREE) + r", clause (viii)). If the "
        r"hole does not emit into the two free directions the ratio against the standard expectation is "
        r"$(2 + o)/(1 + g)$; the value $D = 2 + o$ given above for $g = 0$ is the ratio to a baseline from which "
        r"the term has also been removed, which is not the standard expectation. Which option holds is with "
        r"op.gravitational-field-at-null-momentum.")
    b = append_to_attack_item(b, 3,
        r"(18 November: the ratio under each option is computed; with no emission into the two free directions "
        r"it is $(2 + o)/(1 + g)$ against the standard expectation, and $D = 2 + o$ only against a baseline from "
        r"which the term has also been removed. The decision between the options is with "
        r"op.gravitational-field-at-null-momentum, item 4.)",
        expect_start='The burst baseline: decide from the result')
    b = add_entities(b, [ROT])
    return b


def island(b):
    b = append_known(b,
        r"(18 November.) The return delay $T_{\mathrm{return}} \approx 4M\ln S$ (" + cr(RET) + r") is listed "
        r"here as the timing half of the question of how information returns: it stays conjectured, an estimate "
        r"in modular time with no proved core as a statement about the return of information, since the stored "
        r"theorems that the spreading law rests on (" + cr(SPREAD) + r") do not reach it.")
    b = add_entities(b, [RET])
    return b


def order_four(b):
    b = append_to_attack_item(b, 2,
        r"(18 November: a link from this count to the eigenbundle class of "
        r"op.eigenbundle-class-of-degenerations through real K-theory was tested and is a resemblance, not a "
        r"derivation: the eigenbundle class of the projective wall $\mathbb{RP}^{5}$ has order eight, order "
        r"sixteen first occurring on $\mathbb{RP}^{8}$ (computed, not stored), while the sixteen here is the "
        r"stored $\tfrac{1}{16} = \tfrac12 \cdot \tfrac18$, the eight a spinor count in six dimensions and not "
        r"the order of that class (argued).)",
        expect_start='Answered in part (16 November). The count on')
    return b


if __name__ == '__main__':
    apply([('op.positivity-of-values', positivity),
           ('op.curvature-coupling-across-subjects', curvature),
           ('op.graviton-rate-as-classical-field-process', graviton_rate),
           ('op.island-dictionary', island),
           ('op.order-four-anomaly-and-sixteen', order_four)])
