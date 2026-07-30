from utils.file_loader import load_images

from ocr.paddle import extract_text

from vendors.paloalto.dashboard import parse_dashboard
from vendors.paloalto.disk import parse_disk
from vendors.paloalto.resource import parse_resource
from vendors.paloalto.environment import parse_environment


def process_folder(folder):

    images = load_images(folder)

    result = {}

    print(f"Found {len(images)} image(s)\n")

    for image in images:

        print(f"Processing : {image.name}")

        text = extract_text(str(image))
        lower = text.lower()

        handled = False

        # ==========================
        # Dashboard
        # ==========================
        if (
            "management cpu" in lower
            or "data plane cpu" in lower
            or "session count" in lower
        ):
            print("Type : dashboard")
            result.update(parse_dashboard(text))
            handled = True

        # ==========================
        # Disk
        # ==========================
        if "show system disk-space" in lower:
            print("Type : disk")
            result.update(parse_disk(text))
            handled = True

        # ==========================
        # Environment
        # ==========================
        if "show system environmentals" in lower:
            print("Type : environment")
            result.update(parse_environment(text))
            handled = True

        # ==========================
        # Resource
        # ==========================
        if (
            "show system resources" in lower
            or "show session info" in lower
            or "throughput" in lower
        ):
            print("Type : resource")
            result.update(parse_resource(text))
            handled = True

        if not handled:
            print("Type : unknown")

        print()

    print("\n===== FINAL RESULT =====")
    print(result)

    return result