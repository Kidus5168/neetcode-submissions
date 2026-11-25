# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        r = []

        while list1:
            r.append(list1.val)
            list1 = list1.next
        while list2:
            r.append(list2.val)
            list2 = list2.next
        r.sort()
        re = ListNode(-1)
        cur = re
        for i in range(len(r)):
            newnode = ListNode(r[i])
            cur.next = newnode
            cur = cur.next
        return re.next




        