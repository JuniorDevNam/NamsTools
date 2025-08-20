# ...existing code...
#!/usr/bin/env python3
"""
Bulk rename tool
- Duyệt thư mục (tùy chọn đệ quy)
- Đổi tên theo: replace, prefix, suffix, numbering
- Xem trước (dry-run) trước khi thực hiện
- Ghi log (CSV) để undo
"""
from __future__ import annotations
import argparse
import csv
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Tuple

def find_files(root: Path, pattern: str, recursive: bool) -> List[Path]:
    if recursive:
        return sorted(root.rglob(pattern))
    return sorted(root.glob(pattern))

def build_new_name(p: Path, idx: int | None, args: argparse.Namespace) -> Path:
    stem = p.stem
    suffix = p.suffix  # includes leading dot or '' for no ext

    # replace substring in stem
    if args.replace_from:
        stem = stem.replace(args.replace_from, args.replace_to or "")

    # add prefix/suffix around stem
    if args.prefix:
        stem = f"{args.prefix}{stem}"
    if args.suffix:
        stem = f"{stem}{args.suffix}"

    # numbering (insert before extension)
    if idx is not None:
        fmt = "{:0" + str(args.number_width) + "d}" if args.number_width else "{}"
        num = fmt.format(args.number_start + idx * args.number_step)
        if args.number_position == "prefix":
            stem = f"{num}_{stem}"
        else:
            stem = f"{stem}_{num}"

    return p.with_name(stem + suffix)

def rename_files(files: List[Path], args: argparse.Namespace) -> List[Tuple[Path, Path]]:
    changes = []
    for i, f in enumerate(files):
        new = build_new_name(f, i if args.number else None, args)
        # if same name -> skip
        if f.resolve() == new.resolve():
            continue
        changes.append((f, new))
    # perform changes (after preview/confirm)
    if args.preview:
        for old, new in changes:
            print(f"[PREVIEW] {old} -> {new}")
        return changes

    if not args.yes:
        print("Following renames will be performed:")
        for old, new in changes:
            print(f"  {old} -> {new}")
        ans = input("Proceed? [y/N]: ").strip().lower()
        if ans != "y":
            print("Aborted.")
            return []

    # apply renames
    for old, new in changes:
        new.parent.mkdir(parents=True, exist_ok=True)
        old.rename(new)
        print(f"Renamed: {old} -> {new}")

    # log changes for potential undo
    log_path = Path(args.logfile)
    with log_path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        timestamp = datetime.utcnow().isoformat()
        for old, new in changes:
            writer.writerow([timestamp, str(old.resolve()), str(new.resolve())])
    print(f"Logged {len(changes)} changes to {log_path}")
    return changes

def undo_from_log(logfile: Path, last_n: int | None):
    if not logfile.exists():
        print("Log file not found:", logfile)
        return
    # read all entries then revert in reverse order
    with logfile.open("r", encoding="utf-8", newline="") as fh:
        rows = list(csv.reader(fh))
    if not rows:
        print("No entries to undo.")
        return
    to_undo = rows[-(last_n * 1) :] if last_n else rows[:]
    # to undo latest entries in reverse chronological order
    for timestamp, old_path, new_path in reversed(to_undo):
        old = Path(old_path)
        new = Path(new_path)
        if new.exists():
            try:
                new.rename(old)
                print(f"Reverted: {new} -> {old}")
            except Exception as e:
                print(f"Failed to revert {new} -> {old}: {e}")
        else:
            print(f"Target not found, can't revert: {new}")
    # optionally remove undone rows from log: keep older entries
    remaining = rows[: len(rows) - len(to_undo)]
    with logfile.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerows(remaining)
    print(f"Undo complete. Updated log: {logfile}")

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Bulk rename files")
    p.add_argument("root", nargs="?", default=".", help="Root folder to scan")
    p.add_argument("--pattern", "-p", default="*", help="Glob pattern (eg: *.txt)")
    p.add_argument("--recursive", "-r", action="store_true", help="Recurse into subfolders")
    p.add_argument("--replace", "-R", nargs=2, metavar=("FROM", "TO"), help="Replace substring in filename (stem only)")
    p.add_argument("--prefix", help="Add prefix to filename (stem)")
    p.add_argument("--suffix", help="Add suffix to filename (stem)")
    p.add_argument("--number", action="store_true", help="Add sequential numbers")
    p.add_argument("--number-start", type=int, default=1, help="Start number (default 1)")
    p.add_argument("--number-step", type=int, default=1, help="Number step (default 1)")
    p.add_argument("--number-width", type=int, default=0, help="Zero-pad width for numbers (eg 3 => 001)")
    p.add_argument("--number-position", choices=("prefix", "suffix"), default="suffix", help="Where to add number")
    p.add_argument("--preview", action="store_true", help="Show changes but do not perform them")
    p.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")
    p.add_argument("--logfile", default="rename_log.csv", help="CSV logfile for changes")
    p.add_argument("--undo", action="store_true", help="Undo changes using logfile")
    p.add_argument("--undo-last", type=int, default=0, help="Undo last N entries (0 = all)")
    return p.parse_args()

def main():
    args = parse_args()
    root = Path(args.root).expanduser().resolve()
    if args.replace:
        args.replace_from, args.replace_to = args.replace
    else:
        args.replace_from = None
        args.replace_to = None

    if args.undo:
        logfile = Path(args.logfile)
        last_n = args.undo_last if args.undo_last > 0 else None
        undo_from_log(logfile, last_n)
        return

    files = find_files(root, args.pattern, args.recursive)
    if not files:
        print("No files found.")
        return

    rename_files(files, args)

if __name__ == "__main__":
    main()
# ...existing code...