# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s_list = None
        tail = None
        s = 0
        head = head.next
        while head:
            if head.val!=0:
                s+=head.val
            else:
                if s!=0:
                    new_node = ListNode(s)
                    if not s_list:
                        s_list = new_node
                        tail = new_node
                    else:
                        tail.next = new_node
                        tail = tail.next
                s = 0
            head = head.next
        return s_list
