---
id: odd-extensions.imported-tame-walls-exceptional-algebra-residue
kind: claim
version: 4
title: 'Imported: tame walls, the exceptional algebra, the residue, and conservation'
status: proved
region: odd-extensions
subject: walls
tags: [degenerate-algebras, no-go]
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
  - sheaf.conservation-degeneracy-absolute-form@4
  - sheaf.exceptional-algebra-deformation-normal-cone@5
  - sheaf.invariant-form-t3@2
  - sheaf.metrics-residue-square-root-twist@5
  assumes:
  - sheaf.tameness@1
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_tameness_conditions
- kind: check
  ref: check.py::check_signatures_and_exceptional_fibre
- kind: check
  ref: check.py::check_residue_is_inverse_transversality_datum
- kind: check
  ref: check.py::check_conservation_needs_constant_complement
locators:
  paper: T14a
  number: Fact 10.1
  label: fact:t4
  line: 733
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: (T1)-(T3), side signatures, exceptional fibre, residue k (x) k / delta and conservation on polynomial model walls and the Schwarzschild wall. Version 3 -> 4.'
  env: fact
  context_refs:
  - sheaf.conservation-degeneracy-absolute-form
  - sheaf.exceptional-algebra-deformation-normal-cone
  - sheaf.invariant-form-t3
  - sheaf.metrics-residue-square-root-twist
  flags:
  - 'fact restating several series results: derived from them'
  typing:
    by: ai-typing-pass
    note: 'Restating fact: kept the four series premises matching its provenance and the tameness postulate;
      the remark on signatures in its provenance has no separate store entity. Levels pass: all three
      plain levels now name the tameness hypothesis, and the lay level and one-liner keep the both-sides-nonempty
      condition on conservation.'
---

## formal
A pair $(M,G)$, $G$ a smooth symmetric form on a bundle over $M$, is a tame corank-one degeneration if (T1) the degenerate locus $\Sigma$ is a smooth closed hypersurface, (T2) the corank is exactly one on $\Sigma$ with the radical lines a smooth line bundle spanned locally by $k$, and (T3) the dying eigenvalue crosses zero at nonzero speed along every transversal, invariantly: the section $\delta(k \otimes k) = dg_{k}|_{\Sigma}$ of $\operatorname{Hom}(L^{\otimes 2}, N^{*}\Sigma)$ is nowhere zero. The signatures on the two sides differ by one unit, $(p,q)$ where the dying eigenvalue is positive against $(p-1, q+1)$. Rescaling the dying direction by $t^{-1/2}$ along a transversal gives a continuous family of nondegenerate algebras through the wall whose special fibre, the exceptional algebra, is the Clifford algebra of the surviving form orthogonal to the rate of degeneration, of signature $(p,q)$ on the side approached. The inverse form has a canonical simple pole at the wall whose residue is $\delta^{-1}$, giving $N^{*}\Sigma \cong L^{\otimes 2}$: the dying line is a square root of the conormal bundle and the adjoined partner line a square root of the normal bundle. Conservation, absolute form: for a tame wall with both sides nonempty, any symmetric form on any bundle containing the original, standard outside a neighbourhood of the wall in the sense of being $G \perp K$ there with $K$ nondegenerate of the \emph{same} signature on both exterior regions, degenerates somewhere; the constancy of $\operatorname{sig} K$ across the wall is necessary, a completion allowed to switch $K$'s signature being able to match the two sides. \emph{Provenance:} \cite[Hyp.~2.1, Lem.~2.2, Rem.~2.3, Prop.~6.1, Thm.~6.2, Thm.~5.1]{ButlerT4}.

## technical
A smooth symmetric form $G$ on a bundle over $M$ is a tame corank-one degeneration when its degenerate locus $\Sigma$ is a smooth closed hypersurface, the corank there is exactly one with radical lines forming a smooth line bundle $L$ spanned locally by $k$, and the dying eigenvalue crosses zero at nonzero speed, invariantly $\delta(k\otimes k) = dg_k|_\Sigma \neq 0$. The signatures on the two sides are $(p,q)$ and $(p-1,q+1)$. Rescaling the dying direction by $t^{-1/2}$ gives a continuous family of nondegenerate algebras whose special fibre, the exceptional algebra, is the Clifford algebra of the surviving form orthogonal to the rate of degeneration, of signature $(p,q)$ on the side approached. The inverse form has a canonical simple pole with residue $\delta^{-1}$, so $N^*\Sigma \cong L^{\otimes 2}$.

Conservation, absolute form: if both sides are nonempty, any symmetric form on a larger bundle that equals $G \perp K$ away from the wall, with $K$ nondegenerate of the same signature on both exterior regions, degenerates somewhere. The constancy of the signature of $K$ is necessary. Everything here holds for walls satisfying this tameness hypothesis, which the series takes as a premise.

## lay
This imports the basic theory of the mildest kind of degeneration, assuming the wall is tame in the series' sense: a geometry that loses exactly one direction along a smooth wall, and does so at a steady rate. On each side the geometry is regular, with one direction changing its sign across the wall, and a suitable rescaling gives a well-defined limiting algebra on the wall. If the wall has regions on both sides, the degeneracy cannot be removed by adding extra directions that look the same on both sides; it reappears somewhere.

## one-liner
Imported, under the tameness hypothesis: a tame corank-one wall has an exceptional algebra and a canonical residue giving $N^*\Sigma \cong L^{\otimes 2}$, and, if both sides are nonempty, no completion that is standard with the same signature on both sides removes its degeneracy.
