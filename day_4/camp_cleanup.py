
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        with open(path, 'r') as file_handle:
            items = []
            for line in file_handle:
                first, second = line.rstrip().split(',')
                items.append((first.split('-'), second.split('-')))
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_sum_of_contains(input_list: list) -> int:
    sum = 0
    for line in input_list:
        first, second = line
        if int(first[0]) <= int(second[0]) and int(first[1]) >= int(second[1]):
            sum += 1
        elif int(second[0]) <= int(first[0]) and int(second[1]) >= int(first[1]):
            sum += 1
    return sum


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_sum_of_contains(input))
