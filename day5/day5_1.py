from pathlib import Path
import re

def read_input(path: Path | str | None = None):
    p = Path(path) if path else Path(__file__).parent / "input.txt"
    text = p.read_text()
    # split on the first blank line (handles CRLF and spaces)
    parts = re.split(r'\r?\n\s*\r?\n', text.strip(), maxsplit=1)
    left = parts[0].splitlines() if parts else []
    right = parts[1].splitlines() if len(parts) > 1 else []

    ranges: list[list[int]] = []
    for line in left:
        line = line.strip()
        if not line:
            continue
        a, b = line.split("-", 1)
        ranges.append([int(a), int(b)])

    numbers = [int(x) for x in (l.strip() for l in right) if x]

    return ranges, numbers

def get_fresh_ingredients(ranges: list[list[int]], numbers: list[int]) -> int:
    # merge overlapping/adjacent ranges first for efficient membership tests
    if not ranges:
        return 0

    sorted_ranges = sorted((a, b) for a, b in ranges)
    merged: list[list[int]] = []
    for a, b in sorted_ranges:
        if not merged or a > merged[-1][1] + 1:
            merged.append([a, b])
        else:
            merged[-1][1] = max(merged[-1][1], b)

    # binary search per number against merged ranges
    import bisect
    starts = [s for s, _ in merged]
    ends = [e for _, e in merged]

    count = 0
    for n in numbers:
        i = bisect.bisect_right(starts, n) - 1
        if i >= 0 and ends[i] >= n:
            count += 1

    return count

if __name__ == "__main__":
    ranges, numbers = read_input()
    # print("ranges =", ranges)
    # print("numbers =", numbers)
    result = get_fresh_ingredients(ranges, numbers)
    print("Number of fresh ingredients:", result)