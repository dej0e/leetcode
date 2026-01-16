"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        old_newnode_map = {None: None}
        curr_old = head
        curr_new = None
        new_head = None
        while curr_old:
            new_node = Node(x=curr_old.val)
            curr_old_next = curr_old.next
            curr_old_random = curr_old.random
            if curr_old_random in old_newnode_map:
                new_node.random = old_newnode_map.get(curr_old_random)

            if curr_new:
                curr_new.next = new_node
            else:
                new_head = new_node
            curr_new = new_node
            old_newnode_map[curr_old] = new_node
            curr_old = curr_old.next

        curr_old = head
        curr_new = new_head
        while curr_old:
            curr_new.random = old_newnode_map.get(curr_old.random) 
            curr_old = curr_old.next
            curr_new = curr_new.next

        return new_head
