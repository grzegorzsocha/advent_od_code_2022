import json
import math

file_name = "input.json"


def read_from_file(path: str) -> list:
    try:
        f = open(path)
        data = json.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print(f'File {path} not found.')


def get_monkey_business_sum(inputs: list, level: int) -> int:
    inspections = [0] * len(inputs)
    div = math.prod([2, 3, 5, 7, 11, 13, 17, 19])
    for i in range(level):
        for key, value in inputs.items():
            while len(value["Items"]) != 0:
                if value["Operator"] == "+":
                    if type(value["Operation"]) is int:
                        value["Items"][0] += value["Operation"]
                    else:
                        value["Items"][0] += value["Items"][0]
                elif value["Operator"] == "*":
                    if type(value["Operation"]) is int:
                        value["Items"][0] *= value["Operation"]
                    else:
                        value["Items"][0] *= value["Items"][0]
                inspections[int(key[-1])] += 1
                value["Items"][0] %= div
                if value["Items"][0] % value["Test"] == 0:
                    inputs[f'Monkey {value["true"]}']["Items"].append(value["Items"].pop(0))
                else:
                    inputs[f'Monkey {value["false"]}']["Items"].append(value["Items"].pop(0))
    inspections.sort(reverse=True)
    return inspections[0] * inspections[1]


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        print(get_monkey_business_sum(input, 10_000))
