import urllib.request
import json
import socket
import os
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

RESEND_API_KEY = open(os.path.join(os.path.dirname(__file__), '.resend_key')).read().strip()
SENDER = "Ruban Velankanni | Ruban Designs <ruban@rvsmps.store>"
REPLY_TO = "rubanvelankanni2003@gmail.com"

def send_resend_email(to_email: str, subject: str, plain_body: str, html_body: str):
    """Dispatches professional HTML + Plaintext email via Resend API."""
    payload = {
        "from": SENDER,
        "to": [to_email],
        "reply_to": REPLY_TO,
        "subject": subject,
        "text": plain_body,
        "html": html_body
    }
    
    req = urllib.request.Request(
        "https://api.resend.com/emails",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {RESEND_API_KEY}",
            "Content-Type": "application/json",
            "User-Agent": "resend-python/2.0.0"
        }
    )
    
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"  [+] RESEND SUCCESS ID: {data.get('id')}")
            return True, data.get("id")
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8")
        print(f"  [-] RESEND HTTP ERROR {e.code}: {err_msg}")
        return False, err_msg
    except Exception as e:
        print(f"  [-] RESEND ERROR: {e}")
        return False, str(e)

if __name__ == "__main__":
    ok, res = send_resend_email(
        "rubanvelankanni2003@gmail.com",
        "🚀 Verification Pass: Custom Domain ruban@rvsmps.store Active",
        "Hi Ruba,\n\nYour official custom domain sending is 100% active and verified via Resend!\n\nBest,\nLuffy",
        "<div style='font-family:sans-serif;padding:20px;border:1px solid #e2e8f0;border-radius:8px;'><h2 style='color:#0f172a;'>🚀 Custom Domain 100% Verified!</h2><p>Hi Ruba,</p><p>Your domain <b>rvsmps.store</b> is fully operational. Outgoing pitches now send from <b>ruban@rvsmps.store</b>, while client replies route straight back to your Gmail.</p><p><i>— Luffy & the LeadHunter Flywheel</i></p></div>"
    )
    print("Test status:", ok, res)
