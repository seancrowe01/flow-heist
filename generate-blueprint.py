from PIL import Image, ImageDraw, ImageFont
import math
import random

random.seed(77)

W, H = 2000, 1300
img = Image.new("RGB", (W, H), "#FAF6EF")
draw = ImageDraw.Draw(img)

# ─── FONTS ───
def font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        return ImageFont.load_default()

def font_bold(size):
    try:
        return ImageFont.truetype("arialbd.ttf", size)
    except:
        return font(size)

def font_italic(size):
    try:
        return ImageFont.truetype("ariali.ttf", size)
    except:
        return font(size)

f_title = font_bold(52)
f_subtitle = font(22)
f_section = font_bold(22)
f_body = font(15)
f_body_bold = font_bold(15)
f_small = font(13)
f_badge = font_bold(12)
f_tiny = font(11)

# ─── COLORS ───
CREAM = "#FAF6EF"
DARK = "#2D2D2D"
DARK_BODY = "#4A4A4A"
GRAY = "#7A7A7A"
LIGHT_GRAY = "#B0B0B0"

TEAL = "#0D9488"
TEAL_BG = "#E6FAF7"
TEAL_BORDER = "#2DD4BF"

GREEN = "#16A34A"
GREEN_BG = "#ECFDF5"
GREEN_BORDER = "#4ADE80"

ORANGE = "#EA580C"
ORANGE_BG = "#FFF7ED"
ORANGE_BORDER = "#FB923C"

BLUE = "#2563EB"
BLUE_BG = "#EFF6FF"
BLUE_BORDER = "#60A5FA"

PURPLE = "#7C3AED"
PURPLE_BG = "#F5F3FF"
PURPLE_BORDER = "#A78BFA"

PINK = "#DB2777"
PINK_BG = "#FDF2F8"
PINK_BORDER = "#F472B6"

RED = "#DC2626"
RED_BG = "#FEF2F2"
RED_BORDER = "#F87171"

YELLOW = "#CA8A04"
YELLOW_BG = "#FEFCE8"
YELLOW_BORDER = "#FACC15"

WHITE = "#FFFFFF"

# ─── DRAWING HELPERS ───

def sketchy_rect(x, y, w, h, fill, border_color, border_width=3, radius=16):
    draw.rounded_rectangle([x, y, x+w, y+h], radius=radius, fill=fill)
    for offset in range(border_width):
        o = offset * 0.5
        draw.rounded_rectangle(
            [x+o, y+o, x+w-o, y+h-o],
            radius=radius, fill=None, outline=border_color, width=1
        )

def dashed_line(x1, y1, x2, y2, color=GRAY, width=2, dash_len=8, gap_len=5):
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return
    ux, uy = dx/length, dy/length
    pos = 0
    while pos < length:
        sx = x1 + ux * pos
        sy = y1 + uy * pos
        end = min(pos + dash_len, length)
        ex = x1 + ux * end
        ey = y1 + uy * end
        draw.line([(sx, sy), (ex, ey)], fill=color, width=width)
        pos += dash_len + gap_len

def arrow_down(x, y1, y2, color=DARK, width=2):
    draw.line([(x, y1), (x, y2)], fill=color, width=width)
    draw.polygon([(x, y2), (x-7, y2-12), (x+7, y2-12)], fill=color)

def arrow_right(x1, y, x2, color=DARK, width=2):
    draw.line([(x1, y), (x2, y)], fill=color, width=width)
    draw.polygon([(x2, y), (x2-12, y-7), (x2-12, y+7)], fill=color)

