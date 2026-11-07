# Resolving every imaginary unit (Leon, 7 November 2026, 11:16: "Try to resolve all imaginary units")

This supersedes RULINGS.md R1 (keep i on boundary-mode, atom and window flows) and the "what stays" list of
SWEEP.md rule 6 and of the conventions. The aim is no bare imaginary unit anywhere in a result's formal,
technical, lay and one-liner levels or proofs, and no `outside_ga` declaration left whose reason is a bare i.

## The principle
A complex number must commute with everything it multiplies. So the unit is the pseudoscalar that commutes with
every element the scalars act on:

U1. **I4** (left on even values, the right unit x -> x I4 on others) when the objects the numbers multiply are
    even elements, scalars, tower-plane elements, or abstract spaces built from them: the field theory, the
    horizon's continuum modes, the Hadamard chain, numbers in general (span{1, I4} is the complex field; this is
    also the default scalar field of an abstract complex Hilbert space or matrix algebra, a qubit, a window,
    complex analysis of scalar functions, theta functions and modular forms: tau = I4, q = e^{2 pi I4 tau}).
U2. **J = the pseudoscalar of the plane orthogonal to the atom's plane** for the completed-pair atom and the
    boundary modes in the spacetime radial plane sigma = e0 e1: J = e2 e3 commutes with e0, e1 and so with every
    mode operator built from them, J^2 = -1, and J = +-I4 sigma (store identity I4 B = J,
    synthesis.wedge-reflections-compose-to-the-two-pi-rotor-...). The source's phase flow Ad(e^{itK}),
    K = sigma/2, becomes Ad(e^{J t K}), and the source's e^{-it} v becomes e^{-Jt} v (signs to be fixed by the core
    result below, do not guess). Modular groups and KMS continuations of these algebras use J likewise.
U3. **The central pseudoscalar of the odd extension** where the unit must commute with every vector
    (complexifications V_C, complex null vectors e2 + i e3, Cl(p,q)_C, the Dirac module's complexification,
    tube points m = x + iy of Cl(2,4)_C, i0 shifts of a spacetime vector): for V of even dimension adjoin one
    vector e with Q(e) chosen so that the pseudoscalar I_{V+e} squares to -1; it is central, and
    Cl(V) (x) C = Cl(V + Re) with i -> I_{V+e}. Spacetime: the time extension Cl(2,3), unit I5 = I4 e
    (odd-extensions.mirror-inside-complexified-extension-absent-doubled already uses it). Conformal space:
    Cl(3,4), unit I7 = I6 e. So e2 + i e3 becomes e2 + I5 e3, m = x + I7 y, Q(y - y' - I5 0 e0). For a scalar
    function of a shifted vector the shift may instead be written in scalar form with I4 (the core result
    states this).
U4. **Imported Facts** are restated in geometric algebra with the unit chosen by U1-U3; the source's own form
    moves into `extraction.source_formal` (keep any existing one) with a sentence "the source writes i for
    <unit>". The status stays imported; the declaration goes.
U5. **Bridge results** state the geometric-algebra side in the levels; a standard-formalism expression with i
    either uses the unit by U1-U3 (matrices with entries in span{1, I4}, "the Dirac matrices with i read as
    I5", and so on) or moves to `extraction.source_formal`.
U6. If, after honest effort, an occurrence cannot be resolved exactly (the replacement would change what is
    claimed), leave it, keep or write the declaration with the precise reason, and list it in your report under
    "Could not resolve". Never weaken or change a statement to remove an i.

Never identify two different units (I4 versus I6 versus J versus I5): where two appear in one entity, keep both
and say which acts where. Index letters and Hamilton's named quaternion units are not imaginary units.

## Core results (written first; the sweep cites them)
- std-algebra.complexification-is-the-odd-extension: for (V, Q) of even dimension n with pseudoscalar I_V,
  adjoin e orthogonal to V with Q(e) = -I_V^2 (a sign); then I_{V+e} = I_V e is central with square -1, every
  vector of V commutes with it, and v + a -> ... gives Cl(V) (x) C = Cl(V + Re) with i -> I_{V+e}, V_C =
  V + I_{V+e}V; instances Cl(1,3) -> Cl(2,3) with I5, Cl(2,4) -> Cl(3,4) with I7; a scalar function of a vector
  shifted by I5 epsilon e0 equals the same function with the scalar shift written in span{1, I5}, and since
  I5 commutes with everything there, it may be read as the complex unit of any scalar computation (relation to
  I4 on even values stated, not assumed). Cite odd-extensions.doubling-or-complexification,
  odd-extensions.volume-element-odd-dimension, primer.centre, std-algebra.complexification.
- synthesis.transverse-bivector-is-the-complex-unit-of-the-radial-atom: in Cl(1,3) with radial plane sigma =
  e0 e1 and transverse plane J = e2 e3: J commutes with e0, e1, J^2 = -1, J sigma = +-I4 (fix the sign); for the
  completed pair (singularity.modular-structure-completed-pair: its v, v*, sigma = v*v - v v*), J commutes with
  v, v*, the real span{1, J} is a field over which the pair's algebra is the complex CAR algebra, and
  Ad(e^{J t sigma/2}) v = e^{-+Jt} v (exact signs), so the store's complex phase flow and its modular group and
  KMS continuation are written with J; also note that left I4 is not a scalar there ((I4 v)(I4 w) = +vw).
  Check exactly with GA.py.
