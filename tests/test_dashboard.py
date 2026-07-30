from ocr.paddle import extract_text
from vendors.paloalto.dashboard import parse_dashboard

text = extract_text(
    "samples/NAMA_SCREENSHOT_KAMU.png"
)

result = parse_dashboard(text)

print(result)