"""
Lead Hunter Agent - Pitch Generator Module (Industry-Aware & Professional)
Crafts tailored, non-technical cold pitches in Indian Rupees (₹) and USD with direct 1-click WhatsApp & Gmail actions.
Features dynamic industry case studies, brand-name intelligence, and clean typography.
"""
import urllib.parse
import re

def sanitize_phone_for_whatsapp(raw_phone: str) -> str:
    """Extract and format digits for direct WhatsApp web chat."""
    if not raw_phone:
        return ""
    digits = re.sub(r'\D', '', raw_phone)
    if not digits:
        return ""
    
    # India mobile numbers
    if len(digits) == 10 and digits[0] in '6789':
        return f"91{digits}"
    elif len(digits) == 11 and digits.startswith('0') and digits[1] in '6789':
        return f"91{digits[1:]}"
    elif len(digits) == 12 and digits.startswith('91'):
        return digits
    # US phone numbers
    elif len(digits) == 10 and digits[0] in '23456789':
        return f"1{digits}"
    elif len(digits) == 11 and digits.startswith('1'):
        return digits
        
    return digits if len(digits) >= 10 else ""

def get_niche_case_study(niche: str) -> str:
    """Returns an industry-specific social proof reference instead of generic copy."""
    nl = niche.lower()
    if any(k in nl for k in ['dental', 'clinic', 'doctor', 'health', 'aesthetic']):
        return "I recently redesigned the patient appointment flow for local medical and dental practices, adding instant 1-tap WhatsApp consultation and clear treatment galleries that cut mobile patient drop-off by over 35%."
    elif any(k in nl for k in ['salon', 'spa', 'beauty', 'hair', 'makeover']):
        return "I recently built the direct booking platform for She GLAM Studio (https://sheglam.rvsmps.store), which lets their clients book stylists directly without paying 20-25% third-party aggregator commissions."
    elif any(k in nl for k in ['architecture', 'interior', 'designer', 'home', 'decor']):
        return "I recently developed high-speed luxury editorial portfolios for interior architects in Bengaluru, showcasing high-resolution project galleries with sub-second mobile loading."
    elif any(k in nl for k in ['bridal', 'couture', 'boutique', 'fashion']):
        return "I recently designed luxury boutique showcases with instant WhatsApp trial fitting schedules for premier bridal designers in Bengaluru."
    elif any(k in nl for k in ['cafe', 'dining', 'restaurant', 'food']):
        return "I recently developed interactive mobile digital menus with instant table reservations, eliminating slow PDF menu downloads."
    else:
        return "I recently engineered high-converting mobile websites for local Bengaluru businesses, increasing direct WhatsApp client inquiries by over 30%."

def generate_pitch(lead: dict, mockup_url: str = "") -> dict:
    """
    Generates personalized email and WhatsApp pitches with INR pricing and 1-click links.
    """
    name = lead.get('name', 'Business Owner')
    city = lead.get('city', 'Bengaluru')
    niche = lead.get('niche', 'Services')
    domain = lead.get('domain', 'your website')
    flaws = lead.get('flaws', [])
    emails = lead.get('emails', [])
    raw_phone = lead.get('phone', '')
    recipient = emails[0] if emails else f"contact@{domain}"
    
    clean_phone = sanitize_phone_for_whatsapp(raw_phone)
    case_study = get_niche_case_study(niche)
    
    niche_lower = niche.lower()
    niche_singular = niche_lower[:-1] if niche_lower.endswith('s') else niche_lower
        
    subject = f"Quick visual upgrade concept for {name} ({city})"
    
    city_lower = city.lower()
    is_india = any(k in city_lower for k in [
        'bangalore', 'bengaluru', 'chennai', 'tamil nadu', 'karnataka',
        'mumbai', 'hyderabad', 'delhi', 'india', 'karur', 'coimbatore', 'pune',
        'indiranagar', 'koramangala', 'hsr', 'whitefield', 'jayanagar'
    ])
    
    if flaws:
        bullet_points = "\n".join([f"• {flaw}" for flaw in flaws[:3]])
        wa_bullets = "\n".join([f"👉 {flaw}" for flaw in flaws[:3]])
    else:
        bullet_points = (
            "• Upgrading to an ultra-fast mobile booking flow with instant tap-to-WhatsApp\n"
            "• Modernizing hero visuals to showcase 5-star Google customer reviews and verified work"
        )
        wa_bullets = (
            "👉 Upgrading to a fast mobile booking flow with instant tap-to-WhatsApp\n"
            "👉 Modernizing hero visuals to showcase 5-star Google customer reviews"
        )
        
    mockup_mention_email = f"\nTo show you what an ultra-modern aesthetic could look like for your brand, I designed an interactive concept:\n👉 View Live Concept: {mockup_url}\n" if mockup_url else ""
    mockup_mention_wa = f"\nI designed a clean interactive concept preview for your brand:\n👉 Concept Preview: {mockup_url}\n" if mockup_url else ""

    if is_india:
        body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly have an impressive reputation in the area, but while testing {domain} on mobile, I noticed a couple of friction points that might be losing you direct customer bookings:

