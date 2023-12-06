from typing import Optional

from helper_functions.tree import TreeNode, compare_tree


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return

        current = root
        while current:
            if current.left:
                temp = current.right
                current.right = current.left
                current.left = None

                rightmost = current.right
                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = temp

            current = current.right


if __name__ == "__main__":
    s = Solution()
    for data in [
        (
            [1, 2, 5, 3, 4, None, 6],
            [1, None, 2, None, 3, None, 4, None, 5, None, 6],
        ),
        (
            [1, None, 2, None, 3, None, 4, None, 5, None, 6],
            [1, None, 2, None, 3, None, 4, None, 5, None, 6],
        ),
        (
            [1, 2, None, 3, None, 4, None, 5, None, 6, None],
            [1, None, 2, None, 3, None, 4, None, 5, None, 6],
        ),
        ([], []),
        ([0], [0]),
    ]:
        tree = TreeNode.from_list(data[0])
        want = TreeNode.from_list(data[1])

        s.flatten(tree)

        assert compare_tree(want, tree), (
            f"\nin={data[0]}" f"\nwant ={want}" f"\ngot={tree}"
        )
