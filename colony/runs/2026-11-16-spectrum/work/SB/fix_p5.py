SIB="synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit"
t=open('entity.md').read()
def rep(a,b):
    global t
    assert t.count(a)==1,(t.count(a),a[:90])
    t=t.replace(a,b)
rep("defect: 'clause (iv), the consequence, the technical and lay levels and the one-liner compared","defect: 'clause (iv), the consequence, the technical and lay levels, the one-liner and two sentences of the proof compared")
i=t.index(r"\emph{Note (the conversion to the curvature perturbation; added 16 November).}"); j=t.index("\n## technical",i)
note=r"""\emph{Note (the conversion to the curvature perturbation; added 16 November).} Clauses (i) to (iv) bound the contrast $\delta$ of the energy on the descent slice; by themselves they do not bound the curvature perturbation. Where this entity compares the shot term with $A_{s}$, calls it the finite-range class of index $3$, or concludes that a dense deposit is far too small to carry the primordial spectrum, it reads $\delta$ through $|\zeta| = \delta/4$. That is a hypothesis, (FR): \emph{to first order the descent slice is flat (local criticality, (LC): each region a flat Robertson-Walker field whose expansion rate takes up its density excess), and the deposit is at rest on it, $v = 0$ on the slice, $v$ being the deposit's longitudinal velocity relative to the slice normal.} It does not follow from (i) to (iv) or from the results cited here, and the series adopts no reading of the descent slice: the slice's expansion datum is a free datum of the descent. The conversion is the subject of the result on the descent slice's constraints filed alongside, SIBLING, and is not re-derived here. In its terms: the constraint part of the field equations of the gauge fields $(\hb, \Omega)$ on a slice (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) ties the slice's curvature perturbation $\psi$ (in the metric reading, the spatial part of the derived metric carries the factor $1 - 2\psi$), the perturbation $\kappa_{\theta}$ of its expansion and the contrast by $(k/a)^{2}\psi - H\kappa_{\theta} = -4\pi G\rho\,\delta$, and leaves one function of the slice free. In the radiation era the conserved amplitude outside the Hubble length is, to leading order in $1/X$ with $X = a_{d}H_{d}/k$,
\[
\mathcal{R}_{\infty} = \psi + \tfrac14\delta - \frac{2Hq}{\rho + p},
\]
$q$ being the potential of the deposit's momentum density on the slice, so that the last term has magnitude $2X|v|$. The sign convention, stated once: $\mathcal{R}_{\infty} = -\zeta_{\infty}$, with $\zeta = -\psi + \delta/(3(1 + w))$ the uniform-density variable of Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}; on the growing solution $\mathcal{R} = \tfrac32\Phi$, as in Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations}. Write $s = \Delta_{\delta}^{2}$ for a white shot term. Three readings, each a hypothesis: (FR) $\psi = 0$ and $v = 0$ on the slice, $\Delta_{\mathcal{R}}^{2} = s/16$, index $3$, the numbers of (iv) as stated. (FM) the flat slice (LC) and a deposit with the longitudinal momentum noise of independent modes: for thermal occupations the spectrum of $v$ is $T/(\rho + p)$ against $4T/\rho$ for the contrast, so $\Delta_{\mathcal{R}}^{2} = (1 + 12X^{2})\,s/16$, index $+1$; at the pivot this is below $10^{-38}$ for the Standard Model count at $T_{d} \le 10^{12}$ GeV, so the amplitude verdict stands and the index $3$ does not. Pure pair deposits with partners at opposite momentum have no momentum noise at $k = 0$ and stay in (FR). (UE) slice of uniform expansion, $\kappa_{\theta} = 0$: $\psi = -\tfrac32X^{2}\delta$ and, to leading order in $1/X$, $\Delta_{\mathcal{R}}^{2} = \tfrac94X^{4}s$, index $-1$; for a thermal bath of $g$ effective species of which the fermion modes carry the share $f$ of the density, $\Delta_{\mathcal{R}}^{2} = f\,\tfrac{135}{\pi^{4}g}(H_{d}/T_{d})^{3}X$, which at the pivot is above one at $T_{d} = 10^{12}$ GeV and more than twenty times $A_{s}$ at $10^{10}$ GeV ($g = 106.75$, $f \ge \tfrac12$). Under (UE) a dense thermal deposit is therefore not negligible: it is excluded as the carrier by its index, and in the upper part of the window by its size. In all three readings a quasi-free fermion deposit whose energy structure factor does not vanish at $k = 0$ has an index, $3$, $1$ or $-1$, far from the measured one, so the conclusion that such a deposit does not carry the measured spectrum stands; the ground ``far below $A_{s}$'' holds under the two flat-slice readings only. On the slice $\zeta$ and $-\mathcal{R}$ differ by a quarter of the comoving contrast, a term of the order neglected in Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}; for data with a decaying part it is not small, and $\zeta$ is carried unchanged from the slice only for the growing solution: under (FR), $\zeta = +\tfrac14\delta$ on the slice and $\zeta_{\infty} = -\tfrac14\delta$ afterwards, the same size with the opposite sign.
""".replace("SIBLING",SIB)
t=t[:i]+note+t[j:]
rep("(That reading assumes each region simply started a little earlier or later; a note in the formal statement gives two other readings, in which the size changes but the dependence on scale is still wrong.)","(That reading assumes that space in each region is flat and the matter at rest in it; a note in the formal statement gives two other readings, in which the size changes but the dependence on scale is still wrong. The theory does not say which of them holds.)")
open('entity.md','w').write(t)

