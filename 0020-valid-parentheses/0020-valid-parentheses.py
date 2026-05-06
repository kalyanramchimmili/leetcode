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
        if not stack:
            return True
        else:
            return False
