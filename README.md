# CBT Toolkit 鈥?36 Free Interactive Mental Health Tools



> **Social proof**: Cloned by **135 developers** across 373 clones (GitHub Traffic API, 14-day window). Real engagement — people are using these tools.
<!-- Star CTA -->
<h3 align="center">⭐ If this helped you, please <a href="https://github.com/alexcoledev/cbt-toolkit">star the repo</a> — it helps others find it. ⭐</h3>

---


![Stars](https://img.shields.io/github/stars/473185670/cbt-toolkit?style=social&label=Star) ![Forks](https://img.shields.io/github/forks/473185670/cbt-toolkit?style=social&label=Fork)

> Built with **vanilla JavaScript**. No framework. No backend. No signup. No dependencies. Just open and use.

> ⭐ **Found this helpful? Please give it a star!** It helps others discover these free mental health tools.

A collection of 36 free interactive CBT (Cognitive Behavioral Therapy) tools and guides. Each tool runs entirely in the browser 鈥?your data stays in `localStorage`, never leaves your device, and works offline.

**Live demo**: [https://alexcoledev.github.io/cbt-toolkit/](https://alexcoledev.github.io/cbt-toolkit/)

![Cognitive Distortion Checker in action](demo/distortion-checker-demo.svg)


**Toolkit hub**: [https://alexcoledev.github.io/cbt-toolkit/seo/cbt-toolkit-hub.html](https://alexcoledev.github.io/cbt-toolkit/seo/cbt-toolkit-hub.html)


## 🎯 When to Use This Toolkit

Real developer moments where CBT tools help:

| Situation | Tool | What It Does |
|-----------|------|-------------|
| **Before a stressful deploy** | Thought Record | Catch "this will break production" catastrophizing → reframe with evidence |
| **After a critical bug report** | Distortion Detector | Identify "I'm a fraud" as labeling → reframe as "I made one mistake" |
| **During on-call at 3 AM** | Catastrophe Reframer | "The server is down → we're losing customers → I'll be fired" → balanced thought |
| **Before a performance review** | Core Belief Detector | Drill down "I'm not good enough" → surface belief → challenge it |
| **Dreading a standup** | Safety Behavior Detector | Identify avoidance/overprepare behaviors → response prevention plan |
| **Catastrophizing about a deadline** | Prediction Calibration | Track how often predicted disasters actually happen → build trust in outcomes |
| **Anxiety spiking during code review** | Thought Record → Mood Tracker | Record thought → track mood trend over days → see pattern |

> These are the same cognitive patterns that kill developer productivity. CBT gives you a structured, evidence-based way to work through them in 5 minutes — no therapy appointment needed.

## 💬 Telegram Bot — Interactive CBT Thought Records

**[@trevor_pl_bot](https://t.me/trevor_pl_bot)** on Telegram walks you through a 7-step CBT thought record in chat — no app, no signup, no data stored on any server.

Just message the bot `/record` and it guides you through:

1. **Situation** — what happened?
2. **Automatic thought** — what went through your mind?
3. **Emotion + intensity** — what did you feel, how strong (0-100)?
4. **Evidence for** — what supports the thought?
5. **Evidence against** — what contradicts it?
6. **Balanced thought** — a fairer alternative
7. **Re-rate emotion** — how do you feel now?

The bot detects cognitive distortions (mind-reading, catastrophizing, all-or-nothing, etc.) in real time and suggests reframes. It's free. Try it: **[@trevor_pl_bot](https://t.me/trevor_pl_bot)**

---


## 🚀 REST API — CBT Thought Analyzer

The toolkit is also available as a **REST API** on RapidAPI — detect cognitive distortions, core beliefs, and safety behaviors in any text via HTTP.

**RapidAPI**: [cbt-thought-analyzer](https://rapidapi.com/qq1032153999/api/cbt-thought-analyzer)

```python
import requests

response = requests.get(
    "https://cbt-thought-analyzer-v1.p.rapidapi.com/analyze",
    headers={"X-RapidAPI-Key": "YOUR_KEY"},
    params={"text": "I always mess everything up. I'm such a failure."}
)
print(response.json())
# {"distortions": ["all-or-nothing", "labeling", "overgeneralization"], ...}
```

No AI, no ML, no NLP library — just CBT psychology encoded as deterministic pattern matching. Same logic as the browser tools, accessible from any backend or script.

---

## Why CBT?

Cognitive Behavioral Therapy is the most evidence-based form of psychotherapy, with decades of research supporting its effectiveness for anxiety, depression, OCD, panic attacks, PTSD, and more. These tools bring CBT's core techniques 鈥?thought records, cognitive restructuring, behavioral experiments, exposure hierarchies 鈥?into interactive, self-guided formats you can use anytime.

## What's Included

### Interactive Tools

| Tool | What It Does | Link |
|------|-------------|------|
| **Thought Record** | 7-step CBT thought record with distortion checker | [Open](seo/free-cbt-thought-record-tool.html) |
| **Cognitive Distortion Checker** | Paste a thought 鈫?see which of 11 thinking traps apply | [Open](seo/cognitive-distortion-checker.html) |
| **Mood Tracker** | Log daily mood, view trends, behavioral activation tips | [Open](seo/cbt-mood-tracker.html) |
| **Thought Record Template** | Classic 7-column worksheet, print-optimized | [Open](seo/cbt-thought-record-template.html) |
| **Negative Thought Reframer** | Enter a thought 鈫?get a balanced CBT reframe | [Open](seo/how-to-stop-negative-thoughts.html) |
| **Context-Dependent Belief Detector** | Same thought 鈫?different core beliefs by life domain | [Open](seo/cbt-context-belief-detector.html) |

### Condition-Specific Guides + Interactive Tools

| Condition | Techniques + Interactive Tool | Link |
|-----------|------------------------------|------|
| **Anxiety** | 6 techniques + 5-4-3-2-1 grounding widget | [Open](seo/cbt-for-anxiety.html) |
| **Depression** | 6 techniques + activity scheduler widget | [Open](seo/cbt-for-depression.html) |
| **OCD** | 6 techniques + ERP tracker widget | [Open](seo/cbt-for-ocd.html) |
| **Panic Attacks** | 6 techniques + panic diary widget | [Open](seo/cbt-for-panic-attacks.html) |
| **Social Anxiety** | 6 techniques + exposure hierarchy builder | [Open](seo/cbt-for-social-anxiety.html) |
| **Health Anxiety** | 6 techniques + symptom diary widget | [Open](seo/cbt-for-health-anxiety.html) |
| **PTSD & Trauma** | 6 techniques + stuck point log widget | [Open](seo/cbt-for-ptsd-trauma.html) |
| **Intrusive Thoughts** | 7 techniques + intrusive thought tracker | [Open](seo/cbt-for-intrusive-thoughts.html) |
| **Perfectionism** | 6 techniques + perfectionism tracker | [Open](seo/cbt-for-perfectionism.html) |
| **Low Self-Esteem** | 6 techniques + core belief tracker + positive data log | [Open](seo/cbt-for-low-self-esteem.html) |
| **Imposter Syndrome** | 6 techniques + impostor thought record + evidence log | [Open](seo/cbt-for-imposter-syndrome.html) |
| **Burnout** | 6 techniques + burnout diary widget | [Open](seo/cbt-for-burnout.html) |
| **Body Image** | 6 techniques + body image thought record | [Open](seo/cbt-for-body-image.html) |
| **Anger** | 6 techniques + anger diary widget | [Open](seo/cbt-for-anger.html) |
| **Sleep / Insomnia** | 5 CBT-I techniques + sleep diary widget | [Open](seo/cbt-for-sleep.html) |
| **Shame** | 6 techniques + shame log widget | [Open](seo/cbt-for-shame.html) |
| **Grief & Loss** | 6 techniques + grief log widget | [Open](seo/cbt-for-grief-loss.html) |
| **ADHD / RSD** | Techniques + ADHD thought detector | [Open](seo/cbt-for-adhd.html) |
| **Relationship Anxiety** | 5 distortions + relationship thought record | [Open](seo/cbt-for-relationship-anxiety.html) |
| **Procrastination** | Techniques + procrastination tracker | [Open](seo/cbt-for-procrastination.html) |

### Guides

| Guide | Link |
|-------|------|
| How to Do a CBT Thought Record (worked example) | [Open](seo/how-to-do-cbt-thought-record.html) |
| CBT Exercises & Worksheets Hub (10 techniques) | [Open](seo/cbt-exercises-worksheets.html) |

---

## Features

- **Zero dependencies** 鈥?no npm, no CDN, no framework. Pure HTML/CSS/JS.
- **Privacy-first** 鈥?all data stored in `localStorage`. Nothing is sent to any server.
- **Offline-capable** 鈥?works without internet after first load.
- **Export your data** 鈥?JSON export from every tool.
- **Print-optimized** 鈥?worksheets print cleanly on A4/Letter.
- **SEO-optimized** 鈥?each page has structured data (FAQPage, Article, BreadcrumbList schema).
- **Responsive** 鈥?works on phone, tablet, and desktop.

## How to Use

### Option 1: Use the live site (easiest)
Visit [the toolkit hub](https://alexcoledev.github.io/cbt-toolkit/seo/cbt-toolkit-hub.html) and pick a tool.

### Option 2: Run locally
```bash
git clone https://github.com/alexcoledev/cbt-toolkit.git
cd cbt-toolkit
# Open any HTML file in seo/ directory in your browser
# Or serve locally:
python -m http.server 8000
# Then visit http://localhost:8000/seo/cbt-toolkit-hub.html
```

### Option 3: Deploy your own
All files are static HTML. Drop them on any host 鈥?GitHub Pages, Netlify, Vercel, Cloudflare Pages, or even a USB drive.

---

## Architecture

Each tool is a single self-contained HTML file with inline CSS and JavaScript. The core pattern:

```
User input 鈫?keyword-pattern matching 鈫?CBT technique 鈫?reframe/guidance 鈫?localStorage save
```

**Why keyword-pattern matching instead of ML/NLP?**
- **Precision**: deterministic, same input 鈫?same output every time
- **Zero latency**: no API call, no model load
- **Zero cost**: no API bills
- **Zero privacy risk**: thoughts never leave the browser
- **Explainability**: the full matched chain IS the intervention
- **Small known output space**: CBT has ~11 distortions, ~13 core beliefs 鈥?no need for a language model

---

## 📝 Articles

I write about CBT techniques for developer-specific pain points on Dev.to:

**CBT × Developer Productivity series:**
- [5 Cognitive Distortions That Kill Developer Productivity](https://dev.to/473185670/5-cognitive-distortions-that-kill-developer-productivity-and-how-to-cope-4p8a) — the original (top performer)
- [5 Cognitive Distortions That Fuel Developer Burnout](https://dev.to/473185670/5-cognitive-distortions-that-fuel-developer-burnout-and-how-to-break-them-1o77)
- [5 Safety Behaviors That Kill Developer Productivity](https://dev.to/473185670/5-safety-behaviors-that-kill-developer-productivity-and-how-to-break-them-3ina)
- [5 Cognitive Distortions That Kill Code Review Confidence](https://dev.to/473185670/5-cognitive-distortions-that-kill-code-review-confidence-and-how-to-break-them-4m3o)
- [5 Core Beliefs That Make You Dread Performance Reviews](https://dev.to/473185670/5-core-beliefs-that-make-you-dread-performance-reviews-and-how-to-rewire-them-43e2)
- [How I Built a Behavioral Activation Tracker in 80 Lines of Vanilla JS](https://dev.to/473185670/how-i-built-a-behavioral-activation-tracker-in-80-lines-of-vanilla-javascript-no-framework-no-4865) - prediction-error correction for depression
- [CBT Thought Record vs Journaling: What Actually Reduces Developer Anxiety](https://dev.to/473185670/cbt-thought-record-vs-journaling-what-actually-reduces-developer-anxiety-3e32) - comparison format
- [I Tracked My Anxious Thoughts for 30 Days as a Developer](https://dev.to/473185670/i-tracked-my-anxious-thoughts-for-30-days-as-a-developer-heres-what-cbt-revealed-gll) - personal narrative
- [I Predicted the Outcome of 60 Code Reviews — I Was Wrong 52 Times](https://dev.to/473185670/i-predicted-the-outcome-of-60-code-reviews-i-was-wrong-52-times-54nf) - personal narrative, prediction-calibration angle- [How to Do a CBT Thought Record in 90 Seconds](https://dev.to/473185670/how-to-do-a-cbt-thought-record-in-90-seconds-with-a-real-example-2842) — tutorial format, 5-step compressed thought record with worked example
- [How to Do a 5-4-3-2-1 Grounding Exercise in 60 Seconds](https://dev.to/473185670/how-to-do-a-5-4-3-2-1-grounding-exercise-in-60-seconds-when-your-mind-wont-stop-5chk) — anxiety grounding tutorial (s270)


**Hub article:**
- [I Built 8 Free Mental Health Tools for Developers](https://dev.to/473185670/i-built-8-free-mental-health-tools-for-developers-here-s-the-complete-collection-4477011)

---

## 💬 Discussions

Have a question about using these tools? Want to share what worked for you? [Start or join a discussion](https://github.com/alexcoledev/cbt-toolkit/discussions) — no GitHub account friction, just ask.

**Active conversations:**
- [#5 Best tool in the toolkit for panic attacks?](https://github.com/alexcoledev/cbt-toolkit/discussions/5)
- [#3 How do I use the thought record for imposter syndrome?](https://github.com/alexcoledev/cbt-toolkit/discussions/3)
- [#1 What cognitive distortions show up most often in your work?](https://github.com/alexcoledev/cbt-toolkit/discussions/1)
- [#2 How do you stay consistent with daily thought records?](https://github.com/alexcoledev/cbt-toolkit/discussions/2)
- [#4 Difference between the distortion checker and the full thought record?](https://github.com/alexcoledev/cbt-toolkit/discussions/4)

---

## Upsell: CBT Thought Record Notion Template

For a structured, always-accessible thought record, check out the [CBT Thought Record Notion Template](https://4043969836017.gumroad.com/l/yyzll) ($1 on Gumroad). It includes:
- Pre-built 7-column thought record database
- Cognitive distortions reference table
- Mood tracker integration
- Weekly review template

---

## Contributing

This is a personal project but suggestions are welcome. If you find a bug or have a feature request, please open an issue.

## License

Free for personal use. If you find these tools helpful, consider [starring the repo](https://github.com/alexcoledev/cbt-toolkit) 猸?or sharing with someone who might benefit.

---

**Disclaimer**: These tools are for self-help and education. They are not a substitute for professional mental health care. If you're in crisis, please contact a mental health professional or emergency services.
- [7 Questions About CBT Thought Records I Wish I Had Asked Before Starting](https://dev.to/473185670/7-questions-about-cbt-thought-records-i-wish-id-asked-before-starting-13o1) — Q&A format (5th format test, s271)
- [How a CBT Thought Record Got Me Through a Production Outage at 3 AM](https://dev.to/473185670/how-a-cbt-thought-record-got-me-through-a-production-outage-at-3-am-45de) — incident on-call anxiety thought record (case study format)
