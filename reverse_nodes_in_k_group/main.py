from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    create_linkedlist,
    stringify_linkedlist,
    compare_linkedlist,
)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        # count the nodes
        temp = head
        node_count = 0
        while temp:
            node_count += 1
            temp = temp.next
            # enough for this reversal
            if node_count == k:
                break

        # tail length is less than k
        if node_count < k:
            return head

        # reverse k nodes
        currently_reversed = k
        current = head
        previous = None
        next_node = None
        while current and currently_reversed > 0:
            currently_reversed -= 1
            next_node = current.next
            current.next, previous, current = previous, current, next_node

        # connect the remaining nodes if any
        if next_node:
            # head.next = self.reverse_n_nodes(next_node, k)
            head.next = self.reverseKGroup(next_node, k)

        return previous


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [4, 3, 2, 1, 8, 7, 6, 5]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
        ([1, 2, 3, 4], 1, [1, 2, 3, 4]),
    ]:
        head = create_linkedlist(data[0])
        k = data[1]
        want = create_linkedlist(data[2])
        got = s.reverseKGroup(head, k)

        print(
            f"input={stringify_linkedlist(create_linkedlist(data[0]))}, k={k}\n"
            f"want={stringify_linkedlist(want)}\n"
            f"got ={stringify_linkedlist(got)}"
        )

        assert compare_linkedlist(want, got)
