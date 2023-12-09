# Definition for a Node.
from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    @classmethod
    def from_list(cls, values: list[int]):
        if not values:
            return

        if not values:
            return

        root: Node = cls(values[0])
        queue: List[Node] = [root]
        i = 1

        while queue and i < len(values):
            node = queue.pop(0)

            if values[i] is not None:
                node.left = cls(values[i])
                queue.append(node.left)

            i += 1

            if i < len(values) and values[i] is not None:
                node.right = cls(values[i])
                queue.append(node.right)

            i += 1

        return root

    def __repr__(self):
        return (
            f"Node(val={self.val} left={self.left} right={self.right} next={self.next})"
        )

    def to_list(self) -> List[int | str]:
        if not self:
            return []

        result = []
        queue = deque([self, "#"])

        while queue:
            current = queue.popleft()

            if current == "#":
                result.append("#")
                if queue:
                    queue.append("#")
            else:
                result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

        return result


class Solution:
    def connect_recursive(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return

        def rec_con(left: Optional[Node], right: Optional[Node]):
            if left and right:
                rec_con(left.right, right.left)
            elif left:
                left.next = right
                rec_con(left.left, left.right)
            elif right:
                rec_con(right.left, right.right)

        rec_con(root.left, root.right)

        return root

    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root or not root.left:
            return root

        leftmost = root
        while leftmost and leftmost.left:
            head = leftmost
            next_leftmost = leftmost.left

            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = next_leftmost

        return root


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 4, 5, 6, 7], [1, "#", 2, 3, "#", 4, 5, 6, 7, "#"]),
        ([], []),
        (
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            [1, "#", 2, 3, "#", 4, 5, 6, 7, "#", 8, 9, 10, 11, 12, 13, 14, 15, "#"],
        ),
    ]:
        root = Node.from_list(data[0])
        want = data[1]

        result = s.connect(root)
        recursive = s.connect_recursive(root)
        got = result.to_list() if result else []
        got_rec = recursive.to_list() if recursive else []

        assert want == got == got_rec, f"\nin={data[0]}\nwant={data[1]}got={got}"
