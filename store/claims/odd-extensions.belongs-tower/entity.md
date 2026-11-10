---
id: odd-extensions.belongs-tower
kind: claim
version: 5
title: $\Cl(I^{\perp})$ belongs to this tower
status: proved
region: odd-extensions
subject: tower
tags: [frozen-point, towers-by-residue]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T14a, deposited version
review: typed
derivations:
- name: main
  uses:
  - dark-matter.projection-every-towers-content-dilutes-ones@3
  - odd-extensions.are-ascents-pair-signed@4
  - odd-extensions.imported-frozen-point@8
  - odd-extensions.imported-copy-theorem-soldered-residue@5
  assumes:
  - dark-matter.p1-single-frozen-point@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_soldered_space_is_the_lorentz_frame
- kind: check
  ref: check.py::check_tower_charge_six_not_five_or_seven
- kind: check
  ref: check.py::check_isometry_carries_e_v_to_a_tangent_direction
- kind: proof
  derivation: main
locators:
  paper: T14a
  number: Prop 7.1
  label: prop:belongs
  line: 607
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: soldered space {I,V}^perp of signature (1,3) for every Lambda, residue 6 against the abstract residues 5 and 7, and the isometry of I^perp with R^{1,4} sending e_V to a tangent direction. Version 4 -> 5.'
  env: proposition
  context_refs:
  - odd-extensions.imported-copy-theorem-soldered-residue
  typing:
    by: ai-typing-pass
    added:
    - odd-extensions.imported-copy-theorem-soldered-residue
    - dark-matter.p1-single-frozen-point
    note: 'Added the copy-theorem fact, named in the statement as the reading of the residue the result
      works under, and assumed Premise P1, which the proof of (iii) invokes by name; kept the projection
      lemma, whose sourcing-rule reading of P1 supplies the shared four directions beyond which a fifth
      tangent direction is internal. Levels pass: the lay level and one-liner now state Premise P1 and
      the imported reading of the residue; the technical level names P1.'
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - odd-extensions.imported-copy-theorem-soldered-residue
---

## formal
Under the dark-matter paper's Theorem 3.5 the residue of a sector is the signature of the soldered vector space, the image of the tangent space in the algebra with $v^{2} = g(v,v)$ (Fact \claimref{odd-extensions.imported-copy-theorem-soldered-residue}). For the algebra $\Cl(I^{\perp})$ of Theorem \claimref{odd-extensions.are-ascents-pair-signed}:
\begin{enumerate}
\item[(i)] the soldered vector space is the Lorentz frame $\{I,V\}^{\perp} = e(TM)$, the image of the soldering form, of signature $(1,3)$ for every $\Lambda$ (Theorem \claimref{odd-extensions.are-ascents-pair-signed}(iv)); $V$ is not in it, being orthogonal to $e(TM)$ with $\nabla V = e$ (Fact \claimref{odd-extensions.imported-frozen-point});
\item[(ii)] hence $\Cl(I^{\perp})$ has tower charge $6$: it is a sub-object of this world's rung, the intermediate algebra of this world's own ascent, and not the ground shadow of the residue-$5$ or residue-$7$ tower whose abstract algebra it shares;
\item[(iii)] the coincidence $\Cl(I^{\perp}) \cong \Cl(1,4)$ for $\Lambda > 0$ is induced by an isometry of quadratic spaces ($I^{\perp}$ has signature $(1,4)$ outright) but by no map of soldered data: the isometry carries $e_{V}$, which is not soldered, to a fifth tangent direction of the five-dimensional shadow, which is, and carries the four-dimensional soldered space into a proper subspace of that shadow's tangent space.
\end{enumerate}

## technical
Read the residue of a sector, as the imported copy theorem does, as the signature of its soldered vector space: the image of the tangent space in the algebra, with $Q(v) = g(v,v)$. For the frozen point's algebra $\Cl(I^{\perp})$ the soldered space is the Lorentz frame $\{I,V\}^{\perp} = e(TM)$, of signature $(1,3)$ for every $\Lambda$, and the Stelle-West vector $V$ lies outside it. Hence $\Cl(I^{\perp})$ has tower charge $6$: it is a sub-object of this world's rung, not the ground shadow of the residue-$5$ or residue-$7$ tower whose abstract algebra it shares.

For $\Lambda > 0$ the isomorphism $\Cl(I^{\perp}) \cong \Cl(1,4)$ comes from an isometry of quadratic spaces but from no map of soldered data. Under the premise of one four-dimensional metric (P1), the isometry sends the unsoldered $e_V$ to a fifth tangent direction of a five-dimensional shadow and the four-dimensional soldered space into a proper subspace of that shadow's tangent space.

## lay
The algebra attached to the frozen point looks, as bare algebra, like the algebra of a five-dimensional dark tower. But under the reading the paper imports, which assigns towers by which directions are genuinely tied to spacetime, this algebra's tied directions are just the four ordinary spacetime directions. Assuming, as Premise P1 does, that there is one four-dimensional metric, its fifth direction is not a spacetime direction, so the algebra belongs to our own tower and not to a dark one.

## one-liner
With the residue read as the signature of the soldered space, and under P1, the frozen point's algebra $\Cl(I^{\perp})$ has charge $6$ and belongs to this world's tower, its coincidence with $\Cl(1,4)$ being algebraic and not a map of soldered data.
