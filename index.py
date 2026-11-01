import http.server
import json
import urllib.parse
import os
import csv
import io
import urllib3

from scraper import search_leads
from auditor import audit_lead
from pitch_generator import generate_pitch
from mockup_preview import generate_mockup_html

urllib3.disable_warnings()

# Cache leads across warm serverless requests
CURRENT_LEADS = []

# Embed the Dashboard HTML
dashboard_path = os.path.join(os.path.dirname(__file__), 'dashboard.html')
if os.path.exists(dashboard_path):
    with open(dashboard_path, 'r', encoding='utf-8') as f:
        HTML_PAGE = f.read()
else:
    HTML_PAGE = "<h1>LeadHunter AI</h1>"

# Embed the Portfolio HTML
portfolio_path = os.path.join(os.path.dirname(__file__), 'portfolio.html')
if os.path.exists(portfolio_path):
    with open(portfolio_path, 'r', encoding='utf-8') as f:
        PORTFOLIO_PAGE = f.read()
else:
    PORTFOLIO_PAGE = "<h1>Ruban Designs Portfolio</h1>"

class handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        global CURRENT_LEADS
        parsed = urllib.parse.urlparse(self.path)
        params = urllib.parse.parse_qs(parsed.query)

        if parsed.path == '/' or parsed.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_PAGE.encode('utf-8'))
            return

        elif parsed.path == '/portfolio':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(PORTFOLIO_PAGE.encode('utf-8'))
            return

        elif parsed.path == '/api/hunt':
            niche = params.get('niche', ['Roofing Contractors'])[0]
            city = params.get('city', ['Austin, TX'])[0]
            limit = int(params.get('limit', [5])[0])

            raw_leads = search_leads(niche, city, limit=limit)
            audited = []
            for l in raw_leads:
                res = audit_lead(l)
                audited.append(res)

            CURRENT_LEADS = audited
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'leads': CURRENT_LEADS}).encode('utf-8'))
            return

        elif parsed.path == '/api/pitch':
            idx = int(params.get('idx', [0])[0])
            mockup_url = params.get('mockup_url', [''])[0]
            if 0 <= idx < len(CURRENT_LEADS):
                lead = CURRENT_LEADS[idx]
                pitch = generate_pitch(lead, mockup_url)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps(pitch).encode('utf-8'))
                return
            else:
                self.send_response(404)
                self.end_headers()
                return

        elif parsed.path.startswith('/mockup/'):
            try:
                idx = int(parsed.path.split('/')[-1])
                if 0 <= idx < len(CURRENT_LEADS):
                    lead = CURRENT_LEADS[idx]
                    mockup_html = generate_mockup_html(lead)
                    self.send_response(200)
                    self.send_header('Content-Type', 'text/html; charset=utf-8')
                    self.end_headers()
                    self.wfile.write(mockup_html.encode('utf-8'))
                    return
            except Exception:
                pass
            self.send_response(404)
            self.end_headers()
            return

        elif parsed.path == '/api/export':
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow(['Business Name', 'Website', 'Domain', 'City', 'Niche', 'Grade', 'Score', 'Load Time (s)', 'Has SSL', 'Mobile Ready', 'Copyright Year', 'Emails', 'Phone', 'Flaws Detected'])
            for l in CURRENT_LEADS:
                writer.writerow([
                    l.get('name', ''),
                    l.get('url', ''),
                    l.get('domain', ''),
                    l.get('city', ''),
                    l.get('niche', ''),
                    l.get('grade', ''),
                    l.get('score', ''),
                    l.get('load_time', ''),
                    l.get('has_ssl', ''),
                    l.get('is_mobile_ready', ''),
                    l.get('copyright_year', ''),
                    "; ".join(l.get('emails', [])),
                    l.get('phone', ''),
                    " | ".join(l.get('flaws', []))
                ])
            csv_data = output.getvalue()
            self.send_response(200)
            self.send_header('Content-Type', 'text/csv')
            self.send_header('Content-Disposition', 'attachment; filename="leadhunter_us_leads.csv"')
            self.end_headers()
            self.wfile.write(csv_data.encode('utf-8'))
            return

        self.send_response(404)
        self.end_headers()
