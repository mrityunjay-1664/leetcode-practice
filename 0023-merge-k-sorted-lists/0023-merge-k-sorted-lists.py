import heapq
from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        heap = []
        
        # Initialize the heap with the first node of each non-empty list
        for i, node in enumerate(lists):
            if node:
                # Store a tuple of (value, index, node)
                # The index prevents heapq from comparing ListNode objects if values are equal
                heapq.heappush(heap, (node.val, i, node))
                
        dummy = ListNode(0)
        curr = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # If the current list has a next node, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next
        