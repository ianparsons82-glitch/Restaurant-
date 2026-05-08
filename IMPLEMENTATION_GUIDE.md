# Implementation Guide: Restaurant Operations Templates

## Setup (15 minutes)

### Step 1: Choose Your Template Version
- **Warm & Inviting**: Navy, coral, cream palette (casual dining, neighborhood spots)
- **Modern Restaurant-Specific**: Dark green, charcoal, bronze palette (upscale, fine dining)

### Step 2: Import Into Google Sheets (Recommended)
1. Download the Excel file (`Restaurant-Ops-Template-[Style].xlsx`)
2. Go to Google Drive → New → File Upload → Select the Excel file
3. Right-click → "Open with" → Google Sheets
4. Google automatically converts it to a Sheet
5. Click "File" → "Make a copy" → Name it "Restaurant Operations [Your Restaurant Name]"
6. Edit the copy (keep the original as backup)

**Alternative**: Use Excel directly if your team prefers offline mode or unreliable internet.

### Step 3: Add Your Restaurant Info
In the **Quick Reference Guide** sheet, fill in:
- [ ] Restaurant name
- [ ] Location/address
- [ ] Phone number
- [ ] Manager names
- [ ] Operating hours
- [ ] Logo (paste image in header cell)

---

## Customization Guide

### Changing Colors
All colors are in one place for easy editing:

**For Google Sheets:**
1. Select a cell with your current color
2. Click Format → Fill color → Choose new color
3. Use the provided color palette (see STYLE_GUIDE.md)
4. Colors automatically update in conditional formatting

