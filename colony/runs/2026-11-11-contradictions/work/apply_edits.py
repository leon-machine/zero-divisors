"""Applies the revised proposals (PROPOSALS.md, with Leon's decisions of 11 November 2026) to the store.
Run once from the repository root. Every replacement asserts that its old text is present exactly once."""
import re, sys
NEW = 'synthesis.frozen-point-unique-for-the-field-space-connection'
RED = 'synthesis.dark-to-baryon-total-uses-r1-r2-and-d-only-as-mass-per-unit-ball'
FS = 'synthesis.field-space-premise-parallel-frozen-point'
SRC = 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'

def load(d, i):
    p = f'store/{d}/{i}/entity.md'; return p, open(p).read()

def rep(t, old, new):
    assert t.count(old) == 1, (t.count(old), old[:80]); return t.replace(old, new)

def level(t, name):
    m = re.search(r'\n## ' + re.escape(name) + r'\n(.*?)(?=\n## |\Z)', t, re.S); assert m, name; return m

def set_level(t, name, new):
    m = level(t, name); return t[:m.start(1)] + new.strip('\n') + '\n' + t[m.end(1):]

def append_level(t, name, extra):
    m = level(t, name); return t[:m.end(1)].rstrip('\n') + '\n\n' + extra.strip('\n') + '\n' + t[m.end(1):]

def block_end(lines, start):
    j = start + 1
    while j < len(lines) and (lines[j].startswith(' ') or lines[j].startswith('- ') or lines[j] == ''):
        j += 1
    return j

def bookkeep(t, role, kind, defect, note, evidence=None):
    end = t.index('\n---', 4); fm, body = t[:end], t[end:]
    m = re.search(r'^version: (\d+)$', fm, re.M); v = int(m.group(1)) + 1
    fm = fm[:m.start()] + f'version: {v}' + fm[m.end():]
    L = fm.split('\n')
    q = lambda s: "'" + s.replace("'", "''") + "'"
    i = L.index('credit:'); j = block_end(L, i)
    L[j:j] = ['- name: Claude Fable 5.2', f'  role: {q(role)}', f'  version: {v}', f'  source: {q(SRC)}']
    am = [f'- version: {v}', f'  kind: {kind}', f'  defect: {q(defect)}'] + ([f'  evidence: {q(evidence)}'] if evidence else [])
    if 'amendments:' in L:
        i = L.index('amendments:'); j = block_end(L, i); L[j:j] = am
    else:
        i = L.index('credit:'); j = block_end(L, i); L[j:j] = ['amendments:'] + am
    ex = ['  maintainer_pass_2026_11_11:', '    by: maintainer-2026-11-11', "    date: '2026-11-11'", f'    note: {q(note)}']
    if 'extraction:' in L:
        i = L.index('extraction:'); L[i+1:i+1] = ex
    else:
        L += ['extraction:'] + ex
    return '\n'.join(L) + body, v

def save(p, t): open(p, 'w').write(t)

# ---- 1. P1 and the two theorems on the normal tractor connection
p, t = load('claims', 'dark-matter.p1-single-frozen-point')
t = append_level(t, 'formal', r"""\emph{Note (which connection, 2026-11-11).} The ``one tractor connection'' of (P1a) is not named above, and the two theorems cited there are about the normal tractor connection, for which a tractor is parallel in the physical scale only on Einstein regions. Under Premise \claimref{%s} (FS) the frozen point is parallel, with unit pairing with $X$, for the varied connection $A_{\rho}$ on every field, matter included. For that connection the status of (P1a) is given by Theorem \claimref{%s}: if every tower's frozen point is parallel for the one $A_{\rho}$ on a connected part of the invertible region that contains one point where $-(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$ has no kernel vector (any point with isotropic matter other than $w = -\tfrac13$; on Einstein regions the Weyl condition above), the frozen points agree up to constants $c_{r}$, and the independent choice is confined to a component that is de Sitter at that $\Lambda$, not to every conformally flat region. What stays postulated is unchanged: the one connection, and the normalisation $c_{r} = \pm 1$, to which the common $N$ of (P1c) is equivalent given one $G$; (FS) normalises one tractor and does not supply it. For the tower of reversed signature the connection can be shared up to the sign of the frozen point or the discrete element $\operatorname{Ad}(I_{4})$ (the Remark of that Theorem); whether that element bears on the orientation clause (P1b) is not examined. The premise is unchanged.""" % (FS, NEW))
t, v = bookkeep(t, 'note naming the connection of clause (P1a) under the field-space premise', 'restatement',
    'the status paragraph of (P1a) did not name its connection and cited only theorems about the normal tractor connection, which under (FS) does not carry the frozen point in the physical scale on matter regions',
    f'Version 2 -> 3. A note is added to the formal level: under (FS) the status of (P1a) is given by {NEW}; what is postulated is unchanged (the one connection and the normalisation). The three clauses and their wording are untouched.',
    f'{NEW}: check.py::check_field_strength_and_kernels_on_de_sitter_fluid_and_schwarzschild_fields')
