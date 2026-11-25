# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def print_linked_list(self, head):
    #     curr = head
    #     while curr:
    #         print(curr.val, end=" -> ")
    #         curr = curr.next
    #     print("None")
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        res = []
        a = []
        curr = head
        while curr:
            i = curr.val
            res.append(i)
            curr = curr.next
        l = 0
        r = len(res)-1
        while l<r:
            a.append(res[l])
            a.append(res[r])
            l+=1
            r-=1
        if l == r:
             a.append(res[r])
        print(a)
        node = head              # keep head intact
        for val in a:
            node.val = val
            node = node.next
        
    


        