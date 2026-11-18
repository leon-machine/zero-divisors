"""Correction to group 4 after reading it back: the first margin is between 2.83 and 2.84, so 'about 2.83'."""
from oplib import *


def curvature(b):
    return rep(b, "rate and the entropy, and the margins of the stored exclusion rise, from above $2.2$ and $1.5$ to about\n"
                  "    $2.8$ and $1.96$.",
               "rate and the entropy, and the margins of the stored exclusion rise, from above $2.2$ and $1.5$ to about\n"
               "    $2.83$ and $1.96$.")


if __name__ == '__main__':
    apply([('op.curvature-coupling-across-subjects', curvature)])
