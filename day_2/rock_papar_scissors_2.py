
file_name = "input.txt"


def read_from_file(path):
    try:
        with open(path, 'r') as file_handle:
            result = get_score(file_handle)
            return result
    except FileNotFoundError:
        print(f'File {path} not found.')

# A = rock
# B = paper
# C = scissors

# X = lose
# Y = draw
# Z = win


def get_score(file_handle):
    scores = {
        ('A', 'X'): 3,
        ('A', 'Y'): 4,
        ('A', 'Z'): 8,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 2,
        ('C', 'Y'): 6,
        ('C', 'Z'): 7
    }
    score = 0
    for line in file_handle:
        opponent, me = line.rstrip().split()
        score += scores[(opponent, me)]
    return score


if __name__ == "__main__":
    print(read_from_file(file_name))
