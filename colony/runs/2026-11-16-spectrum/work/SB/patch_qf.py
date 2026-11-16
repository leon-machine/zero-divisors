import re
t=open('entity.md').read()
def rep(a,b,cnt=1):
    global t
    assert t.count(a)==cnt,(t.count(a),a[:70])
    t=t.replace(a,b)
rep("kind: claim\nversion: 4\n","kind: claim\nversion: 5\n")
rep("""review: draft
derivations:""","""- name: Claude Fable 5.2
  role: 'restatement: the reading of the contrast as the curvature perturbation named as hypothesis (FR), with a note on the three readings of the shot term'
  version: 5
  source: run 2026-11-16-spectrum
amendments:
- version: 5
  kind: restatement
  defect: 'clause (iv), the consequence, the technical and lay levels and the one-liner compared the shot term of the energy contrast with A_s and called it index 3 without stating the conversion; that reads the contrast as four times the curvature perturbation, which holds only on a flat slice with the deposit at rest on it. On a flat slice with thermal momentum noise the index is +1, and on a slice of uniform expansion it is -1 with the amplitude raised by (9/4)(a_d H_d/k)^4, above one at the pivot for a thermal deposit at 1e12 GeV. Restated as conditional on hypothesis (FR); the inequalities of (i) to (iv) and every number are unchanged.'
  evidence: 'check.py::check_conversion_readings_of_the_shot_term'
review: draft
derivations:""")
rep("""  - synthesis.imported-planck-2018-lcdm-parameters@3
  proof: proof-main.tex""","""  - synthesis.imported-planck-2018-lcdm-parameters@3
  - synthesis.imported-large-scale-potential-and-sachs-wolfe-relations@2
  - synthesis.imported-superhorizon-zeta-conservation@3
  proof: proof-main.tex""")
