# Jason B. Johnson - Professional Brand Website
Domain: https://jasonjohnson.cc

This repository contains the complete, production-ready website for **Jason B. Johnson** (Educator, School Leader, and Operations Professional).

## Project Structure
- `index.html` - Home Page & Executive Summary
- `about.html` - South Bend Roots, Family Legacy & Career Transition Story
- `education-leadership.html` - Classroom Practice, Coaching, MTSS/PBIS, PLTW & Literacy
- `operations-business.html` - Transportation Management & 20+ Years Corporate Experience
- `experience.html` - Career History Timeline
- `portfolio.html` - Featured Leadership & Instructional Projects
- `resume.html` - Combined Print/Web Résumé
- `contact.html` - Professional Contact Information & Form
- `404.html` - Custom Error Page
- `CNAME` - Domain pointer (`jasonjohnson.cc`)
- `sitemap.xml` & `robots.txt` - SEO Files
- `assets/css/styles.css` - Custom Theme CSS (Navy, Teal, Copper, Ivory)
- `assets/js/main.js` - Navigation & Interactivity JS
- `assets/images/` - Image Assets & Headshot Placeholders
- `assets/docs/` - PDF Documents (`Jason_B_Johnson_Professional_Resume.pdf`)

---

## Deployment Instructions

### Option 1: Cloudflare Pages (Recommended - Free)
1. Log into your **Cloudflare Dashboard**.
2. Go to **Workers & Pages** > **Create** > **Pages**.
3. Select **Connect to Git** and choose this GitHub repository (`jasonjohnson75-cyber/personal-website` or similar).
4. For build settings:
   - **Framework preset:** None (Static HTML)
   - **Build command:** Leave empty
   - **Build output directory:** `/` (root directory)
5. Click **Save and Deploy**.
6. Once deployed, go to the **Custom Domains** tab in Cloudflare Pages and add `jasonjohnson.cc`.

### Option 2: GitHub Pages (Free)
1. Push this repository to GitHub.
2. Go to **Settings** > **Pages**.
3. Under **Source**, select `Deploy from a branch` and choose `main` / `root`.
4. Under **Custom domain**, enter `jasonjohnson.cc` and check **Enforce HTTPS**.

---

## How to Edit Site Content
- **To update the Headshot:** Replace `assets/images/headshot.jpg` with your photo.
- **To update the PDF Résumé:** Replace `assets/docs/Jason_B_Johnson_Professional_Resume.pdf` with your updated resume PDF file.
- **To edit text or links:** Edit the respective HTML file directly in GitHub or your code editor.
