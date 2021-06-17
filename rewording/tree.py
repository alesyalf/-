from rewording.changer import change


def find_arg(data: str):
    start = finish = 0
    for i in range(len(data)):
        if data[i] == '$' and start == 0:
            start = i + 1
            continue
        if data[i] == '$' and start != 0 and finish == 0:
            finish = i
            break
    return data[start:finish]


class Node:
    def __init__(self, data, template):
        self.data = data
        self.template = template
        self.arg = find_arg(data)
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def delete_child(self, index):
        self.children.pop(index)

    def change_pattern(self):
        res = change(self.arg, self.template)
        start = finish = 0

        for i in range(len(self.data)):
            if self.data[i] == '$' and start == 0:
                start = i + 1
            elif self.data[i] == '$' and start != 0 and finish == 0:
                finish = i
                break

        final = self.data[:start] + res + self.data[finish:]
        self.data = final

    def get_child_nodes(self, tree):
        for child in self.children:
            if child.children:
                child.get_child_nodes(tree)
            tree.append(child.data)

    def change_child_nodes(self):
        for child in self.children:
            child.change_pattern()
            child.change_child_nodes()


class Tree:
    def __init__(self, root):
        self.root = root
        self.children = []

    def add_node(self, node):
        self.children.append(node)

    def change_all(self):
        for child in self.children:
            child.change_pattern()

        for child in self.children:
            child.change_child_nodes()

    def delete_child(self, index: int):
        self.children.pop(index)

    def print_all_nodes(self):
        nodes = [self.root]

        for child in self.children:
            nodes.append(child.data)
        for child in self.children:
            child.get_child_nodes(nodes)

        print(*nodes, sep="\n")
        print('Tree Size:' + str(len(nodes)))
