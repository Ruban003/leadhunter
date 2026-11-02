import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from mockup_preview import generate_mockup_html

lead = {
    'name': 'Aesthetic Advanced Dental',
    'city': 'Koramangala, Bengaluru',
    'niche': 'Dental & Aesthetic Clinics',
    'domain': 'aestheticadvanceddental.com',
    'phone': '+91 86603 51505'
}

html = generate_mockup_html(lead)

print("Has Dental Headline:", "World-Class Dentistry" in html)
print("Has Dental Implants:", "Dental Implants" in html)
print("Has Clear Aligners:", "Clear Aligners" in html)
print("Has Hair Balayage (Should be FALSE):", "Balayage" in html)
print("Has Light Theme Default:", 'data-theme="light"' in html)
print("Has Theme Toggle Button:", "btn-theme-toggle" in html)
