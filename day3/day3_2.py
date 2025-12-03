from pathlib import Path

INPUT = Path(__file__).with_name("input.txt")
NUM_DIGITS = 12


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
    Processes the input lines to compute a specific number based on digit selection rules.
    For each line, it selects 12 digits based on the highest digit found in specific segments
    of the line, ensuring that the selected digits are in increasing order of their positions.
    The selected digits are then concatenated to form a number, which is summed across all lines.
    :param lines: List of lists of integers representing the input lines.
    :return: The computed sum as an integer.
    :rtype: int
    """
    result = 0
    for line in lines:
        digits = []
        left_idx = 0
        for j in range(NUM_DIGITS):
            current_digit = 0
            for i in range(left_idx, (len(line) - (NUM_DIGITS - 1 - j))):
                if line[i] > current_digit:
                    current_digit = line[i]
                    left_idx = i + 1
                    if current_digit == 9:
                        break
            digits.append(current_digit)

        result += int("".join([str(current_digit)
                      for current_digit in digits]))

    return result


if __name__ == "__main__":
    lines = read_input()
    # print(f"Read {len(lines)} lines. First line (first 50 digits): {lines[0][:50]}")
    print(get_number(lines))
