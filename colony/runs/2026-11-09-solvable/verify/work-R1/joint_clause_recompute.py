"""R1: the ten Jordan-Wigner Majoranas of five modes (own construction, signed permutations of the occupation
basis), group closure with -1, and the commutant dimension by the character route
dim End_G(V) = (1/|G|) sum_g tr(g)^2 (a different route from the proposal's union-find).
Also the untwisted family: slot Majoranas times the pair parity."""
from fractions import Fraction as F

NM = 5
DIM = 1 << NM


def apply_op(kind, k, S):
    # Jordan-Wigner: sign (-1)^{number of occupied modes below k}
    sgn = -1 if bin(S & ((1 << k) - 1)).count("1") % 2 else 1
    occ = S >> k & 1
    if kind == "c" and occ:
        return sgn, S & ~(1 << k)
    if kind == "d" and not occ:
        return sgn, S | (1 << k)
    return None


def majorana(p):
    """gamma_{2k} = a_k + a_k^*, gamma_{2k+1} = a_k - a_k^* as a signed permutation: tuple of (image, sign)"""
    k, odd = divmod(p, 2)
    out = [None] * DIM
    for S in range(DIM):
        r = apply_op("c", k, S) or apply_op("d", k, S)
        s, T = r
        if odd and apply_op("d", k, S) is not None:     # the a^* part enters with minus sign
            s = -s
        out[S] = (T, s)
    return tuple(out)


def mul(A, B):
    # (A B)(S) = A(B(S))
    out = []
    for S in range(DIM):
        T, s = B[S]
        U, t = A[T]
        out.append((U, s * t))
    return tuple(out)


def trace(A):
    return sum(s for S, (T, s) in enumerate(A) if T == S)


IDN = tuple((S, 1) for S in range(DIM))
NEG = tuple((S, -1) for S in range(DIM))


def closure(gens):
    G = {IDN}
    frontier = [IDN]
    while frontier:
        new = []
        for g in frontier:
            for h in gens:
                x = mul(g, h)
                if x not in G:
                    G.add(x)
                    new.append(x)
        frontier = new
    return G


def parity(modes):
    return tuple((S, -1 if sum(S >> m & 1 for m in modes) % 2 else 1) for S in range(DIM))


def main():
    gam = [majorana(p) for p in range(2 * NM)]
    for i in range(10):
        sq = mul(gam[i], gam[i])
        assert sq == (IDN if i % 2 == 0 else NEG)
        for j in range(i + 1, 10):
            assert mul(gam[i], gam[j]) == mul(NEG, mul(gam[j], gam[i]))
    G = closure(gam + [NEG])
    char = sum(trace(g) ** 2 for g in G)
    print("|G| =", len(G), " commutant dim (character route) =", F(char, len(G)))
    G9 = closure(gam[:9] + [NEG])
    print("nine directions: |G| =", len(G9), " commutant dim =", F(sum(trace(g) ** 2 for g in G9), len(G9)))
    P = parity([2, 3, 4])
    prod = gam[4]
    for g in gam[5:]:
        prod = mul(prod, g)
    print("pair parity = -gamma_5...gamma_10:", P == mul(NEG, prod), "| = +product:", P == prod)
    ut = [mul(g, P) for g in gam[:4]] + gam[4:]
    Gu = closure(ut + [NEG])
    cross = sum(1 for i in range(4) for j in range(4, 10) if mul(ut[i], ut[j]) == mul(ut[j], ut[i]))
    print("untwisted family: same group:", Gu == G, " commuting slot-pair pairs:", cross, "of 24")


if __name__ == "__main__":
    main()
