# Jason B. Johnson - Professional Website
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
- `assets/images/jason-johnson-headshot.jpg` - Professional headshot used on the Home and About pages
- `assets/images/jason-johnson-headshot.webp` - Optimized headshot for modern browsers
- `assets/images/jason-johnson-headshot-560.webp` - Smaller mobile headshot
- `assets/images/jason-johnson-social-card.png` - 1200 x 630 social-sharing image
- `assets/images/favicon.svg` - JJ browser icon
- `assets/docs/` - PDF Documents (`Jason_B_Johnson_Professional_Resume.pdf`)

---

## Deployment Instructions

### Option 1: GitHub Pages (Current Hosting)
1. Keep the website files on the `main` branch of `jasonjohnson75-cyber/jasonjohnson-cc`.
2. Go to **Settings** > **Pages**.
3. Under **Source**, select **Deploy from a branch** and choose `main` / `root`.
4. Keep the custom domain set to `jasonjohnson.cc` and keep **Enforce HTTPS** enabled.
5. Do not delete or rename the root `CNAME` file.

### Option 2: Cloudflare Pages
1. Log into your **Cloudflare Dashboard**.
2. Go to **Workers & Pages** > **Create** > **Pages**.
3. Select **Connect to Git** and choose `jasonjohnson75-cyber/jasonjohnson-cc`.
4. For build settings:
   - **Framework preset:** None (Static HTML)
   - **Build command:** Leave empty
   - **Build output directory:** `/` (root directory)
5. Click **Save and Deploy**.
6. Once deployed, go to the **Custom Domains** tab in Cloudflare Pages and add `jasonjohnson.cc`.

Before connecting the production domain to Cloudflare Pages, remove it from GitHub Pages so the two hosting configurations do not compete for the same domain.

---

## How to Edit Site Content
- **To update the Headshot:** Replace `assets/images/jason-johnson-headshot.jpg` with your photo while keeping the same filename.
- **To update the PDF Résumé:** Replace `assets/docs/Jason_B_Johnson_Professional_Resume.pdf` with your updated resume PDF file.
- **To edit text or links:** Edit the respective HTML file directly in GitHub or your code editor.
- **After changing CSS or JavaScript:** Update the `v=` date on the stylesheet and script links in every HTML page so visitors receive the new files.
- **Before publishing:** Verify the `CNAME` file still contains only `jasonjohnson.cc`.

## Contact Form
The contact form does not send or store data on the website. It opens a completed draft in the visitor's email application. The public email address is `jasonjohnson75@gmail.com`.

## Publishing Checklist
1. Check every page on desktop and mobile.
2. Confirm the Home, About, Experience, Portfolio, Contact, and Résumé navigation links.
3. Confirm the résumé PDF opens.
4. Confirm external project links open in a new tab.
5. Confirm `CNAME`, `robots.txt`, and `sitemap.xml` remain in the repository root.
