"""Sweep scanner: list every entity whose text or check matches a square-class-sensitive pattern."""
import os, re, sys, json
ROOT = "/home/claude/phys-graph/store"
PATS = {
 "sqrtL": r"\\sqrt\s*\{[^{}]*(\\Lambda|\\lambda|3/|\\ell|H\b)|\\sqrt\{\\tfrac|sqrt\(\s*(Lam|lam|3\s*/|abs)|\\sqrt\{-\\Lambda|\\sqrt\{\|\\Lambda",
 "kappaL": r"\\kappa_\{?\\Lambda|kappa_Lambda|kappa_L\b",
 "Rh": r"R_\{?h\}?\b|R_h\b",
 "group": r"S[OoPp]\(\s*(1,\s*4|4,\s*1|2,\s*3|3,\s*2)\)|\\mathfrak\{so\}\(\s*(1,\s*4|2,\s*3|4,\s*1|3,\s*2)|so\(1,\s*4\)|so\(2,\s*3\)|Spin\(\s*(1,\s*4|2,\s*3|4,\s*1|3,\s*2)\)",
 "cl5": r"Cl\(\s*(2,\s*3|1,\s*4|3,\s*2|4,\s*1)\)|\\Cl\(\s*(2,\s*3|1,\s*4|3,\s*2|4,\s*1)\)|Cl_?\{?\(?\s*(2,\s*3|1,\s*4)",
 "unitI": r"e_\{?W\}?|\\hat\{?I\}?_?\{?\\Lambda|I_\{?\\Lambda\}?\s*/\s*\\sqrt|unit (ambient )?boost|unit Stelle|normalised frozen|unit frozen|I/\\sqrt|/\\sqrt\{Q\(I",
 "horizon": r"bifurcation sphere|static boost|null eigen|cosmological horizon|de Sitter horizon",
 "Hubble": r"H\s*=\s*\\sqrt|\\Lambda\s*=\s*3\s*H\^|Lambda = 3H|Hubble|H\^\{?2\}?\s*=\s*\\Lambda/3|3H\^\{?2\}?",
 "radius": r"de Sitter radius|\\ell\s*=\s*\\sqrt|\\ell\^\{?2\}?\s*=\s*3/\\Lambda|ell = sqrt",
 "IL": r"I_\{?\\Lambda|I_Lambda|I_\{?\\Lambda\}?\^\{?\\perp",
}
CRE = {k: re.compile(v) for k, v in PATS.items()}
out = {}
for kind in ("claims", "objects", "notes", "predictions"):
    base = os.path.join(ROOT, kind)
    for eid in sorted(os.listdir(base)):
        d = os.path.join(base, eid)
        if not os.path.isdir(d):
            continue
        hits = {}
        for fn in sorted(os.listdir(d)):
            if not (fn.endswith(".md") or fn.endswith(".tex") or fn.endswith(".py") or fn.endswith(".yaml")):
                continue
            try:
                txt = open(os.path.join(d, fn)).read()
            except Exception:
                continue
            for k, c in CRE.items():
                n = len(c.findall(txt))
                if n:
                    hits.setdefault(k, {})[fn] = n
        if hits:
            out[eid] = hits
json.dump(out, open(sys.argv[1], "w"), indent=1)
from collections import Counter
cnt = Counter(k for h in out.values() for k in h)
print(len(out), dict(cnt))
