"""Correction to group 3 after reading it back: the result treats the static region of Schwarzschild-de Sitter,
not every field with more than one horizon. The statement is re-wrapped; no other sentence changes."""
from oplib import *


def capacity(b):
    new_sentence = (r"So the two cases that were posed, the Schwarzschild field and a field with two horizons in "
                    r"the form of the static region of Schwarzschild-de Sitter, are answered under the present "
                    r"premises: $\rho$ is a free datum there, and the choice between a tube point per observer and "
                    r"per horizon is not reached. Other fields with more than one horizon are not computed. ")
    head = '  statement: >-\n'
    tail = '\n  why:'
    s0 = b.index(head) + len(head)
    s1 = b.index(tail)
    text = ' '.join(b[s0:s1].split())
    a = text.index('So the two cases that were open, fields')
    z = text.index('What is left: whether a further premise')
    assert text[a:z].rstrip().endswith('per horizon is not reached.')
    text = text[:a] + new_sentence + text[z:]
    return b[:s0] + wrap(text, 4) + b[s1:]


if __name__ == '__main__':
    apply([('op.which-capacity', capacity)])
