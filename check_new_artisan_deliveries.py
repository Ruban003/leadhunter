import urllib.request
import json

ids = [
    ('Sample 1 (Dental - Style 1)', '01a19b95-5fd2-7b18-80d9-01d8322285b7'),
    ('Sample 2 (Salon - Style 2)', '01a19b95-6957-745e-8056-8b5bbcadc21b'),
    ('Sample 3 (Architecture - Style 1)', '01a19b95-70a6-74b5-a151-84ed17bb86c6'),
]

for label, email_id in ids:
    req = urllib.request.Request(
        f'https://api.resend.com/emails/{email_id}',
        headers={
            'Authorization': 'Bearer ' + open(os.path.join(os.path.dirname(__file__), '.resend_key')).read().strip()',
            'User-Agent': 'resend-python/2.0.0'
        }
    )
    with urllib.request.urlopen(req) as resp:
        data = json.loads(resp.read().decode('utf-8'))
        print(f"{label}: Event=[{data.get('last_event')}] | Subject=[{data.get('subject')}]")
