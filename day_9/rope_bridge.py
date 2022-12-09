
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append(line.rstrip().split())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def move_tail(head_x: int, head_y: int, tail_x: int, tail_y: int) -> tuple:
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_x, tail_y
    elif tail_x == head_x:
        tail_y += 1 if tail_y < head_y else -1
    elif tail_y == head_y:
        tail_x += 1 if tail_x < head_x else -1
    elif tail_y == head_y - 2:
        tail_y += 1
        tail_x += 1 if tail_x < head_x else -1
    elif tail_y == head_y + 2:
        tail_y -= 1
        tail_x += 1 if tail_x < head_x else -1
    elif tail_x == head_x - 2:
        tail_x += 1
        tail_y += 1 if tail_y < head_y else -1
    elif tail_x == head_x + 2:
        tail_x -= 1
        tail_y += 1 if tail_y < head_y else -1
    return tail_x, tail_y


def get_number_of_visited_positions(inputs: list) -> int:
    visited_positions = []
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    for i in range(len(inputs)):
        if inputs[i][0] == 'R':
            for i in range(int(inputs[i][1]), 0, -1):
                head_x += 1
                tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
                if (tail_x, tail_y) not in visited_positions:
                    visited_positions.append((tail_x, tail_y))
        elif inputs[i][0] == 'L':
            for i in range(int(inputs[i][1]), 0, -1):
                head_x -= 1
                tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
                if (tail_x, tail_y) not in visited_positions:
                    visited_positions.append((tail_x, tail_y))
        elif inputs[i][0] == 'U':
            for i in range(int(inputs[i][1]), 0, -1):
                head_y += 1
                tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
                if (tail_x, tail_y) not in visited_positions:
                    visited_positions.append((tail_x, tail_y))
        elif inputs[i][0] == 'D':
            for i in range(int(inputs[i][1]), 0, -1):
                head_y -= 1
                tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
                if (tail_x, tail_y) not in visited_positions:
                    visited_positions.append((tail_x, tail_y))
    return len(visited_positions)


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_number_of_visited_positions(input))
