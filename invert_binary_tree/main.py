from typing import Optional

from helper_functions.tree import TreeNode, compare_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ]:
        root = TreeNode.from_list(data[0])
        want = TreeNode.from_list(data[1])
        got = s.invertTree(TreeNode.from_list(data[0]))

        assert compare_tree(want, got), f"\ntree={root}\nwant={want}\ngot ={got}"
