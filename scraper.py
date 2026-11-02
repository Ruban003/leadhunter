"""
Lead Hunter Agent - Scraper Module
Searches for genuine US local businesses across high-ticket niches and cities.
Excludes aggregators (Yelp, Angi, etc.) and gathers direct business domains.
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
    'tripadvisor.in', 'tripadvisor.com', 'bodycraft.co.in', 'bodycraft.com'
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

def search_leads(niche: str, city: str, limit: int = 10) -> list:
    """
    Search DuckDuckGo Lite for direct business websites in a specific US city and niche.
    Returns list of dicts: {'name': ..., 'url': ..., 'domain': ..., 'niche': ..., 'city': ...}
    """
    query = f"{niche} in {city}"
    leads = []
    seen_domains = set()
    
    # We query up to 2 pages if needed
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
                
                # Clean up business name from title
                # E.g. "Austin Roofing and Construction - Best Roofers in Austin" -> "Austin Roofing and Construction"
                clean_name = re.split(r'[-–|•:]', title)[0].strip()
                if not clean_name or len(clean_name) < 3:
                    clean_name = domain.split('.')[0].replace('-', ' ').title()
                    
                snippet_text = snippets[idx].get_text(strip=True) if idx < len(snippets) else ""
                
                leads.append({
                    'name': clean_name,
                    'url': clean_href,
                    'domain': domain,
                    'snippet': snippet_text,
                    'niche': niche,
                    'city': city
                })
                
            time.sleep(1) # respectful pause
        except Exception as e:
            print(f"Scraper error: {e}")
            break
            
    return leads

if __name__ == "__main__":
    test_results = search_leads("Roofing", "Austin TX", limit=5)
    print(f"Found {len(test_results)} leads:")
    for l in test_results:
        print(f" - {l['name']} ({l['domain']}) -> {l['url']}")
