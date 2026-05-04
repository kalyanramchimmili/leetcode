class Solution:
    def intToRoman(self, num: int) -> str:
        conv_map = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
   
        ans = ""
        for value, sym in conv_map:
            if num != 0:
                temp = num // value
                ans += sym*temp
                num %= value
            else:
                break
        
        return ans

       