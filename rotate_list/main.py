from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    create_linkedlist,
    compare_linkedlist,
    stringify_linkedlist,
)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        nodes_n = 2  # first and last
        first = head
        switch_n = -1  # how many times should we actually make a switch
        for loop_n in range(k):
            current = first
            while current.next.next:
                if loop_n == 0:  # count nodes only once
                    nodes_n += 1
                current = current.next

            if loop_n == 0:  # calculate number of switches only once
                switch_n = k % nodes_n

            if switch_n == 0:  # no changes needed
                first = head
                break

            if loop_n >= switch_n:
                break

            first, current.next, first.next = current.next, None, first

        return first


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1], 100, [1]),
        ([9, 10], 5, [10, 9]),
        ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
        ([0, 1, 2], 4, [2, 0, 1]),
        ([1, 2, 3], 300, [1, 2, 3]),
        ([1, 2, 3], 299, [2, 3, 1]),
    ]:
        ll = create_linkedlist(data[0])
        k = data[1]
        want = create_linkedlist(data[2])
        got = s.rotateRight(create_linkedlist(data[0]), k)

        assert compare_linkedlist(want, got), (
            f"\ninput={stringify_linkedlist(ll)}\n"
            f"want={stringify_linkedlist(want)}\n"
            f"got ={stringify_linkedlist(got)}"
        )
