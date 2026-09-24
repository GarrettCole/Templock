import requests
from datetime import datetime
TOKEN=open("B2_DNS_check").read().strip()
H={"Authorization": f"Bearer {TOKEN}","Content-Type":"application/json"}
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
for n,ip in [("PC2","192.168.20.101"),("PC3","192.168.30.100"),("SVR1","192.168.20.210"),("SVR2","192.168.30.210")]:
    p={"title":f"DNS misconfiguration - {n}","device":n,"ip":ip,"issue_type":"DNS configuration mismatch","status":"open","description":f"{n} {ip} ROGUE 203.0.113.10 Expected LAB DNS 10.10.10.10 and 10.10.10.20 Fixed {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}"}
    for url in ["http://helpdesk.d522.wgu.internal:5000/api/tickets","http://10.10.10.200:5008/api/tickets","http://10.10.10.200:5000/api/tickets"]:
        try:
            r=requests.post(url, headers=H, json=p, timeout=5)
            print(f"{n} {r.status_code} {url} {r.text[:500]}")
            if r.status_code in [200,201]: break
        except Exception as e: print(f"{n} try {url} {e}") 