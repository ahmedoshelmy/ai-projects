"""
Adds slides to RAG.pptx using images from demos/pics,
matching the 'Side bar Midnight/Dell Blue' Dell design.
"""
import os
import glob
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from PIL import Image

# Config
PPTX_PATH = r'C:\Users\ahelmy\Grind\RAG.pptx'
PICS_DIR = r'C:\code\Personal\ai-projects\demos\pics'
OUTPUT_PATH = r'C:\Users\ahelmy\Grind\RAG_updated.pptx'

# Get sorted images by filename (filenames contain timestamps)
images = sorted(
    glob.glob(os.path.join(PICS_DIR, '*.jpeg')) +
    glob.glob(os.path.join(PICS_DIR, '*.jpg')) +
    glob.glob(os.path.join(PICS_DIR, '*.png'))
)
print(f"Found {len(images)} images")

prs = Presentation(PPTX_PATH)
slide_w = prs.slide_width   # 13.33" = 12192000 EMU
slide_h = prs.slide_height  # 7.50"  = 6858000  EMU

# Find the "Side bar Midnight/Dell Blue" layout
sidebar_layout = None
for layout in prs.slide_master.slide_layouts:
    if layout.name == 'Side bar Midnight/Dell Blue':
        sidebar_layout = layout
        break

if sidebar_layout is None:
    raise RuntimeError("Layout 'Side bar Midnight/Dell Blue' not found")

# Content area dimensions from the layout
CONTENT_LEFT   = Inches(3.79)
CONTENT_TOP    = Inches(0.44)
CONTENT_WIDTH  = Inches(9.17)
CONTENT_HEIGHT = Inches(6.38)

def fit_image(img_path, max_w, max_h):
    """Return (width, height, left, top) to fit image centred in the content box."""
    with Image.open(img_path) as im:
        img_w, img_h = im.size
    ratio = min(max_w / img_w, max_h / img_h)
    new_w = int(img_w * ratio)
    new_h = int(img_h * ratio)
    offset_x = (max_w - new_w) // 2
    offset_y = (max_h - new_h) // 2
    return new_w, new_h, offset_x, offset_y

for i, img_path in enumerate(images):
    filename = os.path.basename(img_path)
    # Extract date/time portion, e.g. "2026-07-02 18:27" for title
    parts = filename.replace('Udemy ScreenShot ', '').replace('.jpeg', '').replace('.jpg', '').replace('.png', '')
    # parts looks like "2026-07-02 18-27-47"
    date_part = parts[:10]  # "2026-07-02"
    time_part = parts[11:16].replace('-', ':')  # "18:27"
    slide_title = f"{date_part}\n{time_part}"

    slide = prs.slides.add_slide(sidebar_layout)

    # Set title text
    title_ph = slide.placeholders[0]
    title_ph.text = slide_title
    for para in title_ph.text_frame.paragraphs:
        for run in para.runs:
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
            run.font.size = Pt(18)
            run.font.bold = True

    # Remove the content placeholder so we can place the image freely
    content_ph = None
    for ph in slide.placeholders:
        if ph.placeholder_format.idx == 1:
            content_ph = ph
            break
    if content_ph is not None:
        sp = content_ph._element
        sp.getparent().remove(sp)

    # Fit image within the content area
    max_w_px = CONTENT_WIDTH
    max_h_px = CONTENT_HEIGHT

    with Image.open(img_path) as im:
        img_w_px, img_h_px = im.size

    # Calculate scaled dimensions maintaining aspect ratio
    max_w_emu = CONTENT_WIDTH
    max_h_emu = CONTENT_HEIGHT
    img_ratio = img_w_px / img_h_px
    box_ratio = max_w_emu / max_h_emu

    if img_ratio > box_ratio:
        # Image is wider than box
        scaled_w = max_w_emu
        scaled_h = Emu(int(max_w_emu * img_h_px / img_w_px))
    else:
        # Image is taller than box
        scaled_h = max_h_emu
        scaled_w = Emu(int(max_h_emu * img_w_px / img_h_px))

    left_offset = CONTENT_LEFT + (max_w_emu - scaled_w) // 2
    top_offset  = CONTENT_TOP  + (max_h_emu - scaled_h) // 2

    slide.shapes.add_picture(img_path, left_offset, top_offset, scaled_w, scaled_h)

    print(f"  [{i+1:02d}/{len(images)}] Added: {filename}")

prs.save(OUTPUT_PATH)
print(f"\nSaved to: {OUTPUT_PATH}")
print(f"Total slides: {len(list(prs.slides))}")