save(p, t)

for i, note in [('synthesis.frozen-point-unique-where-weyl-has-no-kernel',
    r"""\emph{Note (scope, 2026-11-11).} $\nabla$ here is the normal tractor connection, for which a tractor is parallel in the physical scale only on Einstein regions, so the application to towers above concerns frozen points parallel for that connection, that is Einstein regions. Under Premise \claimref{%s} (FS) the frozen point is carried by the connection $A_{\rho}$; the corresponding statement, which reduces to this one on Einstein fields with the same $\Lambda$, is Theorem \claimref{%s}.""" % (FS, NEW)),
    ('synthesis.two-frozen-points-conformally-flat',
    r"""\emph{Note (scope, 2026-11-11).} The statement is for the normal tractor connection. For the connection $A_{\rho}$ of Premise \claimref{%s} (FS) the field strength is $-(\mathcal{R} - \tfrac{\Lambda}{3}\mathrm{id})$, which vanishes on the de Sitter field at that $\Lambda$ and on no other isotropic field with matter, so for that connection the independent choice exists only on a component that is de Sitter at that $\Lambda$ (Theorem \claimref{%s}, clauses (iii) and (iv)).""" % (FS, NEW))]:
    p, t = load('claims', i)
    t = append_level(t, 'formal', note)
    t, v = bookkeep(t, 'scope note: the statement is for the normal tractor connection', 'restatement',
        'the application to the towers did not say that it is for the normal tractor connection, which under (FS) is not the connection that carries the frozen point on matter regions',
        f'A scope note is added to the formal level, pointing to {NEW}; the statement and its proof are unchanged.')
    save(p, t)

