from pathlib import Path

INPUT = Path(__file__).with_name("input.txt")


def read_input(path: Path = INPUT):
    with path.open("r") as f:
        return [[int(ch) for ch in line.strip()] for line in f if line.strip()]


def get_number(lines) -> int:
    sum = 0

    for line in lines:
        digits = []
        left_idx = 0
        for j in range(12):
            dig = 0
            test = list(range(left_idx, (len(line)-(11 - j))))
            for i in range(left_idx, (len(line)-(11 - j))):
                if line[i] > dig:
                    dig=line[i]
                    left_idx=i + 1
                    if dig == 9:
                        break
            digits.append(dig)

        sum += int("".join([str(dig) for dig in digits]))

    return sum



if __name__ == "__main__":
    lines=read_input()
    # print(f"Read {len(lines)} lines. First line (first 50 digits): {lines[0][:50]}")
    print(get_number(lines))
