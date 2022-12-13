import json
import itertools

file_name = "input.json"


def read_from_file(path: str) -> list:
    try:
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_order(left, right) -> bool:
    if type(left) is int:
        if type(right) is int:
            if left < right:
                return True
            elif left > right:
                return False
        else:
            return get_order([left], right)
    elif type(right) is int:
        return get_order(left, [right])
    else:
        for first, second in itertools.zip_longest(left, right):
            if first is None:
                return True
            elif second is None:
                return False
            if get_order(first, second) is not None:
                return get_order(first, second)


def get_sum_of_indices(inputs: list) -> int:
    sum = 0
    for i in range(1, len(inputs), 2):
        if get_order((inputs[i - 1]), (inputs[i])):
            sum += (i + 1) // 2
    return sum


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_sum_of_indices(input))
