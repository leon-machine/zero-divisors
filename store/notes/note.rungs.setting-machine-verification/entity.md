---
id: note.rungs.setting-machine-verification
kind: note
version: 1
title: Machine verification
status: setting
subject: one-relation
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T12-rungs, the series'' standard disclaimer'
comments_on:
- rungs.imported-fock-representation-bogoliubov-group
- rungs.rung-spinor-module-mixings
- rungs.generators-outside-gauge-algebra
- rungs.r-s-are-one-hypothesis-two
locators:
  paper: T12-rungs
  number: Setting
  section: Machine verification
  line: 349
---

## formal
Every computational identity asserted here is verified in exact arithmetic by the deposited script \cite{ButlerVerifyT12R}, \texttt{verify\_T12\_rungs.py}, which imports the series' shared library \texttt{GA.py}: seventeen checks, all passing, no floating point (ranks are computed by \texttt{GA.py}'s elimination over exact rationals). The script builds the five-mode Fock representation explicitly, as thirty-two by thirty-two matrices over the Gaussian integers, and the four-mode one of a single rung, and computes on them rather than restating formulas. They are: the canonical anticommutation relations, the uniqueness of the vacuum and the spanning of the module by creation monomials (Fact \claimref{rungs.imported-fock-representation-bogoliubov-group}, Theorem \claimref{rungs.rung-spinor-module-mixings}(1)); the chirality operator $(-1)^{N}$ as the parity of $j + k$, anticommuting with every generator; the bigraded dimensions counted on the basis; the ten Majorana generators' Clifford relations and the linear independence of the forty-five bilinears; their closure under the commutator with the $\mathfrak{so}(10)$ bracket on all pairs, and their commuting with chirality (Theorem \claimref{rungs.rung-spinor-module-mixings}(3)); the exact dimensions $25$ and $13$ of the subalgebras commuting with the total and with the separate mode numbers, giving $45 - 13 = 32 = 12 + 20$ (Theorem \claimref{rungs.rung-spinor-module-mixings}(2), (3), Proposition \claimref{rungs.generators-outside-gauge-algebra}, Section \ref{sec:fallback}(iv)); the selection of $3N_{\mathrm{rung}} - 2N_{\mathrm{pair}}$ as the trace-free element of the centre, with eigenvalue $3j - 2k$, and the eigenvalue $j - k$ of $K$'s generator, zero on the cells only (Proposition \claimref{rungs.r-s-are-one-hypothesis-two}, Theorem \claimref{rungs.rung-spinor-module-mixings}(3)); the $\su(2)$ and $\su(3)$ Casimirs on every sector and the weights of $\Lambda^{2}W$ (Proposition \claimref{rungs.transported-module-holds-tuple-one-vector}, Fact \ref{fact:sixteen}); the ranks $17$ and $16$ at $n = 3$ against $12$ and $12$ at $n = 2$ (Theorem \claimref{rungs.rung-spinor-module-mixings}(3)); the two volume identities of Lemma \claimref{rungs.mass-bracket-frozen-points-grip-slot} on rational instances and the partial trace of $\Psi \otimes \bar\Psi$ over the slot index on a Gaussian-rational instance; the rung operators of $\uu(2)$ on the one-constituent even sector as the ladder action (Proposition \claimref{rungs.ladder-group-rung-mixing-group-one}); a null momentum staying null in $\Cl(2,4)$ and $\Cl(3,5)$ with the rungs' null pairs in \texttt{GA.py}'s blade engine (Corollary \claimref{rungs.fact-null-momenta-invite-one-rung}); the nullity of all six pairwise bivectors of a four-twistor instance, and, on the four-mode space, the twisted ground generators generating $\mathrm{M}_{8}(\C)$ with the rung's $\{1, v, w, vw\}$ as commutant, $v, w$ anticommuting with chirality and the even part abelian (Proposition \claimref{rungs.two-twistor-bivector-null-invites-one}; the script's twisted generators square to $-1$, so this verifies the complexified statement, not Fact \claimref{rungs.imported-tower-one-qubit-per-rung}'s real isomorphism); the absent $\bar{6}$ weights (Proposition \claimref{rungs.transported-module-holds-tuple-one-vector}); and the dimension counts of Theorem \claimref{rungs.rung-spinor-module-mixings}(4). What the script does not check: the Facts beyond the instances named, verified in their own papers' scripts; the real-form statement of Remark \claimref{note.rungs.compact-form}, which is representation theory imported through Fact \claimref{rungs.imported-fock-representation-bogoliubov-group}; and Hypothesis (R), which is not a computation.

## technical
pending

## lay
pending

## one-liner
pending
