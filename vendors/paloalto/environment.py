import re


def has_false(section, text):

    return re.search(
        rf"{section}.*?False",
        text,
        re.IGNORECASE | re.DOTALL,
    )


def parse_environment(text: str):

    result = {}

    # Thermal / Therma1
    if has_false(r"Therma[l1]", text):
        result["thermal"] = "FALSE"

    # Fan Tray
    if has_false(r"Fan\s*Tray", text):
        result["fan_tray"] = "FALSE"

    # Fans
    if has_false(r"Fans", text):
        result["fans"] = "FALSE"

    # Power
    if (
        has_false(r"Power", text)
        or has_false(r"-+\s*Power\s*-+", text)
    ):
        result["power"] = "FALSE"

    # Power Supplies
    if (
        has_false(r"Power\s*Supplies", text)
        or has_false(r"Power.*?Supplies", text)
    ):
        result["power_supplies"] = "FALSE"

    return result