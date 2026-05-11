"""
1. intiate a hashmap to count all values
2. for val in count.values, if val is even then add to ans, if odd then add val-1 to ans.
3. also mark odd flag, if odd flag is true add 1 to ans and return
4. the approach is for "abccccdd" -> count all even count 4 c's and 2 d's. and one odd to add in between.
5. so count all even val and one add val to ans and return

Time comp :- O(N)
space comp:- O(N)
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        ans = 0
        odd = False
        for char in s:
            count[char] = count.get(char,0)+1
        
        for val in count.values():
            if val%2 == 0:
                ans += val
            else:
                ans += val-1
                odd = True
        
        if odd:
            ans += 1
        
        return ans
