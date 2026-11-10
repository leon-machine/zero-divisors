# Run 2026-11-08-colour-lattice: what is specific to this run

LAB = /home/claude/phys-graph. Run folder: colony/runs/2026-11-08-colour-lattice/ (findings/, work/<name>/, verify/).
Read colony/BRIEF.md and colony/POLICIES.md; this file overrides them. Baseline: baseline.log.

## Target
op.qft-non-abelian-gauge-fields, the attack item "Colour: a colour rotor lattice (none is stored) and its continuum limit;
pure-colour confinement is the Yang-Mills mass-gap problem and is not addressed." Read the problem's statement, known
(including the 2 and 8 November paragraphs) and attack items in store/open_problems.yaml, and the stored lattice results:
synthesis.weak-factor-rotor-lattice-strong-coupling-area-law (SU(2) rotor lattice, (1/4)^A, compact U(1) (1/2)^A),
synthesis.non-abelian-gauge-fixing-has-gribov-copies-and-the-weak-rotor-lattice-with-doublets-has-a-perimeter-law,
synthesis.imported-wilson-lattice-gauge-theory-and-strong-coupling-confinement (Wilson, Osterwalder-Seiler, Elitzur, Guth,
Froehlich-Spencer), synthesis.imported-singer-gauge-slice-neuberger-lattice-brst-and-fradkin-shenker-complementarity,
synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces (b3 = -11 + 4 n_g/3), and the colour block of
synthesis.field-level-brst-differential-of-the-derived-gauge-fields-is-nilpotent (su(3) as the eight traceless bivectors of
the e3..e8 block of Cl(9,0) commuting with J = e34 + e56 + e78).

Leon asked what the graph says about the Yang-Mills mass gap (the Clay problem: construct quantum Yang-Mills on R^4 for a
compact simple group satisfying the Wightman or Osterwalder-Schrader axioms, and prove a mass gap Delta > 0). The graph
currently says nothing on colour. The aim is to store what can be established exactly about a colour rotor lattice and to
state precisely, in the store, what separates it from the mass-gap problem. Nobody expects this run to solve the Clay
problem; a claim that it does is a defect for the referee.

Questions:
(1) Construction: the colour rotor lattice in GA (links are rotors of the e3..e8 block commuting with J and with unit
determinant, i.e. SU(3); say exactly how det = 1 is expressed in GA, for example through the action on the J-complex
volume form or the pseudoscalar of the block). Haar moments on SU(3) needed for strong coupling, exactly: <U_ab>, <U U~>
(degree 1+1), and the baryonic cubic moment <U U U> contracted with the J-complex volume form (nonzero for SU(3), zero
for U(3) and for SU(2) at degree 3). Derive them in GA (a finite subgroup that is a design to the needed degree, or an
invariant-theory derivation with exact arithmetic), not imported.
(2) Strong coupling: the leading coefficient of every rectangular fundamental Wilson loop (with the Wilson action
normalised as in the stored SU(2) result; state beta = 6/g^2 for SU(3) and the per-plaquette leading coefficient), the
centre Z3 and N-ality: fundamental loops area law, loops of N-ality zero (adjoint, or three fundamental lines joined by
the volume form) not confined by the leading term (perimeter or screened), and the Polyakov loop / centre symmetry
statement at finite temperature if it can be done exactly. Leading-order strong-coupling mass gap (the lowest glueball
from the plaquette-plaquette connected correlator in the time direction): an exact leading decay rate at small beta, and
a statement of exactly what is proved (finite order of the expansion) and what Osterwalder-Seiler (imported) adds.
(3) What separates this from the mass gap: the same leading strong-coupling statements hold for compact U(1), which
deconfines at weak coupling (Guth, Froehlich-Spencer, imported); the continuum limit needs beta -> infinity (asymptotic
freedom, b3 < 0, stored); with dynamical quarks (the series has n_g = 3 generations of colour triplets) the fundamental
Wilson loop gets a perimeter law (string breaking), as the weak factor did with doublets. Settle each exactly where it can
be computed, and state the rest as argued. Also: does anything in the series supply a fundamental lattice spacing or
finiteness (for example premise P2) that would make the continuum limit not needed physically? If so, say precisely
that this changes the question and does not touch the Clay problem; if not, say so.

## Pairs
Attacker A (constructive): build the colour rotor lattice and compute (1) and (2) exactly; one strong proposal, at most two.
Attacker B (adversarial and cross-subject): (3): what the colour lattice cannot say. Candidates: a no-go that any finite
order of the strong-coupling expansion is identical in form for SU(3) and a deconfining group (exact statement and its
limits), string breaking with quark triplets at beta = 0 (exact, as the stored doublet perimeter law), Gribov copies for
colour (Singer applies to SU(3); a lattice copy if cheap), and the series' own finiteness premises versus the continuum
limit. Search the store across subjects for anything that bears on a gap (towers, rung gap, pairing gap, gapped doublet
modes, current algebra results of today) and test whether any of it is a mass gap for the gauge field; expect not, and
show why exactly. One strong proposal, at most two. Read your sibling's findings midway and do not duplicate.

Both: everything in GA (rotors, bivectors, J; no matrices or imaginary unit where GA does the work; declare outside_ga
otherwise), derived not imported where feasible (Wilson, Creutz, Drouffe-Zuber, Osterwalder-Seiler, Muenster as prior art
in the extraction note; if a result truly rests on a literature theorem, list it as a decision for Leon: a new imported
Fact is maintainer-only). Exact checks (Fractions, lib/GA.py). Titles, one-liners and lay text must not suggest progress
on the Clay problem beyond what is proved.

## Gate and rules
As BRIEF.md and the previous runs: check4.py exits 0 with no warnings (no W413); validate_one ok
(colony/runs/2026-11-06-edge-normality/verify/final/validate_one.py <dir> colony/runs/2026-11-08-colour-lattice/verify/final);
register with `python3 colony/labcli.py propose_claim @<abs draft json>` (move aside first; copy coverage.yaml back; quote
YAML strings containing ": "); a proposal cannot cite another proposal (E201). Copy the format of the stored
synthesis.weak-factor-rotor-lattice-strong-coupling-area-law. House style: no em dashes; never
"honest"/"honestly"/"load-bearing"; Q(v) for squares; no agent or run names in store text. Credit {name: Claude Opus 5.5,
role: proposal and drafting, source: run 2026-11-08-colour-lattice}. Run checks with PYTHONDONTWRITEBYTECODE=1. One gate
process at a time; 2 CPUs shared; never kill other processes; do not edit store/, commit, push or spawn agents. Findings:
findings/attack-A.md, findings/attack-B.md.
