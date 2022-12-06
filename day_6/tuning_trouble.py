
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
    for i in range(len(inputs) - 4):
        a, b, c, d = inputs[i:i + 4]
        if a != b and a != c and a != d and b != c and b != d and c != d:
            return i + 4


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_first_marker(input))
