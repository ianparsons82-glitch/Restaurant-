#!/usr/bin/env python3
"""
Customization script for Premium PDF Templates
Allows easy modification of restaurant details, colors, and checklist items
"""

import json
import os
from create_interactive_pdfs import PremiumPDFGenerator

class TemplateCustomizer:
    """Handle customization of PDF templates."""

    CONFIG_FILE = "template_config.json"

    @staticmethod
    def create_default_config():
        """Create default configuration file."""
        config = {
            "restaurant": {
                "name": "Restaurant Name",
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
            },
            "customization": {
                "opening_checklist_items": [],
                "closing_checklist_items": [],
                "inventory_items": []
            }
        }

        with open(TemplateCustomizer.CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"✓ Created {TemplateCustomizer.CONFIG_FILE}")
        print("Edit this file to customize your templates.")
        return config

    @staticmethod
    def load_config():
        """Load configuration from file."""
        if not os.path.exists(TemplateCustomizer.CONFIG_FILE):
            print(f"⚠️  {TemplateCustomizer.CONFIG_FILE} not found. Creating default...")
            return TemplateCustomizer.create_default_config()

        with open(TemplateCustomizer.CONFIG_FILE, 'r') as f:
            return json.load(f)

    @staticmethod
    def interactive_setup():
        """Run interactive setup wizard."""
        print("\n" + "=" * 60)
        print("🎨 PDF Template Customization Wizard")
        print("=" * 60)

        config = {
            "restaurant": {},
            "colors": {
                "opening_checklist": "#DC3545",
                "closing_checklist": "#FF9800",
                "weekly_schedule": "#2196F3",
                "inventory_sheet": "#4CAF50",
                "manager_tasks": "#9C27B0"
            }
        }

        # Restaurant info
        print("\n📍 Restaurant Information")
        config["restaurant"]["name"] = input("Restaurant name (default 'Restaurant Name'): ").strip() or "Restaurant Name"
        config["restaurant"]["address"] = input("Address (default '123 Main Street...'): ").strip() or "123 Main Street, City, State 12345"
        config["restaurant"]["phone"] = input("Phone number (optional): ").strip() or ""

        # Colors
        print("\n🎨 Template Colors (optional - press Enter to keep defaults)")
        colors_info = [
            ("opening_checklist", "Opening Checklist (RED)", "#DC3545"),
            ("closing_checklist", "Closing Checklist (ORANGE)", "#FF9800"),
            ("weekly_schedule", "Weekly Schedule (BLUE)", "#2196F3"),
            ("inventory_sheet", "Inventory Sheet (GREEN)", "#4CAF50"),
            ("manager_tasks", "Manager Tasks (PURPLE)", "#9C27B0"),
        ]

        for key, name, default_color in colors_info:
            color_input = input(f"{name} [{default_color}]: ").strip()
            if color_input:
                config["colors"][key] = color_input

        # Save config
        with open(TemplateCustomizer.CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Configuration saved to {TemplateCustomizer.CONFIG_FILE}")
        return config

    @staticmethod
    def generate_from_config(config):
        """Generate PDFs using configuration."""
        rest_info = config.get("restaurant", {})
        rest_name = rest_info.get("name", "Restaurant Name")
        rest_addr = rest_info.get("address", "123 Main Street, City, State 12345")

        templates = [
            ("opening_checklist", "Daily Opening Checklist"),
            ("closing_checklist", "Daily Closing Checklist"),
            ("weekly_schedule", "Weekly Schedule & Labor Tracker"),
            ("inventory_sheet", "Inventory Management Sheet"),
            ("manager_tasks", "Manager Daily & Weekly Tasks"),
        ]

        print("\n" + "=" * 60)
        print("🎨 Generating Customized PDF Templates")
        print("=" * 60)

        for template_key, description in templates:
            gen = PremiumPDFGenerator(template_key, rest_name, rest_addr)
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
        print("✅ Customized PDFs generated successfully!")
        print("\nRestaurant: " + rest_name)
        print("Address: " + rest_addr)
        print("\n📋 Generated Files:")
        for _, name in templates:
            print(f"   • {name}")

def main():
    """Main customization workflow."""
    print("\n" + "=" * 60)
    print("PDF Template Customization Tool")
    print("=" * 60)

    print("\nOptions:")
    print("1. Interactive setup (recommended for first time)")
    print("2. Use/edit template_config.json")
    print("3. Generate from existing config")
    print("4. Create default config.json")

    choice = input("\nSelect option (1-4): ").strip()

    if choice == "1":
        config = TemplateCustomizer.interactive_setup()
        confirm = input("\nGenerate PDFs now? (y/n): ").strip().lower()
        if confirm == "y":
            TemplateCustomizer.generate_from_config(config)
    elif choice == "2":
        if os.path.exists(TemplateCustomizer.CONFIG_FILE):
            print(f"\nEdit {TemplateCustomizer.CONFIG_FILE} and run with option 3")
        else:
            TemplateCustomizer.create_default_config()
    elif choice == "3":
        config = TemplateCustomizer.load_config()
        TemplateCustomizer.generate_from_config(config)
    elif choice == "4":
        TemplateCustomizer.create_default_config()
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
