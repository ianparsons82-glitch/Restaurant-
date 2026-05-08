# Design Style Guide: Restaurant Operations Templates

## Color Systems

### Warm & Inviting Aesthetic
*Best for: Casual dining, neighborhood spots, family restaurants*

**Primary Palette:**
- Primary Navy: #2C3E50 (header backgrounds, primary text)
- Coral Accent: #FF6B6B (buttons, important highlights)
- Cream Background: #F5F3F0 (main sheet background)
- Warm Gray: #8B8680 (secondary text, subtle dividers)
- Gold Accent: #D4AF37 (premium touches, section dividers)

**Alert Colors (Critical - Do Not Change):**
- Alert Red: #E74C3C (failures, critical items, must-do)
- Warning Yellow: #F39C12 (caution, needs review, approaching limits)
- Success Green: #27AE60 (completed, good status, within limits)

**Usage**:
- Headers: Navy backgrounds with white text
- Body: Cream background with navy text (11pt)
- Status cells: Green (good) / Yellow (caution) / Red (alert)
- Section dividers: Gold 3pt lines
- Checkboxes/interactive: Coral
- Accents: Gold (premium feel)

---

### Modern Restaurant-Specific Aesthetic
*Best for: Upscale casual, fine dining, trendy restaurants*

**Primary Palette:**
- Dark Green: #1B4332 (header backgrounds, premium feel)
- Charcoal: #2D2D2D (primary text, dark elements)
- Cream Background: #F5F3F0 (main sheet background)
- Brown Accent: #8B6F47 (wood tones, warm accents)
- Bronze: #B8860B (luxury highlights, premium feel)

**Alert Colors (Critical - Do Not Change):**
- Alert Crimson: #DC143C (failures, critical items, must-do)
- Warning Gold: #FFD700 (caution, needs review, approaching limits)
- Success Deep Green: #2D5016 (completed, good status, within limits)

**Usage**:
- Headers: Dark green backgrounds with cream text
- Body: Cream background with charcoal text (11pt)
- Status cells: Deep green (good) / Gold (caution) / Crimson (alert)
- Section dividers: Bronze 3pt lines
- Buttons/interactive: Brown wood tone
- Accents: Bronze (luxury feel)

---

## Typography

### Header Hierarchy

**Level 1: Sheet Title**
- Font: Montserrat Bold (Warm) / Georgia Bold (Modern)
- Size: 24pt
- Color: Primary color (navy or dark green)
- Margin: 20px top, 15px bottom
- Example: "DAILY OPENING CHECKLIST"

**Level 2: Section Header**
- Font: Montserrat Semi-Bold (Warm) / Georgia Bold (Modern)
- Size: 16pt
- Color: Primary color background, white text
- Margin: 15px top, 10px bottom
- Example: "Equipment Checks"

**Level 3: Subsection Header**
- Font: Open Sans Semi-Bold (Warm) / Segoe UI Semi-Bold (Modern)
- Size: 13pt
- Color: Primary color
- Margin: 10px top, 8px bottom
- Example: "Temperature Logs"

### Body Text

**Standard Body**
- Font: Open Sans Regular (Warm) / Segoe UI Regular (Modern)
- Size: 11pt
- Line height: 1.5 (10px spacing)
- Color: Navy/Charcoal for dark backgrounds
- Color: Navy/Charcoal for light backgrounds

**Form Labels**
- Font: Open Sans Semi-Bold (Warm) / Segoe UI Semi-Bold (Modern)
- Size: 10pt
- Color: Warm Gray / Brown
- Example: "Item Name | Status | Completed By"

**Input Cells (user editable)**
- Font: Open Sans Regular (Warm) / Segoe UI Regular (Modern)
- Size: 11pt
- Background: White or light cream
- Border: 1pt gray

**Emphasis/Alerts**
- Font: Same as body
- Size: Same as body
- Color: Coral (Warm) / Crimson (Modern)
- Weight: Bold for critical alerts

---

## Visual Elements

### Icons & Symbols

Use these symbols consistently throughout (for accessibility):

| Symbol | Meaning | Usage |
|--------|---------|-------|
| ✓ | Completed/Good | Mark items as done |
| ✗ | Failed/Not Done | Mark incomplete or failed items |
| ⚠ | Warning/Caution | Flag items needing review |
| ⏱ | Time | Timestamp fields |
| 👤 | Person/Staff | Staff assignment, initials |
| 📋 | Task/Document | Manager tasks, audit items |
| 🔴 | Red Alert | Critical issue |
| 🟡 | Yellow Alert | Caution/review needed |
| 🟢 | Green Alert | Good/within limits |

### Cell Formatting

**Header Cells:**
- Background: Primary color (navy/dark green)
- Text: White, bold, centered
- Font size: 12pt
- Padding: 8px
- Border: 1pt light gray

