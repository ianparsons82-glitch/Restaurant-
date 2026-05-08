# 🎨 Premium Restaurant Operations PDF Templates

**Professional, interactive PDF forms for restaurant management** - designed to look like premium branded documents when printed and laminated.

## 🚀 Quick Start

### Generate PDFs (Default Restaurant)
```bash
python3 create_interactive_pdfs.py
```

### Customize for Your Restaurant
```bash
python3 customize_templates.py
```

Then choose:
1. **Interactive setup** - Answer questions about your restaurant
2. **Use config file** - Edit `template_config.json` directly
3. **Generate from config** - Use existing configuration

## 📋 The 5 Templates

| Template | Color | Purpose |
|----------|-------|---------|
| **Opening Checklist** | 🔴 RED | Pre-service facility & equipment verification |
| **Closing Checklist** | 🟠 ORANGE | End-of-service cleanup & security |
| **Weekly Schedule** | 🔵 BLUE | Staff scheduling & labor cost tracking |
| **Inventory Sheet** | 🟢 GREEN | Stock level management & reordering |
| **Manager Tasks** | 🟣 PURPLE | Daily priorities & weekly responsibilities |

## ✨ Features

✅ **Professional Design**
- Premium appearance suitable for high-end restaurants
- Consistent design system across all templates
- Strategic color usage (not overwhelming)
- Generous white space and proper hierarchy

✅ **Interactive Forms**
- Clickable checkboxes
- Fillable text fields with underline styling
- Date entry fields
- Works in Adobe Reader and most PDF viewers

✅ **Print-Ready**
- Optimized for standard Letter (8.5" × 11") pages
- Color and B&W compatible
- 0.75" margins for safe printing
- Lamination-ready (3-5 mil thermal laminating pouches recommended)

✅ **Fully Customizable**
- Easy Python script modification
- Support for custom restaurant names and addresses
- Configurable colors for each template
- Extensible item lists

## 📁 Files

```
.
├── create_interactive_pdfs.py      # Main PDF generation script
├── customize_templates.py          # Interactive customization tool
├── template_config.json            # Configuration file (auto-created)
├── opening-checklist.pdf           # Generated template
├── closing-checklist.pdf           # Generated template
├── weekly-schedule.pdf             # Generated template
├── inventory-sheet.pdf             # Generated template
├── manager-tasks.pdf               # Generated template
├── PDF_TEMPLATES_GUIDE.md          # Comprehensive documentation
└── README_TEMPLATES.md             # This file
```

## 🎯 Usage Examples

### Example 1: Single Restaurant Setup
```bash
# Run interactive setup
python3 customize_templates.py

# Answer prompts:
# Restaurant name: "The Golden Fork"
# Address: "456 Oak Lane, Portland, OR 97205"
# Proceed to generate PDFs
```

### Example 2: Multi-Location Business
```bash
# Edit template_config.json for each location
nano template_config.json

# Change restaurant details, keep signature colors
# Generate location-specific PDFs
python3 customize_templates.py
```

### Example 3: Custom Color Branding
```bash
# Edit template_config.json colors section
# Update hex color codes to match your brand
# Re-generate PDFs with new colors
python3 customize_templates.py
```

## 📖 Configuration (template_config.json)

```json
{
  "restaurant": {
    "name": "Your Restaurant Name",
    "address": "123 Main Street, City, State 12345",
    "phone": "(555) 123-4567",
    "manager_contact": ""
  },
  "colors": {
    "opening_checklist": "#DC3545",
    "closing_checklist": "#FF9800",
    "weekly_schedule": "#2196F3",
    "inventory_sheet": "#4CAF50",
    "manager_tasks": "#9C27B0"
  }
}
```

## 🖨️ Printing & Lamination

### Recommended Process
1. **Print**: Use color printer, 100% scale, standard letter size
2. **Cut**: Trim to 8.5" × 11" if needed
3. **Laminate**: Use 3-5 mil thermal laminating pouches
4. **Dry-erase**: Use with dry-erase or wet-erase pens for reusable forms

### Benefits
- **Reusable**: Wipe clean and use again
- **Durable**: Protected from spills and wear
- **Professional**: Looks like branded company documents
- **Cost-effective**: Multiple uses per print

## 📱 Digital Usage

### On Tablets/Phones
- ✅ Adobe Reader app (best support)
- ✅ Google Drive PDF viewer
- ✅ iBooks (iOS)
- ✅ Native PDF apps

### Workflow
1. Email PDF to staff
2. Fill fields on device or print
3. Email back or save to cloud storage
4. Archive for compliance

## 🔧 Customization Guide

### Modifying Checklist Items
Edit `create_interactive_pdfs.py`:

```python
sections = [
    ("FACILITY INSPECTION", [
        ("Your custom item here", False),  # Not emphasized
        ("Critical item", True),            # Emphasized (colored background)
        # Add more items...
    ]),
]
```

