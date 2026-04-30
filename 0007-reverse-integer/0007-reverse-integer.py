class Solution:
    def reverse(self, x: int) -> int:

        reverse = 0

        if x > 0:
            isneg = False
        else:
            isneg = True
            x = x * -1

        while x != 0:
            rem = x % 10
            reverse = reverse*10 + rem
            x = int(x/10)

        if isneg:
            reverse = reverse * -1

        if reverse < -2**31 or reverse > (2**31 - 1):
            return 0
        
        return reverse


        