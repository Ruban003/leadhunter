"""
Lead Hunter Agent - Scraper Module
Searches for genuine Bangalore / Indian local businesses across high-ticket niches.
Excludes aggregators, directories, and day-job domains (Bodycraft).
Extracts clean, genuine brand names.
"""

import urllib.parse
import requests
import re
from bs4 import BeautifulSoup
import time

AGGREGATORS = [
    'duckduckgo.com', 'google.com', 'bing.com', 'yahoo.com',
    'yelp.com', 'angi.com', 'yellowpages.com', 'bbb.org', 'expertise.com',
    'threebestrated.com', 'homeguide.com', 'thumbtack.com', 'houzz.com',
    'facebook.com', 'instagram.com', 'linkedin.com', 'twitter.com',
    'forbes.com', 'mapquest.com', 'superpages.com', 'zoominfo.com',
    'usnews.com', 'healthgrades.com', 'zocdoc.com',
    # Indian Aggregators, Directories & Excluded Domains
    'justdial.com', 'sulekha.com', 'indiamart.com', 'tradeindia.com',
    'practo.com', 'urbancompany.com', 'fresha.com', 'wedmegood.com',
    'weddingwire.in', 'magicbricks.com', '99acres.com', 'quikr.com', 'olx.in',
    'tripadvisor.in', 'tripadvisor.com', 'hexahealth.com', 'lybrate.com', 'credihealth.com',
    'bodycraft.co.in', 'bodycraft.com'
]

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

def clean_url(url: str) -> str:
    """Strip tracking and get clean root/target URL."""
    if 'duckduckgo.com/l/?uddg=' in url or 'uddg=' in url:
        m = re.search(r'uddg=([^&]+)', url)
        if m:
            url = urllib.parse.unquote(m.group(1))
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme in ('http', 'https') and parsed.netloc:
        return f"{parsed.scheme}://{parsed.netloc}"
    return url

def is_aggregator(domain: str) -> bool:
    dom = domain.lower()
    return any(agg in dom for agg in AGGREGATORS)

def clean_brand_name(raw_title: str, domain: str) -> str:
    """
    Extracts the actual brand name rather than SEO keyword strings.
    E.g. 'Dentist in Koramangala & Harlur Road - Aesthetic Advanced Dental' -> 'Aesthetic Advanced Dental'
    """
    # 1. Clean domain fallback stem
    domain_stem = domain.split('.')[0].replace('-', ' ').replace('_', ' ')
    # Capitalize standard domain name (e.g. 'aadhyadentalcare' -> 'Aadhya Dental Care')
    # Use word boundary replacements for common suffixes
    domain_brand = domain_stem
    for word in ['dental', 'clinic', 'salon', 'spa', 'studio', 'care', 'couture', 'interiors', 'design', 'cafe']:
        domain_brand = re.sub(rf'\b{word}\b', f' {word.capitalize()}', domain_brand, flags=re.IGNORECASE)
    domain_brand = " ".join([w.capitalize() for w in domain_brand.split()])
    
    if not raw_title:
        return domain_brand

    # Split title on separators
    parts = [p.strip() for p in re.split(r'[-–|•:]', raw_title) if p.strip()]
    if not parts:
        return domain_brand

    # Filter out parts that are clearly SEO keyword spam
    seo_keywords = ['best', 'top', 'near me', 'in bangalore', 'in bengaluru', 'in koramangala', 'in indiranagar', 'in hsr', 'dentist in', 'salon in', 'clinic in', 'reviews', 'ratings']
    good_candidates = []
    for p in parts:
        p_lower = p.lower()
        if not any(k in p_lower for k in seo_keywords) and len(p) >= 3 and len(p) <= 40:
            good_candidates.append(p)
            
    if good_candidates:
        # Prefer candidate that matches domain words
        for c in good_candidates:
            if any(w in domain.lower() for w in c.lower().split() if len(w) > 3):
                return c
        return good_candidates[0]
        
    return domain_brand

def search_leads(niche: str, city: str, limit: int = 10) -> list:
    """
    Search DuckDuckGo Lite for direct business websites in a specific city and niche.
    Returns list of dicts: {'name': ..., 'url': ..., 'domain': ..., 'niche': ..., 'city': ...}
    """
    query = f"{niche} in {city}"
    leads = []
    seen_domains = set()
    
    for page_idx in range(2):
        if len(leads) >= limit:
            break
            
        data = {'q': query}
        if page_idx > 0:
            data['s'] = str(page_idx * 30)
            
        try:
            r = requests.post('https://lite.duckduckgo.com/lite/', data=data, headers=HEADERS, timeout=12)
            if r.status_code != 200:
                break
                
            soup = BeautifulSoup(r.text, 'html.parser')
            links = soup.select('.result-link')
            snippets = soup.select('.result-snippet')
            
            for idx, a_tag in enumerate(links):
                if len(leads) >= limit:
                    break
                    
                raw_href = a_tag.get('href', '')
                title = a_tag.get_text(strip=True)
                clean_href = clean_url(raw_href)
                
                parsed = urllib.parse.urlparse(clean_href)
                domain = parsed.netloc.lower().replace('www.', '')
                
                if not domain or is_aggregator(domain) or domain in seen_domains:
                    continue
                    
                seen_domains.add(domain)
                clean_name = clean_brand_name(title, domain)
                snippet_text = snippets[idx].get_text(strip=True) if idx < len(snippets) else ""
                
                leads.append({
                    'name': clean_name,
                    'url': clean_href,
                    'domain': domain,
                    'snippet': snippet_text,
                    'niche': niche,
                    'city': city
                })
                
            time.sleep(1)
        except Exception as e:
            print(f"Scraper error: {e}")
            break
            
    return leads