rep("""- kind: check
  ref: check.py::check_shot_term_at_the_pivot
""","""- kind: check
  ref: check.py::check_shot_term_at_the_pivot
- kind: check
  ref: check.py::check_conversion_readings_of_the_shot_term
""")
rep("""is below $10^{-77}$ for every $T_{d}$, more than $10^{68}$ below $A_{s}$.""","""is below $10^{-77}$ for every $T_{d}$; under hypothesis (FR) of the note on the conversion below, where the contrast is four times the curvature perturbation, that is more than $10^{68}$ below $A_{s}$.""")
rep("""the deposit's spectrum differs from the vacuum's by less than $10^{-38}$ in amplitude at the pivot""","""the spectrum of the deposit's contrast differs from the vacuum's by less than $10^{-38}$ in amplitude at the pivot""")
note = r"""
\emph{Note (the conversion to the curvature perturbation; added 16 November).} Clauses (i) to (iv) bound the contrast $\delta$ of the energy on the descent slice; by themselves they do not bound the curvature perturbation. Where this entity compares the shot term with $A_{s}$, calls it the finite-range class of index $3$, or concludes that a dense deposit is far too small to carry the primordial spectrum, it reads $\delta$ through $|\zeta| = \delta/4$. That is a hypothesis, (FR): \emph{to first order the descent slice is flat, each region a flat Robertson-Walker field whose expansion rate takes up its density excess, and the deposit is at rest on the slice, with no longitudinal momentum noise as $k \to 0$.} It does not follow from (i) to (iv) or from the results cited here. The linearised constraint equations of the gauge fields $(\hb, \Omega)$ on a slice (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) tie the slice's curvature perturbation $\psi$, the perturbation $\kappa_{\theta}$ of its expansion and the contrast by $H\kappa_{\theta} + (k/a)^{2}\psi = -4\pi G\rho\,\delta$ (in the metric reading, the linearised Hamiltonian constraint) and leave one function of the slice free. In the radiation era the conserved amplitude outside the Hubble length is, to leading order in $1/X$ with $X = a_{d}H_{d}/k$,
\[
\mathcal{R} = \psi + \tfrac14\delta + 2Xu
\]
up to the sign conventions of the three terms, $u$ being the deposit's longitudinal momentum density over $\rho + p$ (standard linear theory, from memory; the projection on the growing solution is verified by exact series in the check, and its growing solution has $\mathcal{R} = \tfrac32\Phi$ as in Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations}). Write $s = \Delta_{\delta}^{2}$ for a white shot term. Three readings: (FR) $\psi = 0$ and $u = 0$, $\Delta_{\mathcal{R}}^{2} = s/16$, index $3$, the numbers of (iv) as stated. (FM) flat slice and a deposit with the momentum noise of independent modes: for thermal occupations the longitudinal momentum spectrum is $T/(\rho + p)$ against $4T/\rho$ for the contrast, so $\Delta_{\mathcal{R}}^{2} = (1 + 12X^{2})\,s/16$, index $+1$; at the pivot this is below $10^{-38}$ for the Standard Model count at $T_{d} \le 10^{12}$ GeV, so the amplitude verdict stands and the index $3$ does not. Pure pair deposits with partners at opposite momentum have no momentum noise at $k = 0$ and stay in (FR). (UE) slice of uniform expansion, $\kappa_{\theta} = 0$: $\psi = -\tfrac32X^{2}\delta$, $\Delta_{\mathcal{R}}^{2} = \tfrac94X^{4}s$, index $-1$; for a thermal bath of $g$ effective species of which the fermion modes carry the share $f$ of the density, $\Delta_{\mathcal{R}}^{2} = f\,\tfrac{135}{\pi^{4}g}(H_{d}/T_{d})^{3}X$, which at the pivot is above one at $T_{d} = 10^{12}$ GeV and more than twenty times $A_{s}$ at $10^{10}$ GeV ($g = 106.75$, $f \ge \tfrac12$). Under (UE) a dense thermal deposit is therefore not negligible: it is excluded as the carrier by its index, and in the upper part of the window by its size. In all three readings a quasi-free fermion deposit whose energy structure factor does not vanish at $k = 0$ has an index, $3$, $1$ or $-1$, far from the measured one, so the conclusion that such a deposit does not carry the measured spectrum stands; the ground ``far below $A_{s}$'' holds under the two flat-slice readings only. No stored premise was found to select the reading (a search of the stored statements, not an audit of every derivation). The uniform-density $\zeta$ and $\mathcal{R}$ differ on the slice by a quarter of the comoving contrast, a term of the order neglected in Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}; for data with a decaying part it is not small, and $\zeta$ is carried unchanged from the slice only for the growing solution (under (FR) it keeps its magnitude and changes sign).
"""
a="The shot-noise bound itself is unaffected.\n"
assert t.count(a)==1
t=t.replace(a,a+note)
rep("""white noise at the level of the number of quanta, index $3$, the finite-range class whatever the range of the correlations.""","""white noise at the level of the number of quanta, index $3$ for the contrast, and the finite-range class for the curvature perturbation under hypothesis (FR) of the formal note on the conversion, whatever the range of the correlations.""")
rep("""removes the thermal-density deposits (the I-state among them) outright, and names what is left:""","""removes the thermal-density deposits (the I-state among them) outright under the flat-slice readings of that note (under uniform expansion they are excluded by their index, $-1$, and high in the window by their size), and names what is left:""")
rep("""so the fluctuations are about $10^{-40}$, against the measured $5 \\times 10^{-5}$.""","""so the fluctuations are about $10^{-40}$, against the measured $5 \\times 10^{-5}$, when the unevenness of the deposit is read directly as the ripple. (That reading assumes each region simply started a little earlier or later; a note in the formal statement gives two other readings, in which the size changes but the dependence on scale is still wrong.)""")
rep("""the shot term at the pivot is below $10^{-77}$ for every reheating temperature, far below $A_{s} = 2.1 \\times 10^{-9}$, while""","""the shot term of the contrast at the pivot is below $10^{-77}$ for every reheating temperature, far below $A_{s} = 2.1 \\times 10^{-9}$ when the contrast is read as four times the curvature perturbation (flat slice, deposit at rest), while""")
open('entity.md','w').write(t)

