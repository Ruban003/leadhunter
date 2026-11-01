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
from sync_leads_to_gsheet import sync_batch_to_gsheet

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
BASE_DOMAIN = "https://leads.rvsmps.store"

TARGET_NICHES = [
    ("Luxury Salons & Spas", "Indiranagar, Bangalore"),
    ("Dental & Aesthetic Clinics", "Koramangala, Bangalore"),
    ("Bridal Makeover & Couture", "Jayanagar, Bangalore"),
    ("Dermatology & Skin Centers", "HSR Layout, Bangalore"),
    ("Luxury Architecture & Interiors", "Whitefield, Bangalore")
]

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
        
        batch_for_niche = []
        for l in raw_leads:
            if len(collected_leads) >= total_target:
                break
                
            res = audit_lead(l)
            res['niche'] = niche
            res['city'] = city
            name = res.get('name', 'Business')
            grade = res.get('grade', 'C')
            score = res.get('score', 60)
            
            print(f"    Audited: {name[:30]} | Grade {grade} ({score}%)")
            collected_leads.append(res)
            batch_for_niche.append(res)
            time.sleep(0.3)
            
        # Sync this niche batch cleanly to Google Sheet
        if batch_for_niche:
            print(f"  [SYNC] Ingesting {len(batch_for_niche)} leads to Google Sheet...")
            sync_batch_to_gsheet(batch_for_niche, base_domain=BASE_DOMAIN)
            
    print(f"\n=======================================================")
    print(f"🎯 AUTOMATION COMPLETE: {len(collected_leads)} Leads Ingested & Pitched!")
    print(f"🔗 Google Sheet: https://docs.google.com/spreadsheets/d/{SPREADSHEET_ID}/edit")
    print(f"=======================================================\n")
    return collected_leads

if __name__ == "__main__":
    count = 50
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            count = 50
    hunt_and_append_batch(total_target=count, per_niche=max(5, count // len(TARGET_NICHES)))
