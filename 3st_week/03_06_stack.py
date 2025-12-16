class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self,value): # 만약 stack.push(3) 했다고 치면,
        new_head = Node(value) # new_head -> [3]
        new_head.next = self.head # [3].next -> None
        self.head = new_head # self.head -> [3]

    def pop(self):
        deleted_head = self.head
        self.head = self.head.next
        return deleted_head

    def peek(self):
        return self.head.data

    def is_empty(self):
        return self.head is None

stack = Stack()

stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.push(10)
print(stack.peek())
stack.pop()
print(stack.peek())