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
    Processes the numbers provided by the input in such a case, that the largest
    two digit integer of a given integer string will be extracted and summed up
    accross all integerstring.
    :param lines: List of lists of integers representing the input lines.
    :return: The computed sum as an integer.
    :rtype: int
    """
    result = 0

    for line in lines:
        ten_dig = 0
        left_idx = 0
        # last digit excluded because last possibility to form 2 digit number
        # logic improbed in day3_2
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
        result += ten_dig * 10 + digit_dig

    return result


if __name__ == "__main__":
    lines = read_input()
    # print(f"Read {len(lines)} lines. First line (first 50 digits): {lines[0][:50]}")
    print(get_number(lines))
