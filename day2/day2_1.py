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
    if not ranges:
        return 0
    max_b = max(b for _, b in ranges)
    max_len = len(str(max_b))
    total = 0
    # half length k from 1 up to floor(max_len/2)
    for k in range(1, max_len // 2 + 1):
        start = 10 ** (k - 1)
        end = 10 ** k - 1
        for h in range(start, end + 1):
            n = int(str(h) + str(h))
            # skip numbers longer than max_b digits (safety)
            if n > max_b:
                break
            for a, b in ranges:
                if a <= n <= b:
                    total += n
                    break
    return total

if __name__ == "__main__":
    base = os.path.dirname(__file__)
    input_path = os.path.join(base, "input.txt")
    ranges = load_ranges(input_path)
    print(ranges)
    print(sum_repeated_double_ids(ranges))