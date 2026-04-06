from PIL import Image, ImageDraw, ImageFont
import math
import random

random.seed(42)

W, H = 2400, 1200
img = Image.new("RGB", (W, H), "#FAF6EF")
draw = ImageDraw.Draw(img)

# ─── FONTS ───
def font(size):
    try: return ImageFont.truetype("arial.ttf", size)
    except: return ImageFont.load_default()

def font_bold(size):
    try: return ImageFont.truetype("arialbd.ttf", size)
    except: return font(size)

def font_italic(size):
    try: return ImageFont.truetype("ariali.ttf", size)
    except: return font(size)

# ─── COLORS ───
PURPLE = "#862e9c"
PURPLE_BG = "#f3d9fa"
GREEN = "#2f9e44"
GREEN_BG = "#d3f9d8"
RED = "#c92a2a"
RED_BG = "#ffe3e3"
TEAL = "#087f5b"
TEAL_BG = "#c3fae8"
ORANGE = "#d9480f"
ORANGE_BG = "#ffe8cc"
BLUE = "#1971c2"
BLUE_BG = "#d0ebff"
YELLOW = "#e67700"
YELLOW_BG = "#fff3bf"
PINK = "#a61e4d"
PINK_BG = "#fcc2d7"
DARK = "#1e1e1e"
BODY = "#495057"
GRAY = "#868e96"
LIGHT_GRAY = "#ced4da"
WHITE = "#FFFFFF"

# ─── HELPERS ───

