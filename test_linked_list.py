import pytest
from linked_list import Node, LinkedList


def test_cr(capsys):
    with capsys.disabled():
        print("\n")
    captured = capsys.readouterr()
    print(captured.out)


@pytest.mark.parametrize(
    "description, data, expected_data",
    [("Node:constructor:number", 5, 5), ("Node:constructor:text", "ten", "ten")],
)
def test_node(description, data, expected_data, capsys):
    with capsys.disabled():
        print(description)
    captured = capsys.readouterr()
    print(captured.out)

    node = Node(data)
    assert node.get_data() == expected_data
    assert node.get_next() is None

    with capsys.disabled():
        node.log()
    captured = capsys.readouterr()
    print(captured.out)


@pytest.mark.parametrize(
    "description, nodes, expected_first_data, expected_prev_to_last_data, expected_last_data",
    [
        ("LinkedList:empty", [], None, None, None),
        ("LinkedList:from Node", [Node(5)], 5, None, 5),
        ("LinkedList:short", [1, 2], 1, 1, 2),
        ("LinkedList:normal length", [1, 2, 3, 4, 5], 1, 4, 5),
    ],
)
def test_linked_list(
    description,
    nodes,
    expected_first_data,
    expected_prev_to_last_data,
    expected_last_data,
    capsys,
):
    with capsys.disabled():
        print(description)
    captured = capsys.readouterr()
    print(captured.out)
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


@pytest.mark.parametrize(
    "description, nodes",
    [
        ("LinkedList.pop:empty", []),
        ("LinkedList.pop:single", [1]),
        ("LinkedList.pop:short", [1, 2]),
        ("LinkedList.pop:normal length", [1, 2, 3]),
    ],
)
def test_pop(description, nodes, capsys):
    with capsys.disabled():
        print(description)
    captured = capsys.readouterr()
    print(captured.out)

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
