"""
1. The solution is using stack.
2. If it is a number push it to stack, else if it is any operator then, we will have to pop the 2 number n1 and n2
3. the top 2 numbers will be popped, n2 being the first and n1 being 2nd, we perform with the operators either by a switch/match case or if else
4. append the result back to stack
5. at last return stack[0] as the output.

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                n1 = int(stack.pop())
                n2 = int(stack.pop())

                if token == "+":
                    stack.append(n2 + n1)
                elif token == "-":
                    stack.append(n2 - n1)
                elif token == "*":
                    stack.append(n2 * n1)
                elif token == "/":
                    stack.append(int(n2 / n1))
            else:
                stack.append(int(token))

        return stack[0]
