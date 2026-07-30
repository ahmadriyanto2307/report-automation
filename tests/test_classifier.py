from ocr.paddle import extract_text
from classifier.classifier import classify

text = extract_text(
    r"samples/Palo Alto/07 - Juli/13 Juli/FW01/Cuplikan layar 2026-07-13 131244.png"
)

print(classify(text))