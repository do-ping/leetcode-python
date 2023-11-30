from typing import Optional

from helper_functions.linked_list import (
    create_linkedlist,
    compare_linkedlist,
    stringify_linkedlist,
    ListNode,
)


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(next=head)
        current = dummy

        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                skip = current.next.val
                while current.next and current.next.val == skip:
                    current.next = current.next.next
            else:
                current = current.next

        return dummy.next


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
        ([1, 1, 1, 2, 3], [2, 3]),
        ([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6], []),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ]:
        ll = create_linkedlist(data[0])
        want = create_linkedlist(data[1])
        got = s.deleteDuplicates(create_linkedlist(data[0]))

        assert compare_linkedlist(want, got), (
            f"\ninput={stringify_linkedlist(ll)}\n"
            f"want={stringify_linkedlist(want)}\n"
            f"got ={stringify_linkedlist(got)}"
        )
