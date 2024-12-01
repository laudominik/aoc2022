class Node:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.subdirs = []
        self.files = []

    def size(self, lookup, sizes):
        if self.name in sizes:
            return sizes[self.name]
        sizes[self.name] = sum(self.files) + sum([lookup[x].size(lookup, sizes) for x in self.subdirs])
        return sizes[self.name]

def parseTree(commands):
    tree = {'/':0}
    path = ['/']
# [0] - sum [1] - parent
    for command in commands:
        if command.startswith('$ cd'):
            if command[5:] == '..':
                path.pop()
            elif command[5:] != '/':
                path.append(command[5:])
        elif command.startswith('$ ls') or command.startswith('dir'):
            pass
        else:
            val = int(command.split(" ")[0])
            for i in range(len(path)+1):
                p = ".".join(path[:i])
                tv = 0 if p not in tree else tree[p]
                tree[p] = tv + val

    print(sum(list(filter(lambda x: x <= 100000, tree.values()))))
    print(tree)
    print(min(list(filter(lambda x: x >= tree['/'] - 40000000, tree.values()))))

with open("input7.txt", "r") as f:
    parseTree(f.read().split("\n"))