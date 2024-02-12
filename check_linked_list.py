from linked_list import LinkedList, Node


def linked_list_from_a_list(a_list):
    linked_list = LinkedList()
    for item in a_list:
        linked_list.push(item)
    return linked_list


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
