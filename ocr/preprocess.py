import cv2
import numpy as np


def preprocess(image):

    if image is None:
        return image

    # Resize supaya OCR lebih jelas
    image = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC,
    )

    # Grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Contrast
    gray = cv2.equalizeHist(gray)

    # Sharpen
    kernel = np.array([
        [-1, -1, -1],
        [-1,  9, -1],
        [-1, -1, -1]
    ])

    gray = cv2.filter2D(gray, -1, kernel)

    # Binary
    _, gray = cv2.threshold(
        gray,
        170,
        255,
        cv2.THRESH_BINARY,
    )

    return gray