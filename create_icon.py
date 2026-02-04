#!/usr/bin/env python3
"""
Create app icon for Social Media Downloader
Generates a simple but professional icon with PIL
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """Create app icon with download arrow"""
    
    # Icon sizes to generate
    sizes = {
        'icon.png': 512,  # Base icon
        'icon_large.png': 1024,  # For macOS .icns
    }
    
    output_dir = 'src/assets'
    os.makedirs(output_dir, exist_ok=True)
    
    for filename, size in sizes.items():
        # Create image with gradient background
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        # Draw rounded rectangle background (blue gradient)
        margin = size // 10
        draw.rounded_rectangle(
            [margin, margin, size - margin, size - margin],
            radius=size // 8,
            fill=(59, 142, 208, 255)  # Blue color from app theme
        )
        
        # Draw download arrow (white)
        arrow_width = size // 15
        arrow_top = size // 3
        arrow_bottom = size * 2 // 3
        center_x = size // 2
        
        # Vertical line
        draw.rectangle(
            [center_x - arrow_width, arrow_top, 
             center_x + arrow_width, arrow_bottom],
            fill=(255, 255, 255, 255)
        )
        
        # Arrow head (triangle)
        arrow_head_size = size // 5
        arrow_head_y = arrow_bottom - arrow_width
        draw.polygon([
            (center_x, arrow_bottom + arrow_head_size // 2),  # Bottom point
            (center_x - arrow_head_size, arrow_head_y),  # Left point
            (center_x + arrow_head_size, arrow_head_y),  # Right point
        ], fill=(255, 255, 255, 255))
        
        # Save icon
        output_path = os.path.join(output_dir, filename)
        img.save(output_path, 'PNG')
        print(f"✓ Created {output_path}")
    
    print("\n📝 Next steps:")
    print("1. For macOS (.icns):")
    print("   - Use online converter: https://cloudconvert.com/png-to-icns")
    print("   - Upload: src/assets/icon_large.png")
    print("   - Download as: icon.icns")
    print("   - Save to: src/assets/icon.icns")
    print("\n2. For Windows (.ico):")
    print("   - Use online converter: https://convertio.co/png-ico/")
    print("   - Upload: src/assets/icon_large.png")
    print("   - Download as: icon.ico")
    print("   - Save to: src/assets/icon.ico")
    print("\n3. Update build_macos.spec:")
    print("   Change: icon=None")
    print("   To: icon='src/assets/icon.icns'")
    print("\n4. Update build_windows.spec:")
    print("   Change: icon=None")
    print("   To: icon='src/assets/icon.ico'")
    print("\n5. Rebuild: ./build.sh")

if __name__ == "__main__":
    print("Creating Video Downloader icon...")
    print("=" * 50)
    create_icon()
    print("=" * 50)
    print("✅ Icons created successfully!")
