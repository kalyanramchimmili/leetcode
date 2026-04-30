"""
This is quite simple
1. the std reversal of number, get the last digit out, mul the prev rev into 10 and add the rem we get until the orginal number becomes 0
2. for neg numbers, have a flag, mul with -1 first and after reversing mul with -1 again as per que
3. if the reversal overflows return 0 checking with the  if reverse < -2**31 or reverse > (2**31 - 1):
"""
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


        