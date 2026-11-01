import csv
import subprocess
import os

SPREADSHEET_ID = "1puklMoU0iIF8EI7GpGQ9yRy-w077sfTj8TIQMWoDHjA"
GSHEETS_CMD = r"C:\Users\dell\.gemini\config\plugins\gsheets\skills\gsheets\scripts\gsheets.cmd"
CSV_PATH = os.path.join(os.path.dirname(__file__), "clean_leads_pipeline.csv")

headers = [
    "Timestamp", "Status", "Business Name", "City", "Niche", "Website",
    "Grade", "Score", "Phone / WhatsApp", "Email", "Audit Flaws",
    "Mockup Preview URL", "Email Subject", "Email Pitch Body",
    "WhatsApp Pitch", "WhatsApp 1-Click Link", "Gmail 1-Click Link", "Notes"
]

rows = [
    [
        "2026-11-01 16:30", "New Lead", "She GLAM Luxury Studio", "Indiranagar, Bangalore",
        "Luxury Salons & Spas", "https://sheglam.rvsmps.store", "D", "45%",
        "'+91 80986 71563", "contact@sheglam.rvsmps.store",
        "Slow mobile load (4.2s) | Missing instant WhatsApp booking",
        "https://leads.rvsmps.store/mockup/0?name=She%20GLAM&city=Indiranagar%2C%20Bangalore&niche=Luxury%20Salons%20%26%20Spas",
        "Quick visual upgrade concept for She GLAM Indiranagar",
        "Hi She GLAM Team, we audited your web presence in Indiranagar and noticed high bounce rates on mobile. We built an award-winning mobile concept preview with instant booking: https://leads.rvsmps.store/mockup/0?name=She%20GLAM",
        "Hello She GLAM Team! Quick preview of your brand with direct WhatsApp booking & fast mobile speed: https://leads.rvsmps.store/mockup/0?name=She%20GLAM",
        "https://web.whatsapp.com/send?phone=918098671563&text=Hi%20She%20GLAM%20Team",
        "https://mail.google.com/mail/?view=cm&to=contact@sheglam.rvsmps.store&su=Website%20Upgrade",
        "₹2,999 Starter Launch"
    ],
    [
        "2026-11-01 16:30", "New Lead", "Dentistree Aesthetic & Dental", "Koramangala, Bangalore",
        "Dental & Aesthetic Clinics", "https://dentistree.co.in", "C", "68%",
        "'+91 98450 12345", "smile@dentistree.co.in",
        "No one-click emergency appointment | Non-responsive hero banner",
        "https://leads.rvsmps.store/mockup/1?name=Dentistree&city=Koramangala%2C%20Bangalore&niche=Dental%20%26%20Aesthetic%20Clinics",
        "Patient conversion upgrade concept for Dentistree Koramangala",
        "Hi Dentistree Team, patients booking cosmetic dentistry on mobile expect instant WhatsApp consultation booking. We created a modern concept: https://leads.rvsmps.store/mockup/1?name=Dentistree",
        "Hello Dentistree Team! Quick preview of a patient-first mobile design with instant WhatsApp booking: https://leads.rvsmps.store/mockup/1?name=Dentistree",
        "https://web.whatsapp.com/send?phone=919845012345&text=Hi%20Dentistree%20Team",
        "https://mail.google.com/mail/?view=cm&to=smile@dentistree.co.in&su=Patient%20Flow%20Upgrade",
        "₹2,999 Starter Launch"
    ],
    [
        "2026-11-01 16:30", "New Lead", "Studio Vert Architecture & Interiors", "HSR Layout, Bangalore",
        "Architectural & Interior Design", "https://studiovert.in", "D", "40%",
        "'+91 99001 88223", "projects@studiovert.in",
        "Heavy uncompressed portfolio images (8MB hero) | No direct consultation flow",
        "https://leads.rvsmps.store/mockup/2?name=Studio%20Vert&city=HSR%20Layout%2C%20Bangalore&niche=Architectural%20%26%20Interior%20Design",
        "Luxury editorial portfolio upgrade for Studio Vert HSR Layout",
        "Hi Studio Vert Team, high-net-worth interior clients in HSR bounce when pages take >3s to load. We built a luxury editorial concept for your portfolio: https://leads.rvsmps.store/mockup/2?name=Studio%20Vert",
        "Hello Studio Vert Team! We built a high-speed editorial preview of your design portfolio with direct WhatsApp inquiry: https://leads.rvsmps.store/mockup/2?name=Studio%20Vert",
        "https://web.whatsapp.com/send?phone=919900188223&text=Hi%20Studio%20Vert%20Team",
        "https://mail.google.com/mail/?view=cm&to=projects@studiovert.in&su=Portfolio%20Upgrade",
        "₹7,999 3-Page Editorial"
    ],
    [
        "2026-11-01 16:30", "New Lead", "Artisan Coffee Roasters & Cafe", "Whitefield, Bangalore",
        "Fine Dining & Cafes", "https://artisancoffee.in", "D", "52%",
        "'+91 97412 33445", "hello@artisancoffee.in",
        "PDF menu download required | No interactive table reservation",
        "https://leads.rvsmps.store/mockup/3?name=Artisan%20Coffee&city=Whitefield%2C%20Bangalore&niche=Fine%20Dining%20%26%20Cafes",
        "Interactive digital menu & reservation experience for Artisan Coffee",
        "Hi Artisan Coffee Team, customers hate downloading PDF menus on phone networks. We built a live interactive digital menu concept: https://leads.rvsmps.store/mockup/3?name=Artisan%20Coffee",
        "Hello Artisan Coffee Team! Quick preview of an instant mobile menu with one-tap table reservation: https://leads.rvsmps.store/mockup/3?name=Artisan%20Coffee",
        "https://web.whatsapp.com/send?phone=919741233445&text=Hi%20Artisan%20Coffee%20Team",
        "https://mail.google.com/mail/?view=cm&to=hello@artisancoffee.in&su=Interactive%20Menu%20Upgrade",
        "₹2,999 Starter Launch"
    ],
    [
        "2026-11-01 16:30", "New Lead", "Zari & Silk Bridal Couture", "Jayanagar, Bangalore",
        "Bridal Boutiques & Makeovers", "https://zarisilk.in", "C", "60%",
        "'+91 98860 99887", "orders@zarisilk.in",
        "Missing VIP bridal consultation calendar | Broken mobile navigation",
        "https://leads.rvsmps.store/mockup/4?name=Zari%20%26%20Silk&city=Jayanagar%2C%20Bangalore&niche=Bridal%20Boutiques%20%26%20Makeovers",
        "VIP Bridal consultation booking upgrade for Zari & Silk Jayanagar",
        "Hi Zari & Silk Team, bridal shoppers in Jayanagar want immediate slot bookings for trial fittings. We built a luxury concept preview: https://leads.rvsmps.store/mockup/4?name=Zari%20%26%20Silk",
        "Hello Zari & Silk Team! Check out this luxury VIP bridal booking experience we designed for your boutique: https://leads.rvsmps.store/mockup/4?name=Zari%20%26%20Silk",
        "https://web.whatsapp.com/send?phone=919886099887&text=Hi%20Zari%20and%20Silk%20Team",
        "https://mail.google.com/mail/?view=cm&to=orders@zarisilk.in&su=VIP%20Bridal%20Booking%20Upgrade",
        "₹7,999 3-Page Editorial"
    ]
]

# Write RFC 4180 CSV
with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    writer.writerow(headers)
    for r in rows:
        writer.writerow(r)

print(f"Generated clean CSV at {CSV_PATH} with {len(rows)} records.")
