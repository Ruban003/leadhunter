"""
Lead Hunter Agent - Pitch Generator Module
Crafts friendly, value-first, non-technical cold pitch emails from Ruban
tailored directly to each business's specific website audit findings.
"""

def generate_pitch(lead: dict, mockup_url: str = "") -> dict:
    """
    Generates a personalized subject and body for the given lead.
    Returns: {'subject': ..., 'body': ..., 'recipient': ...}
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
    
    # Format specific flaws into customer-friendly bullet points
    if flaws:
        bullet_points = "\n".join([f"• {flaw}" for flaw in flaws[:3]])
    else:
        bullet_points = (
            "• Upgrading to a high-converting mobile layout with instant tap-to-call\n"
            "• Modernizing the hero banner to immediately showcase your 5-star customer reviews"
        )
        
    mockup_mention = f"\nTo show you what a modern look could do for your brand, I put together a clean homepage concept:\n👉 Preview Redesign: {mockup_url}\n" if mockup_url else ""
    
    body = f"""Hi {name} Team,

I came across {name} while looking at {niche_lower} in {city}. You clearly do great work, but while viewing your website ({domain}) on my mobile phone, I noticed a couple of things that might be costing you customer calls:

{bullet_points}

When local customers search on smartphones for a {niche_singular}, over 60% leave within 3 seconds if the site isn't fast and effortless to tap. 
{mockup_mention}
I'm a website & UI designer (Ruban), and to celebrate launching my freelance studio, I am offering a limited $9 Launch Special (normally $299) for a complete modern homepage redesign. If you like the direction, you get the full layered Figma design and mobile assets for just $9.

No strings attached—would you be open to seeing the concept?

Best regards,

Ruban
Website & UI Designer
Direct Email: rubanvelankanni8@gmail.com
"""

    return {
        'subject': subject,
        'body': body.strip(),
        'recipient': recipient
    }

if __name__ == "__main__":
    test_lead = {
        'name': 'Apex Roofing Co',
        'city': 'Austin, TX',
        'niche': 'Roofing Contractors',
        'domain': 'apexroofingaustin.com',
        'grade': 'C',
        'flaws': [
            'Slow load speed (4.2s) — drives away mobile customers',
            'Outdated copyright notice (© 2021) makes the business look inactive',
            "Weak conversion flow: Missing prominent 'Call Now' button"
        ],
        'emails': ['info@apexroofingaustin.com']
    }
    pitch = generate_pitch(test_lead, "http://localhost:8080/mockup/1")
    print("Subject:", pitch['subject'])
    print("\nBody:\n", pitch['body'])
