import json,sys
data_path, today_path = sys.argv[1], sys.argv[2]
try: d=json.load(open(data_path,encoding='utf-8'))
except Exception: d={"snaps":[],"monthly":[]}
t=json.load(open(today_path,encoding='utf-8'))
snaps=[s for s in d.get("snaps",[]) if s.get("date")!=t.get("date")]
snaps.insert(0,t)
snaps.sort(key=lambda s:s.get("date",""), reverse=True)
d["snaps"]=snaps; d["updated"]=t.get("date")
if "monthly" not in d: d["monthly"]=[]
json.dump(d, open(data_path,'w',encoding='utf-8'), ensure_ascii=False, separators=(',',':'))
print("merged",t.get("date"),"total",len(snaps))
