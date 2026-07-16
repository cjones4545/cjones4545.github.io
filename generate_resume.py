from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, PageBreak

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "assets" / "Carson-Jones-Resume.pdf"

styles = getSampleStyleSheet()
style_definitions = [
    ("Heading1", "Title", dict(fontSize=20, leading=24, spaceAfter=10, textColor=colors.HexColor("#1d4ed8"))),
    ("Heading2", "Heading2", dict(fontSize=12, leading=14, spaceAfter=6, textColor=colors.HexColor("#0f172a"), fontName="Helvetica-Bold")),
    ("Body", "BodyText", dict(fontSize=10, leading=13, spaceAfter=6, textColor=colors.HexColor("#334155"))),
    ("Small", "BodyText", dict(fontSize=9, leading=11, textColor=colors.HexColor("#64748b"))),
    ("Bullet", "BodyText", dict(fontSize=10, leading=12, leftIndent=12, bulletIndent=0, spaceAfter=3, textColor=colors.HexColor("#334155"))),
]
for name, parent_name, kwargs in style_definitions:
    try:
        styles.add(ParagraphStyle(name=name, parent=styles[parent_name], **kwargs))
    except KeyError:
        pass

story = []
story.append(Paragraph("Carson Jones", styles["Heading1"]))
story.append(Paragraph("Cloud Infrastructure | Linux | Kubernetes | Automation | DevSecOps", styles["Body"]))
story.append(Paragraph("Huntsville, AL | carsonjones4545@gmail.com | linkedin.com/in/carson-jones-0b4602228", styles["Small"]))
story.append(Spacer(1, 0.15 * inch))

story.append(Paragraph("Professional Summary", styles["Heading2"]))
story.append(Paragraph(
    "Systems Administrator with six years of progressive enterprise IT experience spanning hybrid on-premises and Microsoft Azure environments. Focused on Linux, cloud infrastructure, Kubernetes, automation, CI/CD, and secure software delivery in regulated and disconnected operations.",
    styles["Body"]
))
story.append(Spacer(1, 0.1 * inch))

story.append(Paragraph("Core Skills", styles["Heading2"]))
skills = [
    "Linux administration and hardening",
    "Microsoft Azure and hybrid cloud operations",
    "AKS and RKE2 Kubernetes platforms",
    "Docker, Podman, and container runtimes",
    "Ansible, Terraform, and infrastructure as code",
    "GitLab CI/CD, GitOps, and release automation",
    "Python, Bash, and PowerShell scripting",
    "Root-cause analysis and technical troubleshooting",
    "Technical leadership and cross-functional collaboration"
]
story.append(ListFlowable([ListItem(Paragraph(item, styles["Bullet"])) for item in skills], bulletType='bullet', leftIndent=10, bulletFontName='Helvetica'))
story.append(Spacer(1, 0.1 * inch))

story.append(Paragraph("Experience", styles["Heading2"]))
experience = [
    ("Systems Administrator II | Lockheed Martin | June 2025 – Present", [
        "Engineered and maintained enterprise Linux infrastructure supporting development and production workloads across hybrid on-premises and Microsoft Azure environments.",
        "Designed and administered Kubernetes platforms using Azure Kubernetes Service and RKE2 for containerized application delivery.",
        "Implemented infrastructure as code with Terraform and Ansible to automate provisioning, configuration, and lifecycle operations.",
        "Developed and optimized GitLab CI/CD pipelines for infrastructure deployment, artifact management, and release workflows."
    ]),
    ("Meter Reader | Municipal Utilities Board | June 2024 – June 2025", [
        "Collected and maintained accurate utility meter data for residential, commercial, and industrial customers.",
        "Inspected meter conditions and communicated maintenance or troubleshooting issues.",
        "Delivered reliable customer support and detailed recordkeeping for field operations."
    ]),
    ("Systems Administrator | United States Marine Corps | May 2020 – May 2024", [
        "Supported migration of base-wide on-premises email accounts into a hybrid Microsoft 365 environment.",
        "Provided Tier II support for DNS, DHCP, Microsoft Exchange, networking, and directory services.",
        "Managed enterprise automation, monitoring, and reporting initiatives with Microsoft Power BI and configuration-management tooling.",
        "Supervised technical personnel and contributed to enterprise operations and infrastructure reliability."
    ])
]
for title, bullets in experience:
    story.append(Paragraph(title, styles["Body"]))
    for bullet in bullets:
        story.append(Paragraph("• " + bullet, styles["Bullet"]))
    story.append(Spacer(1, 0.06 * inch))

story.append(Paragraph("Training & Certifications", styles["Heading2"]))
certs = [
    "CompTIA Security+",
    "Data Systems Administrator Course",
    "Data Systems Administrators Supervisors Course",
    "Corporals Course",
    "Martial Arts Instructor Course",
    "Active Top Secret clearance with SCI component"
]
story.append(ListFlowable([ListItem(Paragraph(item, styles["Bullet"])) for item in certs], bulletType='bullet', leftIndent=10, bulletFontName='Helvetica'))
story.append(Spacer(1, 0.1 * inch))

story.append(Paragraph("Education", styles["Heading2"]))
story.append(Paragraph("Liberty University | Lynchburg, Virginia | 2021 – Present", styles["Body"]))
story.append(Paragraph("Current GPA: 3.7 | Expected graduation: 2026", styles["Small"]))

pdf = SimpleDocTemplate(str(OUTPUT), pagesize=LETTER, rightMargin=0.75 * inch, leftMargin=0.75 * inch, topMargin=0.65 * inch, bottomMargin=0.65 * inch)
pdf.build(story)
print(f"Generated {OUTPUT}")