p=open('proof-main.tex').read()
def prep(a,b):
    global p
    assert p.count(a)==1,(p.count(a),a[:90])
    p=p.replace(a,b)
prep(r"and $10^{68}$ times it is below $A_{s} \ge 2.07 \times 10^{-9}$.",r"and $10^{68}$ times it is below $A_{s} \ge 2.07 \times 10^{-9}$ (the comparison with $A_{s}$ is made under hypothesis (FR) of the formal note on the conversion).")
prep(r"gives index $3$ for white noise, which is what the shot term is.",r"gives index $3$ for white noise, which is what the shot term is (under (FR)).")
i=p.index("The conversion note (version 5).")
p=p[:i]+r"""The conversion note (version 5). The comparisons with $A_{s}$ and the index $3$ in the paragraphs above are made under (FR). The constraint and the amplitude $\mathcal{R}_{\infty} = \psi + \tfrac14\delta - 2Hq/(\rho + p)$ of the note are those of the result on the descent slice's constraints filed alongside, SIBLING; they are cited, not re-derived. As evidence for this amendment the check re-verifies the two coefficients the note uses, by exact series in $x = k\eta = 1/X$: for the radiation-era equation $\Phi'' + \tfrac4x\Phi' + \tfrac13\Phi = 0$, with $\mathcal{R} = \Phi + \tfrac12(x\Phi' + \Phi)$ (which is $\tfrac32\Phi$ on the growing solution at leading order, Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations} at $w = \tfrac13$) and the comoving contrast $\Delta_{c} = -\tfrac23x^{2}\Phi$, data $(\mathcal{R}, \Delta_{c})$ at $x$ have the growing amplitude $\mathcal{R}_{\infty} = \mathcal{R}\,(1 + \tfrac{x^{2}}{6} + \dots) + \Delta_{c}\,(\tfrac14 - \tfrac{x^{2}}{24} + \dots)$, and on a slice $\mathcal{R} = \psi - Hq/(\rho + p)$, $\Delta_{c} = \delta - 3Hq/\rho$. With $\psi = -\tfrac32X^{2}\delta$ (the constraint at $\kappa_{\theta} = 0$, taken from the result filed alongside and not tested here) the terms of order $\delta$ cancel, $\mathcal{R}_{\infty} = -\tfrac32X^{2}\delta - 2Hq/(\rho + p) + O(\delta/X^{2})$. In the convention of Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}, $-\zeta = \mathcal{R} - \tfrac14\Delta_{c}$ on a slice, which differs from $\mathcal{R}$ by a term of order $x^{2}\Phi$, the order neglected there; under (FR) the slice has $\mathcal{R} = 0$ and $\Delta_{c} = \delta$, so $\zeta = +\tfrac14\delta$ on the slice and $\zeta_{\infty} = -\mathcal{R}_{\infty} = -\tfrac14\delta$ afterwards. The thermal ratio is this entity's own: the variance formula of (i) gives $\int\omega^{2}n(1 - n) = T^{2}\partial\rho/\partial T = 4\rho T$ for the energy form and a third of it, $(\rho + p)T$, for the longitudinal momentum form, at $k \to 0$, with no cross term by isotropy; hence $P_{\delta} = 4T/\rho$, $P_{v} = T/(\rho + p) = \tfrac{3}{16}P_{\delta}$ and $4X^{2}P_{v} = 12X^{2}\cdot\tfrac{1}{16}P_{\delta}$. With $\Delta_{\delta}^{2} = \tfrac{60}{\pi^{4}g}(k_{d}/T_{d})^{3}$ at the physical wavenumber $k_{d} = H_{d}/X$, the reading (UE) gives $\tfrac{135}{\pi^{4}g}(H_{d}/T_{d})^{3}X$, times the share $f$ for the fermion modes alone. Numbers, each an exact bracket in the check: with $H_{d} = \pi\sqrt{g/90}\,T_{d}^{2}/\bar M_{P}$ the square of the (UE) amplitude is $(135f)^{2}g\,(T_{d}/\bar M_{P})^{6}X^{2}/(90^{3}\pi^{2})$, between $5.7^{2}$ and $5.8^{2}$ at the pivot for $T_{d} = 10^{12}$ GeV, $g = 106.75$, $f = \tfrac12$ and the stored lower bound $X = 3.2 \times 10^{20}$, and between $(26A_{s})^{2}$ and $(28A_{s})^{2}$ at $10^{10}$ GeV where $X$ is a hundred times smaller; under (FM) the shot term of (iv) at $g = 106.75$, below $8 \times 10^{-80}$, times $(1 + 12X^{2})/16$ with $X < 3.44 \times 10^{20}$, is below $7.1 \times 10^{-39}$.
""".replace("SIBLING",SIB)
open('proof-main.tex','w').write(p)

