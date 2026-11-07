---
id: tower.compatibility-connecting-maps-transported
kind: claim
version: 7
title: 'Compatibility: the connecting maps, transported'
status: proved
region: tower
subject: tower
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T03, deposited version
- name: Claude Opus 5.5
  role: 'GA rewrite (declared: a statement in the matrix picture of the tower)'
  version: 7
  source: maintainer pass 2026-11-07 (consistency)
review: typed
about:
- obj.tower.tower
derivations:
- name: main
  uses:
  - tower.grade-twist-when-it-inner@4
  - tower.volume-elements-planes@5
  - transport.rule-1-morita-trivial@6
  - tower.commuting-copies@5
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T03.py
  tags:
  - num:5.2
- kind: check
  ref: check.py::check_identification_data
- kind: check
  ref: check.py::check_transported_connecting_map_is_ad_v_theta
- kind: check
  ref: check.py::check_naive_corrector_and_labelling_convention
locators:
  paper: T03
  number: Lem 5.2
  label: lem:compat
  line: 358
extraction:
  maintainer_pass_ga_rewrite:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 6 -> 7. Not rewritten: the result is the tower embedding transported into the matrix picture A (x) Mat_{2^k}(R) of the commuting-copies identifications (block doubling and the cornerwise corrector V_k), a statement about block matrices over the ground algebra as such; its proof already works with the Clifford elements (the twisted generators, the volume elements u_A and Omega_k, the plane idempotents) and reads their images. Declared outside_ga (bridge).'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: phi_{k+1}^{-1}(Ad(V_k) theta_k(z)) = phi_k^{-1}(z) on every basis element for nine grounds and floors, the identification data, the naive corrector failing for n >= 1, and the labelling dependence. Version 3 -> 4. Wording fix (Leon 2026-10-23): the sentence that exchanging vw and wv exchanges the corners of V_k is replaced by the computed one (with vw and wv exchanged for the new plane, diag(1, u_{T_k}) works and V_k does not; for n = 0 they coincide), and the neighbouring not-diag(1, u_{T_k}) sentence is qualified to this labelling and n >= 1 (formal, technical, lay). CASES widened with Cl(2,0) at k = 2 and Cl(0,2) at k = 1, matching docstring (2); all pass. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  env: lemma
  context_refs:
  - tower.commuting-copies
  typing:
    by: ai-typing-pass
    added: [tower.commuting-copies]
    note: 'Added commuting-copies, whose identifications varphi_k the statement is built on and the proof uses (x^(k) maps to x tensor 1); the three extracted edges are all used in the generator checks.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    cited:
    - tower.commuting-copies
outside_ga:
  kind: bridge
  why: 'the result is the tower embedding transported into the matrix picture A (x) Mat_{2^k}(R) of the commuting-copies identifications, block doubling followed by conjugation by a cornerwise block matrix over the ground algebra; the Clifford side (twisted generators, the volume elements u_A and Omega_k) is in the proof, and the statement is about the block matrices as such'
---

## formal
Let $p - q$ be even, $A := \Cl(p,q)$, and let $\varphi_k : T_k \to A \otimes \Mat_{2^k}(\R)$ be the identifications of Theorem \claimref{tower.commuting-copies}, with every plane's matrix units labelled as in Fact \claimref{transport.rule-1-morita-trivial} and the planes nested in order, the $(k{+}1)$-st plane carrying the outer index of $\Mat_{2^{k+1}} = \Mat_2(\Mat_{2^k})$. Write $\theta_k(z) := z \otimes 1_{2 \times 2}$ for block doubling in the outer index, $u_A \in A$ for the ground volume element, and $\overline\Omega_k \in \Mat_{2^k}(\R)$ for the image of $\Omega_k = \omega_1 \cdots \omega_k$. Then the transported connecting map $\psi_k := \varphi_{k+1} \circ \iota_k \circ \varphi_k^{-1}$ is
\[
\psi_k \;=\; \Ad(V_k) \circ \theta_k, \qquad
V_k \;:=\; \begin{pmatrix} u_A \otimes 1_{2^k} & 0 \\ 0 & 1_A \otimes \overline\Omega_k \end{pmatrix},
\]
with $V_k$ invertible ($u_A^2 = \pm 1$, $\Omega_k^2 = 1$). In this labelling and for $n = p + q \ge 1$, the corrector is \emph{not} the transported single-step corrector $\operatorname{diag}(1, u_{T_k})$ of Lemma \claimref{tower.grade-twist-when-it-inner}: transporting through $\varphi$ splits the correction across the two tensor legs, the ground volume acting in the first corner and the planes' volume in the second. The labelling convention of Fact \claimref{transport.rule-1-morita-trivial} matters: with $vw$ and $wv$ exchanged for the new plane, the transported single-step corrector $\operatorname{diag}(1, u_{T_k})$ is the one that works and $V_k$ is not; for $n = 0$ the two coincide.

## technical
Take $p - q$ even and $A = \Cl(p,q)$, and identify each floor with $A \otimes \Mat_{2^k}(\R)$ by the commuting-copies isomorphisms $\varphi_k$, with the planes nested in order and the newest plane carrying the outer matrix index. The tower embedding then becomes $\psi_k = \varphi_{k+1} \circ \iota_k \circ \varphi_k^{-1} = \operatorname{Ad}(V_k) \circ \theta_k$, where $\theta_k(z) = z \otimes 1_{2 \times 2}$ is block doubling and $V_k = \operatorname{diag}(u_A \otimes 1_{2^k},\ 1_A \otimes \overline\Omega_k)$ is invertible, $u_A$ being the ground volume element and $\overline\Omega_k$ the image of the planes' volume element.

In this labelling, and for $n = p + q \ge 1$, the corrector is not the transported single-step corrector $\operatorname{diag}(1, u_{T_k})$: transport splits the correction across the two tensor legs, the ground volume acting in the first corner and the planes' volume in the second. The labelling convention for the matrix units matters: with $vw$ and $wv$ exchanged for the new plane, the transported single-step corrector $\operatorname{diag}(1, u_{T_k})$ is the one that works and $V_k$ is not; for $n = 0$ the two coincide. The proof checks both sides on generators.

## lay
When each floor of the tower is rewritten as matrices over the ground algebra, the map from one floor to the next becomes simple block doubling followed by a conjugation. This result writes down the conjugating element exactly. It has two pieces sitting in the two diagonal corners, one built from the ground algebra's volume element and one from that of the added planes, rather than the single correction a one-step view would suggest (with the matrix units labelled as the store fixes them; with the other labelling the single correction is the right one).

## one-liner
For even charge the transported tower embedding is block doubling followed by conjugation by the invertible corrector $V_k = \operatorname{diag}(u_A \otimes 1_{2^k},\ 1_A \otimes \overline\Omega_k)$, which splits the correction across the two tensor legs.
