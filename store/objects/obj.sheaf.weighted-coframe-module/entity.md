---
id: obj.sheaf.weighted-coframe-module
kind: object
version: 2
title: The weighted coframe module
status: defined
region: sheaf
subject: walls
tags: [schwarzschild]
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
- obj.synthesis.gtg-flat-spacetime-gauge-fields
locators:
  paper: T04
  number: Def 8.3
  label: def:W
  line: 883
extraction:
  env: definition
  typing:
    by: ai-typing-pass
    note: "Object: levels only."
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [scrambling.imported-collars-coframe-exceptional-set-helicity, sheaf.basic-properties-operational-characterisation, sheaf.chains-radial-dyad-rain-finite, sheaf.characterisation-forced-within-rain-bounded-class, sheaf.matching-connection-level, sheaf.one-sided-completion-singularity, sheaf.rain-duality, sheaf.schwarzschild-degeneration-boundary-tame, sheaf.uniqueness-weighted-module, singularity.imported-no-equivariant-value-wall, singularity.imported-one-sided-completion-singularity, three-routes.imported-boundary-gram-ladder, obj.sheaf.extensions]
    added_about: []
    verdict: connected
    note: 'About from the Schwarzschild statements written in the module W; the variable-weight theorems of Section 9 define their own A-module under the same letter and were not linked.'
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the coframe is placed on the flat background of the Painleve-Gullstrand gauge field hb = 1 - beta P, with t the background time label of that gauge and the one-forms paired with physical vectors through the coframe g^mu = hb^T(e^mu). Module and frame unchanged.'
---

## formal
Let $\Mt_u$ denote $\Mt$ with the quasihomogeneous smooth structure of order two at the boundary: smooth functions of $(u, t, \omega)$, $u = \sqrt{r}$. Define $\shW$ as the $C^\infty(\Mt_u)$-module with frame
\[
\rho := r^{1/2}\,dr \;(= 2u^2\,du), \qquad \dtPG, \qquad \mu_1 := r\,d\theta, \qquad \mu_2 := r\sin\theta\,d\phi ,
\]
where $t$ is Painlev\'e-Gullstrand time, the time label of the flat background in the gauge $\hb = 1 - \beta P$ of Fact \claimref{sheaf.gauge-field-cometric}, and $(r, \theta, \phi)$ are its spherical labels; the one-forms are background covectors, read against physical vectors through the coframe $g^\mu = \hb^{T}(e^\mu)$ of Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields} (the angular pair is a chart expression; the module they generate is global over the sphere).

## technical
Give $\Mt$ the quasihomogeneous smooth structure of order two at the boundary, in which smooth functions are smooth in $(u, t, \omega)$ with $u = \sqrt{r}$, and call the result $\Mt_u$. The weighted coframe module $\shW$ is the $C^\infty(\Mt_u)$-module with frame $\rho = r^{1/2}\,dr = 2u^2\,du$, $\dtPG$, $\mu_1 = r\,d\theta$ and $\mu_2 = r\sin\theta\,d\phi$, where $t$ is Painlev\'e-Gullstrand time, the time label of the flat background in the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$. The angular pair is a chart expression, but the module it generates is global over the sphere.

## lay
Near the Schwarzschild singularity the ordinary one-forms behave badly. The weighted coframe module replaces them by rescaled versions: a radial one weighted by the square root of the radius, two angular ones weighted by the radius, and the time of freely falling observers. To make the rescaled radial form smooth, smoothness near the singularity is measured in the square root of the radius.

## one-liner
$\shW$ is the module over $C^\infty(\Mt_u)$, $u = \sqrt r$, with frame $r^{1/2}\,dr$, $\dtPG$, $r\,d\theta$ and $r\sin\theta\,d\phi$, where $t$ is Painlev\'e-Gullstrand time.
