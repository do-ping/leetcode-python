from typing import Optional

from helper_functions.linked_list import (
    ListNode,
    create_linkedlist,
    stringify_linkedlist,
    compare_linkedlist,
)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        # In-place: 1ms slower, same memory usage, and harder for your brain
        # if list1.val > list2.val:
        #     list1, list2 = list2, list1
        #
        # result = list1
        #
        # while list1 and list2:
        #     while list1.next and list1.next.val < list2.val:
        #         list1 = list1.next
        #
        #     temp = list1.next
        #     list1.next = list2
        #     list1 = list2
        #     list2 = temp
        #
        # return result
        result = ListNode(0)
        current = result

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        current.next = list1 or list2

        return result.next


if __name__ == "__main__":
    s = Solution()
    for data in [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([-22, 45, 67, 100], [-100, 44], [-100, -22, 44, 45, 67, 100]),
        ([-1, 1, 1, 1, 1], [0], [-1, 0, 1, 1, 1, 1]),
    ]:
        l1 = create_linkedlist(data[0])
        l2 = create_linkedlist(data[1])
        want = create_linkedlist(data[2])
        got = s.mergeTwoLists(l1, l2)

        print(
            f"l1  ={stringify_linkedlist(l1)}\n"
            f"l2  ={stringify_linkedlist(l2)}\n"
            f"want={stringify_linkedlist(want)}\n"
            f"got ={stringify_linkedlist(got)}\n"
        )

        assert compare_linkedlist(want, got)
