from typing import Optional

from helper_functions.tree import TreeNode


class Solution:
    def _is_mirror(self, left, right) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (
            left.val == right.val
            and self._is_mirror(left.left, right.right)
            and self._is_mirror(left.right, right.left)
        )

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self._is_mirror(root, root)
        # if not root:
        #     return True
        #
        # queue = [root.left, root.right]
        # while queue:
        #     l = queue.pop(0)
        #     r = queue.pop(0)
        #
        #     if not l and not r:
        #         continue
        #
        #     if l is None or r is None or l.val != r.val:
        #         return False
        #
        #     queue.append(l.left)
        #     queue.append(r.right)
        #     queue.append(l.right)
        #     queue.append(r.left)
        #
        # return True


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([], True),
        ([1], True),
        ([1, 2, 3], False),
    ]:
        tree = TreeNode.from_list(data[0])
        want = data[1]

        got = s.isSymmetric(tree)

        assert got == want, f"tree={tree} want={want} got ={got}"
