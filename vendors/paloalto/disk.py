import re


PATTERNS = {
    "dev_md3": r"/dev/md3[\s\S]{0,120}?(\d+)%",
    "none": r"none[\s\S]{0,80}?(\d+)%",
    "dev_md5": r"/dev/md5[\s\S]{0,120}?(\d+)%",
    "dev_md6": r"/dev/md6[\s\S]{0,120}?(\d+)%",
    "tmpfs_dev_shm": r"tmpfs[\s\S]{0,120}?/dev/shm",
    "dev_md8": r"/dev/md8[\s\S]{0,120}?(\d+)%",
    "tmpfs_run_dpdk": r"tmpfs[\s\S]{0,120}?/run/dpdk",
    "cgroup_root": r"cgroup_root[\s\S]{0,80}?(\d+)%",
    "tmpfs_ssl_private": r"tmpfs[\s\S]{0,120}?ssl/private",
}


def parse_disk(text: str):

    with open("disk_ocr.txt", "w", encoding="utf-8") as f:
        f.write(text)

    text = (
        text.replace("1t", "1%")
            .replace("4t", "4%")
            .replace("6t", "6%")
            .replace("8t", "8%")
            .replace("dnobo/ 0", "0%")
    )

    result = {}

    # md3
    m = re.search(PATTERNS["dev_md3"], text, re.I)
    if m:
        result["dev_md3"] = m.group(1) + "%"

    # none
    m = re.search(PATTERNS["none"], text, re.I)
    if m:
        result["none"] = m.group(1) + "%"

    # md5
    m = re.search(PATTERNS["dev_md5"], text, re.I)
    if m:
        result["dev_md5"] = m.group(1) + "%"

    # md6
    m = re.search(PATTERNS["dev_md6"], text, re.I)
    if m:
        result["dev_md6"] = m.group(1) + "%"

    # /dev/shm
    m = re.search(r"(\d+)%\s*/dev/shm", text, re.I)
    if m:
        result["tmpfs_dev_shm"] = m.group(1) + "%"

    # md8
    m = re.search(PATTERNS["dev_md8"], text, re.I)
    if m:
        result["dev_md8"] = m.group(1) + "%"

    # run/dpdk
    m = re.search(r"(\d+)%\s*/run/dpdk", text, re.I)
    if m:
        result["tmpfs_run_dpdk"] = m.group(1) + "%"

    # cgroup_root
    m = re.search(PATTERNS["cgroup_root"], text, re.I)
    if m:
        result["cgroup_root"] = m.group(1) + "%"
    else:
        result["cgroup_root"] = "0%"

    # ssl/private
    m = re.search(r"(\d+)%\s*/opt/pancfg/mgmt/ssl/private", text, re.I)
    if m:
        result["tmpfs_ssl_private"] = m.group(1) + "%"

    print("\n===== DISK RESULT =====")
    print(result)

    return result