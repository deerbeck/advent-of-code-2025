from pathlib import Path

INPUT = Path(__file__).with_name("input.txt")

def read_input(path: Path = INPUT):
    with path.open("r") as f:
        return [[int(ch) for ch in line.strip()] for line in f if line.strip()]

def get_number(lines) -> int:
    sum = 0

    for line in lines:
        ten_dig = 0
        left_idx = 0
        for i in range(len(line)-1):
            if line[i] > ten_dig:
                ten_dig = line[i]
                left_idx = i
                if ten_dig == 9:
                    break
        digit_dig = 0
        for i in range(-1, -(len(line) - left_idx), -1):
            if line[i] > digit_dig:
                digit_dig = line[i]
                if digit_dig == 9:
                    break
        sum += ten_dig * 10 + digit_dig

    return sum

            

if __name__ == "__main__":
    lines = read_input()
    # print(f"Read {len(lines)} lines. First line (first 50 digits): {lines[0][:50]}")
    print(get_number(lines))