def text_center(x, y, w, text, f, fill=DARK):
    bbox = draw.textbbox((0, 0), text, font=f)
    tw = bbox[2] - bbox[0]
    draw.text((x + (w - tw) // 2, y), text, font=f, fill=fill)

def badge(x, y, text, bg, fg, border):
    tw = draw.textbbox((0,0), text, font=f_badge)[2] - draw.textbbox((0,0), text, font=f_badge)[0]
    pw = tw + 20
    sketchy_rect(x, y, pw, 24, bg, border, border_width=2, radius=12)
    draw.text((x+10, y+4), text, font=f_badge, fill=fg)

def icon_circle(cx, cy, r, color):
    draw.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)

# ─── DECORATIVE DOTS ───
for _ in range(40):
    dx = random.randint(20, W-20)
    dy = random.randint(20, H-20)
    dr = random.uniform(1.5, 3)
    dc = random.choice(["#E5E5E5", "#D4D4D4", "#EBEBEB"])
    icon_circle(dx, dy, dr, dc)

# ═══════════════════════════════════════════════════════
# TITLE
# ═══════════════════════════════════════════════════════

text_center(0, 28, W, "THE FLOW HEIST", f_title, DARK)
for sx, sy in [(340, 30), (355, 55), (1620, 35), (1640, 58)]:
    draw.text((sx, sy), "*", font=font_bold(18), fill=TEAL)

text_center(0, 90, W, "Screenshot Any Automation.  Get a Rebuild Guide.  --  Built in Claude Code", f_subtitle, GRAY)

# ═══════════════════════════════════════════════════════
# ROW 1: SCREENSHOT INPUT (top center)
# ═══════════════════════════════════════════════════════

sketchy_rect(650, 140, 700, 130, BLUE_BG, BLUE_BORDER, border_width=3)

# Camera icon
cx, cy = 670, 155
draw.rectangle([cx, cy, cx+20, cy+14], outline=BLUE, width=2)
draw.ellipse([cx+6, cy+3, cx+14, cy+11], outline=BLUE, width=2)

draw.text((700, 148), "SCREENSHOT IN", font=f_section, fill=BLUE)
draw.text((700, 180), "ManyChat flow builder  |  DM conversations  |  GHL workflows  |  n8n  |  Make", font=f_body, fill=DARK_BODY)
draw.text((700, 202), "Drop any automation screenshot. Claude vision reads every element.", font=f_body, fill=DARK_BODY)

badge(700, 230, "Claude Vision", BLUE_BG, BLUE, BLUE_BORDER)
badge(840, 230, "No OCR needed", BLUE_BG, BLUE, BLUE_BORDER)

# ═══════════════════════════════════════════════════════
# ARROW: Screenshot → Row 2
# ═══════════════════════════════════════════════════════

arrow_down(1000, 275, 330, DARK, 2)

# ═══════════════════════════════════════════════════════
# ROW 2: CAPTURE → REBUILD GUIDE → FLOW LIBRARY
# ═══════════════════════════════════════════════════════

row2_y = 340

# ─── FLOW CAPTURE ───
sketchy_rect(80, row2_y, 380, 200, PURPLE_BG, PURPLE_BORDER, border_width=3)

# Eye icon
ex, ey = 100, row2_y + 10
draw.ellipse([ex, ey, ex+20, ey+14], outline=PURPLE, width=2)
draw.ellipse([ex+7, ey+3, ex+13, ey+11], fill=PURPLE)

draw.text((130, row2_y + 8), "/flow-capture", font=f_section, fill=PURPLE)
draw.text((100, row2_y + 45), "Identify platform automatically", font=f_body, fill=DARK_BODY)
draw.text((100, row2_y + 67), "Map every element (triggers,", font=f_body, fill=DARK_BODY)
draw.text((100, row2_y + 89), "messages, conditions, actions)", font=f_body, fill=DARK_BODY)
draw.text((100, row2_y + 111), "Match to known flow pattern", font=f_body, fill=DARK_BODY)
draw.text((100, row2_y + 133), "Extract all message copy", font=f_body, fill=DARK_BODY)
draw.text((100, row2_y + 158), "Flag compliance issues", font=f_body, fill=DARK_BODY)

# ─── ARROW ───
arrow_right(465, row2_y + 100, 530, DARK, 2)

# ─── REBUILD GUIDE (the star) ───
sketchy_rect(540, row2_y - 20, 480, 240, TEAL_BG, TEAL_BORDER, border_width=4, radius=18)

for sx, sy in [(555, row2_y - 15), (985, row2_y - 15), (555, row2_y + 185), (985, row2_y + 185)]:
    draw.text((sx, sy), "*", font=font_bold(20), fill=TEAL)

text_center(540, row2_y - 8, 480, "REBUILD GUIDE", font_bold(28), TEAL)

# Document icon
dx, dy = 960, row2_y - 5
draw.rectangle([dx, dy, dx+16, dy+20], outline=TEAL, width=2)
draw.polygon([(dx+10, dy), (dx+16, dy+6), (dx+10, dy+6)], outline=TEAL, fill=TEAL_BG)

draw.text((570, row2_y + 30), "Why the flow works (strategy)", font=f_body_bold, fill=DARK_BODY)
draw.text((570, row2_y + 55), "Flow map (every step diagrammed)", font=f_body, fill=DARK_BODY)
draw.text((570, row2_y + 80), "Step-by-step rebuild instructions", font=f_body, fill=DARK_BODY)
draw.text((570, row2_y + 105), "All message copy (ready to paste)", font=f_body, fill=DARK_BODY)
draw.text((570, row2_y + 130), "Backend checklist (tags, fields)", font=f_body, fill=DARK_BODY)
draw.text((570, row2_y + 155), "Improvement suggestions", font=f_body, fill=DARK_BODY)
draw.text((570, row2_y + 183), "Written so a 12 year old can follow it", font=f_body_bold, fill=TEAL)

# ─── ARROW ───
arrow_right(1025, row2_y + 100, 1090, DARK, 2)

# ─── FLOW LIBRARY ───
sketchy_rect(1100, row2_y, 380, 200, GREEN_BG, GREEN_BORDER, border_width=3)

# Database icon
dbx, dby = 1120, row2_y + 10
draw.ellipse([dbx, dby, dbx+20, dby+8], outline=GREEN, width=2)
draw.line([(dbx, dby+4), (dbx, dby+16)], fill=GREEN, width=2)
draw.line([(dbx+20, dby+4), (dbx+20, dby+16)], fill=GREEN, width=2)
draw.arc([dbx, dby+12, dbx+20, dby+20], start=0, end=180, fill=GREEN, width=2)

draw.text((1150, row2_y + 8), "/flow-library", font=f_section, fill=GREEN)
draw.text((1120, row2_y + 45), "Save every captured flow", font=f_body, fill=DARK_BODY)
draw.text((1120, row2_y + 67), "Search by platform, type, rating", font=f_body, fill=DARK_BODY)
draw.text((1120, row2_y + 89), "Browse and filter your swipe file", font=f_body, fill=DARK_BODY)
draw.text((1120, row2_y + 111), "Rate and tag for easy retrieval", font=f_body, fill=DARK_BODY)
draw.text((1120, row2_y + 136), "Week 1: 5 flows", font=f_body, fill=DARK_BODY)
draw.text((1120, row2_y + 158), "Month 3: 100+ flows", font=f_body_bold, fill=GREEN)

badge(1120, row2_y + 210, "Airtable", GREEN_BG, GREEN, GREEN_BORDER)

# ═══════════════════════════════════════════════════════
# CONNECTING LINE: Library → Row 3 (bent down-left)
# ═══════════════════════════════════════════════════════

cx, cy = 1290, row2_y + 205
draw.line([(cx, cy), (cx, cy + 45)], fill=DARK, width=2)
draw.line([(cx, cy + 45), (250, cy + 45)], fill=DARK, width=2)
draw.line([(250, cy + 45), (250, cy + 75)], fill=DARK, width=2)
draw.polygon([(250, cy + 75), (244, cy + 63), (256, cy + 63)], fill=DARK)

# ═══════════════════════════════════════════════════════
# ROW 3: ADAPT → TEMPLATES → AUDIT → EXPORT
# ═══════════════════════════════════════════════════════

row3_y = row2_y + 285

# ─── FLOW ADAPT ───
sketchy_rect(80, row3_y, 310, 155, ORANGE_BG, ORANGE_BORDER, border_width=3)

# Wand icon
draw.line([(100, row3_y + 25), (112, row3_y + 10)], fill=ORANGE, width=2)
draw.text((108, row3_y + 5), "*", font=font_bold(14), fill=ORANGE)

draw.text((125, row3_y + 8), "/flow-adapt", font=f_section, fill=ORANGE)
draw.text((100, row3_y + 42), "Pick any saved flow", font=f_body, fill=DARK_BODY)
draw.text((100, row3_y + 64), "Rewrite ALL copy for your business", font=f_body, fill=DARK_BODY)
draw.text((100, row3_y + 86), "New keywords, CTAs, tags", font=f_body, fill=DARK_BODY)
draw.text((100, row3_y + 108), "Keep the structure, change content", font=f_body, fill=DARK_BODY)

# ─── ARROW ───
arrow_right(395, row3_y + 77, 445, DARK, 2)

# ─── FLOW TEMPLATES ───
sketchy_rect(455, row3_y, 310, 155, YELLOW_BG, YELLOW_BORDER, border_width=3)

# Template icon
draw.rectangle([475, row3_y + 10, 491, row3_y + 26], outline=YELLOW, width=2)
draw.line([(479, row3_y + 16), (487, row3_y + 16)], fill=YELLOW, width=1)
draw.line([(479, row3_y + 20), (487, row3_y + 20)], fill=YELLOW, width=1)

draw.text((500, row3_y + 8), "/flow-templates", font=f_section, fill=YELLOW)
draw.text((475, row3_y + 42), "8 proven architectures", font=f_body, fill=DARK_BODY)
draw.text((475, row3_y + 64), "Lead magnet, quiz, sales,", font=f_body, fill=DARK_BODY)
draw.text((475, row3_y + 86), "webinar, support, launch...", font=f_body, fill=DARK_BODY)
draw.text((475, row3_y + 108), "Personalized to YOUR business", font=f_body_bold, fill=YELLOW)

# ─── ARROW ───
arrow_right(770, row3_y + 77, 820, DARK, 2)

# ─── FLOW AUDIT ───
sketchy_rect(830, row3_y, 310, 155, RED_BG, RED_BORDER, border_width=3)

# Stethoscope icon
draw.arc([850, row3_y + 8, 870, row3_y + 22], start=180, end=0, fill=RED, width=2)
draw.line([(850, row3_y + 15), (850, row3_y + 25)], fill=RED, width=2)

draw.text((880, row3_y + 8), "/flow-audit", font=f_section, fill=RED)
draw.text((850, row3_y + 42), "10-point diagnostic checklist", font=f_body, fill=DARK_BODY)
draw.text((850, row3_y + 64), "Dead ends, compliance, tags,", font=f_body, fill=DARK_BODY)
draw.text((850, row3_y + 86), "copy quality, re-engagement...", font=f_body, fill=DARK_BODY)
draw.text((850, row3_y + 108), "GREEN / YELLOW / RED score", font=f_body_bold, fill=RED)

# ─── ARROW ───
arrow_right(1145, row3_y + 77, 1195, DARK, 2)

# ─── FLOW EXPORT ───
sketchy_rect(1205, row3_y, 280, 155, PINK_BG, PINK_BORDER, border_width=3)

# Export icon
draw.line([(1225, row3_y + 20), (1225, row3_y + 10)], fill=PINK, width=2)
draw.polygon([(1225, row3_y + 8), (1219, row3_y + 16), (1231, row3_y + 16)], fill=PINK)
draw.line([(1218, row3_y + 24), (1232, row3_y + 24)], fill=PINK, width=2)

draw.text((1240, row3_y + 8), "/flow-export", font=f_section, fill=PINK)
draw.text((1225, row3_y + 42), "Markdown documents", font=f_body, fill=DARK_BODY)
draw.text((1225, row3_y + 64), "PDF-ready output", font=f_body, fill=DARK_BODY)
draw.text((1225, row3_y + 86), "CSV library export", font=f_body, fill=DARK_BODY)
draw.text((1225, row3_y + 108), "Share with team or clients", font=f_body, fill=DARK_BODY)

# ═══════════════════════════════════════════════════════
# THE LOOP (feedback - dashed teal line from audit back to library)
# ═══════════════════════════════════════════════════════

fx, fy = 985, row3_y + 155
fx2 = 1560
fy2 = row2_y + 100  # Back up to library

# Down from audit
dashed_line(fx, fy, fx, fy + 40, TEAL, 3)
# Right
dashed_line(fx, fy + 40, fx2, fy + 40, TEAL, 3)
# Up
dashed_line(fx2, fy + 40, fx2, fy2, TEAL, 3)
# Left back to library
dashed_line(fx2, fy2, 1485, fy2, TEAL, 3)
# Arrow head
draw.polygon([(1485, fy2), (1497, fy2-8), (1497, fy2+8)], fill=TEAL)

# THE LOOP label
sketchy_rect(1530, row3_y + 30, 200, 100, TEAL_BG, TEAL_BORDER, border_width=2, radius=14)
draw.text((1560, row3_y + 40), "Best patterns", font=f_body_bold, fill=TEAL)
draw.text((1560, row3_y + 60), "feed back into", font=f_body, fill=TEAL)
draw.text((1560, row3_y + 78), "the library", font=f_body_bold, fill=TEAL)

# Circular arrow icon
draw.arc([1580, row3_y + 100, 1610, row3_y + 120], start=30, end=330, fill=TEAL, width=2)
draw.polygon([(1607, row3_y + 103), (1615, row3_y + 107), (1608, row3_y + 113)], fill=TEAL)

# ═══════════════════════════════════════════════════════
# PLATFORM BADGES (bottom left)
# ═══════════════════════════════════════════════════════

plat_y = row3_y + 175
draw.text((80, plat_y), "PLATFORMS:", font=f_body_bold, fill=GRAY)
badge(210, plat_y - 2, "ManyChat", PURPLE_BG, PURPLE, PURPLE_BORDER)
badge(315, plat_y - 2, "GoHighLevel", ORANGE_BG, ORANGE, ORANGE_BORDER)
badge(440, plat_y - 2, "n8n", GREEN_BG, GREEN, GREEN_BORDER)
badge(495, plat_y - 2, "Make", BLUE_BG, BLUE, BLUE_BORDER)
badge(560, plat_y - 2, "Zapier", YELLOW_BG, YELLOW, YELLOW_BORDER)

# ═══════════════════════════════════════════════════════
# PAIRS WITH (bottom right)
# ═══════════════════════════════════════════════════════

pairs_y = row3_y + 175
sketchy_rect(1100, pairs_y - 10, 400, 55, WHITE, LIGHT_GRAY, border_width=1, radius=12)
draw.text((1120, pairs_y - 2), "PAIRS WITH:", font=f_body_bold, fill=GRAY)
badge(1240, pairs_y - 2, "Ads Machine", BLUE_BG, BLUE, BLUE_BORDER)
badge(1370, pairs_y - 2, "Agency CC", GREEN_BG, GREEN, GREEN_BORDER)
draw.text((1120, pairs_y + 22), "Ads drive traffic. Flows capture leads. ACC tracks results.", font=f_tiny, fill=GRAY)

# ═══════════════════════════════════════════════════════
# BOTTOM BAR
# ═══════════════════════════════════════════════════════

footer_y = H - 55
sketchy_rect(200, footer_y, W-400, 35, WHITE, LIGHT_GRAY, border_width=1, radius=12)
text_center(200, footer_y + 7, W-400,
    "All skills run from Claude Code terminal  |  Airtable backend  |  Claude multimodal vision  |  No API keys for core features",
    f_small, GRAY)

# ═══════════════════════════════════════════════════════
# SAVE
# ═══════════════════════════════════════════════════════

out = "C:/Users/me/amber-ai/flow-machine/docs/blueprint.png"
img.save(out, "PNG", quality=95)
print(f"Saved to {out}")
print(f"Size: {img.size}")
