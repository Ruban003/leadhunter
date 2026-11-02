import subprocess

GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"
SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"

# Clean business names for rows 2 through 7
updates = [
    ("Sheet1!C2", "Bellance Salon & Spa"),
    ("Sheet1!C3", "Vurve Salon"),
    ("Sheet1!C4", "Cosmetic Dental Clinics"),
    ("Sheet1!C5", "Aesthetic Advanced Dental"),
    ("Sheet1!C6", "Aadhya Dental Care"),
    ("Sheet1!C7", "Ethicura Dental"),
]

for cell, val in updates:
    cmd = [GSHEETS_CMD, "mutate", "write", SPREADSHEET_ID, cell, val]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Updated {cell} -> {val}: {res.returncode}")

# Clear row 8 (HexaHealth aggregator)
clear_cmd = [GSHEETS_CMD, "mutate", "clear", SPREADSHEET_ID, "Sheet1!A8:R8"]
res_clear = subprocess.run(clear_cmd, capture_output=True, text=True)
print(f"Cleared row 8 (HexaHealth): {res_clear.returncode}")
