from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "docs" / "Jason_B_Johnson_Professional_Resume.pdf"

NAVY = colors.HexColor("#102A43")
TEAL = colors.HexColor("#14766F")
COPPER = colors.HexColor("#C97842")
SLATE = colors.HexColor("#52606D")
LIGHT = colors.HexColor("#D8E0E5")

pdfmetrics.registerFont(TTFont("DejaVu", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DejaVu-Bold", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"))

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Title"], fontName="DejaVu-Bold", fontSize=23, leading=26, textColor=NAVY, alignment=TA_CENTER, spaceAfter=4))
styles.add(ParagraphStyle(name="Identity", parent=styles["Normal"], fontName="DejaVu-Bold", fontSize=10.5, leading=14, textColor=TEAL, alignment=TA_CENTER, spaceAfter=5))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontName="DejaVu", fontSize=8.7, leading=12, textColor=SLATE, alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="DejaVu-Bold", fontSize=10.8, leading=14, textColor=NAVY, borderColor=LIGHT, borderWidth=0, borderPadding=(0, 0, 4, 0), spaceBefore=8, spaceAfter=5, uppercase=True))
styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontName="DejaVu", fontSize=8.9, leading=12.4, textColor=colors.HexColor("#263746"), spaceAfter=4))
styles.add(ParagraphStyle(name="Role", parent=styles["BodyText"], fontName="DejaVu-Bold", fontSize=9.4, leading=12.5, textColor=NAVY, spaceAfter=1))
styles.add(ParagraphStyle(name="Meta", parent=styles["BodyText"], fontName="DejaVu", fontSize=8.2, leading=11, textColor=TEAL, spaceAfter=3))
styles.add(ParagraphStyle(name="BulletSmall", parent=styles["BodyText"], fontName="DejaVu", fontSize=8.45, leading=11.5, textColor=SLATE, leftIndent=12, firstLineIndent=-7, bulletIndent=2, spaceAfter=1.5))


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(COPPER)
    canvas.setLineWidth(1.2)
    canvas.line(0.6 * inch, 0.48 * inch, 7.9 * inch, 0.48 * inch)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(SLATE)
    canvas.drawString(0.6 * inch, 0.3 * inch, "Jason B. Johnson | Learn - Lead - Grow")
    canvas.drawRightString(7.9 * inch, 0.3 * inch, f"Page {doc.page}")
    canvas.restoreState()


def section(title):
    return [Paragraph(title.upper(), styles["Section"]), Spacer(1, 1)]


def role(title, meta, bullets):
    parts = [Paragraph(title, styles["Role"]), Paragraph(meta, styles["Meta"])]
    parts.extend(Paragraph(f"• {item}", styles["BulletSmall"]) for item in bullets)
    parts.append(Spacer(1, 5))
    return KeepTogether(parts)


story = [
    Paragraph("Jason B. Johnson", styles["Name"]),
    Paragraph("Educator | School Leader | Operations Professional", styles["Identity"]),
    Paragraph("South Bend, Indiana | jasonjohnson75@gmail.com | 574-300-1378<br/>linkedin.com/in/jasonjohnson46637 | jasonjohnson.cc", styles["Contact"]),
]

story += section("Professional Summary")
story.append(Paragraph(
    "Educator, school leader, and operations professional with more than seven years of K-12 experience and more than 20 years in corporate operations, logistics, sales, recruiting, and team leadership. Experience spans fifth grade instruction, academic coaching, student support, Project Lead The Way, school transportation, family engagement, and practical systems improvement.",
    styles["BodySmall"],
))

story += section("Core Strengths")
story.append(Paragraph(
    "Classroom instruction | Academic coaching | MTSS and PBIS | Literacy intervention | Student support | Family communication | STEAM and PLTW | Staff leadership | Transportation and logistics | Scheduling | Recruiting | Customer and account development | Process improvement",
    styles["BodySmall"],
))

