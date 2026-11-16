def glob(t):
    for a,b in (("(C0)","(FR)"),("(C1)","(FM)"),("(CA)","(UE)"),("\\kappa","k_{d}"),("\\beta\\,u","\\beta\\,v"),("_{u","_{v"),("$u$","$v$")):
        t=t.replace(a,b)
    return t
t=glob(open('entity.md').read())
def rep(a,b):
    global t
    assert t.count(a)==1,(t.count(a),a[:90])
    t=t.replace(a,b)
def between(start,end,new):
    global t
    assert t.count(start)==1,(t.count(start),start[:60])
    i=t.index(start); j=t.index(end,i)
    t=t[:i]+new+t[j:]
rep("title: 'Sparse quasi-free deposits need super-Planckian quanta on a flat slice'","title: 'Sparse fermion deposits: closed on flat slices for sub-Planckian quanta, open under (UE)'")
between("    Attack item 3 of the open problem:","---\n## formal",r"""    Attack item 3 of the open problem: sparse or energetically broad quasi-free deposits, which the stored
    shot-noise bound leaves open because their number of quanta is not fixed by the record. What fixes it is the
    energy budget: the density at the descent is the record's, so few quanta means much energy in some of them.
    The stored shot term, the exclusion principle for the soft quanta and the recorded density together bound
    the shot term by the energy of the most energetic quantum in units of the Hubble mass. The conversion of the
    contrast into the curvature perturbation depends on the descent slice, which the series leaves free; the
    result is therefore given under three readings, each a hypothesis here and none adopted: (FR), a flat slice
    with the deposit at rest on it (the reading the stored clause uses at its version 4); (FM), a flat slice with
    the deposit's own longitudinal momentum noise; (UE), a slice of uniform expansion. Their coefficients are
    those of the result on the descent slice's constraints filed alongside,
    synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit, cited in the text and to be
    added to the uses of this result when it is stored. Under (FR) and (FM) the item closes given a second named
    hypothesis, (QP): the deposit's quanta have energies below the Planck mass. (QP) is a hypothesis of this
    result only, not a stored premise. Under (UE) the count closes nothing, and the item stays open there: what
    bounds a deposit under (UE) is the shape of its spectrum against the observed band. Kill condition written
    before the computation: a sparse deposit that reaches the measured amplitude at the largest observed scale
    with every quantum below the Planck mass refutes the closing. None exists under (FR) or (FM) (clauses (iv),
    (v)); under (UE) thermal quanta already meet the necessary condition at the top of the window, so no closing
    is claimed there. Transport-absent: the argument uses the variance bound of the CAR algebra, the exclusion
    principle and the Friedmann relation; the Clifford reading of the variance bound is the stored result's. The
    energy spread at fixed number is covered by the same inequality, since only the largest energy enters. The
    deposits are gauge-invariant, as in the cited clause (iv); paired deposits fall under the cited general bound
    but not under that clause, and are not treated here. Only the largest quantum energy is bounded: the result
    says that some quantum lies above the threshold, not that every quantum does.
""")
rep(r"with one-particle energies $\omega_{p} \ge |p|$,",r"with one-particle energies $\omega_{p} \ge |p|$ (one energy for the $g$ internal states at each momentum),")
between(r"\item[(iv)] \emph{(What an amplitude needs.)}",r"\item[(v)] \emph{(Numbers.)}",r"""\item[(iv)] \emph{(What an amplitude needs.)} Let the conserved curvature perturbation outside the Hubble length be $\mathcal{R} = \alpha\,\delta + \beta\,v$, with coefficients depending on $X$ alone, $v$ being the velocity of (iii); only $|\alpha|$ and $|\beta|$ enter, so the sign convention of $\mathcal{R}$ plays no part here ($\mathcal{R}$ is minus the $\zeta_{\infty}$ of the result filed alongside, synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit). Then $\Delta_{\mathcal{R}}^{2}(k)^{1/2} \le |\alpha|\,\Delta_{\delta,\mathrm{vac}}^{2}(k)^{1/2} + |\beta|\,\Delta_{v,\mathrm{vac}}^{2}(k)^{1/2} + D(k)$ with $D = (|\alpha| + \tfrac34|\beta|)\,s^{1/2}$ the part the deposit's quanta can carry. Three readings of the descent slice in the radiation era, with the coefficients of the result filed alongside to leading order in $1/X$, each a hypothesis here and none adopted: (FR) flat slice with the deposit at rest on it, $v = 0$ on the slice: $|\alpha| = \tfrac14$, $D = \tfrac14 s^{1/2}$; (FM) flat slice with the deposit's own longitudinal momentum noise: $|\alpha| = \tfrac14$, $|\beta| = 2X$, $D = \tfrac14(1 + 6X)s^{1/2}$; (UE) slice of uniform expansion: $|\alpha| = \tfrac32X^{2}$, $|\beta| = 2X$ (the velocity enters with $2X$ on every slice and is subleading here by $1/X$), $D = \tfrac32X^{2}(1 + 1/X)s^{1/2}$. By (ii), $D(k)^{2} \ge A$ requires
\[
\frac{\omega_{\max} + k_{d}}{M_{H}} \;\ge\; \frac{8\pi AX^{3}}{2f + \eta}\ \ \text{(FR)}, \qquad \frac{8\pi AX^{3}}{(2f + \eta)(1 + 6X)^{2}}\ \ \text{(FM)}, \qquad \frac{2\pi A}{9(2f + \eta)X(1 + 1/X)^{2}}\ \ \text{(UE)}.
\]
""")
rep(r"more than $2.3 \times 10^{42}$ and $1.1 \times 10^{27}$ reduced Planck masses; between the two ends the (FM) bound in Hubble masses increases with $X$.",r"more than $2.3 \times 10^{42}$ and $1.1 \times 10^{27}$ reduced Planck masses; the (FM) bound in Hubble masses increases with $X$, and in Planck masses it is least at the top of the window (argued between the two ends, where no stored bracket of $X$ is available: it is proportional to $a_{d}$).")
between("Consequently the number of quanta of a deposit","\n## technical",r"""Consequently the number of quanta of a deposit that does not conserve entropy is fixed by the energy budget of the descent, not by the record of the entropy: a quasi-free fermion deposit whose shot noise reaches the measured amplitude at the present Hubble scale under a flat-slice reading contains a quantum of more than $1.1 \times 10^{27}$ reduced Planck masses under (FM), at both ends of the window and for every share of the density, and a quantum of more than $3.0 \times 10^{15}$ Hubble masses under (FR). \emph{Hypothesis (QP).} The quanta of the deposit have energies below the Planck mass. (QP) is a hypothesis of this result only; it is not a stored premise and is not part of Premise (HD). Its motivation (argued): a quantum with $G\omega^{2} \gg 1$ has a gravitational radius far above its wavelength and is not a quantum of a test field on a Robertson-Walker collar of the descent, and under (FR) the contrast would in addition be far above one at the Hubble scale. \emph{Given (QP)}, a sparse or energetically broad quasi-free fermion deposit does not carry the measured amplitude under (FR) or under (FM): attack item 3 of the open problem is closed under the two flat-slice readings. Under (UE) it is open: the count excludes nothing there, and a deposit is bounded by the shape of its spectrum on the observed band, which this result does not address. No reading of the slice is adopted.
""")
rep("so quanta of thermal energy meet it with more than nine orders to spare.",r"so quanta of thermal energy meet it with more than nine orders to spare (the factor $(1 + 1/X)^{-2}$ only lowers the threshold).")
rep("How much shot noise an amplitude needs depends on how the contrast converts into the curvature perturbation, and the stored statements do not fix this; three conversions are therefore carried as hypotheses.","How much shot noise an amplitude needs depends on how the contrast converts into the curvature perturbation, which depends on the descent slice; the series leaves the slice free, so three readings are carried as hypotheses, with the coefficients of the result on the slice's constraints filed alongside.")
rep(r"needs quanta of more than $10^{15}$ Hubble masses:",r"needs a quantum of more than $10^{15}$ Hubble masses:")
rep(r"and the quanta needed are a few percent of a Hubble mass at $1$ MeV, rising with the temperature in Hubble masses and never below $10^{27}$ reduced Planck masses in the window: lumps of the mass scale of the Hubble volume, not field quanta.",r"and the largest quantum needed is a few percent of a Hubble mass at $1$ MeV, rising with the temperature in Hubble masses and above $10^{27}$ reduced Planck masses at the top of the window, where it is least: a lump of the mass scale of the Hubble volume. Given the hypothesis (QP) that the deposit's quanta lie below the Planck mass, both flat-slice readings are closed.")
rep("On a slice of uniform expansion the conversion gains the fourth power in the spectrum, the condition falls far below thermal energies at the top of the window, and the count is no obstruction; the uniform-expansion reading has to be confronted through the shape of the spectrum instead.","On a slice of uniform expansion the conversion gains the fourth power in the spectrum, the condition falls far below thermal energies at the top of the window, and the count is no obstruction: under (UE) the item stays open, and that reading has to be confronted through the shape of the spectrum instead.")
between("## lay\n","\n## one-liner","""## lay
One loophole in the earlier result was a deposit with very few particles: few particles means large random variation from place to place, perhaps as large as the measured ripples. But the total energy of the newborn universe is known, so few particles means that some of them carry an enormous energy. Working this out, a deposit sparse enough to make the measured ripples would need some particles weighing more than a billion billion billion Planck masses: a sizeable fraction of, or more than, the mass inside the Hubble region at that time. Such objects would behave as black holes rather than particles (argued). So, if one assumes that the particles of the deposit are lighter than the Planck mass, the loophole closes, provided the ripples are read off the deposit with space taken to be flat region by region. There is another way of reading them, in which the geometry of space rather than the expansion rate takes up the unevenness of the deposit; in that reading the argument does not close the loophole, which stays open, and the question becomes whether the pattern has the right dependence on scale. The theory does not say which reading holds.
""")
i=t.index("## one-liner\n")
t=t[:i]+r"""## one-liner
With the density at the descent fixed by the record, the stored shot term is at most $\tfrac{2(2f + \eta)}{\pi}X^{-3}(\omega_{\max} + k_{d})/M_{H}$, so a quasi-free fermion deposit reaching the measured amplitude at the present Hubble scale needs a quantum above $3.0 \times 10^{15}$ Hubble masses under (FR) and above $1.1 \times 10^{27}$ reduced Planck masses under (FM): given the hypothesis (QP) that its quanta lie below the Planck mass, attack item 3 is closed under the two flat-slice readings; under (UE) thermal quanta meet the condition and it stays open.
"""
open('entity.md','w').write(t)
import yaml
print(len(yaml.safe_load(t.split('---')[1])['title']))
p=glob(open('proof-main.tex').read())
def prep(a,b):
    global p
    assert p.count(a)==1,(p.count(a),a[:90])
    p=p.replace(a,b)
