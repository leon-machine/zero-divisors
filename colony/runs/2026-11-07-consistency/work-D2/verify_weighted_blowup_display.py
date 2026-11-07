"""obj.interior.weighted-blow-up-hubble-normalisation-admissible v4: the GA form of the Hubble-normalised display
equals the coframe display, exactly (lib/GA.py, lib/gtg.py, Fractions).

(1) Linear algebra: the bivector-valued one-form -sum_i p_i B_i (x) theta^i, theta^i(a) = e^i . a (the coframe
    dual to the physical frame), evaluated on the unit tangential physical vector e_j is -p_j B_j, for generic
    rational p; so "hat Omega_tau = -sum p_i B_i (x) theta^i + E_tau" and "hat Omega_tau(e_j) = -p_j B_j + E_tau(e_j)
    for every j" are the same condition (E_tau(e_j) the value of the error on e_j).
(2) The Kasner model, torsion-solved by the library: tau omega(e_j) = tau Omega(hb(e_j)) = -p_j B_j for the Kasner
    fields hb^{-1}(e_i) = t^{p_i} e_i, p = (-1/3, 2/3, 2/3) (Schwarzschild exponents) and (-2/7, 3/7, 6/7), at two
    times each; and the Cartan forms omega^i_0 = (p_i/tau) theta^i, assembled in the definition's sign
    (gtg.omega_forms), give the same values (the reading).
Run: python3 -I verify_weighted_blowup_display.py  (from any directory; finds the lab's lib/)
"""
import os
import sys
from fractions import Fraction as F

LAB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(LAB, "lib"))
import GA  # noqa: E402
import gtg  # noqa: E402

ok = True
# (1) the coframe display evaluated on the frame
for p in ((F(-1, 3), F(2, 3), F(2, 3)), (F(3, 5), F(-7, 2), F(1, 9))):
    def display(a, p=p):
        out = {}
        for i in (1, 2, 3):
            th = gtg.vdot(gtg.er(i), a)                    # theta^i(a) = e^i . a
            out = gtg.m_add(out, gtg.m_scal(-p[i - 1] * th, gtg.biv(0, i)))
        return out
    for j in (1, 2, 3):
        ok = ok and gtg.m_sub(display(gtg.e(j)), gtg.m_scal(-p[j - 1], gtg.biv(0, j))) == {}
    ok = ok and display(gtg.e(0)) == {}
GA.check("(1) -sum p_i B_i (x) theta^i on e_j is -p_j B_j", ok)
# (2) the Kasner model, torsion-solved
ok2 = True
n = 0
for p in ((F(-1, 3), F(2, 3), F(2, 3)), (F(-2, 7), F(3, 7), F(6, 7))):
    assert sum(p) == 1 and sum(x * x for x in p) == 1
    for base in (2, 3):
        tau, _ = gtg.kasner_data(p, base)
        T = gtg.Jet.var(0, tau, 4, 2)
        TH = [[F(0)] * 4 for _ in range(4)]
        TH[0][0] = F(1)
        for i in (1, 2, 3):
            TH[i][i] = T.pw(p[i - 1])
        fld = gtg.Field(TH)                                 # Omega solved from the torsion-free condition
        ok2 = ok2 and fld.torsion_free()
        cartan = gtg.omega_forms([(i, i, 0, p[i - 1] / tau) for i in (1, 2, 3)])
        for j in (1, 2, 3):
            hat = gtg.m_scal(tau, fld.omega(j))             # tau omega(e_j) = tau Omega(hb(e_j))
            ok2 = ok2 and gtg.m_sub(hat, gtg.m_scal(-p[j - 1], gtg.biv(0, j))) == {}
            ok2 = ok2 and gtg.m_sub(gtg.m_scal(tau, cartan[j]), hat) == {}
            n += 1
        ok2 = ok2 and fld.omega(0) == {}
GA.check("(2) Kasner: tau omega(e_j) = -p_j B_j (torsion-solved) = the Cartan reading, %d values" % n, ok2 and n == 12)
print("ALL PASS" if ok and ok2 and not GA.FAILURES else "FAIL")
