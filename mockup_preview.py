"""
Lead Hunter Agent - Mockup Preview Generator Module
Generates an interactive, responsive modern UI redesign preview for any targeted business.
"""

def generate_mockup_html(lead: dict) -> str:
    name = lead.get('name', 'Elite Services')
    city = lead.get('city', 'Austin, TX')
    niche = lead.get('niche', 'Home Services')
    phone = lead.get('phone') or '(512) 800-4123'
    domain = lead.get('domain', 'website.com')
    
    # Industry tailored content
    niche_lower = niche.lower()
    if 'roof' in niche_lower:
        badge = "Austin's Premier Roofing & Restoration"
        headline = f"Reliable Roofing & Repairs in {city}"
        subhead = "Protect your home with certified craftsmen, lifetime warranties, and honest upfront pricing. Fast storm damage inspections."
        services = [
            ("Residential Roof Replacement", "Asphalt shingles, metal roofing, and tile installations backed by manufacturer warranties."),
            ("Emergency Leak Repairs", "Rapid-response leak detection and emergency tarping to safeguard your home."),
            ("Free Roof Inspection", "Thorough 21-point structural evaluation with detailed photo report and no obligation.")
        ]
        accent_color = "#f59e0b"
    elif 'dent' in niche_lower or 'ortho' in niche_lower:
        badge = "Compassionate, World-Class Dentistry"
        headline = f"Gentle Dental Care for You & Your Family in {city}"
        subhead = "Experience painless treatments, state-of-the-art dental technology, and personalized care designed around your comfort."
        services = [
            ("Cosmetic Smile Makeovers", "Porcelain veneers, professional teeth whitening, and Invisalign clear aligners."),
            ("Preventative Care & Cleanings", "Comprehensive exams, gentle ultrasonic cleanings, and digital low-radiation X-rays."),
            ("Restorative & Dental Implants", "Permanent natural-looking tooth replacements with maximum durability.")
        ]
        accent_color = "#0ea5e9"
    elif 'spa' in niche_lower or 'aesthet' in niche_lower:
        badge = "Luxury Aesthetic Medical Spa"
        headline = f"Rediscover Your Natural Radiance in {city}"
        subhead = "Physician-led non-invasive aesthetic treatments, laser therapies, and tailored skincare in a relaxing boutique atmosphere."
        services = [
            ("Botox & Dermal Fillers", "Artfully placed injectables that smooth lines while keeping your natural expressions."),
            ("Advanced Laser Skin Resurfacing", "Erase sun damage, acne scars, and uneven texture with zero surgical downtime."),
            ("Medical-Grade Hydrafacials", "Deep pore cleansing, exfoliation, and hydration infusion for an instant glow.")
        ]
        accent_color = "#ec4899"
    else:
        badge = f"Top-Rated {niche} in {city}"
        headline = f"Exceptional {niche} in {city}"
        subhead = "Delivering unmatched quality, transparent pricing, and 5-star customer satisfaction for local homeowners and businesses."
        services = [
            ("Complete Service & Installation", "Full-scale project execution with high-grade materials and experienced technicians."),
            ("Maintenance & Rapid Support", "Routine tune-ups and swift emergency troubleshooting to prevent costly downtime."),
            ("Free Detailed Consultation", "Transparent upfront quotes with zero hidden fees and custom project timelines.")
        ]
        accent_color = "#3b82f6"

    services_html = ""
    for title, desc in services:
        services_html += f"""
        <div class="service-card">
            <div class="service-icon" style="background: {accent_color}1a; color: {accent_color};">✦</div>
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Redesign Preview: {name}</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --primary: #0f172a;
            --accent: {accent_color};
            --text-dark: #0f172a;
            --text-muted: #64748b;
            --bg-light: #f8fafc;
            --white: #ffffff;
            --border: #e2e8f0;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
            background: var(--bg-light);
            color: var(--text-dark);
            line-height: 1.6;
        }}
        /* Designer Banner */
        .preview-banner {{
            background: #1e1b4b;
            color: #c7d2fe;
            padding: 10px 20px;
            font-size: 13px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            position: sticky;
            top: 0;
            z-index: 9999;
            box-shadow: 0 2px 10px rgba(0,0,0,0.15);
        }}
        .preview-banner strong {{ color: #ffffff; }}
        .preview-badge {{
            background: #4f46e5;
            color: #fff;
            padding: 3px 8px;
            border-radius: 4px;
            font-weight: 600;
            font-size: 11px;
            margin-right: 8px;
        }}
        .btn-hire {{
            background: #ffffff;
            color: #1e1b4b;
            padding: 6px 14px;
            border-radius: 6px;
            text-decoration: none;
            font-weight: 700;
            font-size: 12px;
            transition: all 0.2s;
        }}
        .btn-hire:hover {{ background: #e0e7ff; }}

        /* Top Bar */
        .top-bar {{
            background: var(--primary);
            color: #94a3b8;
            font-size: 13px;
            padding: 8px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .top-bar a {{ color: #ffffff; text-decoration: none; font-weight: 600; }}

        /* Header / Nav */
        header {{
            background: var(--white);
            padding: 18px 30px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
        }}
        .logo {{
            font-size: 22px;
            font-weight: 800;
            color: var(--primary);
            letter-spacing: -0.5px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .logo-dot {{ width: 10px; height: 10px; border-radius: 50%; background: var(--accent); }}
        nav ul {{ display: flex; list-style: none; gap: 24px; }}
        nav a {{ text-decoration: none; color: var(--text-dark); font-weight: 600; font-size: 15px; }}
        .nav-cta {{
            background: var(--accent);
            color: var(--primary);
            padding: 10px 20px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
        }}

        /* Hero */
        .hero {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 70px 24px;
            display: grid;
            grid-template-columns: 1.2fr 0.8fr;
            gap: 50px;
            align-items: center;
        }}
        .hero-tag {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: #ffffff;
            border: 1px solid var(--border);
            padding: 6px 14px;
            border-radius: 30px;
            font-size: 13px;
            font-weight: 700;
            color: var(--text-dark);
            margin-bottom: 18px;
        }}
        .hero h1 {{
            font-size: 48px;
            line-height: 1.15;
            letter-spacing: -1.2px;
            font-weight: 800;
            margin-bottom: 20px;
            color: var(--primary);
        }}
        .hero p {{
            font-size: 18px;
            color: var(--text-muted);
            margin-bottom: 30px;
        }}
        .hero-actions {{ display: flex; gap: 14px; align-items: center; margin-bottom: 35px; }}
        .btn-primary {{
            background: var(--primary);
            color: #ffffff;
            padding: 14px 28px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 700;
            font-size: 16px;
            transition: all 0.2s;
        }}
        .btn-primary:hover {{ opacity: 0.92; transform: translateY(-1px); }}
        .btn-secondary {{
            background: #ffffff;
            border: 1px solid var(--border);
            color: var(--text-dark);
            padding: 14px 24px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 700;
            font-size: 16px;
        }}
        .trust-badges {{
            display: flex;
            gap: 20px;
            padding-top: 20px;
            border-top: 1px solid var(--border);
        }}
        .trust-item {{
            font-size: 13px;
            font-weight: 600;
            color: var(--text-dark);
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        /* Hero Card Form */
        .quote-card {{
            background: var(--white);
            padding: 34px;
            border-radius: 18px;
            box-shadow: 0 15px 35px -5px rgba(0,0,0,0.06);
            border: 1px solid var(--border);
        }}
        .quote-card h3 {{ font-size: 22px; margin-bottom: 8px; font-weight: 800; }}
        .quote-card p {{ font-size: 14px; color: var(--text-muted); margin-bottom: 20px; }}
        .form-group {{ margin-bottom: 14px; }}
        .form-group input, .form-group select {{
            width: 100%;
            padding: 12px 14px;
            border: 1px solid var(--border);
            border-radius: 8px;
            font-size: 14px;
            outline: none;
            font-family: inherit;
        }}
        .btn-submit {{
            width: 100%;
            padding: 14px;
            background: var(--primary);
            color: #fff;
            border: none;
            border-radius: 8px;
            font-weight: 700;
            font-size: 15px;
            cursor: pointer;
        }}

        /* Services */
        .services-section {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 70px 24px;
        }}
        .section-header {{ text-align: center; margin-bottom: 45px; }}
        .section-header h2 {{ font-size: 34px; font-weight: 800; margin-bottom: 12px; }}
        .section-header p {{ color: var(--text-muted); font-size: 17px; }}
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 24px;
        }}
        .service-card {{
            background: var(--white);
            padding: 30px;
            border-radius: 14px;
            border: 1px solid var(--border);
            transition: all 0.2s;
        }}
        .service-card:hover {{ transform: translateY(-4px); box-shadow: 0 10px 25px -5px rgba(0,0,0,0.08); }}
        .service-icon {{
            width: 44px;
            height: 44px;
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            margin-bottom: 18px;
        }}
        .service-card h3 {{ font-size: 19px; margin-bottom: 10px; font-weight: 700; }}
        .service-card p {{ font-size: 14px; color: var(--text-muted); line-height: 1.5; }}

        /* Footer */
        footer {{
            background: var(--primary);
            color: #94a3b8;
            padding: 40px 24px;
            text-align: center;
            font-size: 14px;
            border-top: 1px solid #1e293b;
        }}
        footer strong {{ color: #ffffff; }}

        @media (max-width: 900px) {{
            .hero {{ grid-template-columns: 1fr; padding: 40px 20px; }}
            .services-grid {{ grid-template-columns: 1fr; }}
            nav {{ display: none; }}
            .hero h1 {{ font-size: 34px; }}
        }}
    </style>
</head>
<body>

    <div class="preview-banner">
        <div>
            <span class="preview-badge">MODERN REDESIGN CONCEPT</span>
            Crafted for <strong>{name}</strong> by <strong>Ruban (Website & UI Designer)</strong>
        </div>
        <div>
            <a href="mailto:rubanvelankanni2003@gmail.com?subject=Website Redesign Consultation for {name}" class="btn-hire">Contact Ruban to Launch This Site</a>
        </div>
    </div>

    <div class="top-bar">
        <div>📍 Serving homeowners and businesses across {city}</div>
        <div>Need Immediate Help? <a href="tel:{phone}">📞 {phone}</a></div>
    </div>

    <header>
        <div class="logo">
            <span class="logo-dot"></span>
            {name}
        </div>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#reviews">Reviews</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
        <a href="#quote" class="nav-cta">Get Free Estimate</a>
    </header>

    <main>
        <section class="hero">
            <div class="hero-content">
                <div class="hero-tag">
                    <span>★ 4.9 Rating (140+ Reviews)</span> • <span>{badge}</span>
                </div>
                <h1>{headline}</h1>
                <p>{subhead}</p>
                <div class="hero-actions">
                    <a href="#quote" class="btn-primary">Request a Free Quote</a>
                    <a href="tel:{phone}" class="btn-secondary">Call {phone}</a>
                </div>
                <div class="trust-badges">
                    <div class="trust-item">✓ Licensed & Insured</div>
                    <div class="trust-item">✓ 100% Satisfaction Guarantee</div>
                    <div class="trust-item">✓ Same-Day Estimates</div>
                </div>
            </div>

            <div class="quote-card" id="quote">
                <h3>Get Your Free Estimate</h3>
                <p>Fill out the quick form below and our team will get back to you within 30 minutes.</p>
                <form onsubmit="alert('Thank you! This is an interactive demo designed by Ruban.'); return false;">
                    <div class="form-group">
                        <input type="text" placeholder="Your Full Name" required>
                    </div>
                    <div class="form-group">
                        <input type="tel" placeholder="Phone Number" required>
                    </div>
                    <div class="form-group">
                        <select required>
                            <option value="">Select Service Needed...</option>
                            <option value="1">{services[0][0]}</option>
                            <option value="2">{services[1][0]}</option>
                            <option value="3">{services[2][0]}</option>
                        </select>
                    </div>
                    <button type="submit" class="btn-submit">Claim Your Free Quote →</button>
                </form>
            </div>
        </section>

        <section class="services-section" id="services">
            <div class="section-header">
                <h2>Our Core Services</h2>
                <p>Engineered for durability, aesthetic perfection, and lasting value in {city}.</p>
            </div>
            <div class="services-grid">
                {services_html}
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2026 <strong>{name}</strong>. All rights reserved. • Designed & Optimized for Conversions by <strong>Ruban</strong></p>
    </footer>

</body>
</html>
"""
    return html

if __name__ == "__main__":
    test_lead = {
        'name': 'Hargrove Roofing & Construction',
        'city': 'Austin, TX',
        'niche': 'Roofing Contractors',
        'phone': '(512) 555-0199',
        'domain': 'hargroveroofing.com'
    }
    with open("lead_hunter_agent/sample_mockup.html", "w", encoding="utf-8") as f:
        f.write(generate_mockup_html(test_lead))
    print("Generated sample mockup at lead_hunter_agent/sample_mockup.html")