story += section("Education and Professional Preparation")
story.extend([
    Paragraph("Bachelor of Science in Business Management | Bethel University", styles["Role"]),
    Paragraph("Transition to Teaching and Master of Arts in Teaching pathway | Bethel University | In Progress", styles["BodySmall"]),
    Paragraph("Graduate Business Coursework | Youngstown State University, 21 credits | Bethel University, 9 credits", styles["BodySmall"]),
    Paragraph("Project Lead The Way Design and Engineering | STEAM integration | Literacy instruction | MTSS and PBIS | Instructional coaching", styles["BodySmall"]),
])

story += section("Education and School Leadership Experience")
story.extend([
    role("Fifth Grade Teacher | Madison STEAM Academy", "2026 - Present | South Bend, Indiana", [
        "Deliver standards-aligned fifth grade instruction in a STEAM-focused school environment.",
        "Use CKLA, Science of Reading practices, UFLI, i-Ready, ALEKS, Canvas, and family communication systems.",
        "Build classroom routines that connect high expectations, student support, Sports + STEAM, and future careers.",
    ]),
    role("Dean of Students and Academic Coach | Madison STEAM Academy", "2023 - 2025 | South Bend, Indiana", [
        "Supported student behavior, attendance, safety, family communication, and daily school operations.",
        "Coordinated Tier 2 interventions, PBIS resources, MTSS planning, literacy groups, and student progress follow-through.",
        "Supported teachers through coaching, collaborative planning, classroom assistance, and mentoring.",
    ]),
    role("PLTW Instructor, Classroom Educator, and Literacy Intervention", "Elementary and Middle School Experience", [
        "Taught elementary and middle grades, including fourth grade and Project Lead The Way design and engineering.",
        "Led Corrective Reading, IREAD preparation, small-group literacy instruction, and student activity coordination.",
    ]),
])

story.append(PageBreak())
story += section("School Transportation and Operations")
story.append(role("Assistant Director of Transportation | School Transportation", "District Operations Leadership", [
    "Supported approximately 96 drivers and paraprofessionals, 220 routes, and a multi-tier transportation schedule.",
    "Worked with Bytecurve, Tyler Technologies and Versatrans, MyGeo GPS, and geographic routing data.",
    "Coordinated scheduling, route planning, incident response, staff support, and communication with schools and families.",
]))

story += section("Corporate and Business Experience")
story.extend([
    role("AT&T | Store Management and Small-Business Sales", "Prior Corporate Career", [
        "Led teams, retail operations, customer relationships, sales performance, training, and account development.",
    ]),
    role("UPS Freight | Operations Supervisor", "Prior Corporate Career", [
        "Supported freight operations, dispatch, driver scheduling, safety, logistics, and service accountability.",
    ]),
    role("Coca-Cola | Account Developer", "Prior Corporate Career", [
        "Managed customer accounts, product placement, service relationships, and territory execution.",
    ]),
    role("Halvor Lines | Recruiter", "Prior Corporate Career", [
        "Supported recruiting, candidate communication, talent needs, and transportation-industry workforce development.",
    ]),
])

story += section("Technology and Instructional Tools")
story.append(Paragraph(
    "Canvas | Google Classroom | PowerSchool | ClassDojo | CKLA | UFLI | Fundations | Corrective Reading | i-Ready Reading and Math | Achieve3000 | ALEKS | Project Lead The Way | Bytecurve | Tyler Technologies and Versatrans | MyGeo GPS",
    styles["BodySmall"],
))

story += section("Professional Focus")
story.append(Paragraph(
    "Committed to public education, family partnerships, student opportunity, practical leadership, representation, clear communication, and systems that help people succeed. Interested in continued growth across classroom leadership, school administration, academic coaching, operations, transportation, and community-focused work.",
    styles["BodySmall"],
))

doc = SimpleDocTemplate(
    str(OUTPUT), pagesize=letter, rightMargin=0.62 * inch, leftMargin=0.62 * inch,
    topMargin=0.52 * inch, bottomMargin=0.62 * inch, title="Jason B. Johnson Professional Resume",
    author="Jason B. Johnson",
)
doc.build(story, onFirstPage=footer, onLaterPages=footer)
print(OUTPUT)
