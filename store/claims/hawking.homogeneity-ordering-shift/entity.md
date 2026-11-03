---
id: hawking.homogeneity-ordering-shift
kind: claim
version: 6
title: The homogeneity $-2s-2$ is the ordering shift
status: proved
region: hawking
subject: thermality
tags: [conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T07, deposited version
review: typed
derivations:
- name: main
  uses:
  - hawking.imported-twistor-storey-ordering-shift@6
  - hawking.imported-penrose-transform@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T07.py
  tags:
  - label:prop:homogeneity
- kind: check
  ref: check.py::check_palatial_sign_of_realisation
- kind: check
  ref: check.py::check_charge_is_minus_hbar_euler_plus_two
- kind: check
  ref: check.py::check_homogeneity_iff_helicity
- kind: check
  ref: check.py::check_offset_is_the_ordering_shift
locators:
  paper: T07
  number: Prop 5.2
  label: prop:homogeneity
  line: 575
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: q(id) = -hbar(Upsilon + 2) as an operator identity (and -hbar(Upsilon + n/2) for n variables), helicity iff h = -2s - 2, and the offset as the symmetric-ordering shift. Version 4 -> 5. Sample inputs moved to module level; no change to what is tested. Version 5 -> 6.'
  env: proposition
  context_refs:
  - hawking.imported-penrose-transform
  outside_pilot_cites:
  - ButlerT9[Thm.~5.7]
  typing:
    by: ai-typing-pass
    added:
    - hawking.imported-penrose-transform
    note: Added the Penrose transform because the statement's closing clause (the transform's classification
      parameter is the completion's charge) is obtained by combining with it; the operator identity itself
      needs only the ordering-shift fact. The existing pin on that fact is @1 while it is now at version
      2; left for the repin pass.
  source_title: 'The homogeneity $-2s-2$ is the ordering shift'
  source_formal: |-
    On twistor functions, realise the palatial relation of Fact \claimref{hawking.imported-twistor-storey-ordering-shift} by $\bar Z_\nu = -\hbar\,\partial/\partial Z^\nu$ (the realisation with the palatial sign $[Z^\mu, \bar Z_\nu] = +\hbar\,\delta^\mu_\nu$), let $\Upsilon := Z^\mu \partial_\mu$ be the homogeneity (Euler) operator, its eigenvalue written $\mathsf{h}$ in sans serif to keep it clear of the one-particle Hamiltonian $h$, and let the helicity operator be one half the distinguished charge, $\mathsf{s} := \tfrac12\, q(\id)$, the standard twistor helicity operator \cite{Penrose1969, EPW1981} in the symmetric ordering that Fact \claimref{hawking.imported-twistor-storey-ordering-shift} forces storey-wide. Then, as an operator identity,
    \[
    q(\id) \;=\; -\hbar\,(\Upsilon + 2),
    \]
    so a twistor function homogeneous of degree $\mathsf{h}$ is an eigenfunction of $\mathsf{s}$ with eigenvalue $s\hbar$ if and only if
    \[
    \mathsf{h} \;=\; -2s - 2.
    \]
    The $-2$ is exactly the ordering shift: without the symmetric-ordering shift of $-\hbar/2$ per complex dimension the offset would vanish. Combined with Fact \claimref{hawking.imported-penrose-transform}, the classification parameter of the Penrose transform is the completion's own $\mathfrak{u}(1)$ charge, its offset supplied by the ordering. The computation is not new to the series: it appears, without being stated as a result, inside the proof of \cite[Thm.~5.7]{ButlerT9}, where T9's script also checks it; what this proposition adds is the statement at result level, in the transform's context, discharging the homogeneity half of the successor problem T9 assigns to this paper (the transform itself stays open).
  ga_conversion:
    by: ai-ga-pass
    date: '2026-10-21'
    note: 'Converted twistor functions to functions on $\CS$, the complex dimension of $\T$ to that of $\CS$ over $I_6$, and the twistor helicity operator to the helicity operator on $\CS$ (formal, all levels, proof). The palatial relation and $\bar Z$ are kept by name, as Penrose''s palatial programme; the computation is unchanged.'
  cite_pass:
    by: ai-cite-pass
    date: 2026-10-21
    stated_role:
    - hawking.imported-penrose-transform
    note: The proof proves the operator identity only; the closing sentence covers the statement's clause
      combining it with the transform.
---

## formal
On functions on the conformal spinor space $\CS$ (twistor functions), realise the palatial relation of Fact \claimref{hawking.imported-twistor-storey-ordering-shift} by $\bar Z_\nu = -\hbar\,\partial/\partial Z^\nu$ (the realisation with the palatial sign $[Z^\mu, \bar Z_\nu] = +\hbar\,\delta^\mu_\nu$), let $\Upsilon := Z^\mu \partial_\mu$ be the homogeneity (Euler) operator, its eigenvalue written $\mathsf{h}$ in sans serif to keep it clear of the one-particle Hamiltonian $h$, and let the helicity operator be one half the distinguished charge, $\mathsf{s} := \tfrac12\, q(\id)$, the standard helicity operator on $\CS$ (twistor helicity) \cite{Penrose1969, EPW1981} in the symmetric ordering that Fact \claimref{hawking.imported-twistor-storey-ordering-shift} forces storey-wide. Then, as an operator identity,
\[
q(\id) \;=\; -\hbar\,(\Upsilon + 2),
\]
so a function on $\CS$ homogeneous of degree $\mathsf{h}$ is an eigenfunction of $\mathsf{s}$ with eigenvalue $s\hbar$ if and only if
\[
\mathsf{h} \;=\; -2s - 2.
\]
The $-2$ is exactly the ordering shift: without the symmetric-ordering shift of $-\hbar/2$ per complex dimension (over the complex unit $I_6$) the offset would vanish. Combined with Fact \claimref{hawking.imported-penrose-transform}, the classification parameter of the Penrose transform is the completion's own $\mathfrak{u}(1)$ charge, its offset supplied by the ordering. The computation is not new to the series: it appears, without being stated as a result, inside the proof of \cite[Thm.~5.7]{ButlerT9}, where T9's script also checks it; what this proposition adds is the statement at result level, in the transform's context, discharging the homogeneity half of the successor problem T9 assigns to this paper (the transform itself stays open).

## technical
Realise the palatial relation $[Z^{\mu}, \bar Z_{\nu}] = \hbar\,\delta^{\mu}_{\nu}$ on functions on the conformal spinor space $\CS$ by $\bar Z_{\nu} = -\hbar\,\partial/\partial Z^{\nu}$, let $\Upsilon = Z^{\mu}\partial_{\mu}$ be the Euler operator with eigenvalue $\mathsf{h}$, and let the helicity operator be $\mathsf{s} = \tfrac12 q(\id)$ in the symmetric ordering. Then $q(\id) = -\hbar(\Upsilon + 2)$ as an operator identity, so a function homogeneous of degree $\mathsf{h}$ has helicity $s\hbar$ exactly when $\mathsf{h} = -2s - 2$.

The offset $-2$ is precisely the symmetric-ordering shift of $-\hbar/2$ per complex dimension of $\CS$, the complex unit being $I_6$; without it the offset would vanish. Combined with the Penrose transform, this makes the transform's classification parameter the completion's own $\mathfrak{u}(1)$ charge.

## lay
In Penrose's description of massless fields, a field's helicity is read off from how its function on the space of conformal spinors scales. This result shows that the particular offset in that rule, the "minus two", comes from the order in which quantum operators are multiplied at the framework's conformal level. The rule that sorts massless particles by helicity is therefore part of the framework's own algebra.

## one-liner
In the symmetric ordering $q(\id) = -\hbar(\Upsilon + 2)$, so a function on the conformal spinor space of homogeneity $\mathsf{h}$ has helicity $s$ exactly when $\mathsf{h} = -2s - 2$, the $-2$ being the ordering shift.
