"""
LeadHunter AI - Automated Batch Ingestion Engine (50 Leads / Day)
Hunts, audits, crafts pitches, and stores 50 high-ticket Bangalore business leads directly into Google Sheets.
"""
import sys
import os
import time
import datetime
import urllib.parse
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from scraper import search_leads
from auditor import audit_lead
from pitch_generator import generate_pitch

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"
BASE_DOMAIN = "https://leads.rvsmps.store"

TARGET_NICHES = [
    ("Luxury Salons & Spas", "Indiranagar, Bangalore"),
    ("Dental & Aesthetic Clinics", "Koramangala, Bangalore"),
    ("Bridal Makeover & Couture", "Jayanagar, Bangalore"),
    ("Dermatology & Skin Centers", "HSR Layout, Bangalore"),
    ("Luxury Architecture & Interiors", "Whitefield, Bangalore")
]

def clean_for_gsheets(val) -> str:
    if val is None:
        return ""
    s = str(val).replace("\r", " ").replace("\n", " ").replace('"', '""')
    s = s.replace(",", "\\,")
    return s

def hunt_and_append_batch(total_target: int = 50, per_niche: int = 10) -> list:
    print(f"\n=======================================================")
    print(f"🚀 INITIATING 50-LEAD DAILY AUTOMATION PIPELINE")
    print(f"Target: {total_target} leads across {len(TARGET_NICHES)} Bengaluru high-ticket niches")
    print(f"Pipeline: Google Sheet ({SPREADSHEET_ID})")
    print(f"=======================================================\n")
    
    collected_leads = []
    
    for niche, city in TARGET_NICHES:
        if len(collected_leads) >= total_target:
            break
            
        print(f"\n[🔍 SEARCHING] Niche: '{niche}' in '{city}'...")
        raw_leads = search_leads(niche, city, limit=per_niche)
        print(f"  Found {len(raw_leads)} potential domains. Beginning deep mobile/speed audit...")
        
        for l in raw_leads:
            if len(collected_leads) >= total_target:
                break
                
            res = audit_lead(l)
            name = res.get('name', 'Business')
            grade = res.get('grade', 'C')
            score = res.get('score', 60)
            phone = res.get('phone', '')
            emails = res.get('emails', [])
            email = emails[0] if emails else f"contact@{res.get('domain', '')}"
            flaws = " | ".join(res.get('flaws', []))
            
            mockup_url = f"{BASE_DOMAIN}/mockup/0?name={urllib.parse.quote(name)}&city={urllib.parse.quote(city)}&niche={urllib.parse.quote(niche)}&domain={urllib.parse.quote(res.get('domain', ''))}&phone={urllib.parse.quote(phone)}"
            pitch = generate_pitch(res, mockup_url)
            
            now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            
            # Format phone safely for Google Sheets (prefix with single quote so it doesn't parse as formula)
            safe_phone = f"'{phone}" if phone else "Phone on site"
            
            row_cells = [
                clean_for_gsheets(now_str),
                clean_for_gsheets("New Lead"),
                clean_for_gsheets(name),
                clean_for_gsheets(city),
                clean_for_gsheets(niche),
                clean_for_gsheets(res.get('url', '')),
                clean_for_gsheets(grade),
                clean_for_gsheets(f"{score}%"),
                clean_for_gsheets(safe_phone),
                clean_for_gsheets(email),
                clean_for_gsheets(flaws),
                clean_for_gsheets(mockup_url),
                clean_for_gsheets(pitch['subject']),
                clean_for_gsheets(pitch['body']),
                clean_for_gsheets(pitch['whatsapp_body']),
                clean_for_gsheets(pitch['whatsapp_url']),
                clean_for_gsheets(pitch['gmail_url']),
                clean_for_gsheets("₹2,999 Starter Launch")
            ]
            
            row_str = ",".join(row_cells)
            cmd = [GSHEETS_CMD, "mutate", "append", SPREADSHEET_ID, "Sheet1", row_str]
            
            try:
                subprocess.run(cmd, capture_output=True, text=True, check=True)
                print(f"  [✓ APPENDED] {name} (Grade: {grade}, Phone: {phone or 'N/A'})")
                res['pitch_data'] = pitch
                collected_leads.append(res)
            except Exception as e:
                print(f"  [✗ SHEET ERROR] Could not append {name}: {e}")
                
            time.sleep(1) # respectful pause
            
    print(f"\n=======================================================")
    print(f"✅ BATCH COMPLETED: {len(collected_leads)} Leads Ingested into Google Sheet!")
    print(f"Sheet URL: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    print(f"=======================================================\n")
    return collected_leads

if __name__ == "__main__":
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    hunt_and_append_batch(total_target=count, per_niche=max(2, count // len(TARGET_NICHES)))
