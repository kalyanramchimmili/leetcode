"""
1. 2 stack problem, while appending intially I appened to both a and b and sorted it after each append, but that was inefficent, hence the logic now only stores strictly small or equal values of prev value to stack B
2. Intially when stack si empty append the val else check the condition.
3. Pop would return the pop from stackA if the top of stackB match with popped element of A then pop from B also to eliminate the prev min there was.
4. top would return stackA[-1]
5 min woudl return stakcB[-1]

Time comp:- O(1) for all the cases
space comp:- O(2n), assuming n no of elements in stack arranged in decreasing order.
"""
class MinStack:

    def __init__(self):
        self.stackA = []
        self.stackB = []
        

    def push(self, val: int) -> None:
        self.stackA.append(val)
        if len(self.stackB) == 0:
            self.stackB.append(val)

        elif self.stackB[-1] >= val:
            self.stackB.append(val)

    def pop(self) -> None:
        val = self.stackA.pop()
        if val == self.stackB[-1]:
            self.stackB.pop()

    def top(self) -> int:
        return self.stackA[-1]

    def getMin(self) -> int:
        return self.stackB[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()