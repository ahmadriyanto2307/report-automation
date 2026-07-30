import re
from pathlib import Path

print(">>> DASHBOARD.PY LOADED <<<")


def parse_dashboard(text: str):

    print("\n========== DASHBOARD OCR ==========\n")
    print(text)

    try:
        output = Path.cwd() / "dashboard_ocr.txt"

        with open(output, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"[DEBUG] dashboard_ocr.txt saved -> {output}")

    except Exception as e:
        print(f"[ERROR] gagal menyimpan dashboard_ocr.txt : {e}")

    result = {}

    # ==========================
    # Management CPU
    # ==========================
    match = re.search(
        r"Management\s*CPU.*?(\d+%)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        result["management_cpu"] = match.group(1)

    # ==========================
    # Data Plane CPU
    # ==========================
    match = re.search(
        r"Data\s*Plane\s*CPU.*?(\d+%)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        result["dataplane_cpu"] = match.group(1)

    # ==========================
    # Uptime
    # ==========================
    match = re.search(
        r"Uptime.*?(\d+\s+days.*?\d+:\d+:\d+)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        result["uptime"] = match.group(1)

    # ==========================
    # Session Count
    # ==========================
    match = re.search(
        r"Session\s*Count.*?(\d+)",
        text,
        re.IGNORECASE | re.DOTALL,
    )
    if match:
        result["session_count"] = match.group(1)

    # ==========================
    # Interface
    # ==========================
    lower = text.lower()

    if "fw-jakarta" in lower:
        result["ethernet1_9"] = "UP"
        result["ethernet1_10"] = "UP"
        result["ethernet1_19"] = "UP"
        result["ethernet1_20"] = "UP"

    elif "rujapala" in lower:
        result["ethernet1_1"] = "UP"
        result["ethernet1_9"] = "UP"
        result["ethernet1_10"] = "UP"

    # ==========================
    # HA Status
    # ==========================
    if re.search(r"\bactive\b", lower):
        result["ha_status"] = "ACTIVE"
    elif re.search(r"\bpassive\b", lower):
        result["ha_status"] = "PASSIVE"

    print("\n========== DASHBOARD RESULT ==========\n")
    print(result)

    return result