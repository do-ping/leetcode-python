from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    create_linkedlist,
    stringify_linkedlist,
    compare_linkedlist,
)


class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    #     if not head or n == 0:
    #         return head
    #
    #     if not head.next and n == 1:
    #         return None
    #
    #     count = 0
    #     current = head
    #     while current:
    #         count += 1
    #         current = current.next
    #
    #     node_before_removal = count - n
    #     current = head.next if node_before_removal == 0 else head
    #     dummy = ListNode(0)
    #     dummy.next = current
    #     for i in range(1, count):
    #         if i == node_before_removal:
    #             current.next = current.next.next
    #         current = current.next
    #
    #     return dummy.next

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n == 0:
            return head

        if not head.next and n == 1:
            return None

        if not head.next.next:
            if n == 1:
                head.next = None
            else:
                head = head.next
            return head

        fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next

        slow = head
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2, 3, 4, 5, 6], 0, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2, 3], 1, [1, 2]),
        ([1, 2, 3], 2, [1, 3]),
    ]:
        l = data[0]
        remove = data[1]
        want = data[2]
        ll = create_linkedlist(l)
        got = s.removeNthFromEnd(ll, remove)
        #
        # print(
        #     f"input={l}\n"
        #     f"remove node={remove}\n"
        #     f"want={data[2]}\n"
        #     f"got ={stringify_linkedlist(got)}"
        # )
        want_l = create_linkedlist(want)
        assert compare_linkedlist(want_l, got), (
            f"\ninput={l}\n"
            f"remove node={remove}\n"
            f"want={stringify_linkedlist(want_l)}\n"
            f"got ={stringify_linkedlist(got)}"
        )
