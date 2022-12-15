
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                new_line = []
                line = line.strip().split()
                for item in line:
                    if item != '->':
                        new_line.append(item.split(','))
                items.append(new_line)
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def crate_map(inputs: list) -> set:
    map = set()
    for rock in inputs:
        for i in range(len(rock) - 1):
            x_1, y_1 = int(rock[i][0]), int(rock[i][1])
            x_2, y_2 = int(rock[i + 1][0]), int(rock[i + 1][1])
            if x_1 == x_2:
                for y in range(min(y_1, y_2), max(y_1, y_2) + 1):
                    if (x_1, y) not in map:
                        map.add((x_1, y))
            elif y_1 == y_2:
                for x in range(min(x_1, x_2), max(x_1, x_2) + 1):
                    if (x, y_1) not in map:
                        map.add((x, y_1))
    return map


def get_units_of_sand(inputs: list) -> int:
    map = crate_map(inputs)
    lowest = 0
    for point in map:
        if point[1] > lowest:
            lowest = point[1]
    for x in range(0, 1000):
        map.add((x, lowest + 2))
    units = 0
    reached_top = False
    while not reached_top:
        x, y = 500, 0
        filled = False
        while not filled:
            if (x, y + 1) not in map:
                y += 1
            elif (x - 1, y + 1) not in map:
                y += 1
                x -= 1
            elif (x + 1, y + 1) not in map:
                y += 1
                x += 1
            elif x == 500 and y == 0:
                filled = True
                reached_top = True
                units += 1
            else:
                map.add((x, y))
                units += 1
                break
    return units


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_units_of_sand(input))
