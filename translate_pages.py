#!/usr/bin/env python3
"""
Translate CBT pages to Spanish (es) and Portuguese (pt) using MyMemory API.
Translates critical SEO content: title, meta description, h1, h2s, first paragraphs.
Free API: 50000 chars/day with email parameter.
"""
import json, os, re, sys, time, urllib.request, urllib.error, urllib.parse

SEO_DIR = os.path.join(os.path.dirname(__file__), "seo")
API_URL = "https://api.mymemory.translated.net/get"
EMAIL = "cbt.toolkit@gmail.com"
MAX_CHARS = 4500  # MyMemory limit per request

PAGES = [
    "cbt-for-anxiety",
    "cbt-for-depression",
    "cbt-for-adhd",
    "cbt-for-ocd",
    "cbt-for-ptsd-trauma",
    "cbt-for-social-anxiety",
    "cbt-for-anger",
    "cbt-for-perfectionism",
    "cbt-for-procrastination",
    "cbt-for-burnout",
    "cbt-for-panic-attacks",
    "cbt-for-low-self-esteem",
    "cbt-for-stress",
    "cbt-for-bipolar",
    "cbt-for-eating-disorders",
    "cbt-for-imposter-syndrome",
    "cbt-for-body-image",
    "cbt-for-health-anxiety",
    "cbt-for-insomnia",
    "cbt-for-people-pleasing",
]

TARGETS = [("es", "Spanish"), ("pt", "Portuguese")]
LANG_NAMES = {"es": "Español", "pt": "Português"}


def translate(text, target="es"):
    """Translate text via MyMemory. Returns translated text or original on error."""
    text = text.strip()
    if not text or len(text) < 3:
        return text
    if len(text) > MAX_CHARS:
        text = text[:MAX_CHARS]

    # Clean text for URL encoding
    params = urllib.parse.urlencode({
        "q": text,
        "langpair": f"en|{target}",
        "de": EMAIL,
    })
    url = f"{API_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": "CBTToolkit/1.0"})

    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                status = data.get("responseStatus", "")
                if status == "200" or status == 200:
                    return data.get("responseData", {}).get("translatedText", text)
                else:
                    print(f"    API status: {status}")
                    return text
        except Exception as e:
            if attempt < 2:
                time.sleep(2 * (attempt + 1))
            else:
                return text
    return text


