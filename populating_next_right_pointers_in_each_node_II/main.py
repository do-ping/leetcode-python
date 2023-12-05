# Definition for a Node.
from collections import deque
from typing import List


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

    def print(self):
        if not root:
            return

        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()
                print(current.val, end=" ")

                if current.next:
                    print(f"({current.next.val})", end=" ")

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            print()  # Move to the next line after printing a level

    def to_list(self) -> List[int | str]:
        if not root:
            return []

        result = []
        queue = deque([root, "#"])

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
    def connect(self, root: Node) -> Node:
        if not root:
            return root

        # queue = [root]
        # while queue:
        #     level_size = len(queue)
        #     previous_right = None
        #
        #     for i in range(level_size):
        #         current = queue.pop(0)  # popleft
        #
        #         if current.left:
        #             if previous_right:
        #                 previous_right.next = current.left
        #             previous_right = current.left
        #             queue.append(current.left)
        #
        #         if current.right:
        #             if previous_right:
        #                 previous_right.next = current.right
        #             previous_right = current.right
        #             queue.append(current.right)

        queue = [root]
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.pop(0)  # popleft

                if i < level_size - 1:
                    current.next = queue[0]

                if current.left:
                    queue.append(current.left)

                if current.right:
                    queue.append(current.right)
        return root


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 4, 5, None, 7], [1, "#", 2, 3, "#", 4, 5, 7, "#"]),
        ([1, 2, 3, 4, None, None, 5], [1, "#", 2, 3, "#", 4, 5, "#"]),
        ([3, 9, 20, None, None, 15, 7], [3, "#", 9, 20, "#", 15, 7, "#"]),
        ([], []),
    ]:
        root = Node.from_list(data[0])
        want = data[1]

        result = s.connect(root)
        got = result.to_list() if result else []

        # if result:
        #     result.print()
        #     print(result.to_list())
        #     print()

        assert want == got, f"\nin={data[0]}" f"\nwant={data[1]}" f"\ngot ={got}"
