"""
1. check for leading whitestrips, if the ans string is empty then, continuie if not break
2. check for signs plus and neg, if the string ans is empty add else break
3. check if we encounter any non-digit, then break
4. else other numbers we add to char i.e., numbers
5. Check if ans is empty is yes return 0 else convert it into a number
6. check if it is less than 2^31-1 or greater than -2^31 then return the rounded of values
7. return the ans otherwise
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        for char in s:
            if char == " ":
                if ans == "":
                    continue
                else:
                    break
            elif char == "-" or char == "+":
                if ans != "":
                    break
                else:
                    ans += char
            elif not char.isdigit():
                break
            else:
                ans += char

        if ans == "" or ans == "+" or ans == "-":
            return 0

        res = int(ans)
        if res > (2**31)-1 :
            return (2**31)-1
        elif res < (-2**31):
            return (-2**31)
        else:
            return res