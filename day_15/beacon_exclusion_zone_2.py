
file_name = "input.txt"


def read_from_file(path: str):
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append(line.strip().split())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_positions(input: list):
    map = []
    for row in input:
        sensor, beacon = (int(row[0]), int(row[1])), (int(row[2]), int(row[3]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        map.append((sensor, distance))
    possibles = []
    for sensor, distance in map:
        dist = distance + 1
        current_x, current_y = sensor[0], sensor[1] - dist
        while current_x != sensor[0] + dist and current_y != sensor[1]:
            if current_x >= 0 and current_x <= 4_000_000 and current_y >= 0 and current_y <= 4_000_000:
                possibles.append((current_x, current_y))
            current_x += 1
            current_y += 1
        while current_x != sensor[0] and current_y != sensor[1] + dist:
            if current_x >= 0 and current_x <= 4_000_000 and current_y >= 0 and current_y <= 4_000_000:
                possibles.append((current_x, current_y))
            current_x -= 1
            current_y += 1
        while current_x != sensor[0] - dist and current_y != sensor[1]:
            if current_x >= 0 and current_x <= 4_000_000 and current_y >= 0 and current_y <= 4_000_000:
                possibles.append((current_x, current_y))
            current_x -= 1
            current_y -= 1
        while current_x != sensor[0] and current_y != sensor[1] - dist:
            if current_x >= 0 and current_x <= 4_000_000 and current_y >= 0 and current_y <= 4_000_000:
                possibles.append((current_x, current_y))
            current_x += 1
            current_y -= 1
    for possible_x, possible_y in possibles:
        for sensor, distance in map:
            if abs(sensor[0] - possible_x) + abs(sensor[1] - possible_y) <= distance:
                break
        else:
            return possible_x * 4_000_000 + possible_y


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_positions(input))
