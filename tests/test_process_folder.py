from ocr.paddle import extract_text
from vendors.paloalto.disk import parse_disk

text = extract_text(
    r"samples/Palo Alto/07 - Juli/14 Juli/FW01/Cuplikan layar 2026-07-13 131507.png"
)

print(text)

print("\n========== DISK PARSER ==========\n")

print(parse_disk(text))