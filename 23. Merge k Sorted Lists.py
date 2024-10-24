# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def linked_to_arr(self, node):
        arr = []
        while node:
            arr.append(node.val)
            node = node.next
        return arr
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = []
        for i in lists:
            k+=self.linked_to_arr(i)
        k.sort()

        def insert(root, item): 
            temp = ListNode(0) 
            temp.val = item 
            temp.next = root 
            root = temp
            return root

        def arrayToList(arr, n): 
            root = None 
            for i in range(n - 1, -1, -1): 
                root = insert(root, arr[i])
            return root 
        n = len(k) 
        root = arrayToList(k, n); 
        return root
