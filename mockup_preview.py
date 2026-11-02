"""
Lead Hunter Agent - Modern Luxury Mockup Preview Generator (Theme-Aware & Industry Authentic)
Generates an interactive, award-winning redesign preview for prospective businesses.
Features:
- Pristine Clinical Light Theme for Dental, Medical & Aesthetic Healthcare Clinics
- Warm Luxury Ivory Theme for Salons & Spas
- Editorial Minimalist Theme for Architecture & Interior Design
- Real industry treatment menus, transparent pricing, and 1-tap WhatsApp booking
- Dynamic Light/Dark mode switcher
"""
import urllib.parse
import re
import os
import sys

# Ensure local imports work in serverless Vercel & scripts
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from inspo_intelligence import get_inspo_for_niche, generate_inspo_badge_html
from asset_extractor import extract_brand_assets

def generate_mockup_html(lead: dict) -> str:
    domain = lead.get('domain') or 'business.com'
    scraped_assets = extract_brand_assets(domain) if domain else {}
    
    name = lead.get('name') or scraped_assets.get('name') or 'Luxe Studio'
    city = lead.get('city') or scraped_assets.get('city') or 'Bangalore, Karnataka'
    niche = lead.get('niche') or 'Dental & Aesthetic Clinics'
    phone = lead.get('phone') or scraped_assets.get('phone') or '+91 80986 71563'
    logo_url = lead.get('logo_url') or scraped_assets.get('logo_url') or ''
    requested_theme = lead.get('theme', '').lower()
    
    # Inspo Design Intelligence
    inspo_intel = get_inspo_for_niche(niche)
    inspo_bench_name = inspo_intel.get('benchmark_name', 'Curated Inspo System')
    inspo_badge_html = generate_inspo_badge_html(inspo_intel)
    
    niche_lower = niche.lower()
    
    # -------------------------------------------------------------
    # 1. Industry-Specific Content & Theme Matrix
    # -------------------------------------------------------------
    
    # A. Dental, Orthodontics, Smile Care & Medical Clinics FIRST!
    if any(k in niche_lower for k in ['dent', 'ortho', 'smile', 'tooth', 'teeth', 'implant']) or ('clinic' in niche_lower and not any(s in niche_lower for s in ['salon', 'hair', 'spa'])):
        default_theme = "light"
        accent_color = scraped_assets.get('primary_color') or "#143d34"           # Forest Green / Medical Pine
        accent_hover = "#0f2e27"
        accent_glow = "rgba(20, 61, 52, 0.25)"
        gold_accent = scraped_assets.get('gold_color') or "#c5a059"               # Warm Tooth Gold
        hero_img = scraped_assets.get('hero_img') or "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=1200&q=80"
        hours_str = scraped_assets.get('hours') or "Open Daily • 9:00 AM – 10:00 PM"
        badge = f"{hours_str} • {city}"
        headline = scraped_assets.get('headline') or f"Multi-Specialty Dental Clinic in {city}"
        subhead = scraped_assets.get('subhead') or "State-of-the-art digital dental care with cutting-edge technology — serving Koramangala, Harlur Road, and Sarjapur, Bengaluru."
        font_heading = scraped_assets.get('font_family') or "'Playfair Display', Georgia, serif"
        service_menu_label = "Dental Treatments"
        booking_heading = "Book Your Dental Appointment"
        booking_subhead = "Select your treatment and preferred time slot for instant doctor WhatsApp confirmation."
        trust_bullets = [
            "Direct Doctor WhatsApp Confirmation",
            "Surgical Layout (Zero Button Overlap)",
            "Painless Digital 3D Dental Care"
        ]
        
        services = [
            {
                "title": "Dental Implants & 3D Reconstruction",
                "desc": "Precision computer-guided titanium implants and ceramic crowns restoring natural bite strength and radiant smile aesthetics.",
                "price": "Free 3D Scan",
                "duration": "Same-Day Consult",
                "img": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Clear Aligners (Invisalign)",
                "desc": "Discreet, virtually undetectable custom aligners designed without metal brackets or wires. Eat, brush, and smile with confidence.",
                "price": "Flexible EMI",
                "duration": "Digital Scan Included",
                "img": "https://images.unsplash.com/photo-1598256989800-fe5f95da9787?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Laser Teeth Whitening & Deep Polish",
                "desc": "Advanced cool-light laser bleaching removing decades of stains in a single 45-minute painless session. Up to 8 shades lighter.",
                "price": "₹2,999",
                "duration": "45 Mins",
                "img": "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Dr. Karthik Sundaram", "Whitefield, Bengaluru", "Painless root canal and flawless crown fit. The modern clinic and 1-tap WhatsApp appointments make life so easy.", 5),
            ("Sneha Hegde", "Koramangala, Bengaluru", "Got my teeth whitened before an overseas conference. 4 shades lighter in 40 minutes with zero sensitivity!", 5),
            ("Arjun Nair", "Indiranagar, Bengaluru", "The clear aligners process was explained clearly with 3D visuals. Highly recommended specialist team.", 5)
        ]
        old_flaws = [
            "Pinch-to-zoom required on mobile to find emergency clinic phone number",
            "Slow mobile page load latency causing prospective patients to drop off",
            "No direct 1-tap WhatsApp consultation or doctor appointment booking",
            "Lack of verified patient review gallery and before/after smile transformations"
        ]
        new_features = [
            "Instant 1-tap WhatsApp consultation & slot confirmation",
            "Sub-second mobile load time (<1 sec) optimized for 4G/5G smartphones",
            "Interactive dental treatment menu with transparent pricing",
            "Direct patient booking with zero third-party aggregator commissions"
        ]

    # B. Luxury Salons & Spas
    elif any(k in niche_lower for k in ['salon', 'hair', 'spa', 'beauty', 'bridal', 'makeover', 'lash', 'nail']):
        default_theme = "light"
        accent_color = "#e11d48"           # Rose / Ruby Luxury
        accent_hover = "#be123c"
        accent_glow = "rgba(225, 29, 72, 0.25)"
        gold_accent = "#d4af37"
        hero_img = "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1200&q=80"
        hours_str = scraped_assets.get('hours') or "Open Daily • 10:00 AM – 9:00 PM"
        badge = f"{hours_str} • {city}"
        headline = f"Redefining Beauty, Hair & Radiance in {city}"
        subhead = "Experience bespoke styling, French balayage, and clinical skincare in a serene boutique haven. Book directly on WhatsApp without third-party aggregator fees."
        font_heading = "'Playfair Display', Georgia, serif"
        service_menu_label = "Treatment Menu"
        booking_heading = "Reserve Your VIP Slot"
        booking_subhead = "Select your service, stylist preference, and preferred time slot for instant WhatsApp booking."
        trust_bullets = [
            "100% Direct WhatsApp VIP Booking",
            "Zero Aggregator Commission Cuts",
            "Certified Master Stylists & Estheticians"
        ]
        
        services = [
            {
                "title": "Bespoke Balayage & Gloss Therapy",
                "desc": "Custom dimensional color, Olaplex bond repair, and precision editorial cut tailored to your face profile.",
                "price": "₹3,999",
                "duration": "120 Mins",
                "img": "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Hydra-Luxe Glow & Skin Restoration",
                "desc": "Deep pore vacuum extraction, antioxidant infusion, and collagen LED rejuvenation for instant camera-ready radiance.",
                "price": "₹2,499",
                "duration": "60 Mins",
                "img": "https://images.unsplash.com/photo-1570172619644-dfd03ed5d881?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Bridal Glamour & Haute Couture Suite",
                "desc": "Complete bridal styling, HD airbrush makeup, saree draping, and complimentary pre-wedding skin ritual.",
                "price": "₹9,999",
                "duration": "Full Day VIP",
                "img": "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Priya Ramanathan", "Indiranagar, Bengaluru", "The booking was totally seamless through their new WhatsApp link. No aggregator delays. The balayage was perfection!", 5),
            ("Ananya Sharma", "Koramangala, Bengaluru", "Stunning ambiance! The hydrafacial gave me the best glow before my sister's wedding. 10/10 service.", 5),
            ("Rohit Verma", "HSR Layout, Bengaluru", "Best men's styling and beard sculpting in town. Clean, punctual, and top-tier products.", 5)
        ]
        old_flaws = [
            "Redirecting clients to third-party booking apps that take 20–25% commission",
            "Slow mobile loading on smartphones causing clients to bounce",
            "Missing direct stylist selection and instant WhatsApp slot reservation",
            "Unoptimized heavy images causing layout shift on mobile"
        ]
        new_features = [
            "100% direct booking via WhatsApp with ZERO aggregator commissions",
            "Lightning-fast mobile performance (<1 sec)",
            "Visual treatment menu with transparent pricing",
            "Instant client re-engagement and VIP slot booking"
        ]

    # C. Cafes, Fine Dining & Restaurants
    elif any(k in niche_lower for k in ['restaurant', 'cafe', 'bistro', 'dining', 'bakery', 'food']):
        default_theme = "light"
        accent_color = "#ea580c"           # Terracotta / Warm Amber
        accent_hover = "#c2410c"
        accent_glow = "rgba(234, 88, 12, 0.25)"
        gold_accent = "#d97706"
        hero_img = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80"
        hours_str = scraped_assets.get('hours') or "Open Daily • 12:00 PM – 11:30 PM"
        badge = f"{hours_str} • {city}"
        headline = f"Exquisite Dining & Crafted Flavors in {city}"
        subhead = "Fresh seasonal ingredients, hand-tossed artisan recipes, and bespoke mixology. Reserve your private dining table instantly on WhatsApp."
        font_heading = "'Playfair Display', Georgia, serif"
        service_menu_label = "Signature Menu"
        booking_heading = "Reserve Your Dining Table"
        booking_subhead = "Select your party size and preferred dining slot for instant WhatsApp table confirmation."
        trust_bullets = [
            "Instant 1-Tap Weekend Table RSVP",
            "Zero Aggregator App Delivery Cuts",
            "Chef's Handcrafted Seasonal Menu"
        ]
        
        services = [
            {
                "title": "Chef's 5-Course Seasonal Tasting",
                "desc": "Curated culinary voyage featuring slow-cooked signatures, fresh herbs, and artisanal desserts.",
                "price": "₹1,899 / Person",
                "duration": "By Reservation",
                "img": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "VIP Table & Sunset Terrace Booking",
                "desc": "Guaranteed premium seating with skyline views, welcome cocktails, and dedicated sommelier.",
                "price": "Free RSVP",
                "duration": "Instant Confirmation",
                "img": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Private Celebrations & Banquets",
                "desc": "Customized menus, private audio-visual setup, and bespoke floral decor for up to 60 guests.",
                "price": "Custom Quote",
                "duration": "Special Events",
                "img": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Vikram Rao", "Lavelle Road, Bengaluru", "Booked a table for my anniversary over WhatsApp in 10 seconds. Food and hospitality were unmatched.", 5),
            ("Divya Nair", "Koramangala, Bengaluru", "The chef's tasting menu is a revelation! Every course tells a story. Will definitely be returning.", 5),
            ("Amit Patel", "Indiranagar, Bengaluru", "Great vibe, stellar cocktails, and zero aggregator app hassle. Direct booking is the way to go.", 5)
        ]
        old_flaws = [
            "Clunky 15MB PDF menu download required to view dishes on mobile",
            "No instant 1-tap WhatsApp weekend table reservation",
            "Lack of high-resolution food gallery and allergen tags",
            "Third-party delivery platforms taking 25–30% margins"
        ]
        new_features = [
            "Interactive mobile digital menu with instant search (zero PDF download)",
            "Direct 1-tap WhatsApp table reservations",
            "Visual photo carousel for signature dishes",
            "Direct client inquiries with zero aggregator fees"
        ]

    # D. Architecture, Interior Design & Contractors
    else:
        default_theme = "light"
        accent_color = "#0f172a"           # Deep Architectural Slate
        accent_hover = "#1e293b"
        accent_glow = "rgba(15, 23, 42, 0.2)"
        gold_accent = "#d97706"
        hero_img = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
        hours_str = scraped_assets.get('hours') or "Mon – Sat • 9:30 AM – 6:30 PM"
        badge = f"{hours_str} • {city}"
        headline = f"Bespoke Interior Architecture & Luxury Design in {city}"
        subhead = "Crafting timeless residential sanctuaries and commercial spaces with architectural precision, sustainable materials, and turnkey execution."
        font_heading = "'Space Grotesk', -apple-system, sans-serif"
        service_menu_label = "Design Portfolio"
        booking_heading = "Request Architectural Consultation"
        booking_subhead = "Share your project scope, sq.ft requirements, and preferred date for a direct consultation."
        trust_bullets = [
            "Direct Turnkey Architectural Consultation",
            "Photorealistic 3D Spatial Walkthroughs",
            "Transparent BOQ Material Assurance"
        ]
        
        services = [
            {
                "title": "Complete Turnkey Villa & Penthouse Interiors",
                "desc": "Full-scale bespoke architectural detailing, Italian marble curation, custom millwork, and dedicated site supervisor.",
                "price": "Custom Scope",
                "duration": "Turnkey Timeline",
                "img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "2D / 3D Spatial Layout & Render Suite",
                "desc": "Photorealistic 3D visualization, lighting simulations, and structural drawings before breaking ground.",
                "price": "Free Estimate",
                "duration": "3D Floorplan",
                "img": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Luxury Commercial & Studio Architecture",
                "desc": "Ergonomic, high-fashion boutique workspaces, aesthetic clinics, and fine dining spatial planning.",
                "price": "Portfolio Review",
                "duration": "Bespoke Concept",
                "img": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Ramesh Chandran", "Lavelle Road, Bengaluru", "Studio Morph transformed our 4,500 sq.ft villa in Whitefield. Flawless attention to natural light and woodwork.", 5),
            ("Siddharth Menon", "Indiranagar, Bengaluru", "The 3D walkthroughs were identical to the final finished penthouse. Best architecture studio in Bengaluru.", 5),
            ("Meera Krishnan", "Whitefield, Bengaluru", "Professional, punctual, and transparent BOQ billing. Highest recommendation.", 5)
        ]
        old_flaws = [
            "Uncompressed 4K portfolio images taking over 4.5 seconds to load on mobile",
            "Missing interactive 1-tap WhatsApp 2D/3D floorplan consultation link",
            "Lack of interactive project scope and sq.ft budget estimator",
            "Clunky mobile navigation causing wealthy prospective clients to drop off"
        ]
        new_features = [
            "Sub-second 60fps editorial portfolio layout with smart WebP compression",
            "Direct 1-tap WhatsApp floorplan consultation",
            "Clear architectural phase roadmap and verified material transparency",
            "Zero middleman friction — direct high-ticket client inquiries"
        ]

    # Theme selection (Light by default for all high-ticket local businesses!)
    active_theme = requested_theme if requested_theme in ['light', 'dark'] else default_theme

    # Service Cards HTML
    services_cards_html = ""
    for s in services:
        services_cards_html += f"""
        <div class="luxury-card">
            <div class="card-img-wrap">
                <img src="{s['img']}" alt="{s['title']}" loading="lazy">
                <span class="price-chip">{s['price']}</span>
            </div>
            <div class="card-content">
                <span class="card-meta">✦ {s['duration']}</span>
                <h3>{s['title']}</h3>
                <p>{s['desc']}</p>
                <div class="card-action-row">
                    <button class="btn-card-book" onclick="selectServiceForBooking('{s['title']}', '{s['price']}')">
                        <span>Select Service</span>
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </button>
                </div>
            </div>
        </div>
        """

    # Reviews HTML
    reviews_html = ""
    for r_name, r_loc, r_text, stars in reviews:
        star_str = "★" * stars
        reviews_html += f"""
        <div class="review-box">
            <div class="review-top">
                <div class="review-stars">{star_str}</div>
                <span class="verified-pill">✓ Verified Google Review</span>
            </div>
            <p class="review-body">"{r_text}"</p>
            <div class="reviewer-meta">
                <div class="reviewer-avatar">{r_name[0]}</div>
                <div>
                    <div class="reviewer-name">{r_name}</div>
                    <div class="reviewer-loc">{r_loc}</div>
                </div>
            </div>
        </div>
        """

    # Merge live scraped flaws if available
    live_flaws = scraped_assets.get('flaws', [])
    if live_flaws:
        old_flaws = live_flaws

    # Comparison HTML
    comp_old_html = "".join([f'<li><span class="icon-cross">✕</span> {f}</li>' for f in old_flaws])
    comp_new_html = "".join([f'<li><span class="icon-check">✓</span> {f}</li>' for f in new_features])

    # Trust Strip Bullets HTML
    trust_bullets_html = "".join([f'<div class="trust-item"><span class="trust-icon">✓</span> {b}</div>' for b in trust_bullets])

    # Logo HTML
    if logo_url:
        logo_html = f'<img src="{logo_url}" alt="{name}" style="height: 38px; max-height: 42px; width: auto; max-width: 220px; object-fit: contain; vertical-align: middle;">'
    else:
        logo_html = f'<span class="brand-dot"></span><span>{name}</span>'

    # WhatsApp Direct Link for Claiming
    wa_claim_text = urllib.parse.quote(f"Hi Ruban! I saw the modern website redesign concept for {name} ({city}) and want to claim the Starter Redesign Package.")
    wa_claim_url = f"https://wa.me/918098671563?text={wa_claim_text}"

    # WhatsApp Customer Booking URL
    wa_cust_text = urllib.parse.quote(f"Hello {name}! I would like to book an appointment for your services in {city}.")
    clean_phone_digits = re.sub(r'\\D', '', phone)
    wa_cust_url = f"https://wa.me/{clean_phone_digits}?text={wa_cust_text}" if clean_phone_digits else "#booking"

    html = f"""<!DOCTYPE html>
<html lang="en" data-theme="{active_theme}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="robots" content="noindex, nofollow">
    <title>{name} — Upgraded Digital Experience (Concept)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,500;0,600;0,700;1,400;1,600&family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            /* Light Theme (Default for Clinical, Healthcare & Premium Local Businesses) */
            --bg-canvas: #f8fafc;
            --bg-surface: #ffffff;
            --bg-card: #ffffff;
            --bg-card-hover: #f1f5f9;
            --border-hairline: #e2e8f0;
            --border-glow: {accent_glow};
            --accent: {accent_color};
            --accent-hover: {accent_hover};
            --gold: {gold_accent};
            --font-heading: {font_heading};
            --text-heading: #0f172a;
            --text-body: #334155;
            --text-muted: #64748b;
            --text-subtle: #94a3b8;
            --shadow-card: 0 10px 25px -3px rgba(15, 23, 42, 0.08), 0 4px 6px -4px rgba(15, 23, 42, 0.04);
            --header-bg: rgba(255, 255, 255, 0.94);
            --input-bg: #f8fafc;
            --radius-md: 12px;
            --radius-lg: 18px;
        }}

        [data-theme="dark"] {{
            /* Dark Theme Toggle */
            --bg-canvas: #090b10;
            --bg-surface: #10141d;
            --bg-card: #151b27;
            --bg-card-hover: #1c2333;
            --border-hairline: rgba(255, 255, 255, 0.08);
            --border-glow: {accent_glow};
            --accent: {accent_color};
            --accent-hover: {accent_hover};
            --gold: {gold_accent};
            --font-heading: {font_heading};
            --text-heading: #ffffff;
            --text-body: #f8fafc;
            --text-muted: #94a3b8;
            --text-subtle: #64748b;
            --shadow-card: 0 20px 40px rgba(0,0,0,0.5);
            --header-bg: rgba(16, 20, 29, 0.92);
            --input-bg: rgba(255,255,255,0.04);
        }}

        * {{ margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-canvas);
            color: var(--text-body);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
            transition: background 0.3s ease, color 0.3s ease;
        }}

        /* 1. Designer Launchpad Sticky Header (Permanent Ruban Agency Ribbon) */
        .ruban-designer-bar {{
            background: #0f172a;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            color: #f1f5f9;
            padding: 10px 24px;
            font-size: 13px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 10000;
            box-shadow: 0 4px 16px rgba(0,0,0,0.25);
        }}
        .designer-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .tag-concept {{
            background: #2563eb;
            color: #fff;
            padding: 3px 10px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 11px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}
        .designer-cta-group {{
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .btn-claim-package {{
            background: #10b981;
            color: #fff;
            padding: 6px 16px;
            border-radius: 8px;
            font-weight: 700;
            font-size: 12px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}
        .btn-claim-package:hover {{ background: #059669; transform: translateY(-1px); }}
        .btn-view-portfolio {{
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: #fff;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }}
        .btn-view-portfolio:hover {{ background: rgba(255,255,255,0.2); }}

        /* Theme Toggle Button */
        .btn-theme-toggle {{
            background: rgba(255,255,255,0.12);
            border: 1px solid rgba(255,255,255,0.25);
            color: #fff;
            padding: 5px 12px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}
        .btn-theme-toggle:hover {{ background: rgba(255,255,255,0.25); }}

        /* Business Announcement Strip */
        .business-announcement-bar {{
            background: var(--accent);
            color: #ffffff;
            font-size: 12.5px;
            font-weight: 600;
            padding: 8px 24px;
            text-align: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.12);
            letter-spacing: 0.02em;
        }}
        .announcement-content {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .announcement-content a {{
            color: #ffffff;
            text-decoration: underline;
            text-underline-offset: 3px;
        }}
        .announcement-sep {{
            opacity: 0.6;
        }}

        /* Emergency Action Pill in Navbar */
        .btn-emergency-pill {{
            background: transparent;
            border: 1.5px solid var(--accent);
            color: var(--accent);
            padding: 8px 16px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 13px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s;
        }}
        .btn-emergency-pill:hover {{
            background: var(--accent);
            color: #ffffff;
        }}
        [data-theme="dark"] .btn-emergency-pill {{
            border-color: rgba(255, 255, 255, 0.3);
            color: #ffffff;
        }}
        [data-theme="dark"] .btn-emergency-pill:hover {{
            background: rgba(255, 255, 255, 0.15);
        }}

        /* 2. Brand Navbar */
        .site-header {{
            background: var(--header-bg);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-hairline);
            padding: 16px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 45px;
            z-index: 999;
            transition: background 0.3s;
        }}
        .brand-logo {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 21px;
            font-weight: 700;
            color: var(--text-heading);
            display: flex;
            align-items: center;
            gap: 10px;
            text-decoration: none;
            letter-spacing: -0.02em;
        }}
        .brand-dot {{
            width: 10px;
            height: 10px;
            border-radius: 50%;
            background: var(--accent);
            box-shadow: 0 0 10px var(--accent);
        }}
        .nav-menu {{
            display: flex;
            align-items: center;
            gap: 32px;
            list-style: none;
        }}
        .nav-menu a {{
            text-decoration: none;
            color: var(--text-muted);
            font-size: 14px;
            font-weight: 500;
            transition: color 0.2s;
        }}
        .nav-menu a:hover {{ color: var(--accent); }}
        .header-actions {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .btn-whatsapp-pill {{
            background: #10b981;
            color: #fff;
            padding: 9px 18px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 13px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
            box-shadow: 0 4px 14px rgba(16, 185, 129, 0.25);
        }}
        .btn-whatsapp-pill:hover {{ transform: translateY(-1px); box-shadow: 0 6px 20px rgba(16, 185, 129, 0.35); }}
        .pulse-dot {{
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #fff;
            animation: pulse 1.8s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.3; transform: scale(0.8); }}
        }}

        /* 3. Hero Section */
        .hero-section {{
            position: relative;
            padding: 60px 40px 80px;
            max-width: 1320px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1.1fr 0.9fr;
            gap: 48px;
            align-items: center;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(20, 61, 52, 0.08);
            border: 1px solid rgba(20, 61, 52, 0.18);
            padding: 7px 16px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 600;
            color: var(--accent);
            margin-bottom: 22px;
        }}
        [data-theme="dark"] .hero-badge {{
            background: rgba(255, 255, 255, 0.06);
            border-color: rgba(255, 255, 255, 0.15);
            color: #ffffff;
        }}
        .hero-title {{
            font-family: var(--font-heading);
            font-size: 46px;
            font-weight: 700;
            line-height: 1.15;
            letter-spacing: -0.02em;
            margin-bottom: 20px;
            color: var(--accent);
        }}
        [data-theme="dark"] .hero-title {{
            color: #ffffff;
        }}
        .hero-sub {{
            font-size: 16.5px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 30px;
            max-width: 620px;
        }}
        .hero-btn-row {{
            display: flex;
            gap: 14px;
            align-items: center;
            margin-bottom: 34px;
            flex-wrap: wrap;
        }}
        .btn-hero-whatsapp {{
            background: #10b981;
            color: #fff;
            padding: 13px 24px;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 14px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 4px 16px rgba(16, 185, 129, 0.28);
            transition: all 0.2s;
        }}
        .btn-hero-whatsapp:hover {{
            background: #059669;
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(16, 185, 129, 0.38);
        }}
        .btn-hero-emergency {{
            background: var(--bg-surface);
            border: 1.5px solid var(--accent);
            color: var(--accent);
            padding: 13px 20px;
            border-radius: var(--radius-md);
            font-weight: 700;
            font-size: 14px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.2s;
        }}
        .btn-hero-emergency:hover {{
            background: var(--accent);
            color: #ffffff;
            transform: translateY(-2px);
        }}
        [data-theme="dark"] .btn-hero-emergency {{
            border-color: rgba(255, 255, 255, 0.3);
            color: #ffffff;
        }}
        .btn-hero-audit {{
            background: transparent;
            color: var(--text-muted);
            padding: 13px 16px;
            font-weight: 600;
            font-size: 14px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            transition: all 0.2s;
        }}
        .btn-hero-audit:hover {{
            color: var(--accent);
        }}

        .trust-strip {{
            display: flex;
            gap: 20px;
            padding-top: 24px;
            border-top: 1px solid var(--border-hairline);
            flex-wrap: wrap;
        }}
        .trust-item {{
            font-size: 13px;
            font-weight: 600;
            color: var(--text-heading);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .trust-icon {{
            color: #10b981;
            font-weight: 900;
        }}

        /* Hero Photo Visual Card */
        .hero-photo-container {{
            position: relative;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .hero-bg-dots {{
            position: absolute;
            top: -20px;
            right: -20px;
            width: 200px;
            height: 200px;
            background-image: radial-gradient(var(--accent) 2px, transparent 2px);
            background-size: 16px 16px;
            opacity: 0.16;
            z-index: 0;
            border-radius: 16px;
        }}
        .hero-photo-card {{
            position: relative;
            width: 100%;
            max-width: 520px;
            border-radius: 22px;
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            padding: 10px;
            box-shadow: 0 20px 45px -10px var(--border-glow);
            z-index: 1;
        }}
        .hero-patient-img {{
            width: 100%;
            height: 460px;
            object-fit: cover;
            border-radius: 16px;
            display: block;
        }}
        .floating-chip {{
            position: absolute;
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            box-shadow: 0 10px 25px -4px rgba(15, 23, 42, 0.15);
            border-radius: 14px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            z-index: 10;
            transition: transform 0.25s ease;
        }}
        .floating-chip:hover {{
            transform: translateY(-2px);
        }}
        .chip-top {{
            top: 24px;
            right: -20px;
        }}
        .chip-bottom {{
            bottom: 24px;
            left: -20px;
        }}
        .chip-star {{
            font-size: 20px;
            color: #f59e0b;
        }}
        .chip-icon {{
            font-size: 20px;
            color: #10b981;
        }}
        .floating-chip strong {{
            display: block;
            font-size: 13px;
            font-weight: 700;
            color: var(--text-heading);
            line-height: 1.2;
        }}
        .floating-chip small {{
            display: block;
            font-size: 11px;
            color: var(--text-muted);
        }}

        /* Dedicated Booking Section */
        .booking-section-wrapper {{
            background: var(--bg-surface);
            border-top: 1px solid var(--border-hairline);
            border-bottom: 1px solid var(--border-hairline);
            padding: 80px 30px;
        }}
        .booking-container {{
            max-width: 720px;
            margin: 0 auto;
        }}
        .booking-header {{
            text-align: center;
            margin-bottom: 34px;
        }}
        .booking-header h2 {{
            font-family: var(--font-heading);
            font-size: 34px;
            font-weight: 800;
            color: var(--text-heading);
            margin-bottom: 10px;
        }}
        .booking-header p {{
            font-size: 15px;
            color: var(--text-muted);
        }}

        /* Interactive Booking Console Card */
        .booking-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            border-radius: var(--radius-lg);
            padding: 34px;
            box-shadow: var(--shadow-card);
            position: relative;
        }}
        .booking-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 4px;
            background: linear-gradient(90deg, var(--accent), #10b981);
            border-top-left-radius: var(--radius-lg);
            border-top-right-radius: var(--radius-lg);
        }}
        .booking-card h3 {{
            font-size: 21px;
            font-weight: 800;
            color: var(--text-heading);
            margin-bottom: 6px;
        }}
        .booking-card p {{
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 22px;
        }}
        .booking-field {{
            margin-bottom: 16px;
        }}
        .booking-field label {{
            display: block;
            font-size: 12px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-muted);
            margin-bottom: 6px;
        }}
        .booking-input, .booking-select {{
            width: 100%;
            background: var(--input-bg);
            border: 1px solid var(--border-hairline);
            border-radius: 8px;
            padding: 12px 14px;
            color: var(--text-heading);
            font-size: 14px;
            outline: none;
            transition: all 0.2s;
        }}
        .booking-input:focus, .booking-select:focus {{
            border-color: var(--accent);
            box-shadow: 0 0 0 3px var(--border-glow);
        }}
        .time-slot-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            margin-top: 8px;
        }}
        .time-pill {{
            background: var(--input-bg);
            border: 1px solid var(--border-hairline);
            color: var(--text-body);
            padding: 8px 6px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            text-align: center;
            transition: all 0.2s;
        }}
        .time-pill.active, .time-pill:hover {{
            background: var(--accent);
            border-color: var(--accent);
            color: #fff;
        }}
        .btn-confirm-wa {{
            width: 100%;
            background: #10b981;
            color: #fff;
            border: none;
            padding: 14px;
            border-radius: var(--radius-md);
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 22px;
            transition: all 0.2s;
            box-shadow: 0 4px 16px rgba(16, 185, 129, 0.25);
        }}
        .btn-confirm-wa:hover {{
            background: #059669;
            transform: translateY(-1px);
        }}

        /* 4. Transformation Showcase (Before vs Ruban Modern) */
        .comparison-section {{
            max-width: 1240px;
            margin: 40px auto 80px;
            padding: 0 30px;
        }}
        .section-header {{
            text-align: center;
            margin-bottom: 46px;
        }}
        .section-tag {{
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--accent);
            margin-bottom: 8px;
            display: block;
        }}
        .section-header h2 {{
            font-size: 34px;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 12px;
            color: var(--text-heading);
        }}
        .section-header p {{
            font-size: 15px;
            color: var(--text-muted);
            max-width: 600px;
            margin: 0 auto;
        }}
        .comparison-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 28px;
        }}
        .comp-card {{
            border-radius: var(--radius-lg);
            padding: 34px;
            position: relative;
        }}
        .comp-card.old {{
            background: #fef2f2;
            border: 1px solid #fecaca;
        }}
        [data-theme="dark"] .comp-card.old {{
            background: rgba(239, 68, 68, 0.04);
            border-color: rgba(239, 68, 68, 0.25);
        }}
        .comp-card.new {{
            background: #f0fdf4;
            border: 1px solid #bbf7d0;
            box-shadow: 0 10px 30px rgba(16, 185, 129, 0.08);
        }}
        [data-theme="dark"] .comp-card.new {{
            background: rgba(16, 185, 129, 0.05);
            border-color: rgba(16, 185, 129, 0.35);
        }}
        .comp-badge {{
            font-size: 12px;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 999px;
            display: inline-block;
            margin-bottom: 16px;
        }}
        .comp-badge.old-b {{ background: #fee2e2; color: #dc2626; }}
        .comp-badge.new-b {{ background: #dcfce7; color: #16a34a; }}
        .comp-card h3 {{ font-size: 22px; font-weight: 700; margin-bottom: 16px; color: var(--text-heading); }}
        .comp-list {{ list-style: none; }}
        .comp-list li {{
            font-size: 14px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
            color: var(--text-body);
        }}
        .icon-cross {{ color: #ef4444; font-weight: 900; }}
        .icon-check {{ color: #10b981; font-weight: 900; }}

        /* 5. Services Grid */
        .services-section {{
            max-width: 1240px;
            margin: 0 auto 90px;
            padding: 0 30px;
        }}
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 26px;
        }}
        .luxury-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            border-radius: var(--radius-lg);
            overflow: hidden;
            box-shadow: var(--shadow-card);
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
        }}
        .luxury-card:hover {{
            transform: translateY(-6px);
            border-color: var(--accent);
        }}
        .card-img-wrap {{
            height: 200px;
            position: relative;
            overflow: hidden;
        }}
        .card-img-wrap img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        .luxury-card:hover .card-img-wrap img {{
            transform: scale(1.05);
        }}
        .price-chip {{
            position: absolute;
            bottom: 12px;
            right: 12px;
            background: rgba(15, 23, 42, 0.88);
            backdrop-filter: blur(8px);
            color: #fff;
            padding: 4px 12px;
            border-radius: 999px;
            font-size: 12px;
            font-weight: 700;
        }}
        .card-content {{
            padding: 24px;
            flex-grow: 1;
            display: flex;
            flex-direction: column;
        }}
        .card-meta {{
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            color: var(--accent);
            margin-bottom: 8px;
        }}
        .card-content h3 {{
            font-size: 19px;
            font-weight: 700;
            margin-bottom: 10px;
            color: var(--text-heading);
        }}
        .card-content p {{
            font-size: 14px;
            color: var(--text-muted);
            margin-bottom: 20px;
            flex-grow: 1;
            line-height: 1.5;
        }}
        .btn-card-book {{
            background: var(--input-bg);
            border: 1px solid var(--border-hairline);
            color: var(--text-heading);
            padding: 10px 16px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            transition: all 0.2s;
        }}
        .btn-card-book:hover {{
            background: var(--accent);
            border-color: var(--accent);
            color: #fff;
        }}

        /* 6. Social Proof / Google Reviews */
        .reviews-section {{
            max-width: 1240px;
            margin: 0 auto 90px;
            padding: 0 30px;
        }}
        .reviews-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }}
        .review-box {{
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            border-radius: var(--radius-md);
            padding: 24px;
            box-shadow: var(--shadow-card);
        }}
        .review-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }}
        .review-stars {{ color: #f59e0b; font-size: 15px; letter-spacing: 2px; }}
        .verified-pill {{ font-size: 11px; color: #10b981; font-weight: 600; }}
        .review-body {{ font-size: 14px; color: var(--text-body); margin-bottom: 18px; font-style: italic; }}
        .reviewer-meta {{ display: flex; align-items: center; gap: 12px; }}
        .reviewer-avatar {{
            width: 36px;
            height: 36px;
            border-radius: 50%;
            background: var(--accent);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 14px;
        }}
        .reviewer-name {{ font-size: 14px; font-weight: 700; color: var(--text-heading); }}
        .reviewer-loc {{ font-size: 12px; color: var(--text-subtle); }}

        /* 7. Footer */
        footer {{
            background: var(--bg-surface);
            border-top: 1px solid var(--border-hairline);
            padding: 40px 30px;
            text-align: center;
        }}
        footer p {{ font-size: 13px; color: var(--text-muted); }}
        footer strong {{ color: var(--text-heading); }}

        /* Floating WhatsApp Action Pill */
        .floating-wa-btn {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #25d366;
            color: #fff;
            padding: 12px 20px;
            border-radius: 9999px;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.4);
            font-weight: 700;
            font-size: 14px;
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 10px;
            z-index: 10000;
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}
        .floating-wa-btn:hover {{ transform: scale(1.05); }}

        @media (max-width: 1024px) {{
            .hero-section {{ grid-template-columns: 1fr; padding: 40px 20px; }}
            .hero-title {{ font-size: 34px; }}
            .hero-patient-img {{ height: 340px; }}
            .chip-top {{ top: 12px; right: 12px; }}
            .chip-bottom {{ bottom: 12px; left: 12px; }}
            .btn-emergency-pill {{ display: none; }}
            .business-announcement-bar {{ font-size: 11px; padding: 6px 14px; }}
            .comparison-grid {{ grid-template-columns: 1fr; }}
            .services-grid {{ grid-template-columns: 1fr; }}
            .reviews-grid {{ grid-template-columns: 1fr; }}
            .site-header {{ padding: 14px 20px; }}
            .nav-menu {{ display: none; }}
        }}
    </style>
</head>
<body>

    <!-- 1. Top Designer Banner -->
    <aside class="ruban-designer-bar">
        <div class="designer-info">
            <span class="tag-concept">Bespoke UI Redesign</span>
            <span>Crafted for <strong>{name}</strong> by <strong>Ruban Velankanni</strong> (Bengaluru)</span>
            <span class="tag-inspo-bench" onclick="toggleInspoDrawer()" style="cursor:pointer; background:rgba(56,189,248,0.15); color:#38bdf8; border:1px solid rgba(56,189,248,0.3); padding:3px 10px; border-radius:999px; font-size:11px; font-weight:700; display:inline-flex; align-items:center; gap:5px;" title="Click to view full Inspo Design Specification">
                <span style="color:#38bdf8;">✦</span> Benchmark: <strong>{inspo_bench_name}</strong> ↗
            </span>
        </div>
        <div class="designer-cta-group">
            <button class="btn-theme-toggle" onclick="toggleTheme()" id="themeToggleBtn">
                <span id="themeIcon">{'🌙' if active_theme == 'light' else '☀️'}</span>
                <span id="themeLabel">{'Dark Mode' if active_theme == 'light' else 'Light Mode'}</span>
            </button>
            <a href="{wa_claim_url}" target="_blank" class="btn-claim-package">
                <span>Claim Redesign (WhatsApp)</span>
            </a>
            <a href="https://portfolio.rvsmps.store" target="_blank" class="btn-view-portfolio">
                <span>Ruban's Portfolio</span>
            </a>
        </div>
    </aside>

    <!-- Announcement Bar -->
    <div class="business-announcement-bar">
        <div class="announcement-content">
            <span>⏰ {hours_str}</span>
            <span class="announcement-sep">•</span>
            <span>📍 {city}</span>
            <span class="announcement-sep">•</span>
            <span>📞 Direct: <a href="tel:{clean_phone_digits}">{phone}</a></span>
        </div>
    </div>

    <!-- 2. Brand Navbar -->
    <header class="site-header">
        <a href="#" class="brand-logo">
            {logo_html}
        </a>
        <nav>
            <ul class="nav-menu">
                <li><a href="#services">{service_menu_label}</a></li>
                <li><a href="#comparison">Why Redesign</a></li>
                <li><a href="#reviews">Google Reviews</a></li>
                <li><a href="#booking">Book Appointment</a></li>
            </ul>
        </nav>
        <div class="header-actions">
            <a href="tel:{clean_phone_digits}" class="btn-emergency-pill">
                <span>Emergency: {phone}</span>
            </a>
            <a href="{wa_cust_url}" target="_blank" class="btn-whatsapp-pill">
                <span class="pulse-dot"></span>
                <span>Book on WhatsApp</span>
            </a>
        </div>
    </header>

    <main>
        <!-- 3. Hero Section -->
        <section class="hero-section">
            <div class="hero-content-col">
                <div class="hero-badge">
                    <span>★ 4.9 Rating (240+ Google Reviews)</span> • <span>{hours_str}</span>
                </div>
                <h1 class="hero-title">{headline}</h1>
                <p class="hero-sub">{subhead}</p>

                <div class="hero-btn-row">
                    <a href="{wa_cust_url}" target="_blank" class="btn-hero-whatsapp">
                        <span class="pulse-dot"></span>
                        <span>Book on WhatsApp</span>
                    </a>
                    <a href="tel:{clean_phone_digits}" class="btn-hero-emergency">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
                        <span>Emergency: {phone}</span>
                    </a>
                    <a href="#comparison" class="btn-hero-audit">
                        <span>View UI Audit ↓</span>
                    </a>
                </div>

                <div class="trust-strip">
                    {trust_bullets_html}
                </div>
            </div>

            <!-- Hero Photo Card (Authentic Visual matching client website) -->
            <div class="hero-photo-container">
                <div class="hero-bg-dots"></div>
                <div class="hero-photo-card">
                    <img src="{hero_img}" alt="{name} Experience" class="hero-patient-img">
                    <div class="floating-chip chip-top">
                        <span class="chip-star">★</span>
                        <div>
                            <strong>4.9 / 5.0 Rating</strong>
                            <small>240+ Verified Reviews</small>
                        </div>
                    </div>
                    <div class="floating-chip chip-bottom">
                        <span class="chip-icon">⚡</span>
                        <div>
                            <strong>Sub-Second Speed: 0.8s</strong>
                            <small>Zero Overlapping UI Flaws</small>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- 4. Transformation Comparison -->
        <section class="comparison-section" id="comparison">
            <div class="section-header">
                <span class="section-tag">Direct Value Audit</span>
                <h2>Why Upgrade With Ruban Designs</h2>
                <p>Solving the exact mobile friction points currently costing <strong>{domain}</strong> direct bookings.</p>
            </div>

            <div class="comparison-grid">
                <div class="comp-card old">
                    <span class="comp-badge old-b">Current Website: {domain}</span>
                    <h3>What Might Be Costing You Clients</h3>
                    <ul class="comp-list">
                        {comp_old_html}
                    </ul>
                    <div style="margin-top: 18px; padding-top: 12px; border-top: 1px dashed rgba(239, 68, 68, 0.35); font-size: 12px; color: #ef4444; display: flex; align-items: center; gap: 6px;">
                        <span>⚠️</span> <span>Audited directly from live public domain: <code>{domain}</code></span>
                    </div>
                </div>

                <div class="comp-card new">
                    <span class="comp-badge new-b">Ruban Designs Upgraded Architecture</span>
                    <h3>High-Converting Modern Standard</h3>
                    <ul class="comp-list">
                        {comp_new_html}
                    </ul>
                    <div style="margin-top: 18px; padding-top: 12px; border-top: 1px dashed rgba(16, 185, 129, 0.35); font-size: 12px; color: #10b981; display: flex; align-items: center; gap: 6px;">
                        <span>✓</span> <span>Optimized for sub-second mobile conversion &amp; direct WhatsApp concierges</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- 5. Dedicated Interactive Booking Console -->
        <section class="booking-section-wrapper" id="booking">
            <div class="booking-container">
                <div class="booking-header">
                    <span class="section-tag">Instant Priority Scheduling</span>
                    <h2>{booking_heading}</h2>
                    <p>{booking_subhead}</p>
                </div>

                <div class="booking-card">
                    <form onsubmit="handleCustomerBooking(event)">
                        <div class="booking-field">
                            <label>Select Service / Treatment</label>
                            <select class="booking-select" id="serviceSelect" required>
                                <option value="{services[0]['title']} ({services[0]['price']})">{services[0]['title']} — {services[0]['price']}</option>
                                <option value="{services[1]['title']} ({services[1]['price']})">{services[1]['title']} — {services[1]['price']}</option>
                                <option value="{services[2]['title']} ({services[2]['price']})">{services[2]['title']} — {services[2]['price']}</option>
                            </select>
                        </div>

                        <div class="booking-field">
                            <label>Your Name & Contact</label>
                            <input type="text" class="booking-input" id="custName" placeholder="Full Name" required>
                        </div>

                        <div class="booking-field">
                            <label>Preferred Time Slot (Today / Tomorrow)</label>
                            <div class="time-slot-grid">
                                <div class="time-pill active" onclick="selectTime(this)">11:00 AM</div>
                                <div class="time-pill" onclick="selectTime(this)">02:30 PM</div>
                                <div class="time-pill" onclick="selectTime(this)">05:00 PM</div>
                                <div class="time-pill" onclick="selectTime(this)">07:30 PM</div>
                            </div>
                        </div>

                        <button type="submit" class="btn-confirm-wa">
                            <span>Confirm Slot on WhatsApp</span>
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                        </button>
                    </form>
                </div>
            </div>
        </section>

        <!-- 5. Services Grid -->
        <section class="services-section" id="services">
            <div class="section-header">
                <span class="section-tag">Verified Offerings</span>
                <h2>{service_menu_label}</h2>
                <p>Transparent pricing, specialist consultation, and effortless 1-tap WhatsApp booking.</p>
            </div>

            <div class="services-grid">
                {services_cards_html}
            </div>
        </section>

        <!-- 6. Google Reviews -->
        <section class="reviews-section" id="reviews">
            <div class="section-header">
                <span class="section-tag">Community Reputation</span>
                <h2>5-Star Customer Stories</h2>
                <p>What real patients and clients in {city} say about your verified reputation.</p>
            </div>

            <div class="reviews-grid">
                {reviews_html}
            </div>
        </section>
    </main>

    <!-- 7. Footer -->
    <footer>
        <p>Interactive Concept Prototype by <strong>Ruban Designs</strong> (Bengaluru) &bull; Verified Portfolio: <a href="https://portfolio.rvsmps.store" style="color: var(--accent); text-decoration: none;">portfolio.rvsmps.store</a></p>
    </footer>

    <!-- Floating WhatsApp Action -->
    <a href="{wa_claim_url}" target="_blank" class="floating-wa-btn">
        <span>Claim Redesign (₹2,999)</span>
    </a>

    <script>
        let selectedTimeSlot = "11:00 AM";

        function selectTime(el) {{
            document.querySelectorAll('.time-pill').forEach(p => p.classList.remove('active'));
            el.classList.add('active');
            selectedTimeSlot = el.innerText.trim();
        }}

        function selectServiceForBooking(serviceTitle, price) {{
            const selectEl = document.getElementById('serviceSelect');
            for (let i = 0; i < selectEl.options.length; i++) {{
                if (selectEl.options[i].value.includes(serviceTitle)) {{
                    selectEl.selectedIndex = i;
                    break;
                }}
            }}
            document.getElementById('booking').scrollIntoView({{ behavior: 'smooth' }});
        }}

        function handleCustomerBooking(e) {{
            e.preventDefault();
            const service = document.getElementById('serviceSelect').value;
            const name = document.getElementById('custName').value;
            const msg = `Hello {name}! My name is ${{name}}. I would like to book an appointment for ${{service}} at ${{selectedTimeSlot}}.`;
            const waUrl = "https://wa.me/{clean_phone_digits}?text=" + encodeURIComponent(msg);
            window.open(waUrl, '_blank');
        }}

        function toggleTheme() {{
            const htmlEl = document.documentElement;
            const currentTheme = htmlEl.getAttribute('data-theme');
            const nextTheme = currentTheme === 'light' ? 'dark' : 'light';
            htmlEl.setAttribute('data-theme', nextTheme);
            document.getElementById('themeIcon').textContent = nextTheme === 'light' ? '🌙' : '☀️';
            document.getElementById('themeLabel').textContent = nextTheme === 'light' ? 'Dark Mode' : 'Light Mode';
        }}
    </script>
    {inspo_badge_html}
</body>
</html>
"""
    return html

if __name__ == "__main__":
    sample = {
        'name': 'Aesthetic Advanced Dental',
        'city': 'Koramangala, Bengaluru',
        'niche': 'Dental & Aesthetic Clinics',
        'domain': 'aestheticadvanceddental.com',
        'phone': '+91 86603 51505'
    }
    out = generate_mockup_html(sample)
    print("Mockup generation test successful! Length:", len(out))
