"""
Lead Hunter Agent - Modern Luxury Mockup Preview Generator
Generates an interactive, award-winning luxury redesign preview for any prospective business.
Tailored for Indian Metros (Bengaluru) & Global targets with realistic INR pricing and WhatsApp booking.
"""
import urllib.parse

def generate_mockup_html(lead: dict) -> str:
    name = lead.get('name') or 'Luxe Studio'
    city = lead.get('city') or 'Bangalore, Karnataka'
    niche = lead.get('niche') or 'Luxury Salons & Spas'
    phone = lead.get('phone') or '+91 80986 71563'
    domain = lead.get('domain') or 'business.com'
    
    niche_lower = niche.lower()
    
    # 1. Curated Luxury Photography & Content Matrix
    if any(k in niche_lower for k in ['salon', 'hair', 'spa', 'beauty', 'bridal', 'makeover', 'lash', 'nail', 'aesthet']):
        accent_color = "#e11d48"
        accent_glow = "rgba(225, 29, 72, 0.35)"
        gold_accent = "#d4af37"
        hero_img = "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1200&q=80"
        badge = f"Bengaluru's Premier Luxury Sanctuary • {city}"
        headline = f"Redefining Beauty, Hair & Radiance in {city}"
        subhead = "Experience bespoke styling, French balayage, and clinical skincare in a serene boutique haven. Book directly on WhatsApp without third-party fees."
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
    elif any(k in niche_lower for k in ['dent', 'ortho', 'smile', 'clinic', 'derma', 'physio', 'health']):
        accent_color = "#0284c7"
        accent_glow = "rgba(2, 132, 199, 0.35)"
        gold_accent = "#38bdf8"
        hero_img = "https://images.unsplash.com/photo-1629909613654-28e377c37b09?auto=format&fit=crop&w=1200&q=80"
        badge = f"Painless Digital Healthcare & Aesthetics • {city}"
        headline = f"World-Class Dentistry & Smile Artistry in {city}"
        subhead = "Experience pain-free treatments, 3D digital smile scans, and compassionate care designed around your comfort. Transparent upfront pricing."
        services = [
            {
                "title": "3D Digital Smile Makeover & Veneers",
                "desc": "Precision computer-designed porcelain veneers and ceramic crowns for a luminous, symmetrical smile.",
                "price": "₹4,999",
                "duration": "Comprehensive Scan",
                "img": "https://images.unsplash.com/photo-1588776814546-1ffcf47267a5?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Laser Teeth Whitening & Deep Hygiene",
                "desc": "Advanced cool-light laser bleaching removing decades of stains in a single 45-minute painless session.",
                "price": "₹2,999",
                "duration": "45 Mins",
                "img": "https://images.unsplash.com/photo-1606811841689-23dfddce3e95?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Clear Aligners & Invisible Orthodontics",
                "desc": "Virtually undetectable custom aligners designed with zero metal brackets. Eat and smile freely.",
                "price": "₹24,999",
                "duration": "EMI Available",
                "img": "https://images.unsplash.com/photo-1598256989800-fe5f95da9787?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Dr. Karthik Sundaram", "Whitefield, Bengaluru", "Painless root canal and flawless crown fit. The modern clinic and WhatsApp appointments make life so easy.", 5),
            ("Sneha Hegde", "Jayanagar, Bengaluru", "Got my teeth whitened before an overseas conference. 4 shades lighter in 40 minutes with zero sensitivity!", 5),
            ("Arjun Nair", "Indiranagar, Bengaluru", "The clear aligners process was explained clearly with 3D visuals. Highly recommended doctor.", 5)
        ]
    elif any(k in niche_lower for k in ['restaurant', 'cafe', 'bistro', 'dining', 'bakery', 'food']):
        accent_color = "#f59e0b"
        accent_glow = "rgba(245, 158, 11, 0.35)"
        gold_accent = "#fbbf24"
        hero_img = "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=80"
        badge = f"Artisanal Culinary Destination • {city}"
        headline = f"Exquisite Dining & Crafted Flavors in {city}"
        subhead = "Fresh seasonal ingredients, hand-tossed artisan recipes, and bespoke mixology. Reserve your private dining table instantly."
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
    else:
        # General / Architecture / High-Ticket Contractors / Home Services
        accent_color = "#10b981"
        accent_glow = "rgba(16, 185, 129, 0.35)"
        gold_accent = "#34d399"
        hero_img = "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?auto=format&fit=crop&w=1200&q=80"
        badge = f"Top-Rated Quality & Certified Excellence • {city}"
        headline = f"Trusted & Reliable {niche} in {city}"
        subhead = f"Delivering unmatched craftsmanship, transparent upfront estimates, and 5-star customer satisfaction across {city}. Fast turnaround guaranteed."
        services = [
            {
                "title": "Complete Turnkey Project Execution",
                "desc": "Full-scale modern design, premium verified materials, and dedicated supervisor from start to handover.",
                "price": "₹4,999 / Scope",
                "duration": "Guaranteed Timeline",
                "img": "https://images.unsplash.com/photo-1581094794329-c8112a89af12?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Rapid Repairs & Priority Diagnostic",
                "desc": "Swift same-day troubleshooting, detailed photographic evaluation, and zero hidden inspection charges.",
                "price": "₹1,499",
                "duration": "Same-Day Slot",
                "img": "https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=600&q=80"
            },
            {
                "title": "Free Structural Evaluation & 3D Quote",
                "desc": "Comprehensive site inspection with transparent material pricing and custom architectural rendering.",
                "price": "Free Estimate",
                "duration": "Zero Obligation",
                "img": "https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=600&q=80"
            }
        ]
        reviews = [
            ("Ramesh Chandran", "Bengaluru", "Super transparent pricing and punctual team. Booked inspection via WhatsApp and they arrived on time.", 5),
            ("Siddharth Menon", "Indiranagar", "Replaced my old clunky setup with clean modern work. Best contractor experience in Bengaluru.", 5),
            ("Meera Krishnan", "Whitefield", "Professional, courteous, and no hidden charges. Highly recommend their services.", 5)
        ]

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
                        <span>Book Slot</span>
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

    # WhatsApp Direct Link for Claiming
    wa_claim_text = urllib.parse.quote(f"Hi Ruban! I saw the modern website redesign concept for {name} ({city}) and want to claim the ₹2,999 Starter Redesign Package.")
    wa_claim_url = f"https://wa.me/918098671563?text={wa_claim_text}"

    # WhatsApp Customer Booking URL
    wa_cust_text = urllib.parse.quote(f"Hello {name}! I would like to book an appointment for your services in {city}.")
    wa_cust_url = f"https://wa.me/{phone.replace('+', '').replace(' ', '').replace('-', '')}?text={wa_cust_text}" if phone else "#booking"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} — Bespoke Modern Experience</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-canvas: #090b10;
            --bg-surface: #10141d;
            --bg-card: #151b27;
            --border-hairline: rgba(255, 255, 255, 0.08);
            --border-glow: {accent_glow};
            --accent: {accent_color};
            --gold: {gold_accent};
            --text-white: #f8fafc;
            --text-muted: #94a3b8;
            --text-subtle: #64748b;
            --radius-md: 12px;
            --radius-lg: 20px;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; scroll-behavior: smooth; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background: var(--bg-canvas);
            color: var(--text-white);
            line-height: 1.6;
            overflow-x: hidden;
            -webkit-font-smoothing: antialiased;
        }}

        /* 1. Designer Launchpad Sticky Header */
        .ruban-designer-bar {{
            background: rgba(15, 10, 25, 0.96);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(225, 29, 72, 0.3);
            color: #f1f5f9;
            padding: 10px 24px;
            font-size: 13px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 10000;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
        }}
        .designer-info {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
        }}
        .tag-concept {{
            background: #e11d48;
            color: #fff;
            padding: 3px 9px;
            border-radius: 999px;
            font-weight: 700;
            font-size: 11px;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}
        .designer-cta-group {{
            display: flex;
            align-items: center;
            gap: 12px;
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
            box-shadow: 0 2px 10px rgba(16, 185, 129, 0.35);
            transition: all 0.2s;
        }}
        .btn-claim-package:hover {{ transform: translateY(-1px); background: #059669; }}
        .btn-view-portfolio {{
            background: rgba(255,255,255,0.08);
            border: 1px solid var(--border-hairline);
            color: #fff;
            padding: 6px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }}
        .btn-view-portfolio:hover {{ background: rgba(255,255,255,0.15); }}

        /* 2. Brand Luxury Navbar */
        .site-header {{
            background: rgba(16, 20, 29, 0.75);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--border-hairline);
            padding: 16px 40px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 45px;
            z-index: 999;
        }}
        .brand-logo {{
            font-family: 'Space Grotesk', sans-serif;
            font-size: 21px;
            font-weight: 700;
            color: #fff;
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
        .nav-menu a:hover {{ color: #fff; }}
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
            padding: 80px 40px 100px;
            max-width: 1400px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 1.15fr 0.85fr;
            gap: 60px;
            align-items: center;
        }}
        .hero-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--border-hairline);
            padding: 8px 18px;
            border-radius: 9999px;
            font-size: 13px;
            font-weight: 600;
            color: var(--gold);
            margin-bottom: 24px;
        }}
        .hero-title {{
            font-size: 52px;
            font-weight: 800;
            line-height: 1.12;
            letter-spacing: -0.03em;
            margin-bottom: 22px;
            color: #fff;
        }}
        .hero-title span {{
            background: linear-gradient(135deg, #fff 40%, var(--text-muted) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .hero-sub {{
            font-size: 18px;
            color: var(--text-muted);
            line-height: 1.6;
            margin-bottom: 34px;
            max-width: 600px;
        }}
        .hero-btn-row {{
            display: flex;
            gap: 16px;
            align-items: center;
            margin-bottom: 40px;
        }}
        .btn-hero-primary {{
            background: var(--accent);
            color: #fff;
            padding: 15px 32px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 16px;
            text-decoration: none;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            box-shadow: 0 4px 20px var(--border-glow);
            transition: all 0.2s;
        }}
        .btn-hero-primary:hover {{ transform: translateY(-2px); opacity: 0.95; }}
        .btn-hero-secondary {{
            background: rgba(255,255,255,0.05);
            border: 1px solid var(--border-hairline);
            color: #fff;
            padding: 15px 26px;
            border-radius: 12px;
            font-weight: 600;
            font-size: 16px;
            text-decoration: none;
            transition: all 0.2s;
        }}
        .btn-hero-secondary:hover {{ background: rgba(255,255,255,0.1); }}

        .trust-strip {{
            display: flex;
            gap: 28px;
            padding-top: 28px;
            border-top: 1px solid var(--border-hairline);
            flex-wrap: wrap;
        }}
        .trust-item {{
            font-size: 13px;
            font-weight: 600;
            color: var(--text-white);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .trust-icon {{
            color: #10b981;
            font-weight: 900;
        }}

        /* Interactive Booking Console Card */
        .booking-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            border-radius: var(--radius-lg);
            padding: 36px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.5);
            position: relative;
        }}
        .booking-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0; height: 3px;
            background: linear-gradient(90deg, var(--accent), var(--gold));
            border-top-left-radius: var(--radius-lg);
            border-top-right-radius: var(--radius-lg);
        }}
        .booking-card h3 {{
            font-size: 22px;
            font-weight: 800;
            margin-bottom: 6px;
        }}
        .booking-card p {{
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 24px;
        }}
        .booking-field {{
            margin-bottom: 18px;
        }}
        .booking-field label {{
            display: block;
            font-size: 12px;
            font-weight: 700;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 8px;
        }}
        .booking-select, .booking-input {{
            width: 100%;
            background: var(--bg-card);
            border: 1px solid var(--border-hairline);
            color: #fff;
            padding: 13px 16px;
            border-radius: var(--radius-md);
            font-size: 14px;
            outline: none;
            font-family: inherit;
        }}
        .booking-select:focus, .booking-input:focus {{
            border-color: var(--accent);
        }}
        .time-slot-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            margin-top: 8px;
        }}
        .time-pill {{
            background: var(--bg-card);
            border: 1px solid var(--border-hairline);
            color: var(--text-muted);
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
            padding: 15px;
            border-radius: var(--radius-md);
            font-size: 15px;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            margin-top: 24px;
            transition: all 0.2s;
            box-shadow: 0 4px 16px rgba(16, 185, 129, 0.3);
        }}
        .btn-confirm-wa:hover {{
            background: #059669;
            transform: translateY(-1px);
        }}

        /* 4. Transformation Showcase (Before vs Ruban Modern) */
        .comparison-section {{
            max-width: 1300px;
            margin: 40px auto 80px;
            padding: 0 40px;
        }}
        .section-header {{
            text-align: center;
            margin-bottom: 50px;
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
            font-size: 38px;
            font-weight: 800;
            letter-spacing: -0.02em;
            margin-bottom: 12px;
        }}
        .section-header p {{
            font-size: 16px;
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
            padding: 36px;
            position: relative;
        }}
        .comp-card.old {{
            background: rgba(239, 68, 68, 0.04);
            border: 1px solid rgba(239, 68, 68, 0.25);
        }}
        .comp-card.new {{
            background: rgba(16, 185, 129, 0.05);
            border: 1px solid rgba(16, 185, 129, 0.35);
            box-shadow: 0 10px 40px rgba(16, 185, 129, 0.08);
        }}
        .comp-badge {{
            font-size: 12px;
            font-weight: 700;
            padding: 4px 12px;
            border-radius: 999px;
            display: inline-block;
            margin-bottom: 16px;
        }}
        .comp-badge.old-b {{ background: rgba(239, 68, 68, 0.2); color: #f87171; }}
        .comp-badge.new-b {{ background: rgba(16, 185, 129, 0.2); color: #34d399; }}
        .comp-card h3 {{ font-size: 24px; font-weight: 700; margin-bottom: 16px; }}
        .comp-list {{ list-style: none; }}
        .comp-list li {{
            font-size: 14px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .icon-cross {{ color: #ef4444; font-weight: 900; }}
        .icon-check {{ color: #10b981; font-weight: 900; }}

        /* 5. Services Grid */
        .services-section {{
            max-width: 1300px;
            margin: 0 auto 90px;
            padding: 0 40px;
        }}
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 28px;
        }}
        .luxury-card {{
            background: var(--bg-surface);
            border: 1px solid var(--border-hairline);
            border-radius: var(--radius-lg);
            overflow: hidden;
            transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            display: flex;
            flex-direction: column;
        }}
        .luxury-card:hover {{
            transform: translateY(-6px);
            border-color: var(--border-glow);
            box-shadow: 0 15px 35px rgba(0,0,0,0.4);
        }}
        .card-img-wrap {{
            height: 220px;
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
            background: rgba(9, 11, 16, 0.88);
            backdrop-filter: blur(8px);
            border: 1px solid var(--border-hairline);
            color: #fff;
            padding: 5px 12px;
            border-radius: 999px;
            font-size: 13px;
            font-weight: 700;
        }}
        .card-content {{
            padding: 26px;
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
            font-size: 20px;
            font-weight: 700;
            margin-bottom: 10px;
            color: #fff;
        }}
        .card-content p {{
            font-size: 14px;
            color: var(--text-muted);
            margin-bottom: 22px;
            flex-grow: 1;
        }}
        .btn-card-book {{
            background: var(--bg-card);
            border: 1px solid var(--border-hairline);
            color: #fff;
            padding: 10px 18px;
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
        }}

        /* 6. Social Proof / Google Reviews */
        .reviews-section {{
            max-width: 1300px;
            margin: 0 auto 100px;
            padding: 0 40px;
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
            padding: 26px;
        }}
        .review-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 14px;
        }}
        .review-stars {{ color: #f59e0b; font-size: 15px; letter-spacing: 2px; }}
        .verified-pill {{ font-size: 11px; color: #10b981; font-weight: 600; }}
        .review-body {{ font-size: 14px; color: var(--text-white); margin-bottom: 20px; font-style: italic; }}
        .reviewer-meta {{ display: flex; align-items: center; gap: 12px; }}
        .reviewer-avatar {{
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: var(--accent);
            color: #fff;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 700;
            font-size: 15px;
        }}
        .reviewer-name {{ font-size: 14px; font-weight: 700; color: #fff; }}
        .reviewer-loc {{ font-size: 12px; color: var(--text-subtle); }}

        /* 7. Footer */
        footer {{
            background: #06080d;
            border-top: 1px solid var(--border-hairline);
            padding: 50px 40px;
            text-align: center;
        }}
        footer p {{ font-size: 14px; color: var(--text-muted); }}
        footer strong {{ color: #fff; }}

        /* Floating WhatsApp Action Pill */
        .floating-wa-btn {{
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #25d366;
            color: #fff;
            padding: 12px 20px;
            border-radius: 9999px;
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.45);
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
            .hero-section {{ grid-template-columns: 1fr; padding: 40px 24px; }}
            .comparison-grid {{ grid-template-columns: 1fr; }}
            .services-grid {{ grid-template-columns: 1fr; }}
            .reviews-grid {{ grid-template-columns: 1fr; }}
            .site-header {{ padding: 14px 20px; }}
            .nav-menu {{ display: none; }}
            .hero-title {{ font-size: 38px; }}
        }}
    </style>
</head>
<body>

    <!-- 1. Top Designer Banner -->
    <aside class="ruban-designer-bar">
        <div class="designer-info">
            <span class="tag-concept">Bespoke UI Redesign</span>
            <span>Crafted for <strong>{name}</strong> by <strong>Ruban Velankanni</strong> (Bengaluru)</span>
            <span style="color: var(--gold); font-weight: 700;">• 3-Day Turnaround • Starter Offer: ₹2,999</span>
        </div>
        <div class="designer-cta-group">
            <a href="{wa_claim_url}" target="_blank" class="btn-claim-package">
                <span>Claim This Redesign (WhatsApp)</span>
            </a>
            <a href="https://portfolio.rvsmps.store" target="_blank" class="btn-view-portfolio">
                <span>View Ruban's Portfolio</span>
            </a>
        </div>
    </aside>

    <!-- 2. Brand Luxury Navbar -->
    <header class="site-header">
        <a href="#" class="brand-logo">
            <span class="brand-dot"></span>
            <span>{name}</span>
        </a>
        <nav>
            <ul class="nav-menu">
                <li><a href="#services">Treatment Menu</a></li>
                <li><a href="#comparison">Why Redesign</a></li>
                <li><a href="#reviews">Google Reviews</a></li>
                <li><a href="#booking">Book Appointment</a></li>
            </ul>
        </nav>
        <div class="header-actions">
            <a href="{wa_cust_url}" target="_blank" class="btn-whatsapp-pill">
                <span class="pulse-dot"></span>
                <span>Book on WhatsApp</span>
            </a>
        </div>
    </header>

    <main>
        <!-- 3. Hero Section -->
        <section class="hero-section">
            <div>
                <div class="hero-badge">
                    <span>★ 4.9 Rating (240+ Google Reviews)</span> • <span>{badge}</span>
                </div>
                <h1 class="hero-title"><span>{headline}</span></h1>
                <p class="hero-sub">{subhead}</p>

                <div class="hero-btn-row">
                    <a href="#booking" class="btn-hero-primary">
                        <span>Book Instant Slot</span>
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                    </a>
                    <a href="{wa_cust_url}" target="_blank" class="btn-hero-secondary">
                        <span>Chat on WhatsApp</span>
                    </a>
                </div>

                <div class="trust-strip">
                    <div class="trust-item"><span class="trust-icon">✓</span> Direct WhatsApp Confirmation</div>
                    <div class="trust-item"><span class="trust-icon">✓</span> Zero Middleman Aggregator Cuts</div>
                    <div class="trust-item"><span class="trust-icon">✓</span> Certified Master Specialists</div>
                </div>
            </div>

            <!-- Interactive Booking Console Card -->
            <div class="booking-card" id="booking">
                <h3>Reserve Your VIP Slot</h3>
                <p>Select your treatment, date, and preferred time slot for instant WhatsApp booking.</p>

                <form onsubmit="handleCustomerBooking(event)">
                    <div class="booking-field">
                        <label>Select Treatment / Service</label>
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
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.04 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.02L7.55 18.84L4.44 19.66L5.27 16.63L5.07 16.31C4.24 15 3.81 13.48 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
                        <span>Confirm Slot on WhatsApp →</span>
                    </button>
                </form>
            </div>
        </section>

        <!-- 4. Before & After Transformation Section -->
        <section class="comparison-section" id="comparison">
            <div class="section-header">
                <span class="section-tag">High-Conversion UX Upgrade</span>
                <h2>Why {name} Needs This Upgrade</h2>
                <p>See the direct difference between the current website and Ruban's modern redesign.</p>
            </div>

            <div class="comparison-grid">
                <div class="comp-card old">
                    <span class="comp-badge old-b">Current Clunky Website ({domain})</span>
                    <h3>The Friction Bottleneck</h3>
                    <ul class="comp-list">
                        <li><span class="icon-cross">✗</span> Slow load speed drives away 65% of mobile visitors</li>
                        <li><span class="icon-cross">✗</span> Missing direct 1-tap WhatsApp booking button</li>
                        <li><span class="icon-cross">✗</span> Buried reviews and no clear service pricing menu</li>
                        <li><span class="icon-cross">✗</span> Paying 20-25% aggregator commission fees on third-party apps</li>
                    </ul>
                </div>

                <div class="comp-card new">
                    <span class="comp-badge new-b">Ruban Modern Architecture (Concept)</span>
                    <h3>The High-Conversion Engine</h3>
                    <ul class="comp-list">
                        <li><span class="icon-check">✓</span> Instant &lt;1.0s mobile load speed on ultra-fast edge CDN</li>
                        <li><span class="icon-check">✓</span> 1-Click WhatsApp appointment booking prefilled in seconds</li>
                        <li><span class="icon-check">✓</span> Clear treatment cards with upfront INR pricing and star badges</li>
                        <li><span class="icon-check">✓</span> 100% direct client ownership with ZERO commission to aggregators</li>
                    </ul>
                </div>
            </div>
        </section>

        <!-- 5. Treatment Menu / Services -->
        <section class="services-section" id="services">
            <div class="section-header">
                <span class="section-tag">Signature Experiences</span>
                <h2>Featured Treatment Menu</h2>
                <p>Crafted for aesthetic perfection, clinical safety, and lasting satisfaction in {city}.</p>
            </div>

            <div class="services-grid">
                {services_cards_html}
            </div>
        </section>

        <!-- 6. Google Verified Reviews -->
        <section class="reviews-section" id="reviews">
            <div class="section-header">
                <span class="section-tag">Verified Proof</span>
                <h2>Loved by Clients Across {city}</h2>
                <p>Over 240+ five-star verified Google reviews celebrating our quality.</p>
            </div>

            <div class="reviews-grid">
                {reviews_html}
            </div>
        </section>
    </main>

    <!-- Floating WhatsApp Action -->
    <a href="{wa_claim_url}" target="_blank" class="floating-wa-btn">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.04 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.02L7.55 18.84L4.44 19.66L5.27 16.63L5.07 16.31C4.24 15 3.81 13.48 3.81 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
        <span>Claim ₹2,999 Redesign (Ruban)</span>
    </a>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 <strong>{name}</strong> • Designed with conversion architecture by <strong>Ruban Velankanni (Bengaluru)</strong></p>
        <p style="margin-top: 8px; font-size: 12px; color: var(--text-subtle);">This interactive preview demonstrates modern high-converting UI engineering.</p>
    </footer>

    <script>
        let selectedTimeSlot = "11:00 AM";

        function selectTime(el) {{
            document.querySelectorAll('.time-pill').forEach(p => p.classList.remove('active'));
            el.classList.add('active');
            selectedTimeSlot = el.innerText;
        }}

        function selectServiceForBooking(title, price) {{
            const sel = document.getElementById('serviceSelect');
            for (let i = 0; i < sel.options.length; i++) {{
                if (sel.options[i].text.includes(title)) {{
                    sel.selectedIndex = i;
                    break;
                }}
            }}
            document.getElementById('booking').scrollIntoView({{ behavior: 'smooth' }});
        }}

        function handleCustomerBooking(e) {{
            e.preventDefault();
            const service = document.getElementById('serviceSelect').value;
            const name = document.getElementById('custName').value;
            const text = `Hello {name}! My name is ${{name}}. I would like to book an appointment for: ${{service}} at ${{selectedTimeSlot}} in {city}.`;
            const waUrl = `https://wa.me/{phone.replace('+', '').replace(' ', '').replace('-', '')}?text=${{encodeURIComponent(text)}}`;
            window.open(waUrl, '_blank');
        }}
    </script>
</body>
</html>
"""
    return html

if __name__ == "__main__":
    sample = {
        'name': 'Luxe Hair & Spa Studio',
        'city': 'Indiranagar, Bangalore',
        'niche': 'Luxury Salons & Spas',
        'phone': '+91 80986 71563',
        'domain': 'luxehairbangalore.com'
    }
    html = generate_mockup_html(sample)
    print("Mockup generated successfully! Length:", len(html))
