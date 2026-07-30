from paddleocr import PaddleOCR
import cv2

from ocr.preprocess import preprocess

ocr = PaddleOCR(
    use_angle_cls=True,
    lang="en",
    use_gpu=False,
    det_db_thresh=0.2,
    det_db_box_thresh=0.4,
    drop_score=0.3,
)


def normalize(text: str):

    replace = {
        "1t": "1%",
        "4t": "4%",
        "6t": "6%",
        "8t": "8%",
        "23t": "23%",
        "24t": "24%",
        "27t": "27%",
        "28t": "28%",
        "29t": "29%",
        "36t": "36%",
        "37t": "37%",
        "39t": "39%",
        "41t": "41%",
        "68t": "68%",
        "69t": "69%",
        "Uset": "Use%",
        "Use¥": "Use%",
    }

    for old, new in replace.items():
        text = text.replace(old, new)

    return text


def extract_text(image_path):

    image = cv2.imread(image_path)

    image = preprocess(image)

    result = ocr.ocr(image, cls=True)

    lines = []

    for page in result:

        if page is None:
            continue

        for item in page:
            lines.append(item[1][0])

    text = "\n".join(lines)

    return normalize(text)