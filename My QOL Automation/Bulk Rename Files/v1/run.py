#!/usr/bin/env python3
"""
Đổi tên file: chuyển tên tiếng Việt có dấu -> không dấu, giữ nguyên phần mở rộng.
Sử dụng:
  python run.py "C:\path\to\folder" -p "*.*" [-r] [--preview] [-y]
"""
from __future__ import annotations
import argparse
import unicodedata
from pathlib import Path
from typing import Iterable

VI_D_MAP = {
    "đ": "d", "Đ": "D"
}

def remove_vietnamese_accents(s: str) -> str:
    # chuẩn hóa Unicode, loại bỏ dấu kết hợp, xử lý đ/Đ
    s = s.replace("đ", "d").replace("Đ", "D")  # nhanh trước
    nfkd = unicodedata.normalize("NFKD", s)
    no_acc = "".join(ch for ch in nfkd if not unicodedata.combining(ch))
    return no_acc

def find_files(root: Path, pattern: str, recursive: bool) -> Iterable[Path]:
    if recursive:
        candidates = root.rglob(pattern)
    else:
        candidates = root.glob(pattern)
    # chỉ trả về file (không bao gồm thư mục)
    return sorted(p for p in candidates if p.is_file())

def build_new_path(p: Path) -> Path:
    stem = p.stem  # tên không kèm đuôi
    suffix = p.suffix  # .ext or ''
    new_stem = remove_vietnamese_accents(stem)
    return p.with_name(new_stem + suffix)

def rename_in_folder(root: Path, pattern: str, recursive: bool, preview: bool, yes: bool):
    files = list(find_files(root, pattern, recursive))
    if not files:
        print("Không tìm thấy file.")
        return
    changes = []
    for f in files:
        new = build_new_path(f)
        if f.resolve() == new.resolve():
            continue
        changes.append((f, new))

    if not changes:
        print("Không có tên nào cần thay đổi.")
        return

    if preview:
        for old, new in changes:
            print(f"[PREVIEW] {old} -> {new}")
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
        if new.exists():
            print(f"SKIP (đã tồn tại): {new}")
            continue
        try:
            old.rename(new)
            print(f"Renamed: {old.name} -> {new.name}")
        except Exception as e:
            print(f"Failed: {old} -> {new}: {e}")

def parse_args():
    p = argparse.ArgumentParser(description="Bulk remove Vietnamese accents from filenames")
    p.add_argument("root", nargs="?", default=".", help="Folder root")
    p.add_argument("-p", "--pattern", default="*.*", help="Glob pattern, ví dụ '*.txt' or '*.*'")
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