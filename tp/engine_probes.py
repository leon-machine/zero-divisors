"""Small Python expressions whose values the Physics Graph page compares between CPython (computed
here, at site build) and the in-browser engine, to show where the two disagree when a check fails
in the browser. Each probe is evaluated with GA, Fraction (as F) and itertools in scope."""

SETUP = """
from fractions import Fraction as F
import itertools
import re
import GA
import gtg
import fock
import series
S31 = GA.sig(3, 1)
S10 = GA.sig(10, 0)
def gbiv(p, q):
    return GA.mul(GA.gen(p), GA.gen(q), S10)
def occ(i, m):
    return tuple((i >> (m - 1 - k)) & 1 for k in range(m))
def idx(t):
    out = 0
    for b in t:
        out = 2 * out + b
    return out
def ann(k, m):
    out = {}
    for i in range(2 ** m):
        t = occ(i, m)
        if t[k]:
            s = sum(t[:k]) % 2
            u = list(t)
            u[k] = 0
            out[(idx(u), i)] = F(-1 if s else 1)
    return out
def dag(A):
    return {(j, i): c for (i, j), c in A.items()}
def mm(*Ms):
    A = Ms[0]
    for B in Ms[1:]:
        rows = {}
        for (k, j), c in B.items():
            rows.setdefault(k, []).append((j, c))
        out = {}
        for (i, k), a in A.items():
            for j, b in rows.get(k, ()):
                out[(i, j)] = out.get((i, j), F(0)) + a * b
        A = {key: v for key, v in out.items() if v != 0}
    return A
def madd(*Ms):
    out = {}
    for M in Ms:
        for key, v in M.items():
            out[key] = out.get(key, F(0)) + v
    return {key: v for key, v in out.items() if v != 0}
def msc(c, M):
    c = F(c)
    return {key: c * v for key, v in M.items()} if c != 0 else {}
def eye(d):
    return {(i, i): F(1) for i in range(d)}
def p_rows(B):
    rows = {}
    for (k, j), c in B.items():
        rows.setdefault(k, []).append((j, c))
    return rows
def p_pairs(A, rows):
    out = []
    for (i, k), a in A.items():
        for j, b in rows.get(k, ()):
            out.append((i, k, j))
    return out
def p_for_nested(d):
    out = []
    for (a, b), c in d.items():
        out.append((a, b, c))
    return out
def p_rebind(d):
    out = []
    for (k, j), c in d.items():
        pass
    for (i, k), a in d.items():
        out.append(k)
    return out
def p_rebind2(d):
    out = []
    for (k, j), c in d.items():
        out.append(k)
    for (i, k), a in d.items():
        out.append(k)
    return out
def p_setdefault():
    r = {}
    r.setdefault(1, []).append(2)
    r.setdefault(1, []).append(3)
    return r
def p_inner_loop(A, rows):
    out = []
    for key, a in A.items():
        i, k = key
        for j, b in rows.get(k, ()):
            out.append((i, k, j))
    return out
"""