p=open('proof-main.tex').read()
p=p.rstrip('\n')+r"""

The conversion note (version 5). In the radiation era, with $x = k\eta$, the Bardeen potential obeys $\Phi'' + \tfrac4x\Phi' + \tfrac13\Phi = 0$, with the solutions $\Phi_{g} = 1 - \tfrac{x^{2}}{30} + \dots$ and $\Phi_{d} = x^{-3} + \tfrac16x^{-1} - \dots$ (Frobenius series). Put $\mathcal{R} = \Phi + \tfrac12(x\Phi' + \Phi)$, which is $\tfrac32\Phi$ on the growing solution at leading order, the relation of Fact \claimref{synthesis.imported-large-scale-potential-and-sachs-wolfe-relations} at $w = \tfrac13$, and $\Delta_{c} = -\tfrac23x^{2}\Phi$, the comoving contrast (the constraint, in every slicing). Then $\mathcal{R}_{g}\Delta_{d} - \Delta_{g}\mathcal{R}_{d} = -1/x$, and data $(\mathcal{R}, \Delta_{c})$ at $x$ have the growing amplitude $\mathcal{R}_{\infty} = \mathcal{R}\,(1 + \tfrac{x^{2}}{6} + \dots) + \Delta_{c}\,(\tfrac14 - \tfrac{x^{2}}{24} + \dots)$; on the decaying solution $\mathcal{R} + \tfrac14\Delta_{c}$ vanishes to the two leading orders. On a slice with curvature perturbation $\psi$, contrast $\delta$ and momentum potential $q$, $\mathcal{R} = \psi - Hq/(\rho + p)$ and $\Delta_{c} = \delta - 3Hq/\rho$, so in the radiation era $\mathcal{R}_{\infty} = \psi + \tfrac14\delta - 2Hq/(\rho + p)$ at leading order, and $Hq/(\rho + p)$ is $Xu$ up to sign. The energy constraint with $\kappa_{\theta} = 0$ gives $\psi = -\tfrac32X^{2}\delta$, and then the terms of order $\delta$ cancel, $\mathcal{R}_{\infty} = -\tfrac32X^{2}\delta + 2Xu + O(\delta/X^{2})$. The uniform-density variable is $\mathcal{R} - \tfrac14\Delta_{c}$, so it differs from $\mathcal{R}$ by a term of order $x^{2}\Phi$, the order neglected in Fact \claimref{synthesis.imported-superhorizon-zeta-conservation}; under (FR) the slice has $\mathcal{R} = 0$ and $\Delta_{c} = \delta$, so the uniform-density variable is $-\tfrac14\delta$ on the slice and $+\tfrac14\delta$ afterwards. For thermal occupations the variance formula of (i) gives $\int\omega^{2}n(1 - n) = T^{2}\partial\rho/\partial T = 4\rho T$ for the energy form and a third of it, $(\rho + p)T$, for the longitudinal momentum form, at $k \to 0$, with no cross term by isotropy; hence $P_{\delta} = 4T/\rho$, $P_{u} = T/(\rho + p) = \tfrac{3}{16}P_{\delta}$ and $4X^{2}P_{u} = 12X^{2}\cdot\tfrac{1}{16}P_{\delta}$. With $\Delta_{\delta}^{2} = \tfrac{60}{\pi^{4}g}(\kappa/T_{d})^{3}$, $\kappa = H_{d}/X$, the reading (UE) gives $\tfrac{135}{\pi^{4}g}(H_{d}/T_{d})^{3}X$, times the share $f$ for the fermion modes alone. The check verifies the series and the determinant, the three readings on rational data, the thermal ratio, and the numbers: with $H_{d} = \pi\sqrt{g/90}\,T_{d}^{2}/\bar M_{P}$ the square of the (UE) amplitude is $(135f)^{2}g\,(T_{d}/\bar M_{P})^{6}X^{2}/(90^{3}\pi^{2})$, above one at the pivot for $T_{d} = 10^{12}$ GeV, $g = 106.75$, $f = \tfrac12$ and the stored $X > 3.2 \times 10^{20}$, and above $(20A_{s})^{2}$ at $10^{10}$ GeV where $X$ is a hundred times smaller; under (FM) the shot term of (iv) at $g = 106.75$, below $8 \times 10^{-80}$, times $(1 + 12X^{2})/16$ with $X < 3.44 \times 10^{20}$, is below $10^{-38}$.
"""
open('proof-main.tex','w').write(p+"\n")

c=open('check.py').read().rstrip('\n')
import os
c+=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'qf_newcheck.txt')).read()
open('check.py','w').write(c)