# ---- 2. the no-echo prediction
p, t = load('predictions', 'scrambling.no-echo-prediction-registered')
t = rep(t, """derivations:
- name: basis
  uses:
  - interior.imported-equivalence-einstein-equations@3
  assumes:
  - singularity.c1-curvature-cutoff@5
""", f"""derivations:
- name: basis
  uses:
  - interior.imported-equivalence-einstein-equations@3
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@5
  assumes:
  - {FS}@2
  - synthesis.c-loc-local-horizon-premise@6
  - synthesis.n-plus-null-ground-state@12
""")
t = set_level(t, 'formal', r"""The registered prediction: post-merger ringdown is the Kerr quasinormal spectrum of general relativity with \emph{no} modification, and in particular no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$ (the delay at which near-horizon structure at Planck distance would reflect \cite{CardosoPani2017}), of order tens to hundreds of milliseconds for stellar-mass remnants ($35$ ms at $10\,M_\odot$, $0.1$ to $0.25$ s for remnants of $30$ to $70\,M_\odot$): within the sensitivity band of existing detectors. The prediction is stated so that it can fail.

\emph{Basis.} (1) \emph{The field equations at and across the future horizon.} The gravitational field obeys Einstein's equations with a constant $\Lambda$, from the stored action on the field space of Premise \claimref{synthesis.field-space-premise-parallel-frozen-point} (FS) (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}), read on the invertible region through the equivalence of Fact \claimref{interior.imported-equivalence-einstein-equations}; the quasinormal spectrum uses the ingoing condition at the future horizon, which is the regularity of the classical field there. (2) \emph{No structure at the horizon beyond the matter fields.} By the identification clause of Premise \claimref{synthesis.c-loc-local-horizon-premise} the modes on a horizon's light rays are the matter field on those light rays, and the modes that Postulates (C1) and (C2) place at the curvature cutoff are the same set described a second time (its paragraph ``One mode set, per light ray''). (3) \emph{Reading, stated and not derived.} The horizon's modes impose no reflecting condition on classical perturbations of the gravitational field. This does not follow from (2) as written: clause (R$_{\mathrm{loc}}$) of that premise makes the modes thermal before a crossing, and a flux reflectivity equal to the Boltzmann factor $e^{-\hbar|\omega|/kT_{H}}$ has been derived in the literature from detailed balance and the fluctuation-dissipation theorem at a horizon (Oshita, Wang and Afshordi, arXiv:1905.00464, JCAP 04 (2020) 016; abstract checked on 11 November 2026), with echoes as its consequence; the reading excludes it. (4) \emph{A state regular across the horizon.} The local form of Premise \claimref{synthesis.n-plus-null-ground-state} at the points of the horizon's generators, argued there at leading order.

\emph{What an echo would refute.} A single statistically confirmed echo train would refute the field equations at the horizon, and so (FS) with the stored action (its refutation condition (b)), or the reading (3). It does not bear on the Schwarzschild calibration of the count by Postulates (C1) and (C2).

\emph{Note (the earlier basis, 2026-11-11).} Until version 2 the prediction rested on Postulate \claimref{singularity.c1-curvature-cutoff} (C1) alone, with the wording that the quantum structure lies at the stretched singularity ``and nowhere near the horizon''. (C1) is now read as a calibration of the count on the Schwarzschild family only, and by (2) the same modes are on the horizon, on Schwarzschild and on Kerr alike; that wording is withdrawn and (C1) is no longer in the basis. With this basis the prediction is general relativity's own: it registers that the series predicts no departure from general relativity at the horizon, and a null result does not distinguish the series from general relativity. The deposited text (T8, Record 7.1) is kept under source\_formal.""")
t = set_level(t, 'technical', r"""The registered prediction is that post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train at the Planck-structure delay $\tau_{\mathrm{echo}} \approx 8M\ln(M/m_P)$, about 35 ms at $10\,\Msun$ and 0.1 to 0.25 s for remnants of 30 to $70\,\Msun$, within the band of existing detectors.

Its basis has four parts: Einstein's equations at and across the future horizon, from the stored action under the field-space premise (FS); the horizon's modes being the matter field on its light rays (the local-horizon premise), so that no further structure sits at the horizon; the stated reading that these modes reflect no classical perturbation, which excludes the thermal reflectivity proposed in the literature; and a state regular across the horizon (the local form of (N$_{+}$)). One statistically confirmed echo train would refute the field equations at the horizon or that reading.

The prediction is shared with general relativity. Until version 2 it rested on Postulate (C1) and said the quantum structure was nowhere near the horizon; that wording is withdrawn.""")
t = set_level(t, 'lay', """If quantum effects altered a black hole's surface, merging black holes would ring with faint repeated echoes a fraction of a second after the main signal. In this framework gravity obeys Einstein's equations right through the horizon, and nothing sits at the horizon except the ordinary matter fields, which are taken not to reflect gravitational waves. So it predicts no echoes: the ringing should be exactly as general relativity says. A single confirmed echo would refute that. The prediction is the same as general relativity's.""")
t = set_level(t, 'one-liner', r"""Post-merger ringdown is the unmodified Kerr quasinormal spectrum, with no echo train at the delay $8M\ln(M/m_P)$: under (FS) with the stored action the field equations hold across the horizon, and under (C$_{\mathrm{loc}}$) the horizon's modes are the matter field on its light rays, read as imposing no reflection; a prediction shared with general relativity.""")
t, v = bookkeep(t, 'basis restated: field equations under (FS), the identification of (C_loc), a stated no-reflection reading and the local form of (N+); (C1) removed from the basis', 'restatement',
    'the prediction rested on (C1) alone and said the quantum structure is nowhere near the horizon, while (C1) is scoped to a Schwarzschild calibration and (C_loc) places the same modes on the horizon; its one uses edge asserted no field equation',
    "Version 2 -> 3, at Leon's decision of 11 November 2026 ((FS) supplies the field equations). Basis edges: uses the imported Einstein equivalence and the frame equation of the frozen-point functional; assumes (FS), (C_loc) and (N+); the assumes edge to (C1) is removed. The predicted spectrum, the delay and the kill threshold are unchanged. The no-reflection reading is stated as a reading; the cited reflectivity paper was checked by its abstract only.")
