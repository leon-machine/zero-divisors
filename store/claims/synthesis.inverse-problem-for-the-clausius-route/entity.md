---
id: synthesis.inverse-problem-for-the-clausius-route
kind: claim
version: 2
title: 'The inverse problem for the Clausius route'
status: proved
region: synthesis
subject: einstein
tags: [curvature-and-field-equations, forcing-and-uniqueness, horizons, thermal-premises]
proposed_by:
  kind: ai
  session: 2026-10-31-gravity-action
ai_involved: 'yes'
credit:
- name: Leon Butler
  role: direction
- name: Claude Opus 5.5
  role: proposal and drafting
  source: Co-Authored-By trailer of the commit that added it
review: draft
about:
- obj.synthesis.gtg-flat-spacetime-gauge-fields
derivations:
- name: main
  uses:
  - synthesis.einstein-equations-from-c-loc-and-clausius@7
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part@2
  - dark-energy.frozen-point-makes-stelle-west-vector@5
  - dark-energy.imported-henneaux-teitelboim-promotion@5
  - synthesis.einstein-route-makes-n-initial-data@4
  - synthesis.promoted-norm-one-global-pair@4
  - synthesis.euler-term-horizon-entropy-shift@4
  - synthesis.imported-einstein-cartan-matter-coupling@1
  - synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians@1
  - synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form@1
  - synthesis.curvature-only-tractor-actions-are-macdowell-mansouri@3
  - synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared@2
  proof: proof-main.tex
checked_by:
- kind: check
  ref: check.py::check_helmholtz_in_the_metric_selects_the_einstein_form
- kind: check
  ref: check.py::check_lambda_free_form_needs_unimodular_variations
- kind: check
  ref: check.py::check_linearised_lovelock_is_one_line
- kind: check
  ref: check.py::check_matter_cross_helmholtz_forces_the_hilbert_stress
- kind: check
  ref: check.py::check_euler_density_is_invisible_and_weyl_square_is_fourth_order
- kind: proof
  derivation: main
lineage:
  motivated_by:
  - synthesis.einstein-equations-from-c-loc-and-clausius
  - synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part
  - synthesis.series-wald-entropy-changes-without-flux-on-local-horizons
  - synthesis.euler-term-horizon-entropy-shift
  - synthesis.imported-einstein-cartan-matter-coupling
  - synthesis.einstein-route-makes-n-initial-data
extraction:
  open_problem: op.derive-gravitational-action
  maintainer_pass:
    by: maintainer-2026-10-31
    date: '2026-10-31'
    note: 'Version 1 -> 2: Lovelock, Anderson-Duchamp and the Bach-flatness of Einstein fields, cited from memory, now point to the imported Facts approved by Leon, added to uses since clauses (ii) and (iv) rest on them; the curvature-only classification and the Weyl-square identity, cited as filed alongside, are now premises (uses), since the first-order part of (iv) grants the one and quotes the other; pins moved to the new versions of the Einstein-from-Clausius result (6) and the Henneaux-Teitelboim Fact (5), whose changes are added notes. Statement unchanged.'
  note: >-
    Runs the inverse variational problem on the Clausius route's output, which is a solution set. With
    the metric (or the frame) as the varied field and the standard pairing, the Helmholtz condition on
    principal symbols selects the Einstein form among the algebraic rewritings M_beta(G + Lambda); this
    selection depends on the field variable: for a field psi with delta g = M_beta(delta psi), beta not
    -1/4, the form M_beta(G + Lambda) is the Euler-Lagrange expression of the Einstein-Hilbert
    functional, so the route's Ricci form is variational for a densitised metric. The Lambda-free
    trace-free form is not of that kind (M_{-1/4} drops the trace); with the metric alone it is
    variational only on unimodular variations, and the Henneaux-Teitelboim action, an enlarged field
    content, is the route's own variational form with Lambda an integration constant (on the route N is
    initial data, the promoted solution space). A metric action needs a fixed Lambda; the frozen point's
    constraint Q(I) = Lambda/3 carries it as the registered input, it does not compute it. Order at most
    two is needed: the Weyl-squared functional, fourth order, has every Einstein field of every Lambda
    among its solutions, and it is the frozen-point integrand on the tractor gauge field of every
    torsion-free field (\claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}).
    Given Lovelock and Anderson-Duchamp (\claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}), the action is Einstein-Hilbert with
    G = 1/(4 eta) up to null Lagrangians; on the I-preserving first-order field space within the
    curvature-only class (\claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri})
    the route fixes the normalisation of eps(I, X, F, F) and not the Holst-type and Chern-Weil terms.
    For the open problem's imports: (a) not derived (the route is compatible with a local action at fixed
    Lambda, witnessed by the stored functional, and does not single one out); (b) not shrunk (the route
    fixes the Einstein-Hilbert and volume coefficients and leaves exactly the Euler and Pontryagin
    coefficients that distinguish the MacDowell-Mansouri functional); (c) restated: its energy part is
    equivalent to the identification of the heat tensor with the Hilbert stress, its spin part untouched.
    Transport-absent.
