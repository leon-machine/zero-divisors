---
id: singularity.imported-induced-geometry-interior-slice
kind: claim
version: 2
title: 'Imported: the induced geometry of an interior slice'
status: imported
region: singularity
subject: entropy
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
  source: authorship disclosure of T05, deposited version
review: typed
imported_from:
- citation: 'none given: the source says the result is read off the static form of the metric in its own
    appendix'
locators:
  paper: T05
  number: Fact 10.5
  label: fact:slice
  line: 2161
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'Restated in Gauge Theory Gravity: the slice is the background surface r = r_c of the Painleve-Gullstrand gauge field and its induced metric is read from hb^{-1} on its tangent vectors (Q(hb^{-1}(e_t)) = 1 - 2M/r_c); on r = const the static and PG times differ by a function of r only, so the induced metric is the same, and the static chart, singular at the horizon, is not needed.'
  env: fact
  flags:
  - 'labelled imported but derived in the paper: candidate to become a proved claim'
  typing:
    by: ai-typing-pass
    note: Left as imported, as the status rules give no route from imported to proved; the extraction
      flag that the paper reads it off its own appendix still stands for a reviewer.
---

## formal
Inside the horizon, for the Schwarzschild field in the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$, $\beta = \sqrt{2M/r}$, of Fact \claimref{sheaf.gauge-field-cometric}, the background surface $r = r_c$ ($0 < r_c < 2M$) is spacelike: its tangent vectors $e_t$, $e_\theta$, $e_\phi$ have physical squares $Q(\hb^{-1}(e_t)) = 1 - 2M/r_c < 0$ and $-r_c^{2}$, $-r_c^{2}\sin^{2}\theta$ in the coordinate normalisation, so its induced metric is $ds_3^{2} = |f(r_c)|\,dt^{2} + r_c^{2}\,d\Omega^{2}$ with $|f(r_c)| = 2M/r_c - 1$: Killing time $t$ is a spatial coordinate along it. On a surface of constant $r$ the static time and the Painlev\'e-Gullstrand time differ by a function of $r$ alone, so this is also the induced metric read in the static chart. \emph{Provenance:} this is read off the static form of the metric, Appendix \ref{app:metric}, with $f < 0$ for $r < 2M$.

## technical
Inside the horizon, for $0 < r_c < 2M$, the background surface $r = r_c$ of the Painlev\'e-Gullstrand gauge field is spacelike: the physical square of its time direction, $Q(\hb^{-1}(e_t)) = 1 - 2M/r_c$, is negative. Its induced metric is $ds_3^{2} = |f(r_c)|\,dt^{2} + r_c^{2}\,d\Omega^{2}$ with $|f(r_c)| = 2M/r_c - 1$, the same in the static chart since the two times differ by a function of $r$ on the slice.

Killing time $t$ is therefore a spatial coordinate along the slice. The result is read off the static form of the Schwarzschild metric, using $f < 0$ for $r < 2M$.

## lay
Inside a black hole the roles of space and time swap, so a surface at fixed radius is a slice of space rather than a moment of time. Described by the gravitational field on flat spacetime, the background direction of outside clock time has become spacelike there, stretched by a factor that depends on the radius. This is read directly from the standard form of the black-hole field.

## one-liner
Inside the horizon the background surface $r = r_c$ of the Painlev\'e-Gullstrand field is spacelike, with induced metric $|f(r_c)|\,dt^2 + r_c^2\,d\Omega^2$, so Killing time is a spatial coordinate on it.
