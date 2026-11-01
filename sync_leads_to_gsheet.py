"""
LeadHunter to Google Sheet Sync Engine
Appends audited leads and complete outreach pitches directly to Ruban's Google Sheet pipeline.
Spreadsheet ID: 1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA
"""
import subprocess
import datetime
import urllib.parse
from pitch_generator import generate_pitch

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

def escape_csv_cell(val) -> str:
    if val is None:
        return ""
    s = str(val).replace("\r", " ").replace("\n", " ").replace('"', '""')
    s = s.replace(",", "\\,")
    return s

def append_lead_to_gsheet(lead: dict, base_domain: str = "https://leads.rvsmps.store") -> bool:
    name = lead.get('name', 'Business')
    city = lead.get('city', 'Bangalore, Karnataka')
    niche = lead.get('niche', 'Luxury Salons')
    url = lead.get('url', '')
    grade = lead.get('grade', 'C')
    score = lead.get('score', 65)
    phone = lead.get('phone', '')
    emails = lead.get('emails', [])
    email = emails[0] if emails else f"contact@{lead.get('domain', '')}"
    flaws = " | ".join(lead.get('flaws', []))
    
    mockup_url = f"{base_domain}/mockup/0?name={urllib.parse.quote(name)}&city={urllib.parse.quote(city)}&niche={urllib.parse.quote(niche)}&domain={urllib.parse.quote(lead.get('domain', ''))}&phone={urllib.parse.quote(phone)}"
    
    pitch = generate_pitch(lead, mockup_url)
    
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    status = "New Lead"
    
    row_cells = [
        escape_csv_cell(now_str),
        escape_csv_cell(status),
        escape_csv_cell(name),
        escape_csv_cell(city),
        escape_csv_cell(niche),
        escape_csv_cell(url),
        escape_csv_cell(grade),
        escape_csv_cell(score),
        escape_csv_cell(phone),
        escape_csv_cell(email),
        escape_csv_cell(flaws),
        escape_csv_cell(mockup_url),
        escape_csv_cell(pitch['subject']),
        escape_csv_cell(pitch['body']),
        escape_csv_cell(pitch['whatsapp_body']),
        escape_csv_cell(pitch['whatsapp_url']),
        escape_csv_cell(pitch['gmail_url']),
        escape_csv_cell("Ready for ₹2,999 outreach")
    ]
    
    row_str = ",".join(row_cells)
    
    cmd = [GSHEETS_CMD, "mutate", "append", SPREADSHEET_ID, "Sheet1", row_str]
    try:
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print("Successfully synced to Google Sheet:", name)
        return True
    except subprocess.CalledProcessError as e:
        print("Failed to sync to Google Sheet:", e.stderr)
        return False

if __name__ == "__main__":
    sample_lead = {
        'name': 'She GLAM Luxury Studio',
        'city': 'Indiranagar, Bangalore',
        'niche': 'Luxury Salons & Spas',
        'url': 'https://sheglam.rvsmps.store',
        'domain': 'sheglam.rvsmps.store',
        'grade': 'D',
        'score': 45,
        'phone': '+91 80986 71563',
        'emails': ['contact@sheglam.rvsmps.store'],
        'flaws': ['Slow mobile rendering', 'Missing instant WhatsApp booking', 'High third-party aggregator reliance']
    }
    append_lead_to_gsheet(sample_lead)