save(p, t)

# ---- 3. the conjecture
p, t = load('claims', 'transport.obstructions-are-moved-never-destroyed')
old_formal = level(t, 'formal').group(1).strip()
t = set_level(t, 'formal', r"""Proposition \claimref{transport.no-transport-terminates} is the zero-dimensional instance of a principle the transport programme repeatedly meets: a completion never removes degeneracy, it relocates it. The family form is conjectured as follows. A \emph{completion} of a family of quadratic forms $G$ is a standard one: a form $h = G \perp K$ on a larger bundle, with $K$ nondegenerate on a complement and of the same signature on every region where $G$ is nondegenerate (the reading of Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}). \emph{Conjecture.} For a family degenerating along a locus where one of the tameness hypotheses (T1) to (T3) of \claimref{sheaf.tameness} fails (higher corank, a degeneration that is not first-order, or a locus that is not a smooth hypersurface), any completion that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other side, so that no completion is nondegenerate globally; and a cohomological invariant measures the displaced degeneracy, presumably a class built from the mod-8 residues on the two sides of the wall, the state machine of Proposition \claimref{transport.fusion-occurs-most-once} evaluated in families. For tame corank-one degenerations the statement is proved: the one-sided completion theorem and the shadow wall (Theorem \claimref{sheaf.one-sided-completion}), and Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} with clause (1) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}, where the obstruction is the clock mismatch $2 \in \mathbb{Z}_{8}$.

\emph{Note (what is not conjectured, 2026-11-11).} The deposited wording (T1, Conjecture 7.9, kept under source\_formal) states its hypothesis as ``degenerating tamely'', which is the proved case, while asserting that the pattern is not an artefact of the tame case, and it does not say what a completion is. Read loosely, with the exterior model allowed to change across the wall, the statement would be false on tame walls: clauses (2) and (3) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction} give forms nondegenerate at every point and of one signature. There the obstruction is not destroyed either, but it is paid for in rungs and not in a displaced wall: a completion by $k$ hyperbolic planes needs $w_{1}(\shL)^{k} = 0$ (Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}), the class of the dying line is conserved along the wall sequence (Theorem \claimref{synthesis.twisted-wall-induction-conserves-dying-line-class}), and the stored counts on lens walls grow with the dimension. The sheaf-level form of the question is Conjecture \claimref{sheaf.wall-class}.""")
t = set_level(t, 'technical', r"""Conjectured, in the strict reading: a completion is $G \perp K$ with one signature of $K$ on every region where $G$ is nondegenerate. For families degenerating beyond the tame corank-one case, any such completion that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other, and a cohomological invariant, presumably built from the mod-8 residues on the two sides, measures it. The tame corank-one case is proved (the one-sided completion theorem and the shadow wall; the obstruction is the clock mismatch $2 \in \mathbb{Z}_{8}$).

With the exterior model allowed to change across the wall the statement would be false on tame walls, where nondegenerate forms of one signature exist; the obstruction is then paid for in rungs, counted by the class of the dying line.""")
t = set_level(t, 'lay', """Each repair of a failure of division seems to create a new failure somewhere else. This conjecture proposes that the same holds when the geometry varies from place to place: fixing a degeneration on one side of a boundary pushes it to a new boundary on the other side. That is proved in the simplest case, and conjectured beyond it. If the repair may use different extra structure on the two sides, the failure can be removed, but only by adding more structure, and how much must be added is itself a measure of the obstruction.""")
t = set_level(t, 'one-liner', r"""Conjecturally, beyond the tame corank-one case (where it is proved), no standard completion $G \perp K$ of a degenerating family of quadratic forms is nondegenerate globally: completion relocates the degeneration; with the exterior model allowed to change, the obstruction is instead paid for in rungs.""")
t = rep(t, "  - sheaf.conservation-degeneracy-located\nabout:", "  - sheaf.conservation-degeneracy-located\n  - synthesis.wall-class-one-rung-obstruction\n  - synthesis.wall-rung-count-is-height-of-dying-line-class\nabout:")
t = rep(t, "extraction:\n  env: conjecture\n", "extraction:\n  source_formal: '" + old_formal.replace("'", "''") + "'\n  env: conjecture\n")
t, v = bookkeep(t, 'restatement: completion read strictly, hypothesis moved beyond the tame corank-one case, note on the rung count', 'restatement',
    'the hypothesis (degenerating tamely) was the case already proved while the text said the pattern is not an artefact of the tame case, and completion was undefined: read loosely the statement is contradicted on tame walls by clauses (2) and (3) of synthesis.wall-class-one-rung-obstruction',
    'Version 2 -> 3. The deposited wording (T1 Conjecture 7.9, checked against T01_transport_principle.tex line 1555) is kept under source_formal. Status unchanged (conjectured).')
