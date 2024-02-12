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
