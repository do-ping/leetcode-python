# Definition for singly-linked list.
from typing import Optional, List

from helper_functions.linked_list import (
    ListNode,
    make_linked_list,
    linkedlist_to_string,
)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True

            slow = slow.next
            fast = fast.next.next

        return False


if __name__ == "__main__":
    s = Solution()
    intput_: tuple[list[int], int, bool]
    for input_ in [
        ([3, 2, 0, -4], 1, True),
        ([1, 2], 0, True),
        ([1], -1, False),
        ([1, 2, 3, 4, -5, 7, 11], 3, True),
        ([1, 2, 3], 2, True),
        ([1, 2, 3, 4], 0, True),
        (
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            11,
            True,
        ),
        ([1, 2], -1, False),
        (
            [
                -21,
                10,
                17,
                8,
                4,
                26,
                5,
                35,
                33,
                -7,
                -16,
                27,
                -12,
                6,
                29,
                -12,
                5,
                9,
                20,
                14,
                14,
                2,
                13,
                -24,
                21,
                23,
                -21,
                5,
            ],
            -1,
            False,
        ),
    ]:
        l_ = input_[0]
        cycle: int = input_[1]
        expected = input_[2]

        ll = make_linked_list(l_, cycle)

        ll_str = linkedlist_to_string(ll, True if cycle >= 0 else False)
        result = s.hasCycle(ll)

        print(f"tail_to={cycle} input={ll_str}\nexpected={expected}, actual={result}")
        assert (
            expected == result
        ), f"ll={input_[0]}, cycle_n={input_[1]}, expected={expected}, got={result}"
