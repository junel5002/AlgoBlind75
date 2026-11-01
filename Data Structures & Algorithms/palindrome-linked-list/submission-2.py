# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        """Approach:
        1. Traverse the linked list and store each node's value in an      array.
        2. Initialize two pointers at the beginning and end of the array.
        3. Compare the values at both pointers.
        4. If they differ, return False.
        5. Otherwise, move both pointers inward.
        6. If all pairs match, return True.
        """

        array = []

        cur = head

        while cur is not None:
            array.append(cur.val)
            cur = cur.next

            l, r  = 0, len(array) - 1

        while l < r:
            if array[l] != array[r]:
                return False
            l, r = l + 1, r - 1

        return True