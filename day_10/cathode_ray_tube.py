
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append(line.rstrip().split())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_signal_strength_sum(inputs: list) -> int:
    sum, x, i = 0, 1, 1
    for input in inputs:
        if input[0] == "addx":
            i += 1
            sum += i * x if (i + 20) % 40 == 0 else 0
            i += 1
            x += int(input[1])
        else:
            i += 1
        sum += i * x if (i + 20) % 40 == 0 else 0
    return sum


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_signal_strength_sum(input))
