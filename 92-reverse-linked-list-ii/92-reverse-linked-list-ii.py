# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev, cur = dummy, head
        for _ in range(left - 1):
            prev = cur
            cur = cur.next
        left_prev, left_node = prev, cur
        
        prev, cur = None, left_node
        for _ in range(right - left + 1):
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        right_node, right_next = prev, cur
        
        left_prev.next = right_node
        left_node.next = right_next
        
        return dummy.next