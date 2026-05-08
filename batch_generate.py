#!/usr/bin/env python3
"""
Batch PDF Generation for Multi-Location Restaurants
Generate customized PDF templates for multiple restaurant locations
"""

import json
import os
from pathlib import Path
from create_interactive_pdfs import PremiumPDFGenerator

class BatchGenerator:
    """Handle batch generation of PDFs for multiple locations."""

    BATCH_CONFIG = "locations.json"

    @staticmethod
    def create_sample_config():
        """Create sample multi-location configuration."""
        config = {
            "locations": [
                {
                    "id": "downtown",
                    "name": "Downtown Location",
                    "address": "123 Main Street, Portland, OR 97205",
                    "phone": "(503) 555-0001",
                    "colors": {
                        "opening_checklist": "#DC3545",
                        "closing_checklist": "#FF9800",
                        "weekly_schedule": "#2196F3",
                        "inventory_sheet": "#4CAF50",
                        "manager_tasks": "#9C27B0"
                    }
                },
                {
                    "id": "eastside",
                    "name": "Eastside Location",
                    "address": "456 Oak Avenue, Portland, OR 97214",
                    "phone": "(503) 555-0002",
                    "colors": {
                        "opening_checklist": "#DC3545",
                        "closing_checklist": "#FF9800",
                        "weekly_schedule": "#2196F3",
                        "inventory_sheet": "#4CAF50",
                        "manager_tasks": "#9C27B0"
                    }
                }
            ],
            "output_directories": True,
            "include_branded_header": True
        }

        with open(BatchGenerator.BATCH_CONFIG, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"✓ Created sample {BatchGenerator.BATCH_CONFIG}")
        print("Edit this file to add your restaurant locations.")
        return config

    @staticmethod
    def load_config():
        """Load batch configuration."""
        if not os.path.exists(BatchGenerator.BATCH_CONFIG):
            print(f"⚠️  {BatchGenerator.BATCH_CONFIG} not found. Creating sample...")
            return BatchGenerator.create_sample_config()

        with open(BatchGenerator.BATCH_CONFIG, 'r') as f:
            return json.load(f)

    @staticmethod
    def generate_batch(config):
        """Generate PDFs for all locations."""
        locations = config.get("locations", [])
        create_dirs = config.get("output_directories", True)

        if not locations:
            print("❌ No locations found in configuration")
            return

        print("\n" + "=" * 70)
        print("🍽️  Batch PDF Generation for Multiple Locations")
        print("=" * 70)

        total_pdfs = 0
        failed_locations = []

        for location in locations:
            location_id = location.get("id", "unknown")
            location_name = location.get("name", "Unknown Location")
            address = location.get("address", "Unknown Address")
            phone = location.get("phone", "")

            print(f"\n📍 {location_name}")
            print(f"   ID: {location_id}")
            print(f"   Address: {address}")

            # Create output directory if enabled
            if create_dirs:
                output_dir = f"PDFs_{location_id}"
                os.makedirs(output_dir, exist_ok=True)
                original_cwd = os.getcwd()
                os.chdir(output_dir)
                print(f"   📁 Output: {output_dir}/")

            try:
                # Generate all 5 templates
                templates = [
                    ("opening_checklist", "Opening Checklist"),
                    ("closing_checklist", "Closing Checklist"),
                    ("weekly_schedule", "Weekly Schedule"),
                    ("inventory_sheet", "Inventory Sheet"),
                    ("manager_tasks", "Manager Tasks"),
                ]

                for template_key, template_name in templates:
                    gen = PremiumPDFGenerator(template_key, location_name, address)

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

                    total_pdfs += 1

                print(f"   ✅ Generated 5 PDFs")

                if create_dirs:
                    os.chdir(original_cwd)

            except Exception as e:
                print(f"   ❌ Error: {str(e)}")
                failed_locations.append(location_name)
                if create_dirs:
                    os.chdir(original_cwd)

        print("\n" + "=" * 70)
        print("✅ Batch generation complete!")
        print(f"   Total PDFs generated: {total_pdfs}")

        if failed_locations:
            print(f"\n⚠️  Failed locations: {', '.join(failed_locations)}")
        else:
            print("\n🎉 All locations generated successfully!")

        if create_dirs:
            print("\n📁 Generated directories:")
            for location in locations:
                location_id = location.get("id", "unknown")
                print(f"   • PDFs_{location_id}/")

    @staticmethod
    def interactive_batch_setup():
        """Interactive setup for multi-location batch generation."""
        print("\n" + "=" * 70)
        print("🍽️  Multi-Location Batch Setup Wizard")
        print("=" * 70)

        locations = []
        location_count = int(input("\nHow many locations? "))

        for i in range(location_count):
            print(f"\n📍 Location {i + 1}")
            location = {
                "id": input("Location ID (e.g., 'downtown'): ").strip().lower().replace(" ", "_"),
                "name": input("Location name: ").strip(),
                "address": input("Address: ").strip(),
                "phone": input("Phone (optional): ").strip() or "",
                "colors": {
                    "opening_checklist": "#DC3545",
                    "closing_checklist": "#FF9800",
                    "weekly_schedule": "#2196F3",
                    "inventory_sheet": "#4CAF50",
                    "manager_tasks": "#9C27B0"
                }
            }
            locations.append(location)

        config = {
            "locations": locations,
            "output_directories": True,
            "include_branded_header": True
        }

        with open(BatchGenerator.BATCH_CONFIG, 'w') as f:
            json.dump(config, f, indent=2)

        print(f"\n✓ Configuration saved to {BatchGenerator.BATCH_CONFIG}")
        return config

    @staticmethod
    def generate_manifest(config):
        """Generate a manifest of all generated PDFs."""
        locations = config.get("locations", [])
        manifest = {
            "generated_date": str(__import__('datetime').datetime.now()),
            "total_locations": len(locations),
            "total_pdfs": len(locations) * 5,
            "locations": []
        }

        for location in locations:
            location_id = location.get("id", "unknown")
            location_name = location.get("name", "Unknown")

            location_manifest = {
                "id": location_id,
                "name": location_name,
                "pdfs": [
                    f"PDFs_{location_id}/opening-checklist.pdf",
                    f"PDFs_{location_id}/closing-checklist.pdf",
                    f"PDFs_{location_id}/weekly-schedule.pdf",
                    f"PDFs_{location_id}/inventory-sheet.pdf",
                    f"PDFs_{location_id}/manager-tasks.pdf",
                ]
            }
            manifest["locations"].append(location_manifest)

        manifest_file = "BATCH_MANIFEST.json"
        with open(manifest_file, 'w') as f:
            json.dump(manifest, f, indent=2)

        print(f"\n📄 Manifest saved to {manifest_file}")

