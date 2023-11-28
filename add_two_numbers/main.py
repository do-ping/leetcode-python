# Definition for singly-linked list.
from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    make_linked_list,
    linkedlist_to_string,
    linked_lists_equal,
)


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        result = ListNode(0)
        current = result
        carry = 0
        while l1 or l2:
            current_sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry

            current.next = ListNode(current_sum % 10)
            current = current.next

            carry = current_sum // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            current.next = ListNode(carry)

        return result.next


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]:
        arr1 = make_linked_list(data[0])
        arr2 = make_linked_list(data[1])
        expected = make_linked_list(data[2])

        actual = s.addTwoNumbers(arr1, arr2)

        print(
            f"l1={linkedlist_to_string(arr1)}\nl2={linkedlist_to_string(arr2)}\nwanted="
            f"{linkedlist_to_string(expected)}\nresult={linkedlist_to_string(actual)}"
        )
        assert linked_lists_equal(expected, actual)
