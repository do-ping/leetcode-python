from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linkedlist(arr: List[int], last_points_to: int = -1) -> Optional[ListNode]:
    """
    Make a linked list from a given list.
    Optionally, if the linked list is cyclic, specify the index of a list element to which the tail is pointing to.
    :param arr: input list
    :param last_points_to: index of an element the tail to be pointing to (cyclic list). -1 by default (non-cyclic)
    :return: head of the created linked list or None if input array is empty
    """
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


def stringify_linkedlist(head: ListNode, cyclic: bool = False, separator="->") -> str:
    """
    Print given linked list elements, separated by (optionally) given separator.
    If the linked list is cyclic, set cyclic to True.
    :param head:
    :param cyclic:
    :param separator:
    """
    if not head:
        return ""

    s = []
    current = head
    if cyclic:
        seen = set()
        current = head
        while current:
            if current in seen:
                s.append(f" ~{current.val}...")
                break

            seen.add(current)
            s.append(current.val)

            current = current.next
    else:
        while current:
            s.append(current.val)
            current = current.next

    return separator.join((str(e) for e in s))


def compare_linkedlist(l1: Optional[ListNode], l2: Optional[ListNode]) -> bool:
    if not l1 and not l2:
        return True
    if not l1 or not l2:
        return False

    current1 = l1
    current2 = l2

    while current1 and current2:
        if current1.val != current2.val:
            return False
        current1 = current1.next
        current2 = current2.next

    return (not current1) and (not current2)
