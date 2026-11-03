"""Structural LaTeX checks for statement and proof text (layer 1).

This is not a renderer.  It catches the faults that stop maths rendering on the
site: unbalanced braces, unclosed math, mismatched environments, unpaired
\\left/\\right, and macros that are neither standard nor declared in the
store's notation registry (notation.yaml).  A full KaTeX render pass runs in
the site build, where KaTeX is available.
"""
from __future__ import annotations

import re

STANDARD = set(("""renewcommand centering arraybackslash textwidth linewidth addlinespace endhead endfirsthead endfoot endlastfoot rlap llap coloneqq l L roman theenumi labelenumi theenumii arabic alph Roman 
documentclass usepackage begin end label ref eqref cref Cref cite citep citet
emph textbf textit texttt textrm textsf textsc textup text mathrm mathbf mathit
mathcal mathbb mathfrak mathsf mathtt mathscr boldsymbol bm operatorname
item par noindent newline linebreak quad qquad hspace vspace hfill smallskip
medskip bigskip footnote S ldots cdots vdots ddots dots dotsc dotsb
frac dfrac tfrac binom sqrt sum prod coprod int iint oint lim limsup liminf sup
inf max min det dim ker log ln exp sin cos tan sinh cosh tanh arcsin arccos
arctan sec csc cot deg arg gcd hom Pr mod bmod pmod
left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl Biggr middle
langle rangle lfloor rfloor lceil rceil lvert rvert lVert rVert vert Vert
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi
psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega
pm mp times div cdot ast star circ bullet oplus ominus otimes oslash odot
wedge vee cap cup setminus sqcup sqcap uplus amalg dagger ddagger
leq geq le ge neq ne equiv sim simeq approx cong propto prec succ preceq succeq
ll gg subset supset subseteq supseteq subsetneq supsetneq in notin ni owns
perp parallel mid nmid models vdash dashv
to rightarrow leftarrow Rightarrow Leftarrow leftrightarrow Leftrightarrow
longrightarrow longleftarrow Longrightarrow Longleftarrow longleftrightarrow
Longleftrightarrow mapsto longmapsto hookrightarrow hookleftarrow
rightharpoonup leftharpoonup uparrow downarrow Uparrow Downarrow updownarrow
nearrow searrow swarrow nwarrow iff implies impliedby twoheadrightarrow
xrightarrow xleftarrow rightleftharpoons
infty partial nabla forall exists nexists emptyset varnothing neg lnot
Re Im aleph hbar ell wp prime backslash angle triangle square Box Diamond
top bot flat natural sharp clubsuit diamondsuit heartsuit spadesuit
hat widehat tilde widetilde bar overline underline vec dot ddot check breve
acute grave ring overbrace underbrace overrightarrow overleftarrow
stackrel overset underset substack atop choose
displaystyle textstyle scriptstyle scriptscriptstyle limits nolimits
mathrel mathbin mathop mathord mathpunct mathopen mathclose
colon vdots cdot ldotp cdotp ast
lbrace rbrace lbrack rbrack
phantom vphantom hphantom mathstrut strut
not ncong nsim nleq ngeq nsubseteq nsupseteq
tag notag nonumber intertext
quad enspace thinspace negthinspace
Biggm bigm Bigm biggm
emptyset complement
circlearrowleft circlearrowright curvearrowright
lhd rhd unlhd unrhd triangleleft triangleright
blacktriangleright blacktriangleleft
checkmark
bigotimes bigoplus bigcup bigcap bigvee bigwedge bigsqcup biguplus bigodot
varinjlim varprojlim injlim projlim leavevmode ltimes rtimes imath jmath
lnot land lor varkappa varsigma varPhi varPsi varOmega varGamma varDelta
mathring overleftrightarrow underrightarrow underleftarrow
text mbox hbox textnormal mathnormal emph
lesssim gtrsim toprule midrule bottomrule cmidrule small footnotesize scriptsize large
setcounter qedhere nparallel labelenumi hline cline multicolumn tabularnewline
""").split())

ENVS_MATH = {"equation", "equation*", "align", "align*", "gather", "gather*",
             "multline", "multline*", "aligned", "gathered", "cases", "pmatrix",
             "bmatrix", "vmatrix", "Vmatrix", "matrix", "smallmatrix",
             "psmallmatrix", "split", "array", "subarray"}

MACRO_RE = re.compile(r"(?<!\\)(?:\\\\)*\\([A-Za-z]+)")
ENV_RE = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")


def strip_comments(s: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", s)


def structural_errors(text: str) -> list[str]:
    s = strip_comments(text)
    errs = []
    depth = 0
    i = 0
    while i < len(s):
        c = s[i]
        if c == "\\" and i + 1 < len(s):
            i += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth < 0:
                errs.append("E110 unmatched '}'")
                depth = 0
        i += 1
    if depth > 0:
        errs.append(f"E110 {depth} unclosed '{{'")
    stack = []
    for m in ENV_RE.finditer(s):
        if m.group(1) == "begin":
            stack.append(m.group(2))
        else:
            if not stack or stack[-1] != m.group(2):
                opened = ("\\begin{" + stack[-1] + "}") if stack else "any open environment"
                errs.append("E110 \\end{" + m.group(2) + "} does not match " + opened)
                if m.group(2) in stack:
                    while stack and stack.pop() != m.group(2):
                        pass
            else:
                stack.pop()
    if stack:
        errs.append(f"E110 unclosed environment(s): {', '.join(stack)}")
    # inline math: count unescaped $ (ignoring $$ pairs as two)
    dollars = len(re.findall(r"(?<!\\)\$", s))
    if dollars % 2:
        errs.append("E110 odd number of '$' (unclosed inline maths)")
    if len(re.findall(r"(?<!\\)\\\[", s)) != len(re.findall(r"(?<!\\)\\\]", s)):
        errs.append("E110 unbalanced \\[ \\]")
    lefts = len(re.findall(r"\\left(?![a-zA-Z])", s))
    rights = len(re.findall(r"\\right(?![a-zA-Z])", s))
    if lefts != rights:
        errs.append(f"E110 \\left x{lefts} vs \\right x{rights}")
    return errs


# file access, catcode tricks and links: never allowed in store text, whatever
# notation.yaml declares (the text is compiled by LaTeX and typeset on the site)
FORBIDDEN = {"input", "include", "includeonly", "write", "openin", "openout", "read",
             "immediate", "catcode", "def", "gdef", "edef", "xdef", "csname",
             "expandafter", "href", "url", "special", "newwrite", "newread",
             "InputIfFileExists", "lstinputlisting", "verbatiminput", "usepackage",
             "documentclass", "require", "class", "cssId", "style", "unicode"}


def forbidden_macros(text: str) -> list[str]:
    return sorted(set(MACRO_RE.findall(strip_comments(text))) & FORBIDDEN)


def unknown_macros(text: str, notation: dict) -> list[str]:
    s = strip_comments(text)
    found = set(MACRO_RE.findall(s))
    known = (STANDARD | set(notation) | {"claimref"}) - FORBIDDEN
    return sorted(m for m in found if m not in known and m not in FORBIDDEN)