PROBES = [
    "1 << 70", "(1 << 70) >> 3", "2 ** 64 + 1", "-7 // 2", "-7 % 3", "7 % -3", "(-1) ** 5", "(-1) ** 4",
    "13 >> 2 & 1", "5 & 3 | 8", "6 ^ 3", "bin(45).count('1')", "(-1) ** bin(13 & ((1 << 3) - 1)).count('1')",
    "int('-42')", "abs(-3)", "divmod(-7, 2)", "pow(3, 5, 7)", "10 ** 20 // 7", "(10 ** 20) % 7",
    "F(3, 4)", "F(6, 8) == F(3, 4)", "F(1, 3) + F(1, 6)", "F(2, 3) * F(9, 4)", "F(1) / 3", "F(-5, 10)",
    "F(3) == 3", "F(0) == 0", "F(0) != 0", "bool(F(0))", "bool(F(1, 2))", "F(1, 2) < F(2, 3)", "F(-1) ** 3",
    "F(2) ** -2", "F(7, 3) // 1", "F(-7, 3) // 1", "F(7, 3) % 1", "-F(1, 2)", "F(10 ** 30, 3)", "hash(F(4, 2)) == hash(2)",
    "sum([F(1, 2), F(1, 3), F(1, 6)])", "sum(F(1, k) for k in range(1, 6))", "max(F(1, 3), F(2, 7))",
    "str(F(-3, 9))", "F('3/12')", "F(5, 1).denominator", "F(-6, 4).numerator", "round(F(7, 2))",
    "{(1, 2): F(1)} == {(1, 2): F(1)}", "{(): F(0)} == {}", "{(1,): F(1)} == {(1,): 1}", "sorted([(2, 1), (1, 3), (1, 2)])",
    "list(itertools.combinations(range(4), 2))", "list(itertools.product([0, 1], repeat=2))",
    "list(itertools.permutations(range(3)))[3]", "len(list(itertools.combinations(range(10), 5)))",
    "tuple(sorted({3, 1, 2}))", "frozenset([1, 2]) == frozenset([2, 1])", "[x for x in range(10) if x % 3 == 0]",
    "all([]) and not any([])", "next((r for r in range(5) if r > 2), None)",
    "hash(F(1, 3)) == hash(F(2, 6))", "len({F(1, 3), F(2, 6), F(-1, 3), abs(F(-1, 3))})", "{F(1, 2): 'a'}[F(2, 4)]",
    "F(5, 7) in {F(10, 14)}", "sorted({abs(F(-3, 4)), F(3, 4), F(1, 4)})", "{F(1): 'x'}[1]", "{(F(1, 2), 3): 1}[(F(2, 4), 3)]",
    "(lambda T: (lambda a, b: (exec('X = 1\\ndef f():\\n    return X', a.__dict__), exec('X = 2\\ndef f():\\n    return X', b.__dict__), a.f(), b.f())[2:])(T.ModuleType('pa'), T.ModuleType('pb')))(__import__('types'))",
    "occ(2, 2)", "occ(3, 2)", "idx([1, 0])", "ann(0, 2)", "ann(1, 2)", "dag(ann(0, 2))", "eye(4)",
    "mm(dag(ann(0, 2)), ann(0, 2))", "msc(-2, mm(dag(ann(0, 2)), ann(0, 2)))",
    "madd(eye(4), msc(-2, mm(dag(ann(0, 2)), ann(0, 2))))",
    "p_rows(ann(0, 2))", "p_pairs(dag(ann(0, 2)), p_rows(ann(0, 2)))", "p_inner_loop(dag(ann(0, 2)), p_rows(ann(0, 2)))",
    "p_for_nested({(1, 2): 3, (4, 5): 6})", "p_rebind({(1, 2): 3, (4, 5): 6})", "p_rebind2({(1, 2): 3, (4, 5): 6})",
    "p_setdefault()", "{1: [2]}.get(1, ())", "{1: [2]}.get(5, ())", "(lambda *Ms: Ms[0])(1, 2)",
    "{(j, i): c for (i, j), c in {(1, 2): 3, (4, 5): 6}.items()}",
    "[(a, b, c) for (a, b), c in {(1, 2): 3}.items()]",
    "(lambda d: [k for (i, k), a in d.items()])({(1, 2): 3, (4, 5): 6})",
    "sum((1, 0, 1)[:0]) % 2", "sum((1, 0, 1)[:2]) % 2", "list((0, 1))", "(lambda t: (t.__setitem__(1, 0), t)[1])([1, 1])",
    "gtg.kretschmann(gtg.op_type_d(F(1, 2), gtg.biv(1, 0)))", "gtg.ricci_scalar(gtg.op_type_d(F(1, 2), gtg.biv(1, 0)))",
    "sorted(fock.mm(fock.cre(1, 3), fock.ann(0, 3)).items())", "[fock.jw_sign(s, 2, 3) for s in range(8)]",
    "series.ps_mul(series.taylor_sin(6), series.taylor_cos(6), 6)",
    "13 | 1 << 2", "not 13 >> 2 & 1", "[s for s in range(8) if not s >> 1 & 1]",
    "F('1.5')", "F('1.220890e19')", "F('-2.5e-3')", "F('0.000502')", "F(' 3/7 ')", "F('12')", "F('1e3')",
    "re.match(r'(?P<a>\\d*)(?:\\.(?P<b>\\d*))?', '1.25').groupdict()",
    "re.match(r'(?=\\d|\\.\\d)(?P<num>\\d*)(?:\\.(?P<dec>\\d+))?(?:E(?P<exp>[-+]?\\d+))?', '1.5e3', re.I).groupdict()",
    "re.findall(r'[a-z]+', 'ab cd 12 ef')", "re.sub(r'\\s+', ' ', 'a  b\\tc')",
    "GA.blade_mul((0, 1), (1, 2), S31)", "GA.blade_mul((1, 0), (0,), S31)", "GA.blade_mul((3,), (3,), S31)",
    "GA.mul(GA.gen(0), GA.gen(1), S31)", "GA.mul(GA.mul(GA.gen(0), GA.gen(1), S31), GA.mul(GA.gen(1), GA.gen(2), S31), S31)",
    "GA.reverse(GA.mul(GA.gen(0), GA.mul(GA.gen(1), GA.gen(2), S31), S31))",
    "GA.add(GA.sc(1), GA.gen(2), GA.scal(-1, GA.sc(1)))", "GA.eq(GA.mul(GA.gen(3), GA.gen(3), S31), GA.sc(-1))",
    "GA.anticommutes(GA.gen(0), GA.gen(2), S31)", "GA.commutes(gbiv(0, 1), gbiv(2, 3), S10)",
    "GA.sub(GA.mul(gbiv(0, 6), gbiv(1, 6), S10), GA.mul(gbiv(1, 6), gbiv(0, 6), S10))",
    "GA.dot(GA.add(GA.gen(0), GA.gen(3)), GA.add(GA.gen(0), GA.gen(3)), S31)",
    "len(GA.all_blades(5))", "GA.all_blades(3)[4]",
    "GA.rank_of_vectors([[F(1), F(2), F(3)], [F(2), F(4), F(6)], [F(0), F(1), F(1)]])",
    "GA.mat_rank([[1, 2], [3, 4]])", "GA.congruence_signature([[0, 1], [1, 0]])",
    "GA.mat_mul([[1, 2], [3, 4]], [[0, 1], [1, 0]])",
    "GA.qi(1, 2) * GA.qi(3, -1)", "GA.qi(1, 1) / GA.qi(0, 1)", "GA.qi(0, 0) == 0", "bool(GA.qi(0, 0))",
    "GA.field_rank([[GA.qi(1), GA.qi(0, 1)], [GA.qi(0, 1), GA.qi(-1)]])",
    "(GA.RF.var() * GA.RF.var() - GA.RF.const(1)).eval(F(3))",
    "((GA.RF.var() + GA.RF.const(1)) / (GA.RF.var() - GA.RF.const(1))).eval(F(2))",
]


