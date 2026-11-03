---
id: synthesis.bkl-bounce-invariant-holonomy-and-bound
kind: claim
version: 2
title: What of the weighted limit survives the BKL bounces, for approaches that return to non-Taub Kasner models
status: proved
region: synthesis
subject: interior
tags: [kasner, limits, rotors-and-stabilisers]
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
derivations:
- name: main
  uses:
  - interior.weighted-limit-theorem@5
  - interior.boosts-generate-exactly-levi-factor@4
  - interior.transport-level-convergence-along-tangential-curves@4
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_circle_and_era_end
- kind: check
  ref: check.py::check_generated_algebra
- kind: check
  ref: check.py::check_bound_epoch_independent
- kind: proof
  derivation: main
about:
- obj.interior.weighted-blow-up-hubble-normalisation-admissible
- obj.synthesis.gtg-flat-spacetime-gauge-fields
extraction:
  open_problem: op.generic-weighted-limit
  note: >-
    The billiard half of the problem: replace the fixed Kasner frame by data that the BKL maps
    carry along, and ask which part of the weighted limit survives each bounce. Two parts do:
    the Gronwall constant of the transport comparison, because it uses only the quadric sum
    p_i^2 = 1 that every bounce preserves, and the values-level holonomy algebra Lambda^2 W,
    because the last epoch of every era has all three exponents at least 2/7 in size. The
    exponents and the frame do not survive. The result is stated for approaches that return,
    along a sequence of times, close to a non-Taub Kasner model; that a BKL approach with
    irrational parameter does so (once per era) is the BKL picture and Ringstrom's attractor
    theorem for Bianchi IX, cited from memory and not proved here. Transport-essential in its
    object, classical in its Kasner arithmetic. Fix round 2026-10-22-toe: the model's coframe is
    rotated with its bivectors; the bounce lemma and the one-dimensional algebra at the Taub point
    are cited (filed alongside, synthesis.bkl-bounces-no-framewise-invariant) instead of restated;
    the return hypothesis is in the title.
  maintainer_pass:
    by: maintainer-2026-10-23-gtg
    date: '2026-10-23'
    note: 'GTG restatement: the Einstein synchronous metric on the collar becomes a gravitational field (hb, Omega) in synchronous gauge with R(a) = Lambda a (store sign; Ric = Lambda g for the derived metric); the connection is the rotation-gauge field, the frame rotation a rotation-gauge transformation, the transport D-transport; geometry becomes gravitational field in technical and lay. Clauses (i)-(iii) unchanged; check unchanged. Fix (Leon 2026-10-23, referee GR1): displayed connection values re-signed to the GTG sign of the definition, D_a = a.nabla + Omega(a) x (Cartan forms omega^i_0 = sigma_i theta^i assemble to -sigma_i B_i; Hubble-normalised Kasner model -sum_i p_i B_i, DICTIONARY C10); content unchanged. Check: the generated algebra is now computed from the displayed values -p_i B_i.'
---

