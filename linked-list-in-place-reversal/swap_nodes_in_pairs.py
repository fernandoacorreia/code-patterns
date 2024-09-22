import pytest
from pprint import pprint


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node):
        current = self.head
        if current == None:
            self.head = node
            return
        while current.next != None:
            current = current.next
        current.next = node

    def append_multiple(self, elements):
        for el in elements:
            new_node = Node(el)
            self.append(new_node)

    def to_list(self):
        l = []
        current = self.head
        while current != None:
            l.append(current.data)
            current = current.next
        return l

    def swap_adjacent_pairs(self):
        last_tail = None
        current = self.head
        while current != None and current.next != None:
            second_element = current.next
            next_pair = second_element.next
            second_element.next = current
            if last_tail == None:
                self.head = second_element
            else:
                last_tail.next = second_element
            last_tail = current
            current.next = next_pair # will be overwritten if there is another swap, or kept if there is a dangling node
            current = next_pair

@pytest.mark.parametrize("elements", [
    ([]),
    ([1]),
    ([1, 9]),
    ([10, 12, 20, 17, 42]),
])
def test_append(elements):
    l = LinkedList()
    l.append_multiple(elements)
    visited = l.to_list()
    assert visited == elements

@pytest.mark.parametrize("input, expected_output", [
    ([1,2,3,4,5,6,7,8],[2,1,4,3,6,5,8,7]),
    ([1,2],[2,1]),
    ([1],[1]),
    ([],[]),
    (["a","b","c","d","e","f"],["b","a","d","c","f","e"]),
    ([1,2,3],[2,1,3]),
])
def test_append(input, expected_output):
    l = LinkedList()
    l.append_multiple(input)
    assert l.to_list() == input
    l.swap_adjacent_pairs()
    output = l.to_list()
    assert output == expected_output
