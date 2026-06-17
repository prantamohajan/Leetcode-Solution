# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
          def pairSum(self, head: Optional[ListNode]) -> int:
           arr = []
           node = head
           while node:
                 arr.append(node.val)
                 node = node . next

                 n = len(arr)
                 max_sum  = 0
                 for i in range (n // 2 ):
                       twin_sum = arr[i] + arr [n-1-i]
                       max_sum = max(max_sum , twin_sum)
                       return max_sum
