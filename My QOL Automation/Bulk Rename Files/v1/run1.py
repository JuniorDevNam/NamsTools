#!/usr/bin/env python3
"""
Tool: Tự động duyệt file và xóa cụm từ "Ho chieu" (Hộ chiếu) trong tên file.
- Chạy sau khi đã chuyển tên sang không dấu.
- Hỗ trợ các biến thể: "Ho chieu", "Ho_chieu", "Ho-chieu", "Ho.chieu" (không phân biệt hoa thường).
- Có chế độ preview (--preview), đệ quy (-r) và xác nhận (-y).
"""
from __future__ import annotations
import argparse
import re
from pathlib import Path
from typing import Iterable

PAT = re.compile(r"(?i)\bho[._\-\s]?chieu\b")  # bắt các biến thể phổ biến, ignore case
SEP_CLEAN = re.compile(r"[._\-\s]{2,}")        # dồn nhiều phân cách thành 1 khoảng trắng

def find_files(root: Path, pattern: str, recursive: bool) -> Iterable[Path]:
    candidates = root.rglob(pattern) if recursive else root.glob(pattern)
    return sorted(p for p in candidates if p.is_file())

def clean_stem(stem: str) -> str:
    # xóa cụm từ, dọn phần phân cách thừa, trim
    out = PAT.sub("", stem)
    out = SEP_CLEAN.sub(" ", out)   # nhiều phân cách -> 1 space
    out = out.strip(" .-_ ")        # loại bỏ phân cách ở đầu/cuối
    out = out.strip()
    if out == "":
        out = "untitled"
    return out

def unique_target(path: Path, new_stem: str) -> Path:
    suffix = path.suffix
    parent = path.parent
    candidate = parent / (new_stem + suffix)
    if not candidate.exists() or candidate.resolve() == path.resolve():
        return candidate
    # thêm hậu tố tăng dần để tránh ghi đè
    i = 1
    while True:
        candidate = parent / (f"{new_stem} ({i})" + suffix)
        if not candidate.exists():
            return candidate
        i += 1

def rename_in_folder(root: Path, pattern: str, recursive: bool, preview: bool, yes: bool):
    files = list(find_files(root, pattern, recursive))
    if not files:
        print("Không tìm thấy file.")
        return
    changes = []
    for f in files:
        stem = f.stem
        new_stem = clean_stem(stem)
        new_path = unique_target(f, new_stem)
        if f.resolve() == new_path.resolve():
            continue
        changes.append((f, new_path))

    if not changes:
        print("Không có tên nào cần thay đổi.")
        return

    if preview:
        for old, new in changes:
            print(f"[PREVIEW] {old.name} -> {new.name}")
        return

    if not yes:
        print("Những thay đổi sẽ thực hiện:")
        for old, new in changes:
            print(f"  {old.name} -> {new.name}")
        ans = input("Tiếp tục? [y/N]: ").strip().lower()
        if ans != "y":
            print("Hủy.")
            return

    for old, new in changes:
        try:
            old.rename(new)
            print(f"Renamed: {old.name} -> {new.name}")
        except Exception as e:
            print(f"Failed: {old} -> {new}: {e}")

def parse_args():
    p = argparse.ArgumentParser(description='Remove "Ho chieu" from filenames')
    p.add_argument("root", nargs="?", default=".", help="Folder root")
    p.add_argument("-p", "--pattern", default="*.*", help="Glob pattern, ví dụ '*.pdf' or '*.*'")
    p.add_argument("-r", "--recursive", action="store_true", help="Duyệt thư mục con")
    p.add_argument("--preview", action="store_true", help="Chỉ hiển thị (không thực hiện)")
    p.add_argument("-y", "--yes", action="store_true", help="Không hỏi xác nhận")
    return p.parse_args()

def main():
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    rename_in_folder(root, args.pattern, args.recursive, args.preview, args.yes)

if __name__ == "__main__":
    main()