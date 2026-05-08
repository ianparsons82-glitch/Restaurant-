# 🚀 Setup Guide - Premium Restaurant PDF Templates

Complete step-by-step instructions to get your restaurant PDF templates up and running.

## ⏱️ Time Required
- **Basic setup (single location):** 5-10 minutes
- **Full customization:** 15-20 minutes
- **Multi-location setup:** 20-30 minutes

---

## 📋 Prerequisites

### Software Required
- Python 3.7+ (check with `python3 --version`)
- reportlab library (will be installed automatically)

### Files You Have
- `create_interactive_pdfs.py` - Main PDF generator
- `customize_templates.py` - Customization tool
- `batch_generate.py` - Multi-location tool
- `PDF_TEMPLATES_GUIDE.md` - Complete documentation
- `README_TEMPLATES.md` - Overview and examples
- `QUICK_REFERENCE.md` - Quick lookup guide

---

## 🎯 Option 1: Quick Start (5 minutes)

Use defaults, customize restaurant name later.

### Step 1: Generate PDFs
```bash
# Run with default settings
python3 create_interactive_pdfs.py
```

**Result:** 5 PDF files generated
- `opening-checklist.pdf`
- `closing-checklist.pdf`
- `weekly-schedule.pdf`
- `inventory-sheet.pdf`
- `manager-tasks.pdf`

### Step 2: Verify PDFs
```bash
# List generated files
ls -lh *.pdf
```

You should see 5 PDF files (2-7 KB each).

### Step 3: Print & Test
1. Open `opening-checklist.pdf` in Adobe Reader
2. Click on checkboxes to test interactivity
3. Click in text fields to verify fillable areas
4. Print a sample to verify layout

### Done! ✅
Your PDFs are ready. See **Option 2** to customize for your restaurant.

---

## 🎯 Option 2: Customized Setup (15 minutes)

Generate PDFs with your restaurant name and info.

### Step 1: Run Interactive Setup
```bash
python3 customize_templates.py
```

### Step 2: Answer Prompts
```
Options:
1. Interactive setup (recommended for first time)
2. Use/edit template_config.json
3. Generate from existing config
4. Create default config.json

Select option (1-4): 1
```

### Step 3: Enter Restaurant Information
```
Restaurant name: The Golden Fork
Address: 456 Oak Lane, Portland, OR 97205
Phone: (503) 555-1234
```

### Step 4: Confirm Colors (Optional)
Press Enter to keep default colors, or enter hex color codes:
```
Opening Checklist [#DC3545]: 
Closing Checklist [#FF9800]:
Weekly Schedule [#2196F3]:
Inventory Sheet [#4CAF50]:
Manager Tasks [#9C27B0]:
```

### Step 5: Generate PDFs
```
Generate PDFs now? (y/n): y
```

**Result:** Custom PDFs generated with your restaurant name!

### Step 6: Verify
```bash
ls -lh *.pdf
# Open opening-checklist.pdf
# Verify "The Golden Fork" appears in header
```

### Done! ✅
Customized PDFs ready for your restaurant.

---

## 🎯 Option 3: Multi-Location Setup (20 minutes)

Generate PDFs for multiple restaurant locations.

### Step 1: Run Batch Generator
```bash
python3 batch_generate.py
```

### Step 2: Select Interactive Setup
```
Options:
1. Interactive setup (recommended for first time)
2. Use/edit locations.json
3. Generate from existing config
4. Create sample config

Select option (1-4): 1
```

### Step 3: Enter Location Count
```
How many locations? 2
```

### Step 4: Enter Each Location
```
📍 Location 1
Location ID (e.g., 'downtown'): downtown
Location name: Downtown Location
Address: 123 Main Street, Portland, OR 97205
Phone: (503) 555-0001

📍 Location 2
Location ID (e.g., 'eastside'): eastside
Location name: Eastside Location
Address: 456 Oak Avenue, Portland, OR 97214
Phone: (503) 555-0002
```

### Step 5: Generate All PDFs
```
Generate PDFs now? (y/n): y
```

**Result:** Organized folder structure:
```
PDFs_downtown/
├── opening-checklist.pdf
├── closing-checklist.pdf
├── weekly-schedule.pdf
├── inventory-sheet.pdf
└── manager-tasks.pdf

PDFs_eastside/
├── opening-checklist.pdf
├── closing-checklist.pdf
├── weekly-schedule.pdf
├── inventory-sheet.pdf
└── manager-tasks.pdf
```

