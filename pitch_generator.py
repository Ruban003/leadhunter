"""
Lead Hunter Agent - Pitch Generator Module (Upgraded for Global & India/Bangalore Outreach)
Crafts friendly, value-first, non-technical cold pitch emails and 1-Click WhatsApp messages from Ruban
tailored directly to each business's specific website audit findings.
"""
import urllib.parse

def generate_pitch(lead: dict, mockup_url: str = "") -> dict:
    """
    Generates personalized email and WhatsApp pitches for the given lead.
    Returns: {'subject': ..., 'body': ..., 'whatsapp_body': ..., 'whatsapp_url': ..., 'recipient': ...}
    """
    name = lead.get('name', 'Business Owner')
    city = lead.get('city', 'your area')
    niche = lead.get('niche', 'services')
    domain = lead.get('domain', 'your website')
    flaws = lead.get('flaws', [])
    grade = lead.get('grade', 'B')
    emails = lead.get('emails', [])
    recipient = emails[0] if emails else f"contact@{domain}"
    
    # Clean singular niche for natural phrasing
    niche_lower = niche.lower()
    if niche_lower.endswith('s'):
        niche_singular = niche_lower[:-1]
    else:
        niche_singular = niche_lower
        
    subject = f"Quick visual idea for {name}'s website"
    
    # Check if target is in India vs International
    city_lower = city.lower()
    is_india = any(k in city_lower for k in [
        'bangalore', 'bengaluru', 'chennai', 'tamil nadu', 'karnataka',
        'mumbai', 'hyderabad', 'delhi', 'india', 'karur', 'coimbatore', 'pune', 'indiranagar', 'koramangala', 'hsr'
    ])
    
    # Format specific flaws
    if flaws:
        bullet_points = "\n".join([f"• {flaw}" for flaw in flaws[:3]])
        wa_bullets = "\n".join([f"👉 {flaw}" for flaw in flaws[:3]])
    else:
        bullet_points = (
            "• Upgrading to a high-converting mobile layout with instant tap-to-call\n"
            "• Modernizing the hero banner to immediately showcase your 5-star customer reviews"
        )
        wa_bullets = (
            "👉 Upgrading to a high-converting mobile layout with instant tap-to-book\n"
            "👉 Modernizing the hero banner to showcase 5-star customer reviews"
        )
        
    mockup_mention_email = f"\nTo show you what a modern look could do for your brand, I put together a clean homepage concept:\n👉 Preview Redesign: {mockup_url}\n" if mockup_url else ""
    mockup_mention_wa = f"\nI put together a clean redesign concept for your brand:\nPreview: {mockup_url}\n" if mockup_url else ""

    if is_india:
        body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly do great work, but while viewing your website ({domain}) on my mobile phone, I noticed a couple of things that might be costing you direct customer inquiries:

{bullet_points}

When local customers search on smartphones for a {niche_singular}, over 60% leave within 3 seconds if the site isn't fast and effortless to navigate. 
{mockup_mention_email}
I'm a website & UI designer in Bengaluru (Ruban). I recently built the platform for She GLAM Salon (https://sheglam.rvsmps.store), which lets their clients book directly without third-party aggregator commissions.

You can explore my verified portfolio here: https://portfolio.rvsmps.store

Would you be open to a quick 30-second preview of the concept?

Best regards,

Ruban Velankanni
Website & UI Designer | Bengaluru
WhatsApp: +91 80986 71563
Portfolio: https://portfolio.rvsmps.store
"""
        wa_body = f"""Hello {name} Team,

I came across your profile and noticed your excellent reputation in {city}!

I recently engineered the website for She GLAM Salon (https://sheglam.rvsmps.store), which lets clients book directly without paying 20-25% aggregator platform commissions on every booking.

While reviewing {domain} on mobile, I noticed a few quick areas that could bring you 15-20 direct bookings weekly:
{wa_bullets}
{mockup_mention_wa}
Here is my verified portfolio: https://portfolio.rvsmps.store

Can I share the 30-second redesign preview with you here?

Warm regards,
Ruban Velankanni
Website & UI Designer | Bengaluru
+91 80986 71563"""

    else:
        # International (US/UK)
        body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly do great work, but while viewing your website ({domain}) on my mobile phone, I noticed a couple of things that might be costing you customer calls:

{bullet_points}

When local customers search on smartphones for a {niche_singular}, over 60% leave within 3 seconds if the site isn't fast and effortless to tap. 
{mockup_mention_email}
I'm a website & UI designer (Ruban), and to celebrate launching my freelance studio, I am offering a limited $9 Launch Special (normally $299) for a complete modern homepage redesign concept. 

My verified live portfolio: https://portfolio.rvsmps.store

No strings attached—would you be open to seeing the concept?

Best regards,

Ruban Velankanni
Website & UI Designer
Direct Email: rubanvelankanni8@gmail.com
WhatsApp: +91 80986 71563
"""
        wa_body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}.

I noticed a couple of mobile friction points on {domain} that might be costing you direct customer calls:
{wa_bullets}
{mockup_mention_wa}
I put together a clean, modern concept preview for your brand. You can check my live portfolio at https://portfolio.rvsmps.store

Would you like to see the 30-second concept?

Best regards,
Ruban Velankanni
Website & UI Designer
+91 80986 71563"""

    wa_url = f"https://web.whatsapp.com/send?text={urllib.parse.quote(wa_body.strip())}"

    return {
        'subject': subject,
        'body': body.strip(),
        'whatsapp_body': wa_body.strip(),
        'whatsapp_url': wa_url,
        'recipient': recipient
    }

if __name__ == "__main__":
    test_lead = {
        'name': 'Luxe Hair & Spa Studio',
        'city': 'Bangalore, Karnataka',
        'niche': 'Luxury Salons',
        'domain': 'luxehairbangalore.com',
        'grade': 'D',
        'flaws': [
            'Missing mobile booking integration',
            'No instant WhatsApp consultation button',
            'Slow page load on 4G network'
        ],
        'emails': ['contact@luxehairbangalore.com']
    }
    pitch = generate_pitch(test_lead, "https://portfolio.rvsmps.store")
    print("Subject:", pitch['subject'])
    print("\nWhatsApp URL:\n", pitch['whatsapp_url'][:80] + "...")
