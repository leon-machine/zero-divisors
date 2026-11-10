---
id: one-relation.measure-indifference-borns-rule-located
kind: claim
version: 4
title: 'Born''s rule located: the Dirac density; squared-norm weights under (P) for a sharp state'
status: proved
region: one-relation
subject: one-relation
tags: [indifference, measurement-and-records, recovers-known-physics]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T16, deposited version
- name: Claude Opus 5.5
  role: 'maintainer pass, uses edge to the imported envariance Fact at Leon''s decisions'
  version: 3
  source: maintainer pass 2026-11-07 (decisions)
- name: Claude Fable 5.2
  role: 'restatement: the stored result on the weights of a state sharp on an atom under Premise (P) in place of the imported envariance argument; statement narrowed to what that route covers'
  version: 4
  source: maintainer pass of 2026-11-10
review: typed
derivations:
- name: main
  uses:
  - one-relation.dirac-current-conserved-density@3
  - one-relation.imported-indifference-instrument@4
  - synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional@1
  - synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects@1
  assumes:
  - synthesis.premise-positivity-of-values@2
  proof: proof-main.tex
checked_by:
- kind: legacy
  script: verify_T16.py
  tags:
  - label:prop:born
- kind: check
  ref: check.py::check_density_is_positive_and_frame_relative
- kind: check
  ref: check.py::check_indifference_forces_equality_on_transitive_orbits
- kind: check
  ref: check.py::check_fine_graining_returns_squared_norms
- kind: check
  ref: check.py::check_squared_norm_of_the_split_is_the_dirac_density
- kind: check
  ref: check.py::check_sharp_state_weights_are_squared_norm_ratios
locators:
  paper: T16
  number: Prop 6.2
  label: prop:born
  line: 817
