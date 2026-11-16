"""Maintainer pass 2026-11-16 (spectrum): edits to store/open_problems.yaml, items M2(d) and M3.
Exact-string replacements inside the two problems' blocks; every replacement must match once."""
import re, sys, yaml
PATH = '/home/claude/phys-graph/store/open_problems.yaml'
P1 = 'synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit'
P2 = 'synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary'
P3 = 'synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape'
P4 = 'synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta'
def cr(x): return '\\claimref{' + x + '}'

text = open(PATH).read()

def block(text, oid):
    i = text.index('\n- id: ' + oid + '\n') + 1
    m = re.search(r'\n(?:- id: |# -{10,})', text[i + 5:])
    j = i + 5 + m.start() + 1 if m else len(text)
    return i, j

def rep(b, old, new):
    assert b.count(old) == 1, (old[:70], b.count(old))
    return b.replace(old, new)

# ------------------------------------------------------------------ op.descent-state-and-spectrum
i, j = block(text, 'op.descent-state-and-spectrum')
b = text[i:j]

# source
b = rep(b, "and Leon''s decision of 10 November keeping no mechanism'\n",
           "and Leon''s decision of 10 November keeping no mechanism; the slice-datum results and Leon''s decisions of 16 November'\n")

# known: qualifiers on the earlier sentences
b = rep(b, "    The finite-range bound: a deposit whose correlations have range $R$ gives $\\Delta^{2}(k) \\le\n",
           "    The finite-range bound: a deposit whose $\\zeta$ has correlations of range $R$ gives $\\Delta^{2}(k) \\le\n")
b = rep(b, "at every reheating temperature; a deposit of finite range at\n    the Hubble or thermal length gives $n_{s} - 1 \\to 3$; active sources",
           "at every reheating temperature; a deposit whose $\\zeta$ has finite\n    range at the Hubble or thermal length gives $n_{s} - 1 \\to 3$ (a matter deposit of finite range has such a\n    $\\zeta$ under the reading (FR) of the 16 November paragraph below, and not under (UE)); active sources")
b = rep(b, "gives $n_{s} - 1 = 2\\Delta$: finite range\n    gives $3$,",
           "gives $n_{s} - 1 = 2\\Delta$: finite range of\n    $\\zeta$ gives $3$,")
b = rep(b, "and hotter ones are thermal deposits of finite range (argued).",
           "and hotter ones are thermal deposits of finite range (argued; of finite range in $\\zeta$ under (FR)).")
b = rep(b, "(energy spread $c_{k} \\le 1.31$), the shot\n    term at the pivot is below $10^{-77}$, while a sparse",
           "(energy spread $c_{k} \\le 1.31$), the shot\n    term of the contrast at the pivot is below $10^{-77}$ (read as the curvature perturbation under (FR), where\n    it is more than $10^{68}$ below $A_{s}$), while a sparse")
b = rep(b, "So attack lines 1 and 2\n    are closed for dense quasi-free deposits, whatever the placement of partners. (ii)",
           "So attack lines 1 and 2\n    are closed for dense quasi-free deposits, whatever the placement of partners, under the flat-slice\n    readings (for (UE) see the 16 November paragraph below). (ii)")
b = rep(b, "(viii) Under the charge reading and\n    the mirror's deposit law, a classical modulation",
           "(viii) Under the charge reading and\n    the mirror's deposit law, and with each patch flat (Hypothesis (LC) of the 16 November paragraph below), a\n    classical modulation")
b = rep(b, "(occupations at most one, and the shot term below $10^{-77}$ at the\n    pivot for a thermal-density deposit), so band data",
           "(occupations at most one, and the shot term of the contrast below $10^{-77}$ at the\n    pivot for a thermal-density deposit, read under (FR)), so band data")

