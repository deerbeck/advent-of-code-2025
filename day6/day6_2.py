from pathlib import Path
import numpy as np


def read_input(path: Path | str | None = None):
    p = Path(path) if path else Path(__file__).parent / "input.txt"
    lines = p.read_text().splitlines()
    return lines

def scan_lines(lines):
    # lines may be a path result from read_input
    if isinstance(lines, (Path, str)):
        lines = read_input(lines)

    # operator row is the last line
    grid = [ln.rstrip("\n") for ln in lines]
    maxlen = max(len(ln) for ln in grid)
    grid = [ln.ljust(maxlen, " ") for ln in grid]

    op_row = grid[-1]
    num_rows = grid[:-1]

    col = maxlen - 1
    problems = []  # list of (numbers_list, operator_char)

    while col >= 0:
        # skip separator columns (all spaces in numeric rows)
        if all(r[col] == " " for r in num_rows):
            col -= 1
            continue

        # collect contiguous non-blank columns for one problem (right-to-left)
        group_cols = []
        while col >= 0 and not all(r[col] == " " for r in num_rows):
            group_cols.append(col)
            col -= 1

        # group_cols is right-to-left order; for each column build the number by reading top->bottom
        numbers = []
        for c in group_cols:
            digits = "".join(ch for ch in (r[c] for r in num_rows) if ch != " ")
            if digits:
                numbers.append(int(digits))

        # find the operator for this problem within the group's columns (prefer rightmost)
        operator = None
        for c in group_cols:
            if op_row[c] in ("+", "*"):
                operator = op_row[c]
                break
        if operator is None:
            raise ValueError("Operator not found for problem columns: %s" % group_cols)

        problems.append((numbers, operator))

    # problems were collected from rightmost problem to leftmost; order doesn't matter for sum,
    # but keep it as-is (right-to-left).
    return problems

def do_math(problems):
    total = 0
    for numbers, op in problems:
        if op == "+":
            total += sum(numbers)
        elif op == "*":
            prod = 1
            for n in numbers:
                prod *= n
            total += prod
        else:
            raise ValueError("Unknown operator: %r" % op)
    return total

if __name__ == "__main__":
    lines = read_input()
    problems = scan_lines(lines)
    print(do_math(problems))