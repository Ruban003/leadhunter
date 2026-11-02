import subprocess
import csv
import os
import socket

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"

cmd = [GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R30"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace', check=True)
lines = [l.split("\t") for l in res.stdout.splitlines() if l.strip()]

headers = lines[0]
valid_rows = []

for r in lines[1:]:
    while len(r) < 18:
        r.append("")
    domain = r[5].lower()
    name = r[2].lower()
    email_val = r[9].strip().lower()
    
    # 1. Exclude Bodycraft, TripAdvisor, and demo domains
    if any(ex in domain for ex in ["bodycraft", "tripadvisor", "sheglam.rvsmps.store", "zarisilk.in", "studiovert.in", "artisancoffee.in", "dentistree.co.in"]):
        continue
    if any(ex in name for ex in ["bodycraft", "tripadvisor", "zari & silk", "studio vert", "artisan coffee", "dentistree", "she glam"]):
        continue
        
    # 2. Exclude fake email strings or invalid domains
    if "@" not in email_val:
        continue
    user, dom = email_val.split("@", 1)
    if any(k in email_val for k in ['rspack', 'boxicons', 'sentry', 'wixpress', 'schema.org']):
        continue
        
    # 3. DNS Host resolution check - verify domain exists
    try:
        socket.gethostbyname(dom.strip())
    except Exception:
        print(f"[-] Discarding invalid/dead domain: {dom}")
        continue
        
    # Clean phone
    phone = r[8].strip()
    if phone.startswith("#ERROR") or phone == "#ERROR!":
        phone = ""
    elif phone.startswith("+") and not phone.startswith("'"):
        phone = f"'{phone}"
    r[8] = phone
        
    valid_rows.append(r[:18])

print(f"Total genuine verified leads in Google Sheet: {len(valid_rows)}")

# Clear sheet and re-import
temp_csv = os.path.join(os.path.dirname(__file__), "cleaned_pipeline.csv")
with open(temp_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for vr in valid_rows:
        writer.writerow(vr)

clear_cmd = [GSHEETS_CMD, "mutate", "clear", SPREADSHEET_ID, "Sheet1!A1:R50"]
subprocess.run(clear_cmd, capture_output=True, text=True, check=True)

import_cmd = [GSHEETS_CMD, "mutate", "import-csv", SPREADSHEET_ID, temp_csv, "--sheet", "Sheet1"]
subprocess.run(import_cmd, capture_output=True, text=True, check=True)

# Format header
fmt_header = [GSHEETS_CMD, "mutate", "format", SPREADSHEET_ID, "--start-row", "0", "--end-row", "1", "--start-col", "0", "--end-col", "18", "--bg-color", "#0F172A", "--fg-color", "#FFFFFF", "--bold"]
subprocess.run(fmt_header, capture_output=True, text=True)

# Format data rows
fmt_data = [GSHEETS_CMD, "mutate", "format", SPREADSHEET_ID, "--start-row", "1", "--end-row", "50", "--start-col", "0", "--end-col", "18", "--bg-color", "#FFFFFF", "--fg-color", "#1E293B", "--wrap"]
subprocess.run(fmt_data, capture_output=True, text=True)

print("Cleaned verified leads successfully re-imported and formatted in Google Sheet.")
