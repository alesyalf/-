from rewording.changer import change


class Node:
    def __init__(self, template, data):
        self.template = template
        self.words = template.split('$')
        self.data = data
        self.children = []

    def add_child(self, node):
        self.children.append(node)

    def delete_child(self, index):
        self.children.pop(index)

    @property
    def result(self):
        return '$'.join(self.words)

    def apply_in_position(self, index, new_word):
        self.words[index] = change(self.words[index], new_word)
        for child in self.children:
            try:
                child.apply_in_position(child.data.index(new_word) * 2 + 1, new_word)
            except ValueError:
                pass

    def apply_no_cascade(self):
        for i, word in enumerate(self.data):
            index = i * 2 + 1
            self.words[index] = change(self.words[index], word)

    def apply_template(self):
        for i, word in enumerate(self.data):
            self.apply_in_position(i * 2 + 1, word)

    def get_children_results(self):
        results = []
        for child in self.children:
            results.append(child.result)
            if child.children:
                results.extend(child.get_children_results())
        return results

    def apply_for_children_nodes(self):
        for child in self.children:
            child.apply_no_cascade()
            child.apply_for_children_nodes()

    def print_result(self):
        print(self.result)


class Tree:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_node(self, node):
        self.children.append(node)

    def apply_all(self):
        for child in self.children:
            child.apply_no_cascade()
            child.apply_for_children_nodes()

    def delete_child(self, index: int):
        self.children.pop(index)

    def print_all_results(self):
        results = [self.name]

        for child in self.children:
            results.append(child.result)
            results.extend(child.get_children_results())

        print(*results, sep="\n")
        print('Tree Size:' + str(len(results)))
