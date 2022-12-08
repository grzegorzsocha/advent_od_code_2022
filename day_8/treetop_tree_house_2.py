
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


def from_top(x: int, y: int, inputs: list) -> int:
    trees = 0
    check_y = y
    while check_y > 0:
        check_y -= 1
        trees += 1
        if inputs[y][x] <= inputs[check_y][x]:
            break
    return trees


def from_bottom(x: int, y: int, inputs: list) -> int:
    trees = 0
    check_y = y
    while check_y < len(inputs) - 1:
        check_y += 1
        trees += 1
        if inputs[y][x] <= inputs[check_y][x]:
            break
    return trees


def from_right(x: int, y: int, inputs: list) -> int:
    trees = 0
    check_x = x
    while check_x < len(inputs) - 1:
        check_x += 1
        trees += 1
        if inputs[y][x] <= inputs[y][check_x]:
            break
    return trees


def from_left(x: int, y: int, inputs: list) -> int:
    trees = 0
    check_x = x
    while check_x > 0:
        check_x -= 1
        trees += 1
        if inputs[y][x] <= inputs[y][check_x]:
            break
    return trees


def get_best_score_tree(inputs: list) -> int:
    best = 0
    for i in range(1, len(inputs) - 1):
        for j in range(1, len(inputs[i]) - 1):
            current = 0
            current = from_top(j, i, inputs) * from_bottom(j, i, inputs) *\
                from_right(j, i, inputs) * from_left(j, i, inputs)
            if current > best:
                best = current
    return best


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_best_score_tree(input))
