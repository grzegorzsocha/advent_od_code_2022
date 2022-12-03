
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
    for line in input_list:
        first, second = line[:len(line)//2], line[len(line)//2:]
        for character in first:
            if character in second:
                if character.isupper():
                    sum += ord(character) - 38
                    break
                else:
                    sum += ord(character) - 96
                    break
    return sum


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_sum_of_priorities(input))
