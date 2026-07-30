from utils.file_loader import load_images
from ocr.paddle import extract_text

images = load_images(
    "samples/Palo Alto/07 - Juli/06 Juli/FW01"
)

for image in images:
    print("=" * 60)
    print(image.name)
    print("=" * 60)

    text = extract_text(str(image))

    print(text)