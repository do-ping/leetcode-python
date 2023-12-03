from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @classmethod
    def from_list(cls, values: list[int | None]):
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

    def __repr__(self):
        left_repr = f", left={repr(self.left)}" if self.left else ""
        right_repr = f", right={repr(self.right)}" if self.right else ""
        return f"TreeNode({self.val}{left_repr}{right_repr})"


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_depth = 1
        stack = [(root, max_depth)]
        while stack:
            current, depth = stack.pop()

            max_depth = max(max_depth, depth)

            if current.left:
                stack.append((current.left, depth + 1))
            if current.right:
                stack.append((current.right, depth + 1))

        return max_depth


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([], 0),
        ([1], 1),
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([1, 2, 2, 3, 3, None, None, 4, None, None], 4),
    ]:
        tree_input = data[0]
        root = TreeNode.from_list(tree_input)
        want = data[1]
        got = s.maxDepth(root)

        assert got == want, f"tree={root} want={want} got ={got}"
