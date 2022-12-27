import pytest

from main.main import (
    LinkedList,
    Node
)


def test_nodes_str():
    node_one = Node("A")
    actual = str(node_one)
    expected = "A"
    assert actual == expected