---

## formal
Units $\hbar = c = 1$, signature $(1,3)$, the store's curvature sign. Let $(\hb, \Omega)$ be a gravitational field on flat spacetime (Definition \claimref{obj.synthesis.gtg-flat-spacetime-gauge-fields}) with derived metric $g$ and zero torsion, the setting of Theorem \claimref{synthesis.einstein-equations-from-c-loc-and-clausius}, which under the premise (C$_{\mathrm{loc}}$) and its hypotheses (H1) to (H4) delivers the solution set of $\mathcal{R}(a) + 8\pi G_{\mathrm{cl}}T(a) = (\Lambda + 4\pi G_{\mathrm{cl}}\tau)a$, $\Lambda$ an integration constant, $G_{\mathrm{cl}} = 1/(4\eta)$, $T$ the heat tensor of (H1) and (H3). For a symmetric linear function $S(a)$ and rational $\beta$ put $M_{\beta}S(a) = S(a) + \beta\,\tr(S)\,a$, built from $g$ alone. The route's form is $M_{-1/2}$ of the Einstein form $\mathcal{G}(a) + \Lambda a + 8\pi G_{\mathrm{cl}}T(a)$, and $M_{-1/4}$ of it is the trace-free form $\mathcal{R}^{\circ}(a) + 8\pi G_{\mathrm{cl}}T^{\circ}(a)$, free of $\Lambda$. An operator is an Euler-Lagrange expression of a local functional of a field only if its Fr\'echet derivative in that field is self-adjoint (the Helmholtz condition: the second variation is symmetric). Principal symbols are read at a point in a normal gauge, $d_{a} \to p_{a}$, on symmetric $h_{ab} = \delta g_{ab}$ with $\ip{k}{h} = k_{ab}h^{ab}$; the Lorentz-covariant second-order symbols are spanned by $A_{1} = p_{a}p_{b}\tr h$, $A_{2} = \eta_{ab}\,p\cdot h\cdot p$, $A_{3} = \eta_{ab}p^{2}\tr h$, $A_{4} = p^{2}h_{ab}$, $A_{5} = p_{a}(hp)_{b} + p_{b}(hp)_{a}$.
\begin{enumerate}
\item[(i)] \emph{(With the metric as the varied field, the Helmholtz condition selects the Einstein form; proved.)} With $g$ (equivalently the frame) varied and the pairing above, $M_{\beta}(\mathcal{G} + \Lambda)$ is the Euler-Lagrange expression of a local functional only if $\beta = 0$, and for $\beta = 0$ it is one: the metric Euler-Lagrange expression of the Einstein-Hilbert functional with $\Lambda$, and the frame equation of the stored functional (Theorem \claimref{synthesis.macdowell-mansouri-principle-fixes-the-trace-free-part}(i)). On principal symbols the self-adjoint covariant ones form a space of dimension $4$; the Einstein symbol $-\tfrac12(A_{1} + A_{2} - A_{3} + A_{4} - A_{5})$ lies in it, and the asymmetry of $M_{\beta}\mathcal{G}$ is $\beta$ times a fixed nonzero form. The selection depends on the field variable: for $\beta \neq -\tfrac14$, $M_{\beta}$ is invertible, and for the field $\psi$ with $\delta g = M_{\beta}(\delta\psi)$ the $\psi$-derivative of $M_{\beta}(\mathcal{G} + \Lambda)$ has the self-adjoint symbol $M_{\beta}\,\sigma(\mathcal{G})\,M_{\beta}$, the Euler-Lagrange expression of the Einstein-Hilbert functional in $\psi$. So the route's Ricci form ($\beta = -\tfrac12$) is variational for a densitised metric; the trace-free form ($\beta = -\tfrac14$) is not of this kind.
\item[(ii)] \emph{($\Lambda$ for the metric alone; proved in the family, by Lovelock's theorem in general.)} $M_{-1/4}$ has rank $9$ (it drops the trace and $\Lambda$ with it), so the trace-free form is the only member of the family that keeps $\Lambda$ free; for the metric alone it passes the Helmholtz condition on trace-free variations (those fixing the volume element; there it is the Euler-Lagrange expression of the Einstein-Hilbert functional at fixed volume element) and fails it on all variations. With an enlarged field content it is variational with $\Lambda$ an integration constant: the Henneaux-Teitelboim form (Fact \claimref{dark-energy.imported-henneaux-teitelboim-promotion}), which is the route's own variational form, consistent with the stored statements that on the route $N$ is initial data and the solution space is the promoted one (Theorem \claimref{synthesis.einstein-route-makes-n-initial-data}), the norm mode then being one global pair with no local mode (Theorem \claimref{synthesis.promoted-norm-one-global-pair}). For the metric alone: by Lovelock's theorem (Fact \claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}(a)) every natural Euler-Lagrange expression of order at most two in four dimensions is $a\mathcal{G} + b$, with the single vacuum value $\Lambda = b/a$, so the route's solution set with $\Lambda$ free is not that of any natural variational problem of order at most two for the metric, and a metric action needs a fixed $\Lambda$. The frozen point's constraint $Q(I) = \Lambda/3$ (Theorem \claimref{dark-energy.frozen-point-makes-stelle-west-vector}) carries that value as an input, the registered input; it does not compute it. De Sitter fields of every $\Lambda'$ solve the trace-free form, and of them the Einstein form at $\Lambda = 3Q(I)$ keeps only $\Lambda' = \Lambda$. The order bound is needed: the Weyl-squared functional, of fourth order (its second variation at the flat background is fourth order in $p$), has every Einstein field of every $\Lambda$ among its solutions (Fact \claimref{synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form}(a)).
\item[(iii)] \emph{(Linearised Lovelock; proved.)} The covariant second-order symbols that are transverse, $p^{a}E_{ab} = 0$ for every $h$ (the linearised Noether identity of displacement-gauge invariance, which the route's Bianchi step uses with $\nabla\cdot T = 0$), form a plane spanned by the Einstein symbol and $(p_{a}p_{b} - \eta_{ab}p^{2})\tr h$, which is not self-adjoint; the transverse self-adjoint ones are the multiples of the Einstein symbol.
\item[(iv)] \emph{(The metric action, up to terms the route does not see; given imported theorems.)} Assume a local, natural functional $S$ of the metric whose Euler-Lagrange expression has order at most two and is, with the matter source of (v), the route's equation at the fixed $\Lambda = 3Q(I)$. By Lovelock's theorem its gravitational part is a constant multiple of $\mathcal{G} + \Lambda$, and against the matter term of (v) the constant is the one with $G = G_{\mathrm{cl}} = 1/(4\eta)$; by the exactness of the variational complex and the classification of natural null Lagrangians (Anderson and Duchamp, Fact \claimref{synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians}(b)), $S$ is the Einstein-Hilbert functional with $G_{\mathrm{cl}}$ and $\Lambda$ plus $c_{E}$ times the Euler density, $c_{P}$ times the Pontryagin density and a divergence, with $c_{E}$, $c_{P}$ free. The Euler density has zero second variation at the flat background (checked), as it has no field equations. The frozen-point MacDowell-Mansouri functional is the member with Euler coefficient $\alpha = -3/(4\Lambda)$ in $(R - 2\Lambda + \alpha E_{4})/16\pi G$ (Theorem \claimref{synthesis.euler-term-horizon-entropy-shift}(i)); the route does not fix $\alpha$. In first-order variables on the field space of connections preserving $I$, within the curvature-only class of the tractor gauge field (the classification of Theorem \claimref{synthesis.curvature-only-tractor-actions-are-macdowell-mansouri}(iii), granted here: $\kappa\,\epsilon(I, X, F, F) + \kappa' H + \kappa'' K$), the route fixes $\kappa$ by $G = G_{\mathrm{cl}}$ and leaves $\kappa'$ (the Holst-type density, whose frame equation vanishes on torsion-free curvatures, the only ones the route sees) and $\kappa''$ (the Chern-Weil density) free. On the normal tractor connections of torsion-free fields the same integrand is the Weyl square (Theorem \claimref{synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared}(iii)), of fourth order, which the order bound excludes.
\item[(v)] \emph{(Matter; proved.)} Let the matter equations be $E_{\psi} = \delta S_{m}/\delta\psi$ for a local $S_{m}[g, \psi]$, with Hilbert stress $T_{H}$ normalised so that the frame equation of the Einstein-Hilbert functional plus $S_{m}$ is $\mathcal{G} + \Lambda + 8\pi G_{\mathrm{cl}}T_{H} = 0$. The system $(\mathcal{G} + \Lambda + 8\pi G_{\mathrm{cl}}T, E_{\psi})$ is the Euler-Lagrange system of a local functional (up to a constant factor on its first member) if and only if $T = T_{H} + \Theta[g]$ with $\Theta$ independent of the matter ($\Theta = 0$ if $T$ and $T_{H}$ both vanish in the matter vacuum). For a scalar field at the flat background the cross condition holds with the Hilbert stress for minimal coupling (background gradient, linear potential) and for the coupling $\xi\psi^{2}\mathcal{R}$ (constant background), and fails for a source with an altered trace term and for the minimal stress beside the matter equation of $\xi\psi^{2}\mathcal{R}$: the condition does not select minimal coupling, and on the torsion-free route it does not reach the spin coupling of Fact \claimref{synthesis.imported-einstein-cartan-matter-coupling}.
\end{enumerate}
\emph{Reading.} For the three imports of the problem: (a) the route's equations are compatible with a local action at fixed $\Lambda$ (witness: the stored functional), and the route does not single one out, so (a) is not derived; (b) is not shrunk: the route fixes the Einstein-Hilbert and volume coefficients and leaves the Euler and Pontryagin coefficients, which are what distinguish the MacDowell-Mansouri functional from the Einstein-Hilbert functional; (c) its energy part is equivalent to the identification $T = T_{H}$ of the heat tensor with the Hilbert stress, and its spin part is untouched. The result is transport-absent: the frozen point enters only as the carrier of the input $\Lambda$.

## technical
The Clausius route of the store gives Einstein's equations as a solution set and keeps $\Lambda$ as an integration constant. This result runs the inverse variational problem on that output, under the route's premise (C$_{\mathrm{loc}}$) and its hypotheses, and with the metric (or the frame) as the varied field. An operator can be the Euler-Lagrange expression of a local functional only if its linearisation is self-adjoint (the Helmholtz condition), which for second-order operators is tested on the principal symbol at a point; the five Lorentz-covariant second-order symbols on metric perturbations are written down and the conditions solved in exact arithmetic. Of the algebraic rewritings $M_{\beta}(\mathcal{G} + \Lambda)$, only the Einstein form passes when the metric is varied; for a reparametrised field ($\delta g = M_{\beta}\delta\psi$, $\beta \neq -\tfrac14$) the corresponding rewriting passes, so the route's Ricci form is variational for a densitised metric. The trace-free form, which leaves $\Lambda$ free, is not of that kind: for the metric alone it is variational only at fixed volume element, and its variational home with all variations is the Henneaux-Teitelboim form, an enlarged field content, which is the route's own variational form (on the route $N$ is initial data). Given Lovelock's theorem (an imported Fact), no natural variational problem of order at most two for the metric alone has the route's solution set with $\Lambda$ free, so a metric action needs a fixed $\Lambda$, which the frozen point's constraint carries as the registered input. The order bound matters: the Weyl-squared functional has every Einstein field among its solutions, and it is the frozen-point integrand on the tractor gauge field of torsion-free fields. Transverse self-adjoint symbols form one line, the linearised Einstein operator. Given Lovelock and Anderson-Duchamp (imported Facts), the metric action is Einstein-Hilbert with $G = 1/(4\eta)$ up to the Euler and Pontryagin terms; on the $I$-preserving first-order field space within the curvature-only class the Holst-type and Chern-Weil terms also stay free. With matter, the coupled system is variational if and only if the heat tensor is the Hilbert stress of the matter functional up to a matter-independent term; minimal coupling is not singled out and the spin coupling is not reached. None of the three imports of the open problem is derived: (a) and (b) are not, and (c) is restated as the identification of the heat tensor with the Hilbert stress. Transport-absent.

## lay
Earlier work in the series showed, following Jacobson, that Einstein's equations follow if every small horizon has a temperature and an entropy proportional to its area, with heat raising that entropy. Gravity is usually written instead as the result of minimising an action. This result asks what the first picture, run backwards, says about the second. Equations come from an action only if a certain symmetry test passes, and the test depends on which variable is varied. With the usual choice of variable, the metric, only the standard Einstein form passes; with a rescaled variable other forms pass too, but the form in which the cosmological constant is left free passes only if the volume of space-time is held fixed, or in the known unimodular version of gravity with an extra field. So an ordinary action for the metric needs a definite cosmological constant, which the series carries in its frozen point as an input. Assuming two theorems from the literature, and that the equations involve at most two derivatives, the action is then fixed apart from terms that change no equations for fields without twisting, including the Euler term about which the two pictures disagree; so the route does not single out the series' action. With matter, the test holds exactly when the heat in the Clausius argument is the usual energy tensor obtained from the matter's own action. The result is conditional on the series' horizon premise.

## one-liner
Under (C$_{\mathrm{loc}}$) and the Clausius route's hypotheses, with the metric as the varied field, the Helmholtz condition (checked exactly on principal symbols) passes for the Einstein form $\mathcal{G} + \Lambda$ of the route's equations and not for its other algebraic rewritings, which pass for reparametrised fields except the $\Lambda$-free trace-free form (variational for the metric only at fixed volume, and with an enlarged field as the Henneaux-Teitelboim form); given Lovelock and Anderson-Duchamp (imported Facts) and order at most two, which excludes the Weyl square, a metric action needs a fixed $\Lambda$, carried as an input by the frozen point, and is Einstein-Hilbert with $G = 1/(4\eta)$ up to Euler, Pontryagin and, in first-order form, Holst-type terms the route does not see; the coupled system is variational if and only if the heat tensor is the Hilbert stress up to a matter-independent term.
