"""
1. map a dict whichs serves as hash map, instead of handling 4 and 9's map those at as well
2. from first value and its symbol, first do a floor of num and value to get how many times of value is the number and add the symbol that many times to ans string
3. Modify the num by over-writing it with reminder and continue until it is not 0

time comp:- o(1) // runs 13 times (13 entires in dict)
space comp:- o(1)
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        conv_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
   
        ans = ""
        for value, sym in conv_map:
            if num != 0:
                temp = num // value
                ans += sym*temp
                num %= value #similar to num = num - (temp*value)
            else:
                break
        
        return ans

       