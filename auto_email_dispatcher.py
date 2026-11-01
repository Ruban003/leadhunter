"""
LeadHunter AI - Automated Cold Email Drip Dispatcher Engine
Dispatches tailored cold emails with safe human-like intervals (3-4 mins) to avoid spam filters.
Updates the Google Sheet row status to 'Contacted (Email)' live upon sending.
"""
import sys
import os
import time
import datetime
import smtplib
import ssl
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

# Default configuration (Can be set via environment variables or prompt)
def is_valid_company_email(email: str) -> bool:
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    if len(parts) != 2:
        return False
    user, dom = parts
    if not user or not dom or "." not in dom:
        return False
    # Discard version strings or library tags
    if any(k in email.lower() for k in ['sentry', 'wixpress', 'schema.org', 'cloudflare', '1.1.', '0.0.', '2.0.']):
        return False
    tld = dom.split(".")[-1].lower()
    return tld in ['com', 'in', 'co.in', 'org', 'net', 'io', 'ai', 'biz', 'store', 'online']
SENDER_EMAIL = os.environ.get("RUBAN_EMAIL", "rubanvelankanni8@gmail.com")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "") # 16-character Google App Password

def fetch_pipeline_rows():
    """Reads all rows from Google Sheet using gsheets CLI."""
    cmd = [GSHEETS_CMD, "readonly", "read-all", SPREADSHEET_ID, "--json"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        # Parse output
        import json
        data = json.loads(res.stdout)
        return data.get("values", [])
    except Exception as e:
        print(f"[!] Error fetching Google Sheet rows: {e}")
        # Fallback to TSV read
        cmd_tsv = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R100"]
        res_tsv = subprocess.run(cmd_tsv, capture_output=True, text=True)
        lines = [line.split("\t") for line in res_tsv.stdout.splitlines() if line.strip()]
        return lines

def update_gsheet_status(row_idx: int, new_status: str, note: str = ""):
    """Updates the status and notes cells for a specific row in Google Sheet."""
    cmd_status = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!B{row_idx}", new_status]
    try:
        subprocess.run(cmd_status, capture_output=True, text=True, check=True)
        if note:
            cmd_note = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!R{row_idx}", note]
            subprocess.run(cmd_note, capture_output=True, text=True)
        print(f"  [✓ SHEET UPDATED] Row {row_idx} status set to '{new_status}'")
    except Exception as e:
        print(f"  [!] Failed to update Sheet row {row_idx}: {e}")

def send_smtp_email(to_email: str, subject: str, body_text: str) -> bool:
    """Sends a single cold email via Gmail SMTP with TLS."""
    if not GMAIL_APP_PASSWORD:
        return False
        
    msg = MIMEMultipart()
    msg['From'] = f"{SENDER_NAME} <{SENDER_EMAIL}>"
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body_text, 'plain', 'utf-8'))
    
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(SENDER_EMAIL, GMAIL_APP_PASSWORD)
            server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        return True
    except Exception as e:
        print(f"  [✗ SMTP FAILED] Error sending to {to_email}: {e}")
        return False

def run_email_dispatcher(limit: int = 30, interval_sec: int = 180, live: bool = False):
    print("\n=======================================================")
    print("📧 LEAD HUNTER - AUTOMATED COLD EMAIL DRIP ENGINE")
    print(f"Mode: {'🟢 LIVE SENDING' if live else '🟡 DRY-RUN / AUDIT SIMULATION'}")
    print(f"Daily Target Limit: {limit} emails | Human Drip Interval: {interval_sec}s")
    print("=======================================================\n")
    
    rows = fetch_pipeline_rows()
    if not rows or len(rows) <= 1:
        print("[!] No leads found in Google Sheet.")
        return
        
    header = rows[0]
    print(f"[✓] Connected to Google Sheet. Found {len(rows)-1} total records.\n")
    
    dispatched_count = 0
    
    # Header format: [Timestamp, Status, Business Name, City, Niche, Website, Grade, Score, Phone, Email, Flaws, Mockup URL, Subject, Email Body, ...]
    for idx, row in enumerate(rows[1:], start=2):
        if dispatched_count >= limit:
            print(f"\n[★] Reached daily limit of {limit} dispatched emails.")
            break
            
        status = row[1].strip() if len(row) > 1 else ""
        name = row[2].strip() if len(row) > 2 else "Business Owner"
        email = row[9].strip() if len(row) > 9 else ""
        subject = row[12].strip() if len(row) > 12 else f"Quick visual upgrade concept for {name}"
        body = row[13].strip() if len(row) > 13 else ""
        mockup_url = row[11].strip() if len(row) > 11 else ""
        
        # Only process "New Lead" entries with valid emails
        if status.lower() == "new lead" and is_valid_company_email(email):
            print(f"-------------------------------------------------------")
            print(f"[{dispatched_count + 1}/{limit}] TARGET: {name}")
            print(f"  Recipient: {email}")
            print(f"  Subject:   {subject}")
            print(f"  Mockup:    {mockup_url}")
            
            if live and GMAIL_APP_PASSWORD:
                print(f"  [🚀 SENDING] Dispatching via Gmail SMTP...")
                success = send_smtp_email(email, subject, body)
                if success:
                    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                    update_gsheet_status(idx, "Contacted (Email)", f"Dispatched on {now_str}")
                    dispatched_count += 1
                    print(f"  [⏳ DRIP PAUSE] Waiting {interval_sec}s before next email (protecting inbox reputation)...")
                    time.sleep(interval_sec)
                else:
                    print(f"  [!] Skipped due to send failure.")
            else:
                # Dry run
                print(f"  [SIMULATED] Email preview verified. (Set GMAIL_APP_PASSWORD and pass --live to dispatch).")
                dispatched_count += 1
                time.sleep(1)
                
    print("\n=======================================================")
    print(f"✅ EMAIL DISPATCH RUN FINISHED: {dispatched_count} leads processed.")
    print(f"Live Pipeline: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    print("=======================================================\n")

if __name__ == "__main__":
    is_live = "--live" in sys.argv
    lim = 30
    for arg in sys.argv:
        if arg.startswith("--limit="):
            lim = int(arg.split("=")[1])
            
    run_email_dispatcher(limit=lim, interval_sec=180, live=is_live)
