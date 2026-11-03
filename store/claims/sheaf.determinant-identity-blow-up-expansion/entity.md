---
id: sheaf.determinant-identity-blow-up-expansion
kind: claim
version: 3
title: The determinant identity, and the blow-up expansion
status: proved
region: sheaf
subject: walls
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
- obj.sheaf.collar-data-coupling
derivations:
- name: main
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T04.py
  tags:
  - num:4.3
- kind: check
  ref: check.py::check_schur_complement_and_determinant_identity
- kind: check
  ref: check.py::check_blow_up_expansion
locators:
  paper: T04
  number: Lem 4.3
  label: lem:det
  line: 581
extraction:
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: the Schur complement, det h = det G (-(1 + 2 mu nu beta^2 s)) on three collar models and four couplings, and tau s -> 1/lambda''(0) with an O(1) remainder. Version 1 -> 2. Sample inputs moved to module level; pole and sign tests rewritten in equivalent forms; no change to what is tested. Version 2 -> 3.'
  env: lemma
  unresolved_refs:
  - rem:coords
  typing:
    by: ai-typing-pass
    note: "no premise edges needed; added about: obj.sheaf.collar-data-coupling since h, e, beta, mu and nu are the collar data of that definition"
---

## formal
On the collar minus $\Sig$ (where $G$ is invertible), set
\[
s \;:=\; G^{-1}(e, e) \qquad (e = \text{evaluation at } u) .
\]
Then, in any local frame of $T^*M$ extended by $(\nO, \nInf)$:
\begin{enumerate}
\item the Schur complement of the $G$-block in the Gram matrix of $h$ is
\[
\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} - \beta^2 s \begin{pmatrix} \nu^2 & \mu\nu \\ \mu\nu & \mu^2 \end{pmatrix},
\qquad \det = -\bigl(1 + 2\mu\nu\beta^2 s\bigr),
\]
and hence, exactly,
\[
\det h \;=\; \det G \cdot \bigl(-\bigl(1 + 2\mu\nu\beta^2 s\bigr)\bigr) ;
\]
\item along any transversal with parameter $\tau$ as in Remark \ref{rem:coords},
\[
s \;=\; \frac{1}{\lambda} + O(1),
\]
with the $O(1)$ term locally uniform on the collar. In particular $s \to +\infty$ on the side where $\lambda > 0$ and $s \to -\infty$ on the side where $\lambda < 0$, as the wall is approached.
\end{enumerate}

## technical
On the collar minus the wall, where $G$ is invertible, put $s = G^{-1}(e, e)$, with $e$ evaluation at the transversal $u$. Block elimination of the Gram matrix of the ambient form $h$, in a frame of $T^*M$ extended by $(\nO, \nInf)$, gives the Schur complement $\begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} - \beta^2 s \begin{pmatrix} \nu^2 & \mu\nu \\ \mu\nu & \mu^2 \end{pmatrix}$ and hence the exact identity $\det h = \det G \cdot \bigl(-(1 + 2\mu\nu\beta^2 s)\bigr)$.

Along any transversal, $s = 1/\lambda + O(1)$ with the error locally uniform on the collar, where $\lambda$ is the dying eigenvalue. So $s \to +\infty$ as the wall is approached from the side where $\lambda > 0$, and $s \to -\infty$ from the side where $\lambda < 0$.

## lay
The enlarged geometry built around a degenerating wall has a determinant that factorises exactly into the original determinant times a simple correction factor. The correction involves a quantity that blows up as the wall is approached, like one over the vanishing eigenvalue, with opposite signs on the two sides. Knowing exactly how it blows up is what lets one control where the enlarged geometry stays non-degenerate.

## one-liner
Off the wall within the collar, $\det h = \det G \cdot \bigl(-(1 + 2\mu\nu\beta^2 s)\bigr)$ exactly, and $s = 1/\lambda + O(1)$ diverges with the sign of $\lambda$ as the wall is approached.
