import pytest
from linked_list import Node, LinkedList


@pytest.mark.parametrize("data, expected_data", [(5, 5), (10, 10)])
def test_node(data, expected_data, capsys):
    node = Node(data)
    assert node.get_data() == expected_data
    assert node.get_next() is None

    with capsys.disabled():
        node.log()
    captured = capsys.readouterr()
    print(captured.out)


@pytest.mark.parametrize(
    "nodes, expected_first_data, expected_prev_to_last_data, expected_last_data",
    [
        ([], None, None, None),
        ([Node(5)], 5, None, 5),
        ([1, 2], 1, 1, 2),
        ([1, 2, 3, 4, 5], 1, 4, 5),
    ],
)
def test_linked_list(
    nodes, expected_first_data, expected_prev_to_last_data, expected_last_data, capsys
):
    linked_list = LinkedList()
    for node in nodes:
        linked_list.push(node)

    try:
        assert linked_list.get_first().get_data() == expected_first_data
    except AttributeError:
        assert expected_first_data is None

    try:
        assert (
            linked_list.get_previous_to_last().get_data() == expected_prev_to_last_data
        )
    except AttributeError:
        assert expected_prev_to_last_data is None

    try:
        assert linked_list.get_last().get_data() == expected_last_data
    except AttributeError:
        assert expected_last_data is None

    with capsys.disabled():
        linked_list.log()
    captured = capsys.readouterr()
    print(captured.out)


@pytest.mark.parametrize("nodes", [[], [1], [1, 2], [1, 2, 3]])
def test_pop(nodes, capsys):
    linked_list = LinkedList()
    for node in nodes:
        linked_list.push(node)

    linked_list.pop()

    try:
        assert linked_list.get_last().get_data() == nodes[-2]
    except AttributeError:
        assert linked_list.get_first() is None

    with capsys.disabled():
        linked_list.log()
    captured = capsys.readouterr()
    print(captured.out)


if __name__ == "__main__":
    pytest.main()
