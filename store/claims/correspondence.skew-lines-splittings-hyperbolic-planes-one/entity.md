---
id: correspondence.skew-lines-splittings-hyperbolic-planes-one
kind: claim
version: 4
title: "Skew lines, splittings, hyperbolic planes: one datum"
status: proved
region: correspondence
subject: conformal-spacetime
tags: [hyperbolic-plane, conformal-spinors]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T09, deposited version
review: typed
derivations:
- name: main
  uses:
  - correspondence.spinor-identification@7
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T09.py
  tags:
  - label:prop:skewwitt
- kind: check
  ref: check.py::check_hyperbolic_plane_gives_skew_lines
- kind: check
  ref: check.py::check_splitting_gives_hyperbolic_plane
locators:
  paper: T09
  number: Prop 4.1
  label: prop:skewwitt
  line: 427
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: hyperbolic planes give skew lines and normalised splittings and back (round trip), and the mixed slot S_omega ^ S_pi is psi of {n0, ninf}^perp. Version 2 -> 3. Check strengthened: meeting-lines sample asserted to give two distinct lines (rank 3) before eps = 0; sample moved to module level. Version 3 -> 4.'
  env: proposition
  typing:
    by: ai-typing-pass
    note: 'Kept the single edge to the spinor identification, whose nullity criterion the proof uses.
      Levels pass: conditions already kept.'
  source_title: "Skew lines, splittings, hyperbolic planes: one datum"
  source_formal: |-
    The following three data on $\T$ determine one another naturally:
    \begin{enumerate}
    \item an ordered pair of skew (disjoint) lines $(L_\infty, L_0)$ in $\PT$, with a joint normalisation of scale;
    \item a direct-sum splitting $\T = \Som \oplus \Spi$ into two $2$-planes, with volume elements $N_\infty \in \Lambda^2\Som$, $N_0 \in \Lambda^2\Spi$ normalised by $\varepsilon(N_0 \wedge N_\infty) = 1$;
    \item a hyperbolic plane in $V_\C$ spanned by an ordered pair of null vectors $\nInf, \nO$ with $\ip{\nO}{\nInf} = 1$.
    \end{enumerate}
    Under the correspondence, the mixed subspace $\Som \wedge \Spi \subset \Lambda^2\T$ is exactly the orthogonal complement $\{\nO, \nInf\}^\perp$, of dimension four.
  ga_conversion:
    by: ai-ga-pass
    date: 2026-10-21
    note: "Renamed twistor space and projective twistor space to the conformal spinor space and its projective space (\\CS, \\PCS) in all levels and the proof. The hyperbolic plane is still taken in the complexified $V_\\C$ of the Fock model, as in the original."
---

## formal
The following three data on the conformal spinor space $\CS$ (twistor space) determine one another naturally:
\begin{enumerate}
\item an ordered pair of skew (disjoint) lines $(L_\infty, L_0)$ in $\PCS$, with a joint normalisation of scale;
\item a direct-sum splitting $\CS = \Som \oplus \Spi$ into two $2$-planes, with volume elements $N_\infty \in \Lambda^2\Som$, $N_0 \in \Lambda^2\Spi$ normalised by $\varepsilon(N_0 \wedge N_\infty) = 1$;
\item a hyperbolic plane in $V_\C$ spanned by an ordered pair of null vectors $\nInf, \nO$ with $\ip{\nO}{\nInf} = 1$.
\end{enumerate}
Under the correspondence, the mixed subspace $\Som \wedge \Spi \subset \Lambda^2\CS$ is exactly the orthogonal complement $\{\nO, \nInf\}^\perp$, of dimension four.

## technical
Three data on the conformal spinor space $\CS$ determine one another naturally: an ordered pair of skew lines $(L_\infty, L_0)$ in $\PCS$ with a joint normalisation of scale; a splitting $\CS = \Som\oplus\Spi$ into two planes with volume elements $N_\infty \in \Lambda^2\Som$, $N_0 \in \Lambda^2\Spi$ normalised by $\varepsilon(N_0\wedge N_\infty) = 1$; and a hyperbolic plane in $V_\C$ spanned by null vectors $\nInf$, $\nO$ with $\ip{\nO}{\nInf} = 1$. Under this correspondence the mixed subspace $\Som\wedge\Spi \subset \Lambda^2\CS$ is exactly the four-dimensional orthogonal complement $\{\nO, \nInf\}^\perp$.

## lay
Three different-looking pieces of structure turn out to be the same thing: a pair of non-intersecting lines in the projective spinor space, a splitting of the conformal spinor space into two planes, and a pair of lightlike directions of the kind the completion adds. Given any one, the other two follow. The four remaining directions, which mix the two planes, are exactly the directions perpendicular to the added pair.

## one-liner
An ordered pair of skew lines in the projective spinor space, a normalised splitting of the conformal spinor space into two planes and a normalised null pair in $V_\C$ determine one another, with the mixed slot equal to the orthogonal complement of the null pair.
