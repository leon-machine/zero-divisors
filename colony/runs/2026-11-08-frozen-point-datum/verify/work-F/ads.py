# AdS side: is <1,-1,-1,-1,-d> (d<0) similar to <1,1,-1,-1,-1> over Q? expect iff -d sum of two squares
exec(open('own.py').read().split('std=[1,-1,-1,-1,-1]')[0].split('for L in')[0])
src=open('own.py').read(); i=src.index('# Hilbert'); j=src.index('std=[1,-1'); exec(src[i:j])
std=[1,1,-1,-1,-1]
for d in (F(-2),F(-3),F(-5),F(-7,9),F(-1,2),F(-6)):
    q=[1,-1,-1,-1,-d]; c=-d
    cq=[c*a for a in q]
    print("d",d,"similar to (2,3):",all(hasse(cq,p)==hasse(std,p) for p in (2,3,5,7)))