**Data Input Cells:**
- Background: White
- Text: Navy/Charcoal, 11pt
- Border: 1pt gray
- Padding: 5px

**Status/Alert Cells:**
- Background: Color-coded (green/yellow/red)
- Text: White or dark (high contrast)
- Font: Bold for alerts
- Border: 1pt darker shade of background color

**Formula/Auto-Calculate Cells:**
- Background: Light shade of primary color (subtle, indicates read-only)
- Text: Navy/Charcoal, 11pt
- Border: Dashed 1pt gray (indicates system-generated)
- Include note: "(Auto-calculated)"

### Borders & Dividers

**Section Dividers**
- Color: Gold (Warm) / Bronze (Modern)
- Weight: 3pt
- Style: Solid
- Spacing: 10px above and below

**Cell Borders**
- Default: 1pt light gray
- Headers: 1pt darker primary color
- Status cells: 1pt darker alert color
- Form grid: 1pt gray with clear organization

### Spacing Rules

**Margins (all sheets):**
- Top/Bottom: 0.75"
- Left/Right: 0.75"

**Padding (cells):**
- Headers: 8px
- Body: 5px
- Section headers: 10px

**Line Spacing:**
- Between sections: 15px
- Between rows in lists: 5px
- Between checklist items: 8px

**Column Widths (approx):**
- Item name: 2.5"
- Status/checkmark: 0.75"
- Time/date: 1"
- Notes: 2"
- Initials: 0.5"

---

## Layout Specifications

### Print Optimization

**Page Setup:**
- Paper size: 8.5" × 11" (standard letter)
- Orientation: Portrait (checklists), Landscape (schedule/inventory)
- Margins: 0.75" all sides
- Font minimum: 10pt (readable when printed)

**Print Scaling:**
- Design to fit on single page (or multi-page if content-heavy)
- No content should require horizontal scrolling in print
- Avoid colored backgrounds extending to page edges (printer waste)
- Header should repeat on each page (indicate this in print settings)

**Contrast for B&W Printing:**
- All text should be dark (navy, charcoal, black)
- Backgrounds should be cream or white
- Alerts (red/yellow) should be clearly distinct even in grayscale
- Icons and symbols should remain visible in B&W

### Digital/Mobile Optimization

