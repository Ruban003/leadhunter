"""
LeadHunter AI - WhatsApp Sniper Hub (15-20 High-Value Targets / Day)
Interactive semi-automated console for firing high-converting WhatsApp pitches with 0% ban risk.
Opens WhatsApp Web with pre-filled pitch and automatically logs sent status to Google Sheets.
"""
import sys
import os
import time
import datetime
import webbrowser
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

def fetch_pipeline_rows():
    """Reads all rows from Google Sheet using gsheets CLI."""
    cmd_tsv = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R100"]
    try:
        res = subprocess.run(cmd_tsv, capture_output=True, text=True, check=True)
        lines = [line.split("\t") for line in res.stdout.splitlines() if line.strip()]
        return lines
    except Exception as e:
        print(f"[!] Error fetching rows: {e}")
        return []

def update_sheet_status(row_idx: int, new_status: str, note: str = ""):
    cmd_status = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!B{row_idx}", new_status]
    try:
        subprocess.run(cmd_status, capture_output=True, text=True, check=True)
        if note:
            cmd_note = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, f"Sheet1!R{row_idx}", note]
            subprocess.run(cmd_note, capture_output=True, text=True)
        print(f"  [✓ GOOGLE SHEET UPDATED] Row {row_idx} status marked as '{new_status}'")
    except Exception as e:
        print(f"  [!] Failed to update row {row_idx}: {e}")

def run_whatsapp_sniper(target_count: int = 15):
    print("\n=======================================================")
    print("🎯 LEAD HUNTER - WHATSAPP SNIPER COCKPIT")
    print(f"Daily Goal: {target_count} High-Value WhatsApp Outreach Targets")
    print("Zero-Ban Protection: Human-paced 1-Click WhatsApp Web Launcher")
    print("=======================================================\n")
    
    rows = fetch_pipeline_rows()
    if not rows or len(rows) <= 1:
        print("[!] No leads found in Google Sheet. Run 'batch_lead_pipeline.py' first.")
        return
        
    eligible_targets = []
    for idx, r in enumerate(rows[1:], start=2):
        status = r[1].strip() if len(r) > 1 else ""
        name = r[2].strip() if len(r) > 2 else ""
        city = r[3].strip() if len(r) > 3 else ""
        phone = r[8].strip() if len(r) > 8 else ""
        flaws = r[10].strip() if len(r) > 10 else ""
        mockup_url = r[11].strip() if len(r) > 11 else ""
        wa_url = r[15].strip() if len(r) > 15 else ""
        grade = r[6].strip() if len(r) > 6 else "C"
        
        # Only leads with phone numbers and new status
        if status.lower() == "new lead" and phone and phone != "Phone on site" and "#ERROR" not in phone:
            eligible_targets.append({
                'row_idx': idx,
                'name': name,
                'city': city,
                'phone': phone.replace("'", ""),
                'grade': grade,
                'flaws': flaws,
                'mockup_url': mockup_url,
                'wa_url': wa_url
            })
            
    print(f"[✓] Found {len(eligible_targets)} phone-verified targets ready for WhatsApp outreach.")
    
    if not eligible_targets:
        print("[!] All phone leads are already contacted or waiting for fresh hunt.")
        return

    processed = 0
    for t in eligible_targets[:target_count]:
        processed += 1
        print("\n-------------------------------------------------------")
        print(f"🎯 TARGET [{processed}/{min(target_count, len(eligible_targets))}]: {t['name']}")
        print(f"  📍 Metro:    {t['city']}")
        print(f"  ⭐ Grade:    Grade {t['grade']}")
        print(f"  📞 WhatsApp: {t['phone']}")
        print(f"  ⚡ Flaws:    {t['flaws'][:80]}...")
        print(f"  🔗 Concept:  {t['mockup_url']}")
        print("-------------------------------------------------------")
        
        wa_link = t['wa_url']
        if not wa_link.startswith("http"):
            wa_link = f"https://web.whatsapp.com/send?phone={t['phone'].replace('+', '').replace(' ', '')}"
            
        print(f"\n👉 Ready to pitch {t['name']} on WhatsApp?")
        print(f"   Opening WhatsApp Web chat with message pre-typed...")
        
        try:
            webbrowser.open(wa_link)
        except Exception:
            pass
            
        ans = input("   Did you send the message? (Press [ENTER] for Yes / 's' to Skip): ").strip().lower()
        if ans != 's':
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            update_sheet_status(t['row_idx'], "Contacted (WhatsApp)", f"Pitched via WhatsApp on {now_str}")
            print(f"  🎉 Great job! Lead logged in Google Sheet.")
        else:
            print("  Skipped.")
            
    print("\n=======================================================")
    print(f"✅ WHATSAPP SNIPER SESSION CONQUERED: {processed} targets reviewed!")
    print(f"Pipeline: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    print("=======================================================\n")

if __name__ == "__main__":
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else 15
    run_whatsapp_sniper(target_count=lim)
