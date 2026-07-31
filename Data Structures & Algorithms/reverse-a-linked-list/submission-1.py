# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next    #this is to save the next node as nxt
            curr.next = prev   #this line reverses the arrow
            prev = curr        #this moves the previous node forward
            curr = nxt         #this is to move the curr forward

        return prev

#NB: Note that in a linkedin list we do not reverse values, rather we reverse arrows