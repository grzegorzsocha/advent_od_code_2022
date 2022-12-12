
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append([*line.rstrip()])
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def reogranise_input(input: list) -> tuple:
    end = None
    for i in range(len(input)):
        for j in range(len(input[i])):
            input[i][j] = ord(input[i][j])
            if input[i][j] == 83:
                input[i][j] = 97
            elif input[i][j] == 69:
                end = (i, j)
                input[i][j] = 122
    return input, end


def get_neighbours(map: list, x: int, y: int) -> list:
    neighbours = []
    if x > 0 and map[x - 1][y] - map[x][y] <= 1:
        neighbours.append((x - 1, y))
    if x < len(map) - 1 and map[x + 1][y] - map[x][y] <= 1:
        neighbours.append((x + 1, y))
    if y > 0 and map[x][y - 1] - map[x][y] <= 1:
        neighbours.append((x, y - 1))
    if y < len(map[0]) - 1 and map[x][y + 1] - map[x][y] <= 1:
        neighbours.append((x, y + 1))
    return neighbours


def get_fewest_steps(map: list, start: tuple, end: tuple) -> int:
    visited = set()
    queue = [(start, 0)]
    while queue:
        current, steps = queue.pop(0)
        if current == end:
            return steps
        if current not in visited:
            visited.add(current)
            for neighbour in get_neighbours(map, *current):
                queue.append((neighbour, steps + 1))


def get_all_a_squares(input: list) -> list:
    a_squares = []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 97:
                a_squares.append((i, j))
    return a_squares


def get_best_start(input: list) -> int:
    steps = []
    map, end = reogranise_input(input)
    for start in get_all_a_squares(input):
        fewest_steps = get_fewest_steps(map, start, end)
        if fewest_steps is not None:
            steps.append(fewest_steps)
    return min(steps)


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_best_start(input))
