import sys
import os
import time

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from auto_email_dispatcher import build_artisan_email, build_punchy_email, send_resend_email

TARGET_EMAIL = "rubanvelankanni2003@gmail.com"

TESTS = [
    {
        "style_label": "STYLE 1: Apple Minimalist Designer Note (Dental)",
        "subject": "Quick mobile concept I built for Aesthetic Dental (Koramangala)",
        "func": build_artisan_email,
        "name": "Aesthetic Advanced Dental",
        "city": "Koramangala, Bengaluru",
        "niche": "Dental & Aesthetic Clinics",
        "domain": "aestheticadvanceddental.com",
        "flaws": [
            "Missing direct 1-tap WhatsApp patient consultation & emergency slot button",
            "Hero section lacks verified before/after smile transformation gallery",
            "Slow mobile page load latency causing prospective patients to drop off"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/0?name=Aesthetic%20Advanced%20Dental&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=aestheticadvanceddental.com"
    },
    {
        "style_label": "STYLE 2: Short & Punchy 4-Liner (Salon)",
        "subject": "Quick question regarding Bellance Salon's mobile booking",
        "func": build_punchy_email,
        "name": "Bellance Salon & Spa",
        "city": "Indiranagar, Bengaluru",
        "niche": "Luxury Salons & Spas",
        "domain": "bellancesalon.com",
        "flaws": [
            "Redirecting clients to third-party booking apps that take 20% commission fees"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/1?name=Bellance%20Salon%20%26%20Spa&city=Indiranagar,%20Bengaluru&niche=Luxury%20Salons%20%26%20Spas&domain=bellancesalon.com"
    },
    {
        "style_label": "STYLE 1: Apple Minimalist Designer Note (Interior Architecture)",
        "subject": "Quick mobile layout concept for Studio Morph Architecture",
        "func": build_artisan_email,
        "name": "Studio Morph Architecture",
        "city": "Whitefield, Bengaluru",
        "niche": "Interior Design & Architecture",
        "domain": "studiomorph.in",
        "flaws": [
            "Uncompressed 4K portfolio images taking over 4 seconds to load on mobile",
            "Missing interactive 1-tap WhatsApp 2D/3D floorplan consultation link",
            "No interactive project cost estimate calculator for homeowners"
        ],
        "mockup_url": "https://leads.rvsmps.store/mockup/2?name=Studio%20Morph%20Architecture&city=Whitefield,%20Bengaluru&niche=Interior%20Design%20%26%20Architecture&domain=studiomorph.in"
    }
]

def main():
    print("=" * 65)
    print("[*] Dispatching Human Artisan Email Samples...")
    print(f"[*] Target: {TARGET_EMAIL}")
    print(f"[*] Sender: Ruban Velankanni | Ruban Designs <ruban@rvsmps.store>")
    print("=" * 65)
    
    for idx, t in enumerate(TESTS, 1):
        plain_body, html_body = t["func"](
            name=t["name"],
            city=t["city"],
            niche=t["niche"],
            domain=t["domain"],
            flaws=t["flaws"],
            mockup_url=t["mockup_url"]
        )
        
        print(f"\n[{idx}/3] Sending: {t['style_label']}")
        print(f"  Subject: {t['subject']}")
        
        ok, res_id = send_resend_email(TARGET_EMAIL, t["subject"], plain_body, html_body)
        if ok:
            print(f"  [+] SUCCESS! Resend ID: {res_id}")
        else:
            print(f"  [-] FAILED: {res_id}")
            
        time.sleep(1.5)
        
    print("\n" + "=" * 65)
    print("[*] All tests dispatched successfully!")

if __name__ == "__main__":
    main()
