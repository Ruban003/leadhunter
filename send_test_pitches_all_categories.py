import sys
import os
import time
import json
import urllib.request
import urllib.error

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from auto_email_dispatcher import build_professional_email, send_resend_email

TARGET_EMAIL = "rubanvelankanni2003@gmail.com"

CATEGORIES = [
    {
        "cat_id": "DENTAL",
        "name": "Aesthetic Advanced Dental",
        "city": "Koramangala, Bengaluru",
        "niche": "Dental & Aesthetic Clinics",
        "domain": "aestheticadvanceddental.com",
        "flaws": [
            "Missing 1-tap WhatsApp patient consultation & emergency slot button",
            "Hero section lacks verified before/after smile transformation gallery",
            "Mobile page load latency (3.1s) causing prospective patients to drop off"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Aesthetic%20Advanced%20Dental&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=aestheticadvanceddental.com",
        "subject_tag": "DENTAL CLINIC"
    },
    {
        "cat_id": "SALON",
        "name": "Bellance Salon & Spa",
        "city": "Indiranagar, Bengaluru",
        "niche": "Luxury Salons & Spas",
        "domain": "bellancesalon.com",
        "flaws": [
            "Missing direct stylist selection & instant mobile time-slot booking",
            "Redirects clients to third-party aggregators charging 20% booking fees",
            "Heavy mobile hero banner causes 2.4s initial layout shift on smartphones"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/1?name=Bellance%20Salon%20%26%20Spa&city=Indiranagar,%20Bengaluru&niche=Luxury%20Salons%20%26%20Spas&domain=bellancesalon.com",
        "subject_tag": "LUXURY SALON"
    },
    {
        "cat_id": "ARCHITECTURE",
        "name": "Studio Morph Architecture",
        "city": "Whitefield, Bengaluru",
        "niche": "Interior Design & Architecture",
        "domain": "studiomorph.in",
        "flaws": [
            "Uncompressed 4K portfolio images taking over 4 seconds to load on mobile",
            "Missing interactive 1-tap WhatsApp 2D/3D floorplan consultation link",
            "No interactive project cost & sq.ft estimate calculator for homeowners"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/2?name=Studio%20Morph%20Architecture&city=Whitefield,%20Bengaluru&niche=Interior%20Design%20%26%20Architecture&domain=studiomorph.in",
        "subject_tag": "INTERIOR ARCHITECTURE"
    },
    {
        "cat_id": "BRIDAL",
        "name": "Aara Bridal Couture",
        "city": "Jayanagar, Bengaluru",
        "niche": "Bridal & Haute Couture",
        "domain": "aaracouture.in",
        "flaws": [
            "Missing private VIP bridal trial fitting scheduler on smartphone screens",
            "No instant WhatsApp concierge button for custom lehenga/sherwani inquiry",
            "Lookbook lacks quick tap-to-zoom for handcrafted zardozi embroidery details"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/3?name=Aara%20Bridal%20Couture&city=Jayanagar,%20Bengaluru&niche=Bridal%20%26%20Haute%20Couture&domain=aaracouture.in",
        "subject_tag": "BRIDAL COUTURE"
    },
    {
        "cat_id": "CAFE",
        "name": "Lavelle Artisanal Bistro",
        "city": "Lavelle Road, Bengaluru",
        "niche": "Artisanal Cafes & Dining",
        "domain": "lavellebistro.in",
        "flaws": [
            "Menu requires downloading a clunky 15MB PDF instead of mobile web viewing",
            "Missing instant 1-tap weekend table reservation via direct WhatsApp",
            "No visual food gallery or allergen highlights for signature dishes"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/4?name=Lavelle%20Artisanal%20Bistro&city=Lavelle%20Road,%20Bengaluru&niche=Artisanal%20Cafes%20%26%20Dining&domain=lavellebistro.in",
        "subject_tag": "ARTISANAL CAFE"
    }
]

def main():
    print(f"[*] Starting dispatch of sample pitches for all {len(CATEGORIES)} categories...")
    print(f"[*] Recipient: {TARGET_EMAIL}")
    print(f"[*] Sender: Ruban Velankanni | Ruban Designs <ruban@rvsmps.store>")
    print("=" * 65)
    
    results = []
    
    for idx, cat in enumerate(CATEGORIES, 1):
        subject = f"[{cat['subject_tag']}] Quick visual upgrade concept for {cat['name']} ({cat['city'].split(',')[0]})"
        plain_body, html_body = build_professional_email(
            name=cat['name'],
            city=cat['city'],
            niche=cat['niche'],
            domain=cat['domain'],
            flaws=cat['flaws'],
            mockup_url=cat['mockup_url']
        )
        
        print(f"\n[{idx}/{len(CATEGORIES)}] Dispatching {cat['subject_tag']} pitch...")
        print(f"  Business: {cat['name']} ({cat['domain']})")
        print(f"  Subject:  {subject}")
        
        ok, res_id = send_resend_email(TARGET_EMAIL, subject, plain_body, html_body)
        if ok:
            results.append({"category": cat['cat_id'], "subject": subject, "id": res_id, "status": "sent"})
            print(f"  [+] Success! Resend ID: {res_id}")
        else:
            results.append({"category": cat['cat_id'], "subject": subject, "error": res_id, "status": "failed"})
            print(f"  [-] Failed: {res_id}")
            
        time.sleep(1.5)  # respectful pacing
        
    print("\n" + "=" * 65)
    print(f"[*] All {len(results)} category test pitches dispatched to {TARGET_EMAIL}!")
    for r in results:
        print(f"  - {r['category']}: {r.get('id', r.get('error'))} ({r['status']})")

if __name__ == "__main__":
    main()
