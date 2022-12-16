
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


def get_positions(input: list) -> int:
    map, beacons = [], set()
    for row in input:
        sensor, beacon = (int(row[0]), int(row[1])), (int(row[2]), int(row[3]))
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        beacons.add((beacon))
        map.append((sensor, distance))
    cannot_contain = 0
    for i in range(-5_000_000, 5_000_000):
        for sensor, distance in map:
            if abs(sensor[0] - i) + abs(sensor[1] - 2_000_000) <= distance and (i, 2_000_000) not in beacons:
                cannot_contain += 1
                break
    return cannot_contain


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_positions(input))
