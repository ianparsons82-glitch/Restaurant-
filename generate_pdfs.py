#!/usr/bin/env python3
"""
Restaurant Operations PDF Generator
Creates printable PDF versions of checklists optimized for posting/lamination
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# Color palettes
COLORS_WARM = {
    "primary": colors.HexColor("#2C3E50"),      # Navy
    "accent": colors.HexColor("#FF6B6B"),        # Coral
    "background": colors.HexColor("#F5F3F0"),    # Cream
    "secondary": colors.HexColor("#8B8680"),     # Warm Gray
    "gold": colors.HexColor("#D4AF37"),          # Gold
    "red": colors.HexColor("#E74C3C"),           # Alert Red
    "yellow": colors.HexColor("#F39C12"),        # Warning Yellow
    "green": colors.HexColor("#27AE60"),         # Success Green
    "white": colors.HexColor("#FFFFFF"),
    "black": colors.HexColor("#000000"),
}

COLORS_MODERN = {
    "primary": colors.HexColor("#1B4332"),       # Dark Green
    "accent": colors.HexColor("#8B6F47"),        # Brown
    "background": colors.HexColor("#F5F3F0"),    # Cream
    "secondary": colors.HexColor("#2D2D2D"),     # Charcoal
    "gold": colors.HexColor("#B8860B"),          # Bronze
    "red": colors.HexColor("#DC143C"),           # Alert Crimson
    "yellow": colors.HexColor("#FFD700"),        # Warning Gold
    "green": colors.HexColor("#2D5016"),         # Success Deep Green
    "white": colors.HexColor("#FFFFFF"),
    "black": colors.HexColor("#000000"),
}

class ChecklistPDFGenerator:
    def __init__(self, aesthetic="warm"):
        self.aesthetic = aesthetic
        self.colors = COLORS_WARM if aesthetic == "warm" else COLORS_MODERN
        if aesthetic == "warm":
            self.dir_name = "Warm-&-Inviting"
            self.name_suffix = "Warm"
        else:
            self.dir_name = "Modern-Restaurant-Specific"
            self.name_suffix = "Modern"

    def _get_header_style(self):
        return TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), self.colors["primary"]),
            ('TEXTCOLOR', (0, 0), (-1, -1), self.colors["white"]),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ])

    def _get_row_style(self):
        return TableStyle([
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9F9F9")]),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ])

    def create_opening_checklist_pdf(self):
        """Generate Opening Checklist PDF."""
        filename = f"{self.dir_name}/Opening-Checklist-{self.name_suffix}.pdf"

        # Create PDF document
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
        )

        # Container for PDF elements
        elements = []

        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=self.colors["primary"],
            spaceAfter=12,
            alignment=1  # center
        )
        elements.append(Paragraph("DAILY OPENING CHECKLIST", title_style))

        # Date and manager info
        info_style = ParagraphStyle(
            'Info',
            fontName='Helvetica',
            fontSize=11,
            spaceAfter=6,
        )
        elements.append(Paragraph(f"<b>Date:</b> _________________ <b>Manager:</b> _________________ <b>Est. Time: 20 minutes</b>", info_style))
        elements.append(Spacer(1, 0.2*inch))

        # Checklist items
        checklist_items = [
            "☐ Equipment check (fryer, grill, ovens)",
            "☐ Walk-in cooler temperature check & log",
            "☐ Freezer temperature check & log",
            "☐ POS system powered on and operational",
            "☐ Cash register opened & drawer balanced",
            "☐ Hand washing stations fully stocked",
            "☐ Prep area sanitized and ready",
            "☐ Fresh produce inspection (quality, not expired)",
            "☐ Expiration date verification",
            "☐ Staff food safety briefing completed",
            "☐ Lighting & HVAC systems operational",
            "☐ Safety equipment accessible and stocked",
            "☐ Staff briefing & role assignments done",
            "☐ All staff ready for service",
        ]

        checklist_style = ParagraphStyle(
            'Checklist',
            fontName='Helvetica',
            fontSize=12,
            leading=20,
            leftIndent=20,
            spaceAfter=3,
        )

        for item in checklist_items:
            elements.append(Paragraph(item, checklist_style))

        elements.append(Spacer(1, 0.3*inch))

        # Notes section
        elements.append(Paragraph("<b>Notes / Issues Found:</b>", info_style))
        elements.append(Paragraph("_________________________________________________________________", info_style))
        elements.append(Paragraph("_________________________________________________________________", info_style))
        elements.append(Spacer(1, 0.2*inch))

        # Sign-off
        elements.append(Paragraph("<b>Manager Signature:</b> _________________________ <b>Time Completed:</b> _________", info_style))

        # Build PDF
        doc.build(elements)
        print(f"✓ Created {filename}")

    def create_closing_checklist_pdf(self):
        """Generate Closing Checklist PDF."""
        filename = f"{self.dir_name}/Closing-Checklist-{self.name_suffix}.pdf"

        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
        )

        elements = []

        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            fontName='Helvetica-Bold',
            fontSize=18,
            textColor=self.colors["primary"],
            spaceAfter=12,
            alignment=1
        )
        elements.append(Paragraph("DAILY CLOSING CHECKLIST", title_style))

        # Date and manager info
        info_style = ParagraphStyle(
            'Info',
            fontName='Helvetica',
            fontSize=11,
            spaceAfter=6,
        )
        elements.append(Paragraph(f"<b>Date:</b> _________________ <b>Manager:</b> _________________ <b>Est. Time: 45 minutes</b>", info_style))
        elements.append(Spacer(1, 0.2*inch))

        # Checklist items
        closing_items = [
            "☐ All customers have left the building",
            "☐ Kitchen deep clean (all surfaces & equipment)",
            "☐ Floor swept and mopped throughout",
            "☐ Trash emptied (all areas)",
            "☐ Compost emptied and secured",
            "☐ Beverage station cleaned and restocked",
            "☐ Bathrooms cleaned (toilet, sink, mirrors)",
            "☐ Front-of-house tables and chairs cleaned",
            "☐ Walk-in cooler temperature checked & logged",
            "☐ Freezer temperature checked & logged",
            "☐ All food properly stored in labeled containers",
            "☐ Equipment properly shut down",
            "☐ Lights off (except security/exit lights)",
            "☐ All doors locked and secured",
            "☐ Security system armed",
            "☐ Till counted and reconciled with manager",
        ]

        checklist_style = ParagraphStyle(
            'Checklist',
            fontName='Helvetica',
            fontSize=12,
            leading=20,
            leftIndent=20,
            spaceAfter=3,
        )

        for item in closing_items:
            elements.append(Paragraph(item, checklist_style))

        elements.append(Spacer(1, 0.2*inch))

        # Notes section
        elements.append(Paragraph("<b>Issues / Damage Reported:</b>", info_style))
        elements.append(Paragraph("_________________________________________________________________", info_style))

        elements.append(Spacer(1, 0.2*inch))

        # Sign-off
        elements.append(Paragraph("<b>Manager Signature:</b> _________________________ <b>Time Completed:</b> _________", info_style))

        doc.build(elements)
        print(f"✓ Created {filename}")

    def create_inventory_checklist_pdf(self):
        """Generate Inventory Checklist PDF."""
        filename = f"{self.dir_name}/Inventory-Checklist-{self.name_suffix}.pdf"

        doc = SimpleDocTemplate(
            filename,
            pagesize=landscape(letter),
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.5*inch,
            bottomMargin=0.5*inch,
        )

        elements = []

        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            fontName='Helvetica-Bold',
            fontSize=16,
            textColor=self.colors["primary"],
            spaceAfter=12,
            alignment=1
        )
        elements.append(Paragraph("WEEKLY INVENTORY CHECK", title_style))

        info_style = ParagraphStyle(
            'Info',
            fontName='Helvetica',
            fontSize=10,
            spaceAfter=6,
        )
        elements.append(Paragraph(f"<b>Week of:</b> _________________ <b>Checked by:</b> _________________ <b>Reorder Threshold: 30% of Par</b>", info_style))
        elements.append(Spacer(1, 0.15*inch))

        # Inventory table
        inventory_data = [
            ["Item", "Par Level", "Current Qty", "Status", "Supplier", "Notes"]
        ]

        items = [
            ["Chicken Breast (lbs)", "20", "", "", "", ""],
            ["Ground Beef (lbs)", "15", "", "", "", ""],
            ["Mixed Vegetables (lbs)", "25", "", "", "", ""],
            ["Olive Oil (gal)", "2", "", "", "", ""],
            ["Flour (lbs)", "10", "", "", "", ""],
            ["Pasta (lbs)", "5", "", "", "", ""],
            ["Rice (lbs)", "10", "", "", "", ""],
            ["Eggs (doz)", "30", "", "", "", ""],
            ["Butter (lbs)", "5", "", "", "", ""],
            ["Cheese (lbs)", "10", "", "", "", ""],
        ]

        inventory_data.extend(items)

        # Create table with styling
        table = Table(inventory_data, colWidths=[2*inch, 1.2*inch, 1.2*inch, 0.8*inch, 1.5*inch, 1.5*inch])

        table_style = TableStyle([
            # Header row
            ('BACKGROUND', (0, 0), (-1, 0), self.colors["primary"]),
            ('TEXTCOLOR', (0, 0), (-1, 0), self.colors["white"]),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            # Data rows
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F9F9F9")]),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ])

        table.setStyle(table_style)
        elements.append(table)

        elements.append(Spacer(1, 0.2*inch))

        # Items to reorder section
        elements.append(Paragraph("<b style='color: {}'>ITEMS BELOW 30% PAR - ORDER TODAY:</b>".format(self.colors["red"].hexval()), info_style))
        elements.append(Paragraph("_________________________________________________________________", info_style))
        elements.append(Paragraph("_________________________________________________________________", info_style))

        elements.append(Spacer(1, 0.15*inch))

        # Sign-off
        elements.append(Paragraph("<b>Checked by:</b> _________________________ <b>Date/Time:</b> _________", info_style))

        doc.build(elements)
        print(f"✓ Created {filename}")

    def create_quick_card_pdf(self):
        """Generate Quick Reference Card PDF (pocket-sized)."""
        filename = f"{self.dir_name}/Quick-Card-{self.name_suffix}.pdf"

        # Standard credit card size mockup on letter
        doc = SimpleDocTemplate(
            filename,
            pagesize=letter,
            rightMargin=0.5*inch,
            leftMargin=0.5*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch,
        )

        elements = []

        title_style = ParagraphStyle(
            'Title',
            fontName='Helvetica-Bold',
            fontSize=12,
            textColor=self.colors["primary"],
            spaceAfter=8,
            alignment=1
        )

        body_style = ParagraphStyle(
            'Body',
            fontName='Helvetica',
            fontSize=9,
            spaceAfter=4,
        )

        # Card 1: Opening Checklist Summary
        elements.append(Paragraph("OPENING CHECKLIST SUMMARY", title_style))
        opening_summary = [
            "✓ Equipment operational",
            "✓ Temperatures logged",
            "✓ POS system ready",
            "✓ Staff briefed",
            "✓ ~20 minutes to complete"
        ]
        for item in opening_summary:
            elements.append(Paragraph(item, body_style))

        elements.append(Spacer(1, 0.3*inch))

        # Card 2: Labor Cost Alert
        alert_style = ParagraphStyle(
            'Alert',
            fontName='Helvetica-Bold',
            fontSize=9,
            textColor=self.colors["red"],
            spaceAfter=4,
        )
        elements.append(Paragraph("⚠️ LABOR COST ALERT", alert_style))
        elements.append(Paragraph("Target: ≤30% of revenue", body_style))
        elements.append(Paragraph("Over? Review schedule for gaps", body_style))

        elements.append(Spacer(1, 0.3*inch))

        # Card 3: Inventory Reorder
        elements.append(Paragraph("INVENTORY REORDER", title_style))
        elements.append(Paragraph("RED (below 30% par) = Order today", body_style))
        elements.append(Paragraph("YELLOW (30-50% par) = Plan to order", body_style))
        elements.append(Paragraph("GREEN (above 50%) = You're good", body_style))

        elements.append(Spacer(1, 0.3*inch))

        # Card 4: Emergency Contacts
        elements.append(Paragraph("EMERGENCY CONTACTS", title_style))
        elements.append(Paragraph("Health Dept: _______________", body_style))
        elements.append(Paragraph("Gas Emergency: _______________", body_style))
        elements.append(Paragraph("Manager On-Call: _______________", body_style))

        doc.build(elements)
        print(f"✓ Created {filename}")

def main():
    """Generate PDFs for both aesthetics."""
    print("Generating PDF files...\n")

    for aesthetic in ["warm", "modern"]:
        gen = ChecklistPDFGenerator(aesthetic)
        print(f"\n📄 Creating {aesthetic.title()} PDFs:")
        gen.create_opening_checklist_pdf()
        gen.create_closing_checklist_pdf()
        gen.create_inventory_checklist_pdf()
        gen.create_quick_card_pdf()

    print("\n✅ All PDFs created successfully!")
    print("Ready for printing and laminating.")

if __name__ == "__main__":
    # Ensure directories exist
    os.makedirs("Warm-&-Inviting", exist_ok=True)
    os.makedirs("Modern-Restaurant-Specific", exist_ok=True)

    main()
