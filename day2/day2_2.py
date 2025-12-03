import os

def load_ranges(path):
    s = open(path, "r").read().strip()
    if not s:
        return []
    parts = [p for p in s.replace("\n", "").split(",") if p]
    ranges = []
    for p in parts:
        a, b = p.split("-")
        ranges.append((int(a), int(b)))
    return ranges

def sum_repeated_double_ids(ranges):
    # ...existing code...
    if not ranges:
        return 0
    max_b = max(b for _, b in ranges)
    max_len = len(str(max_b))
    total = 0
    seen = set()
    # base length l from 1 up to max_len-1
    for l in range(1, max_len):
        base_start = 10 ** (l - 1)
        base_end = 10 ** l - 1
        # repeat count r at least 2
        for r in range(2, max_len // l + 1):
            for base in range(base_start, base_end + 1):
                s = str(base) * r
                if len(s) > max_len:
                    break
                n = int(s)
                if n > max_b:
                    break
                if n in seen:
                    continue
                for a, b in ranges:
                    if a <= n <= b:
                        total += n
                        seen.add(n)
                        break
    return total
    # ...existing code...

if __name__ == "__main__":
    base = os.path.dirname(__file__)
    input_path = os.path.join(base, "input.txt")
    ranges = load_ranges(input_path)
    print(ranges)
    print(sum_repeated_double_ids(ranges))