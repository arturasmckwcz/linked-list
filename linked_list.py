class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next_node

    def set_next(self, node):
        self.__next_node = node

    def log(self):
        print(self.__data)


class LinkedList:
    def __init__(self, start=None):
        if not (isinstance(start, Node) or start == None):
            start = Node(start)
        self.__first_node = start
        self.__last_node = start

    def is_empty(self):
        return self.__first_node is None and self.__last_node is None

    def get_first(self):
        return self.__first_node

    def get_last(self):
        return self.__last_node

    def push(self, node):
        if isinstance(node, Node):
            node.set_next(None)
        else:
            node = Node(node)
        if self.is_empty():
            self.__first_node = node
            self.__last_node = node
        else:
            self.__last_node.set_next(node)
            self.__last_node = node

    def pop(self):
        if self.__first_node == self.__last_node:
            self.__first_node = None
            self.__last_node = None
            return
        self.__last_node = self.get_previous_to_last()
        self.__last_node.set_next(None)

    def get_previous_to_last(self):
        node = self.__first_node
        if node == None or node.get_next() is None:
            return None
        while True:
            if node.get_next().get_next() is None:
                return node
            else:
                node = node.get_next()

    def log(self):
        if self.is_empty():
            print("The list is empty.")
            return

        arrow = " -> "
        printout = "START: "
        node = self.__first_node
        while True:
            printout += str(node.get_data()) + arrow
            if node.get_next() == None:
                break
            else:
                node = node.get_next()
        printout = printout[: -len(arrow)] + " :END"
        print(printout)


def linked_list_from_a_list(a_list):
    linked_list = LinkedList()
    for item in a_list:
        linked_list.push(item)
    return linked_list


if __name__ == "__main__":
    nums = [n for n in range(3)]
    names = ["John", "Ann", "Sarah", "Eva", "Petter", "George"]
    delimiter = "-----------------------------"

    print(delimiter)
    print("names:")
    linked_list = linked_list_from_a_list(sorted(names))
    linked_list.log()
    print("the first:")
    linked_list.get_first().log()
    print("the last:")
    linked_list.get_last().log()
    print("previous to the last:")
    linked_list.get_previous_to_last().log()
    print("push data:")
    linked_list.push("Theo")
    linked_list.log()
    print("push node:")
    linked_list.push(Node("Xana", Node("nothing")))
    linked_list.log()
    print("the last:")
    linked_list.get_last().log()

    print(delimiter)
    print("numbers:")
    linked_list = linked_list_from_a_list(list(range(4)))
    node = linked_list.get_first()
    linked_list.log()
    print("the first:")
    linked_list.get_first().log()
    print("the last:")
    linked_list.get_last().log()
    print("previous to the last:")
    linked_list.get_previous_to_last().log()
    print("pop:")
    while not linked_list.is_empty():
        linked_list.pop()
        linked_list.log()

    print(delimiter)
    print("single element:")
    linked_list = LinkedList(Node("single"))
    linked_list.log()
    print("the first:")
    linked_list.get_first().log()
    print("the last:")
    linked_list.get_last().log()
    print("previous to the last:")
    prev_to_last = linked_list.get_previous_to_last()
    if prev_to_last == None:
        print(None)
    else:
        prev_to_last.log()

    print(delimiter)
    print("empty:")
    linked_list = LinkedList()
    linked_list.log()
    print("the first:")
    first = linked_list.get_first()
    if first == None:
        print(None)
    else:
        first.log()
    print("the last:")
    last = linked_list.get_last()
    if last == None:
        print(None)
    else:
        last.log()
    print("previous to the last:")
    prev_to_last = linked_list.get_previous_to_last()
    if prev_to_last == None:
        print(None)
    else:
        prev_to_last.log()
    print("pop (empty):")
    if linked_list.is_empty():
        linked_list.pop()
        linked_list.log()
