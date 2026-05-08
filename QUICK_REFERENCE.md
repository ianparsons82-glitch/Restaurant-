# 🚀 Quick Reference Guide - PDF Templates

## 📋 Template Overview

### 1️⃣ Daily Opening Checklist
**File:** `opening-checklist.pdf` | **Color:** 🔴 RED (#DC3545)

**When:** Before service starts (20-30 min)
**Who:** Opening manager
**Sections:** 
- Facility Inspection (10 items)
- Equipment & Safety (9 items) 
- Kitchen Prep (9 items)
- Front of House (6 items)
- Staff Briefing (5 items)

**Critical Items:** Equipment temp checks, cooler/freezer temps, fire safety

---

### 2️⃣ Daily Closing Checklist
**File:** `closing-checklist.pdf` | **Color:** 🟠 ORANGE (#FF9800)

**When:** After service ends (45-60 min)
**Who:** Closing manager
**Sections:**
- End of Service (10 items)
- Kitchen Deep Clean (13 items)
- Front of House Close (11 items)
- Inventory & Security (8 items)
- Manager Sign-Off (3 items)

**Critical Items:** Door locks, alarm system, cash security, sanitization

---

### 3️⃣ Weekly Schedule & Labor Tracker
**File:** `weekly-schedule.pdf` | **Color:** 🔵 BLUE (#2196F3)

**When:** Sunday evening or Monday morning
**Who:** Scheduling manager
**Sections:**
- Schedule Grid (7 days + 6 positions)
- Labor Cost Summary
- Notes & Scheduling Alerts

**Key Metrics:**
- Total labor hours
- Labor cost % (target <28%)
- Identify clopenings and overtime

---

### 4️⃣ Inventory Management Sheet
**File:** `inventory-sheet.pdf` | **Color:** 🟢 GREEN (#4CAF50)

**When:** Weekly (same day/time)
**Who:** Kitchen manager or owner
**Sections:**
- Current Inventory Levels (15 items)
- Reorder Summary
- Delivery Tracking

**Status Coding:**
- 🟢 GREEN = OK (≥70% par)
- 🟡 YELLOW = LOW (30-70% par)
- 🔴 RED = CRITICAL (<30% par)

---

### 5️⃣ Manager Daily & Weekly Tasks
**File:** `manager-tasks.pdf` | **Color:** 🟣 PURPLE (#9C27B0)

**When:** Every morning + weekly reviews
**Who:** Restaurant manager
**Sections:**
- Today's Priorities (5 tasks)
- Daily Recurring Tasks (5 tasks)
- Weekly Tasks (5 tasks)
- Notes & Follow-ups

**Frequency:**
- Daily: Check items 1 & 2 daily
- Weekly: Check items 3 weekly
- Review: Refer back for continuity

---

## 🎯 Quick Usage Tips

### Opening Checklist
```
✓ Arrive early (30 min before service)
✓ Complete sections in order
✓ Initial each item as you verify it
✓ Note any issues in notes section
✓ Manager signs off before staff briefing
✓ File for compliance records
```

### Closing Checklist
```
✓ Start during final hour of service
✓ Assign sections to closing team
✓ Each person initials their sections
✓ Verify all items before manager sign-off
✓ Manager walks through facility
✓ Arm alarm and lock all doors
✓ File in manager office
```

### Weekly Schedule
```
✓ Print previous week's actual labor hours
✓ Review sales numbers for staffing needs
✓ Build schedule avoiding clopenings
✓ Calculate estimated labor cost
✓ Compare to 28% budget target
✓ Share with team by Friday
✓ Post in staff area
```

### Inventory Sheet
```
✓ Same time each week (e.g., Monday 10am)
✓ Count each item carefully
✓ Compare to par level
✓ Mark items below 50% par for reorder
✓ Total order cost and date needed
✓ Contact suppliers
✓ File completed sheet with other records
```

### Manager Tasks
```
✓ Complete "Today's Priorities" first thing
✓ Check off "Daily" items throughout shift
✓ Weekly items: Friday or Monday morning
✓ Use "Notes" for follow-up items
✓ Review previous week's notes for continuity
✓ Share priorities with team
```

---

## 🔧 Common Customizations

### Change Restaurant Name
```bash
python3 customize_templates.py
# Select option 1 (Interactive setup)
# Enter your restaurant name
```

### Multi-Location Setup
```bash
python3 batch_generate.py
# Select option 1 (Interactive setup)
# Add each location
# Generate all PDFs organized by location
```

### Update Checklist Items
Edit `create_interactive_pdfs.py`:
```python
sections = [
    ("YOUR SECTION", [
        ("Item 1", False),   # Not emphasized
        ("Item 2", True),    # Emphasized
    ]),
]
```

### Change Colors
Edit `template_config.json`:
```json
"colors": {
    "opening_checklist": "#YOUR_HEX_COLOR",
}
```

---

## 📊 Typical Weekly Workflow

### Monday
- Generate new Weekly Schedule
- Review previous week's checklists
- Update inventory from weekend counts
- Assign manager daily tasks

### Tuesday-Friday
- Complete daily opening checklist
- Complete daily closing checklist
- Track inventory movements
- Manager daily task review

### Friday Evening
- Review week's labor costs
- Finalize next week's schedule
- Plan inventory ordering
- Document issues for next week

### Sunday Evening
- Create schedule for next week
- Calculate labor projections
- Order inventory
- Plan manager priorities

---

## 🖨️ Print Setup

### Basic Setup
```
Paper Size: 8.5" × 11" (Letter)
Color: Full color recommended
Scale: 100% (no scaling)
Margins: Default (0.75"+)
Quality: Best available
```

### Schedule (Landscape)
```
Paper Size: 11" × 8.5" (Landscape Letter)
Color: Full color
Scale: 100%
Quality: Best available
```

### Lamination
```
Material: 3-5 mil thermal laminating pouches
Process: Standard laminating machine
Pens: Dry-erase or wet-erase only
Cleaning: Mild soap and water
```

---

## ✅ Compliance & Records

### Daily Checklists
- **Keep:** 30-60 days minimum
- **Purpose:** Verify procedures were followed
- **Value:** Proof of food safety compliance
- **Review:** Weekly for patterns

### Weekly Schedule
- **Keep:** 1-2 years
- **Purpose:** Labor compliance, scheduling records
- **Value:** Track hours for payroll accuracy
- **Review:** Monthly for labor trends

### Inventory Sheets
- **Keep:** 1 year minimum
- **Purpose:** Food cost tracking
- **Value:** COGS analysis, theft detection
- **Review:** Monthly for cost control

### Manager Tasks
- **Keep:** 30-90 days
- **Purpose:** Management continuity
- **Value:** Accountability documentation
- **Review:** Refer for follow-up items

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| PDFs won't open | Install Adobe Reader |
| Form fields not working | Use Adobe Reader, not browser |
| Can't fill in fields | Disable "Reader Security" |
| Printing looks wrong | Check print scale is 100% |
| Colors look faded | Print on quality paper |
| Checkboxes don't work | Try Adobe Reader DC |
| Text is cut off | Adjust margins to 0.75" |
| Laminating failed | Use proper thermal pouches |

---

## 📱 Digital Workflow

### Email Distribution
```
1. Email PDF to staff
2. Staff fills on device or prints
3. Email back to manager
4. Save to cloud (Google Drive, etc.)
5. Archive with date stamp
```

### Cloud Storage
```
Google Drive: PDFs/ → Daily/ → 2024-05-08/
OneDrive:    Checklists/ → Weekly/ → Week-of-05-06/
Dropbox:     Restaurant/Compliance/ → Monthly/
```

### Mobile Viewing
```
Adobe Reader App (iOS/Android)
Fill fields on phone/tablet
Email completed form back
No printing required
```

---

## 💡 Tips for Success

✨ **Make it Routine**
- Same time each day for checklists
- Same day/time each week for inventory
- Consistent manager task review

📍 **Be Specific**
- Note exact temperatures on coolers
- Document specific issues found
- Reference items by section number

📋 **Keep Records**
- File completed forms immediately
- Create binder by month
- Review monthly for patterns

👥 **Train Your Team**
- Walk through each template
- Explain why items matter
- Practice filling out forms
- Recognize good compliance

🎯 **Review Regularly**
- Weekly: Scan for issues
- Monthly: Analyze trends
- Quarterly: Update procedures
- Annually: Refresh training

---

## 📞 Quick Support

**Template not opening:**
- Try Adobe Reader (most compatible)
- Download latest version
- Check file isn't corrupted

**Custom setup:**
- Run `customize_templates.py`
- Follow interactive prompts
- Re-generate PDFs

**Multi-location:**
- Run `batch_generate.py`
- Creates separate folders per location
- Generates all 5 PDFs per location

**Need to modify items:**
- Edit `create_interactive_pdfs.py`
- Update checklist sections
- Re-run to generate new PDFs

---

## 🎓 Training Checklist

### For Managers
- [ ] Review all 5 templates
- [ ] Understand purpose of each
- [ ] Know critical items (emphasized)
- [ ] Practice filling out forms
- [ ] Set up filing system
- [ ] Plan weekly review schedule

### For Staff
- [ ] Show relevant templates for role
- [ ] Explain sign-off requirements
- [ ] Demonstrate form filling
- [ ] Practice on sample form
- [ ] Know where to report issues
- [ ] Understand accountability (initials)

### For Owner/Corporate
- [ ] Review compliance aspects
- [ ] Plan audit process
- [ ] Set record retention policy
- [ ] Establish review cadence
- [ ] Train multiple managers
- [ ] Create backup procedures

---

**Last Updated:** May 2024  
**Template Version:** 1.0  
**Status:** Production Ready

See [PDF_TEMPLATES_GUIDE.md](PDF_TEMPLATES_GUIDE.md) for detailed documentation
