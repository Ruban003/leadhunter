"""
LeadHunter AI - Master Agency Flywheel Orchestrator
Command center for the 50-pitch/day client acquisition flywheel.
"""
import sys
import os
import argparse
import subprocess

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from batch_lead_pipeline import hunt_and_append_batch
from auto_email_dispatcher import run_email_dispatcher
from whatsapp_sniper_hub import run_whatsapp_sniper

SPREADSHEET_URL = "https://docs.google.com/spreadsheets/d/1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA/edit"

def main():
    parser = argparse.ArgumentParser(description="LeadHunter Agency Flywheel (50 Pitches/Day)")
    parser.add_argument("--hunt", type=int, default=0, help="Number of fresh Bangalore leads to hunt and ingest into Google Sheet (e.g. 50)")
    parser.add_argument("--email", type=int, default=0, help="Number of cold emails to dispatch via drip engine (e.g. 30)")
    parser.add_argument("--dry-run", action="store_true", help="Simulate email sending without actually firing SMTP")
    parser.add_argument("--whatsapp", type=int, default=0, help="Launch WhatsApp Sniper Cockpit for N top leads (e.g. 15)")
    parser.add_argument("--all", action="store_true", help="Run full 50-pitch flywheel (Hunt 50 + Email 30 + WhatsApp 15)")

    args = parser.parse_args()

    print("\n" + "="*60)
    print("🏴‍☠️ RUBAN DESIGNS - LEAD ACQUISITION & OUTREACH ENGINE")
    print("="*60)
    print(f"📊 Google Sheet Pipeline: {SPREADSHEET_URL}")
    print("="*60 + "\n")

    live_email_mode = not args.dry_run

    if args.all:
        print("⚡ EXECUTING FULL DAILY FLYWHEEL (50-PITCH SYSTEM)...")
        # Step 1: Hunt 50 Leads
        hunt_and_append_batch(total_target=50, per_niche=10)
        # Step 2: Drip Email 30 Leads
        run_email_dispatcher(limit=30, interval_sec=120, live=live_email_mode)
        # Step 3: WhatsApp Sniper 15 Leads
        run_whatsapp_sniper(target_count=15)
        return

    executed_something = False

    if args.hunt > 0:
        executed_something = True
        hunt_and_append_batch(total_target=args.hunt, per_niche=max(2, args.hunt // 5))

    if args.email > 0:
        executed_something = True
        run_email_dispatcher(limit=args.email, interval_sec=120, live=live_email_mode)

    if args.whatsapp > 0:
        executed_something = True
        run_whatsapp_sniper(target_count=args.whatsapp)

    if not executed_something:
        print("Usage Examples:")
        print("  1. Hunt 50 fresh Bangalore leads into Google Sheet:")
        print("     python run_agency_flywheel.py --hunt 50\n")
        print("  2. Send cold emails to leads in Google Sheet (live SMTP):")
        print("     python run_agency_flywheel.py --email 30\n")
        print("  3. Launch WhatsApp Sniper Cockpit (15 top targets):")
        print("     python run_agency_flywheel.py --whatsapp 15\n")
        print("  4. Run Full Daily Machine (Hunt + Email + WhatsApp):")
        print("     python run_agency_flywheel.py --all\n")

if __name__ == "__main__":
    main()
