---
id: obj.transport.obstruction-types
kind: object
version: 1
title: Obstruction types
status: defined
region: transport
subject: zero-divisors
tags: [obstruction-types, idempotents]
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T01, deposited version
review: typed
locators:
  paper: T01
  number: Def 3.1
  label: def:types
  line: 561
extraction:
  env: definition
  unresolved_refs:
  - ex:hyperbolic-idem
  typing:
    by: ai-typing-pass
    note: 'Definition: levels only, no edge changes.'
  connect_pass:
    by: ai-connect-pass
    date: 2026-10-21
    added_premises: []
    added_dependants: [correspondence.imported-forced-completion-fibre-quadric, descent-lift.pairing-creator-under-transport-algorithm, interior.gauge-trajectory-unipotent-ray, odd-extensions.imported-minimal-completion-degenerate-algebra-rule, rule2.odd-lorentzian-dimension-exactly-one-real, rule2.rule-2-kaluza-klein-algebra, rule2.where-obstruction-sits-commuting-square, rule2.which-residues-obstruct-which-way, tower.rigidity-clock-frozen, transport.existence-locus-type-p, transport.fusion-occurs-most-once, transport.no-transport-terminates, transport.odd-lorentzian-dimension-exactly-one-real, transport.one-generator-minimal-minimal-completions-classified, transport.pair-canonical-label-bit, transport.rule-1-morita-trivial, transport.rule-2-ideal-fusion-sharp-form, transport.type-p-self-repairing, transport.where-obstruction-lies-commuting-square, transport.which-residues-obstruct-which-way, transport.existence-locus-type-n, transport.existence-classification-type-c, transport.transport-principle, transport.obstructions-are-moved-never-destroyed, obj.transport.transport, refuted.the-two-one-generator-ascents-differ-as-algebras]
    added_about: []
    verdict: connected
    note: 'About from every statement that names a type N, P or C obstruction; the two existence results are linked although they speak of null vectors and central idempotents, since they are the existence loci of types N and C.'
---

## formal
Let $A = \Cl(p,q)$, nondegenerate. A zero-divisor obstruction of $A$ is classified as:
\begin{itemize}
\item \textbf{Type N (isotropic vector).} A null vector $v \in \mathbb{V}$, $v \neq 0$, $v^2 = Q(v) = 0$, together with the annihilating idempotent $wv$ it acquires through a hyperbolic partner (Example \ref{ex:hyperbolic-idem}). Geometrically: an isotropic line, a direction without a metric partner.
\item \textbf{Type P (non-central idempotent).} An idempotent $e = e^2$ with $e \notin \{0, 1\}$ and $e$ not central. Prototype: $e = \tfrac12(1 + u)$ with $u^2 = 1$, $u \neq \pm 1$. Each such $e$ is a zero divisor via $e(1 - e) = 0$.
\item \textbf{Type C (central idempotent).} An idempotent $e \notin \{0,1\}$ lying in the centre of $A$. The two-sided ideals $eA$ and $(1-e)A$ then annihilate one another and $A$ splits as their direct sum.
\end{itemize}

## technical
In a nondegenerate $A = \Cl(p,q)$ a zero-divisor obstruction is of one of three types. Type N is a nonzero null vector $v$, $Q(v) = 0$, together with the annihilating idempotent $wv$ it acquires through a hyperbolic partner $w$: geometrically an isotropic line, a direction without a metric partner. Type P is a non-central idempotent $e = e^2$ with $e \notin \{0, 1\}$, prototype $e = \tfrac12(1 + u)$ with $u^2 = 1$, $u \neq \pm 1$; it is a zero divisor through $e(1 - e) = 0$.

Type C is a central idempotent $e \notin \{0, 1\}$. Then the two-sided ideals $eA$ and $(1 - e)A$ annihilate one another and $A = eA \oplus (1 - e)A$.

## lay
Division can fail in a Clifford algebra in three different ways, and this definition names them. Type N is a direction of zero length, such as a light ray in spacetime. Type P is an element that equals its own square without being 0 or 1, like a projection that keeps part of a space and discards the rest. Type C is such a projection that commutes with everything, which means the whole algebra falls apart into two independent pieces.

## one-liner
Zero-divisor obstructions in a nondegenerate real Clifford algebra are classified as type N (a null vector with the idempotent its partner supplies), type P (a non-central idempotent) or type C (a central idempotent splitting the algebra).
