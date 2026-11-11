---
id: transport.obstructions-are-moved-never-destroyed
kind: claim
version: 3
title: Obstructions are moved, never destroyed
status: conjectured
region: transport
subject: zero-divisors
tags: [degenerate-algebras, obstruction-types]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
- name: Claude Fable 5.2
  role: 'restatement: completion read strictly, hypothesis moved beyond the tame corank-one case, note on the rung count'
  version: 3
  source: 'maintainer pass of 2026-11-11 (run 2026-11-11-contradictions)'
amendments:
- version: 3
  kind: restatement
  defect: 'the hypothesis (degenerating tamely) was the case already proved while the text said the pattern is not an artefact of the tame case, and completion was undefined: read loosely the statement is contradicted on tame walls by clauses (2) and (3) of synthesis.wall-class-one-rung-obstruction'
review: typed
lineage:
  motivated_by:
  - transport.fusion-occurs-most-once
  - transport.no-transport-terminates
  - sheaf.one-sided-completion
  - sheaf.conservation-degeneracy-located
  - synthesis.wall-class-one-rung-obstruction
  - synthesis.wall-rung-count-is-height-of-dying-line-class
about:
- obj.transport.obstruction-types
locators:
  paper: T01
  number: Conj 7.9
  label: conj:conservation
  line: 1555
extraction:
  maintainer_pass_2026_11_11:
    by: maintainer-2026-11-11
    date: '2026-11-11'
    note: 'Version 2 -> 3. The deposited wording (T1 Conjecture 7.9, checked against T01_transport_principle.tex line 1555) is kept under source_formal. Status unchanged (conjectured).'
  source_formal: 'Proposition \claimref{transport.no-transport-terminates} is the zero-dimensional instance of a principle the transport programme repeatedly meets: a completion never removes degeneracy, it relocates it. We conjecture the following family form. For any family of quadratic forms degenerating tamely along a locus (in the sense of the series'' sheaf-theoretic paper \cite{ButlerT4}), any completion of the family that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other side; no completion is nondegenerate globally. The one-sided completion theorem and shadow wall of that paper prove exactly this for tame corank-one degenerations; the conjecture asserts the pattern is not an artefact of the tame case, and asks for the cohomological invariant that measures it, presumably a class built from the mod-8 residues on the two sides of the wall, the state machine of Proposition \claimref{transport.fusion-occurs-most-once} evaluated in families.'
  env: conjecture
  context_refs:
  - transport.fusion-occurs-most-once
  - transport.no-transport-terminates
  typing:
    by: ai-typing-pass
    note: 'Conjecture: lineage already present; levels only.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: []
    added_about: [obj.transport.obstruction-types]
    verdict: standalone
    note: 'Open conjecture, so nothing proved rests on it (the wall-class conjecture already cites it in lineage); added to motivated_by the one-sided completion theorem and the located conservation of degeneracy, which the statement names as proving the tame corank-one case.'
---

## formal
Proposition \claimref{transport.no-transport-terminates} is the zero-dimensional instance of a principle the transport programme repeatedly meets: a completion never removes degeneracy, it relocates it. The family form is conjectured as follows. A \emph{completion} of a family of quadratic forms $G$ is a standard one: a form $h = G \perp K$ on a larger bundle, with $K$ nondegenerate on a complement and of the same signature on every region where $G$ is nondegenerate (the reading of Theorem \claimref{sheaf.conservation-degeneracy-absolute-form}). \emph{Conjecture.} For a family degenerating along a locus where one of the tameness hypotheses (T1) to (T3) of \claimref{sheaf.tameness} fails (higher corank, a degeneration that is not first-order, or a locus that is not a smooth hypersurface), any completion that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other side, so that no completion is nondegenerate globally; and a cohomological invariant measures the displaced degeneracy, presumably a class built from the mod-8 residues on the two sides of the wall, the state machine of Proposition \claimref{transport.fusion-occurs-most-once} evaluated in families. For tame corank-one degenerations the statement is proved: the one-sided completion theorem and the shadow wall (Theorem \claimref{sheaf.one-sided-completion}), and Theorem \claimref{sheaf.conservation-degeneracy-absolute-form} with clause (1) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction}, where the obstruction is the clock mismatch $2 \in \mathbb{Z}_{8}$.

\emph{Note (what is not conjectured, 2026-11-11).} The deposited wording (T1, Conjecture 7.9, kept under source\_formal) states its hypothesis as ``degenerating tamely'', which is the proved case, while asserting that the pattern is not an artefact of the tame case, and it does not say what a completion is. Read loosely, with the exterior model allowed to change across the wall, the statement would be false on tame walls: clauses (2) and (3) of Theorem \claimref{synthesis.wall-class-one-rung-obstruction} give forms nondegenerate at every point and of one signature. There the obstruction is not destroyed either, but it is paid for in rungs and not in a displaced wall: a completion by $k$ hyperbolic planes needs $w_{1}(\shL)^{k} = 0$ (Theorem \claimref{synthesis.wall-rung-count-is-height-of-dying-line-class}), the class of the dying line is conserved along the wall sequence (Theorem \claimref{synthesis.twisted-wall-induction-conserves-dying-line-class}), and the stored counts on lens walls grow with the dimension. The sheaf-level form of the question is Conjecture \claimref{sheaf.wall-class}.

## technical
Conjectured, in the strict reading: a completion is $G \perp K$ with one signature of $K$ on every region where $G$ is nondegenerate. For families degenerating beyond the tame corank-one case, any such completion that is nondegenerate of constant signature on one side of the locus degenerates on a displaced locus on the other, and a cohomological invariant, presumably built from the mod-8 residues on the two sides, measures it. The tame corank-one case is proved (the one-sided completion theorem and the shadow wall; the obstruction is the clock mismatch $2 \in \mathbb{Z}_{8}$).

With the exterior model allowed to change across the wall the statement would be false on tame walls, where nondegenerate forms of one signature exist; the obstruction is then paid for in rungs, counted by the class of the dying line.

## lay
Each repair of a failure of division seems to create a new failure somewhere else. This conjecture proposes that the same holds when the geometry varies from place to place: fixing a degeneration on one side of a boundary pushes it to a new boundary on the other side. That is proved in the simplest case, and conjectured beyond it. If the repair may use different extra structure on the two sides, the failure can be removed, but only by adding more structure, and how much must be added is itself a measure of the obstruction.

## one-liner
Conjecturally, beyond the tame corank-one case (where it is proved), no standard completion $G \perp K$ of a degenerating family of quadratic forms is nondegenerate globally: completion relocates the degeneration; with the exterior model allowed to change, the obstruction is instead paid for in rungs.
