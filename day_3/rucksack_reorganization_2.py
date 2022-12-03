
file_name = "input.txt"


def read_from_file(path):
    try:
        with open(path, 'r') as file_handle:
            items = []
            for line in file_handle:
                items.append(line.rstrip())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_sum_of_priorities(input_list):
    sum = 0
    first, second, third = None, None, None
    for line in input_list:
        if first is None:
            first = line
        elif second is None:
            second = line
        elif third is None:
            third = line
            for character in first:
                if character in second and character in third:
                    if character.isupper():
                        sum += ord(character) - 38
                        break
                    else:
                        sum += ord(character) - 96
                        break
            first, second, third = None, None, None
    return sum


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_sum_of_priorities(input))
