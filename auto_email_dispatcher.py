"""
LeadHunter AI - Automated Professional Cold Email Drip Engine
Dispatches executive HTML + Plaintext tailored proposals with DNS host verification.
Uses Resend API (ruban@rvsmps.store) with custom domain authentication and Gmail SMTP fallback.
Includes professional Ruban Designs executive signature card and live concept CTA button.
"""
import sys
import os
import time
import datetime
import smtplib
import ssl
import socket
import urllib.request
import urllib.error
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

def _get_secret(env_var: str, file_name: str) -> str:
    val = os.environ.get(env_var, "")
    if not val:
        path = os.path.join(os.path.dirname(__file__), file_name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                val = f.read().strip()
    return val

# Resend Custom Domain Config
RESEND_API_KEY = _get_secret("RESEND_API_KEY", ".resend_key")
SENDER_NAME = "Ruban Velankanni | Ruban Designs"
PRIMARY_SENDER = f"{SENDER_NAME} <ruban@rvsmps.store>"
REPLY_TO_EMAIL = "rubanvelankanni2003@gmail.com"

# Secondary Fallback (Gmail SMTP)
SENDER_EMAIL = os.environ.get("RUBAN_EMAIL", "rubanvelankanni2003@gmail.com")
GMAIL_APP_PASSWORD = _get_secret("GMAIL_APP_PASSWORD", ".gmail_key")

def is_valid_company_email(email_str: str) -> bool:
    """Validates email format and verifies domain actually exists via DNS host resolution."""
    if not email_str or "@" not in email_str:
        return False
    parts = email_str.split("@")
    if len(parts) != 2:
        return False
    user, dom = parts
    dom = dom.strip().lower()
    if not user or not dom or "." not in dom:
        return False
        
    # Discard libraries, analytics, framework tags
    if any(k in email_str.lower() for k in [
        'sentry', 'wixpress', 'schema.org', 'cloudflare', '1.1.', '0.0.', '2.0.',
        'rspack', 'boxicons', 'webpack', 'react', 'vue', 'npm'
    ]):
        return False
        
    # Discard non-existent demo/test domains & aggregators
    if any(d in dom for d in ['zarisilk.in', 'studiovert.in', 'artisancoffee.in', 'dentistree.co.in', 'rvsmps.store', 'hexahealth.com', 'bodycraft.co.in']):
        return False

    # Verify domain actually resolves in DNS
    try:
        socket.gethostbyname(dom)
        return True
    except Exception:
        return False

def get_niche_case_study(niche: str) -> str:
    """Returns an industry-specific social proof reference instead of generic copy."""
    nl = niche.lower()
    if any(k in nl for k in ['dental', 'clinic', 'doctor', 'health', 'aesthetic']):
        return "I recently redesigned the patient appointment flow for local medical & dental practices, adding instant 1-tap WhatsApp consultation and treatment galleries that cut mobile drop-off by over 35%."
    elif any(k in nl for k in ['salon', 'spa', 'beauty', 'hair', 'makeover']):
        return "I recently built the direct booking platform for She GLAM Studio (https://sheglam.rvsmps.store), allowing clients to book stylists directly without paying 20-25% aggregator commissions."
    elif any(k in nl for k in ['architecture', 'interior', 'designer', 'home', 'decor']):
        return "I recently developed high-speed luxury editorial portfolios for interior architects in Bengaluru, showcasing high-resolution project galleries with sub-second mobile loading."
    elif any(k in nl for k in ['bridal', 'couture', 'boutique', 'fashion']):
        return "I recently designed luxury boutique showcases with instant WhatsApp trial fitting schedules for premier bridal designers in Bengaluru."
    elif any(k in nl for k in ['cafe', 'dining', 'restaurant', 'food', 'bistro']):
        return "I recently developed interactive mobile digital menus with instant table reservations, eliminating clunky PDF downloads and aggregator fees."
    else:
        return "I recently engineered high-converting mobile experiences for local Bengaluru businesses, increasing direct customer inquiries by over 30%."

def build_artisan_email(name: str, city: str, niche: str, domain: str, flaws: list, mockup_url: str):
    """
    Style 1: The Apple Minimalist / Personal Designer Note.
    100% human-crafted tone. Zero corporate boxes or badges.
    Looks and feels like a personal note typed directly by Ruban on Apple Mail.
    """
    flaws_text = flaws if flaws else ["Slow mobile rendering speed", "Missing direct 1-tap WhatsApp consultation", "Lack of verified customer review showcase"]
    case_study = get_niche_case_study(niche)
    
    # Plain text bullets
    plain_bullets = "\n".join([f"  • {f}" for f in flaws_text[:3]])
    
    plain_body = f"""Hey {name} Team,

I was looking at {domain} on my phone earlier and noticed a couple of friction points with the mobile experience:
{plain_bullets}

Instead of just pointing them out, I spent 20 minutes putting together a clean, interactive mobile prototype to show how effortless your direct customer booking could look:

👉 View the live interactive preview:
{mockup_url}

{case_study}

I'm an independent UI/UX designer based here in Bengaluru (Ruban Designs). If you like the direction and want to use this layout for your brand, I'm happy to help you put it live this week or hand over the clean code. If not, no worries at all — hope the concept gives some good inspiration for your team!

Best,

Ruban Velankanni
Independent Website & UI Designer | Ruban Designs
Bengaluru • WhatsApp: +91 80986 71563
portfolio.rvsmps.store
"""

    # HTML bullets
    html_bullets = "".join([f'<li style="margin-bottom: 6px; color: #334155;">{f}</li>' for f in flaws_text[:3]])

    html_body = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 1.6; color: #1e293b; background-color: #ffffff; margin: 0; padding: 12px;">
  <p style="margin-top: 0; margin-bottom: 16px;">Hey {name} Team,</p>
  
  <p style="margin-bottom: 16px;">I was looking at <strong>{domain}</strong> on my phone earlier and noticed a couple of friction points with the mobile experience:</p>
  
  <ul style="margin: 0 0 18px 0; padding-left: 20px;">
    {html_bullets}
  </ul>
  
  <p style="margin-bottom: 16px;">Instead of just pointing them out, I spent 20 minutes putting together a clean, interactive mobile prototype to show how effortless your direct customer booking could look:</p>
  
  <p style="margin: 18px 0; padding: 12px 16px; background-color: #f8fafc; border-left: 3px solid #0f172a; border-radius: 4px;">
    <strong>👉 View Live Concept Preview:</strong><br>
    <a href="{mockup_url}" style="color: #2563eb; text-decoration: underline; font-weight: 500; word-break: break-all;">{mockup_url}</a>
  </p>
  
  <p style="margin-bottom: 16px; color: #475569; font-size: 14px;"><em>{case_study}</em></p>
  
  <p style="margin-bottom: 16px;">I'm an independent UI/UX designer based here in Bengaluru (Ruban Designs). If you like the direction and want to use this layout for your brand, I'm happy to help you put it live this week or hand over the clean code. If not, no worries at all — hope the prototype gives you some good design ideas!</p>
  
  <div style="margin-top: 28px; padding-top: 16px; border-top: 1px solid #e2e8f0; font-size: 14px; color: #475569;">
    <strong style="color: #0f172a; font-size: 15px;">Ruban Velankanni</strong><br>
    Independent Website &amp; UI Designer &bull; Ruban Designs<br>
    Bengaluru &bull; <a href="https://wa.me/918098671563" style="color: #16a34a; text-decoration: none;">WhatsApp: +91 80986 71563</a><br>
    <a href="https://portfolio.rvsmps.store" style="color: #2563eb; text-decoration: none;">portfolio.rvsmps.store</a>
  </div>
</body>
</html>"""

    return plain_body, html_body

def build_punchy_email(name: str, city: str, niche: str, domain: str, flaws: list, mockup_url: str):
    """
    Style 2: The Short & Punchy 4-Liner.
    Under 65 words. Respects busy owners' time. Gets straight to the point.
    """
    flaws_summary = flaws[0] if flaws else "slow mobile load latency"
    
    plain_body = f"""Hey {name} Team,

Your brand visuals look great, but while viewing {domain} on mobile earlier, I noticed {flaws_summary.lower()} that makes direct booking on smartphones tricky.

I put together an interactive mobile prototype to show how clean and instant it could look:
👉 {mockup_url}

It takes 30 seconds to tap through on your phone. Would you be open to me putting this live for your team this week?

Best,

Ruban Velankanni | Ruban Designs
WhatsApp: +91 80986 71563 • portfolio.rvsmps.store
"""

    html_body = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; font-size: 15px; line-height: 1.6; color: #1e293b; background-color: #ffffff; margin: 0; padding: 12px;">
  <p style="margin-top: 0; margin-bottom: 14px;">Hey {name} Team,</p>
  
  <p style="margin-bottom: 14px;">Your brand visuals look great, but while viewing <strong>{domain}</strong> on mobile earlier, I noticed {flaws_summary.lower()} that makes direct booking on smartphones tricky.</p>
  
  <p style="margin-bottom: 14px;">I put together an interactive mobile prototype to show how clean and instant it could look:</p>
  
  <p style="margin: 16px 0; padding: 10px 14px; background-color: #f8fafc; border-left: 3px solid #0f172a; border-radius: 4px;">
    👉 <strong>Interactive Preview:</strong> <a href="{mockup_url}" style="color: #2563eb; text-decoration: underline; font-weight: 500;">{mockup_url}</a>
  </p>
  
  <p style="margin-bottom: 16px;">It takes 30 seconds to tap through on your phone. Would you be open to me putting this live for your team this week?</p>
  
  <div style="margin-top: 24px; padding-top: 14px; border-top: 1px solid #e2e8f0; font-size: 14px; color: #475569;">
    <strong style="color: #0f172a;">Ruban Velankanni</strong> &bull; Ruban Designs<br>
    <a href="https://wa.me/918098671563" style="color: #16a34a; text-decoration: none;">WhatsApp: +91 80986 71563</a> &bull; <a href="https://portfolio.rvsmps.store" style="color: #2563eb; text-decoration: none;">portfolio.rvsmps.store</a>
  </div>
</body>
</html>"""

    return plain_body, html_body

def build_professional_email(name: str, city: str, niche: str, domain: str, flaws: list, mockup_url: str):
    # Default to the Human Artisan style
    return build_artisan_email(name, city, niche, domain, flaws, mockup_url)

def send_resend_email(to_email: str, subject: str, plain_body: str, html_body: str) -> tuple[bool, str]:
    """Sends a multipart email via Resend API using verified custom domain ruban@rvsmps.store."""
    if not RESEND_API_KEY:
        return False, "Missing RESEND_API_KEY"
        
    payload = {
        "from": PRIMARY_SENDER,
        "to": [to_email],
        "reply_to": REPLY_TO_EMAIL,
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
            msg_id = data.get("id", "ok")
            print(f"  [+] Resend sent to {to_email} (ID: {msg_id})")
            return True, msg_id
    except urllib.error.HTTPError as e:
        err = e.read().decode("utf-8", errors="replace")
        print(f"  [-] Resend HTTP error {e.code}: {err}")
        return False, err
    except Exception as e:
        print(f"  [-] Resend error: {e}")
        return False, str(e)

def send_smtp_fallback(to_email: str, subject: str, plain_body: str, html_body: str) -> bool:
    """Fallback to Gmail SMTP if Resend fails."""
    if not GMAIL_APP_PASSWORD:
        return False
        
    msg = MIMEMultipart('alternative')
    msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    part1 = MIMEText(plain_body, 'plain', 'utf-8')
    part2 = MIMEText(html_body, 'html', 'utf-8')
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        print(f"  [+] Gmail SMTP fallback sent to {to_email}")
        return True
    except Exception as e:
        print(f"  [-] Gmail SMTP fallback failed for {to_email}: {e}")
        return False

def dispatch_email(to_email: str, subject: str, plain_body: str, html_body: str) -> bool:
    """Primary dispatch with Resend (ruban@rvsmps.store) + fallback."""
    ok, _ = send_resend_email(to_email, subject, plain_body, html_body)
    if ok:
        return True
    print("  [*] Attempting Gmail SMTP fallback...")
    return send_smtp_fallback(to_email, subject, plain_body, html_body)

def fetch_pipeline_rows():
    """Reads all rows from Google Sheet using gsheets CLI."""
    cmd_tsv = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R100"]
    try:
        res = subprocess.run(cmd_tsv, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
        lines = [line.split("\t") for line in res.stdout.splitlines() if line.strip()]
        return lines
    except Exception as e:
        print(f"[!] Error fetching Google Sheet rows: {e}")
        return []

def update_gsheet_status(row_idx: int, new_status: str, note: str = ""):
    """Updates the status and notes cells for a specific row in Google Sheet."""
    cmd_status = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!B{row_idx}", new_status]
    try:
        subprocess.run(cmd_status, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
        if note:
            cmd_note = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!R{row_idx}", note]
            subprocess.run(cmd_note, capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(f"  [+] Sheet row {row_idx} status updated to '{new_status}'")
    except Exception as e:
        print(f"  [-] Failed to update Sheet row {row_idx}: {e}")

if __name__ == "__main__":
    print("[*] Professional Cold Email Dispatch Engine loaded.")
    print(f"[*] Primary Sender: {PRIMARY_SENDER}")
    print(f"[*] Reply-To: {REPLY_TO_EMAIL}")
