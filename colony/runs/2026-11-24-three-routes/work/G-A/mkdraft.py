import json,sys,os
d=os.path.abspath(sys.argv[1])
j={"entity_md":open(d+'/entity.md').read(),"proofs":{"proof-main.tex":open(d+'/proof-main.tex').read()}}
if os.path.exists(d+'/check.py'): j["check_py"]=open(d+'/check.py').read()
json.dump(j,open(d+'/draft.json','w'))
print(d+'/draft.json')
