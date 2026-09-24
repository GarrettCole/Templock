import smtplib
from email.mime.text import MIMEText
from datetime import datetime
for name,ip in [("PC2","192.168.20.101"),("PC3","192.168.30.100"),("SVR1","192.168.20.210"),("SVR2","192.168.30.210")]:
    now=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    body=f"Dear Stakeholders,\n\nThis is an automated alert to inform you that the following device(s) have been identified as compromised during the recent network scan:\n\nDevice Name: {name}\nIP Address: {ip}\nLast Checked: {now}\n\nImmediate investigation and remediation are recommended to prevent further impact.\n\nBest regards,\nNetwork Monitoring System"
    m=MIMEText(body); m['Subject']="URGENT: Device Compromise Detected—Immediate Attention Required"; m['From']="soc@d522.wgu.internal"; m['To']="security@d522.wgu.internal"
    for host,port in [("10.10.10.100",1025),("10.10.10.100",25),("smtp.d522.wgu.internal",25),("192.168.10.15",1025)]:
        try:
            with smtplib.SMTP(host,port,timeout=5) as s: s.send_message(m)
            print(f"{now} ALERT {name} via {host}:{port}"); break
        except Exception as e:
            print(f"try {host}:{port} fail {e}"); continue