### Step 6: Generate Manifest (Optional)
```
Generate manifest file? (y/n): y
```

Creates `BATCH_MANIFEST.json` with all file locations.

### Step 7: Verify Structure
```bash
ls -R PDFs_*
# Should show all 5 PDFs in each location folder
```

### Done! ✅
All locations set up with customized PDFs.

---

## 🎨 Option 4: Advanced Customization (20+ minutes)

Customize checklist items, colors, and layout.

### Step 1: Edit Configuration File
```bash
nano template_config.json
# or use your favorite editor
```

### Example Configuration:
```json
{
  "restaurant": {
    "name": "The Golden Fork",
    "address": "456 Oak Lane, Portland, OR 97205",
    "phone": "(503) 555-1234",
    "manager_contact": "Manager: John Smith"
  },
  "colors": {
    "opening_checklist": "#E74C3C",
    "closing_checklist": "#E67E22",
    "weekly_schedule": "#3498DB",
    "inventory_sheet": "#27AE60",
    "manager_tasks": "#8E44AD"
  }
}
```

### Step 2: Modify Checklist Items (Optional)

Edit `create_interactive_pdfs.py`:

```python
# Find this section (around line 400):
sections = [
    ("FACILITY INSPECTION", [
        ("Building exterior checked", False),
        ("Entrance doors unlocked & cleaned", False),
        # Add your custom items:
        ("Your custom item", False),  # Not emphasized
        ("Critical safety item", True),  # Emphasized with color
    ]),
]
```

Format: `("Item description", is_emphasized)`
- `False` = normal item
- `True` = emphasized (colored background)

### Step 3: Regenerate PDFs
```bash
python3 customize_templates.py
# Select option 3: Generate from existing config
```

### Step 4: Review Changes
```bash
# Open and verify the new PDFs
# Check restaurant name appears correctly
# Verify colors match your configuration
# Review any custom items you added
```

### Done! ✅
Advanced customization complete.

---

## 🖨️ Printing & Setup (10 minutes)

### Step 1: Open PDF
```
1. Open opening-checklist.pdf in Adobe Reader
2. Print to color printer
3. Use standard 8.5" × 11" paper
```

### Step 2: Print Settings
```
✓ Page scaling: None (100%)
✓ Color output: Yes
✓ Quality: Best available
✓ Margins: Default (0.75"+)
```

### Step 3: Verify Print Quality
```
Check:
☑ Text is clear and readable
☑ Colors are vibrant
☑ Checkboxes are visible
☑ Margins look right (0.75")
☑ No text cutoff
```

### Step 4: Lamination (Optional but Recommended)
```
Materials needed:
- 3-5 mil thermal laminating pouches
- Thermal laminating machine

Process:
1. Print PDF on standard paper
2. Insert in laminating pouch
3. Run through laminator
4. Cool completely

Result:
- Reusable forms (use dry-erase pens)
- Water-resistant
- Professional appearance
- Long-lasting
```

### Done! ✅
PDFs ready for use in your restaurant.

---

## 📚 Documentation Guide

**New to the templates?**
→ Start with [README_TEMPLATES.md](README_TEMPLATES.md)

