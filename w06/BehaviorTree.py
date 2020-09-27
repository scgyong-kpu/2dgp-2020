
level = 0
def indent():
    global level
    level += 1

def unindent():
    global level
    level -= 1

def print_indent():
    for i in range(level):
        print("    ", end='')


class BehaviorTree:
    FAIL, RUNNING, SUCCESS = -1, 0, 1

    def __init__(self, root_node):
        self.root = root_node

    def run(self):
        self.root.run()

    def print(self):
        self.root.print()

    @staticmethod
    def build(dict):
        return BehaviorTree(build_node(dict))

class Node:
    def add_child(self, child):
        self.children.append(child)
    def add_children(self, *children):
        for child in children:
            self.children.append(child)


class SelectorNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.SUCCESS == result:
                self.prev_running_pos = 0
                return BehaviorTree.SUCCESS
        self.prev_running_pos = 0
        return BehaviorTree.FAIL

    def print(self):
        print_indent()
        print("SELECTOR NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()

class SequenceNode(Node):
    def __init__(self, name):
        self.children = []
        self.name = name
        self.prev_running_pos = 0

    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.FAIL == result:
                self.prev_running_pos = 0
                return BehaviorTree.FAIL
        self.prev_running_pos = 0
        return BehaviorTree.SUCCESS

    def print(self):
        print_indent()
        print("SEQUENCE NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()


class LeafNode(Node):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def add_child(self, child):
        print("ERROR: you cannot add child node to leaf node")

    def add_children(self, *children):
        print("ERROR: you cannot add children node to leaf node")

    def run(self):
        return self.func()

    def print(self):
        print_indent()
        print("LEAF NODE: " + self.name)


def build_node(dict):
    name = dict["name"]
    clazz = dict["class"]
    if clazz == LeafNode:
        func = dict["function"]
        return clazz(name, func)

    node = clazz(name)
    children = dict["children"]
    for child in children:
        node.add_child(build_node(child))

    return node
