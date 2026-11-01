import http.server
import json
import urllib.parse
import urllib.request
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
            lead = {}
            if 0 <= idx < len(CURRENT_LEADS):
                lead = dict(CURRENT_LEADS[idx])
            else:
                # Support query fallback
                if params.get('name'):
                    lead['name'] = params.get('name')[0]
                if params.get('city'):
                    lead['city'] = params.get('city')[0]
                if params.get('niche'):
                    lead['niche'] = params.get('niche')[0]
                if params.get('domain'):
                    lead['domain'] = params.get('domain')[0]
                if params.get('phone'):
                    lead['phone'] = params.get('phone')[0]
                if params.get('email'):
                    lead['emails'] = [params.get('email')[0]]
                if not lead.get('name'):
                    lead = {'name': 'Business Team', 'city': 'Bangalore, Karnataka', 'niche': 'Luxury Salons & Spas', 'domain': 'business.com'}

            pitch = generate_pitch(lead, mockup_url)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(pitch).encode('utf-8'))
            return

        elif parsed.path.startswith('/mockup/'):
            try:
                idx_str = parsed.path.split('/')[-1]
                idx = int(idx_str) if idx_str.isdigit() else 0
                lead = {}
                if 0 <= idx < len(CURRENT_LEADS):
                    lead = dict(CURRENT_LEADS[idx])
                
                # Query param fallback / overrides
                if params.get('name'):
                    lead['name'] = params.get('name')[0]
                if params.get('city'):
                    lead['city'] = params.get('city')[0]
                if params.get('niche'):
                    lead['niche'] = params.get('niche')[0]
                if params.get('domain'):
                    lead['domain'] = params.get('domain')[0]
                if params.get('phone'):
                    lead['phone'] = params.get('phone')[0]

                if not lead.get('name'):
                    lead = {'name': 'Luxe Hair & Spa Studio', 'city': 'Bangalore, Karnataka', 'niche': 'Luxury Salons & Spas', 'phone': '+91 80986 71563'}

                mockup_html = generate_mockup_html(lead)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(mockup_html.encode('utf-8'))
                return
            except Exception as e:
                lead = {'name': 'Luxe Hair & Spa Studio', 'city': 'Bangalore, Karnataka', 'niche': 'Luxury Salons & Spas', 'phone': '+91 80986 71563'}
                mockup_html = generate_mockup_html(lead)
                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(mockup_html.encode('utf-8'))
                return

        elif parsed.path == '/api/export':
            output = io.StringIO()
            writer = csv.writer(output)
            writer.writerow([
                'Timestamp',
                'Status',
                'Business Name',
                'City',
                'Niche',
                'Website',
                'Domain',
                'Audit Grade',
                'Audit Score',
                'Phone / WhatsApp',
                'Email',
                'Flaws Detected',
                'Custom Mockup Preview URL',
                'Cold Email Subject',
                'Cold Email Body',
                'WhatsApp Pitch Message',
                'WhatsApp 1-Click Link',
                'Gmail 1-Click Link',
                'Offer Price'
            ])
            
            host_header = self.headers.get('Host', 'leads.rvsmps.store')
            base_url = f"https://{host_header}"
            
            for idx, l in enumerate(CURRENT_LEADS):
                name = l.get('name', '')
                city = l.get('city', '')
                niche = l.get('niche', '')
                domain = l.get('domain', '')
                phone = l.get('phone', '')
                emails = l.get('emails', [])
                email = emails[0] if emails else f"contact@{domain}"
                
                mockup_url = f"{base_url}/mockup/{idx}?name={urllib.parse.quote(name)}&city={urllib.parse.quote(city)}&niche={urllib.parse.quote(niche)}&domain={urllib.parse.quote(domain)}&phone={urllib.parse.quote(phone)}"
                pitch = generate_pitch(l, mockup_url)
                
                writer.writerow([
                    l.get('scanned_at', '2026-11-01'),
                    'New Lead',
                    name,
                    city,
                    niche,
                    l.get('url', ''),
                    domain,
                    l.get('grade', 'C'),
                    f"{l.get('score', 60)}%",
                    phone,
                    email,
                    " | ".join(l.get('flaws', [])),
                    mockup_url,
                    pitch.get('subject', ''),
                    pitch.get('body', ''),
                    pitch.get('whatsapp_body', ''),
                    pitch.get('whatsapp_url', ''),
                    pitch.get('gmail_url', ''),
                    '₹2,999 Starter'
                ])
            csv_data = output.getvalue()
            self.send_response(200)
            self.send_header('Content-Type', 'text/csv; charset=utf-8')
            self.send_header('Content-Disposition', 'attachment; filename="leadhunter_pipeline_leads.csv"')
            self.end_headers()
            self.wfile.write(csv_data.encode('utf-8'))
            return

        elif parsed.path == '/api/sync-sheet':
            # Accepts POST or GET with webhook URL to push all leads to Google Sheets
            webhook_url = params.get('webhook_url', [''])[0]
            if not webhook_url:
                webhook_url = os.environ.get('GSHEET_WEBHOOK_URL', '')
                
            host_header = self.headers.get('Host', 'leads.rvsmps.store')
            base_url = f"https://{host_header}"
            
            payload_leads = []
            for idx, l in enumerate(CURRENT_LEADS):
                name = l.get('name', '')
                city = l.get('city', '')
                niche = l.get('niche', '')
                domain = l.get('domain', '')
                phone = l.get('phone', '')
                emails = l.get('emails', [])
                email = emails[0] if emails else f"contact@{domain}"
                
                mockup_url = f"{base_url}/mockup/{idx}?name={urllib.parse.quote(name)}&city={urllib.parse.quote(city)}&niche={urllib.parse.quote(niche)}&domain={urllib.parse.quote(domain)}&phone={urllib.parse.quote(phone)}"
                pitch = generate_pitch(l, mockup_url)
                
                payload_leads.append({
                    'timestamp': '2026-11-01',
                    'status': 'New Lead',
                    'name': name,
                    'city': city,
                    'niche': niche,
                    'url': l.get('url', ''),
                    'grade': l.get('grade', 'C'),
                    'score': l.get('score', 60),
                    'phone': phone,
                    'email': email,
                    'flaws': " | ".join(l.get('flaws', [])),
                    'mockup_url': mockup_url,
                    'pitch_subject': pitch.get('subject', ''),
                    'pitch_body': pitch.get('body', ''),
                    'whatsapp_body': pitch.get('whatsapp_body', ''),
                    'whatsapp_url': pitch.get('whatsapp_url', ''),
                    'gmail_url': pitch.get('gmail_url', ''),
                    'notes': '₹2,999 Starter'
                })
                
            if webhook_url and payload_leads:
                try:
                    req = urllib.request.Request(
                        webhook_url,
                        data=json.dumps({'leads': payload_leads}).encode('utf-8'),
                        headers={'Content-Type': 'application/json'},
                        method='POST'
                    )
                    with urllib.request.urlopen(req, timeout=10) as resp:
                        resp_data = resp.read().decode('utf-8')
                        self.send_response(200)
                        self.send_header('Content-Type', 'application/json')
                        self.end_headers()
                        self.wfile.write(json.dumps({'status': 'synced', 'count': len(payload_leads), 'response': resp_data}).encode('utf-8'))
                        return
                except Exception as e:
                    self.send_response(500)
                    self.send_header('Content-Type', 'application/json')
                    self.end_headers()
                    self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))
                    return
            else:
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'ready', 'leads': payload_leads, 'spreadsheet_id': '1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA'}).encode('utf-8'))
                return

        self.send_response(404)
        self.end_headers()
