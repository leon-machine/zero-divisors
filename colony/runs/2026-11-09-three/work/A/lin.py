"""First-order perturbation of a GTG field (hb, Omega): exact, jets over Fractions.
TH = TH0 + eps TH1; Omega = Om0 + eps Om1 from the linearised torsion-free condition;
linearised Ricci vector calR1(gamma_b)."""
from fractions import Fraction as F
import GA, gtg
from gtg import Jet, m_add, m_scal, m_sub, m_neg, m_d, m_val, comm, S13, bivector_blades

def lin_field(fld, TH1, sq=S13):
    """fld: background gtg.Field (jets). TH1[a][mu]: jets. Returns (Om1 list of bivector-jet dicts)."""
    d = fld.d
    g1 = [{(a,): TH1[a][mu] for a in range(d) if TH1[a][mu]} for mu in range(d)]
    bl = bivector_blades(d); nb = len(bl)
    A0 = gtg._torsion_matrix(fld.g, sq)
    rhs = []
    for p in range(d):
        for q in range(p + 1, d):
            # first-order torsion with Om1 = 0: d_p g1_q - d_q g1_p + Om0_p x g1_q - Om0_q x g1_p
            t = m_add(m_d(g1[q], p), m_neg(m_d(g1[p], q)),
                      comm(fld.Om[p], g1[q], sq), m_neg(comm(fld.Om[q], g1[p], sq)))
            for a in range(d):
                rhs.append(-t.get((a,), F(0)))
    sol = gtg.ring_solve(A0, rhs)
    Om1 = [{bl[j]: sol[mu * nb + j] for j in range(nb) if sol[mu * nb + j]} for mu in range(d)]
    return g1, Om1

def lin_ricci(fld, TH1, sq=S13):
    """Values of the first-order Ricci vectors calR1(gamma_b), b = 0..d-1 (dict blade -> Fraction)."""
    d = fld.d
    g1, Om1 = lin_field(fld, TH1, sq)
    Hi0 = fld.hb_matrix()                       # values Hi0[mu][a]
    TH1v = [[gtg._val(TH1[a][mu]) for mu in range(d)] for a in range(d)]
    # Hi1 = -Hi0 TH1 Hi0
    Hi1 = [[-sum(Hi0[mu][a] * TH1v[a][nu] * Hi0[nu][b] for a in range(d) for nu in range(d))
            for b in range(d)] for mu in range(d)]
    R0, R1 = {}, {}
    for mu in range(d):
        for nu in range(mu + 1, d):
            R0[(mu, nu)] = fld.strength(mu, nu)
            R1[(mu, nu)] = m_val(m_add(m_d(Om1[nu], mu), m_neg(m_d(Om1[mu], nu)),
                                       comm(fld.Om[mu], Om1[nu], sq), comm(Om1[mu], fld.Om[nu], sq)))
    Rc1 = {}
    for a in range(d):
        for b in range(a + 1, d):
            acc = {}
            for mu in range(d):
                for nu in range(mu + 1, d):
                    c0 = Hi0[mu][a] * Hi0[nu][b] - Hi0[nu][a] * Hi0[mu][b]
                    c1 = (Hi1[mu][a] * Hi0[nu][b] + Hi0[mu][a] * Hi1[nu][b]
                          - Hi1[nu][a] * Hi0[mu][b] - Hi0[nu][a] * Hi1[mu][b])
                    if c0 and R1[(mu, nu)]:
                        acc = m_add(acc, m_scal(c0, R1[(mu, nu)]))
                    if c1 and R0[(mu, nu)]:
                        acc = m_add(acc, m_scal(c1, R0[(mu, nu)]))
            Rc1[(a, b)] = m_scal(gtg.STORE_SIGN, acc)
    return [gtg.ricci(Rc1, GA.gen(b), sq) for b in range(d)], Rc1

def lin_ricci_jet(fld, TH1, sq=S13):
    """Jets of the first-order Ricci vectors calR1(gamma_b)."""
    d = fld.d
    g1, Om1 = lin_field(fld, TH1, sq)
    H0 = fld.hb_matrix_jet()
    H1 = [[-sum((H0[mu][a] * TH1[a][nu] * H0[nu][b] for a in range(d) for nu in range(d)), F(0))
           for b in range(d)] for mu in range(d)]
    Rc1 = {}
    R0, R1 = {}, {}
    for mu in range(d):
        for nu in range(mu + 1, d):
            R0[(mu, nu)] = fld.strength_jet(mu, nu)
            R1[(mu, nu)] = m_add(m_d(Om1[nu], mu), m_neg(m_d(Om1[mu], nu)),
                                 comm(fld.Om[mu], Om1[nu], sq), comm(Om1[mu], fld.Om[nu], sq))
    for a in range(d):
        for b in range(a + 1, d):
            acc = {}
            for mu in range(d):
                for nu in range(mu + 1, d):
                    c0 = H0[mu][a] * H0[nu][b] - H0[nu][a] * H0[mu][b]
                    c1 = (H1[mu][a] * H0[nu][b] + H0[mu][a] * H1[nu][b]
                          - H1[nu][a] * H0[mu][b] - H0[nu][a] * H1[mu][b])
                    if R1[(mu, nu)]:
                        acc = m_add(acc, m_scal(c0, R1[(mu, nu)]))
                    if R0[(mu, nu)]:
                        acc = m_add(acc, m_scal(c1, R0[(mu, nu)]))
            Rc1[(a, b)] = m_scal(gtg.STORE_SIGN, acc)
    return [gtg.ricci(Rc1, GA.gen(b), sq) for b in range(d)]
