class Node:
    def __init__(self, key = 0, val = 0):
        self.key = key

        self.val = val

        self.next = None

        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = Node()
        self.right = Node()

        self.right.prev = self.left
        self.left.next = self.right
    
    def delete(self, node: Node) -> None:

        previousnode = node.prev
        nextnode = node.next
        previousnode.next = nextnode
        nextnode.prev = previousnode

    def insert(self, node: Node) -> None:

        # insert at the end
        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.delete(node)
        self.insert(node)

        return self.cache[key].val        

    def put(self, key: int, value: int) -> None:
        # update existing
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.delete(node)
            self.insert(node)
        else:
        # if full, evict latest and remove key from dict
            if len(self.cache) == self.capacity:
                least_recent = self.left.next
                self.delete(least_recent)
                del self.cache[least_recent.key]
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
        
