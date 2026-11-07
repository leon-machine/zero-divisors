---
id: interior.complex-factorisation-location-ring
kind: claim
version: 5
title: Complex factorisation and the location of the ring
status: proved
region: interior
subject: interior
tags: [kerr, pseudoscalar-and-centre, curvature-and-field-equations]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
review: typed
derivations:
- name: main
  uses:
  - interior.exact-scale-decoupling@4
  - interior.imported-kerr-curvature@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T06.py
  tags:
  - num:6.4
- kind: check
  ref: check.py::check_pseudoscalar_subalgebra_is_a_field
- kind: check
  ref: check.py::check_kerr_scale_times_shape
- kind: check
  ref: check.py::check_noninvertibility_locus_is_the_ring
- kind: check
  ref: check.py::check_a_zero_is_schwarzschild_from_gauge_fields
locators:
  paper: T06
  number: Prop 6.4
  label: prop:ring
  line: 809
extraction:
  maintainer_pass_ga_units:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Group F (found by the language check''s bare-unit detector): nothing replaced; the i stays and is declared outside_ga (bridge): the proof of (1) identifies the commutative subalgebra R + R I of Cl(1,3) with the complex numbers by x + Iy -> x + iy; the i is the unit of C on the other side of that comparison, which is the point of the clause.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: R + RI as a field, the Kerr scale times the shape operator with ratio 2:(-1), the ring as the non-invertibility locus, and the a = 0 case against the curvature computed from the Schwarzschild gauge fields. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5.'
  typing:
    by: ai-typing-pass
    added: [interior.imported-kerr-curvature]
    note: 'Added the imported Kerr curvature fact from context_refs since the scale and factorisation are read from it; the source says the criterion locates the ring correctly, matching the classical location already stated in that fact, but no imported claim gives the whole proposition, so no standard-route was added.'
  env: proposition
  context_refs:
  - interior.imported-kerr-curvature
  cite_pass:
    by: ai-cite-pass
    date: '2026-10-21'
    cited:
    - interior.imported-kerr-curvature
outside_ga:
  kind: bridge
  why: 'the proof of (1) identifies the commutative subalgebra R + R I of Cl(1,3) with the complex numbers by x + Iy -> x + iy; the i is the unit of C on the other side of that comparison, which is the point of the clause'
---

## formal
Write $\mathfrak{M} := -M\,(r - Ia\cos\theta)^{-3}$ for the scale in Fact \claimref{interior.imported-kerr-curvature}, so that $R(B) = -\tfrac{\mathfrak M}{2}(B + 3\sigma_rB\sigma_r) = \mathfrak{M}\,S(B)$ with $S = 1 - 3\Pi$ the shape operator of Proposition \claimref{interior.exact-scale-decoupling} built on the principal plane pair. Then:
\begin{enumerate}
\item the subalgebra $\R \oplus \R I \subset \Cl(1,3)$ is a field isomorphic to $\C$: $I^2 = -1$, and $z = x + Iy$ is invertible in it if and only if $z\tilde z = x^2 + y^2 \neq 0$, where $\tilde z := x - Iy$;
\item the Kerr curvature is the Schwarzschild curvature with $r^3$ replaced by $z^3 = (r - Ia\cos\theta)^3$ in the scale, $R = \mathfrak M\,S$ against Schwarzschild's $R = -(M/r^3)S$: same shape $S$, same identity $S^2 + S = 2$, same spectrum ratio $2{:}(-1)$, now with eigenvalues valued in $\C$;
\item for $a \neq 0$ the non-invertibility locus of the scale's base $z = r - Ia\cos\theta$ within the subalgebra is exactly $\{r^2 + a^2\cos^2\theta = 0\} = \{r = 0,\ \theta = \pi/2\}$: the ring. In particular the disc interior $\{r = 0,\ \theta \neq \pi/2\}$ carries an invertible scale and finite curvature: the framework's own criterion, invertibility within the algebra, locates the Kerr singularity correctly and accounts for the regularity of the disc without further input;
\item at $a = 0$ the factorisation reduces identically to Proposition \claimref{interior.exact-scale-decoupling}.
\end{enumerate}

## technical
Write the Kerr curvature scale as $\mathfrak M = -M(r - Ia\cos\theta)^{-3}$, so that the curvature operator is $R(B) = \mathfrak M\,S(B)$ with $S = 1 - 3\Pi$ the shape operator built on the principal plane pair. The subalgebra $\R \oplus \R I$ of $\Cl(1,3)$ is a field isomorphic to $\C$, since $I^2 = -1$, and $z = x + Iy$ is invertible in it exactly when $x^2 + y^2 \neq 0$. The Kerr curvature is therefore the Schwarzschild curvature with $r^3$ replaced by $z^3$: the same shape $S$, the same identity $S^2 + S = 2$ and the same eigenvalue ratio $2 : (-1)$, with eigenvalues now valued in $\C$.

For $a \neq 0$ the base $z = r - Ia\cos\theta$ fails to be invertible exactly on $r^2 + a^2\cos^2\theta = 0$, that is on the ring $r = 0$, $\theta = \pi/2$. The disc interior carries an invertible scale and finite curvature, so the criterion of invertibility within the algebra locates the Kerr singularity and accounts for the regular disc. At $a = 0$ the factorisation reduces to the Schwarzschild scale decoupling.

## lay
The curvature of a rotating black hole can be written as the curvature of a non-rotating one, with the radius replaced by a complex number built from the radius and the angle. The series' rule is that trouble arises where a quantity cannot be inverted. Applied to this complex number, the rule picks out exactly the ring where a rotating black hole is singular, and says that the disc spanning the ring is regular.

## one-liner
The Kerr curvature is the Schwarzschild shape operator times the complex scale $-M(r - Ia\cos\theta)^{-3}$ in $\R \oplus \R I \cong \C$, and the scale's base fails to be invertible exactly on the ring $r = 0$, $\theta = \pi/2$.
