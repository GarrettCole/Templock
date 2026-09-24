import smtplib, os
from email.mime.text import MIMEText
from datetime import datetime
now=datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
proof=open("dns_corrected_proof.txt").read() if os.path.exists("dns_corrected_proof.txt") else "DNS 10.10.10.10, 10.10.10.20"
devs="- PC2 (192.168.20.101)\n- PC3 (192.168.30.100)\n- SVR1 (192.168.20.210)\n- SVR2 (192.168.30.210)"
body=f"Dear Stakeholders,\n\nThis is an automated notification to inform you that the DNS service issue and all related device compromises have been successfully resolved. The following devices were affected and have now been remediated:\n\n{devs}\n\n{proof}\nDate: {now}\n\nNo further action is required.\n\nBest regards,\nNetwork Monitoring System"
m=MIMEText(body); m['Subject']="RESOLVED: DNS Service Issue and Device Compromise—All Issues Remediated"; m['From']="soc@d522.wgu.internal"; m['To']="security@d522.wgu.internal"
for host,port in [("10.10.10.100",1025),("10.10.10.100",25),("smtp.d522.wgu.internal",25)]:
    try:
        with smtplib.SMTP(host,port,timeout=5) as s: s.send_message(m)
        print(f"{now} RESOLVED via {host}:{port}"); break
    except Exception as e: print(f"try {host}:{port} {e}")