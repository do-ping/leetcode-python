from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        nodes: dict[Node, Node] = {}
        current = head

        # two-pass: faster
        while current:
            nodes[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            node = nodes[current]
            if current.next:
                node.next = nodes[current.next]
            if current.random:
                node.random = nodes[current.random]
            current = current.next

        # # one pass, slower
        # while current:
        #     if current not in nodes:
        #         nodes[current] = Node(current.val)
        #
        #     if current.next:
        #         if current.next not in nodes:
        #             nodes[current.next] = Node(current.next.val)
        #         nodes[current].next = nodes[current.next]
        #
        #     if current.random:
        #         if current.random not in nodes:
        #             nodes[current.random] = Node(current.random.val)
        #         nodes[current].random = nodes[current.random]
        #
        #     current = current.next

        return nodes[head]


def _make_list(nodes: list[list[int, Optional[int]]]) -> Optional[Node]:
    if not nodes:
        return None

    node_dict = {}  # Used to map indices to corresponding nodes

    # Create nodes without setting the "next" or "random" pointers
    for i, (val, _) in enumerate(nodes):
        node = Node(val)
        node_dict[i] = node

    # Set the "next" and "random" pointers
    for i, (val, random_index) in enumerate(nodes):
        current_node = node_dict[i]

        # Set "next" pointer
        if i < len(nodes) - 1:
            current_node.next = node_dict[i + 1]

        # Set "random" pointer
        if random_index is not None:
            current_node.random = node_dict[random_index]

    return node_dict[0]


def _print_ll(head: Node):
    s = []
    current = head
    while current:
        s.append(
            f"val={current.val} pointing_to={current.random.val if current.random else None} -> "
        )
        current = current.next
    print("".join(s))


if __name__ == "__main__":
    s = Solution()
    data: list[list[int | None]]
    for data in [
        [[7, None], [13, 1], [11, 4], [10, 2], [1, 0]],
        [[1, 1], [2, 1]],
        [[3, None], [3, 0], [3, None]],
    ]:
        ll = _make_list(data)
        print("input")
        _print_ll(ll)
        result = s.copyRandomList(ll)
        print("result")
        _print_ll(result)
        print()
