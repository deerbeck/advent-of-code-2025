from pathlib import Path
import numpy as np

def read_input(path: Path | str | None = None):
    p = Path(path) if path else Path(__file__).parent / "input.txt"
    text = p.read_text()
    lines = [line.strip() for line in text.strip().splitlines() if line.strip()]
    return lines

def scan_lines(lines):
    list_lines = []
    for line in lines:
        list_lines.append([x for x in line.strip().split(" ") if x != ""])
    return list_lines

def do_math(lines):
    mul_lines = np.empty((len(lines)-1,), dtype=object)
    sum_lines = np.empty((len(lines)-1,), dtype=object)
    for i in range(len(lines)-1):
        mul_lines[i] = np.array([int(lines[i][j]) for j in range(len(lines[i])) if lines[-1][j] == "*"])
        sum_lines[i] = np.array([int(lines[i][j]) for j in range(len(lines[i])) if lines[-1][j] == "+"])
    
    result_mul = np.prod(mul_lines, axis=0)
    result_sum = np.sum(sum_lines, axis=0)
    return np.sum(result_mul) + np.sum(result_sum)

        
        
        


if __name__ == "__main__":
    lines = read_input()
    scanned_lines = scan_lines(lines)
    print(do_math(scanned_lines))
    print(int("02"))