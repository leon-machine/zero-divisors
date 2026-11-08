import sys; sys.path.insert(0,'.')
from fractions import Fraction as F
import cert1
cert1.cert(4,2,(1,1,2),F(0),F(0),F(1),F(19,20),den=1<<12)