save(p, t)

# ---- 5. Premise D and the reduction theorem
p, t = load('claims', 'dark-matter.d-democracy-total-mass')
t = rep(t, "no stored statement of the fitted total with the cell radius as unit has D in its past cone, and Observation",
    r"no stored statement of the fitted total with the cell radius as unit has D in its past cone, with one exception, the audit \claimref{%s}, which sets the two readings side by side (its clause (ii) is under D, its clause (i) under R1 to R3) and so has both among its conditions, and Observation" % RED)
t, v = bookkeep(t, 'note corrected: the one stored result with both D and R2 among its conditions is named', 'restatement',
    f'the note said no stored statement of the fitted total has D in its past cone; {RED} states the total and holds given D and R2',
    'Version 2 -> 3. One clause added to the note of 10 November naming the exception; the premise is unchanged.')
save(p, t)

p, t = load('claims', RED)
m = level(t, 'formal'); f = m.group(1)
f = rep(f, "they differ as soon as R2 is varied, and the stored wording does not choose between them.",
    "they differ as soon as R2 is varied. Premise R3 as now stated chooses the second, each tower's own cell radius (the Status paragraph below); clause (i) is a statement about the first.")
f = rep(f, "so it is a model of P1, P2, P3, P4, the common ceiling coupling and R3 in the fixed-length reading",
    "so it is a model of P1, P2, P3, the common ceiling coupling and R3 in the fixed-length reading")
t = t[:m.start(1)] + f + t[m.end(1):]
t, v = bookkeep(t, 'two stale sentences corrected (the reading of R3; the retired P4)', 'restatement',
    'clause (i) said the stored wording of R3 does not choose between the two readings, against the Status paragraph of the same result and R3 version 2; the model was called a model of the retired premise P4',
    "Version 1 -> 2. Two sentences of the formal level corrected; no clause changes. Not split, by Leon's decision of 11 November 2026: the result is an audit setting the two readings side by side, and Premise D's note names it as the exception.")
save(p, t)

# ---- 6. the unit of epsilon
p, t = load('claims', 'synthesis.matter-asymmetry-registered-free-input')
t = append_level(t, 'formal', r"""\emph{Note (the unit of $\epsilon$, 2026-11-11).} The words ``per mode'' and the formula $Q = \epsilon N$ are the charge reading's own (Proposition \claimref{dark-matter.stored-asymmetry-charge-not-number}; Theorem \claimref{dark-matter.mirror-tower-copy-one}(v)), whose argument uses only that $N$ is common to the two towers. They do not give $\epsilon$ a number: with $N = M_{P}/H$, about $10^{61}$, no count of modes makes $8.7 \times 10^{-11}$ the factor (the baryon number inside the de Sitter radius is about $5 \times 10^{78}$ today, and it is not constant, the radius being fixed while the density dilutes). The figure $8.7 \times 10^{-11}$ is this tower's yield $n_{B}/s$ today: the conserved charge per comoving volume, measured with this tower's entropy as the unit of comoving volume. It is the descent's datum only if no entropy is produced in this tower after the descent. The equality along the reversal orbit is an equality of charge per comoving volume, $n_{B}' = n_{B}$; it is not $n_{B}'/s' = n_{B}/s$, which is the thermal reading that clause (iv) of the Proposition rejects (the mirror's own ratio is larger by $\xi^{-3}$, the stored $\eta' = \eta/\xi^{3}$). What the premise registers is unchanged.""")
t, v = bookkeep(t, 'note on the unit of epsilon: the quoted figure is a yield per unit entropy used as a comoving ruler', 'restatement',
    'the valuation sentence could be read as epsilon = 8.7e-11 beside Q = epsilon N with N = M_P/H, for which no per-mode reading gives that factor; baryons per unit entropy is the quantity of the thermal reading the charge result rejects',
    'Version 3 -> 4. A note is added to the formal level; the premise and its refutation condition are unchanged. The copy theorem and the charge result, which carry the same wording, are not edited; the note names them.')
