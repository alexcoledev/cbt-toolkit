#!/usr/bin/env python3
"""
Wikipedia enrichment: inject 'What is [condition]?' sections into CBT pages.
Uses Wikipedia REST API (no auth). Idempotent — skips pages already enriched.
"""
import json, os, re, sys, time, urllib.request, urllib.error, urllib.parse

SEO_DIR = os.path.join(os.path.dirname(__file__), "seo")
API = "https://en.wikipedia.org/api/rest_v1/page/summary/{}"
MARKER = 'id="condition-overview"'

# filename (without .html) -> (Wikipedia title, display name)
MAP = {
    "cbt-for-adhd": ("Attention deficit hyperactivity disorder", "ADHD"),
    "cbt-for-anxiety": ("Anxiety", "Anxiety"),
    "cbt-for-anger": ("Anger", "Anger"),
    "cbt-for-anger-issues": ("Anger", "Anger Issues"),
    "cbt-for-arachnophobia": ("Arachnophobia", "Arachnophobia"),
    "cbt-for-astraphobia": ("Astraphobia", "Astraphobia"),
    "cbt-for-autism": ("Autism", "Autism"),
    "cbt-for-aviophobia": ("Aviophobia", "Fear of Flying"),
    "cbt-for-bipolar": ("Bipolar disorder", "Bipolar Disorder"),
    "cbt-for-body-dysmorphic-disorder": ("Body dysmorphic disorder", "Body Dysmorphic Disorder"),
    "cbt-for-body-image": ("Body image", "Body Image"),
    "cbt-for-burnout": ("Burnout (psychology)", "Burnout"),
    "cbt-for-chronic-fatigue-syndrome": ("Chronic fatigue syndrome", "Chronic Fatigue Syndrome"),
    "cbt-for-chronic-pain": ("Chronic pain", "Chronic Pain"),
    "cbt-for-claustrophobia": ("Claustrophobia", "Claustrophobia"),
    "cbt-for-codependency": ("Codependency", "Codependency"),
    "cbt-for-compulsive-buying": ("Oniomania", "Compulsive Buying"),
    "cbt-for-death-anxiety": ("Death anxiety (psychology)", "Death Anxiety"),
    "cbt-for-depression": ("Depression (mood)", "Depression"),
    "cbt-for-dissociation-depersonalization": ("Depersonalization", "Depersonalization & Dissociation"),
    "cbt-for-eating-disorders": ("Eating disorder", "Eating Disorders"),
    "cbt-for-excoriation-disorder": ("Excoriation disorder", "Excoriation Disorder (Skin Picking)"),
    "cbt-for-fear-of-flying": ("Aviophobia", "Fear of Flying"),
    "cbt-for-grief": ("Grief", "Grief"),
    "cbt-for-health-anxiety": ("Illness anxiety disorder", "Health Anxiety"),
    "cbt-for-hoarding": ("Hoarding disorder", "Hoarding"),
    "cbt-for-imposter-syndrome": ("Impostor syndrome", "Imposter Syndrome"),
    "cbt-for-insomnia": ("Insomnia", "Insomnia"),
    "cbt-for-intrusive-thoughts": ("Intrusive thought", "Intrusive Thoughts"),
    "cbt-for-low-self-esteem": ("Self-esteem", "Low Self-Esteem"),
    "cbt-for-ocd": ("Obsessive–compulsive disorder", "OCD"),
    "cbt-for-panic-attacks": ("Panic attack", "Panic Attacks"),
    "cbt-for-perfectionism": ("Perfectionism (psychology)", "Perfectionism"),
    "cbt-for-procrastination": ("Procrastination", "Procrastination"),
    "cbt-for-ptsd-trauma": ("Post-traumatic stress disorder", "PTSD"),
    "cbt-for-public-speaking-anxiety": ("Glossophobia", "Public Speaking Anxiety"),
    "cbt-for-self-criticism": ("Self-criticism", "Self-Criticism"),
    "cbt-for-separation-anxiety-disorder": ("Separation anxiety disorder", "Separation Anxiety Disorder"),
    "cbt-for-shame": ("Shame", "Shame"),
    "cbt-for-social-anxiety": ("Social anxiety disorder", "Social Anxiety"),
    "cbt-for-social-media-anxiety": ("Social media", "Social Media Anxiety"),
    "cbt-for-stress": ("Stress (psychology)", "Stress"),
    "cbt-for-substance-use": ("Substance use disorder", "Substance Use"),
    "cbt-for-test-anxiety": ("Test anxiety", "Test Anxiety"),
    "cbt-for-trichotillomania": ("Trichotillomania", "Trichotillomania (Hair Pulling)"),
    "cbt-for-trust-issues": ("Trust (social science)", "Trust Issues"),
    "cbt-for-sleep": ("Insomnia", "Sleep Problems"),
    "cbt-for-sleep-anxiety": ("Somniphobia", "Sleep Anxiety"),
    "cbt-for-relationship-anxiety": ("Relationship", "Relationship Anxiety"),
    "cbt-for-rejection-sensitivity": ("Rejection sensitive dysphoria", "Rejection Sensitivity"),
    "cbt-for-people-pleasing": ("People-pleasing", "People Pleasing"),
    "cbt-for-pet-loss": ("Grief", "Pet Loss Grief"),
    "cbt-for-empty-nest": ("Empty nest syndrome", "Empty Nest Syndrome"),
    "cbt-for-quarter-life-crisis": ("Quarter-life crisis", "Quarter-Life Crisis"),
    "cbt-for-climate-anxiety": ("Eco-anxiety", "Climate Anxiety"),
    "cbt-for-aging-anxiety": ("Gerascophobia", "Aging Anxiety"),
    "cbt-for-workplace-bullying": ("Workplace bullying", "Workplace Bullying"),
    "cbt-for-caregiver-burnout": ("Caregiver stress", "Caregiver Burnout"),
    "cbt-for-compassion-fatigue": ("Compassion fatigue", "Compassion Fatigue"),
    "cbt-for-complex-ptsd": ("Complex post-traumatic stress disorder", "Complex PTSD"),
    "cbt-for-survivor-guilt": ("Survivor guilt", "Survivor Guilt"),
    "cbt-for-somatic-symptom-disorder": ("Somatic symptom disorder", "Somatic Symptom Disorder"),
    "cbt-for-tinnitus": ("Tinnitus", "Tinnitus"),
    "cbt-for-driving-anxiety": ("Amaxophobia", "Driving Anxiety"),
    "cbt-for-dental-phobia": ("Dental fear", "Dental Phobia"),
    "cbt-for-existential-crisis-meaning": ("Existential crisis", "Existential Crisis"),
    "cbt-for-religious-trauma-spiritual": ("Religious trauma", "Religious Trauma"),
    "cbt-for-body-dysmorphia": ("Body dysmorphic disorder", "Body Dysmorphia"),
    "cbt-for-ocd-compulsive-behaviors": ("Compulsive behavior", "Compulsive Behaviors"),
    "cbt-for-overthinking-rumination": ("Rumination (psychology)", "Overthinking & Rumination"),
    "cbt-for-panic-attacks-agoraphobia": ("Agoraphobia", "Panic Attacks & Agoraphobia"),
    "cbt-for-phobias": ("Phobia", "Phobias"),
    "cbt-for-pregnancy-anxiety": ("Tokophobia", "Pregnancy Anxiety"),
    "cbt-for-postpartum-depression": ("Postpartum depression", "Postpartum Depression"),
    "cbt-for-chronic-illness": ("Chronic condition", "Chronic Illness"),
    "cbt-for-abandonment-issues": ("Fear of abandonment", "Abandonment Issues"),
    "cbt-for-self-sabotage": ("Self-sabotage", "Self-Sabotage"),
    "cbt-for-divorce-separation": ("Divorce", "Divorce & Separation"),
    "cbt-for-decision-anxiety": ("Decidophobia", "Decision Anxiety"),
    "cbt-for-entrepreneurs": ("Entrepreneurship", "Entrepreneur Stress"),
    "cbt-for-developers": ("Software engineering", "Developer Stress"),
    "cbt-for-students": ("Student", "Student Stress"),
    "cbt-for-teachers": ("Teacher burnout", "Teacher Stress"),
    "cbt-for-veterans": ("Veteran", "Veteran Mental Health"),
    "cbt-for-parents": ("Parenting stress", "Parenting Stress"),
    "cbt-for-shift-workers": ("Shift work", "Shift Worker Stress"),
    "cbt-for-retirement": ("Retirement", "Retirement Anxiety"),
    "cbt-for-retirement-anxiety": ("Retirement", "Retirement Anxiety"),
    "cbt-for-relocation-anxiety": ("Agoraphobia", "Relocation Anxiety"),
    "cbt-for-return-to-work-anxiety": ("Workplace stress", "Return-to-Work Anxiety"),
    "cbt-for-spiritual-crisis": ("Spiritual crisis", "Spiritual Crisis"),
    "cbt-for-doomscrolling-news-anxiety": ("Doomscrolling", "Doomscrolling"),
    "cbt-for-sunday-scaries-monday-dread": ("Sunday scaries", "Sunday Scaries"),
    "cbt-for-pregnancy-loss-miscarriage": ("Miscarriage", "Pregnancy Loss & Miscarriage"),
    "cbt-for-pregnancy-loss": ("Miscarriage", "Pregnancy Loss"),
    "cbt-for-birth-trauma": ("Birth trauma", "Birth Trauma"),
    "cbt-for-cynophobia": ("Cynophobia", "Cynophobia (Fear of Dogs)"),
    "cbt-for-emetophobia": ("Emetophobia", "Emetophobia"),
    "cbt-for-entomophobia": ("Entomophobia", "Entomophobia (Fear of Insects)"),
    "cbt-for-ophidiophobia": ("Ophidiophobia", "Ophidiophobia (Fear of Snakes)"),
    "cbt-for-ornithophobia": ("Ornithophobia", "Ornithophobia (Fear of Birds)"),
    "cbt-for-pyrophobia": ("Pyrophobia", "Pyrophobia (Fear of Fire)"),
    "cbt-for-thalassophobia": ("Thalassophobia", "Thalassophobia (Fear of Deep Water)"),
    "cbt-for-thanatophobia": ("Death anxiety (psychology)", "Thanatophobia"),
    "cbt-for-trypanophobia": ("Trypanophobia", "Trypanophobia (Fear of Needles)"),
    "cbt-for-trypophobia": ("Trypophobia", "Trypophobia"),
    "cbt-for-chiroptophobia": ("Chiroptophobia", "Chiroptophobia (Fear of Bats)"),
    "cbt-for-ailurophobia": ("Ailurophobia", "Ailurophobia (Fear of Cats)"),
    "cbt-for-aquaphobia": ("Aquaphobia", "Aquaphobia (Fear of Water)"),
    "cbt-for-autophobia": ("Autophobia", "Autophobia (Fear of Being Alone)"),
    "cbt-for-atychiphobia": ("Atychiphobia", "Atychiphobia (Fear of Failure)"),
    "cbt-for-blood-injury-phobia": ("Blood-injection-injury type phobia", "Blood-Injury Phobia"),
    "cbt-for-coulrophobia": ("Coulrophobia", "Coulrophobia (Fear of Clowns)"),
    "cbt-for-complicated-grief": ("Complicated grief", "Complicated Grief"),
    "cbt-for-caregivers": ("Caregiver", "Caregiver Stress"),
    "cbt-for-caretaker-burnout": ("Caregiver stress", "Caretaker Burnout"),
    "cbt-for-adhd-burnout-overwhelm": ("Burnout (psychology)", "ADHD Burnout & Overwhelm"),
    "cbt-for-ai-anxiety": ("AI anxiety", "AI Anxiety"),
    "cbt-for-code-review-anxiety": ("Code review", "Code Review Anxiety"),
    "cbt-for-debugging-stress": ("Debugging", "Debugging Stress"),
    "cbt-for-on-call-anxiety": ("On-call duty", "On-Call Anxiety"),
    "cbt-for-womens-mental-health": ("Women's mental health", "Women's Mental Health"),
    "cbt-for-religious-deconstruction": ("Religious deconstruction", "Religious Deconstruction"),
    "cbt-for-retirement-caregiver-spouse": ("Caregiver stress", "Retirement Caregiver Spouse"),
    "cbt-for-retirement-later-life": ("Retirement", "Retirement & Later Life"),
}


