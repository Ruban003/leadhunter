import urllib.request
import json

ids = [
    ('DENTAL', '01a19b4b-4406-70e0-b5ba-f08e1441e9fd'),
    ('SALON', '01a19b4b-4d68-781d-9a49-10542d8750bc'),
    ('ARCHITECTURE', '01a19b4b-54a8-7460-8d41-22595afe9c15'),
    ('BRIDAL', '01a19b4b-5beb-7ba0-8866-2d944265db23'),
    ('CAFE', '01a19b4b-633f-7122-9502-22e0ad278bdb'),
]

for cat, email_id in ids:
    req = urllib.request.Request(
        f'https://api.resend.com/emails/{email_id}',
        headers={
            'Authorization': 'Bearer ' + open(os.path.join(os.path.dirname(__file__), '.resend_key')).read().strip()',
            'User-Agent': 'resend-python/2.0.0'
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            print(f"{cat}: Event=[{data.get('last_event')}] | Subject=[{data.get('subject')}]")
    except Exception as e:
        print(f"{cat} error: {e}")
