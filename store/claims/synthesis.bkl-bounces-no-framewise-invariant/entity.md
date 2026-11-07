---
id: synthesis.bkl-bounces-no-framewise-invariant
kind: claim
version: 2
title: 'Under the BKL transition law: no framewise limit, no continuous invariant'
status: proved
region: synthesis
subject: interior
tags: [kasner, limits, no-go, schwarzschild]
proposed_by:
  kind: ai
  session: 2026-10-22-toe
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
derivations:
- name: main
  uses:
  - interior.weighted-limit-theorem@6
  - interior.kasner-form-interior@6
  - sheaf.collision-census@2
  - dark-energy.wall-counterterm@4
  - interior.boosts-generate-exactly-levi-factor@5
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_bkl_bounces
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - interior.weighted-limit-theorem
extraction:
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG sign (Leon 2026-10-23, referee GR1): the limiting tangential connection is displayed as -sum_i p_i B_i (x) theta^i, the sign of the rotation-gauge field of the definition (DICTIONARY C10); jumps, orbits and algebras unchanged. Check: the generated algebra is computed from -p_i B_i. Version 1 -> 2.'
  open_problem: op.generic-weighted-limit
  note: >-
    Answers the first attack line of the problem (the Kasner exponents modulo the BKL maps) negatively for
    framewise data and for every continuous function of the exponents, and records the two exact facts that
    organise the failure. The BKL transition law is taken as the model of a bounce (V. A. Belinskii, I. M.
    Khalatnikov and E. M. Lifshitz, Adv. Phys. 19 (1970) 525; the u-parametrisation is Khalatnikov-Lifshitz;
    cited from memory); that actual generic Einstein solutions follow it is the BKL picture, proved for Bianchi
    IX by H. Ringstrom (Ann. Henri Poincare 2 (2001) 405, cited from memory), not here. What does survive every
    bounce are the two Kasner relations and, while two exponents are nonzero, the generated algebra; those
    positive statements are not part of this claim. Transport-convenient: the
    objects are the limiting values of the Hubble-normalised connection of the weighted limit theorem.
---

