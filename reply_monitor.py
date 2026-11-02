"""
LeadHunter AI - Automated Gmail Reply Monitor & CRM Sync
Monitors inbox for replies from pitched leads via IMAP.
When a prospect replies, updates the Google Sheet status to 'Replied (Hot Lead!)' live.
"""
import sys
import os
import time
import datetime
import imaplib
import email
from email.header import decode_header
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

GMAIL_USER = os.environ.get("RUBAN_EMAIL", "rubanvelankanni2003@gmail.com")
GMAIL_APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", "ttdmfubqrzukjema")

def decode_mime_header(header_val):
    if not header_val:
        return ""
    decoded_parts = decode_header(header_val)
    res = ""
    for part, enc in decoded_parts:
        if isinstance(part, bytes):
            res += part.decode(enc or 'utf-8', errors='replace')
        else:
            res += str(part)
    return res

def fetch_contacted_leads():
    """Returns a dict of lead_email.lower(): (row_idx, business_name)."""
    cmd = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R50"]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
        lines = [l.split("\t") for l in res.stdout.splitlines() if l.strip()]
        leads = {}
        for idx, row in enumerate(lines[1:], start=2):
            if len(row) > 9:
                lead_email = row[9].strip().lower()
                name = row[2].strip() if len(row) > 2 else "Lead"
                status = row[1].strip() if len(row) > 1 else ""
                if lead_email and "@" in lead_email:
                    leads[lead_email] = {
                        "row_idx": idx,
                        "name": name,
                        "status": status
                    }
        return leads
    except Exception as e:
        print(f"[!] Error fetching leads from Google Sheet: {e}")
        return {}

def update_gsheet_reply(row_idx: int, reply_sender: str, snippet: str):
    new_status = "Replied (Hot Lead!)"
    cmd_status = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!B{row_idx}", new_status]
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    note_text = f"Replied on {now_str}: {snippet[:50]}"
    cmd_note = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!R{row_idx}", note_text]
    try:
        subprocess.run(cmd_status, capture_output=True, text=True, encoding='utf-8', errors='replace')
        subprocess.run(cmd_note, capture_output=True, text=True, encoding='utf-8', errors='replace')
        print(f"  [🔥 GOOGLE SHEET UPDATED] Row {row_idx} marked as '{new_status}'!")
    except Exception as e:
        print(f"  [!] Failed to update Sheet row {row_idx}: {e}")

def check_for_replies():
    print(f"\n=======================================================")
    print(f"📬 LEAD HUNTER - INBOX REPLY RADAR ({datetime.datetime.now().strftime('%H:%M:%S')})")
    print(f"Account: {GMAIL_USER}")
    print(f"=======================================================")
    
    leads = fetch_contacted_leads()
    print(f"[*] Monitoring replies from {len(leads)} active pipeline leads...")
    
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        mail.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        mail.select("inbox")
        
        # Check messages from today / last 2 days
        date_str = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%d-%b-%Y")
        search_query = f'(SINCE "{date_str}")'
        status, messages = mail.search(None, search_query)
        
        if status != "OK" or not messages[0]:
            print("[✓] No incoming emails in the monitored window yet.")
            mail.logout()
            return
            
        msg_ids = messages[0].split()
        print(f"[*] Scanning {len(msg_ids)} recent incoming emails...")
        
        reply_count = 0
        
        for mid in reversed(msg_ids[-50:]): # Check latest 50
            res, data = mail.fetch(mid, "(RFC822.HEADER BODY[TEXT])")
            if res != "OK":
                continue
                
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            
            from_header = decode_mime_header(msg.get("From", ""))
            subject = decode_mime_header(msg.get("Subject", ""))
            
            sender_email = ""
            if "<" in from_header and ">" in from_header:
                sender_email = from_header.split("<")[1].split(">")[0].lower().strip()
            else:
                sender_email = from_header.lower().strip()
                
            # Check if this sender matches any of our pitched leads
            if sender_email in leads:
                lead_info = leads[sender_email]
                # Avoid triggering on our own sent echoes
                if sender_email == GMAIL_USER.lower():
                    continue
                    
                print(f"\n🎉 [HOT LEAD DETECTED] Incoming reply from: {lead_info['name']} ({sender_email})!")
                print(f"   Subject: {subject}")
                
                # Extract text preview
                body_snippet = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body_snippet = part.get_payload(decode=True).decode('utf-8', errors='replace')[:80]
                            break
                else:
                    body_snippet = msg.get_payload(decode=True).decode('utf-8', errors='replace')[:80]
                    
                print(f"   Snippet: {body_snippet.strip()}")
                
                # Update Google Sheet
                update_gsheet_reply(lead_info['row_idx'], sender_email, body_snippet.strip())
                reply_count += 1
                
        mail.logout()
        print(f"\n[✓] Reply Radar check complete. New replies found: {reply_count}")
        
    except Exception as e:
        print(f"[!] IMAP Radar error: {e}")

def run_standing_monitor(interval_minutes: int = 15):
    print(f"\n📡 Starting standing reply monitor daemon (Checking every {interval_minutes}m)...")
    while True:
        try:
            check_for_replies()
        except Exception as e:
            print(f"[!] Error in monitor loop: {e}")
        time.sleep(interval_minutes * 60)

if __name__ == "__main__":
    if "--daemon" in sys.argv:
        run_standing_monitor(interval_minutes=15)
    else:
        check_for_replies()
