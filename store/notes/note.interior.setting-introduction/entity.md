---
id: note.interior.setting-introduction
kind: note
version: 1
title: Introduction
status: setting
subject: singularity
proposed_by:
  kind: extraction
  session: settings-2026-10-21
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: 'idea, direction and review'
- name: Claude Fable 5
  role: mathematics and drafting
  source: authorship disclosure of T06, deposited version
comments_on:
- interior.gauge-trajectory-unipotent-ray
- interior.exact-scale-decoupling
- interior.covariant-form-vacuum-equations
- interior.scale-tractor-leaves-cone
locators:
  paper: T06
  number: Setting
  section: Introduction
  line: 331
---

## formal
T5 of this series \cite{ButlerT5} runs a six-step chain from the Schwarzschild gauge field to the Page curve, and at three of its links it defers to a companion geometry paper: for the detailed geometry of where and how division fails, for the covariant meaning of the ascent at the level of the field equations, and for the tests that decide whether the ascended description has physical content or is only a redescription. This is that paper.

The object under study is the gauge-theoretic formulation of general relativity in the spacetime algebra $\Cl(1,3)$, due to Lasenby, Doran and Gull \cite{LDG1998}: gravity as a position-dependent linear map $\hb$ on a flat background, with every metrical statement built from $\hb^{-1}$. The theory's geometric content exists exactly where $\hb$ is invertible, and the series' transport principle \cite{ButlerT1} is a general theory of the loci where it is not. Three questions arise the moment the principle is applied to a black hole, and they organise the paper's three parts.

\emph{Where, exactly, does division fail, and what is the algebraic character of the approach?} Part one (Section \ref{sec:fails}) answers with two exact factorisations. The Schwarzschild gauge trajectory is a ray in a one-parameter unipotent group: at every radius the field is a finite null-type shear of the identity, and the singularity is the divergence of the shear parameter (Proposition \claimref{interior.gauge-trajectory-unipotent-ray}). The curvature factorises exactly, at every radius, into a divergent conformal prefactor $-M/r^3$ times a fixed, mass-independent shape operator $S$ satisfying $S^2 + S = 2$ (Proposition \claimref{interior.exact-scale-decoupling}): the entire approach to the singularity is carried by a single conformal weight, and what survives the approach is conformal data.

\emph{Is the ascent $\Cl(1,3) \to \Cl(2,4)$ a property of the equations or something added to them?} Part two (Section \ref{sec:tractor}) proves the strongest available answer: no limit is needed. The vacuum field equations are exactly equivalent, at every radius, to the covariant constancy of the distinguished null scale section of the rank-six ambient (tractor) bundle: a parallel ideal point of the fibre quadric (Theorem \claimref{interior.covariant-form-vacuum-equations}). The equations of vacuum gravity are natively a statement in the ascended description, and the familiar metric form is what that statement looks like after a scale is chosen. The cosmological constant enters at theorem level: for $\Lambda \neq 0$ the frozen point leaves the cone, its squared norm is $\Lambda/3$, and its stabiliser rotates from the parabolic Poincar\'e group to the reductive de Sitter or anti-de Sitter group (Theorem \claimref{interior.scale-tractor-leaves-cone}, Proposition \claimref{interior.stabiliser-rotates-parabolic-reductive}): $\Lambda$ measures precisely the failure of infinity to be parabolic.

\emph{Does the covariant description actually reach the singularity?} Part three answers in two halves. Section \ref{sec:approach} proves the weighted limit theorem: blowing up the interior along the singular locus with direction-dependent weights equal to the Kasner exponents $(-1/3, 2/3, 2/3)$, the Hubble-normalised connection and the parallel tractor extend continuously to the exceptional boundary, with explicit rates ($O(\tau^{2/3})$ in the boosts, $O(\tau^{1/3})$ in the rotations), and the values-level boundary holonomy algebra is exactly $\mathfrak{so}(1,3)$, which for $\Lambda = 0$ is the Levi factor of the frozen point's parabolic stabiliser with no component in the nilradical, and for $\Lambda \neq 0$ a proper subalgebra of its reductive stabiliser (Theorem \claimref{interior.weighted-limit-theorem}). The theorem is proved in full for the Schwarzschild class, extends verbatim to Schwarzschild-de Sitter (Theorem \claimref{interior.schwarzschild-de-sitter-weighted-limit}), and carries a sharp delimiter: for generic mixmaster singularities the frame limit provably fails to exist, and the correct generic statement must be billiard-invariant (Remark \claimref{note.interior.generic-delimiter-mixmaster}). Section \ref{sec:kerr} then runs the Kerr tests: the whole Kerr family is unipotent on a null shear (Proposition \claimref{interior.unipotency-across-kerr-family}); the curvature takes the Schwarzschild form with a complexified scale whose non-invertibility locus is exactly the ring, with the disc interior regular (Proposition \claimref{interior.complex-factorisation-location-ring}); the complex scale is the inverse cube of the Walker-Penrose Killing spinor, so the framework's scalar-plus-pseudoscalar scale is a hidden twistorial object (Proposition \claimref{interior.complex-scale-inverse-cube-killing-spinor}); and at the perturbed Cauchy horizon the imported PDE results establish survival by derivative level, point-level structure (metric and conformal alike) extending continuously while connection-level structure generically fails (proved in spherical symmetry, expected for Kerr), with the strict conformal-over-metric separation registered as the sharpest successor problem (Section \ref{subsec:cauchy}).

## technical
pending

## lay
pending

## one-liner
pending
