---
id: sheaf.schwarzschild-degeneration-boundary-tame
kind: claim
version: 6
title: The Schwarzschild degeneration is boundary-tame in $\shW$
status: proved
region: sheaf
subject: singularity
tags: [schwarzschild, degenerate-algebras]
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
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - sheaf.gauge-field-cometric@3
  proof: proof-main.tex
checked_by:
- kind: proof
  derivation: main
- kind: check
  ref: check.py::check_gram_matrix_of_the_cometric
- kind: check
  ref: check.py::check_nondegenerate_off_the_wall
- kind: check
  ref: check.py::check_corank_one_on_the_wall
- kind: check
  ref: check.py::check_first_order_degeneration
- kind: check
  ref: check.py::check_schwarzschild_frame_transition
- kind: check
  ref: check.py::check_rain_identity
locators:
  paper: T04
  number: Thm 8.7
  label: thm:schwtame
  line: 913
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: cometric of hb = 1 - beta P on Cl(1,3): Gram matrix, det -r, signature, corank one at the wall with radical k, G(k,k) = -r, Schwarzschild frame transition, rain identity and D-parallel rain. Version 3 -> 4. Check migrated to the shared library (lib/gtg.py, lib/fock.py, lib/series.py); same check functions, asserted values and premises. Version 4 -> 5. Check strengthened: the frame transition matrix is solved from the frames and compared with the hand-written unitriangular matrix before its determinant is taken. Version 5 -> 6.'
  env: theorem
  unresolved_refs:
  - ex:eigenentry
  typing:
    by: ai-typing-pass
    note: "kept the single edge to the imported gauge-field fact, from which every entry is computed; the reference to the eigenvalue-versus-entry example is context only"
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Painleve-Gullstrand cometric is named as the derived cometric G(a,b) = hb^T(a).hb^T(b) of the stored gauge field hb = 1 - beta P; the infalling geodesic congruence is the free-fall congruence (D-parallel velocity) along the background direction d_t - beta d_r. Gram, determinant, radical and identities unchanged. Proof: one opening sentence pointing to the GTG dictionary Fact.'
---

## formal
On the frame $(\rho, \dtPG, \mu_1, \mu_2)$ of $\shW$, the derived cometric $G(a,b) = \hb^{T}(a) \cdot \hb^{T}(b)$ of the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ of Fact \claimref{sheaf.gauge-field-cometric} (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) has Gram matrix
\[
G(r) \;=\;
\begin{pmatrix}
m^2 - r & -m & 0 & 0\\
-m & 1 & 0 & 0\\
0 & 0 & -1 & 0\\
0 & 0 & 0 & -1
\end{pmatrix},
\]
with entries polynomial in $r$, hence extending smoothly to $E$. Moreover:
\begin{enumerate}
\item (nondegeneracy off the wall) $\det G = -r$, so $G$ is nondegenerate of signature $(1,3)$ at every $r > 0$, the horizon included;
\item (corank one) at $E$ the Gram has rank exactly three; the radical is the line spanned by
\[
k \;=\; \rho + m\,\dtPG ,
\]
and the $G$-orthogonal complement $V_1 = \langle \rho, \mu_1, \mu_2\rangle$ is nondegenerate, carrying the form $\mathrm{diag}(m^2, -1, -1)$ of signature $(1,2)$;
\item (first-order degeneration) $g_k := G(k,k) = -r$ \emph{exactly}, at every radius: the dying eigenvalue vanishes to precisely first order in the defining function $r$, with transversality datum $\delta(k \otimes k) = -\,dr|_E$, a nowhere-zero section of the $r$-conormal line $N^*_rE$ (Conventions);
\item (gauge robustness) the same module and the same radical are obtained from the Schwarzschild coordinate frame: the transition $\dtS = \dtPG + \tfrac{m}{m^2 - r}\rho$ is a smooth invertible change of $\shW$-frame at $E$, it diagonalises $G$, and $k = m\,\dtS + \tfrac{r}{r - m^2}\rho$, so that on $E$ the radical line is spanned by the Killing-time covector $\dtS$;
\item (the rain identity) $k = d\Phi$ with $\Phi = m t + \tfrac23 r^{3/2}$, and $k$ annihilates the infalling free-fall congruence (worldlines of $D$-parallel velocity) along the background direction $\partial_t - \beta\,\partial_r$ at \emph{every} radius: the dying direction is the conormal to the foliation ruled by the rain.
\end{enumerate}

## technical
In the frame $(\rho, \dtPG, \mu_1, \mu_2)$ of the weighted module $\shW$, the derived cometric of the Painlev\'e-Gullstrand gauge field $\hb = 1 - \beta P$ on flat spacetime has Gram matrix with $(\rho, \dtPG)$ block $\begin{pmatrix} m^2 - r & -m \\ -m & 1 \end{pmatrix}$ and angular block $\mathrm{diag}(-1, -1)$, with entries polynomial in $r$ and so extending smoothly to the boundary $E$. Then $\det G = -r$, giving signature $(1,3)$ at every $r > 0$, horizon included; at $E$ the rank is exactly three, with radical spanned by $k = \rho + m\,\dtPG$ and nondegenerate complement $\langle \rho, \mu_1, \mu_2 \rangle$ carrying $\mathrm{diag}(m^2, -1, -1)$, of signature $(1,2)$; and $Q(k) = G(k,k) = -r$ exactly, so the degeneration is first order with transversality datum $\delta(k \otimes k) = -\,dr|_E$.

The same module and radical arise from the Schwarzschild coordinate frame through the smooth invertible change of frame $\dtS = \dtPG + \tfrac{m}{m^2 - r}\rho$, and on $E$ the radical is spanned by $\dtS$. Finally $k = d\Phi$ with $\Phi = m t + \tfrac23 r^{3/2}$, and $k$ annihilates the infalling free-fall congruence along $\partial_t - \beta\,\partial_r$ at every radius.

## lay
At the centre of a Schwarzschild black hole the gravitational field is singular. Once the singularity is opened up into a boundary and suitably rescaled directions are used, the field's measure of lengths extends smoothly to that boundary and degenerates there in the mildest possible way: exactly one direction loses its length, and it does so at a linear rate. That dying direction is the same in two standard coordinate systems, and it is perpendicular to the slices traced out by observers falling freely inward.

## one-liner
In the weighted module at the blown-up Schwarzschild singularity, the derived cometric of the Painlev\'e-Gullstrand gauge field extends smoothly to the boundary and degenerates there with corank exactly one and to exactly first order, with radical $k = \rho + m\,\dtPG$ annihilating the infalling congruence.
