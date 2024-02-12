import pytest
from linked_list import Node, LinkedList

# Test Node class
@pytest.mark.parametrize("data, expected_data", [(5, 5), (10, 10)])
def test_node(data, expected_data, capsys):
    # Create a node with the provided data
    node = Node(data)
    # Check if the data in the node matches the expected data
    assert node.get_data() == expected_data
    # Check if the next node is None
    assert node.get_next() is None

    # Capture the console output by calling the log method
    with capsys.disabled():
        node.log()
    # Retrieve the captured output
    captured = capsys.readouterr()
    # Print the captured output
    print(captured.out)

# Test LinkedList class
@pytest.mark.parametrize("nodes, expected_first_data, expected_prev_to_last_data, expected_last_data", [
    ([], None, None, None),
    ([Node(5)], 5, None, 5),
    ([1, 2], 1, 1, 2),
    ([1, 2, 3, 4, 5], 1, 4, 5)
])
def test_linked_list(nodes, expected_first_data, expected_prev_to_last_data, expected_last_data, capsys):
    # Create a linked list with the provided nodes
    linked_list = LinkedList()
    for node in nodes:
        linked_list.push(node)

    try:
        assert linked_list.get_first().get_data() == expected_first_data
    except AttributeError:
        assert expected_first_data is None

    try:
        assert linked_list.get_previoust_to_last().get_data() == expected_prev_to_last_data
    except AttributeError:
        assert expected_prev_to_last_data is None

    try:
        assert linked_list.get_last().get_data() == expected_last_data
    except AttributeError:
        assert expected_last_data is None

    # Capture the console output by calling the log method
    with capsys.disabled():
        linked_list.log()
    # Retrieve the captured output
    captured = capsys.readouterr()
    # Print the captured output
    print(captured.out)

@pytest.mark.parametrize("nodes", [[],[1],[1,2],[1,2,3]])
def test_pop(nodes, capsys):
    # Create a linked list with the provided nodes
    linked_list = LinkedList()
    for node in nodes:
        linked_list.push(node)

    linked_list.pop()

    try:
        assert linked_list.get_last().get_data() == nodes[-2]
    except AttributeError:
        assert linked_list.get_first() is None

    # Capture the console output by calling the log method
    with capsys.disabled():
        linked_list.log()
    # Retrieve the captured output
    captured = capsys.readouterr()
    # Print the captured output
    print(captured.out)

if __name__ == "__main__":
    # Run the test cases using pytest
    pytest.main()
