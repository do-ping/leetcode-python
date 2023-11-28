# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


def _make_linked_list(arr: List[int], last_points_to: int) -> Optional[ListNode]:
    if not arr:
        return None

    head: ListNode = None
    current: ListNode = None
    cycle_item: ListNode = None

    for n, item in enumerate(arr):
        if n == 0:
            head = ListNode(item)
            current = head
        else:
            current.next = ListNode(item)
            current = current.next

        if 0 <= last_points_to == n:
            cycle_item = current

    if cycle_item:
        current.next = cycle_item

    return head


def _print_linkedlist(head: ListNode):
    s = ""
    current = head
    while current:
        s += str(current.val)
        current = current.next
        if current:
            s += " -> "
        else:
            break
    print(s)


if __name__ == "__main__":
    s = Solution()
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
        ll = _make_linked_list(input_[0], input_[1])
        expected = input_[2]
        result = s.hasCycle(ll)
        assert (
            expected == result
        ), f"ll={input_[0]}, cycle_n={input_[1]}, expected={expected}, got={result}"
