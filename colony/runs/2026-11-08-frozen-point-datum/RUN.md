# Run 2026-11-08-frozen-point-datum: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-08-frozen-point-datum/ (findings/, work/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them. Baseline (store at 12e45eb plus the new open problem):
0 errors, 0 warnings (baseline.log).

## The problem and Leon's decision
Open problem op.frozen-point-rational-datum (store/open_problems.yaml). Over Q, Q(I_Lambda) = Lambda/3, so statements that
normalise by it, use the static de Sitter boost's null eigen-directions, or name an algebra type built on it hold only when
Lambda/3 is a rational square. Since 7 November the store's foundation (synthesis.premise-the-bit,
synthesis.premise-minimal-non-commutativity, synthesis.premise-superposition-over-the-integers,
synthesis.division-gives-the-rationals, synthesis.continuum-completion-premise) places the series' scalars in Q until the
completion F4. LEON'S DECISION (8 November): the series' rational datum is H, with Lambda = 3 H^2. Every affected result is
restated with H as its datum, so that it holds over Q (and any field of characteristic 0) as written. Over R nothing changes.
Prior evidence (from a scratch session, NOT in the store; re-prove everything): work/open-problem-draft.md and
work/realplace_tests.py (30 exact checks, 0 failures), work/ids.txt.

## Leon's standing rules (binding)
Everything in geometric algebra; derive, do not import (literature as prior art in extraction notes only; no imported Facts);
no imaginary unit (store/conventions.md, unit principle U1 to U6; write quadratic fields as Q(sqrt(-3)) only as numbers
inside span{1, unit} or by discriminant, never with a bare i); house style: no em dashes; never "honest"/"honestly"; never
"load-bearing"; Q(v) for squares; no agent or run names in store text.

## Stage 1 (agent S): the theorem and the sweep
(a) File ONE result (new entity), working title "The frozen point's datum is H": over any field K of characteristic 0
    and Lambda in K, Lambda > 0 where an order is needed: the static boost has null eigen-directions over K, the unit boost
    and R_h = 1/H exist over K, the bifurcation sphere has a K-point, Cl(1,3) + <Lambda/3 normalised> is Cl(2,3) over K (and
    the doubling/complexification reading of the mirror extensions holds), each exactly when Lambda/3 is a square in K; with
    H in K (Lambda = 3H^2) all hold. Include the counterexamples (Lambda = 7/3, Lambda/3 = 2) and the extra conditions found
    (SO(1,4) as a group over Q; the unitary pair form needs Q(sqrt 2) besides H): state each exactly, with its own condition.
    Exact checks with lib/GA.py and Fractions (work over Q and over quadratic extensions represented exactly).
(b) Sweep the WHOLE store (claims, objects, notes; formal and technical levels and checks) for every statement that depends
    on the square class of Lambda/3 or of any other non-unit square that the series treats as a datum (search sqrt, Lambda,
    H, kappa_Lambda, R_h, de Sitter radius, frozen point, I_Lambda, SO(1,4), Cl(2,3), Cl(1,4), the static boost). For each hit
    record in findings/sweep.md: id, the clause, class (A: holds over Q for every Lambda; B: holds over Q iff Lambda/3 is a
    square, so restating with H fixes it; C: needs more than H, with the exact extra condition; D: already written with H or
    kappa_Lambda), and the minimal restatement for class B and C. Verify each B and C by an exact check in work/S/.
Stage 2 (agent T, after S): restate every class B and C result with H as the datum, as a proposal of the next version of
that entity (`tp accept --update` takes it), keeping everything else; class C keeps its extra condition, stated exactly.
Stage 3: blind referee of the theorem and the restatements; one fix round; close-out (Leon's decisions, open problem
settled into open_problems_settled.yaml).

## Gate and rules
As BRIEF.md: exact arithmetic, import GA, premise() per premise, mutation-sensitive checks (check4 must show no W413);
check4.py exits 0 and validate_draft ok (helper: colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py
<proposal dir> <out dir>, out dir colony/runs/2026-11-08-frozen-point-datum/verify/final); register each proposal with
`python3 colony/labcli.py propose_claim @<abs path to draft json>` (move a hand-made folder aside first; propose_claim does
not copy coverage.yaml: copy it back and quote any YAML string containing ": "). A proposal cannot cite another proposal
(E201): name sibling proposals in plain text. Credit {name: Claude Opus 5.5, role: proposal and drafting, source: run
2026-11-08-frozen-point-datum}. One gate process at a time; 2 CPUs shared; never kill other processes; do not edit store/,
commit, push or spawn agents.

## Leon's decisions on the sweep (8 November), binding on Stage 2
- D1: the datum is H with Lambda = 3 eps H^2, eps = +-1: Lambda < 0 clauses use H' with Lambda = -3 H'^2.
- D2 (taken as recommended): restate synthesis.frozen-point-complement-window-lowest-causal with Lambda = 3H^2 so its census holds over Q.
- D3: group labels SO(1,4), so(1,4), SO(2,3), so(2,3): add the hypothesis Lambda = 3H^2 (Lambda = -3H'^2 for the (2,3) labels);
  the labels stay.
- D4/C-rows: restate with H and state each extra condition exactly (sqrt 2, sqrt 3 in the field); the exceptional algebra
  normalises by H and H', with the sqrt|Lambda| rescaling kept as a remark with its sqrt 3 condition; the mass weight: take
  nu as the datum, m^2 = (9/4 + nu^2) H^2.
- D5: the imported Fact dark-energy.imported-macdowell-mansouri-theorem-stelle-west is restated by the maintainer, not a filer.
- D7: rewrite the 19 over-R wording rows (sweep section 4) to H, 1/H, no change of content.
- D8: constant normalisations (sqrt 2, sqrt 3, sqrt 6 not data) stay as they are.

## Stage 2 (restaters T1, T2, T3)
Each restated entity is a proposal of the NEXT version of the stored entity (same id), keeping every unchanged field, with a
maintainer-style note in extraction (key maintainer_pass_2026_11_08: by: ai-maintainer-pass, note: "Version v -> v+1. Leon's
decision of 8 November 2026 (op.frozen-point-rational-datum): ..."), a credit entry {name: Claude Opus 5.5, role: 'restated
with H as the rational datum', version: v+1, source: run 2026-11-08-frozen-point-datum}, and the check updated where its
literals encode Lambda (keep it mutation-sensitive). Cite the new theorem in plain text (synthesis.frozen-point-datum-is-h is a
proposal: E201 forbids citing it). Find the update route with `python3 colony/labcli.py tools` (validate_draft and the
proposal tools); `python3 -m tp accept --update <id>` will take a higher-version proposal. Never change a statement's content
beyond the datum and the stated conditions; flag anything else in findings.
- T1: sweep section 1 (class B, rows B1 to B22, except B14, the import, which is D5) and C1, C2.
- T2: sweep section 1b (B(sum2), rows G1 to G20) and C3, C4.
- T3: sweep section 4 (the 19 wording rows).