### Changing Template Colors
Edit `template_config.json`:

```json
"colors": {
    "opening_checklist": "#YOUR_HEX_COLOR",
    "closing_checklist": "#YOUR_HEX_COLOR",
    ...
}
```

### Adding Restaurant Information
Option 1: Use interactive setup
```bash
python3 customize_templates.py
# Select option 1
```

Option 2: Edit `template_config.json` directly
```json
"restaurant": {
    "name": "Your Restaurant",
    "address": "Your Address",
    "phone": "Your Phone"
}
```

## 📊 Design System

### Typography
- **Headers**: Helvetica Bold, 12-18pt, signature color
- **Body**: Helvetica, 9-11pt, dark gray (#333333)
- **Labels**: Helvetica, 9-10pt, medium gray (#666666)

### Colors
- **Primary**: Signature color (unique per template)
- **Emphasis**: 10% tinted version of signature color
- **Text**: #333333 (primary), #666666 (secondary)
- **Accents**: #CCCCCC (borders), #F8F8F8 (alternating rows)

### Spacing
- **Margins**: 0.75" all sides
- **Section spacing**: 25px between sections
- **Item spacing**: 18px line height
- **Table spacing**: 15px rows

## ✅ Quality Standards

Each template includes:
- ✅ Professional header with logo space
- ✅ Restaurant name and address
- ✅ Template title and date fields
- ✅ Multiple content sections (3-5)
- ✅ Interactive checkboxes
- ✅ Fillable text fields
- ✅ Proper visual hierarchy
- ✅ Professional footer with sign-off
- ✅ Color-coded emphasis items

## 🚨 Troubleshooting

### PDFs won't open
- Ensure PDF reader installed (Adobe Reader recommended)
- Download latest version of PDF application
- Try alternative viewer (Chrome, Firefox)

### Form fields not working
- Use Adobe Reader (best compatibility)
- Save PDF before editing
- Check PDF reader supports interactive forms

### Printing issues
- Print at 100% scale (no shrinking)
- Select color printer
- Set margins to 0.75"
- Check paper orientation (Portrait for most, Landscape for schedule)

### Customization not applying
- Verify `template_config.json` is valid JSON
- Re-run `customize_templates.py`
- Check for file permission issues

## 📚 Documentation

For comprehensive details, see:
- **PDF_TEMPLATES_GUIDE.md** - Complete template documentation
- **create_interactive_pdfs.py** - Source code with inline comments
- **customize_templates.py** - Customization tool documentation

## 🎓 Training Tips

### For Managers
1. Walk through each template's sections
2. Identify critical items (colored emphasis)
3. Explain initials for accountability
4. Demonstrate form filling

### For Staff
1. Show relevant sections for their role
2. Explain sign-off requirements
3. Practice completing forms
4. Review examples of completed documents

## 🔄 Version History

### v1.0 (Initial Release)
- 5 premium PDF templates
- Interactive form fields
- Professional design system
- Customization support
- Comprehensive documentation

## 💡 Best Practices

### Daily Use
- Print fresh or use laminated/reusable versions
- Complete throughout the shift (not end of day)
- Initial items as completed for accountability
- File completed documents for compliance

### Weekly Review
- Review all completed checklists
- Identify patterns or recurring issues
- Update training if needed
- Archive for records

### Monthly
- Review template effectiveness
- Adjust items based on feedback
- Update colors if branding changes
- Train new staff

## 🤝 Support & Feedback

### For Issues
1. Check PDF_TEMPLATES_GUIDE.md troubleshooting section
2. Verify configuration is correct
3. Try with default settings
4. Check file permissions

### For Enhancements
- Customize the Python scripts directly
- Add new template types
- Modify color schemes
- Extend checklist items

## 📄 License & Attribution

These PDF templates are designed for restaurant operations management. 

### Usage Rights
✅ Use within your restaurant(s)
✅ Print and laminate
✅ Customize for your operations
✅ Distribute to your team

## 🎯 Next Steps

1. **Generate default PDFs**
   ```bash
   python3 create_interactive_pdfs.py
   ```

2. **Customize for your restaurant**
   ```bash
   python3 customize_templates.py
   ```

3. **Print and test**
   - Print a sample
   - Test form fields in Adobe Reader
   - Verify all items are legible

4. **Laminate and deploy**
   - Laminate for durability
   - Distribute to team
   - Train staff on usage

5. **Implement in operations**
   - Add to daily procedures
   - Archive completed forms
   - Review regularly for improvements

---

**Created:** May 2024  
**Design System:** Premium Restaurant Operations  
**Version:** 1.0  
**Status:** Production Ready

For detailed documentation, see [PDF_TEMPLATES_GUIDE.md](PDF_TEMPLATES_GUIDE.md)