## formal
Let the gravitational field $(\hb, \Omega)$ on the collar of flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) be Einstein, $\mathcal{R}(a) = \Lambda a$ in the store's sign (so its derived metric has $\Ric = \Lambda g$), in synchronous gauge, with Hubble-normalised rotation-gauge field $\widehat\Omega_{\tau}$ on unit tangential directions as in Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}, but with no fixed Kasner data. Parametrise the Kasner circle $\sum_{i}p_{i} = \sum_{i}p_{i}^{2} = 1$ by the BKL parameter, $p(u) = \bigl(-u,\ 1 + u,\ u(1 + u)\bigr)/(1 + u + u^{2})$, $u \ge 1$, up to the order of the axes. For a Kasner point $p$ and a spatial rotation $R$ of the orthonormal physical frame (a rotation-gauge transformation), the Kasner model in the rotated frame $Re_{i}$ is $-\sum_{i}p_{i}\,(RB_{i}R^{-1})\otimes(R\hat\theta)^{i}$, with $(R\hat\theta)^{i}$ the coframe dual to $Re_{i}$ (the sign of the Definition's $\Omega$, as in Definition \claimref{obj.interior.weighted-blow-up-hubble-normalisation-admissible}).
\begin{enumerate}
\item[(i)] \emph{(Era ends.)} On the arc $1 \le u \le 2$, $\min_{i}|p_{i}(u)| \ge \tfrac27$, with equality only at $u = 2$. Every era of the BKL map ends in an epoch on this arc.
\item[(ii)] \emph{(The transport bound is bounce-invariant.)} At every time $\tau$, for every Kasner point $p$ and every rotation $R$, put $E_{\tau} := \widehat\Omega_{\tau} + \sum_{i}p_{i}\,(RB_{i}R^{-1})\otimes(R\hat\theta)^{i}$. For every tangential curve at time $\tau$ inside a compact $K$ of Hubble-normalised length $\lambda$, the $D$-transport and the transport of that Kasner model satisfy $\|T_{\gamma}(\lambda) - T^{0}_{\gamma}(\lambda)\| \le \lambda\|E_{\tau}\|_{K}\,e^{\lambda(1 + \|E_{\tau}\|_{K})}$, the bound of Theorem \claimref{interior.transport-level-convergence-along-tangential-curves} with the same constant whichever point of the Kasner circle, and hence whichever epoch or era, and whichever frame the model belongs to.
\item[(iii)] \emph{(The holonomy algebra is bounce-invariant.)} Suppose there are times $\tau_{k} \to 0$, Kasner points $p^{(k)} = p(u_{k})$ with $1 \le u_{k} \le 2$, and rotations $R_{k}$ such that $\|E_{\tau_{k}}\|_{K} \to 0$ for these models on every compact $K$. Then the accumulation values of $\widehat\Omega_{\tau}$ on unit tangential directions as $\tau \to 0$ include the three weighted boosts $-p_{i}\,RB_{i}R^{-1}$, $i = 1, 2, 3$, for some $p = p(u)$ with $1 \le u \le 2$ and some rotation $R$, and the Lie algebra generated by all accumulation values is exactly $\Lambda^{2}W \cong \mathfrak{so}(1,3)$. So clause (4) of Theorem \claimref{interior.weighted-limit-theorem} holds with limiting values replaced by accumulation values.
\end{enumerate}

## technical
Near a generic singularity the gravitational field passes through a sequence of Kasner epochs separated by bounces, and the weighted limit theorem, stated for one fixed set of Kasner exponents in one fixed frame, cannot apply as it stands. Two of its parts survive every bounce. The transport comparison along tangential curves holds at each time against whichever Kasner model is current, in whichever rotated frame, with the same constant, because that constant uses only $\sum p_{i}^{2} = 1$, which holds on the whole Kasner circle. And the algebra generated by the connection's values is still $\Lambda^{2}W \cong \mathfrak{so}(1,3)$ provided the approach keeps returning close to Kasner models on the arc where every exponent is at least $2/7$ in size, which contains the last epoch of every era.

The bounce map itself, and what it destroys (the exponents and the frame, with no framewise limit and no continuous invariant), are the subject of a companion result filed alongside, synthesis.bkl-bounces-no-framewise-invariant, which also records that at the Taub point (the flat Kasner point $(1,0,0)$ up to order) the values generate a one-dimensional algebra. Whether a given approach returns close to non-Taub models is a statement about the dynamics, which the BKL picture and the attractor theorem for Bianchi IX supply in the cases they cover; this result takes it as a hypothesis.

## lay
Close to a typical singularity, space does not settle into one pattern of stretching and squeezing but keeps switching between such patterns. An earlier result described the limit for one fixed pattern. This result shows what survives the switches: the size of the error in comparing paths with the simple model is controlled the same way in every pattern, and, provided the switching keeps passing through patterns where all three directions take part, the set of transformations the gravitational field generates in the limit is the same full set of Lorentz transformations. Which direction is stretched or squeezed does not survive.

## one-liner
For approaches that return to non-Taub Kasner models, the tangential transport bound holds epoch by epoch with one constant (it uses only $\sum p_{i}^{2} = 1$) and, since every era ends with $\min|p_{i}| \ge 2/7$, the accumulated values still generate $\Lambda^{2}W$.