def main():
    """Main batch generation workflow."""
    print("\n" + "=" * 70)
    print("Batch PDF Generation Tool")
    print("=" * 70)

    print("\nOptions:")
    print("1. Interactive setup (recommended for first time)")
    print("2. Use/edit locations.json")
    print("3. Generate from existing config")
    print("4. Create sample config")

    choice = input("\nSelect option (1-4): ").strip()

    if choice == "1":
        config = BatchGenerator.interactive_batch_setup()
        confirm = input("\nGenerate PDFs now? (y/n): ").strip().lower()
        if confirm == "y":
            BatchGenerator.generate_batch(config)
            manifest_confirm = input("Generate manifest file? (y/n): ").strip().lower()
            if manifest_confirm == "y":
                BatchGenerator.generate_manifest(config)

    elif choice == "2":
        if os.path.exists(BatchGenerator.BATCH_CONFIG):
            print(f"\nEdit {BatchGenerator.BATCH_CONFIG} and run with option 3")
        else:
            BatchGenerator.create_sample_config()

    elif choice == "3":
        config = BatchGenerator.load_config()
        BatchGenerator.generate_batch(config)
        manifest_confirm = input("\nGenerate manifest file? (y/n): ").strip().lower()
        if manifest_confirm == "y":
            BatchGenerator.generate_manifest(config)

    elif choice == "4":
        BatchGenerator.create_sample_config()

    else:
        print("Invalid option")

    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()
