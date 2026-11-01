"""
Lead Hunter Agent - Auditor & Contact Extractor Module
Inspects business websites for mobile responsiveness, load speed, security,
outdated copyright, and conversion bottlenecks. Extracts emails and phone numbers.
"""

import requests
import re
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def clean_email(email: str) -> bool:
    email = email.lower()
    junk_ends = ('.png', '.jpg', '.jpeg', '.svg', '.webp', '.js', '.css', '.woff', '.ttf')
    junk_words = ['sentry', 'example', 'wixpress', 'schema.org', 'wordpress', 'cloudflare', 'domain.com']
    if email.endswith(junk_ends) or any(w in email for w in junk_words):
        return False
    return True

def audit_lead(lead: dict) -> dict:
    """
    Audits a single lead website.
    Returns enriched dict with audit score, grade, flaws, emails, phone, and social links.
    """
    url = lead.get('url', '')
    domain = lead.get('domain', '')
    
    result = dict(lead)
    result.update({
        'status': 'scanned',
        'score': 100,
        'grade': 'A',
        'load_time': 0.0,
        'has_ssl': False,
        'is_mobile_ready': True,
        'copyright_year': 'Unknown',
        'is_outdated': False,
        'flaws': [],
        'emails': [],
        'phone': '',
        'social_links': {},
        'title': lead.get('name', '')
    })
    
    if not url:
        result['status'] = 'no_url'
        result['score'] = 0
        result['grade'] = 'F'
        result['flaws'].append("No website URL provided")
        return result

    start_t = time.time()
    try:
        r = requests.get(url, headers=HEADERS, timeout=12, verify=False)
        load_time = round(time.time() - start_t, 2)
        result['load_time'] = load_time
        result['has_ssl'] = r.url.startswith("https://")
        
        soup = BeautifulSoup(r.text, 'html.parser')
        if soup.title and soup.title.string:
            result['title'] = soup.title.string.strip()
            
        # 1. Check Mobile Responsiveness
        viewport = soup.find('meta', attrs={'name': lambda x: x and x.lower() == 'viewport'})
        if not viewport or 'width=device-width' not in viewport.get('content', '').lower():
            result['is_mobile_ready'] = False
            result['score'] -= 30
            result['flaws'].append("Not optimized for mobile screens (missing responsive viewport tag)")
            
        # 2. Check Load Time
        if load_time > 3.5:
            result['score'] -= 20
            result['flaws'].append(f"Slow load speed ({load_time}s) — drives away mobile customers")
        elif load_time > 2.0:
            result['score'] -= 10
            result['flaws'].append(f"Moderate load latency ({load_time}s)")
            
        # 3. Check SSL
        if not result['has_ssl']:
            result['score'] -= 25
            result['flaws'].append("Missing SSL / HTTPS security (Google marks site as 'Not Secure')")
            
        # 4. Check Copyright Year
        text_content = soup.get_text()
        copyright_matches = re.findall(r'(?:©|copyright|\(c\))\s*(?:20\d\d[-–])?\s*(20\d\d)', text_content, re.IGNORECASE)
        if copyright_matches:
            c_year = copyright_matches[-1]
            result['copyright_year'] = c_year
            if c_year.isdigit() and int(c_year) < 2025:
                result['is_outdated'] = True
                result['score'] -= 15
                result['flaws'].append(f"Outdated copyright notice (© {c_year}) makes the business look inactive")
                
        # 5. Check Call To Action (CTA)
        cta_keywords = ['call', 'quote', 'contact', 'book', 'schedule', 'estimate', 'consultation', 'get started']
        buttons = soup.find_all(['button', 'a'])
        cta_count = sum(1 for b in buttons if any(k in b.get_text(strip=True).lower() for k in cta_keywords))
        has_tel_link = any(a.get('href', '').startswith('tel:') for a in soup.find_all('a', href=True))
        
        if cta_count < 2 or not has_tel_link:
            result['score'] -= 10
            result['flaws'].append("Weak conversion flow: Missing prominent 'Call Now' or 'Instant Estimate' buttons")
            
        # 6. Extract Emails
        all_emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', r.text))
        valid_emails = [e for e in all_emails if clean_email(e)]
        
        # Prioritize domain emails
        domain_emails = [e for e in valid_emails if domain in e]
        other_emails = [e for e in valid_emails if domain not in e]
        result['emails'] = domain_emails + other_emails
        
        # 7. Extract Phone Numbers & WhatsApp (Support India +91, Landline, US, and direct tel: links)
        # Check tel: links first
        for a in soup.find_all('a', href=True):
            href = a['href']
            if href.startswith('tel:'):
                tel_num = href.replace('tel:', '').strip()
                if tel_num and len(re.sub(r'\D', '', tel_num)) >= 10:
                    result['phone'] = tel_num
                    break
            elif 'wa.me/' in href or 'api.whatsapp.com/send' in href:
                wa_match = re.search(r'(?:wa\.me/|phone=)(\+?\d+)', href)
                if wa_match:
                    result['phone'] = wa_match.group(1)
                    break

        if not result['phone']:
            # Indian Mobile Numbers: +91 98xxx xxxxx, 98xxx xxxxx, 098xxx xxxxx
            in_phones = re.findall(r'(?:(?:\+91|0)[\s.-]?)?([6-9]\d{4}[\s.-]?\d{5})', text_content)
            if in_phones:
                clean_in = re.sub(r'\D', '', in_phones[0])
                if len(clean_in) == 10:
                    result['phone'] = f"+91 {clean_in[:5]} {clean_in[5:]}"
                else:
                    result['phone'] = in_phones[0]
            else:
                # Bangalore / Indian Landline: 080-xxxxxxxx
                landlines = re.findall(r'080[\s.-]?\d{7,8}', text_content)
                if landlines:
                    result['phone'] = landlines[0]
                else:
                    # US Phone Numbers
                    us_phones = re.findall(r'(?:\+?1[-. ]?)?\(?([2-9][0-9]{2})\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})', text_content)
                    if us_phones:
                        p = us_phones[0]
                        result['phone'] = f"({p[0]}) {p[1]}-{p[2]}"
            
        # 8. Extract Social Media Links
        for a in soup.find_all('a', href=True):
            href = a['href']
            for platform in ['facebook', 'instagram', 'linkedin', 'twitter', 'yelp']:
                if platform in href and platform not in result['social_links']:
                    result['social_links'][platform] = href
                    
        # Check /contact or /about page if no email was found on home
        if not result['emails']:
            contact_links = [a['href'] for a in soup.find_all('a', href=True) if any(x in a['href'].lower() for x in ['contact', 'about'])]
            if contact_links:
                sub_url = urljoin(url, contact_links[0])
                try:
                    sub_r = requests.get(sub_url, headers=HEADERS, timeout=8, verify=False)
                    sub_emails = set(re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', sub_r.text))
                    sub_valid = [e for e in sub_emails if clean_email(e)]
                    if sub_valid:
                        result['emails'] = sub_valid
                except Exception:
                    pass

    except Exception as e:
        result['status'] = f"scan_error: {str(e)[:40]}"
        result['score'] = 40
        result['flaws'].append("Website took too long to respond or failed connection")
        
    # Cap score
    result['score'] = max(10, min(100, result['score']))
    s = result['score']
    result['grade'] = "A" if s >= 90 else "B" if s >= 75 else "C" if s >= 60 else "D" if s >= 45 else "F"
    
    return result

if __name__ == "__main__":
    import urllib3
    urllib3.disable_warnings()
    test_lead = {'name': 'Kingfisher Roofing', 'url': 'https://kingfisher-roofing.com', 'domain': 'kingfisher-roofing.com'}
    res = audit_lead(test_lead)
    print("Grade:", res['grade'], "Score:", res['score'], "Emails:", res['emails'], "Flaws:", res['flaws'])
