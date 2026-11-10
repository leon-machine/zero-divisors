import sys
sys.path.insert(0,'.')
from tp.mcp_server import Lab
lab=Lab('store')
for i in sys.argv[1:]:
    c=lab.cone(id=i,direction='future',limit=100000)
    print('##',i,len(c)); 
    for x in c: print('   ',x['id'],'|',x['status'],'|',x['one_liner'][:230])
