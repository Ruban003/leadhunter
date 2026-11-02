import subprocess

GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"
SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"

res = subprocess.run([GSHEETS_CMD, "readonly", "read", SPREADSHEET_ID, "Sheet1!A1:R25"], capture_output=True, text=True, encoding='utf-8', errors='replace')
lines = [l.split('\t') for l in res.stdout.splitlines() if l.strip()]

for idx, r in enumerate(lines):
    status = r[1] if len(r) > 1 else ""
    name = r[2] if len(r) > 2 else ""
    website = r[5] if len(r) > 5 else ""
    email = r[9] if len(r) > 9 else ""
    print(f"Row {idx+1}: Status=[{status}] | Name=[{name}] | Web=[{website}] | Email=[{email}]")