def cloud_bubble(cx, cy, w, h, fill, outline, width=3):
    """Draw a wobbly cloud-like bubble shape"""
    r = min(w, h) // 3
    draw.rounded_rectangle([cx - w//2, cy - h//2, cx + w//2, cy + h//2],
                           radius=r, fill=fill, outline=outline, width=width)
    # Add wobble passes
    for _ in range(2):
        ox, oy = random.randint(-2, 2), random.randint(-2, 2)
        draw.rounded_rectangle([cx - w//2 + ox, cy - h//2 + oy, cx + w//2 + ox, cy + h//2 + oy],
                               radius=r, fill=None, outline=outline, width=1)

def sketchy_line(x1, y1, x2, y2, color, width=2):
    """Draw a slightly wobbly line"""
    mx = (x1 + x2) / 2 + random.randint(-3, 3)
    my = (y1 + y2) / 2 + random.randint(-3, 3)
    draw.line([(x1, y1), (mx, my), (x2, y2)], fill=color, width=width)

def sunburst(cx, cy, inner_r, outer_r, color, n_rays=16, width=3):
    """Draw radiating spiky lines like Clawdbot"""
    for i in range(n_rays):
        angle = (2 * math.pi * i / n_rays) + random.uniform(-0.1, 0.1)
        r_out = outer_r + random.randint(-8, 8)
        x1 = cx + inner_r * math.cos(angle)
        y1 = cy + inner_r * math.sin(angle)
        x2 = cx + r_out * math.cos(angle)
        y2 = cy + r_out * math.sin(angle)
        draw.line([(x1, y1), (x2, y2)], fill=color, width=width)

def doodle_icon_camera(x, y, color, size=24):
    """Tiny camera doodle"""
    draw.rounded_rectangle([x, y, x+size, y+size*0.7], radius=4, outline=color, width=2)
    draw.ellipse([x+size*0.3, y+size*0.15, x+size*0.7, y+size*0.55], outline=color, width=2)

def doodle_icon_doc(x, y, color, size=20):
    """Tiny document doodle"""
    draw.rectangle([x, y, x+size*0.7, y+size], outline=color, width=2)
    draw.polygon([(x+size*0.5, y), (x+size*0.7, y+size*0.2), (x+size*0.5, y+size*0.2)], outline=color)
    for i in range(3):
        draw.line([(x+3, y+size*0.35+i*size*0.18), (x+size*0.5, y+size*0.35+i*size*0.18)], fill=color, width=1)

def doodle_icon_search(x, y, color, size=20):
    """Tiny magnifying glass"""
    draw.ellipse([x, y, x+size*0.7, y+size*0.7], outline=color, width=2)
    draw.line([(x+size*0.55, y+size*0.55), (x+size, y+size)], fill=color, width=2)

def doodle_icon_wand(x, y, color, size=20):
    """Tiny wand with sparkle"""
    draw.line([(x, y+size), (x+size, y)], fill=color, width=2)
    draw.text((x+size-2, y-5), "*", font=font_bold(12), fill=color)

def doodle_icon_stethoscope(x, y, color, size=20):
    """Tiny stethoscope"""
    draw.arc([x, y, x+size*0.6, y+size*0.4], start=180, end=0, fill=color, width=2)
    draw.line([(x, y+size*0.2), (x, y+size*0.7)], fill=color, width=2)
    draw.ellipse([x-3, y+size*0.7, x+5, y+size*0.85], fill=color)

def doodle_icon_layers(x, y, color, size=20):
    """Tiny stacked layers"""
    for i in range(3):
        off = i * 5
        draw.rounded_rectangle([x+off, y+off, x+size*0.7+off, y+size*0.4+off], radius=3, outline=color, width=2)

def doodle_icon_folder(x, y, color, size=20):
    """Tiny folder"""
    draw.rectangle([x, y+4, x+size, y+size], outline=color, width=2)
    draw.line([(x, y+4), (x+size*0.3, y+4), (x+size*0.4, y), (x+size*0.7, y), (x+size*0.7, y+4)], fill=color, width=2)

def doodle_icon_share(x, y, color, size=20):
    """Tiny share/export icon"""
    draw.line([(x+size*0.5, y+size), (x+size*0.5, y+size*0.3)], fill=color, width=2)
    draw.polygon([(x+size*0.5, y), (x+size*0.25, y+size*0.3), (x+size*0.75, y+size*0.3)], fill=color)
    draw.arc([x, y+size*0.6, x+size, y+size*1.1], start=0, end=180, fill=color, width=2)

def badge(x, y, text, bg, fg, outline):
    tw = draw.textbbox((0,0), text, font=font_bold(13))[2] - draw.textbbox((0,0), text, font=font_bold(13))[0]
    pw = tw + 20
    draw.rounded_rectangle([x, y, x+pw, y+26], radius=13, fill=bg, outline=outline, width=2)
    draw.text((x+10, y+4), text, font=font_bold(13), fill=fg)
    return pw

# ─── SCATTERED DOTS ───
for _ in range(80):
    dx, dy = random.randint(20, W-20), random.randint(20, H-20)
    dr = random.uniform(1.5, 3)
    draw.ellipse([dx-dr, dy-dr, dx+dr, dy+dr], fill=random.choice(["#e9ecef", "#dee2e6"]))

# ═══════════════════════════════════════════════════════
# TITLE (hand-written feel, top center)
# ═══════════════════════════════════════════════════════

draw.text((W//2, 30), "The Flow Heist", fill=DARK, font=font_bold(62), anchor="mt")

# Sparkle doodles around title
for sx, sy in [(420, 25), (440, 60), (1950, 30), (1970, 55)]:
    for a in range(0, 360, 45):
        r = math.radians(a)
        s = random.randint(6, 10)
        draw.line([(sx, sy), (sx + s*math.cos(r), sy + s*math.sin(r))], fill=TEAL, width=2)

draw.text((W//2, 95), "Screenshot any automation.  Get a rebuild guide.  Steal the pattern.", fill=GRAY, font=font_italic(20), anchor="mt")

# ═══════════════════════════════════════════════════════
# CENTRAL MASCOT AREA (camera with sunburst)
# ═══════════════════════════════════════════════════════

cx, cy = W//2, 480

# Sunburst rays (Clawdbot style)
sunburst(cx, cy, 85, 155, TEAL_BG, 20, 3)
sunburst(cx, cy, 90, 135, TEAL, 14, 2)

# Central circle
draw.ellipse([cx-80, cy-80, cx+80, cy+80], fill=WHITE, outline=TEAL, width=4)

# Camera icon inside
draw.rounded_rectangle([cx-35, cy-25, cx+35, cy+20], radius=8, outline=TEAL, width=3, fill=TEAL_BG)
draw.ellipse([cx-14, cy-14, cx+14, cy+8], outline=TEAL, width=3, fill=WHITE)
draw.ellipse([cx-5, cy-7, cx+5, cy+1], fill=TEAL)
draw.rectangle([cx+18, cy-25, cx+28, cy-18], fill=TEAL)

# Labels
draw.text((cx, cy + 95), "Screenshot In", fill=TEAL, font=font_bold(20), anchor="mt")
draw.text((cx, cy + 118), "/flow-capture", fill=TEAL, font=font_italic(16), anchor="mt")

# ═══════════════════════════════════════════════════════
# FEATURE BUBBLES (radiating outward like Clawdbot)
# ═══════════════════════════════════════════════════════

# --- TOP LEFT: Capture ---
bx, by = 300, 210
cloud_bubble(bx, by, 340, 130, PURPLE_BG, PURPLE)
doodle_icon_camera(bx-150, by-45, PURPLE, 22)
draw.text((bx, by-40), "/flow-capture", fill=PURPLE, font=font_bold(20), anchor="mt")
draw.text((bx, by-12), "Reads any screenshot", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+10), "Maps every element", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+32), "Full rebuild guide", fill=PURPLE, font=font_bold(15), anchor="mt")
sketchy_line(bx + 140, by + 50, cx - 85, cy - 50, PURPLE, 2)

# --- TOP RIGHT: Library ---
bx, by = 2100, 210
cloud_bubble(bx, by, 340, 130, GREEN_BG, GREEN)
doodle_icon_search(bx+130, by-50, GREEN, 22)
draw.text((bx, by-40), "/flow-library", fill=GREEN, font=font_bold(20), anchor="mt")
draw.text((bx, by-12), "Save every captured flow", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+10), "Search by platform, type", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+32), "100+ flows by month 3", fill=GREEN, font=font_bold(15), anchor="mt")
sketchy_line(bx - 140, by + 50, cx + 85, cy - 50, GREEN, 2)

# --- LEFT: Adapt ---
bx, by = 180, 560
cloud_bubble(bx, by, 300, 120, ORANGE_BG, ORANGE)
doodle_icon_wand(bx-130, by-40, ORANGE, 20)
draw.text((bx, by-35), "/flow-adapt", fill=ORANGE, font=font_bold(20), anchor="mt")
draw.text((bx, by-8), "Rewrite for YOUR business", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+14), "Same structure, new copy", fill=ORANGE, font=font_bold(15), anchor="mt")
sketchy_line(bx + 150, by, cx - 85, cy, ORANGE, 2)

# --- RIGHT: Audit ---
bx, by = 2220, 560
cloud_bubble(bx, by, 300, 120, RED_BG, RED)
doodle_icon_stethoscope(bx+120, by-45, RED, 22)
draw.text((bx, by-35), "/flow-audit", fill=RED, font=font_bold(20), anchor="mt")
draw.text((bx, by-8), "10-point diagnostic", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+14), "GREEN / YELLOW / RED", fill=RED, font=font_bold(15), anchor="mt")
sketchy_line(bx - 150, by, cx + 85, cy, RED, 2)