**Responsive Breakpoints:**
- Desktop: Full width with all columns visible
- Tablet (8"): Slightly compressed, all columns still visible
- Mobile (5"): May need horizontal scroll for wide tables, but checkboxes/inputs must be touch-friendly
- Minimum touch target: 24px × 24px (for checkboxes, buttons)

**Mobile Considerations:**
- Scroll horizontally for schedule/inventory if needed (common on mobile)
- Keep essential info (item name, status) always visible in left columns
- Use color-coding heavily (color is visible even at small sizes)
- Avoid tiny text (minimum 11pt for body, 14pt for headers on mobile)

---

## Component Designs

### Checklist Item Layout
```
┌─────────────────────────────────────────────┐
│ ▢ Item Name          [ Status ] 8:15 AM  JD │
│   Notes field: ___________________________ │
└─────────────────────────────────────────────┘
```

- Checkbox: 16pt, left-aligned
- Item name: 11pt bold
- Status dropdown: Centered, yellow/red/green
- Time: Right-aligned, gray text
- Initials: Right-aligned, small (9pt)
- Notes: Full width, lighter background (subtle)

### Schedule Grid
```
┌──────────┬───────┬───────┬───────┬───────┬───────┬───────┬───────┐
│ Position │  Mon  │  Tue  │  Wed  │  Thu  │  Fri  │  Sat  │  Sun  │
├──────────┼───────┼───────┼───────┼───────┼───────┼───────┼───────┤
│ Manager  │10-6pm │10-6pm │ OFF   │10-6pm │10-6pm │8-4pm  │8-4pm  │
│ FOH      │2-9pm  │2-9pm  │2-9pm  │2-9pm  │2-9pm  │2-9pm  │2-9pm  │
│ BOH      │11-8pm │11-8pm │ OFF   │11-8pm │11-8pm │11-8pm │11-8pm │
└──────────┴───────┴───────┴───────┴───────┴───────┴───────┴───────┘
```

- Day headers: Primary color background, white text, bold
- Position names: Left-aligned, bold
- Shift times: Centered, readable
- OFF shifts: Gray background
- Clopen alerts: Red background
- Understaffed: Yellow background

### Inventory Item
```
┌────────────────┬──────┬────────┬──────────┬──────────┐
│ Item           │ Par  │ Current│  Status  │ Supplier │
├────────────────┼──────┼────────┼──────────┼──────────┤
│ Chicken Breast │ 20 lb│ 8 lb   │ 🔴 ORDER │  Vendor A│
└────────────────┴──────┴────────┴──────────┴──────────┘
```

- Item name: Left-aligned, bold
- Par level: Right-aligned, 11pt
- Current quantity: Right-aligned, 11pt
- Status: Center, red/yellow/green background
- Color coding:
  - Green: Above 50% par
  - Yellow: 30-50% par (approaching reorder)
  - Red: Below 30% par (REORDER NOW)

### Alert/Flag Design
```
┌─────────────────────────────────────┐
│  🔴 FAILED: Walk-in Temp Alarm     │
│  Action: Check compressor, refill   │
│  Assigned to: John (Manager)        │
│  Due: Today at 11:00 AM             │
└─────────────────────────────────────┘
```

- Background: Coral/Crimson
- Text: White, readable at 11pt
- Icon: Large and clear
- Call-to-action: Bold, specific action item
- Deadline: Visible, in bold

---

## Brand Customization Tips

### Changing Primary Color
1. Choose your brand color (navy → burgundy, green → teal, etc.)
2. Keep the same brightness level (not too light for text)
3. Ensure contrast with white text (test with WCAG contrast checker)
4. Update all header cells at once (select all headers → fill color)

### Adding Logo
- Insert company logo in top-left or top-right of sheet
- Size: 1-1.5" wide (proportional height)
- Format: PNG or GIF (transparent background preferred)
- Placement: Leave 0.25" margin from edges
- Don't make it larger than sheet title (maintains hierarchy)

### Custom Color Palette
Template colors are suggestions. You can use:
- **Corporate colors**: Match your restaurant's official brand
- **Seasonal themes**: Light pastels (spring), warm tones (fall)
- **Industry standards**: Still maintain red/yellow/green alerts

Just remember:
- High contrast between text and background
- Distinct alert colors (red, yellow, green must be visually different)
- Professional appearance (avoid neon or overly bright colors)

---

## Accessibility Guidelines

### Color Contrast
- Text on colored backgrounds: Minimum 4.5:1 contrast ratio (WCAG AA)
- Test with: WebAIM Contrast Checker or similar tool
- Example: Navy (#2C3E50) on cream (#F5F3F0) = 11.5:1 (excellent)

### Icon Usage
- Never rely on color alone for meaning (red ≠ only red, also use ✗ symbol)
- Include text labels with every icon
- Test icon clarity at small sizes (printed at 100%)

### Font Sizes
- Minimum 10pt for printed documents
- Minimum 11pt for digital reading
- Larger (14-16pt) for important data that's frequently referenced

### Mobile Accessibility
- Touch targets minimum 24px × 24px
- Sufficient spacing between clickable elements
- Text should be readable without zoom on 5" screen

---

## File Format Specifics

### Google Sheets Considerations
- Fonts: Use Google Fonts or system fonts (Arial, Helvetica, Georgia)
- Effects: Conditional formatting for color coding
- Formulas: Use standard Google Sheets functions (SUM, IF, VLOOKUP, etc.)
- Limitations: No macros or VBA (use formulas instead)
- Performance: Keep to under 50 columns, 1000 rows per sheet for responsiveness

### Excel Specifics
- Fonts: Use standard fonts (Arial, Calibri, Garamond)
- Effects: Conditional formatting, data validation dropdowns
- Formulas: Use standard Excel functions
- Optional: Simple macros for one-click reporting (not required)
- Protection: Can lock cells to prevent accidental formula deletion

### PDF Specifics
- Resolution: 300 DPI for crisp printing
- Fonts: Embedded fonts (avoid custom fonts showing as blank)
- Colors: CMYK or RGB (not Pantone)
- File size: Under 10MB for fast download
- Bleeds: No color backgrounds to edges (standard 0.5" margin)

---

## Design Checklist

Before shipping a template, verify:

- [ ] Colors match selected aesthetic (Warm or Modern)
- [ ] Headers clearly show sheet name and date
- [ ] Section headers are visually distinct from body text
- [ ] Alert colors (red/yellow/green) are used consistently
- [ ] All text is readable at 11pt minimum
- [ ] Checkboxes/buttons are at least 24px × 24px
- [ ] Footer shows "Time estimate: X minutes"
- [ ] Print preview looks clean (no awkward page breaks)
- [ ] Mobile view readable without horizontal scroll (if possible)
- [ ] Formulas are hidden from view (shows results only)
- [ ] Status cells show color-coded alerts clearly
- [ ] Logo placement doesn't interfere with content
- [ ] Column widths accommodate longest expected input
- [ ] All borders are consistent (1pt gray, or primary color for headers)
- [ ] White space provides breathing room (not cramped)

---

## Version History

**v1.0** (2026-05-08)
- Initial style guide for Warm & Inviting and Modern aesthetics
- Color palettes, typography, spacing defined
- Print and digital optimization guidelines

---

*For implementation details, see IMPLEMENTATION_GUIDE.md*  
*For project overview, see README.md*
