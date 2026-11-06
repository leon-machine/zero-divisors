"""Exploration (floats, not evidence): modular conjugation of the CAR subalgebra of the first n0 modes
in a pure gauge-invariant quasi-free (Slater) state on n0 + n1 modes, versus the polar part W of the
off-diagonal block X = P1 E P0. Convention: omega(a*(f) a(g)) = <g, E f>, so <a_j* a_l> = E_{lj}."""
import numpy as np, itertools
rng = np.random.default_rng(1)

def jw(n):
    I2 = np.eye(2); Zs = np.diag([1., -1.]); lo = np.array([[0, 1], [0, 0]], dtype=complex)  # |0>=(1,0) empty
    ops = []
    for j in range(n):
        m = np.array([[1.]])
        for k in range(n):
            m = np.kron(m, Zs if k < j else (lo if k == j else I2))
        ops.append(m.astype(complex))
    return ops  # annihilators a_j

def slater(E, a):
    n = E.shape[0]
    w, V = np.linalg.eigh(E)
    occ = V[:, w > 0.5]
    vac = np.zeros(2 ** n, complex); vac[0] = 1
    psi = vac
    for k in range(occ.shape[1]):
        phi = occ[:, k]
        adag = sum(phi[j] * a[j].conj().T for j in range(n))
        psi = adag @ psi
    return psi / np.linalg.norm(psi)

def modular(Om, Mbasis):
    # S x Om = x* Om; build S on span{x Om}; polar decompose
    X = np.array([x @ Om for x in Mbasis]).T
    Y = np.array([x.conj().T @ Om for x in Mbasis]).T
    # S antilinear: S(X c) = Y conj(c). As real-linear: S = Y C X^{-1}
    Xi = np.linalg.pinv(X)
    # S v = Y conj(Xi v) = (Y conj(Xi)) conj(v) ; write S = A K with K complex conjugation
    A = Y @ Xi.conj()
    # S*S = Delta: S = A K, S* = K A^dag ... Delta = (AK)^*(AK) = K A^dag A K = conj(A^dag A)
    D = (A.conj().T @ A).conj()
    w, V = np.linalg.eigh(D)
    Dmh = V @ np.diag(w ** -0.5) @ V.conj().T
    # J = S Delta^{-1/2} = A K Dmh = A conj(Dmh) K
    Jm = A @ Dmh.conj()   # J = Jm K
    return Jm, D

def run(n0, n1, r):
    n = n0 + n1
    a = jw(n)
    G = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, _ = np.linalg.qr(G)
    E = Q[:, :r] @ Q[:, :r].conj().T
    Om = slater(E, a)
    # check two-point function
    for j in range(n):
        for l in range(n):
            assert abs(Om.conj() @ a[j].conj().T @ a[l] @ Om - E[l, j]) < 1e-10
    # basis of M = CAR(first n0 modes): monomials
    gens = []
    for j in range(n0):
        gens.append([np.eye(2 ** n), a[j], a[j].conj().T, a[j].conj().T @ a[j]])
    Mbasis = []
    for combo in itertools.product(*[range(4) for _ in range(n0)]):
        m = np.eye(2 ** n, dtype=complex)
        for j, c in enumerate(combo):
            m = m @ gens[j][c]
        Mbasis.append(m)
    Jm, D = modular(Om, Mbasis)
    J = lambda Op: Jm @ Op.conj() @ Jm.conj()  # J Op J with J = Jm K, J^{-1} = J
    # check J Om = Om
    print('J Om - Om', np.linalg.norm(Jm @ Om.conj() - Om))
    X = E[n0:, :n0]
    U, s, Vh = np.linalg.svd(X)
    W = U[:, :n0] @ Vh            # polar part, n1 x n0 (n1 >= n0)
    Gam = np.diag([(-1) ** bin(k).count('1') for k in range(2 ** n)]).astype(complex)
    Zt = (np.eye(2 ** n) + 1j * Gam) / (1 + 1j)
    Gam0 = np.eye(2 ** n, dtype=complex)  # parity of first n0 modes
    for j in range(n0):
        Gam0 = Gam0 @ (np.eye(2 ** n) - 2 * a[j].conj().T @ a[j])
    for j in range(n0):
        lhs = J(a[j])
        adW = sum(W[l, j] * a[n0 + l].conj().T for l in range(n1))   # a*(W e_j)
        cands = {'Z a*(We) Z*': Zt @ adW @ Zt.conj().T, 'Gam a*(We)': Gam @ adW, 'Gam0 a*(We)': Gam0 @ adW,
                 'a*(We)': adW, 'a*(We) Gam0': adW @ Gam0}
        for nm, c in cands.items():
            for ph in (1, -1, 1j, -1j):
                if np.linalg.norm(lhs - ph * c) < 1e-8:
                    print('mode', j, 'J a J =', ph, nm)

run(1, 1, 1)
run(2, 2, 2)
run(2, 3, 2)
run(2, 3, 3)