# known: the dated paragraph, appended as a new paragraph of the folded scalar
PARA = r"""
    Results and Leon's decisions of 16 November. The slice datum. On a slice of a first-order scalar
    perturbation of the spatially flat Robertson-Walker field, the part of the field equation contracted with
    the slice's normal ties the slice's curvature, the perturbation $\delta_{H}$ of its expansion and the
    deposit's contrast $\delta$: the scalar curvature of the slice is $6H^{2}(\delta - 2\delta_{H})$, that is,
    the slice's first-order local density parameter, $\Omega_{\Sigma} - 1 = \delta - 2\delta_{H}$. The slice
    data are free, and in the radiation field the conserved amplitude outside the Hubble length is an exact
    linear function of them, to leading order $\zeta_{\infty} = \tfrac32X^{2}(\Omega_{\Sigma} - 1) -
    \tfrac14\delta - 2Xv$ with $X = a_{d}H_{d}/k$ and $v$ the deposit's longitudinal velocity relative to the
    slice's normal (\claimref{@P1@}). So a deposit's contrast does not fix the curvature perturbation: the
    expansion datum of the descent slice is a second, independent datum. A white deposit has three readings,
    each a hypothesis: (UE), a slice of uniform expansion, $\delta_{H} = 0$, gives index $n_{s} - 1 = -1$ with
    $\Delta^{2}_{\zeta} = \tfrac94X^{4}\Delta^{2}_{\delta}$; (FM), a flat slice (local criticality, (LC),
    $\Omega_{\Sigma} = 1$) with the deposit's own longitudinal momentum noise, gives $+1$; (FR), a flat slice
    with the deposit at rest on it, gives $+3$. (FR) is the reading the earlier parts of this text used
    without naming it; they are now marked. For the thermal deposit under (UE) the amplitude at the pivot is
    between $2.6 \times 10^{-60}$ and $2.7 \times 10^{-60}$ at $T_{d} = 1$ MeV, between $3.4 \times 10^{-12}$
    and $3.6 \times 10^{-12}$ at the ceiling $7.3 \times 10^{8}$ GeV of the window under Premise (R), equal to
    $A_{s}$ for $T_{d}$ between $3.6 \times 10^{9}$ and $3.7 \times 10^{9}$ GeV, and between $12$ and $13$ at
    $10^{12}$ GeV, where the reading is not a perturbation; the index being $-1$, the reading is a perturbation
    only on a band with an infrared end and is not a candidate for the measured spectrum at any temperature.
    As a rough remark, conditional on (UE) and with no analysis of the largest observed scales made: the
    thermal term equals $A_{s}$ at $k = a_{0}H_{0}$ for $T_{d}$ between $9.2 \times 10^{8}$ and $9.5 \times
    10^{8}$ GeV, so under (UE) the descent's temperature would be capped near $10^{9}$ GeV. Under (FM) the same
    deposit is below $4 \times 10^{-41}$ at the pivot for every $T_{d} \le 10^{12}$ GeV. The string-gas
    conversion of (vii) above is the reading (UE), up to the factor between $\Phi$ and $\tfrac23\zeta$, so (vii)
    and (i) above read thermal noise through different slice data. No stored premise was found that selects a
    reading (argued, from a search of the stored statements, not an audit of every derivation): the nearest
    candidate, the second reading of the dating's join, puts a metric stage before the deposit but has no
    junction rule. By Leon's decision none is adopted: the descent slice is left free, its expansion datum
    (its local density parameter) is a free datum of the descent, and (UE), (LC), (FR) and (FM) are named
    hypotheses of the results that use them, never premises. White energy noise. Within the homogeneous
    gauge-invariant quasi-free deposits the white term of the energy spectrum vanishes exactly for the pure
    stationary states (filled bands); every state with entropy, and every pure state of pairs, keeps it. The
    filled ball of a Weyl field has an excess over the vacuum linear in $k$, which under (UE) gives $n_{s} = 1$
    on observed scales, between $8.3$ and $8.4$ standard deviations from the measured index, with amplitude
    $3H_{d}^{2}/8\pi^{2}\bar M_{P}^{2}$ ($\bar M_{P}$ the reduced Planck mass), more than $10^{17}$ below
    $A_{s}$ on the window; the stored deposit is mixed and far inside the white regime (argued), so its row
    under (UE) is index $-1$, and the scale-invariant row is a statement about a deposit the stored state
    rules do not produce (\claimref{@P2@}). Exchangeable deposits. A deposit whose state is invariant under
    relabellings of its units that are transitive on unordered pairs supplies two second moments and no shape
    of its own. In two cases its matter spectrum is white plus a term at $k = 0$: cells that tile the slice,
    and point cells on a periodic lattice. The boundary of the statement is point cells off a lattice, where
    the second moment multiplies the placement's own structure factor; so (argued) a deposit set before the
    metric carries a spectrum other than the white one only through an invariance group that separates pairs
    of units, or through its placement (\claimref{@P3@}). Sparse deposits. With the density at the descent
    fixed by the record, a quasi-free fermion deposit whose shot noise reaches the measured amplitude at the
    present Hubble scale contains some quantum of more than $3.0 \times 10^{15}$ Hubble masses under (FR) and
    of more than $1.1 \times 10^{27}$ reduced Planck masses under (FM). Given Hypothesis (QP) of that result,
    that the deposit's quanta have energies below the Planck mass (a hypothesis of that result only, not a
    clause of the Hadamard-deposit premise), attack item 3 is closed on flat slices; under (UE) it stays open,
    since quanta of thermal energy already meet the condition there (\claimref{@P4@}). The index ledger of 10
    November gains three rows, none a mode equation: $-1$ (a white deposit under (UE)), $+1$ (a white deposit
    under (FM)) and $0$ (the filled ball under (UE), a deposit the stored state rules do not produce); its
    finite-range row $+3$ is the reading (FR). In each reading a white deposit is far from the measured index;
    what has changed is the reason: far below $A_{s}$ holds on flat slices only, and under (UE) the thermal
    deposit is excluded by its index and, high in the window, by its size. The position is unchanged: the
    series records no mechanism for the measured spectrum, and the amplitude and the index are both still
    free.
""".replace('@P1@', P1).replace('@P2@', P2).replace('@P3@', P3).replace('@P4@', P4)
tail = "the amplitude or the running, obtained from the same structure with no further chosen number.\n  attack:\n"
assert b.count(tail) == 1
b = b.replace(tail, "the amplitude or the running, obtained from the same structure with no further chosen number.\n" + PARA + "  attack:\n")

