import paramiko
from datetime import datetime
USER="ubuntu"; PASS="ubuntu"; LAB1="10.10.10.10"; ROGUE="203.0.113.10"
DEVS=[("PC2","192.168.20.101"),("PC3","192.168.30.100"),("SVR1","192.168.20.210"),("SVR2","192.168.30.210"),("PC1","192.168.10.102")]
print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')} LAB {LAB1}")
for n,ip in DEVS:
    try:
        c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        c.connect(ip, username=USER, password=PASS, timeout=8, look_for_keys=False, allow_agent=False)
        _,o,_=c.exec_command("cat /etc/resolv.conf"); d=o.read().decode()
        st="OK" if LAB1 in d and ROGUE not in d else "ROGUE"
        print(f"{n} {st} - {ip} - {d.strip()[:120]}"); c.close()
    except Exception as e: print(f"{n} ROGUE - {ip} - {e}") 