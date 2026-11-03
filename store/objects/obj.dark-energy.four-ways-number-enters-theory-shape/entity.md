---
id: obj.dark-energy.four-ways-number-enters-theory-shape
kind: object
version: 1
title: Four ways a number enters a theory of this shape
status: defined
region: dark-energy
subject: dark-energy
tags:
- undetermined-input
proposed_by:
  kind: extraction
  session: pilot-2026-10-20
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T10, deposited version
review: typed
locators:
  paper: T10
  number: Def 5.6
  label: def:fourways
  line: 1015
extraction:
  typing:
    by: ai-typing-pass
    note: Definition; levels explain the four clauses without adding claims.
  env: definition
  connect_pass:
    by: ai-connect-pass
    date: '2026-10-21'
    added_premises: []
    added_dependants:
    - dark-energy.imported-henneaux-teitelboim-promotion (about)
    - programme.n-parameter-of-the-laws (about)
    - standard-model.what (about)
    - standard-model.trichotomy-what-kind-number (about)
    - dark-matter.imported-frozen-point-de-sitter-radius (about)
    - dark-matter.imported-trichotomy-descents-data (about)
    added_about: []
    verdict: connected
    note: Linked by about from the claims whose statements use its clauses (parameter of the laws, dynamically
      fixed, initial data).
---

## formal
Let a theory consist of a kinematic structure $\mathcal{K}$ with a notion of isomorphism, a family of action functionals $S_\mu$ indexed by parameters $\mu$ on a configuration space carrying $\mathcal{K}$, with solution spaces $\mathcal{S}_\mu$ and an evolution on each. A real quantity $q$ defined on $\bigcup_\mu \mathcal{S}_\mu$ and conserved by the evolution is called
\begin{enumerate}
\item[(K)] \emph{kinematic} if it factors through the kinematic isomorphism class: $q(x) = q(y)$ whenever $x, y$ have isomorphic kinematic structures;
\item[(D)] \emph{dynamically fixed} if it is constant on $\bigcup_\mu \mathcal{S}_\mu$;
\item[(P)] \emph{a parameter of the laws} if it is constant on each $\mathcal{S}_\mu$ but not on the union: $q$ is a function of $\mu$ and of nothing else;
\item[(I)] \emph{initial data} if it is not constant on some $\mathcal{S}_\mu$.
\end{enumerate}

## technical
The setting is a theory with a kinematic structure $\mathcal{K}$ carrying a notion of isomorphism, and a family of action functionals $S_\mu$, indexed by parameters $\mu$, with solution spaces $\mathcal{S}_\mu$ and an evolution on each. A conserved real quantity $q$ on $\bigcup_\mu\mathcal{S}_\mu$ is kinematic (K) if it factors through the kinematic isomorphism class; dynamically fixed (D) if it is constant on the whole union; a parameter of the laws (P) if it is constant on each $\mathcal{S}_\mu$ but not on the union, so a function of $\mu$ alone; and initial data (I) if it is not constant on some $\mathcal{S}_\mu$.

## lay
This definition sorts the ways a number can enter a physical theory. It might be fixed by the kinematic setting, forced to a single value by the dynamics, be a setting of the laws that differs between versions of the theory, or vary from one solution to another as initial data. It makes precise the question of what kind of number a constant such as the cosmological constant is.

## one-liner
A conserved quantity in a theory with actions $S_\mu$ is kinematic, dynamically fixed, a parameter of the laws or initial data, according to how it depends on the kinematic class, the solution and the parameter $\mu$.
