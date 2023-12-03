from typing import Optional

from helper_functions.tree import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

        # stack = deque([(p, q)])
        # while stack:
        #     current_p, current_q = stack.pop()
        #
        #     if not current_p and not current_q:
        #         continue
        #
        #     if not (current_p and current_q):
        #         return False
        #
        #     if current_p.val != current_q.val:
        #         return False
        #
        #     stack.append((current_p.left, current_q.left))
        #     stack.append((current_p.right, current_q.right))
        #
        # return not stack


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [2], False),
        ([1], [], False),
        (
            [1, 2, 3, 4, 5, None, 6, None, None, None, None, None, None, None, 7],
            [1, 2, 3, 4, 5, None, 6, None, None, None, None, None, None, None, 7],
            True,
        ),
        ([1, 2, 3, 4, 5, 6, None], [1, 2, 3, 4, 5, None, 6], False),
    ]:
        p_values = data[0]
        q_values = data[1]

        p = TreeNode.from_list(p_values)
        q = TreeNode.from_list(q_values)
        want = data[2]
        got = s.isSameTree(p, q)

        assert got == want, f"p={p} q={q} want={want} got ={got}"
