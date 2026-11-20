#!/usr/bin/env python3
"""GTA6-01 thumbnail — top-down neon city game"""
from PIL import Image, ImageDraw, ImageFont
import random, os

W, H = 1280, 720
img = Image.new('RGB', (W, H), '#0a0a14')
draw = ImageDraw.Draw(img)

# Sky gradient — synthwave sunset
for y in range(H):
    r = int(10 + (y/H) * 80)
    g = int(10 + (y/H) * 10)
    b = int(20 + (y/H) * 60)
    draw.line([(0, y), (W, y)], fill=(r, g, b))

# Sun
for i in range(100, 0, -1):
    alpha = int(100 - i)
    clr = (255, min(100 + i, 255), min(40 + i, 255))
    draw.ellipse([640-i, 300-i, 640+i, 300+i], fill=clr)

# Ground
draw.rectangle([0, 520, W, H], fill='#111122')

# Road
road_y = 520
draw.rectangle([0, road_y, W, road_y + 80], fill='#222233')
for i in range(0, W, 60):
    draw.rectangle([i, road_y + 37, i + 30, road_y + 43], fill='#ffcc00')

# Buildings silhouette
for bx in range(0, W, 80):
    bh = random.randint(60, 200)
    bcolor = f'#{random.randint(10,30):02x}{random.randint(10,25):02x}{random.randint(30,60):02x}'
    draw.rectangle([bx, road_y - bh, bx + 70, road_y], fill=bcolor)
    # Windows lit
    for wy in range(road_y - bh + 10, road_y - 10, 20):
        for wx in range(bx + 10, bx + 60, 15):
            if random.random() > 0.39:
                wc = random.choice(['#ffdd88', '#ff6699', '#66ccff', '#ffaa44'])
                draw.rectangle([wx, wy, wx + 6, wy + 8], fill=wc)

# Palm trees
for px in [150, 350, 850, 1050]:
    draw.rectangle([px-4, road_y-140, px+4, road_y], fill='#2a1f0e')
    for _ in range(5):
        angle = random.uniform(-0.8, 0.8)
        lx = px + int(30 * random.uniform(0.5, 1.2) * (1 if random.random() > 0.5 else -1))
        ly = road_y - 140 - random.randint(0, 30)
        draw.ellipse([lx-15, ly-8, lx+25, ly+8], fill='#1a5c2a')

# Car — pink neon sports car from top-down
cx, cy = 640, 540
car_clr = '#ff2e6e'
# Shadow
draw.rectangle([cx-46, cy-7, cx+46, cy+9], fill='#00000044')
# Body
draw.rectangle([cx-45, cy-13, cx+45, cy+13], fill=car_clr)
# Dark top
draw.rectangle([cx-40, cy-9, cx-5, cy+9], fill='#cc1144')
draw.rectangle([cx+5, cy-9, cx+40, cy+9], fill='#cc1144')
# Windshield
draw.rectangle([cx-8, cy-7, cx-2, cy+7], fill='#88ccff')
draw.rectangle([cx+2, cy-7, cx+8, cy+7], fill='#88ccff')
# Wheels
draw.rectangle([cx-42, cy-16, cx-32, cy-13], fill='#111')
draw.rectangle([cx-42, cy+13, cx-32, cy+16], fill='#111')
draw.rectangle([cx+32, cy-16, cx+42, cy-13], fill='#111')
draw.rectangle([cx+32, cy+13, cx+42, cy+16], fill='#111')
# Headlights
draw.ellipse([cx+43, cy-6, cx+49, cy-2], fill='#ffaa00')
draw.ellipse([cx+43, cy+2, cx+49, cy+6], fill='#ffaa00')

# Neon glow under car
draw.rectangle([cx-40, cy+14, cx+40, cy+18], fill='#ff2e6e88')

# Title
try:
    font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 64)
    font_sm = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 28)
except:
    font_big = ImageFont.load_default()
    font_sm = ImageFont.load_default()

# Shadow text
for ox, oy in [(-2,-2), (-2,2), (2,-2), (2,2)]:
    draw.text((50+ox, 60+oy), "GTA VI", fill='black', font=font_big)
draw.text((50, 60), "GTA VI", fill='#ff2e6e', font=font_big)
draw.text((50, 140), "VICE CITY BROWSER EDITION", fill='white', font=font_sm)

# HUD elements
draw.rectangle([W-280, 20, W-20, 55], fill='#000000aa')
draw.text((W-270, 25), " ★★★☆☆  $12,450  ❤️ 87", fill='white', font=font_sm)

os.makedirs("/output", exist_ok=True)
img.save("/output/gta6-01-thumb.png", "PNG")
print("gta6-01-thumb.png generated")