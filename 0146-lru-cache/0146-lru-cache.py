class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoublyLinkedList:

    def __init__(self):
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count = 0

    def insert(self, node : Node):
        temp = self.tail.prev
        node.next = self.tail
        node.prev = temp
        temp.next = node
        self.tail.prev = node
        
        self.count+=1

    def delete(self, node: Node):
        node.prev.next= node.next
        node.next.prev = node.prev

        self.count-=1

class LRUCache:

    def __init__(self, capacity: int):
        self.doublyLL = DoublyLinkedList()
        self.capacity = capacity
        self.dictionary = {}
        

    def get(self, key: int) -> int:
        if key in self.dictionary:
            node = self.dictionary[key]
                
            self.doublyLL.delete(node)
            self.doublyLL.insert(node)
            
            return node.val

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)


        if self.capacity == self.doublyLL.count:
            if key not in self.dictionary:
                del_node = self.doublyLL.head.next
                self.doublyLL.delete(del_node)
                self.dictionary.pop(del_node.key)
            

        if key in self.dictionary: 
            self.doublyLL.delete(self.dictionary[key])   
               
        self.doublyLL.insert(node)
        self.dictionary[key] = node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)