def expected():
    """[(expression, repr in CPython)] for the page."""
    env = {}
    exec(SETUP, env)
    out = []
    for p in PROBES:
        try:
            out.append([p, repr(eval(p, env))])
        except Exception as exc:  # noqa: BLE001
            out.append([p, f"<{type(exc).__name__}: {exc}>"])
    return out


# State tracing: the page inserts _tp_trace(line, locals()) after each simple statement of a check
# function and records a digest of the local state; the lab replays the same instrumented source in
# CPython and finds the first statement after which the two engines disagree.
TRACE_CODE = r"""
TRACE = []

def _tp_canon(x, depth=0):
    if depth > 6:
        return "..."
    t = type(x)
    if x is None or t in (bool, int, str):
        return repr(x)
    if t.__name__ == "Fraction":
        return "F(%d,%d)" % (x.numerator, x.denominator)
    if t in (list, tuple):
        return ("[" if t is list else "(") + ",".join(_tp_canon(v, depth + 1) for v in x) + ("]" if t is list else ")")
    if t in (set, frozenset):
        return "{" + ",".join(sorted(_tp_canon(v, depth + 1) for v in x)) + "}"
    if t is dict:
        return "{" + ",".join(sorted(_tp_canon(k, depth + 1) + ":" + _tp_canon(v, depth + 1) for k, v in x.items())) + "}"
    if callable(x) or t.__name__ in ("module", "type", "generator"):
        return "<" + t.__name__ + ">"
    d = getattr(x, "__dict__", None)
    if isinstance(d, dict):
        return t.__name__ + _tp_canon(d, depth + 1)
    return t.__name__

def _tp_digest(s):
    h = 1469598103934665603
    for ch in s:
        h = ((h ^ ord(ch)) * 1099511628211) % 18446744073709551616
    return "%016x" % h

def _tp_trace(line, loc):
    if len(TRACE) >= 400:
        return
    items = sorted((k, v) for k, v in loc.items() if k.isidentifier() and not k.startswith("_"))
    TRACE.append([line, _tp_digest(";".join(k + "=" + _tp_canon(v) for k, v in items))])
"""
