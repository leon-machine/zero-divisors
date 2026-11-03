"""tower.volume-elements-planes: exact checks.

Floor T_k over the ground Cl(p,q), in GA.py's blade engine with the layout of the tower: indices
0..n-1 are the ground generators (p squaring +1, then q squaring -1), and plane j (j = 1..k)
occupies indices n + 2(j-1) (e_j, square +1) and n + 2j - 1 (f_j, square -1). Computed for every
ground with n = p + q <= 3 (degenerate grounds excluded, as in the tower) and every k <= 3:
(1) omega_j = e_j f_j squares to 1, anticommutes with e_j and f_j, commutes with every ground
    generator and every generator of another plane, and the omega_j commute pairwise;
(2) Omega_k = omega_1 ... omega_k squares to 1, commutes with every ground generator and
    anticommutes with every plane generator e_j, f_j (j <= k).
Each statement is tested as an exact multivector identity, with a control: omega_j does NOT
commute with its own plane, and Omega_k does NOT commute with a plane generator.
"""
import GA

GROUNDS = [(p, q) for n in range(4) for p in range(n + 1) for q in [n - p]]
KS = [1, 2, 3]


def floor(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def plane(n, j):
    """Generators (e_j, f_j) of plane j (1-based)."""
    return GA.gen(n + 2 * (j - 1)), GA.gen(n + 2 * j - 1)


def plane_labels(k):
    """The labels 1..k of the planes of floor k."""
    return range(1, k + 1)


def check_plane_volume_elements():
    for p, q in GROUNDS:
        n = p + q
        for k in KS:
            S = floor(p, q, k)
            oms = []
            for j in plane_labels(k):
                e, f = plane(n, j)
                om = GA.mul(e, f, S)
                oms.append(om)
                assert GA.eq(GA.mul(om, om, S), GA.sc(1)), (p, q, k, j)
                # anticommutes with its own plane, and does not commute with it
                for g in (e, f):
                    assert GA.anticommutes(om, g, S)
                    assert not GA.commutes(om, g, S)
                # commutes with every ground generator and every other plane's generators
                others = [GA.gen(i) for i in range(n)]
                for i in plane_labels(k):
                    if i != j:
                        others.extend(plane(n, i))
                for g in others:
                    assert GA.commutes(om, g, S), (p, q, k, j)
            for a in oms:
                for b in oms:
                    assert GA.commutes(a, b, S)
    return True


def check_product_omega_k():
    for p, q in GROUNDS:
        n = p + q
        for k in KS:
            S = floor(p, q, k)
            Om = GA.sc(1)
            for j in range(1, k + 1):
                e, f = plane(n, j)
                Om = GA.mul(Om, GA.mul(e, f, S), S)
            # Omega_k is the product of the 2k plane letters: a blade of grade 2k
            assert list(Om.keys()) == [tuple(range(n, n + 2 * k))]
            assert GA.eq(GA.mul(Om, Om, S), GA.sc(1)), (p, q, k)
            for i in range(n):
                assert GA.commutes(Om, GA.gen(i), S)
            for j in range(1, k + 1):
                for g in plane(n, j):
                    assert GA.anticommutes(Om, g, S)
                    assert not GA.commutes(Om, g, S)
    return True
