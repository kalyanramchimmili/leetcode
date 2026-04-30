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