{bullet_points}

Over 70% of local customers in {city} search for a {niche_singular} on smartphones, and leave within 3 seconds if the site isn't instant or effortless to book.
{mockup_mention_email}
I am an independent Website & UI/UX Designer based in Bengaluru (Ruban Designs). {case_study}

To celebrate opening my client schedule for November, I am offering a limited ₹2,999 Starter Launch Package (normally ₹15,000) for a complete mobile-first redesign with direct WhatsApp booking and 3-5 day turnaround.

My verified live portfolio: https://portfolio.rvsmps.store

Would you be open to a quick 30-second preview of the concept?

Best regards,

Ruban Velankanni
Independent Website & UI Designer | Bengaluru
WhatsApp: +91 80986 71563
Portfolio: https://portfolio.rvsmps.store
"""
        wa_body = f"""Hello {name} Team,

I came across your profile and noticed your strong reputation in {city}!

{case_study}

While reviewing {domain} on mobile, I spotted a few quick opportunities to generate 15-20 more direct weekly inquiries:
{wa_bullets}
{mockup_mention_wa}
I'm offering a special ₹2,999 Starter Package for local {city} brands—turnaround in 3-5 days with direct WhatsApp appointment booking.

Verified Portfolio: https://portfolio.rvsmps.store

Would you like to see the 30-second concept?

Warm regards,
Ruban Velankanni
Website & UI Designer | Bengaluru
+91 80986 71563"""

    else:
        # International
        body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly do great work, but while viewing your website ({domain}) on mobile, I noticed a couple of friction points that might be costing you direct customer calls:

{bullet_points}

Over 65% of local traffic comes from smartphones, and prospective clients bounce if the layout is hard to navigate on mobile.
{mockup_mention_email}
I specialize in high-converting landing pages and websites with sub-second load times. We offer starter launches with direct booking and 3-5 day delivery.

Live Portfolio: https://portfolio.rvsmps.store

Would you be open to a quick 30-second walkthrough of the concept?

Best regards,

Ruban Velankanni
UI/UX & Web Designer
portfolio.rvsmps.store"""
        wa_body = f"""Hello {name} Team,

I spotted your business in {city} and saw a few quick mobile improvements for {domain}:
{wa_bullets}
{mockup_mention_wa}
Live Portfolio: https://portfolio.rvsmps.store

Would you like to see the concept preview?
Ruban Velankanni"""

    whatsapp_url = f"https://web.whatsapp.com/send?phone={clean_phone}&text={urllib.parse.quote(wa_body)}" if clean_phone else ""
    gmail_url = f"https://mail.google.com/mail/?view=cm&to={urllib.parse.quote(recipient)}&su={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"
    mailto_url = f"mailto:{recipient}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body)}"

    return {
        'subject': subject,
        'body': body,
        'whatsapp_body': wa_body,
        'whatsapp_url': whatsapp_url,
        'gmail_url': gmail_url,
        'mailto_url': mailto_url,
        'recipient': recipient,
        'phone': clean_phone
    }
