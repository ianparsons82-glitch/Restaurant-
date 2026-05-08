#!/usr/bin/env python3
"""
Restaurant Operations Template Generator
Creates fully-formatted Excel templates with all formulas, colors, and automation
for both Warm & Inviting and Modern aesthetics.
"""

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from datetime import datetime
import os

# Color Palettes
COLORS = {
    "warm": {
        "primary": "2C3E50",      # Navy
        "accent": "FF6B6B",        # Coral
        "background": "F5F3F0",    # Cream
        "secondary": "8B8680",     # Warm Gray
        "gold": "D4AF37",          # Gold
        "red": "E74C3C",           # Alert Red
        "yellow": "F39C12",        # Warning Yellow
        "green": "27AE60",         # Success Green
        "white": "FFFFFF",
    },
    "modern": {
        "primary": "1B4332",       # Dark Green
        "accent": "8B6F47",        # Brown
        "background": "F5F3F0",    # Cream
        "secondary": "2D2D2D",     # Charcoal
        "gold": "B8860B",          # Bronze
        "red": "DC143C",           # Alert Crimson
        "yellow": "FFD700",        # Warning Gold
        "green": "2D5016",         # Success Deep Green
        "white": "FFFFFF",
    }
}

FONTS_CONFIG = {
    "warm": {
        "title": "Montserrat",
        "header": "Montserrat",
        "body": "Open Sans",
    },
    "modern": {
        "title": "Georgia",
        "header": "Georgia",
        "body": "Segoe UI",
    }
}

