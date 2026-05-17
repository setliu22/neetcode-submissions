class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        # Dictionary stores:
        # key -> reference to the whole linked list node
        self.cache = {}

        # Dummy nodes:
        # left side = least recently used
        # right side = most recently used
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Start with an empty linked list:
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        # Remove node from its current position in the linked list.
        # Before:
        # prev_node <-> node <-> next_node
        #
        # After:
        # prev_node <-> next_node
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def insert(self, node):
        # Insert node right before self.right.
        # This makes node the most recently used.
        #
        # MUTATION nuance:
        # prev_node and next_node are references to existing node objects.
        # So when we do prev_node.next = node or next_node.prev = node,
        # we are mutating those actual objects, not creating copies.
        #
        # Since next_node = self.right, changing next_node.prev
        # also changes self.right.prev, because they refer to the same object.
        #
        # But doing next_node = node would only reassign the local variable
        # and would NOT change self.right.

        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:
        # So yes, the linked list updates because Python variables store 
        # references to objects, and assigning to .prev or .next MUTATES 
        # the object.
        if key not in self.cache:
            return -1

        # Dictionary gives us the actual node immediately.
        node = self.cache[key]

        # Since this key was just used,
        # move it to the most recently used side.
        # This is how to simulate that (same operation as remove, insert)
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        # If the key already exists, remove its old node from the list.
        if key in self.cache:
            self.remove(self.cache[key])

        # Create a new node for this key-value pair.
        node = Node(key, value)

        # Dictionary stores a reference to the whole node.
        self.cache[key] = node

        # Put the node on the most recently used side.
        self.insert(node)

        # If we are over capacity, remove the least recently used node.
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]