**Important**: Don't change these critical colors (functionality depends on them):
- ❌ **Red** = Critical alerts, must-do items (keep as #E74C3C or #DC143C)
- ⚠️ **Yellow** = Caution/review items (keep as #F39C12 or #FFD700)
- ✅ **Green** = Completed/good items (keep as #27AE60 or #2D5016)

**Safe to change**:
- Navy/Dark Green = header backgrounds (choose your primary color)
- Coral/Brown = accent colors (choose your secondary color)
- Cream/Off-white = text backgrounds (keep light for readability)

### Editing Checklist Items
All checklists are fully editable. To customize:

1. **Opening Checklist**: Sheet tab "Opening Checklist"
   - Add/remove items by inserting/deleting rows
   - Keep the structure: [ Item ] [ ✓ Complete ] [ Time ] [ Initials ]
   - Don't delete the header row or formula row

2. **Closing Checklist**: Sheet tab "Closing Checklist"
   - Same process as opening
   - Critical items (food safety, lock-up) keep at bottom for visibility

3. **Inventory List**: Sheet tab "Inventory"
   - Add new items to the list (copy a row to maintain formatting)
   - Don't change column headers: Item | Par Level | Current Qty | Status | Supplier | Cost

4. **Manager Tasks**: Sheet tab "Manager Tasks"
   - Add weekly recurring tasks as needed
   - System auto-populates daily tasks

### Adjusting Par Levels (Inventory)
Par level = the target quantity you want to always have in stock

1. Open "Inventory" sheet
2. Find the item in column "Par Level"
3. Change the number (e.g., "20" = you want 20 units in stock at all times)
4. The sheet auto-calculates reorder alerts based on 30% threshold

**Example**:
- Par level: 20 units
- Reorder trigger: 20 × 0.30 = 6 units
- When you hit 6 units, system shows "REORDER NOW" alert

### Adjusting Labor Cost Threshold
Default is 30% (industry standard). To change:

1. Open "Schedule + Labor Cost" sheet
2. Find the cell labeled "Labor Cost Alert Threshold"
3. Change 30% to your target (e.g., 28% for fine dining, 32% for casual)
4. Conditional formatting automatically highlights cells exceeding your threshold

### Adding Managers/Staff Names
1. Open "Schedule + Labor Cost" sheet
2. In the staff list section, add names in column A
3. Pre-set hourly rates (column B) - system calculates labor cost automatically
4. Update the schedule grid to include new staff positions

---

## Using the Templates

### Daily Opening Checklist
**Who**: Opening shift manager
**When**: 30-60 minutes before first customer
**Time**: ~15-20 minutes to complete
**Steps**:
1. Print the PDF or open the digital sheet
2. Check each item (temperature logs, equipment startup, etc.)
3. Enter time when completed
4. Initial the row
5. If item fails, mark RED and note the issue in "Notes" column
6. System auto-generates summary of failed items for manager review

### Daily Closing Checklist
**Who**: Closing shift manager
**When**: After last customer leaves
**Time**: ~30-45 minutes
**Steps**:
1. Follow the checklist in order
2. Team completes deep clean, inventory spot-checks, security
3. Manager reviews all items, signs off
4. System auto-adds any failed items to next day's Manager Task list

### Weekly Schedule
**Who**: General manager
**When**: Create by end of week for following week
**Time**: ~20-30 minutes
**Steps**:
1. Fill in staff names in grid (columns = days, rows = positions)
2. Enter shift times (e.g., "10am-6pm")
3. System auto-calculates:
   - Total hours per employee
   - Labor cost (based on hourly rates)
   - Labor cost % of revenue
   - Overtime alerts (>40 hours/week)
4. Color-coding shows:
   - Yellow = Coverage gap (understaffed)
   - Red = Clopen alert (close-to-open, <10 hours rest)
5. Review alerts before finalizing schedule

### Inventory Management
**Who**: Kitchen manager or owner
**When**: 2-3 times per week (or daily for high-turnover items)
**Time**: ~10-15 minutes
**Steps**:
1. Count current stock for each item
2. Enter quantity in "Current Qty" column
3. System auto-shows status:
   - Green = Good, above par
   - Yellow = Approaching reorder level
   - Red = REORDER NOW (below 30% par)
4. System generates weekly reorder list (auto-populate what to order)
5. Mark items as "Ordered" when purchase order sent

### Manager Daily/Weekly Tasks
**Who**: Manager
**When**: Check every morning and Friday for weekly planning
**Time**: ~5 minutes daily
**Steps**:
1. Check "Today's Tasks" (highlights tasks due today in red)
2. Assign to specific staff member if delegating
3. Add completion date/notes when done
4. System auto-updates recurring weekly tasks each Monday
5. Compliance failures auto-appear here for follow-up

### Compliance Audit Log
**Who**: Manager (reviewing) + Staff (reporting issues)
**When**: Ongoing as issues arise
**Time**: ~2-3 minutes per entry
**Steps**:
1. When a health/safety issue is discovered, add to log
2. Document what happened, who observed it, corrective action
3. Mark as "Open" for follow-up
4. When fixed, mark as "Closed" and enter resolution date
5. System auto-generates monthly compliance summary (for insurance)

---

## Common Tasks

### How do I see if something failed in opening/closing?
1. Open the Opening or Closing Checklist sheet
2. Look for RED cells (marks failed items)
3. Check the "Notes" column for details
4. System auto-adds to Manager Tasks as "Follow-up: [Item Name]"

### How do I get the weekly reorder list?
1. Open Inventory sheet
2. Look for the "REORDER NOW" alerts (red background)
3. Items below 30% par level are automatically highlighted
4. Copy/send this list to your supplier

### How do I know if labor is over budget?
1. Open Schedule sheet
2. Look at "Labor Cost %" row
3. If RED, labor exceeds your threshold (default 30%)
4. Review schedule for optimization opportunities (cross-training, adjusted hours)

### How do I print for the team?
1. For digital use: Share the Google Sheets link with your team
2. For printing: Use the provided PDF files (optimized for 8.5" × 11" paper)
3. Laminate PDFs for kitchen/bar use (durable, wipeable)
4. Keep digital version as official record

---

## Tips for Success

**🎯 Consistency is Key**
- Assign one person per shift to complete checklists
- Set a specific time each day (e.g., 5:30am for opening manager)
- Make it habit, not burden

**📱 Mobile First**
- The sheet works on phones/tablets
- Don't need WiFi to view (if using Google Sheets offline mode)
- Use during shift, not after

**👥 Team Training (30 minutes)**
- Show staff how to fill out checklist
- Explain color system (red = alert, green = good)
- Clarify: Who completes what? Who reviews? Who signs off?

**🔄 Monthly Review**
- Review trends (What keeps failing? What's working?)
- Adjust items if needed (simplify if too complex, add if gaps exist)
- Share wins with team ("We've had perfect openings 3 weeks in a row!")

**💾 Keep Backups**
- Export Google Sheets to Excel monthly (Archive → Downloads)
- Print key sheets (schedule, compliance log) for physical records
- Maintain 12-month history for insurance/audit purposes

**🎨 Brand Your Template**
- Add your restaurant logo in the header
- Change colors to match your restaurant branding
- Add your specific health department requirements in Compliance sheet

---

## Troubleshooting

**Q: A formula is broken (showing #ERROR or #N/A)**
A: Don't panic. Usually caused by:
- Deleting a row that the formula references (undo with Ctrl+Z)
- Changing a column header name (use the original names)
- If unfixable, restore from backup Excel file and re-copy your custom data

**Q: Why is labor cost showing as 0% or -100%?**
A: Missing hourly rates. In Schedule sheet:
- Column "Hourly Rate" - fill in rates for each staff member
- Formula needs this to calculate labor cost

**Q: My schedule won't auto-calculate hours or labor cost**
A: Check:
- Are shift times formatted as "10am-6pm" or "10:00 AM-6:00 PM"?
- System expects 12-hour time format
- Dates should be in "Mon, May 8" format (not "5/8/26")

**Q: The conditional formatting colors aren't showing**
A: Google Sheets sometimes lags on color updates:
- Refresh the page (Ctrl+R or Cmd+R)
- Or manually recalculate: Tools → Recalculate

**Q: I can't edit the template**
A: Make sure you:
- Opened a COPY (not the original file)
- Have edit permissions (owner or can edit)
- Aren't in viewer mode (check top right, switch to edit mode)

---

## Next Steps

1. ✅ Download and import the Excel file
2. ✅ Customize colors to match your brand
3. ✅ Add your restaurant info and staff names
4. ✅ Adjust par levels and labor thresholds to match your operation
5. ✅ Print PDFs and post in kitchen/front-of-house
6. ✅ Share Google Sheets link with your management team
7. ✅ Train staff on how to complete checklists (30 minutes)
8. ✅ Start using tomorrow at opening

---

**Questions?** See the Quick Reference Guide sheet in the template for quick answers.  
**Need to customize further?** Review STYLE_GUIDE.md for all color codes and font specifications.

**Version**: 1.0  
**Last Updated**: 2026-05-08