c=open('check.py').read()
def crep(a,b):
    global c
    assert c.count(a)==1,(c.count(a),a[:90])
    c=c.replace(a,b)
crep('''    S = _radiation_projection()
    ok = S["residual_ok"]
    ok &= S["g"][2] == F(-1, 30) and S["d"][-1] == F(1, 6)
''','''    S = _radiation_projection()
    marks = []
    ok = S["residual_ok"]
    ok &= S["g"][2] == F(-1, 30) and S["d"][-1] == F(1, 6)
    marks.append(ok)
    GA.check("note: the two Frobenius solutions of the radiation-era equation, term by term", ok)
    ok = True
''')
crep('''    ok &= S["Rg"][0] == (3 * w + 5) / (3 * (w + 1)) == F(3, 2)
''','''    ok &= S["Rg"][0] == (3 * w + 5) / (3 * (w + 1)) == F(3, 2)
    marks.append(ok)
    GA.check("note: R = (3/2) Phi on the growing solution, the stored relation at w = 1/3", ok)
    ok = True
''')
crep('''    # slice data in the radiation era: R = psi + r, Delta_c = delta + 4 r, r = -H q/(rho + p); x = 1/X
''','''    marks.append(ok)
    GA.check("note: determinant -1/x, projection coefficients 1, 1/6, 1/4, -1/24; decaying solution has R + Delta/4 = 0 to two orders", ok)
    ok = True
    # slice data in the radiation era: R = psi + r, Delta_c = delta + 4 r, r = -H q/(rho + p); x = 1/X
''')
crep('''    # under (FR) the uniform-density variable R - Delta_c/4 on the slice is -delta/4: opposite sign, same size
    ok &= (F(0) - delta / 4) * fr < 0 and abs(fr + (F(0) - delta / 4)) == delta / (24 * X ** 2)
''','''    marks.append(ok)
    GA.check("note: readings (FM), (UE), (FR) on rational slice data: delta/4 + 2r, -(3/2) X^2 delta + 2r, delta/4", ok)
    ok = True
    # under (FR), in the stored Fact's convention zeta = -(R - Delta_c/4): +delta/4 on the slice (R = 0,
    # Delta_c = delta), and zeta_inf = -R_inf = -delta/4 afterwards: opposite sign, same size
    zeta_slice, zeta_inf = -(F(0) - delta / 4), -fr
    ok &= zeta_slice == delta / 4 and zeta_slice * zeta_inf < 0 and abs(zeta_inf + zeta_slice) == delta / (24 * X ** 2)
    marks.append(ok)
    GA.check("note: under (FR) zeta is +delta/4 on the slice and -delta/4 afterwards", ok)
    ok = True
''')
crep('''    # numbers.  (FM) at the pivot, Standard Model count: shot < 8e-80, X < 7.63e22/222
''','''    marks.append(ok)
    GA.check("note: thermal ratio P_v = (3/16) P_delta, so (FM) is (1 + 12 X^2)/16 of the shot term", ok)
    ok = True
    # numbers.  (FM) at the pivot, Standard Model count: shot < 8e-80, X < 7.63e22/222
''')
crep('''    # (UE), thermal: amplitude^2 = (135 f)^2 g (T/M)^6 X^2/(90^3 pi^2), M the reduced Planck mass 2.435e18 GeV
''','''    marks.append(ok)
    GA.check("note: (FM) at the pivot between 7.0e-39 and 7.1e-39 for the Standard Model count", ok)
    ok = True
    # (UE), thermal: amplitude^2 = (135 f)^2 g (T/M)^6 X^2/(90^3 pi^2), M the reduced Planck mass 2.435e18 GeV
''')
crep('''    GA.check("conversion: R_inf = psi + delta/4 + 2 r; readings (FR), (FM), (UE); thermal numbers", ok)
    assert ok
''','''    marks.append(ok)
    GA.check("note: (UE) thermal amplitude between 5.7 and 5.8 at 1e12 GeV and between 26 and 28 A_s at 1e10 GeV (f = 1/2)", ok)
    assert all(marks)
''')
open('check.py','w').write(c)
