from pathlib import Path
from typing import List, Tuple


def parse_input(path: Path | str) -> List[Tuple[str, int]]:
    """Read the input file and return a sorted list of tuples (dir, int).

    Each non-empty line is expected to be like 'L10' or 'R42'. The returned
    list is sorted by direction (string) then by the integer value.
    """
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    items: List[Tuple[str, int]] = []
    for ln in lines:
        if len(ln) < 2:
            continue
        dir_char = ln[0]
        try:
            val = int(ln[1:])
        except ValueError:
            # skip malformed lines
            continue
        items.append((dir_char, val))

    return items

def find_key(items: List[Tuple[str, int]]) -> int:
    start_num = 50
    key = 0

    for dir_char, val in items:
        if dir_char == 'L':
            start_num -= val
        elif dir_char == 'R':
            start_num += val
        # Ensure the number stays within 0-99 range
        start_num %= 100
        if start_num == 0:
            key += 1

    return key


if __name__ == "__main__":
    input_path = Path(__file__).parent / "input.txt"
    parsed = parse_input(input_path)
    # Print as a Python list of tuples
    print(parsed)
    key = find_key(parsed)
    print(f"The final key is: {key}")