# attack: item 3 marked, two items added
b = rep(b, "      deposit does not conserve entropy, and whether the record excludes them.\n",
           "      deposit does not conserve entropy, and whether the record excludes them. (16 November.) Closed on\n"
           "      flat slices under Hypothesis (QP), that the deposit's quanta have energies below the Planck mass: the\n"
           "      energy budget of the descent fixes the number, and under the readings (FR) and (FM) a deposit that\n"
           "      reaches the measured amplitude contains some quantum far above the Planck mass\n"
           "      (" + cr(P4) + ").\n"
           "      Open under (UE): the count excludes nothing there, and a sparse deposit is bounded only by the shape\n"
           "      of its spectrum on the observed band.\n")
b = rep(b, "      fixing them in order to supply a spectrum.\n  success: >-\n",
           "      fixing them in order to supply a spectrum.\n"
           "    - >-\n"
           "      The slice datum: find what in the series fixes the expansion datum of the descent slice (a locality\n"
           "      premise would select (LC); a junction rule at the join would fix the slice data), without fixing it\n"
           "      in order to obtain a spectrum\n"
           "      (" + cr(P1) + ").\n"
           "    - >-\n"
           "      Under (UE), carry out the analysis of the largest observed scales that turns the rough ceiling on the\n"
           "      descent temperature, near $10^{9}$ GeV, into a bound with a stated confidence.\n"
           "  success: >-\n")

# entities
b = rep(b, "    - synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources\n  added: '2026-10-22'",
           "    - synthesis.red-tilt-criterion-on-power-law-stages-and-the-index-ledger-of-the-stored-sources\n"
           "    - " + P1 + "\n    - " + P2 + "\n    - " + P3 + "\n    - " + P4 + "\n  added: '2026-10-22'")
text = text[:i] + b + text[j:]

# ------------------------------------------------------------------ op.deposit-state-is-hadamard (M3)
i, j = block(text, 'op.deposit-state-is-hadamard')
b = text[i:j]
b = rep(b, "    finite-range deposit cannot seed the CMB\n    (\\claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}); the collapsing hole's flux\n",
           "    finite-range deposit cannot seed the CMB\n    (\\claimref{synthesis.finite-range-descent-deposit-cannot-seed-cmb}; the bound is on a $\\zeta$ of\n"
           "    finite range, which a matter deposit of finite range has under the flat-slice reading (FR) of\n"
           "    " + cr(P1) + ", and since 16\n"
           "    November the series leaves the descent slice free); the collapsing hole's flux\n")
text = text[:i] + b + text[j:]

yaml.safe_load(text)
open(PATH, 'w').write(text)
print('ok')
