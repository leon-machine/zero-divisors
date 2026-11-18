"""Correction to group 1 after reading it back: the stored result's reduction of a wall under the one-rung
hypotheses to its setting uses the homotopy invariance of bundles, cited from memory there; say so."""
from oplib import *


def eigenbundle(b):
    head = '\n\n    (18 November, second pass.) Three results, all proved.'
    tail = '\n  attack:'
    s0 = b.index(head) + 2
    s1 = b.index(tail)
    text = ' '.join(b[s0:s1].split())
    old = ("(every wall under the hypotheses of the one-rung theorem, with the collar thin enough; the first-order "
           "clause of tameness and smoothness are not used)")
    new = ("(every wall under the hypotheses of the one-rung theorem, with the collar thin enough and given the "
           "homotopy invariance of bundles, which is cited from memory; the first-order clause of tameness and "
           "smoothness are not used)")
    assert text.count(old) == 1
    return b[:s0] + wrap(text.replace(old, new), 4) + b[s1:]


if __name__ == '__main__':
    apply([('op.eigenbundle-class-of-degenerations', eigenbundle)])