i=p.index("The three conversions are the readings of the linearised constraint equations"); j=p.index(r"(v) With $f \le 1$")
p=p[:i]+r"For (UE), $\tfrac32X^{2} + \tfrac34\cdot2X = \tfrac32X^{2}(1 + 1/X)$, and $s \ge 4A/(9X^{4}(1 + 1/X)^{2})$ gives the third. The coefficients $|\alpha|$ and $|\beta|$ of the three readings are those of the result on the descent slice's constraints filed alongside, synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit (its growing-mode amplitude in the radiation era, to leading order outside the Hubble length: a quarter of the contrast on a flat slice, $\tfrac32X^{2}$ times it on a slice of uniform expansion, and $2X$ times the velocity on every slice); they are not re-derived here and enter as hypotheses."+"\n\n"+p[j:]
prep(r"$s \ge 16A$, $s \ge 16A/(1 + 6X)^{2}$ and $s \ge 4A/(9X^{4})$ respectively,",r"$s \ge 16A$ and $s \ge 16A/(1 + 6X)^{2}$ for (FR) and (FM),")
prep("gives the three thresholds. ","gives the first two thresholds. ")
prep(r"the threshold is below $2.5 \times 10^{-30}$;",r"the threshold without the factor $(1 + 1/X)^{-2}$ is below $2.5 \times 10^{-30}$, and that factor is below one;")
i=p.index("The consequence combines (iv) and (v).")
p=p[:i]+r"The consequence combines (iv) and (v): they bound $\omega_{\max}$, the largest energy on the support of the occupation profile, so they show that some quantum lies above the threshold. The closing under (FR) and (FM) is conditional on Hypothesis (QP), which is stated in the result and is not among the stored premises; its motivation, that a single quantum with $G\omega^{2} \gg 1$ has a gravitational radius far above its wavelength and is not a quantum of a test field on the collar, is argued."+"\n"
open('proof-main.tex','w').write(p)