save(p, t)

# ---- smaller items
p, t = load('claims', 'standard-model.dating-descent')
m = level(t, 'formal'); f = rep(m.group(1), "In any $\\Lambda$-dominated epoch the age of the universe is automatically of order $N$ Planck times, since $t \\sim 1/H$ and $N = M_{P}/H$: the Dirac coincidence is an identity of the era we observe from, not a clock pointing at the descent.",
    "Near the onset of $\\Lambda$-domination the age of the universe is automatically of order $N$ Planck times, since $t \\sim 1/H$ there and $N = M_{P}/H$ (later the age grows while $1/H$ stays fixed): the Dirac coincidence is a property of the epoch we observe from, not a clock pointing at the descent.")
t = t[:m.start(1)] + f + t[m.end(1):]
t, v = bookkeep(t, 'clause (i) corrected: the coincidence holds near the onset of Lambda-domination', 'restatement',
    'clause (i) said the age is of order N Planck times in any Lambda-dominated epoch; there 1/H is constant and the age grows without bound, so it holds only near the onset, the epochal form of standard-model.what (iii)',
    'Version 6 -> 7. One sentence of clause (i) corrected.')
save(p, t)

p, t = load('predictions', 'pred.dimmed-evaporation-bursts')
m = level(t, 'formal'); f = rep(m.group(1), "If the four odd towers hold matter, as Observation \\claimref{dark-matter.which-towers-are-populated} infers from the observed dark remainder, then",
    "If the four odd towers hold matter, which Premise \\claimref{dark-matter.odd-towers-populated} now postulates on the inference of Observation \\claimref{dark-matter.which-towers-are-populated} from the observed dark remainder, then")
t = t[:m.start(1)] + f + t[m.end(1):]
t, v = bookkeep(t, 'wording: the population of the odd towers is now a registered premise', 'restatement',
    'the text gave the population of the odd towers as an inference only; since 10 November it is the registered premise dark-matter.odd-towers-populated',
    'Version 6 -> 7. One clause reworded; no edge added and the prediction is unchanged.')
save(p, t)

p, t = load('claims', 'neutrino.double-prediction-sum-predicted-floor')
t = append_level(t, 'formal', r"""\emph{Note (2026-11-11).} The condition named above as unused is now adopted: it is the field-space premise (FS) (\claimref{%s}), on which the $w = -1$ prediction is registered (\claimref{pred.dark-energy-w-minus-one}). The two stances are exposed in opposite senses (\claimref{pred.neutrino-mass-sum-floor}, Note): the bound below the floor is obtained with $w = -1$ held, so if $w = -1$ falls by its registered rule the floor is relieved, not refuted. ``One joint prediction'' above is to be read with that.""" % FS)
t, v = bookkeep(t, 'note: the condition of w = -1 is now (FS), and the two stances are exposed in opposite senses', 'restatement',
    'the text called the condition of the w = -1 prediction unused, while the store now adopts it as (FS), and called the two stances one joint prediction, against the note of pred.neutrino-mass-sum-floor',
    'Version 1 -> 2. A note is added to the formal level; the observation is otherwise unchanged.')
save(p, t)

# ---- open problem: two attack items
op = open('store/open_problems.yaml').read()
a = op.index('- id: op.pre-descent-theory'); s = op.index('\n  success: >-', a)
item = r"""
    - >-
      Decide whether the discrete element $\operatorname{Ad}(I_{4})$, by which the tower of reversed signature
      shares the field-space connection (Remark of
      \claimref{synthesis.frozen-point-unique-for-the-field-space-connection}), bears on the orientation clause
      (P1b), and whether the normalisation $c_{r} = \pm 1$ of the towers' frozen points can be derived.
    - >-
      Give the charge reading a statement in comoving terms: an identification of the boundary-mode windows
      of \claimref{synthesis.tower-charge-sector-label-temperature-not} with comoving regions of the two
      towers, under which equal sector labels are equal charge per comoving volume; without it the common $N$
      of (P1c) is what matches the two towers' mode sets."""
op = op[:s] + item + op[s:]
open('store/open_problems.yaml', 'w').write(op)
print('applied')
