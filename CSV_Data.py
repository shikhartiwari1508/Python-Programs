# CSV Data Cleaner and Summarizer

import csv
import statistics
import sys
from pathlib import Path


def clean_rows(path: str) -> list[dict]:
    """Read a CSV, strip whitespace, drop empty and duplicate rows."""
    seen, rows = set(), []
    with Path(path).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            row = {k.strip(): (v or "").strip() for k, v in row.items()}
            key = tuple(row.values())
            if any(row.values()) and key not in seen:
                seen.add(key)
                rows.append(row)
    return rows


def summarize(rows: list[dict], column: str) -> dict:
    values = []
    for r in rows:
        try:
            values.append(float(r[column]))
        except (ValueError, KeyError):
            continue
    if not values:
        return {}
    return {"count": len(values), "mean": statistics.mean(values),
            "median": statistics.median(values), "min": min(values), "max": max(values)}


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("Usage: python csv_clean.py <file.csv> <numeric_column>")
    data = clean_rows(sys.argv[1])
    print(f"Clean rows: {len(data)}")
    for stat, value in summarize(data, sys.argv[2]).items():
        print(f"{stat:<8} {value:.2f}" if stat != "count" else f"{stat:<8} {value}")