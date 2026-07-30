import re


def parse_resource(text: str):

    result = {}

    print("\n========== RESOURCE OCR ==========\n")
    print(text)

    with open("resource_ocr.txt", "w", encoding="utf-8") as f:
        f.write(text)

    # ==========================================
    # CPU
    # ==========================================
    match = re.search(
        r"Cpu\(s\)\s*:\s*([0-9.]+)",
        text,
        re.IGNORECASE,
    )

    if match:
        result["analysis_cpu"] = match.group(1) + "%"

    # ==========================================
    # Throughput
    # ==========================================
    match = re.search(
        r"Throughput\s*:?\s*([0-9]+)\s*kbps",
        text,
        re.IGNORECASE,
    )

    if match:
        result["uplink"] = match.group(1) + " kbps"

    # ==========================================
    # MEMORY
    # ==========================================
    mem = re.search(
        r"MiB\s+Mem\s*:?\s*([0-9.]+).*?([0-9.]+)\s+free.*?([0-9.]+)\s+used.*?([0-9.]+)\s+buff/cache",
        text,
        re.IGNORECASE | re.DOTALL,
    )

    avail = re.search(
        r"([0-9.]+)\s+avai[l1i]\s+Mem",
        text,
        re.IGNORECASE,
    )

    if mem and avail:

        total_mem = float(mem.group(1))
        free_mem = float(mem.group(2))
        used_mem = float(mem.group(3))
        avail_mem = float(avail.group(1))

        if total_mem > 0:

            result["total_memory"] = str(total_mem)
            result["free_memory"] = str(free_mem)
            result["available_memory"] = str(avail_mem)
            result["used_memory"] = f"{round((used_mem / total_mem) * 100, 2)}%"

    print("\n========== RESOURCE RESULT ==========\n")
    print(result)

    return result