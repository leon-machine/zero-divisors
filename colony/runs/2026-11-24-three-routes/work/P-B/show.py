import sys,json
d=json.loads(sys.stdin.read())
def show(x,ind=0):
    if isinstance(x,dict):
        for k,v in x.items():
            if isinstance(v,(dict,list)):
                print(' '*ind+str(k)+':'); show(v,ind+2)
            else: print(' '*ind+str(k)+': '+str(v))
    elif isinstance(x,list):
        for v in x:
            if isinstance(v,(dict,list)):
                print(' '*ind+'-'); show(v,ind+2)
            else: print(' '*ind+'- '+str(v))
    else: print(x)
show(d)
