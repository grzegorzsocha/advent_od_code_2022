
file_name = "input.txt"


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.dirs = []
        self.size = 0
        self.to_delete = []

    def add_file(self, file):
        self.files.append(file)

    def add_dir(self, dir):
        self.dirs.append(dir)

    def set_size(self):
        self.size = self.get_sum_of_files()
        for dir in self.dirs:
            dir.set_size()
            self.size += dir.size

    def get_sum_of_files(self):
        sum = 0
        for file in self.files:
            sum += int(file[0])
        return sum

    def get_children_by_name(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def get_sum_of_dirs_less_than(self, size):
        sum = 0
        for dir in self.dirs:
            if dir.size <= size:
                sum += dir.size
            sum += dir.get_sum_of_dirs_less_than(size)
        return sum

    def get_root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.get_root()

    def get_dirs_to_delete(self):
        free_space = 7_870_454
        for dir in self.dirs:
            if dir.size >= free_space:
                self.get_root().to_delete.append(dir.size)
            dir.get_dirs_to_delete()
        return self.to_delete


def read_from_file(path: str) -> list:
    try:
        items = []
        with open(path, 'r') as file_handle:
            for line in file_handle:
                items.append(line.rstrip().split())
            return items
    except FileNotFoundError:
        print(f'File {path} not found.')


def create_file_tree(commands: list) -> Directory:
    root = None
    current_dir = None
    for i in range(len(commands)):
        if commands[i][1] == 'cd' and commands[i][2] == '..':
            current_dir = current_dir.parent
        elif commands[i][1] == 'cd' and current_dir is None:
            root = Directory(commands[i][2], None)
            current_dir = root
        elif commands[i][1] == 'cd':
            current_dir = current_dir.get_children_by_name(commands[i][2])
        elif commands[i][1] == 'ls':
            continue
        elif commands[i][0] == 'dir':
            current_dir.add_dir(Directory(commands[i][1], current_dir))
        else:
            current_dir.add_file(commands[i])
    return root


if __name__ == "__main__":
    input = read_from_file(file_name)
    if input is not None:
        tree = create_file_tree(input)
        tree.set_size()
        tree.get_dirs_to_delete()
        tree.to_delete.sort()
        print(tree.to_delete[0])
