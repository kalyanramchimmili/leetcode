"""
1. Stack solution, if opening brackets push it in stack, if not check the closing brackets match with opening ones and stack is not empty, if so stack.pop

2. if any mismatch with brackets then return False, check if stack is empty at the end, if so pass true else false

time comp:- O(N)
space comp:- O(N)
"""
class Solution:
    def isValid(self, char: str) -> bool:
        stack = []
        for s in char:
            if s == "(" or s == "[" or s == "{":
                stack.append(s)
            else:
                if stack and (
                    (s == ")" and stack[-1] == "(")
                    or (s == "]" and stack[-1] == "[")
                    or (s == "}" and stack[-1] == "{")
                ):
                    stack.pop()
                else:
                    return False

        return not stack