extraction:
  maintainer_pass_2026_11_10:
    by: maintainer-2026-11-10
    date: '2026-11-10'
    note: >-
      Version 3 -> 4, Leon's decision 4 of 10 November 2026 (replace the import). The fine-graining and
      continuity steps, which rested on the imported Fact one-relation.imported-envariance-born-rule, are
      replaced by the stored theorem that under Premise (P) a state sharp on an atom is that atom's
      scalar-part functional (clause (iii) of
      synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional); (P) is a new
      assumes edge; the residual postulate (weights exist and add) is identified with (P) through the stored
      result on weights on effects. The statement is narrowed, because the new route does not cover the
      statement of versions 1 to 3 as worded: it covers finite Clifford algebras over an ordered field,
      states of (P) sharp on an atom and projectors self-adjoint for the split; it does not cover the claim
      that the squared-norm measure is the only weight assignment consistent with vacuum indifference, the
      measure over space of the Dirac field, states not assumed sharp, or outcomes that act on a spinor
      through right multiplication. This is not a derivation of the Born rule: the non-contextuality
      assumption is relocated into (P), not removed. The title is changed to say what is located and under
      which premise; the old title was "The measure from indifference: Born's rule located". Two check
      functions added (the squared norm of the split is the Dirac density; the weights of the atom's
      functional are squared-norm ratios); the fine-graining check is kept as a comparison with the prior-art
      route. The envariance argument (W. H. Zurek, Phys. Rev. A 71 (2005) 052105, arXiv:quant-ph/0405161) is
      named as prior art; the imported Fact is retired. Its verification record is carried here: the
      reference was checked on 2026-11-07 against the OSTI record (title, journal, DOI
      10.1103/PhysRevA.71.052105, abstract) and the steps against the arXiv text quant-ph/0405161v2: phase
      and swap envariance with Facts 1 to 3 and assumptions (a) to (c); fine-graining in Sec. II.D through a
      counter (a piece of the environment or an ancilla), Eqs. (8) to (10), giving p_k = m_k/M; the
      irrational case "by continuity as rational numbers are dense among reals"; the paper states the
      additivity premise itself ("we have assumed that orthogonal states correspond to mutually exclusive
      events") and defers its motivation to Sec. V. The locator (T16, Prop 6.2) is the paper's proposition,
      which has the envariance route; this store version diverges from it as described.
  locator_divergence: 'T16 Prop 6.2 obtains the weights from indifference by the envariance argument (fine-graining and continuity); this store version, from version 4, obtains them under Premise (P) for a state sharp on an atom and names the envariance argument as prior art.'
  maintainer_pass_decisions:
    by: maintainer-2026-11-07
    date: '2026-11-07'
    note: 'Version 2 -> 3. Decision item B5 (routine): the fine-graining and continuity steps, Zurek''s envariance argument imported with its critique, now pin the new Fact one-relation.imported-envariance-born-rule (uses edge added, cited in the formal and the proof); statement unchanged.'
  maintainer_pass_tests:
    by: maintainer-2026-10-23-tests
    date: '2026-10-23'
    note: 'Own exact check added: J = psi gamma_0 psi~ for even psi: J . gamma_0 is the sum of squares of psi, J^2 = a^2 + b^2, and a boosted frame gives a different positive density; invariant weight spaces equal the orbit counts (uniform on transitive orbits); fine-graining returns the squared norms. Version 1 -> 2.'
  env: proposition
  context_refs:
  - one-relation.schr-odinger-slow-shadow
  typing:
    by: ai-typing-pass
    note: 'Kept both edges; the slow-shadow proposition in context_refs is cited only for the unsourced
      frame and is not a premise; the envariance argument (Zurek) is the standard counterpart but is not
      in the store, so no standard-route derivation. Levels pass: the lay level now marks indifference
      as a premise rather than a theorem, keeps the frame-relativity of the density and says the result
      is conditional.'
---

## formal
\emph{Not a derivation of the Born rule.} This proposition says where the squared-norm rule sits in the series and under which premises; it does not derive the rule. From version 4 the weights are obtained from Premise (P), positivity of values (Premise \claimref{synthesis.premise-positivity-of-values}), assumed and not derived, for a state that is sharp on an atom, which is itself assumed; physical states are not shown to be sharp. The non-contextuality assumption (linearity of values across elements that do not commute) is relocated into (P), not removed. The statement is narrower than that of versions 1 to 3; the Scope paragraph says by how much.
\begin{enumerate}
\item[(a)] \emph{(The density; proved, cited.)} The unique conserved density among constant sesquilinear ones is the Dirac density of Lemma \claimref{one-relation.dirac-current-conserved-density}, the $\gamma_{0}$ component of the geometric current $J = \psi\gamma_{0}\tilde{\psi}$: positivity, conservation and uniqueness in that class are proved there. The current is fixed up to scale; the \emph{density} is its component along a timelike $\gamma_{0}$, which is the laboratory's rest frame, declared unsourced in Proposition \claimref{one-relation.schr-odinger-slow-shadow}(3): the located Born density is frame-relative.
\item[(b)] \emph{(The density is the squared norm of the split; proved, computed on samples.)} In $\Cl_{k}(1,3)$, $k$ an ordered field, with generators $\gamma_{0}$, $Q(\gamma_{0}) = 1$, and $\gamma_{1}, \gamma_{2}, \gamma_{3}$, $Q(\gamma_{i}) = -1$, the adjoint of (P) for this split is $x^{\dagger} = \gamma_{0}\tilde{x}\gamma_{0}$. For every $x$, $\langle x^{\dagger}x\rangle_{0}$ is the sum of the squares of the coefficients of $x$, and for even $\psi$ it is the density: $\langle\psi^{\dagger}\psi\rangle_{0} = J \cdot \gamma_{0}$. The projector $\Pi = \tfrac12(1 + \gamma_{0})$ is an atom in the sense of Theorem \claimref{synthesis.born-weights-under-positivity-a-state-sharp-on-an-atom-is-its-trace-functional} (its clause (i): $\gamma_{0}$ is the only blade of square $1$ that commutes with $\gamma_{0}$; the corner of $\Pi$ has dimension four), and $\langle(\psi\Pi)^{\dagger}(\psi\Pi)\rangle_{0} = \tfrac12 J \cdot \gamma_{0}$ for even $\psi$. A boosted frame is another split: it changes the adjoint, the atom and the squared norm together, so the frame-relativity of the density in (a) is the dependence of (P) on the split.
\item[(c)] \emph{(The weights, under (P) and sharpness; proved, by clause (iii) of the theorem cited in (b).)} Let $\Pi$ be an atom of $\Cl_{k}(p,q)$, $\psi$ an element with $\psi\Pi \ne 0$, and $\Pi_{\psi} = \psi\Pi\psi^{\dagger}/n_{\psi}$ the atom of clause (ii) of that theorem. If a state $\omega$ of (P) is sharp on $\Pi_{\psi}$, that is $\omega(\Pi_{\psi}) = 1$, then for every projector $E$ ($E = E^{\dagger} = E^{2}$)
\[
\omega(E) = \frac{\langle(E\psi\Pi)^{\dagger}(E\psi\Pi)\rangle_{0}}{\langle(\psi\Pi)^{\dagger}(\psi\Pi)\rangle_{0}} ,
\]
the sum of the squares of the coefficients of the component $E\psi\Pi$ over that of $\psi\Pi$. For projectors $E_{1}, \dots, E_{r}$ with $E_{i}E_{j} = 0$ ($i \ne j$) and sum $1$ the components $E_{i}\psi\Pi$ sum to $\psi\Pi$ and the weights sum to $1$; components of equal squared norm receive equal weights. All weights lie in $k$; no fine-graining and no continuity step is used. Instances (computed): in $\Cl_{\Q}(2,2)$ with the vacuum projector $\Pi_{0}$ and the number projectors $n_{j} = w_{j}v_{j}$, the element $\psi = 3w_{1} + 4w_{2}$ gives $\omega(n_{1}) = \tfrac{9}{25}$, $\omega(n_{2}) = \tfrac{16}{25}$; in $\Cl_{\Q}(1,3)$ with $\Pi = \tfrac12(1 + \gamma_{0})$ and one sample even $\psi$ the projectors $\tfrac12(1 + \gamma_{0}\gamma_{1})$, $\tfrac12(1 + \gamma_{1}\gamma_{2}\gamma_{3})$ and $\Pi$ receive $\tfrac{23}{34}$, $\tfrac{13}{34}$, $\tfrac{11}{17}$.
\item[(d)] \emph{(Indifference; a premise, cited.)} The indifference premise (Fact \claimref{one-relation.imported-indifference-instrument}, a structural premise of the series and not a theorem) says: for a superposition of equal-norm, flag-degenerate components related by exact symmetries of the frozen vacuum, any unequal weight assignment would instantiate a preference nothing caused, so indifference forces equality. Under (P) and sharpness the equality of the weights of components of equal squared norm is part of (c), which does not use the premise. Without (P) the premise gives equal weights on exact orbits and says nothing about components of unequal norm.
\end{enumerate}
\emph{Prior art, not used.} The passage from equal weights to rational weights by fine-graining into equal-norm constituents, and to all weights by continuity, is the envariance argument of Zurek \cite{Zurek2005}: phases of the Schmidt amplitudes of a system entangled with an environment can be undone on the environment, so weights depend on moduli only; swaps of Schmidt states of equal modulus likewise, so equal moduli give equal weights; fine-graining through an ancilla gives $p_{k} = m_{k}/M$ for rational squared moduli, and continuity the rest. Versions 1 to 3 of this proposition transplanted that argument, in version 3 through an imported Fact that is now retired. It is named here as prior art and is not a premise of this version. Its standing critique is that the fine-graining step presupposes that weights exist and add. On rational instances the fine-graining count, given additivity, returns the numbers that (c) gives without it (computed: $\tfrac{9}{25} + \tfrac{16}{25}$, $\tfrac{25}{169} + \tfrac{144}{169}$, $\tfrac{64}{289} + \tfrac{225}{289}$).

\emph{The residual postulate.} Versions 1 to 3 isolated \emph{that weights exist and add} as the residual postulate, smaller than Born's rule and not zero. In this version it is not removed: it is Premise (P). By clause (ii) of Theorem \claimref{synthesis.positivity-of-values-is-additivity-of-non-negative-weights-on-effects} (for $k = \Q$ and every Archimedean ordered $k$), (P) is equivalent to: the values of effects are non-negative, normalised and additive; that this is the reading of the residual postulate is argued there, not proved. Additivity is asked across effects that do not commute, which is the non-contextuality assumption that theorems of Gleason's type derive from weaker ones for projectors. Here it is assumed.

\emph{Scope: what (c) covers against what versions 1 to 3 claimed.} Versions 1 to 3 claimed that, under the indifference premise and granting that weights exist and add, the squared-norm measure on the conserved Dirac density is the only weight assignment consistent with vacuum indifference. Clause (c) covers: a Clifford algebra $\Cl_{k}(p,q)$ of finite dimension over an ordered field with one fixed split; the states of (P) that are sharp on an atom; and the projectors of the algebra that are self-adjoint for that split. In the mode algebras $\Cl_{k}(\ell,\ell)$ the corner of the vacuum projector is $k\Pi_{0}$ and (c) is the squared-overlap rule for the elements $\psi\Pi_{0}$ and all projectors of the algebra. It does not cover: (1) states that are not sharp on an atom: sharpness is assumed, and physical states are not shown to be sharp; (2) which projectors are outcomes of measurements; (3) the measure over space of the Dirac field: (b) is an identity at a point, and the weights of regions as integrals of the density, with infinitely many modes and a completion, are outside a theorem on finite algebras, so the identification of the conserved density with occupation weight is proved in the algebraic form of (b) and (c) only; (4) in $\Cl_{k}(1,3)$ the atom $\Pi_{\psi}$ does not determine the spinor: $\Pi_{\psi r} = \Pi_{\psi}$ for $r = \gamma_{2}\gamma_{3}$ (computed; the same holds for every $r$ that commutes with $\gamma_{0}$ and has $rr^{\dagger} = 1$), while $\psi$ and $\psi r$ have different spin vectors $\psi\gamma_{3}\tilde{\psi}$, so outcomes that act on a spinor through right multiplication, the spin projectors among them (argued), are not projectors of the algebra and their weights are not given by (c); (5) the uniqueness claim under indifference alone: without (P) nothing stored excludes a weight assignment that respects vacuum indifference and is not the squared norm. The statement of versions 1 to 3 is therefore not recovered as worded.

\emph{Level and refutation.} Structural-conditional: (a) and (b) are proved; (c) holds given (P) and sharpness; (d) is a premise. The refutation condition of versions 1 to 3 (a weight assignment respecting vacuum indifference that is not the squared norm) belonged to the envariance route. For this version: (c) is a theorem under (P), so what can fail is (P) itself (values of effects that are not additive, or not non-negative), the sharpness of physical states, or the identification of outcomes with projectors self-adjoint for the laboratory's split.

## technical
This is not a derivation of the Born rule; it records where the rule sits and what is assumed. The unique conserved density among constant sesquilinear ones is the Dirac density, the $\gamma_{0}$ component of the geometric current $J = \psi\gamma_{0}\tilde{\psi}$; it is positive, conserved and unique in that class, and frame-relative, since $\gamma_{0}$ is the laboratory's unsourced rest frame. In the algebra $\Cl_{k}(1,3)$ this density is the squared norm that Premise (P), positivity of values, uses: with the adjoint $x^{\dagger} = \gamma_{0}\tilde{x}\gamma_{0}$ of the split defined by $\gamma_{0}$, the scalar part of $\psi^{\dagger}\psi$ is $J \cdot \gamma_{0}$ for even $\psi$, and a boosted frame is another split.

The weights then come from a stored theorem, under (P), which is assumed and not derived: a state that is sharp on an atom (a self-adjoint idempotent whose corner has only its own multiples as self-adjoint elements) is that atom's scalar-part functional, so the weight it gives a projector $E$ is the squared norm of the component $E\psi\Pi$ divided by the squared norm of $\psi\Pi$. No fine-graining and no continuity step is used. Sharpness on an atom is assumed, and physical states are not shown to be sharp. The indifference premise gives equal weights to components related by exact vacuum symmetries; under (P) and sharpness that equality is already part of the theorem.

Versions 1 to 3 reached the squared norm from indifference by the envariance argument (Zurek), imported with its critique that fine-graining presupposes that weights exist and add. That argument is now prior art and not a premise. The residual postulate it isolated has not gone away: it is (P), which a stored result shows equivalent to non-negative, normalised, additive values on effects, and whose additivity across elements that do not commute is the non-contextuality assumption. The assumption is relocated into (P), not removed. The new route covers finite Clifford algebras over an ordered field, states of (P) sharp on an atom, and projectors self-adjoint for the split; it does not cover the measure over space of the Dirac field, outcomes acting on a spinor by right multiplication (spin projectors), states not assumed sharp, or the earlier claim that the squared norm is the only assignment consistent with vacuum indifference.

## lay
Born's rule says the chance of a quantum outcome is the squared size of its part of the wave. This result does not derive that rule; it says where the rule sits in the series and what has to be assumed. First, the relevant density is fixed as the unique conserved, positive one, measured in the laboratory's rest frame. Second, the series has an assumption about averages, called (P): averages add up, never go negative on a quantity times its mirror image, and treat a quantity and its mirror image alike. Assuming (P), and assuming also that the state answers yes with certainty to one of the finest yes-or-no questions the algebra contains, the chances are the squared-size rule, and the squared size is the conserved density.

Earlier versions reached the rule another way, by a borrowed argument (Zurek's) that splits outcomes into equal pieces and uses the series' premise that nothing may prefer one of several equivalent outcomes. That argument had to assume that chances exist and add up. The assumption has not been removed; it has been moved into (P), which also assumes that chances do not depend on which other questions are asked alongside. Nothing here shows that physical states are certain on a finest question, or which questions are measurements, and the result covers finite algebras only, not the wave spread over space. So the result is conditional on (P), on that certainty, and, for equal chances of equivalent outcomes without (P), on the indifference premise.

## one-liner
Not a derivation of the Born rule: under Premise (P), assumed, a state sharp on an atom of $\Cl_{k}(p,q)$ (sharpness assumed; physical states are not shown to be sharp) gives each projector self-adjoint for the split the squared norm of its component over the total, and in $\Cl_{k}(1,3)$ with the split of $\gamma_{0}$ that squared norm is the conserved Dirac density at a point; the non-contextuality assumption of the envariance argument (Zurek, prior art) is relocated into (P), not removed, and indifference alone gives only equal weights on exact orbits.
