
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items = [*line.rstrip()]
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_first_marker(inputs: list) -> int:
    temp = []
    for i in range(len(inputs) - 4):
        if len(temp) == 14:
            return i
        elif inputs[i] not in temp:
            temp.append(inputs[i])
        else:
            while(inputs[i] in temp):
                temp.pop(0)
            temp.append(inputs[i])


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_first_marker(input))
