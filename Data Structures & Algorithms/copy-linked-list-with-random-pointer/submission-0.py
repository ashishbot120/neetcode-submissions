"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        deep = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            deep[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = deep[curr]
            copy.next = deep.get(curr.next)
            copy.random = deep.get(curr.random)
            curr = curr.next
        return deep[head]