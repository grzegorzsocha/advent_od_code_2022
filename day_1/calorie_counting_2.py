
file_name = "input.txt"


def read_from_file(path):
    try:
        with open(path, 'r') as file_handle:
            result = get_top_three_calories(file_handle)
    except FileNotFoundError:
        print(f'File {path} not found.')
    return result


def get_top_three_calories(file_handle):
    calories = []
    current = 0
    for line in file_handle:
        if line == '\n':
            calories.append(current)
            current = 0
        else:
            current += int(line.rstrip())
    if current != 0:
        calories.append(current)
    calories.sort()
    return calories[-1] + calories[-2] + calories[-3]


if __name__ == "__main__":
    print(read_from_file(file_name))