# --- BOTTOM LEFT: Templates ---
bx, by = 350, 780
cloud_bubble(bx, by, 340, 120, YELLOW_BG, YELLOW)
doodle_icon_layers(bx-150, by-40, YELLOW, 22)
draw.text((bx, by-35), "/flow-templates", fill=YELLOW, font=font_bold(20), anchor="mt")
draw.text((bx, by-8), "8 proven architectures", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+14), "Personalized to you", fill=YELLOW, font=font_bold(15), anchor="mt")
sketchy_line(bx + 130, by - 40, cx - 60, cy + 75, YELLOW, 2)

# --- BOTTOM CENTER: Batch ---
bx, by = W//2, 770
cloud_bubble(bx, by, 340, 110, BLUE_BG, BLUE)
doodle_icon_folder(bx-150, by-35, BLUE, 22)
draw.text((bx, by-30), "/flow-batch", fill=BLUE, font=font_bold(20), anchor="mt")
draw.text((bx, by-3), "Folder of screenshots in", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+19), "All processed at once", fill=BLUE, font=font_bold(15), anchor="mt")
sketchy_line(bx, by - 55, cx, cy + 80, BLUE, 2)

# --- BOTTOM RIGHT: Export ---
bx, by = 2050, 780
cloud_bubble(bx, by, 300, 120, PINK_BG, PINK)
doodle_icon_share(bx+120, by-40, PINK, 22)
draw.text((bx, by-35), "/flow-export", fill=PINK, font=font_bold(20), anchor="mt")
draw.text((bx, by-8), "Markdown + PDF", fill=BODY, font=font(15), anchor="mt")
draw.text((bx, by+14), "Share with anyone", fill=PINK, font=font_bold(15), anchor="mt")
sketchy_line(bx - 130, by - 40, cx + 60, cy + 75, PINK, 2)

