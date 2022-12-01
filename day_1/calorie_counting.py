
file_name = "input.txt"


def read_from_file(path):
    try:
        with open(path, 'r') as file_handle:
            result = get_max_calories(file_handle)
    except FileNotFoundError:
        print(f'File {path} not found.')
    return result


def get_max_calories(file_handle):
    max = 0
    current = 0
    for line in file_handle:
        if line == '\n':
            if current > max:
                max = current
            current = 0
        else:
            current += int(line.rstrip())
    if current > max:
        max = current
    return max


if __name__ == "__main__":
    print(read_from_file(file_name))