def translate_page(filepath, target_lang):
    """Create a translated version of a CBT page."""
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    base = os.path.basename(filepath).replace(".html", "")
    lang_name = LANG_NAMES.get(target_lang, target_lang)

    # 1. Update lang attribute
    html = re.sub(r'<html lang="en">', f'<html lang="{target_lang}">', html)

    # 2. Translate <title>
    title_match = re.search(r'<title>(.*?)</title>', html, re.DOTALL)
    if title_match:
        t = translate(title_match.group(1), target_lang)
        html = html.replace(title_match.group(0), f'<title>{t}</title>')

    # 3. Translate meta description
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.DOTALL)
    if desc_match:
        t = translate(desc_match.group(1), target_lang)
        html = html.replace(desc_match.group(0), f'<meta name="description" content="{t}"')

    # 4. Translate meta keywords
    kw_match = re.search(r'<meta name="keywords" content="(.*?)"', html, re.DOTALL)
    if kw_match:
        t = translate(kw_match.group(1), target_lang)
        html = html.replace(kw_match.group(0), f'<meta name="keywords" content="{t}"')

    # 5. Translate og:title and og:description
    for og_tag in ["og:title", "og:description", "twitter:title", "twitter:description"]:
        og_match = re.search(rf'<meta property="{og_tag}" content="(.*?)"', html, re.DOTALL)
        if og_match:
            t = translate(og_match.group(1), target_lang)
            html = html.replace(og_match.group(0), f'<meta property="{og_tag}" content="{t}"')

    # 6. Translate <h1>
    h1_match = re.search(r'<h1>(.*?)</h1>', html, re.DOTALL)
    if h1_match:
        t = translate(h1_match.group(1), target_lang)
        html = html.replace(h1_match.group(0), f'<h1>{t}</h1>')

    # 7. Translate hero <p>
    hero_p = re.search(r'(<div class="hero">.*?<p>)(.*?)(</p>)', html, re.DOTALL)
    if hero_p:
        t = translate(hero_p.group(2), target_lang)
        html = html.replace(hero_p.group(0), hero_p.group(1) + t + hero_p.group(3))

    # 8. Translate all <h2> tags
    for h2_match in re.finditer(r'<h2>(.*?)</h2>', html, re.DOTALL):
        original = h2_match.group(0)
        t = translate(h2_match.group(1), target_lang)
        html = html.replace(original, f'<h2>{t}</h2>', 1)

    # 9. Translate first <p class="lead"> if exists
    lead_match = re.search(r'(<p class="lead">)(.*?)(</p>)', html, re.DOTALL)
    if lead_match:
        t = translate(lead_match.group(2), target_lang)
        html = html.replace(lead_match.group(0), lead_match.group(1) + t + lead_match.group(3), 1)

    # 10. Translate first <p> in each card (up to 5 cards)
    card_count = 0
    for card_match in re.finditer(r'(<div class="card">.*?<p>)(.*?)(</p>)', html, re.DOTALL):
        if card_count >= 5:
            break
        original = card_match.group(0)
        t = translate(card_match.group(2), target_lang)
        replacement = card_match.group(1) + t + card_match.group(3)
        if original in html:
            html = html.replace(original, replacement, 1)
            card_count += 1

    # 11. Update canonical URL
    new_url = f"https://alexcoledev.github.io/cbt-toolkit/seo/{base}-{target_lang}.html"
    html = re.sub(
        r'<link rel="canonical" href="[^"]*">',
        f'<link rel="canonical" href="{new_url}">',
        html,
    )

    # 12. Add translation notice at top of body
    notice = (
        f'\n<div style="background:#fff5e7;border-bottom:2px solid #ed8936;padding:0.5rem 1rem;text-align:center;font-size:0.85rem;color:#744210;">'
        f'&#127760; Versión en {lang_name} &middot; '
        f'<a href="./{base}.html" style="color:#2b6cb0;">English version</a>'
        f'</div>\n'
    )
    html = html.replace("<body>", f"<body>{notice}", 1)

    # 13. Update JSON-LD datePublished
    today = time.strftime("%Y-%m-%d")
    html = re.sub(r'"datePublished": "[^"]*"', f'"datePublished": "{today}"', html)

    return html


def main():
    total_created = 0
    total_skipped = 0
    total_failed = 0

    for lang_code, lang_name in TARGETS:
        print(f"\n=== Translating to {lang_name} ({lang_code}) ===")
        for page in PAGES:
            src = os.path.join(SEO_DIR, page + ".html")
            dst = os.path.join(SEO_DIR, page + "-" + lang_code + ".html")

            if not os.path.exists(src):
                print(f"  SKIP (no source): {page}")
                total_skipped += 1
                continue
            if os.path.exists(dst):
                print(f"  SKIP (exists): {page}-{lang_code}")
                total_skipped += 1
                continue

            print(f"  {page} -> {lang_code}...", end="", flush=True)
            try:
                translated = translate_page(src, lang_code)
                if translated:
                    with open(dst, "w", encoding="utf-8") as f:
                        f.write(translated)
                    total_created += 1
                    print(f" OK ({len(translated)} bytes)")
                else:
                    total_failed += 1
                    print(" FAILED")
            except Exception as e:
                total_failed += 1
                print(f" ERROR: {str(e)[:60]}")

            time.sleep(0.5)  # be nice to MyMemory API

    print(f"\nCreated: {total_created} | Skipped: {total_skipped} | Failed: {total_failed}")


if __name__ == "__main__":
    main()
