from typing import List, Optional

from helper_functions.tree import TreeNode, compare_tree


class Solution:
    # preorder = Root-Left-Right, root -> traverse left subtree -> traverse right
    # inorder = Left-Root-Right, left -> visit root -> traverse right
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        inorder_root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:inorder_root_index])
        root.right = self.buildTree(preorder, inorder[inorder_root_index + 1 :])

        return root


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7], [3, 9, 20, None, None, 15, 7]),
        (
            [3, 9, 20, 15, 7],
            [7, 15, 20, 9, 3],
            [3, 9, None, 20, None, 15, None, 7, None],
        ),
        (
            [3, 9, 20, 15, 7],
            [3, 9, 20, 15, 7],
            [3, None, 9, None, 20, None, 15, None, 7],
        ),
        ([-1], [-1], [-1]),
    ]:
        preorder = data[0]
        inorder = data[1]
        want = TreeNode.from_list(data[2])

        got = s.buildTree(preorder, inorder)

        assert compare_tree(want, got), (
            f"\ninorder={inorder}"
            f"\npreorder={preorder}"
            f"\nwant={want}"
            f"\ngot={got}"
        )