**Need quick lookup?**
→ Use [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

**Detailed information?**
→ Read [PDF_TEMPLATES_GUIDE.md](PDF_TEMPLATES_GUIDE.md)

**Understanding the design?**
→ See PDF_TEMPLATES_GUIDE.md > Design System section

---

## ✅ Verification Checklist

After setup, verify everything works:

### PDF Generation
- [ ] All 5 PDFs generated without errors
- [ ] Files are 2-7 KB each
- [ ] PDFs open in Adobe Reader

### Content Verification
- [ ] Restaurant name appears in headers
- [ ] Address appears correctly
- [ ] Template titles are correct
- [ ] Section headers are visible
- [ ] Checkboxes are present

### Interactive Features
- [ ] Checkboxes can be clicked
- [ ] Text fields are fillable
- [ ] Fields remain editable after save
- [ ] Forms work in Adobe Reader

### Print Testing
- [ ] Colors print correctly
- [ ] Text is clear and readable
- [ ] Margins are correct (0.75"+)
- [ ] No content cutoff
- [ ] Professional appearance

### Ready for Use
- [ ] Staff trained on templates
- [ ] Filing system set up
- [ ] Printing/lamination completed
- [ ] First day trial run successful

---

## 🆘 Troubleshooting

### PDFs Won't Generate
```
Error: ModuleNotFoundError: No module named 'reportlab'

Solution:
pip install reportlab
```

### PDFs Won't Open
```
Error: File corrupted or invalid PDF

Solution:
1. Delete PDFs
2. Re-run generation script
3. Use Adobe Reader (not browser)
```

### Form Fields Don't Work
```
Issue: Can't click checkboxes or type in fields

Solution:
1. Open in Adobe Reader (not Preview/browser)
2. Try on different device
3. Re-download PDF
```

### Configuration Not Applied
```
Issue: Restaurant name still shows "Restaurant Name"

Solution:
1. Verify template_config.json is valid JSON
2. Use quotes around values: "name": "Value"
3. Re-run customize_templates.py option 3
```

### Print Quality Issues
```
Issue: Colors look washed out or text is blurry

Solution:
1. Use quality color printer
2. Print at 100% scale (no shrinking)
3. Use standard quality paper
4. Check printer drivers are up to date
```

---

## 📞 Quick Support

### Problem: Can't find Python
**Solution:** Install Python 3.7+
```bash
# Check if Python installed
python3 --version

# Install on Mac (Homebrew)
brew install python3

# Install on Windows
Download from python.org
```

### Problem: Scripts won't run
**Solution:** Make sure file permissions are set
```bash
chmod +x create_interactive_pdfs.py
python3 create_interactive_pdfs.py
```

### Problem: Reports about old syntax
**Solution:** Use Python 3.7 or newer
```bash
python3 --version  # Should be 3.7+
```

### Problem: Need to customize more
**Solution:** Edit create_interactive_pdfs.py
```
Look for "sections = [" around line 400
Add/modify checklist items
Re-run to generate new PDFs
```

---

## 🎓 Training Your Team

### For Staff
1. **Show them the template**
   - Open example PDF
   - Click checkboxes to show interactivity
   - Explain initials for accountability

2. **Practice together**
   - Walk through sample checklist
   - Have staff fill out one section
   - Show where to file completed forms

3. **Explain importance**
   - Why each section matters
   - How compliance helps the business
   - Their role in food safety/operations

### For Managers
1. **Complete walkthroughs**
   - Review all 5 templates
   - Understand each section
   - Identify critical items

2. **Review compliance aspects**
   - Food safety requirements
   - Labor law requirements
   - Record retention policies

3. **Set up review schedule**
   - Daily: Spot check opening/closing
   - Weekly: Review inventory and schedule
   - Monthly: Analyze patterns
   - Quarterly: Staff training refresher

---

## 📋 Next Steps

1. **Generate PDFs**
   ```bash
   python3 customize_templates.py
   ```

2. **Test digital forms**
   - Open in Adobe Reader
   - Try clicking and typing
   - Verify save functionality

3. **Print sample**
   - Use color printer
   - Check quality
   - Verify all content visible

4. **Laminate** (optional)
   - Use 3-5 mil pouches
   - Professional appearance
   - Reusable with dry-erase pens

5. **Deploy to team**
   - Print for each shift
   - Train staff on usage
   - Set up filing system

6. **Monitor & refine**
   - Review completed forms
   - Adjust items if needed
   - Update training as needed

---

## 🎉 You're All Set!

Your premium PDF templates are ready to transform your restaurant's operations management.

### Key Points
- ✅ Professional appearance
- ✅ Easy to customize
- ✅ Interactive forms
- ✅ Compliance-ready
- ✅ Training materials included

### Where to Go From Here
- **Need help?** See QUICK_REFERENCE.md
- **Want details?** Read PDF_TEMPLATES_GUIDE.md
- **Need more?** Edit Python files directly
- **Multi-location?** Use batch_generate.py

---

**Created:** May 2024  
**Status:** Production Ready  
**Version:** 1.0  

**Support Documentation:**
- README_TEMPLATES.md - Overview
- PDF_TEMPLATES_GUIDE.md - Comprehensive guide
- QUICK_REFERENCE.md - Quick lookup
- create_interactive_pdfs.py - Source code
