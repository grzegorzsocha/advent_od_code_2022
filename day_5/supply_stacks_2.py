
file_name = "input.txt"


def read_from_file(path: str) -> list:
    try:
        with open(path, 'r') as file_handle:
            items = []
            for line in file_handle:
                temp = line.rstrip().split(' ')
                items.append((temp[1], temp[3], temp[5]))
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_supply_arrangement(input_list: list) -> str:
    stacks = {
        1: ['T', 'D', 'W', 'Z', 'V', 'P'],
        2: ['L', 'S', 'W', 'V', 'F', 'J', 'D'],
        3: ['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'],
        4: ['R', 'S', 'J'],
        5: ['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'],
        6: ['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'],
        7: ['V', 'J', 'P', 'C', 'B', 'D', 'N'],
        8: ['P', 'T', 'B', 'Q'],
        9: ['H', 'G', 'Z', 'R', 'C']
    }

    for line in input_list:
        quanity, first, second = line
        temp = []
        for i in range(int(quanity)):
            temp.append(stacks[int(first)].pop())
        for i in range(int(quanity)):
            stacks[int(second)].append(temp.pop())

    result = ''
    for i in range(1, 10):
        result += stacks[i][-1]
    return result


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_supply_arrangement(input))
