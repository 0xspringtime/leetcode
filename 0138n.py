# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    if not head:
        return None
    
    # Creating a dictionary to save the node mappings (old node -> new node)
    mappings = {}
    
    # Create new nodes for each node in original list
    node = head
    while node:
        mappings[node] = Node(node.val, None, None)
        node = node.next
    
    # Set up next and random pointers for the new nodes
    node = head
    while node:
        if node.next:
            mappings[node].next = mappings[node.next]
        if node.random:
            mappings[node].random = mappings[node.random]
        node = node.next
    
    return mappings[head]
#time O(n)
#space O(n)
