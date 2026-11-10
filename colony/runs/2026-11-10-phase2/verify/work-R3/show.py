import json,subprocess,sys
for i in sys.argv[1:]:
    lv='formal'
    if ':' in i: i,lv=i.split(':')
    r=subprocess.run(['python3','colony/labcli.py','get_claim',json.dumps({"id":i})],capture_output=True,text=True)
    try: d=json.loads(r.stdout)
    except Exception as e: print(i,'ERR',r.stdout[:300],r.stderr[:300]); continue
    fm=d.get('front_matter',{})
    print('#####',i,'v',fm.get('version'),fm.get('status'),'|',fm.get('title'))
    print(d.get('levels',{}).get(lv,'')); print()
