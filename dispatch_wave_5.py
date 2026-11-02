"""
LeadHunter AI - Wave of 5 Dispatches (Excluding Aesthetic Advanced Dental)
Targets 5 verified local Bengaluru businesses:
1. Bellance Luxury Salon (contact@bellancesalon.com)
2. Vurve Salon (contact@vurvesalon.com)
3. Dr. Shilpa Shetty Cosmetic Dental Clinic (drshilpashetty@gmail.com)
4. Aadhya Dental Care (info@aadhyadentalcare.com)
5. Ethicura Dental (ethicuradental@gmail.com)
"""
import os
import sys
import time
import json
import urllib.request
import urllib.error

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from auto_email_dispatcher import build_artisan_email, send_resend_email, PRIMARY_SENDER, REPLY_TO_EMAIL

TARGETS = [
    {
        "name": "Bellance Luxury Salon",
        "email": "contact@bellancesalon.com",
        "city": "Indiranagar, Bengaluru",
        "niche": "Luxury Salons & Spas",
        "domain": "bellancesalon.com",
        "flaws": [
            "Redirecting high-ticket clients to third-party booking apps charging 20-25% commissions",
            "Slow mobile image load latency on smartphone 4G/5G connections",
            "Missing direct 1-tap WhatsApp VIP stylist reservation"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Bellance%20Luxury%20Salon&city=Indiranagar,%20Bengaluru&niche=Luxury%20Salons%20%26%20Spas&domain=bellancesalon.com"
    },
    {
        "name": "Vurve Salon",
        "email": "contact@vurvesalon.com",
        "city": "Indiranagar, Bengaluru",
        "niche": "Luxury Salons & Spas",
        "domain": "vurvesalon.com",
        "flaws": [
            "Third-party booking aggregator friction taking high commissions per client",
            "Heavy unoptimized hero video and images slowing mobile viewport load",
            "Lack of instant 1-tap WhatsApp consultation for bridal and balayage packages"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Vurve%20Salon&city=Indiranagar,%20Bengaluru&niche=Luxury%20Salons%20%26%20Spas&domain=vurvesalon.com"
    },
    {
        "name": "Dr. Shilpa Shetty Cosmetic Dental Clinic",
        "email": "drshilpashetty@gmail.com",
        "city": "Koramangala, Bengaluru",
        "niche": "Dental & Aesthetic Clinics",
        "domain": "cosmeticdentalclinics.in",
        "flaws": [
            "Emergency clinic phone number requires pinch-and-zoom on smaller smartphones",
            "Slow mobile page load latency causing prospective cosmetic patients to bounce",
            "Missing structured 1-tap WhatsApp smile design consultation slot selector"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Dr.%20Shilpa%20Shetty%20Dental%20Clinic&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=cosmeticdentalclinics.in"
    },
    {
        "name": "Aadhya Dental Care",
        "email": "info@aadhyadentalcare.com",
        "city": "Koramangala, Bengaluru",
        "niche": "Dental & Aesthetic Clinics",
        "domain": "aadhyadentalcare.com",
        "flaws": [
            "Outdated mobile navigation menu making treatment options hard to locate",
            "Slow mobile page load speed causing patient drop-off",
            "Missing 1-tap direct WhatsApp doctor appointment booking"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Aadhya%20Dental%20Care&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=aadhyadentalcare.com"
    },
    {
        "name": "Ethicura Dental",
        "email": "ethicuradental@gmail.com",
        "city": "Koramangala, Bengaluru",
        "niche": "Dental & Aesthetic Clinics",
        "domain": "ethicuradental.in",
        "flaws": [
            "Uncompressed clinic images slowing mobile load times on 4G smartphones",
            "No direct 1-tap WhatsApp consultation or doctor appointment booking",
            "Lack of verified patient review gallery and transparent treatment guide"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Ethicura%20Dental&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=ethicuradental.in"
    }
]

def run_dispatch():
    print(f"=== Starting Wave of 5 Dispatches via {PRIMARY_SENDER} ===")
    results = []
    
    for i, t in enumerate(TARGETS, 1):
        print(f"\n[{i}/5] Preparing pitch for {t['name']} ({t['email']})...")
        plain, html = build_artisan_email(
            name=t["name"],
            city=t["city"],
            niche=t["niche"],
            domain=t["domain"],
            flaws=t["flaws"],
            mockup_url=t["mockup_url"]
        )
        
        subject = f"Quick 60s concept preview for {t['name']} ({t['city'].split(',')[0]})"
        
        success, msg_id = send_resend_email(
            to_email=t["email"],
            subject=subject,
            plain_body=plain,
            html_body=html
        )
        
        res = {
            "name": t["name"],
            "email": t["email"],
            "subject": subject,
            "success": success,
            "msg_id": msg_id
        }
        results.append(res)
        
        if success:
            print(f"  [SUCCESS] Dispatched to {t['email']} | Resend ID: {msg_id}")
        else:
            print(f"  [FAILED] {t['email']} | Error: {msg_id}")
            
        time.sleep(2) # 2-second polite pacing
        
    print("\n=== Dispatch Summary ===")
    success_count = sum(1 for r in results if r["success"])
    print(f"Successfully dispatched: {success_count} / {len(TARGETS)}")
    return results

if __name__ == "__main__":
    run_dispatch()
