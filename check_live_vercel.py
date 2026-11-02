import urllib.request
import time

time.sleep(12)
url = "https://leads.rvsmps.store/mockup/0?name=Aesthetic%20Advanced%20Dental&city=Koramangala,%20Bengaluru&niche=Dental%20%26%20Aesthetic%20Clinics&domain=aestheticadvanceddental.com"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8")
        print("HTTP Status:", resp.status)
        print("Has Dental Headline:", "World-Class Dentistry" in html)
        print("Has Implants:", "Dental Implants" in html)
        print("Has Balayage (Should be False):", "Balayage" in html)
        print("Has Light Theme Default:", 'data-theme="light"' in html)
        print("Has Theme Toggle:", "btn-theme-toggle" in html)
except Exception as e:
    print("Fetch error:", e)
