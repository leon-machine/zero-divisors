"""Exact closed-surface integrals with the real degree-2 moment int M_ab M_cd = (d d + J J)/6."""
import time
from fractions import Fraction as F
from itertools import product


def surface_integral(faces):
    """faces: list of lists of (link, +1/-1); every link occurs exactly twice. Returns
    int prod_f (1/6) tr_R(prod X) with X = M or M^T, using the degree-2 moment."""
    occ = {}
    for f, face in enumerate(faces):
        L = len(face)
        for k, (l, d) in enumerate(face):
            row, col = ((f, k), (f, (k + 1) % L)) if d > 0 else ((f, (k + 1) % L), (f, k))
            occ.setdefault(l, []).append((row, col))
    links = sorted(occ)
    assert all(len(occ[l]) == 2 for l in links)
    # edges: (node_a, node_b, link) meaning A_{a b}
    adj = {}
    for li, l in enumerate(links):
        (r1, c1), (r2, c2) = occ[l]
        for a, b in ((r1, r2), (c1, c2)):
            adj.setdefault(a, []).append((b, li, +1))
            adj.setdefault(b, []).append((a, li, -1))  # traversed backwards: transpose
    assert all(len(v) == 2 for v in adj.values())
    # cycles
    seen = set()
    cycles = []
    for start in adj:
        if start in seen:
            continue
        cyc = []
        prev = None
        node = start
        used = set()
        while True:
            seen.add(node)
            choices = [e for e in adj[node] if (node, e) not in used]
            # pick an edge not the one we came along
            for e in adj[node]:
                key = (min(node, e[0]), max(node, e[0]), e[1])
                if key not in used:
                    used.add(key)
                    cyc.append((e[1], e[2]))
                    node = e[0]
                    break
            if node == start:
                break
        cycles.append(cyc)
    E = len(links)
    total = F(0)
    for sig in product((0, 1), repeat=E):
        val = F(1)
        for cyc in cycles:
            k = 0
            sgn = 1
            for li, d in cyc:
                if sig[li]:
                    k += 1
                    if d < 0:
                        sgn = -sgn
            if k % 2:
                val = 0
                break
            val *= sgn * (6 if k % 4 == 0 else -6)
        total += val
    return total / F(6) ** E / F(6) ** len(faces)


def cube_tube(t):
    """spatial plaquette at time 0 and t (in the 1-2 plane), tube of temporal plaquettes."""
    # sites (x, y, tau), x,y in {0,1}
    def link(a, b):
        return (a, b) if a < b else (b, a), (1 if a < b else -1)
    def loop(cs):
        out = []
        for a, b in zip(cs, cs[1:] + cs[:1]):
            l, d = link(a, b)
            out.append((l, d))
        return out
    sq = [(0, 0), (1, 0), (1, 1), (0, 1)]
    faces = [loop([(x, y, 0) for x, y in sq]), loop([(x, y, t) for x, y in sq])]
    for tau in range(t):
        for (x, y), (x2, y2) in zip(sq, sq[1:] + sq[:1]):
            faces.append(loop([(x, y, tau), (x2, y2, tau), (x2, y2, tau + 1), (x, y, tau + 1)]))
    return faces


def disc(R, T):
    def link(a, b):
        return (a, b) if a < b else (b, a), (1 if a < b else -1)
    def loop(cs):
        return [link(a, b) for a, b in zip(cs, cs[1:] + cs[:1])]
    faces = [loop([(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]) for x in range(R) for y in range(T)]
    bd = [(x, 0) for x in range(R + 1)] + [(R, y) for y in range(1, T + 1)]
    bd += [(x, T) for x in range(R - 1, -1, -1)] + [(0, y) for y in range(T - 1, 0, -1)]
    faces.append(loop(bd))
    return faces


if __name__ == '__main__':
    t0 = time.time()
    print('1x1', disc(1, 1) and surface_integral(disc(1, 1)), F(1, 18))
    print('2x1', surface_integral(disc(2, 1)), F(1, 18 ** 2))
    print('2x2', surface_integral(disc(2, 2)), F(1, 18 ** 4), time.time() - t0)
    print('tube t=1', surface_integral(cube_tube(1)), F(1, 18) * F(1, 18) ** 4, time.time() - t0)
    print('tube t=2', surface_integral(cube_tube(2)), F(1, 18) * F(1, 18) ** 8, time.time() - t0)