def fetch_wiki(title):
    """Fetch Wikipedia summary. Returns (extract, url) or None."""
    url = API.format(urllib.parse.quote(title, safe="()"))
    req = urllib.request.Request(url, headers={"User-Agent": "CBTToolkit/1.0 (educational project)"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
                extract = data.get("extract", "")
                page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")
                if extract and len(extract) > 50:
                    return extract, page_url
                return None  # real 404 or empty
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None  # article doesn't exist
            time.sleep(1 * (attempt + 1))
        except Exception:
            time.sleep(2 * (attempt + 1))
    return None


def inject_wikipedia(html, display_name, extract, wiki_url):
    """Inject a Wikipedia card into the HTML. Handles multiple page structures."""
    card_html = (
        '\n  <div class="card" id="condition-overview">\n'
        f'    <h2>What is {display_name}?</h2>\n'
        f'    <p>{extract}</p>\n'
        f'    <p style="font-size: 0.85rem; color: #718096; margin-top: 1rem;">'
        f'Learn more: <a href="{wiki_url}" target="_blank" rel="noopener noreferrer">Wikipedia</a></p>\n'
        '  </div>\n'
    )

    # Structure 1: pages with <div class="card"> (newer pages)
    pattern1 = r'(<div class="card">)'
    matches1 = list(re.finditer(pattern1, html))
    if len(matches1) >= 2:
        pos = matches1[1].start()
        return html[:pos] + card_html + html[pos:]

    # Structure 2: pages with <div class="intro"> + <div class="technique"> (older pages)
    intro_end = re.search(r'(</div>\s*\n\s*)(<div class="technique">)', html)
    if intro_end:
        pos = intro_end.start(2)
        return html[:pos] + card_html + html[pos:]

    # Structure 3: inject after first <div class="container"> + intro
    container = re.search(r'(<div class="container">.*?</div>)', html, re.DOTALL)
    if container:
        pos = container.end()
        return html[:pos] + card_html + html[pos:]

    return None


def main():
    enriched = 0
    skipped = 0
    failed = 0
    not_found = 0

    for filename, (wiki_title, display_name) in sorted(MAP.items()):
        filepath = os.path.join(SEO_DIR, filename + ".html")
        if not os.path.exists(filepath):
            continue

        html = open(filepath, "r", encoding="utf-8").read()

        # Idempotent check
        if MARKER in html:
            skipped += 1
            continue

        result = fetch_wiki(wiki_title)
        if result is None:
            not_found += 1
            print(f"  SKIP: {filename} -> {wiki_title}")
            continue

        extract, wiki_url = result
        new_html = inject_wikipedia(html, display_name, extract, wiki_url)
        if new_html is None:
            failed += 1
            continue

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_html)
        enriched += 1
        print(f"  OK:  {filename} <- {wiki_title}")
        time.sleep(0.3)  # be nice to Wikipedia

    print(f"\nEnriched: {enriched} | Skipped (already done): {skipped} | 404: {not_found} | Failed: {failed}")


if __name__ == "__main__":
    main()
