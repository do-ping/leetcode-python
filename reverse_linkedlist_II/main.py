from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    create_linkedlist,
    stringify_linkedlist,
    compare_linkedlist,
)


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        next_node = None

        for _ in range(right - left + 1):
            temp = current.next
            current.next = next_node
            next_node = current
            current = temp

        prev.next.next = current
        prev.next = next_node

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
        ([1, 2, 3, 8, 9, 10, 11, 12], 4, 8, [1, 2, 3, 12, 11, 10, 9, 8]),
    ]:
        l = data[0]
        left = data[1]
        right = data[2]
        want = create_linkedlist(data[3])
        ll = create_linkedlist(l)
        got = s.reverseBetween(ll, left, right)

        print(
            f"input={stringify_linkedlist(ll)}\n"
            f"left={left} right={right}\n"
            f"want={stringify_linkedlist(want)}\n"
            f"got={stringify_linkedlist(got)}"
        )

        assert compare_linkedlist(want, got)
