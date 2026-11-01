"""
LeadHunter to Google Sheet Sync Engine (Clean CSV Ingestion)
Syncs audited leads and complete outreach pitches to Ruban's Google Sheet pipeline.
Spreadsheet ID: 1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA
"""
import csv
import os
import subprocess
import datetime
import urllib.parse
from pitch_generator import generate_pitch

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

HEADERS = [
    "Timestamp", "Status", "Business Name", "City", "Niche", "Website",
    "Grade", "Score", "Phone / WhatsApp", "Email", "Audit Flaws",
    "Mockup Preview URL", "Email Subject", "Email Pitch Body",
    "WhatsApp Pitch", "WhatsApp 1-Click Link", "Gmail 1-Click Link", "Notes"
]

def format_lead_row(lead: dict, base_domain: str = "https://leads.rvsmps.store") -> list:
    name = lead.get('name', 'Business')
    city = lead.get('city', 'Bangalore, Karnataka')
    niche = lead.get('niche', 'Luxury Salons')
    url = lead.get('url', '')
    grade = lead.get('grade', 'C')
    score = f"{lead.get('score', 65)}%"
    
    raw_phone = str(lead.get('phone', '')).strip()
    if raw_phone and not raw_phone.startswith("'"):
        phone = f"'{raw_phone}"
    else:
        phone = raw_phone
        
    emails = lead.get('emails', [])
    email = emails[0] if emails else f"contact@{lead.get('domain', '')}"
    flaws = " | ".join(lead.get('flaws', []))
    
    mockup_url = f"{base_domain}/mockup/0?name={urllib.parse.quote(name)}&city={urllib.parse.quote(city)}&niche={urllib.parse.quote(niche)}"
    pitch = generate_pitch(lead, mockup_url)
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    status = "New Lead"
    
    # Sanitize pitch text so no internal raw newlines break cells
    email_body = pitch['body'].replace('\r\n', ' ').replace('\n', ' ')
    wa_body = pitch['whatsapp_body'].replace('\r\n', ' ').replace('\n', ' ')
    
    return [
        now_str,
        status,
        name,
        city,
        niche,
        url,
        grade,
        score,
        phone,
        email,
        flaws,
        mockup_url,
        pitch['subject'],
        email_body,
        wa_body,
        pitch['whatsapp_url'],
        pitch['gmail_url'],
        "₹2,999 Starter Launch"
    ]

def sync_batch_to_gsheet(leads: list, base_domain: str = "https://leads.rvsmps.store") -> bool:
    """Writes all leads cleanly into a temporary RFC 4180 CSV and imports into Google Sheet."""
    if not leads:
        return True
        
    temp_csv = os.path.join(os.path.dirname(__file__), "temp_gsheet_sync.csv")
    
    # Read existing rows to avoid overwriting headers
    try:
        read_cmd = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R100"]
        existing = subprocess.run(read_cmd, capture_output=True, text=True, check=True).stdout
        existing_lines = [l.strip() for l in existing.splitlines() if l.strip()]
    except Exception:
        existing_lines = []

    # Write CSV
    with open(temp_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        # Always write headers first
        writer.writerow(HEADERS)
        
        # Append existing rows if any (excluding header)
        for line in existing_lines[1:]:
            parts = line.split("\t")
            if len(parts) >= 2:
                # pad to 18
                while len(parts) < 18:
                    parts.append("")
                writer.writerow(parts[:18])
                
        # Append new leads
        for lead in leads:
            writer.writerow(format_lead_row(lead, base_domain))
            
    # Import CSV cleanly into Sheet1
    cmd = [GSHEETS_CMD, "mutate", "import-csv", SPREADSHEET_ID, temp_csv, "--sheet", "Sheet1"]
    try:
        subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(f"Successfully synced {len(leads)} leads to Google Sheet via clean CSV.")
        return True
    except subprocess.CalledProcessError as e:
        print("Failed to import CSV into Google Sheet:", e.stderr)
        return False
