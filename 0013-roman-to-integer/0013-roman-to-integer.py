"""
1. similar to previous problem, converting roman to int
2. list out dict as hashmap, iterate through the string 
3. to check for 4 and 9s case if next char is bigger than prev char it is either 4 or 9, hence subtract the present value and add next value
for eg:- 
IV :- sub 1 and add 5 so it results in 4
5. else add it to the ans int and return the ans

time comp:- o(n) -> no of char in str of len n
space comp:- o(1)
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        conv_map = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }
        ans = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and conv_map[s[i]] < conv_map[s[i+1]]:
                ans -= conv_map[s[i]]
            else:
                ans += conv_map[s[i]]
        return ans