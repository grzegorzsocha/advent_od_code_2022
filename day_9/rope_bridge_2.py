
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
    knots = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
    for i in range(len(inputs)):
        if inputs[i][0] == 'R':
            for _ in range(int(inputs[i][1]), 0, -1):
                knots[0][0] += 1
                for k in range(len(knots) - 1):
                    knots[k + 1][0], knots[k + 1][1] = move_tail(knots[k][0], knots[k][1], knots[k + 1][0], knots[k + 1][1])
                if (knots[9][0], knots[9][1]) not in visited_positions:
                    visited_positions.append((knots[9][0], knots[9][1]))
        elif inputs[i][0] == 'L':
            for _ in range(int(inputs[i][1]), 0, -1):
                knots[0][0] -= 1
                for k in range(len(knots) - 1):
                    knots[k + 1][0], knots[k + 1][1] = move_tail(knots[k][0], knots[k][1], knots[k + 1][0], knots[k + 1][1])
                if (knots[9][0], knots[9][1]) not in visited_positions:
                    visited_positions.append((knots[9][0], knots[9][1]))
        elif inputs[i][0] == 'U':
            for _ in range(int(inputs[i][1]), 0, -1):
                knots[0][1] += 1
                for k in range(len(knots) - 1):
                    knots[k + 1][0], knots[k + 1][1] = move_tail(knots[k][0], knots[k][1], knots[k + 1][0], knots[k + 1][1])
                if (knots[9][0], knots[9][1]) not in visited_positions:
                    visited_positions.append((knots[9][0], knots[9][1]))
        elif inputs[i][0] == 'D':
            for _ in range(int(inputs[i][1]), 0, -1):
                knots[0][1] -= 1
                for k in range(len(knots) - 1):
                    knots[k + 1][0], knots[k + 1][1] = move_tail(knots[k][0], knots[k][1], knots[k + 1][0], knots[k + 1][1])
                if (knots[9][0], knots[9][1]) not in visited_positions:
                    visited_positions.append((knots[9][0], knots[9][1]))
    return len(visited_positions)


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_number_of_visited_positions(input))
