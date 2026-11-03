---
id: sheaf.chains-radial-dyad-rain-finite
kind: claim
version: 4
title: The chain's radial dyad is rain-finite
status: proved
region: sheaf
subject: walls
tags: [schwarzschild, null-directions]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T04, deposited version
review: typed
about:
- obj.sheaf.weighted-coframe-module
derivations:
- name: main
  uses:
  - sheaf.rain-duality@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_dyad_null_with_constant_rain_components
- kind: check
  ref: check.py::check_gauge_field_carries_flat_dyad_to_physical_dyad
- kind: check
  ref: check.py::check_dyad_in_geometric_algebra
locators:
  paper: T04
  number: Prop 8.23
  label: prop:dyad
  line: 1111
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: nullity and constant rain components of n_+-, the gauge map eta(L a, L b) = G(a, b) carrying the flat dyad to the physical one, as RF identities and in GA. Version 2 -> 3. Check maintenance: comparisons over zip now also compare lengths, so a length mismatch cannot pass on a shorter prefix; no change to what is claimed. Version 3 -> 4.'
  env: proposition
  context_refs:
  - sheaf.gauge-field-cometric
  typing:
    by: ai-typing-pass
    note: 'Kept rain duality, used for nullity and the components; the gauge-field fact names the map
      L, but the proof fixes L internally from the identity eta(La, Lb) = G(a, b), so it was not added
      (doubtful). Levels pass: conditions already kept.'
---

## formal
Let $n_\pm := k/\sqrt r \pm \dtPG$. Then, at every interior radius, exactly: $n_\pm$ are $G$-null; they are $\shW_{\mathrm{exc}}$-sections with \emph{constant unit} rain components, $n_\pm(V) = \pm 1$ and $n_\pm(e_{\hat r}) = 1$; and the gauge field of Fact \claimref{sheaf.gauge-field-cometric} carries the flat radial null dyad onto them,
\[
L^{-1}(\dtPG + dr) \;=\; n_+, \qquad L^{-1}(\dtPG - dr) \;=\; -\,n_- ,
\]
where $L$ is the covector action of the gauge field, fixed internally by the identity $\eta(L a, L b) = G(a,b)$ on all coordinate pairs. Hence the s-wave sector's physical null dyad, the radial structure on which the chain of \cite{ButlerT5} runs, is exactly finite in the infalling frame all the way to the wall, even though the individual coordinate legs are not.

## technical
Set $n_\pm = k/\sqrt r \pm \dtPG$. At every interior radius, exactly, the $n_\pm$ are $G$-null sections of $\shW_{\mathrm{exc}}$ with constant unit rain components, $n_\pm(V) = \pm 1$ and $n_\pm(e_{\hat r}) = 1$. The covector action $L$ of the gauge field, fixed by $\eta(La, Lb) = G(a,b)$, carries the flat radial null dyad onto them: $L^{-1}(\dtPG + dr) = n_+$ and $L^{-1}(\dtPG - dr) = -n_-$. So the physical radial null dyad of the s-wave sector, on which the chain runs, is exactly finite in the infalling frame all the way to the wall, although its coordinate legs are not.

## lay
The chain construction for black holes runs along the two light directions pointing inwards and outwards along the radius. This result shows that, as measured by an observer falling freely inwards, these light directions stay exactly finite all the way to the wall, even though the coordinates used to write them blow up. They are precisely the images of the flat-space light directions under the gauge field.

## one-liner
The null covectors $n_\pm = k/\sqrt r \pm \dtPG$ are the gauge-field images of the flat radial null dyad and have constant unit components in the infalling frame, so the chain's radial dyad is exactly finite up to the wall.
