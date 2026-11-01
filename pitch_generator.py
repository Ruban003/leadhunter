"""
Lead Hunter Agent - Pitch Generator Module (Upgraded for Global & India/Bangalore Outreach)
Crafts value-first, non-technical cold pitches in Indian Rupees (₹) and USD with direct 1-click WhatsApp & Gmail actions.
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

def generate_pitch(lead: dict, mockup_url: str = "") -> dict:
    """
    Generates personalized email and WhatsApp pitches with INR pricing and 1-click links.
    Returns: {
        'subject': ...,
        'body': ...,
        'whatsapp_body': ...,
        'whatsapp_url': ...,
        'gmail_url': ...,
        'mailto_url': ...,
        'recipient': ...,
        'phone': ...
    }
    """
    name = lead.get('name', 'Business Owner')
    city = lead.get('city', 'Bengaluru')
    niche = lead.get('niche', 'services')
    domain = lead.get('domain', 'your website')
    flaws = lead.get('flaws', [])
    emails = lead.get('emails', [])
    raw_phone = lead.get('phone', '')
    recipient = emails[0] if emails else f"contact@{domain}"
    
    clean_phone = sanitize_phone_for_whatsapp(raw_phone)
    
    # Clean singular niche for natural phrasing
    niche_lower = niche.lower()
    if niche_lower.endswith('s'):
        niche_singular = niche_lower[:-1]
    else:
        niche_singular = niche_lower
        
    subject = f"Quick visual upgrade concept for {name} ({city})"
    
    # Check if target is in India vs International
    city_lower = city.lower()
    is_india = any(k in city_lower for k in [
        'bangalore', 'bengaluru', 'chennai', 'tamil nadu', 'karnataka',
        'mumbai', 'hyderabad', 'delhi', 'india', 'karur', 'coimbatore', 'pune',
        'indiranagar', 'koramangala', 'hsr', 'whitefield', 'jayanagar'
    ])
    
    # Format specific flaws
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

I came across {name} while looking at {niche_lower} in {city}. You clearly have an impressive reputation, but while testing {domain} on mobile, I noticed a couple of friction points that might be losing you direct customer bookings:

{bullet_points}

Over 70% of local customers in {city} search for a {niche_singular} on smartphones, and leave within 3 seconds if the site isn't instant or effortless to book.
{mockup_mention_email}
I am an independent Website & UI Designer based in Bengaluru (Ruban Designs). I recently built the booking platform for She GLAM Salon (https://sheglam.rvsmps.store), which lets their clients book directly without paying 20-25% third-party aggregator commissions.

To celebrate opening my client schedule for November, I am offering a limited ₹2,999 Starter Launch Package (normally ₹15,000) for a complete mobile-first redesign with direct WhatsApp booking and 3-5 day turnaround.

My verified live portfolio: https://portfolio.rvsmps.store

Would you be open to a quick 30-second preview of the concept?

Best regards,

Ruban Velankanni
Website & UI Designer | Bengaluru
WhatsApp: +91 80986 71563
Portfolio: https://portfolio.rvsmps.store
"""
        wa_body = f"""Hello {name} Team,

I came across your profile and noticed your strong reputation in {city}!

I recently engineered the website for She GLAM Salon (https://sheglam.rvsmps.store), which allows their clients to book directly without paying 20-25% aggregator platform cuts.

While reviewing {domain} on mobile, I spotted a few quick opportunities to generate 15-20 more direct weekly inquiries:
{wa_bullets}
{mockup_mention_wa}
I'm offering a special ₹2,999 Starter Package (normally ₹15,000) for local {city} brands—turnaround in 3-5 days with direct WhatsApp appointment booking.

Verified Portfolio: https://portfolio.rvsmps.store

Would you like to see the 30-second concept?

Warm regards,
Ruban Velankanni
Website & UI Designer | Bengaluru
+91 80986 71563"""

    else:
        # International (US/UK)
        body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly do great work, but while viewing your website ({domain}) on mobile, I noticed a couple of friction points that might be costing you direct customer calls:

{bullet_points}

When local customers search on smartphones for a {niche_singular}, over 60% leave within 3 seconds if the site isn't fast and effortless to tap.
{mockup_mention_email}
I'm an independent website & UI designer (Ruban), and to celebrate launching my studio, I am offering a limited $49 Launch Special (normally $450) for a complete modern homepage redesign concept with fast 3-day delivery.

My verified live portfolio: https://portfolio.rvsmps.store

No strings attached—would you be open to seeing the concept?

Best regards,

Ruban Velankanni
Website & UI Designer
WhatsApp: +91 80986 71563
Portfolio: https://portfolio.rvsmps.store
"""
        wa_body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}.

I noticed a couple of mobile friction points on {domain} that might be costing you customer inquiries:
{wa_bullets}
{mockup_mention_wa}
I put together a clean, modern concept preview for your brand with a fast 3-day turnaround. You can check my live portfolio at https://portfolio.rvsmps.store

Would you like to see the 30-second concept?

Best regards,
Ruban Velankanni
Website & UI Designer
+91 80986 71563"""

    # Direct WhatsApp URL
    if clean_phone:
        wa_url = f"https://web.whatsapp.com/send?phone={clean_phone}&text={urllib.parse.quote(wa_body.strip())}"
    else:
        wa_url = f"https://web.whatsapp.com/send?text={urllib.parse.quote(wa_body.strip())}"

    # Direct Gmail Web compose URL
    gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(recipient)}&su={urllib.parse.quote(subject)}&body={urllib.parse.quote(body.strip())}"
    
    # Native mailto fallback
    mailto_url = f"mailto:{urllib.parse.quote(recipient)}?subject={urllib.parse.quote(subject)}&body={urllib.parse.quote(body.strip())}"

    return {
        'subject': subject,
        'body': body.strip(),
        'whatsapp_body': wa_body.strip(),
        'whatsapp_url': wa_url,
        'gmail_url': gmail_url,
        'mailto_url': mailto_url,
        'recipient': recipient,
        'phone': clean_phone or raw_phone
    }
