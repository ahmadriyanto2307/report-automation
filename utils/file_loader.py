from pathlib import Path


def load_images(folder):

    exts = (".png", ".jpg", ".jpeg")

    images = []

    for file in Path(folder).iterdir():

        if file.suffix.lower() in exts:
            images.append(file)

    return sorted(images)