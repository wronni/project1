from PIL import Image
from pillow_heif import register_heif_opener

# Register HEIF opener with Pillow
register_heif_opener()

# Open and convert the HEIC image
img = Image.open("IMG_3772.HEIC")

# Convert to RGB if necessary (HEIC might be in different color mode)
if img.mode != "RGB":
    img = img.convert("RGB")

# Save as JPEG
img.save("image.jpg", "JPEG", quality=95)

print("Image converted successfully to image.jpg")