## formal
Let a Kasner epoch be a triple $p = (p_{1}, p_{2}, p_{3})$ on the constraint variety $\sum p_{i} = 1$, $\sum p_{i}^{2} = 1$, carried by the axes of a fixed frame, with limiting tangential connection $\widehat\Omega_{0}(p) = -\sum_{i} p_{i} B_{i}\otimes\hat\theta^{i}$ (the sign of the rotation-gauge field of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}) as in Theorem \claimref{interior.weighted-limit-theorem}. Take as the model of a bounce the BKL transition law: if $p_{a} < 0$, then $p'_{a} = -p_{a}/(1 + 2p_{a})$ and $p'_{b} = (p_{b} + 2p_{a})/(1 + 2p_{a})$ for $b \neq a$; and write the ordered triple as $p(u) = (-u,\ 1 + u,\ u(1 + u))/(1 + u + u^{2})$, $u \geq 1$. The bounce lemma (the law preserves both Kasner relations and acts as $u \mapsto u - 1$, followed by $u \mapsto 1/(u - 1)$ at the end of an era, each era ending in an epoch with $1 \leq u \leq 2$) is filed alongside, synthesis.bkl-bounce-invariant-holonomy-and-bound, and is recalled in the proof; on $p(u)$ the bouncing axis receives $p_{2}(u - 1) > 0$.
\begin{enumerate}
\item[(i)] \emph{(No framewise limit, if the approach follows the BKL law.)} Suppose the approach to the singularity passes through the sequence of epochs that the transition law generates. At a bounce from an epoch with $1 \leq u \leq 2$ the coefficient of the fixed boost $B_{a}$ in $\widehat\Omega_{0}$ jumps by $u/(u^{2} + u + 1) + u/(u^{2} - u + 1) \geq 20/21$. Every era (maximal run of steps $u \mapsto u - 1$) ends with such an epoch, and for irrational initial $u$ there are infinitely many eras, so the fixed-frame values $\widehat\Omega_{0}(p^{(n)})$ along the bounce sequence are not Cauchy.
\item[(ii)] \emph{(Rational orbits.)} For rational $u = [a_{0}; a_{1}, \ldots, a_{k}]$ the orbit reaches $u = 1$, the Schwarzschild exponents $(-\tfrac13, \tfrac23, \tfrac23)$ of Lemma \claimref{interior.kasner-form-interior}, after $a_{0} + \cdots + a_{k} - 1$ bounces, and the next bounce sends them to $(1, 0, 0)$, where no exponent is negative and the orbit stops. These are the two collision points of Proposition \claimref{sheaf.collision-census}. At $(1, 0, 0)$ the triple is outside the admissible class of Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible} ($p_{i} \neq 0$ fails) and the limiting values generate the one-dimensional algebra $\R B_{a}$ (the Taub point, flat Kasner; also recorded alongside), against $\Lambda^{2}W \cong \mathfrak{so}(1,3)$ at every other epoch, where all three exponents are nonzero.
\item[(iii)] \emph{(No continuous invariant; standard.)} Every continuous function of the unordered triple that is invariant under the transition law is constant. In particular $e_{3} = p_{1}p_{2}p_{3}$, the coordinate of the unordered triple ($e_{1} = 1$, $e_{2} = 0$ being fixed) and, times eight, the coefficient of the wall counterterm of Theorem \claimref{dark-energy.wall-counterterm}, changes at every bounce except one from the epoch $u = (1 + \sqrt5)/2$, the fixed point of the map. The absence of nonconstant continuous invariants is classical for the Gauss-map dynamics of the BKL parameter and is transport-absent; the content specific to the series is its consequence for the limiting connection and for the wall counterterm.
\end{enumerate}

## technical
Near a generic singularity the BKL picture replaces a single Kasner regime by a sequence of Kasner epochs joined by bounces, each governed by an explicit rational law on the exponents. Working with that law exactly, and assuming the approach follows it: once per era the bounce moves the coefficient of one fixed boost by at least $20/21$, so for an irrational $u$, with infinitely many eras, the fixed-frame limit of the weighted limit theorem does not exist. For a rational $u$ the orbit is Euclid's algorithm: it ends, after as many bounces as the sum of the partial quotients, at Schwarzschild's exponents and then at the Taub point $(1, 0, 0)$ (flat Kasner), where admissibility fails and the generated algebra collapses from $\mathfrak{so}(1,3)$ to a line. Because every rational orbit reaches the same point, any continuous function (a classical fact about this map) of the exponents that every bounce preserves is constant; in particular the wall counterterm's coefficient $8p_{1}p_{2}p_{3}$ changes at every bounce except from the golden-ratio epoch.

## lay
Close to a generic singularity, space is thought to stretch and squeeze in a sequence of stages, with abrupt switches between them. Each stage is described by three numbers, and the switches follow a precise rule. Applying that rule exactly shows that the series' limit statement, written in a fixed set of directions, cannot survive the switches: once in each long run of stages one of its numbers jumps by almost one, forever. No smooth quantity built from the three numbers survives the switches either. A special set of starting values ends after finitely many switches, always passing through the values of a Schwarzschild black hole's singularity and then stopping at the values of flat space seen by an accelerated observer.

## one-liner
If the approach follows the BKL transition law, the fixed-frame weighted limit jumps by at least $20/21$ once per era (no framewise limit for irrational $u$), every continuous invariant of the exponents is constant (so $8p_{1}p_{2}p_{3}$ changes at every bounce except at the golden epoch), and every rational orbit ends at Schwarzschild's $(-\tfrac13, \tfrac23, \tfrac23)$ and then the inadmissible Taub point $(1, 0, 0)$.