# ═══════════════════════════════════════════════════════
# "WHAT YOU GET" callout (top center, between title and hub)
# ═══════════════════════════════════════════════════════

gx, gy = W//2, 155
draw.rounded_rectangle([gx-280, gy-30, gx+280, gy+30], radius=20, fill=TEAL_BG, outline=TEAL, width=2)
draw.text((gx, gy-8), "Strategy  +  Flow Map  +  Rebuild Guide  +  Copy  +  Checklist", fill=TEAL, font=font_bold(16), anchor="mt")

# ═══════════════════════════════════════════════════════
# BOTTOM SECTION: Platforms + How to Use
# ═══════════════════════════════════════════════════════

# Platforms
py = 920
draw.text((200, py), "PLATFORMS", fill=GRAY, font=font_bold(14))
x = 340
for name, bg, fg, border in [
    ("ManyChat", PURPLE_BG, PURPLE, PURPLE),
    ("GoHighLevel", ORANGE_BG, ORANGE, ORANGE),
    ("n8n", GREEN_BG, GREEN, GREEN),
    ("Make", BLUE_BG, BLUE, BLUE),
    ("Zapier", YELLOW_BG, YELLOW, YELLOW),
]:
    pw = badge(x, py - 2, name, bg, fg, border)
    x += pw + 12

# How to use (casual, bottom right)
draw.text((1400, py), "HOW TO USE", fill=GRAY, font=font_bold(14))
draw.text((1400, py + 25), "1. Screenshot any flow", fill=BODY, font=font(16))
draw.text((1400, py + 48), "2. /flow-capture", fill=BODY, font=font_bold(16))
draw.text((1400, py + 71), "3. Done.", fill=TEAL, font=font_bold(16))

# ═══════════════════════════════════════════════════════
# BOTTOM BADGES (like Clawdbot's stars/taglines)
# ═══════════════════════════════════════════════════════

by = 1040
x = 300
for text, bg, fg, border in [
    ("Free + Open Source", TEAL_BG, TEAL, TEAL),
    ("MIT License", GREEN_BG, GREEN, GREEN),
    ("No API keys for core features", BLUE_BG, BLUE, BLUE),
    ("Claude Code + Airtable", PURPLE_BG, PURPLE, PURPLE),
    ("Works on any platform", YELLOW_BG, YELLOW, YELLOW),
]:
    pw = badge(x, by, text, bg, fg, border)
    x += pw + 15

# Footer
draw.text((W//2, H-25), "github.com/seancrowe01/flow-heist", fill=LIGHT_GRAY, font=font(14), anchor="mm")

# ═══════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════

out = "C:/Users/me/amber-ai/flow-machine/docs/blueprint.png"
img.save(out, "PNG", quality=95)
print(f"Saved to {out}")
print(f"Size: {img.size}")
