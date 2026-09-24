import requests
from datetime import datetime, timezone

TOKEN="vGkbXkGLqQSo7YLflp9DutuG8st4xdPPF7wnTcwB0FE"


H = {
    "Authorization":f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json",
}

print(
    f"Date: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}"
)

devices = [
    ("PC2", "192.168.20.101"),
    ("PC3", "192.168.30.100"),
    ("SVR1", "192.168.20.210"),
    ("SVR2", "192.168.30.210"),
]

urls = [
    "http://helpdesk.d522.wgu.internal:5000/api/tickets"
]

for n, ip in devices:
    p = {
        "title": f"DNS misconfiguration - {n}",
        "device": n,
        "ip": ip,
        "issue_type": "DNS configuration mismatch",
        "status": "open",
        "description": (
            f"{n} {ip} ROGUE 203.0.113.10 "
            f"Expected LAB DNS 10.10.10.10 and 10.10.10.20 "
            f"Fixed {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}"
        ),
    }

    for url in urls:
        try:
            r = requests.post(
                url,
                headers=H,
                json=p,
                timeout=5,
            )

            print("Status:", r.status_code)
            print("Response:", r.text)
            print("WWW-Authenticate:", r.headers.get("WWW-Authenticate"))

            if r.status_code in (200, 201):
                break

        except requests.RequestException as e:
            print(f"{n} {url} ERROR: {e}")