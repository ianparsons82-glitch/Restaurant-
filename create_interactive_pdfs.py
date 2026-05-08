#!/usr/bin/env python3
"""
Premium Interactive PDF Templates for Restaurant Operations Management
Creates 5 professional, interactive PDF templates with form fields
"""

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak, Frame, PageTemplate
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
    def __init__(self, template_key):
        self.template = TEMPLATES[template_key]
        self.template_key = template_key
        self.sig_color = colors.HexColor(self.template["color"])
        self.sig_color_light = self._lighten_color(self.template["rgb"])

    def _lighten_color(self, rgb, opacity=0.1):
        """Create a lighter tinted version of color for emphasis boxes."""
        r, g, b = rgb
        # Blend towards white with 10% opacity
        factor = 1 - opacity
        r_light = int(r * factor + 255 * opacity)
        g_light = int(g * factor + 255 * opacity)
        b_light = int(b * factor + 255 * opacity)
        return colors.Color(r_light / 255.0, g_light / 255.0, b_light / 255.0)

    def _create_header(self, c, width, height):
        """Draw premium header section."""
        # Header background
        c.setFillColor(self.sig_color)
        c.rect(0, height - 120, width, 120, fill=1, stroke=0)

        # Logo placeholder
        c.setFillColor(colors.HexColor("#CCCCCC"))
        c.rect(15, height - 105, 80, 80, fill=1, stroke=1)
        c.setStrokeColor(colors.HexColor("#999999"))
        c.setLineWidth(0.5)
        c.rect(15, height - 105, 80, 80, fill=0, stroke=1)

        # Logo text
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#666666"))
        c.drawCentredString(55, height - 60, "LOGO")

        # Restaurant info
        c.setFont("Helvetica-Bold", 18)
        c.setFillColor(colors.white)
        c.drawString(105, height - 45, "Restaurant Name")

        c.setFont("Helvetica", 10)
        c.drawString(105, height - 60, "123 Main Street, City, State 12345")

        c.setFont("Helvetica", 10)
        c.drawString(105, height - 75, "Manager: _________________________")

        # Template title (right aligned)
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(colors.white)
        title_width = c.stringWidth(self.template["name"], "Helvetica-Bold", 14)
        c.drawString(width - 15 - title_width, height - 45, self.template["name"])

        # Week of field
        c.setFont("Helvetica", 10)
        c.drawString(width - 15 - title_width, height - 65, "Week of: ________________")

    def _create_footer(self, c, width, height):
        """Draw footer section."""
        footer_y = 60

        # Border top
        c.setStrokeColor(colors.HexColor("#CCCCCC"))
        c.setLineWidth(0.5)
        c.line(15, footer_y + 40, width - 15, footer_y + 40)

        # Footer content
        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(15, footer_y + 20, "Completed by: _________________________")
        c.drawString(width - 15 - c.stringWidth("Date: _________________________", "Helvetica", 10),
                     footer_y + 20, "Date: _________________________")

    def _create_section_header(self, c, x, y, width, title, num):
        """Draw section header with signature color."""
        # Background
        c.setFillColor(self.sig_color)
        c.rect(x, y, width, 25, fill=1, stroke=0)

        # Text
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(colors.white)
        c.drawString(x + 10, y + 7, f"{num} {title}")

    def _create_checkbox_item(self, c, x, y, text, initials_width=25):
        """Draw checkbox item with initials field."""
        c.setFont("Helvetica", 11)
        c.setFillColor(colors.HexColor("#333333"))

        # Checkbox
        c.setStrokeColor(self.sig_color)
        c.setLineWidth(1)
        c.rect(x, y - 3, 12, 12, fill=0, stroke=1)

        # Text
        c.drawString(x + 18, y, text)

        # Initials field (underline)
        initials_x = x + 18 + c.stringWidth(text, "Helvetica", 11) + 10
        c.setStrokeColor(self.sig_color)
        c.setLineWidth(1)
        c.line(initials_x, y - 2, initials_x + initials_width, y - 2)

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#666666"))
        c.drawString(initials_x - c.stringWidth("Initials: ", "Helvetica", 9) - 5, y + 1, "Initials:")

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

        # Sections
        sections = [
            ("FACILITY INSPECTION", [
                "Building exterior checked",
                "Entrance doors unlocked & cleaned",
                "Windows/lights checked",
                "Parking lot inspected",
                "Entry mats clean and secure",
                "Interior lighting operational",
                "HVAC system operational",
                "No visible safety hazards",
            ]),
            ("EQUIPMENT & SAFETY", [
                "Fryer operational & temperature set",
                "Grill operational & preheated",
                "Ovens operational & temperature logged",
                "POS system powered on",
                "Walk-in cooler temperature logged",
                "Walk-in freezer temperature logged",
                "Fire extinguishers accessible",
                "First aid kit stocked",
            ]),
            ("KITCHEN PREP", [
                "Prep area sanitized & ready",
                "Fresh produce inspected",
                "Expiration dates verified",
                "Food storage organized",
                "Hand washing station stocked",
                "Sanitizer buckets prepared",
                "Cutting boards clean",
                "Ingredients at correct temperature",
            ]),
            ("FRONT OF HOUSE", [
                "Dining area cleaned",
                "Tables set properly",
                "Bathrooms cleaned & stocked",
                "Host stand organized",
                "Menus clean & complete",
                "Ambient temperature comfortable",
            ]),
            ("STAFF BRIEFING", [
                "Team arrived on time",
                "Safety briefing completed",
                "Daily specials communicated",
                "Staff roles assigned",
                "Service standards reviewed",
            ]),
        ]

        section_num = 1
        for section_title, items in sections:
            if current_y < margin + 150:  # Need new page
                self._create_footer(c, page_width, page_height)
                c.showPage()
                self._create_header(c, page_width, page_height)
                current_y = page_height - 140

            # Section header
            self._create_section_header(c, margin, current_y, section_width, section_title, section_num)
            current_y -= 35

            # Items
            for item in items:
                # Emphasis on safety/temp items
                is_important = any(keyword in item.lower() for keyword in ["temperature", "safety", "fire", "sanitizer"])

                if is_important:
                    c.setFillColor(self.sig_color_light)
                    c.rect(margin, current_y - 12, section_width, 16, fill=1, stroke=0)

                self._create_checkbox_item(c, margin + 10, current_y, item)
                current_y -= 20

                if current_y < margin + 80:
                    self._create_footer(c, page_width, page_height)
                    c.showPage()
                    self._create_header(c, page_width, page_height)
                    current_y = page_height - 140

            current_y -= 10
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
                "All customers have left",
                "Cash register reconciliation started",
                "Till counted accurately",
                "Cash secured in safe",
                "Daily sales record completed",
                "Payment methods reconciled",
                "Credit card batches closed",
                "Electronic payments verified",
                "Shift notes documented",
                "Manager notified of issues",
            ]),
            ("KITCHEN DEEP CLEAN", [
                "All cooking equipment cooled & cleaned",
                "Fryer oil drained & filtered",
                "Grill scraped & cleaned",
                "Oven interior wiped down",
                "Range hood filters cleaned",
                "Prep surfaces sanitized",
                "Cutting boards sanitized & stored",
                "Walk-in cooler organized & cleaned",
                "Walk-in freezer organized & cleaned",
                "Grease trap cleaned",
                "Floor swept & mopped thoroughly",
                "Wall baseboards wiped",
            ]),
            ("FRONT OF HOUSE CLOSE", [
                "All tables cleaned & chairs stacked",
                "Bathrooms cleaned & locked",
                "Toilet areas sanitized",
                "Sinks stocked with soap/towels",
                "Trash emptied from all areas",
                "Recycling bins emptied",
                "Compost properly secured",
                "Entry area swept & cleaned",
                "Host stand cleaned & organized",
                "Ambient music turned off",
                "Dining lights dimmed (except safety)",
            ]),
            ("INVENTORY & SECURITY", [
                "All doors locked & checked",
                "Windows locked & checked",
                "Security system armed",
                "Exterior lights operational",
                "Exit signs illuminated",
                "Emergency contact numbers posted",
                "All equipment powered down",
                "Non-essential lights off",
            ]),
            ("MANAGER SIGN-OFF", [
                "All sections complete & verified",
                "Issues documented for next shift",
                "Ready for next opening",
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

            for item in items:
                is_important = any(keyword in item.lower() for keyword in ["locked", "armed", "security", "emergency", "sanitized"])

                if is_important:
                    c.setFillColor(self.sig_color_light)
                    c.rect(margin, current_y - 12, usable_width, 16, fill=1, stroke=0)

                self._create_checkbox_item(c, margin + 10, current_y, item)
                current_y -= 20

                if current_y < margin + 80:
                    self._create_footer(c, page_width, page_height)
                    c.showPage()
                    self._create_header(c, page_width, page_height)
                    current_y = page_height - 140

            current_y -= 10
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
        c.drawString(margin, current_y, "1 SCHEDULE GRID")
        current_y -= 25

        # Table data
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Total Hours", "Labor $"]
        positions = ["Server", "Cook", "Host", "Bartender", "Manager"]

        # Draw table headers
        col_width = (page_width - 2 * margin - 100) / len(days)
        x_pos = margin + 100

        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "Position")

        for day in days:
            c.drawString(x_pos, current_y, day[:3])
            x_pos += col_width

        current_y -= 20

        # Draw rows
        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        for pos in positions:
            c.drawString(margin, current_y, pos)
            current_y -= 18
            c.setLineWidth(0.5)
            c.setStrokeColor(colors.HexColor("#CCCCCC"))
            c.line(margin, current_y + 2, page_width - margin, current_y + 2)

        current_y -= 20

        # Section 2: Labor Cost Summary
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "2 LABOR COST SUMMARY")
        current_y -= 25

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(margin, current_y, "Total Hours: __________ × Avg Rate: $__________ = Total Labor: $__________")
        current_y -= 20

        c.drawString(margin, current_y, "Expected Revenue (week): $__________")
        current_y -= 20

        c.drawString(margin, current_y, "Labor Cost %: __________")
        c.setFont("Helvetica", 8)
        c.setFillColor(colors.HexColor("#666666"))
        c.drawString(margin + 150, current_y, "(Target: <28%)")

        current_y -= 30

        # Section 3: Notes
        c.setFont("Helvetica-Bold", 11)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "3 NOTES & SCHEDULING ALERTS")
        current_y -= 25

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(margin, current_y, "__________________________________________________________________")
        current_y -= 20
        c.drawString(margin, current_y, "__________________________________________________________________")
        current_y -= 20
        c.drawString(margin, current_y, "__________________________________________________________________")

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

        # Section 1: Current Inventory Levels
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "1 CURRENT INVENTORY LEVELS")
        current_y -= 25

        # Table header
        headers = ["Item", "Current Qty", "Par Level", "Status", "Reorder?"]
        col_widths = [2, 1.2, 1, 0.8, 0.8]
        x_pos = margin

        c.setFont("Helvetica-Bold", 9)
        c.setFillColor(colors.white)

        for header, width in zip(headers, col_widths):
            header_width = width * inch
            c.setFillColor(self.sig_color)
            c.rect(x_pos, current_y - 18, header_width, 18, fill=1, stroke=1)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 9)
            c.drawString(x_pos + 5, current_y - 10, header)
            x_pos += header_width

        current_y -= 25

        # Inventory items
        items = [
            "Chicken Breast", "Ground Beef", "Fish Fillets", "Vegetables Mix",
            "Olive Oil", "Flour", "Pasta", "Rice", "Eggs", "Butter",
            "Cheese", "Milk", "Cream", "Salt", "Sugar"
        ]

        c.setFont("Helvetica", 9)
        for item in items:
            x_pos = margin

            # Item name
            c.setFillColor(colors.HexColor("#F5F5F5"))
            c.rect(x_pos, current_y - 15, 2 * inch, 15, fill=1, stroke=1)
            c.setFillColor(colors.HexColor("#333333"))
            c.drawString(x_pos + 5, current_y - 8, item)

            x_pos += 2 * inch

            # Other columns (editable spaces)
            for width in col_widths[1:]:
                c.setFillColor(colors.white)
                c.rect(x_pos, current_y - 15, width * inch, 15, fill=1, stroke=1)
                x_pos += width * inch

            current_y -= 16

            if current_y < margin + 150:
                self._create_footer(c, page_width, page_height)
                c.showPage()
                self._create_header(c, page_width, page_height)
                current_y = page_height - 140

        current_y -= 20

        # Section 2: Reorder Summary
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "2 REORDER SUMMARY")
        current_y -= 25

        c.setFont("Helvetica", 9)
        c.setFillColor(colors.HexColor("#333333"))
        for i in range(5):
            c.drawString(margin, current_y, "• ______________________________")
            current_y -= 18

        current_y -= 20

        # Section 3: Delivery Tracking
        c.setFont("Helvetica-Bold", 12)
        c.setFillColor(self.sig_color)
        c.drawString(margin, current_y, "3 DELIVERY TRACKING")
        current_y -= 25

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        c.drawString(margin, current_y, "Date Received: ________________")
        current_y -= 20
        c.drawString(margin, current_y, "Supplier: ________________")
        current_y -= 20
        c.drawString(margin, current_y, "Received by (Initials): ________________")
        current_y -= 20
        c.drawString(margin, current_y, "Issues: ________________________________________________________________")

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
        current_y -= 35

        # Emphasis background
        c.setFillColor(self.sig_color_light)
        c.rect(margin, current_y - 100, usable_width, 100, fill=1, stroke=0)

        priorities = [
            "Task 1: _________________________________________________________________",
            "Task 2: _________________________________________________________________",
            "Task 3: _________________________________________________________________",
            "Task 4: _________________________________________________________________",
            "Task 5: _________________________________________________________________",
        ]

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        for priority in priorities:
            c.drawString(margin + 10, current_y, priority)
            current_y -= 18

        current_y -= 25

        # Section 2: Daily Recurring Tasks
        self._create_section_header(c, margin, current_y, usable_width, "DAILY RECURRING TASKS", 2)
        current_y -= 35

        daily_tasks = [
            "Check opening checklist completion",
            "Review overnight issues/notes",
            "Staff briefing prep",
            "Check closing checklist completion",
            "Review sales/labor numbers",
        ]

        for task in daily_tasks:
            self._create_checkbox_item(c, margin + 10, current_y, task, initials_width=20)
            current_y -= 20

        current_y -= 25

        # Section 3: Weekly Tasks
        self._create_section_header(c, margin, current_y, usable_width, "WEEKLY TASKS", 3)
        current_y -= 35

        weekly_tasks = [
            "Review schedule for next week",
            "Review labor cost analysis",
            "Inventory ordering",
            "Staff performance check-ins",
            "Customer feedback review",
        ]

        for task in weekly_tasks:
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.HexColor("#333333"))

            # Checkbox
            c.setStrokeColor(self.sig_color)
            c.setLineWidth(1)
            c.rect(margin + 10, current_y - 3, 12, 12, fill=0, stroke=1)

            # Task text
            c.drawString(margin + 28, current_y, task)

            # Due date field
            due_x = margin + 400
            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#666666"))
            c.drawString(due_x - c.stringWidth("Complete by: ", "Helvetica", 9) - 5, current_y + 1, "Complete by:")

            c.setStrokeColor(self.sig_color)
            c.setLineWidth(1)
            c.line(due_x, current_y - 2, due_x + 80, current_y - 2)

            current_y -= 20

        current_y -= 25

        # Section 4: Notes & Follow-ups
        self._create_section_header(c, margin, current_y, usable_width, "NOTES & FOLLOW-UPS", 4)
        current_y -= 35

        c.setFont("Helvetica", 10)
        c.setFillColor(colors.HexColor("#333333"))
        for i in range(4):
            c.drawString(margin, current_y, "_" * 95)
            current_y -= 18

        self._create_footer(c, page_width, page_height)
        c.save()
        print(f"✓ Created {filename}")

def main():
    """Generate all 5 premium interactive PDFs."""
    print("🎨 Creating Premium Interactive PDF Templates...\n")

    # Create opening checklist
    gen_opening = PremiumPDFGenerator("opening_checklist")
    gen_opening.create_opening_checklist()

    # Create closing checklist
    gen_closing = PremiumPDFGenerator("closing_checklist")
    gen_closing.create_closing_checklist()

    # Create weekly schedule
    gen_schedule = PremiumPDFGenerator("weekly_schedule")
    gen_schedule.create_weekly_schedule()

    # Create inventory sheet
    gen_inventory = PremiumPDFGenerator("inventory_sheet")
    gen_inventory.create_inventory_sheet()

    # Create manager tasks
    gen_tasks = PremiumPDFGenerator("manager_tasks")
    gen_tasks.create_manager_tasks()

    print("\n✅ All 5 premium PDFs created successfully!")
    print("\n📋 Generated Files:")
    for key, template in TEMPLATES.items():
        print(f"  • {template['file']} - {template['name']}")
    print("\n💾 Files are ready for download and use!")

if __name__ == "__main__":
    main()
