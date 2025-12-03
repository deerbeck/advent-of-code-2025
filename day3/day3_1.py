from pathlib import Path

INPUT = Path(__file__).with_name("input.txt")


def read_input(path: Path = INPUT):
    """
    Reads the input file and returns a list of lists of integers.
    Each line in the file is converted to a list of its digit characters as integers.
    :param path: Path to the input file.
    :return: List of lists of integers.
    """
    with path.open("r") as f:
        return [[int(ch) for ch in line.strip()] for line in f if line.strip()]


def get_number(lines) -> int:
    """
    Processes the input lines to find the largest two-digit number from each line
    by selecting the maximum digit for the tens place and the maximum digit for the ones place,
    then sums these numbers across all lines.
    :param lines: List of lists of integers representing the input lines.
    :return: The computed sum as an integer.
    :rtype: int
    """
    result = 0

    for line in lines:
        second_digit = 0
        left_idx = 0
        # last digit excluded because last possibility to form 2 digit number
        # logic improbed in day3_2
        for i in range(len(line)-1):
            if line[i] > second_digit:
                second_digit = line[i]
                left_idx = i
                if second_digit == 9:
                    break
        first_digit = 0
        for i in range(-1, -(len(line) - left_idx), -1):
            if line[i] > first_digit:
                first_digit = line[i]
                if first_digit == 9:
                    break
        result += second_digit * 10 + first_digit

    return result


if __name__ == "__main__":
    lines = read_input()
    # print(f"Read {len(lines)} lines. First line (first 50 digits): {lines[0][:50]}")
    print(get_number(lines))
