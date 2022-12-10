
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


def get_signal_strength_sum(inputs: list) -> str:
    output, x, i, line = "", 1, 0, 0
    for input in inputs:
        if input[0] == "addx":
            output += '#' if i in [x + 40 * line + 1, x + 40 * line - 1, x + 40 * line] else '.'
            i += 1
            if i % 40 == 0:
                output += '\n'
                line += 1
            output += '#' if i in [x + 40 * line + 1, x + 40 * line - 1, x + 40 * line] else '.'
            x += int(input[1])
            i += 1
        else:
            output += '#' if i in [x + 40 * line + 1, x + 40 * line - 1, x + 40 * line] else '.'
            i += 1
        if i % 40 == 0:
            output += '\n'
            line += 1
    return output


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_signal_strength_sum(input))
