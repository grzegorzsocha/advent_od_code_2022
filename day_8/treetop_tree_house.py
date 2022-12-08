
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append(line.rstrip())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def is_around(x: int, y: int, inputs: list) -> bool:
    if x == 0 or y == 0 or y == len(inputs) - 1 or x == len(inputs[x]) - 1:
        return True
    return False


def from_top(x: int, y: int, inputs: list) -> bool:
    check_y = y
    while check_y > 0:
        check_y -= 1
        if inputs[y][x] <= inputs[check_y][x]:
            return False
    return True


def from_bottom(x: int, y: int, inputs: list) -> bool:
    check_y = y
    while check_y < len(inputs) - 1:
        check_y += 1
        if inputs[y][x] <= inputs[check_y][x]:
            return False
    return True


def from_right(x: int, y: int, inputs: list) -> bool:
    check_x = x
    while check_x < len(inputs) - 1:
        check_x += 1
        if inputs[y][x] <= inputs[y][check_x]:
            return False
    return True


def from_left(x: int, y: int, inputs: list) -> bool:
    check_x = x
    while check_x > 0:
        check_x -= 1
        if inputs[y][x] <= inputs[y][check_x]:
            return False
    return True


def get_visible_trees(inputs: list) -> int:
    visible_trees = 0
    for i in range(len(inputs)):
        for j in range(len(inputs[i])):
            if (is_around(j, i, inputs) or from_top(j, i, inputs) or
                    from_bottom(j, i, inputs) or from_left(j, i, inputs) or
                    from_right(j, i, inputs)):
                visible_trees += 1
    return visible_trees


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_visible_trees(input))
