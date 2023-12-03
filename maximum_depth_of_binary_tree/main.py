from typing import Optional

from helper_functions.tree import TreeNode


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
