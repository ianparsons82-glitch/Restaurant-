#!/usr/bin/env python3
"""
Premium Interactive PDF Templates for Restaurant Operations Management
Creates 5 professional, interactive PDF templates with form fields and professional design
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from datetime import datetime
import os

# Template definitions with signature colors
TEMPLATES = {
    "opening_checklist": {
        "name": "Daily Opening Checklist",
        "color": "#DC3545",  # RED
        "rgb": (220, 53, 69),
        "file": "opening-checklist.pdf"
    },
    "closing_checklist": {
        "name": "Daily Closing Checklist",
        "color": "#FF9800",  # ORANGE
        "rgb": (255, 152, 0),
        "file": "closing-checklist.pdf"
    },
    "weekly_schedule": {
        "name": "Weekly Schedule & Labor Tracker",
        "color": "#2196F3",  # BLUE
        "rgb": (33, 150, 243),
        "file": "weekly-schedule.pdf"
    },
    "inventory_sheet": {
        "name": "Inventory Management Sheet",
        "color": "#4CAF50",  # GREEN
        "rgb": (76, 175, 80),
        "file": "inventory-sheet.pdf"
    },
    "manager_tasks": {
        "name": "Manager Daily & Weekly Tasks",
        "color": "#9C27B0",  # PURPLE
        "rgb": (156, 39, 176),
        "file": "manager-tasks.pdf"
    }
}

class PremiumPDFGenerator:
    """Generates premium interactive PDF templates for restaurant operations."""

    def __init__(self, template_key, restaurant_name="Restaurant Name",
                 restaurant_address="123 Main Street, City, State 12345"):
        """Initialize PDF generator with template and restaurant info."""
        self.template = TEMPLATES[template_key]
        self.template_key = template_key
        self.sig_color = colors.HexColor(self.template["color"])
        self.sig_color_light = self._lighten_color(self.template["rgb"])
        self.restaurant_name = restaurant_name
        self.restaurant_address = restaurant_address

    def _lighten_color(self, rgb, opacity=0.1):
        """Create a lighter tinted version of color for emphasis boxes."""
        r, g, b = rgb
        factor = 1 - opacity
        r_light = int(r * factor + 255 * opacity)
        g_light = int(g * factor + 255 * opacity)
        b_light = int(b * factor + 255 * opacity)
        return colors.Color(r_light / 255.0, g_light / 255.0, b_light / 255.0)

    def _create_header(self, c, width, height):
        """Draw premium header section with logo, restaurant info, and title."""
        # Header background (full width)
        c.setFillColor(self.sig_color)
        c.rect(0, height - 120, width, 120, fill=1, stroke=0)

        # Logo placeholder (80x80 left side)
        c.setFillColor(colors.HexColor("#E8E8E8"))
        c.rect(15, height - 105, 80, 80, fill=1, stroke=1)
        c.setStrokeColor(colors.HexColor("#999999"))
        c.setLineWidth(0.5)
        c.rect(15, height - 105, 80, 80, fill=0, stroke=1)

        # Logo text
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#666666"))
        c.drawCentredString(55, height - 60, "LOGO")

        # Restaurant Name
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(colors.white)
        c.drawString(105, height - 48, self.restaurant_name)

        # Restaurant Address
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#F0F0F0"))
        c.drawString(105, height - 62, self.restaurant_address)

        # Manager field
        c.setFont("Helvetica", 9)
        c.drawString(105, height - 76, "Manager: ________________________")

        # Template title (right aligned)
        c.setFont("Helvetica-Bold", 13)
        c.setFillColor(colors.white)
        title_width = c.stringWidth(self.template["name"], "Helvetica-Bold", 13)
        c.drawString(width - 15 - title_width, height - 48, self.template["name"])

        # Week of field
        c.setFont("Helvetica", 9)
        c.drawString(width - 15 - c.stringWidth("Week of: __________________", "Helvetica", 9),
                     height - 68, "Week of: __________________")

    def _create_footer(self, c, width, height):
        """Draw footer with completion tracking fields."""
        footer_y = 50

        # Dividing line
        c.setStrokeColor(colors.HexColor("#CCCCCC"))
        c.setLineWidth(0.5)
        c.line(15, footer_y + 45, width - 15, footer_y + 45)

        # Footer content
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(15, footer_y + 20, "Completed by: __________________________")

        date_text = "Date: __________________________"
        date_width = c.stringWidth(date_text, "Helvetica", 9)
        c.drawString(width - 15 - date_width, footer_y + 20, date_text)

        # Footer note
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#888888"))
        c.drawString(15, footer_y + 5, "Archive completed documents for compliance records")

    def _create_section_header(self, c, x, y, width, title, num):
        """Draw section header with signature color background."""
        # Background
        c.setFillColor(self.sig_color)
        c.rect(x, y, width, 26, fill=1, stroke=0)

        # Section number and title
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(colors.white)
        c.drawString(x + 10, y + 8, f"{num}  {title}")

    def _create_checkbox_item(self, c, x, y, text, initials_width=25, emphasized=False):
        """Draw checkbox item with optional initials field and emphasis."""
        # Emphasis background if important
        if emphasized:
            c.setFillColor(self.sig_color_light)
            c.rect(x - 5, y - 15, 500, 18, fill=1, stroke=0)

        # Checkbox
        c.setStrokeColor(self.sig_color)
        c.setLineWidth(1.2)
        c.rect(x, y - 4, 12, 12, fill=0, stroke=1)

        # Item text
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(x + 18, y, text)

        # Initials field
        initials_x = x + 20 + c.stringWidth(text, "Helvetica", 10) + 8
        if initials_x < 500:  # Ensure field fits on page
            c.setStrokeColor(self.sig_color)
            c.setLineWidth(0.8)
            c.line(initials_x, y - 2, initials_x + initials_width, y - 2)

    def _draw_emphasis_box(self, c, x, y, width, height):
        """Draw emphasis box background for important items."""
        c.setFillColor(self.sig_color_light)
        c.rect(x, y, width, height, fill=1, stroke=0)

    def create_opening_checklist(self):
        """Create Daily Opening Checklist PDF."""
        filename = self.template["file"]
        page_width, page_height = letter

        c = canvas.Canvas(filename, pagesize=letter)
        margin = 0.75 * inch
        usable_width = page_width - (2 * margin)

        # Header
        self._create_header(c, page_width, page_height)
        current_y = page_height - 140
        section_width = usable_width

        # Content sections
        sections = [
            ("FACILITY INSPECTION", [
                ("Building exterior checked", False),
                ("Entrance doors unlocked & cleaned", False),
                ("Windows/lights checked", False),
                ("Parking lot inspected", False),
                ("Entry mats clean and secure", False),
                ("Interior lighting operational", False),
                ("HVAC system operational", True),
                ("No visible safety hazards", True),
                ("Floors clean and safe", False),
                ("All areas accessible", False),
            ]),
            ("EQUIPMENT & SAFETY", [
                ("Fryer operational & temperature set", True),
                ("Grill operational & preheated", True),
                ("Ovens operational & temperature logged", True),
                ("POS system powered on", False),
                ("Walk-in cooler temperature logged", True),
                ("Walk-in freezer temperature logged", True),
                ("Fire extinguishers accessible", True),
                ("First aid kit stocked", True),
                ("Emergency exits clear", True),
            ]),
            ("KITCHEN PREP", [
                ("Prep area sanitized & ready", False),
                ("Fresh produce inspected", False),
                ("Expiration dates verified", False),
                ("Food storage organized", False),
                ("Hand washing station stocked", True),
                ("Sanitizer buckets prepared", True),
                ("Cutting boards clean & sanitized", False),
                ("Ingredients at correct temperature", True),
                ("Cooler/freezer organized", False),
            ]),
            ("FRONT OF HOUSE", [
                ("Dining area cleaned", False),
                ("Tables set properly", False),
                ("Bathrooms cleaned & stocked", False),
                ("Host stand organized", False),
                ("Menus clean & complete", False),
                ("Ambient temperature comfortable", False),
            ]),
            ("STAFF BRIEFING", [
                ("Team arrived on time", False),
                ("Safety briefing completed", True),
                ("Daily specials communicated", False),
                ("Staff roles assigned", False),
                ("Service standards reviewed", False),
            ]),
        ]

        section_num = 1
        for section_title, items in sections:
            # Page break if needed
            if current_y < margin + 150:
                self._create_footer(c, page_width, page_height)
                c.showPage()
                self._create_header(c, page_width, page_height)
                current_y = page_height - 140

            # Section header
            self._create_section_header(c, margin, current_y, section_width, section_title, section_num)
            current_y -= 35

            # Items
            for item_text, is_emphasized in items:
                self._create_checkbox_item(c, margin + 10, current_y, item_text, emphasized=is_emphasized)
                current_y -= 18

                if current_y < margin + 80:
                    self._create_footer(c, page_width, page_height)
                    c.showPage()
                    self._create_header(c, page_width, page_height)
                    current_y = page_height - 140

            current_y -= 8
            section_num += 1

        # Footer
        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

    def create_closing_checklist(self):
        """Create Daily Closing Checklist PDF."""
        filename = self.template["file"]
        page_width, page_height = letter

        c = canvas.Canvas(filename, pagesize=letter)
        margin = 0.75 * inch
        usable_width = page_width - (2 * margin)

        self._create_header(c, page_width, page_height)
        current_y = page_height - 140

        sections = [
            ("END OF SERVICE", [
                ("All customers have left", False),
                ("Cash register reconciliation started", False),
                ("Till counted accurately", False),
                ("Cash secured in safe", True),
                ("Daily sales record completed", False),
                ("Payment methods reconciled", False),
                ("Credit card batches closed", False),
                ("Electronic payments verified", False),
                ("Shift notes documented", False),
                ("Manager notified of issues", False),
            ]),
            ("KITCHEN DEEP CLEAN", [
                ("All cooking equipment cooled & cleaned", False),
                ("Fryer oil drained & filtered", False),
                ("Grill scraped & cleaned", False),
                ("Oven interior wiped down", False),
                ("Range hood filters cleaned", False),
                ("Prep surfaces sanitized", True),
                ("Cutting boards sanitized & stored", True),
                ("Walk-in cooler organized & cleaned", False),
                ("Walk-in freezer organized & cleaned", False),
                ("Grease trap cleaned", True),
                ("Floor swept & mopped thoroughly", False),
                ("Wall baseboards wiped", False),
                ("Storage areas organized", False),
            ]),
            ("FRONT OF HOUSE CLOSE", [
                ("All tables cleaned & chairs stacked", False),
                ("Bathrooms cleaned & locked", False),
                ("Toilet areas sanitized", True),
                ("Sinks stocked with soap/towels", False),
                ("Trash emptied from all areas", False),
                ("Recycling bins emptied", False),
                ("Compost properly secured", True),
                ("Entry area swept & cleaned", False),
                ("Host stand cleaned & organized", False),
                ("Ambient music turned off", False),
                ("Dining lights dimmed (except safety)", False),
            ]),
            ("INVENTORY & SECURITY", [
                ("All doors locked & checked", True),
                ("Windows locked & checked", True),
                ("Security system armed", True),
                ("Exterior lights operational", True),
                ("Exit signs illuminated", True),
                ("Emergency contact numbers posted", False),
                ("All equipment powered down", False),
                ("Non-essential lights off", False),
            ]),
            ("MANAGER SIGN-OFF", [
                ("All sections complete & verified", False),
                ("Issues documented for next shift", False),
                ("Ready for next opening", False),
            ]),
        ]

        section_num = 1
        for section_title, items in sections:
            if current_y < margin + 150:
                self._create_footer(c, page_width, page_height)
                c.showPage()
                self._create_header(c, page_width, page_height)
                current_y = page_height - 140

            self._create_section_header(c, margin, current_y, usable_width, section_title, section_num)
            current_y -= 35

            for item_text, is_emphasized in items:
                self._create_checkbox_item(c, margin + 10, current_y, item_text, emphasized=is_emphasized)
                current_y -= 18

                if current_y < margin + 80:
                    self._create_footer(c, page_width, page_height)
                    c.showPage()
                    self._create_header(c, page_width, page_height)
                    current_y = page_height - 140

            current_y -= 8
            section_num += 1

        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

    def create_weekly_schedule(self):
        """Create Weekly Schedule & Labor Cost Tracker."""
        filename = self.template["file"]
        page_width, page_height = landscape(letter)

        c = canvas.Canvas(filename, pagesize=landscape(letter))
        margin = 0.75 * inch

        self._create_header(c, page_width, page_height)
        current_y = page_height - 140

        # Section 1: Schedule Grid
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "1  WEEKLY SCHEDULE GRID")
        current_y -= 28

        # Days of week
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Total", "Cost"]
        positions = ["Server", "Cook", "Host", "Bartender", "Manager", "Assistant Manager"]

        # Table dimensions
        col_width = (page_width - 2*margin - 100) / len(days)
        row_height = 18

        # Headers
        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "Position")

        x_pos = margin + 100
        for day in days:
            c.drawString(x_pos + col_width/2 - c.stringWidth(day, "Helvetica-Bold", 9)/2,
                         current_y, day)
            x_pos += col_width

        current_y -= row_height
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor("#CCCCCC"))
        c.line(margin, current_y, page_width - margin, current_y)

        # Position rows
        c.setFont("Helvetica", 9)
        for i, pos in enumerate(positions):
            c.setFillColor(colors.HexColor("#333333"))
            c.drawString(margin + 5, current_y - 4, pos)

            # Alternating row backgrounds
            if i % 2 == 0:
                c.setFillColor(colors.HexColor("#F8F8F8"))
            else:
                c.setFillColor(colors.white)

            x_pos = margin + 100
            for _ in days:
                c.rect(x_pos, current_y - row_height, col_width, row_height, fill=1, stroke=1)
                x_pos += col_width

            current_y -= row_height

        current_y -= 20

        # Labor Cost Summary
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "2  LABOR COST SUMMARY")
        current_y -= 25

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(margin, current_y, "Total Hours: ________ × Avg Rate: $________ = Total Labor $: ________")
        current_y -= 20

        c.drawString(margin, current_y, "Expected Revenue (week): $__________  |  Labor Cost %: __________  (Target: <28%)")
        current_y -= 25

        # Notes
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "3  NOTES & SCHEDULING ALERTS")
        current_y -= 18

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        for _ in range(3):
            c.drawString(margin, current_y, "_" * 120)
            current_y -= 16

        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

    def create_inventory_sheet(self):
        """Create Inventory Management Sheet."""
        filename = self.template["file"]
        page_width, page_height = letter

        c = canvas.Canvas(filename, pagesize=letter)
        margin = 0.75 * inch
        usable_width = page_width - (2 * margin)

        self._create_header(c, page_width, page_height)
        current_y = page_height - 140

        # Section 1: Inventory Levels
        self._create_section_header(c, margin, current_y, usable_width, "CURRENT INVENTORY LEVELS", 1)
        current_y -= 30

        # Table header
        headers = ["Item", "Current Qty", "Par Level", "Status", "Reorder?"]
        col_widths = [2.0, 1.2, 1.0, 0.8, 0.7]
        x_pos = margin

        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(colors.white)
        header_y = current_y

        for header, width in zip(headers, col_widths):
            header_width = width * inch
            c.setFillColor(self.sig_color)
            c.rect(x_pos, current_y - 18, header_width, 18, fill=1, stroke=1)
            c.setFillColor(colors.white)
            c.drawString(x_pos + 5, current_y - 10, header)
            x_pos += header_width

        current_y -= 20

        # Inventory items
        items = [
            "Chicken Breast", "Ground Beef", "Fish Fillets", "Beef Ribs", "Vegetables Mix",
            "Olive Oil", "Flour", "Pasta", "Rice", "Eggs", "Butter", "Cheese", "Milk",
            "Cream", "Salt", "Sugar"
        ]

        c.setFont("Helvetica", 9)
        c.setLineWidth(0.5)
        c.setStrokeColor(colors.HexColor("#CCCCCC"))

        for i, item in enumerate(items):
            x_pos = margin

            # Item name
            if i % 2 == 0:
                c.setFillColor(colors.HexColor("#F9F9F9"))
            else:
                c.setFillColor(colors.white)

            c.rect(x_pos, current_y - 15, 2.0 * inch, 15, fill=1, stroke=1)
            c.setFillColor(colors.HexColor("#333333"))
            c.drawString(x_pos + 5, current_y - 8, item)

            x_pos += 2.0 * inch

            # Other columns (editable spaces)
            for width in col_widths[1:]:
                if i % 2 == 0:
                    c.setFillColor(colors.HexColor("#F9F9F9"))
                else:
                    c.setFillColor(colors.white)
                c.rect(x_pos, current_y - 15, width * inch, 15, fill=1, stroke=1)
                x_pos += width * inch

            current_y -= 16

            if current_y < margin + 150:
                self._create_footer(c, page_width, page_height)
                c.showPage()
                self._create_header(c, page_width, page_height)
                current_y = page_height - 140

        current_y -= 15

        # Section 2: Reorder Summary
        self._create_section_header(c, margin, current_y, usable_width, "REORDER SUMMARY", 2)
        current_y -= 30

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        for i in range(6):
            c.drawString(margin + 10, current_y, f"• _______________________________")
            current_y -= 15

        current_y -= 15

        # Section 3: Delivery Tracking
        self._create_section_header(c, margin, current_y, usable_width, "DELIVERY TRACKING", 3)
        current_y -= 30

        c.setFont("Helvetica", 9)
        fields = [
            "Date Received: ________________________",
            "Supplier: ________________________",
            "Received by (Initials): ________________________",
            "Issues/Discrepancies: _________________________________________________________",
        ]

        for field in fields:
            c.drawString(margin, current_y, field)
            current_y -= 16

        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

    def create_manager_tasks(self):
        """Create Manager Daily & Weekly Tasks."""
        filename = self.template["file"]
        page_width, page_height = letter

        c = canvas.Canvas(filename, pagesize=letter)
        margin = 0.75 * inch
        usable_width = page_width - (2 * margin)

        self._create_header(c, page_width, page_height)
        current_y = page_height - 140

        # Section 1: Today's Priorities
        self._create_section_header(c, margin, current_y, usable_width, "TODAY'S PRIORITIES", 1)
        current_y -= 30

        # Emphasis box
        c.setFillColor(self.sig_color_light)
        c.rect(margin, current_y - 98, usable_width, 100, fill=1, stroke=0)

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))

        for i in range(5):
            c.drawString(margin + 10, current_y, f"{i+1}. _______________________________________________________")
            current_y -= 18

        current_y -= 20

        # Section 2: Daily Recurring Tasks
        self._create_section_header(c, margin, current_y, usable_width, "DAILY RECURRING TASKS", 2)
        current_y -= 30

        daily_tasks = [
            "Check opening checklist completion",
            "Review overnight issues/notes",
            "Staff briefing preparation",
            "Check closing checklist completion",
            "Review sales/labor numbers",
        ]

        for task in daily_tasks:
            self._create_checkbox_item(c, margin + 10, current_y, task, initials_width=20)
            current_y -= 18

        current_y -= 20

        # Section 3: Weekly Tasks
        self._create_section_header(c, margin, current_y, usable_width, "WEEKLY TASKS", 3)
        current_y -= 30

        weekly_tasks = [
            "Review & finalize next week's schedule",
            "Review labor cost analysis",
            "Process inventory ordering",
            "Conduct staff performance check-ins",
            "Review customer feedback",
        ]

        for task in weekly_tasks:
            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#333333"))

            # Checkbox
            c.setStrokeColor(self.sig_color)
            c.setLineWidth(1)
            c.rect(margin + 10, current_y - 4, 12, 12, fill=0, stroke=1)

            # Task text
            c.drawString(margin + 28, current_y, task)

            # Due date
            due_text = "Complete by: _______________"
            c.drawString(margin + 380, current_y, due_text)

            current_y -= 18

        current_y -= 20

        # Section 4: Notes & Follow-ups
        self._create_section_header(c, margin, current_y, usable_width, "NOTES & FOLLOW-UPS", 4)
        current_y -= 30

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        for i in range(5):
            c.drawString(margin, current_y, "_" * 95)
            current_y -= 16

        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

def main():
    """Generate all 5 premium interactive PDFs."""
    print("🎨 Creating Premium Interactive PDF Templates...\n")
    print("=" * 60)

    templates = [
        ("opening_checklist", "Daily Opening Checklist"),
        ("closing_checklist", "Daily Closing Checklist"),
        ("weekly_schedule", "Weekly Schedule & Labor Tracker"),
        ("inventory_sheet", "Inventory Management Sheet"),
        ("manager_tasks", "Manager Daily & Weekly Tasks"),
    ]

    for template_key, description in templates:
        gen = PremiumPDFGenerator(template_key)
        print(f"\n📄 {description}")

        if template_key == "opening_checklist":
            gen.create_opening_checklist()
        elif template_key == "closing_checklist":
            gen.create_closing_checklist()
        elif template_key == "weekly_schedule":
            gen.create_weekly_schedule()
        elif template_key == "inventory_sheet":
            gen.create_inventory_sheet()
        elif template_key == "manager_tasks":
            gen.create_manager_tasks()

    print("\n" + "=" * 60)
    print("\n✅ All 5 premium PDFs created successfully!")
    print("\n📋 Generated Files:")
    print("   • opening-checklist.pdf        (Daily opening procedures)")
    print("   • closing-checklist.pdf        (Daily closing procedures)")
    print("   • weekly-schedule.pdf          (Staff scheduling & labor)")
    print("   • inventory-sheet.pdf          (Inventory management)")
    print("   • manager-tasks.pdf            (Manager task tracking)")
    print("\n💾 Files are ready for download, printing, and lamination!")
    print("\n📖 See PDF_TEMPLATES_GUIDE.md for detailed documentation.")

if __name__ == "__main__":
    main()
