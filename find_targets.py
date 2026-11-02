import csv
import glob
import os

emails = set()
leads = []

for fpath in glob.glob("c:/Users/dell/Music/Ruban 2/clude/leadhunter_deploy/*.csv"):
    try:
        with open(fpath, encoding="utf-8", errors="ignore") as f:
            reader = csv.DictReader(f)
            for r in reader:
                em = (r.get("Email") or r.get("Emails") or "").strip()
                name = (r.get("Business Name") or r.get("Name") or "").strip()
                domain = (r.get("Domain") or r.get("Website") or "").strip()
                niche = (r.get("Niche") or "").strip()
                city = (r.get("City") or "Bengaluru, Karnataka").strip()
                
                # Exclude Aesthetic Advanced and aggregator
                if em and "@" in em and em.lower() not in emails:
                    if any(x in em.lower() for x in ["aestheticadvanced", "hexahealth", "example", "sentry"]):
                        continue
                    emails.add(em.lower())
                    leads.append({
                        "name": name,
                        "email": em,
                        "domain": domain,
                        "niche": niche or "Local Business",
                        "city": city
                    })
    except Exception as e:
        pass

print(f"Total non-Aesthetic candidates found: {len(leads)}")
for i, l in enumerate(leads):
    print(f"{i+1}. {l['name']} | {l['email']} | {l['niche']} | {l['domain']}")
