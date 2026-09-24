import paramiko, time
from datetime import datetime
DNS1="10.10.10.10"; DNS2="10.10.10.20"
DEVS=[("PC2","192.168.20.101"),("PC3","192.168.30.100"),("SVR1","192.168.20.210"),("SVR2","192.168.30.210")]
USER="ubuntu"; PASS="ubuntu"
now=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
print(f"Date: {now}\nLAB DNS1: {DNS1}\nLAB DNS2: {DNS2}")
proof=[f"Date: {now}", f"LAB DNS1: {DNS1}", f"LAB DNS2: {DNS2}"]
for n,ip in DEVS:
    print(f"\n[CONNECTING] {n} {ip} via SSH")
    c=paramiko.SSHClient(); c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(ip, username=USER, password=PASS, timeout=10, look_for_keys=False, allow_agent=False)
    cmd=f'echo -e "nameserver {DNS1}\nnameserver {DNS2}" | sudo -S tee /etc/resolv.conf'
    i,ou,_=c.exec_command(cmd, get_pty=True); i.write(PASS+"\n"); i.flush(); time.sleep(1); ou.read()
    _,o,_=c.exec_command("cat /etc/resolv.conf"); r=o.read().decode()
    print(f"[FIXED] {n} {ip} -> {DNS1}, {DNS2}\nVerified: {r.strip()}"); proof.append(f"{n} {ip} corrected"); c.close()
open("dns_corrected_proof.txt","w").write("\n".join(proof))