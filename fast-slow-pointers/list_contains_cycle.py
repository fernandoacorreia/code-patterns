import pytest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, elements):
        self.head = None
        for el in elements:
            self.append(el)

    def append(self, el):
        new_node = Node(el)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def contains_cycle(self):
        slow_pointer = self.head
        if slow_pointer == None:
            return False
        fast_pointer = slow_pointer.next
        if fast_pointer == None:
            return False

        while slow_pointer != fast_pointer:
            # Increment slow pointer by 1 element
            slow_pointer = slow_pointer.next
            # Increment fast pointer by 2 elements
            fast_pointer = fast_pointer.next
            if fast_pointer == None:
                return False
            fast_pointer = fast_pointer.next
            if fast_pointer == None:
                return False

        return True


@pytest.mark.parametrize("items", [
    ([]),
    ([1]),
    ([1, 2, 3, 4, 5]),
])
def test_contains_cycle_no(items):
    l = LinkedList(items)
    assert l.contains_cycle() == False

@pytest.mark.parametrize("items, cycle_to, cycle_from", [
    ([1, 2, 3, 4, 5], 0, 4),
    ([1, 2, 3, 4, 5], 3, 4),
    ([1, 2, 3, 4, 5], 0, 1),
    ([1, 2, 3, 4, 5], 1, 3),
])
def test_contains_cycle_yes(items, cycle_to, cycle_from):
    l = LinkedList(items)

    # Add cycle to list. Constraint: cycle_to must be < cycle_from and both must be < linked list length.
    node_to = None
    node_from = None
    i = 0
    current_node = l.head
    while i <= cycle_from:
        print(f"i={i}")
        if i == cycle_to:
            print(f"to node {current_node.data}")
            node_to = current_node
        if i == cycle_from:
            print(f"from node {current_node.data}")
            node_from = current_node
        current_node = current_node.next
        print(f"current_node={current_node}")
        i += 1
    node_from.next = node_to

    assert l.contains_cycle() == True

