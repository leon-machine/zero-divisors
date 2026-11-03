---
id: note.descent-lift.setting-setting-what-imported
kind: note
version: 1
title: Setting, and what is imported
status: setting
subject: descent
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: 'authorship disclosure of T05-descent-lift, the series'' standard disclaimer'
comments_on:
- descent-lift.imported-pinching-one-way-door
locators:
  paper: T05-descent-lift
  number: Setting
  section: Setting, and what is imported
  line: 143
---

## formal
The transport principle is a rule for elements: where an element has no inverse, adjoin the minimum that gives it one, and keep the descent that forgets the adjunction \cite[Thm.~4.13, Prop.~7.5, Thm.~7.6]{ButlerT1}. The descent is a conditional expectation, the pinching onto the algebra that commutes with the ladder's occupation projector, and it is one-way: no homomorphism returns from the ascent to the base. The singularity paper reads the same pinching, mode by mode, as the parity average $\EN(x) = \tfrac12(x + \G x\G)$ and, on several modes, as the pinching onto the joint-number-diagonal algebra \cite[Thm.~5.7, Prop.~9.6]{ButlerT5}; applied to an entangled pair $c\ket{00} + s\ket{11}$ it returns the classical shared bit $\operatorname{diag}(c^{2}, s^{2})$.

This note asks the inverted question. A map without an inverse can still be lifted: enlarged to a reversible map on a bigger system, followed by forgetting the enlargement. That is Stinespring's dilation, and it is the exact analogue for maps of what the transport principle does for elements. The question is whether the descent's lift can be built inside the tower, from rungs, by operations the framework's own premises allow, and what it costs. The answer is computed exactly, in the singularity paper's conventions, and the kill conditions of Section \ref{sec:kill} were fixed before the computation.

Three things are fixed on this page. First, the states. The singularity paper's premise (P) says physical states of the modes are even, and its imported univalence rule says the observable algebra is the even subalgebra \cite[Prem.~7.8, Fact~7.9]{ButlerT5}. Everything below is stated on even states, and a single mode then has nothing to lift: its only even pure state is the vacuum, on which the descent is the identity. The descent's first physical action is on the pair. Second, the reduced state. For fermions the reduced state of a subsystem is the restriction of the joint state to the subsystem's algebra; the tensor-product partial trace agrees with it when the complementary factor is even, which is the only case the lift uses, and the script computes the restriction throughout. Third, the vocabulary, for a reader of quantum information who has not read the series: a \emph{rung} is one $(1,1)$ ascent of the tower, which adjoins one fermionic mode \cite[Thm.~4.2]{ButlerT3}; the \emph{descent} is the pinching above; the \emph{supplied class} is the set of generators the singularity paper's completion provides, polynomials in the parity sections $\sigma_{k} = 2N_{k} - 1$, all joint-number-diagonal \cite[Prem.~7.30, Thm.~C.8]{ButlerT5}; a \emph{pairing} generator is $a^{\dagger}_{i}a^{\dagger}_{j}$ or its adjoint, the part of $\mathfrak{so}(2\nu)$ that moves the vacuum \cite[Prop.~13.4]{ButlerT5}; and the two-ledger words \emph{transport-essential}, \emph{convenient} and \emph{absent} grade a result by whether the $(1,1)$ increment does irreplaceable work in it, some work, or none \cite{ButlerT17}.

## technical
pending

## lay
pending

## one-liner
pending
