from pathlib import Path
from datetime import datetime

from utils.process_folder import process_folder
from excel.writer import write_excel


EXCEL_FILE = "Monitoring Harian Palo Juli.xlsx"


# Nama bulan Indonesia
MONTHS = {
    1: "Januari",
    2: "Februari",
    3: "Maret",
    4: "April",
    5: "Mei",
    6: "Juni",
    7: "Juli",
    8: "Agustus",
    9: "September",
    10: "Oktober",
    11: "November",
    12: "Desember",
}


today = datetime.now()

month_folder = f"{today.month:02d} - {MONTHS[today.month]}"
day_folder = f"{today.day:02d} {MONTHS[today.month]}"

BASE = Path("samples") / "Palo Alto" / month_folder / day_folder

DEVICES = {
    "FW01": BASE / "FW01",
    "FW02": BASE / "FW02",
    "RJ01": BASE / "RJ01",
    "RJ02": BASE / "RJ02",
}

print(f"\nProcessing folder : {BASE}\n")

all_results = {}

for sheet, folder in DEVICES.items():

    print(f"\n========== {sheet} ==========\n")

    if not folder.exists():
        print(f"Folder tidak ditemukan : {folder}")
        continue

    result = process_folder(folder)

    all_results[sheet] = result

    print(result)

write_excel(
    excel_file=EXCEL_FILE,
    all_results=all_results,
)

print("\nSELESAI")