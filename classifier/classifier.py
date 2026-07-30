def classify(text: str):

    text = text.lower()

    # Dashboard GUI
    if "management cpu" in text:
        return "dashboard"

    # CLI Disk
    if "show system disk-space" in text:
        return "disk"

    # CLI Resource
    if "show system resources" in text:
        return "resource"

    # CLI Environment
    if "show system environmentals" in text:
        return "environment"

    return "unknown"