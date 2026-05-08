"""
1. 2 stacks for a queue, to push, push it to stack 1
2. to pop, push all elements of stack 1 to stack 2, pop the stack 2, store the values, and shift all the elements back from stack 2 to stack 1, and return the value
3. for peek return stack[0] the first element in stack
4. for empty, check the size of stack 1, return true or false

time comp:- O(n)
space:- O(n)
"""
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 =[]

    def push(self, x: int) -> None:
        self.stack1.append(x)
        

    def pop(self) -> int:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        popped_item = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())
        
        return popped_item
        

    def peek(self) -> int:
        return self.stack1[0]
        

    def empty(self) -> bool:
        if len(self.stack1) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()