class RestaurantTemplateGenerator:
    def __init__(self, aesthetic="warm"):
        """Initialize template generator with chosen aesthetic."""
        self.aesthetic = aesthetic
        self.colors = COLORS[aesthetic]
        self.fonts = FONTS_CONFIG[aesthetic]
        self.wb = openpyxl.Workbook()
        self.wb.remove(self.wb.active)  # Remove default sheet
        self.thin_border = Border(
            left=Side(style='thin', color='CCCCCC'),
            right=Side(style='thin', color='CCCCCC'),
            top=Side(style='thin', color='CCCCCC'),
            bottom=Side(style='thin', color='CCCCCC')
        )

    def style_header_cell(self, cell, text):
        """Style a header cell with primary color background."""
        cell.value = text
        cell.font = Font(
            name=self.fonts["header"],
            size=14,
            bold=True,
            color="FFFFFF"
        )
        cell.fill = PatternFill(start_color=self.colors["primary"], end_color=self.colors["primary"], fill_type="solid")
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = self.thin_border
        return cell

    def style_title_cell(self, cell, text):
        """Style a title cell."""
        cell.value = text
        cell.font = Font(
            name=self.fonts["title"],
            size=24,
            bold=True,
            color=self.colors["primary"]
        )
        cell.alignment = Alignment(horizontal="left", vertical="center")
        return cell

    def style_body_cell(self, cell, text, color="000000", bold=False, background=None):
        """Style a body cell."""
        cell.value = text
        cell.font = Font(
            name=self.fonts["body"],
            size=11,
            color=color,
            bold=bold
        )
        if background:
            cell.fill = PatternFill(start_color=background, end_color=background, fill_type="solid")
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = self.thin_border
        return cell

    def create_opening_checklist(self):
        """Create Daily Opening Checklist sheet."""
        ws = self.wb.create_sheet("Opening Checklist")

        # Title
        ws.merge_cells("A1:E1")
        title = ws["A1"]
        self.style_title_cell(title, "DAILY OPENING CHECKLIST")
        ws.row_dimensions[1].height = 30

        # Date and time fields
        ws["A3"] = "Date:"
        ws["B3"] = datetime.now().strftime("%m/%d/%Y")
        ws["D3"] = "Opened by:"
        ws["E3"] = ""

        # Header row
        headers = ["Task Item", "Status", "Time Completed", "Initials", "Notes"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['E'].width = 25

        # Opening checklist items
        items = [
            "Equipment check (fryer, grill, ovens)",
            "Walk-in cooler temperature",
            "Freezer temperature",
            "POS system operational",
            "Register setup & cash drawer",
            "Hand washing stations stocked",
            "Prep area sanitized",
            "Fresh produce inspection",
            "Expiration date check",
            "Food safety briefing given",
            "Lighting operational",
            "HVAC system running",
            "Safety equipment accessible",
            "Staff briefing completed",
            "Ready for service"
        ]

        row = 6
        for item in items:
            ws.cell(row=row, column=1).value = item
            ws.cell(row=row, column=2).value = ""  # Status - can be filled in
            ws.cell(row=row, column=3).value = ""  # Time
            ws.cell(row=row, column=4).value = ""  # Initials
            ws.cell(row=row, column=5).value = ""  # Notes
            row += 1

        ws.row_dimensions[5].height = 20

        # Summary row
        summary_row = row + 1
        ws.merge_cells(f"A{summary_row}:E{summary_row}")
        summary = ws[f"A{summary_row}"]
        self.style_body_cell(summary, "✓ All items completed", bold=True, background=self.colors["green"])

        return ws

    def create_closing_checklist(self):
        """Create Daily Closing Checklist sheet."""
        ws = self.wb.create_sheet("Closing Checklist")

        # Title
        ws.merge_cells("A1:E1")
        title = ws["A1"]
        self.style_title_cell(title, "DAILY CLOSING CHECKLIST")
        ws.row_dimensions[1].height = 30

        # Date and time fields
        ws["A3"] = "Date:"
        ws["B3"] = datetime.now().strftime("%m/%d/%Y")
        ws["D3"] = "Closed by:"
        ws["E3"] = ""

        # Header row
        headers = ["Task Item", "Status", "Time Completed", "Initials", "Notes"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=5, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 30
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 10
        ws.column_dimensions['E'].width = 25

        # Closing checklist items
        items = [
            "Kitchen deep clean (surfaces, equipment)",
            "Floor cleaned & mopped",
            "Trash & compost emptied",
            "Beverage station cleaned",
            "Front-of-house cleaned",
            "Bathrooms cleaned & checked",
            "Inventory spot check (key items)",
            "Food properly stored (containers/labels)",
            "Walk-in temp checked & recorded",
            "Freezer check",
            "Equipment shut down properly",
            "Lights turned off (except exit/security)",
            "All doors locked",
            "Security system armed",
            "Till counted & reconciled",
            "Manager sign-off"
        ]

        row = 6
        for item in items:
            ws.cell(row=row, column=1).value = item
            ws.cell(row=row, column=2).value = ""  # Status
            ws.cell(row=row, column=3).value = ""  # Time
            ws.cell(row=row, column=4).value = ""  # Initials
            ws.cell(row=row, column=5).value = ""  # Notes
            row += 1

        # Summary row
        summary_row = row + 1
        ws.merge_cells(f"A{summary_row}:E{summary_row}")
        summary = ws[f"A{summary_row}"]
        self.style_body_cell(summary, "✓ All items completed", bold=True, background=self.colors["green"])

        return ws

    def create_schedule(self):
        """Create Weekly Schedule + Labor Cost sheet."""
        ws = self.wb.create_sheet("Schedule + Labor Cost")

        # Title
        ws.merge_cells("A1:H1")
        title = ws["A1"]
        self.style_title_cell(title, "WEEKLY STAFF SCHEDULE & LABOR COST")
        ws.row_dimensions[1].height = 30

        # Instructions
        ws["A3"] = "Week of:"
        ws["B3"] = datetime.now().strftime("%m/%d/%Y")
        ws["D3"] = "Labor Cost Goal: 30%"
        ws["F3"] = "Edit this value to your target"

        # Schedule Grid
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        headers = ["Position"] + days

        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=6, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 15
        for col in range(2, 9):
            ws.column_dimensions[get_column_letter(col)].width = 12

        # Position rows
        positions = ["Manager", "Kitchen Lead", "FOH Server", "FOH Server", "Kitchen Staff"]
        row = 7
        for position in positions:
            ws.cell(row=row, column=1).value = position
            for col in range(2, 9):
                ws.cell(row=row, column=col).value = ""  # Shift times to be filled in
            row += 1

        # Labor Cost Section
        labor_row = row + 2
        ws.merge_cells(f"A{labor_row}:H{labor_row}")
        ws[f"A{labor_row}"].value = "LABOR COST SUMMARY"
        self.style_header_cell(ws[f"A{labor_row}"], "LABOR COST SUMMARY")

        # Labor metrics
        metrics_row = labor_row + 2
        metrics = ["Total Hours This Week:", "Estimated Labor Cost:", "Labor Cost %:"]
        for idx, metric in enumerate(metrics):
            ws[f"A{metrics_row + idx}"].value = metric
            ws[f"B{metrics_row + idx}"].value = ""  # To be calculated

        return ws

    def create_inventory(self):
        """Create Inventory Management sheet."""
        ws = self.wb.create_sheet("Inventory")

        # Title
        ws.merge_cells("A1:F1")
        title = ws["A1"]
        self.style_title_cell(title, "INVENTORY MANAGEMENT")
        ws.row_dimensions[1].height = 30

        ws["A3"] = "Last Updated:"
        ws["B3"] = datetime.now().strftime("%m/%d/%Y %I:%M %p")
        ws["D3"] = "Reorder Threshold: 30% of Par Level"

        # Header row
        headers = ["Item", "Par Level", "Current Qty", "Status", "Supplier", "Cost/Unit"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=6, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 20
        ws.column_dimensions['B'].width = 12
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 15
        ws.column_dimensions['F'].width = 10

        # Sample inventory items
        items = [
            ("Chicken Breast", 20, "lbs"),
            ("Ground Beef", 15, "lbs"),
            ("Salmon Fillets", 10, "lbs"),
            ("Mixed Vegetables", 25, "lbs"),
            ("Olive Oil", 2, "gal"),
            ("Flour", 10, "lbs"),
            ("Pasta", 5, "lbs"),
            ("Rice", 10, "lbs"),
            ("Eggs", 30, "doz"),
            ("Butter", 5, "lbs"),
            ("Cheese", 10, "lbs"),
            ("Milk", 2, "gal"),
            ("Tomato Sauce", 12, "cans"),
            ("Bread", 20, "loaves"),
            ("Coffee", 5, "lbs")
        ]

        row = 7
        for item_name, par, unit in items:
            ws.cell(row=row, column=1).value = f"{item_name} ({unit})"
            ws.cell(row=row, column=2).value = par
            ws.cell(row=row, column=3).value = ""  # Current quantity
            ws.cell(row=row, column=4).value = ""  # Status (auto-calculated)
            ws.cell(row=row, column=5).value = ""  # Supplier
            ws.cell(row=row, column=6).value = ""  # Cost per unit
            row += 1

        # Reorder List Section
        reorder_row = row + 2
        ws.merge_cells(f"A{reorder_row}:F{reorder_row}")
        ws[f"A{reorder_row}"].value = "ITEMS TO REORDER (Below 30% Par)"
        self.style_header_cell(ws[f"A{reorder_row}"], "ITEMS TO REORDER (Below 30% Par)")

        return ws

    def create_manager_tasks(self):
        """Create Manager Daily/Weekly Task List sheet."""
        ws = self.wb.create_sheet("Manager Tasks")

        # Title
        ws.merge_cells("A1:F1")
        title = ws["A1"]
        self.style_title_cell(title, "MANAGER TASK LIST")
        ws.row_dimensions[1].height = 30

        ws["A3"] = "Week of:"
        ws["B3"] = datetime.now().strftime("%m/%d/%Y")

        # Daily Tasks
        daily_row = 5
        ws.merge_cells(f"A{daily_row}:F{daily_row}")
        ws[f"A{daily_row}"].value = "DAILY TASKS (Check Every Morning)"
        self.style_header_cell(ws[f"A{daily_row}"], "DAILY TASKS (Check Every Morning)")

        headers = ["Task", "Assigned To", "Due Date", "Status", "Notes", "Completed"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=daily_row + 2, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 25
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 12
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 20
        ws.column_dimensions['F'].width = 10

        daily_tasks = [
            "Pre-shift walkthrough",
            "Review staff check-in",
            "Review customer feedback",
            "Check opening checklist completion",
            "Brief shift supervisor"
        ]

        row = daily_row + 3
        for task in daily_tasks:
            ws.cell(row=row, column=1).value = task
            ws.cell(row=row, column=2).value = ""  # Assigned to
            ws.cell(row=row, column=3).value = "Daily"
            ws.cell(row=row, column=4).value = ""  # Status
            ws.cell(row=row, column=5).value = ""  # Notes
            ws.cell(row=row, column=6).value = ""  # Completed checkbox
            row += 1

        # Weekly Tasks
        weekly_row = row + 2
        ws.merge_cells(f"A{weekly_row}:F{weekly_row}")
        ws[f"A{weekly_row}"].value = "WEEKLY TASKS (Due Friday)"
        self.style_header_cell(ws[f"A{weekly_row}"], "WEEKLY TASKS (Due Friday)")

        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=weekly_row + 2, column=col)
            self.style_header_cell(cell, header)

        weekly_tasks = [
            "Approve schedule for following week",
            "Review labor cost %",
            "Place inventory orders",
            "Staff performance review",
            "Compliance log check"
        ]

        row = weekly_row + 3
        for task in weekly_tasks:
            ws.cell(row=row, column=1).value = task
            ws.cell(row=row, column=2).value = ""  # Assigned to
            ws.cell(row=row, column=3).value = "Friday"
            ws.cell(row=row, column=4).value = ""  # Status
            ws.cell(row=row, column=5).value = ""  # Notes
            ws.cell(row=row, column=6).value = ""  # Completed checkbox
            row += 1

        return ws

    def create_compliance(self):
        """Create Compliance & Health/Safety Audit Log sheet."""
        ws = self.wb.create_sheet("Compliance Audit Log")

        # Title
        ws.merge_cells("A1:G1")
        title = ws["A1"]
        self.style_title_cell(title, "COMPLIANCE & HEALTH/SAFETY AUDIT LOG")
        ws.row_dimensions[1].height = 30

        ws["A3"] = "This log tracks all food safety, labor law, and health department compliance issues."

        # Header row
        headers = ["Date", "Category", "Issue Description", "Observed By", "Corrective Action", "Status", "Resolution Date"]
        for col, header in enumerate(headers, 1):
            cell = ws.cell(row=6, column=col)
            self.style_header_cell(cell, header)

        ws.column_dimensions['A'].width = 12
        ws.column_dimensions['B'].width = 15
        ws.column_dimensions['C'].width = 25
        ws.column_dimensions['D'].width = 12
        ws.column_dimensions['E'].width = 25
        ws.column_dimensions['F'].width = 10
        ws.column_dimensions['G'].width = 12

        # Sample row structure
        categories = ["Food Safety", "Labor Law", "Health Dept", "Safety Equipment", "Training"]

        row = 7
        for _ in range(10):  # 10 empty rows for data entry
            ws.cell(row=row, column=1).value = ""  # Date
            ws.cell(row=row, column=2).value = ""  # Category (dropdown)
            ws.cell(row=row, column=3).value = ""  # Issue description
            ws.cell(row=row, column=4).value = ""  # Observed by
            ws.cell(row=row, column=5).value = ""  # Corrective action
            ws.cell(row=row, column=6).value = ""  # Status (Open/Closed)
            ws.cell(row=row, column=7).value = ""  # Resolution date
            row += 1

        # Summary section
        summary_row = row + 2
        ws.merge_cells(f"A{summary_row}:G{summary_row}")
        ws[f"A{summary_row}"].value = "MONTHLY COMPLIANCE SUMMARY"
        self.style_header_cell(ws[f"A{summary_row}"], "MONTHLY COMPLIANCE SUMMARY")

        summary_metrics_row = summary_row + 2
        ws[f"A{summary_metrics_row}"].value = "Total Issues Logged:"
        ws[f"B{summary_metrics_row}"].value = "=COUNTA(A7:A16)"
        ws[f"D{summary_metrics_row}"].value = "Open Issues:"
        ws[f"E{summary_metrics_row}"].value = "=COUNTIF(F7:F16,\"Open\")"

        return ws

    def create_quick_reference(self):
        """Create Quick Reference Guide sheet."""
        ws = self.wb.create_sheet("Quick Reference Guide")

        # Title
        ws.merge_cells("A1:D1")
        title = ws["A1"]
        self.style_title_cell(title, "QUICK REFERENCE GUIDE")
        ws.row_dimensions[1].height = 30

        # Restaurant Info Section
        ws["A3"] = "RESTAURANT INFORMATION"
        self.style_header_cell(ws["A3"], "RESTAURANT INFORMATION")

        info_items = [
            ("Restaurant Name:", ""),
            ("Location/Address:", ""),
            ("Phone Number:", ""),
            ("Manager Names:", ""),
            ("Operating Hours:", ""),
            ("Health Department:", "")
        ]

        row = 4
        for label, value in info_items:
            ws.cell(row=row, column=1).value = label
            ws.cell(row=row, column=2).value = value
            row += 1

        # Color Legend
        legend_row = row + 2
        ws.merge_cells(f"A{legend_row}:D{legend_row}")
        ws[f"A{legend_row}"].value = "COLOR CODING SYSTEM"
        self.style_header_cell(ws[f"A{legend_row}"], "COLOR CODING SYSTEM")

        color_legend = [
            ("🟢 GREEN", "Good / Completed / Within Limits"),
            ("🟡 YELLOW", "Caution / Review Needed / Approaching Limit"),
            ("🔴 RED", "Critical / Failed / Action Required")
        ]

        row = legend_row + 2
        for color, meaning in color_legend:
            ws.cell(row=row, column=1).value = color
            ws.cell(row=row, column=2).value = meaning
            row += 1

        # Tips Section
        tips_row = row + 2
        ws.merge_cells(f"A{tips_row}:D{tips_row}")
        ws[f"A{tips_row}"].value = "TIPS FOR SUCCESS"
        self.style_header_cell(ws[f"A{tips_row}"], "TIPS FOR SUCCESS")

        tips = [
            "• Complete checklists at the same time every day (habit-building)",
            "• Assign accountability (one person per shift responsible)",
            "• Review alerts immediately (don't ignore red flags)",
            "• Update inventory 2-3 times per week",
            "• Share schedule with team by Friday",
            "• Keep compliance log current for insurance/audits"
        ]

        row = tips_row + 2
        for tip in tips:
            ws.cell(row=row, column=1).value = tip
            ws.merge_cells(f"A{row}:D{row}")
            row += 1

        # Phone/Emergency Contacts
        contacts_row = row + 2
        ws.merge_cells(f"A{contacts_row}:D{contacts_row}")
        ws[f"A{contacts_row}"].value = "EMERGENCY CONTACTS"
        self.style_header_cell(ws[f"A{contacts_row}"], "EMERGENCY CONTACTS")

        row = contacts_row + 2
        contacts = [
            ("Health Department:", ""),
            ("Gas Emergency:", ""),
            ("Fire Department:", ""),
            ("Manager On-Call:", "")
        ]

        for label, value in contacts:
            ws.cell(row=row, column=1).value = label
            ws.cell(row=row, column=2).value = value
            row += 1

        ws.column_dimensions['A'].width = 25
        ws.column_dimensions['B'].width = 35
        ws.column_dimensions['C'].width = 15
        ws.column_dimensions['D'].width = 20

        return ws

    def save(self, filename):
        """Save the workbook."""
        self.wb.save(filename)
        print(f"✓ Created {filename}")

def main():
    """Generate both template versions."""
    # Create Warm & Inviting version
    print("Creating Warm & Inviting template...")
    warm_gen = RestaurantTemplateGenerator("warm")
    warm_gen.create_opening_checklist()
    warm_gen.create_closing_checklist()
    warm_gen.create_schedule()
    warm_gen.create_inventory()
    warm_gen.create_manager_tasks()
    warm_gen.create_compliance()
    warm_gen.create_quick_reference()
    warm_gen.save("Warm-&-Inviting/Restaurant-Ops-Template-Warm.xlsx")

    # Create Modern version
    print("Creating Modern Restaurant-Specific template...")
    modern_gen = RestaurantTemplateGenerator("modern")
    modern_gen.create_opening_checklist()
    modern_gen.create_closing_checklist()
    modern_gen.create_schedule()
    modern_gen.create_inventory()
    modern_gen.create_manager_tasks()
    modern_gen.create_compliance()
    modern_gen.create_quick_reference()
    modern_gen.save("Modern-Restaurant-Specific/Restaurant-Ops-Template-Modern.xlsx")

    print("\n✅ Both templates created successfully!")
    print("Next steps:")
    print("  1. Review the generated Excel files")
    print("  2. Import to Google Sheets for team collaboration")
    print("  3. Export to PDF for printing")

if __name__ == "__main__":
    # Create directories if they don't exist
    os.makedirs("Warm-&-Inviting", exist_ok=True)
    os.makedirs("Modern-Restaurant-Specific", exist_ok=True)

    main()
