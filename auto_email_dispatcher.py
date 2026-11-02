"""
LeadHunter AI - Automated Professional Cold Email Drip Engine
Dispatches executive HTML + Plaintext tailored proposals with DNS host verification.
Includes professional Ruban Designs executive signature card and live concept CTA button.
"""
import sys
import os
import time
import datetime
import smtplib
import ssl
import socket
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

SENDER_NAME = "Ruban Velankanni | Ruban Designs"
SENDER_EMAIL = os.environ.get("RUBAN_EMAIL", "rubanvelankanni2003@gmail.com")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "ttdmfubqrzukjema")

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
        
    # Discard non-existent demo/test domains
    if any(d in dom for d in ['zarisilk.in', 'studiovert.in', 'artisancoffee.in', 'dentistree.co.in', 'rvsmps.store']):
        return False

    # Verify domain actually resolves in DNS
    try:
        socket.gethostbyname(dom)
        return True
    except Exception:
        return False

def build_professional_email(name: str, city: str, niche: str, domain: str, flaws: list, mockup_url: str):
    """Builds both high-converting Plaintext and Executive HTML email proposals."""
    clean_niche = niche.lower().replace('&', 'and')
    flaws_text = flaws if flaws else ["Slow mobile rendering speed", "Missing direct 1-tap WhatsApp consultation", "Lack of verified customer review showcase"]
    
    # 1. Plain Text Version
    plain_bullets = "\n".join([f"  • {f}" for f in flaws_text[:3]])
    
    plain_body = f"""Hi {name} Team,

I came across your business while researching leading {clean_niche} in {city}. You clearly have an established reputation in the local community.

While reviewing {domain} on mobile, I noticed a few friction points that often cause prospective customers on smartphones to drop off before booking:
{plain_bullets}

Over 70% of clients in {city} now search and book services directly from mobile devices. To show you how an ultra-modern, lightning-fast digital experience would look for your brand, I put together an interactive concept preview:

👉 View Your Live Concept Preview:
{mockup_url}

What this concept includes:
- Lightning-fast mobile loading (<1 second)
- Instant 1-tap WhatsApp inquiry & booking button
- Clean showcase for client reviews, pricing, and verified work
- Zero third-party aggregator commissions

I am an independent Website & UI/UX Designer based in Bengaluru. We launch complete starter packages for local studios starting at just ₹2,999 with a 3 to 4 day turnaround.

No pressure or sales pitch — just wanted to share the concept preview with you. If you'd like to put it live this week or explore custom tweaks, feel free to reply directly to this email or message me on WhatsApp.

Warm regards,

Ruban Velankanni
Independent Website & UI/UX Designer | Ruban Designs
Bengaluru, Karnataka
Portfolio: https://portfolio.rvsmps.store
WhatsApp: +91 80986 71563
"""

    # 2. Executive HTML Version
    html_bullets = "".join([f'<li style="margin-bottom: 8px; color: #334155;">{f}</li>' for f in flaws_text[:3]])
    
    html_body = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; line-height: 1.6; color: #1e293b; background-color: #f8fafc; margin: 0; padding: 20px; }}
  .container {{ max-width: 600px; margin: 0 auto; background: #ffffff; border-radius: 12px; border: 1px solid #e2e8f0; padding: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); }}
  .badge {{ display: inline-block; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; background: #eff6ff; color: #2563eb; padding: 4px 10px; border-radius: 9999px; margin-bottom: 16px; }}
  h2 {{ font-size: 20px; font-weight: 700; color: #0f172a; margin-top: 0; margin-bottom: 16px; }}
  p {{ margin-bottom: 16px; font-size: 14px; color: #334155; }}
  .card {{ background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 8px; padding: 16px; margin: 20px 0; }}
  .cta-btn {{ display: inline-block; background: #0f172a; color: #ffffff !important; font-size: 14px; font-weight: 600; text-decoration: none; padding: 12px 24px; border-radius: 8px; margin: 16px 0; }}
  .signature {{ margin-top: 32px; padding-top: 20px; border-top: 1px solid #e2e8f0; }}
</style>
</head>
<body>
  <div class="container">
    <div class="badge">Website Experience Concept</div>
    <h2>Quick visual upgrade concept for {name}</h2>
    
    <p>Hi {name} Team,</p>
    
    <p>I came across your business while researching premier <strong>{clean_niche} in {city}</strong>. You have an established presence in the community, but while reviewing <strong>{domain}</strong> on mobile, I noticed a few friction points that might be losing you direct bookings:</p>
    
    <div class="card">
      <ul style="margin: 0; padding-left: 20px;">
        {html_bullets}
      </ul>
    </div>
    
    <p>Over 70% of local customers in {city} search and book from their phones. To show you how an ultra-fast, modern mobile experience would look for your brand, I designed an interactive concept preview:</p>
    
    <div style="text-align: center; margin: 24px 0;">
      <a href="{mockup_url}" class="cta-btn" target="_blank">👉 View Live Concept Preview</a>
      <div style="font-size: 12px; color: #64748b; margin-top: 6px;">Live interactive prototype &bull; Mobile-optimized</div>
    </div>
    
    <p><strong>What this design solves:</strong></p>
    <ul style="font-size: 13px; color: #475569; padding-left: 20px;">
      <li>Instant 1-tap WhatsApp consultation &amp; appointment button</li>
      <li>Sub-second mobile load time to stop visitor bounce</li>
      <li>Showcase for 5-star customer testimonials and verified work</li>
      <li>Zero aggregator commissions (100% direct client bookings)</li>
    </ul>
    
    <p>I am an independent UI/UX and web designer based here in Bengaluru. Complete starter launches for local studios start at <strong>₹2,999</strong> with a 3–4 day turnaround.</p>
    
    <p>No hard sales pitch — just wanted to share the concept. If you'd like to launch it or customize the branding, feel free to reply directly to this email or reach out on WhatsApp.</p>
    
    <div class="signature">
      <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
        <tr>
          <td style="width: 50px; vertical-align: top; padding-right: 14px;">
            <div style="width: 44px; height: 44px; border-radius: 50%; background: #0f172a; color: #ffffff; text-align: center; line-height: 44px; font-weight: bold; font-size: 16px;">RV</div>
          </td>
          <td style="vertical-align: middle;">
            <div style="font-size: 15px; font-weight: 700; color: #0f172a;">Ruban Velankanni</div>
            <div style="font-size: 13px; color: #64748b; margin-top: 2px;">Independent Website &amp; UI/UX Designer &bull; Bengaluru</div>
            <div style="font-size: 12px; margin-top: 4px;">
              <a href="https://portfolio.rvsmps.store" style="color: #2563eb; text-decoration: none; font-weight: 500;">portfolio.rvsmps.store</a> &nbsp;&bull;&nbsp; 
              <a href="https://wa.me/918098671563" style="color: #16a34a; text-decoration: none; font-weight: 500;">WhatsApp: +91 80986 71563</a>
            </div>
          </td>
        </tr>
      </table>
    </div>
  </div>
</body>
</html>"""

    return plain_body, html_body

def send_smtp_email(to_email: str, subject: str, plain_body: str, html_body: str) -> bool:
    """Sends a multipart (Plaintext + Executive HTML) email via Gmail SMTP with SSL/TLS."""
    if not GMAIL_APP_PASSWORD:
        print("  [!] Missing GMAIL_APP_PASSWORD.")
        return False
        
    msg = MIMEMultipart('alternative')
    msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach plain text first, then HTML as alternative
    part1 = MIMEText(plain_body, 'plain', 'utf-8')
    part2 = MIMEText(html_body, 'html', 'utf-8')
    msg.attach(part1)
    msg.attach(part2)
    
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"  [✗ SMTP FAILED] Error sending to {to_email}: {e}")
        return False

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
        print(f"  [✓ SHEET UPDATED] Row {row_idx} status set to '{new_status}'")
    except Exception as e:
        print(f"  [!] Failed to update Sheet row {row_idx}: {e}")

if __name__ == "__main__":
    print("[*] Professional Cold Email Dispatch Engine loaded.")
