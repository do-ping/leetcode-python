from typing import Optional, List


class TreeNode:
    """
    Definition of a binary tree node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, values: List[Optional[int]]):
        """
        Creates a binary tree from given list of values and returns its root.
        :param values: list of integers or Nones
        :return:
        """
        if not values:
            return

        root = cls(values[0])
        queue = [root]
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

    def __repr__(self) -> str:
        left_repr = f", left={repr(self.left)}" if self.left else ""
        right_repr = f", right={repr(self.right)}" if self.right else ""
        return f"TreeNode({self.val}{left_repr}{right_repr})"
