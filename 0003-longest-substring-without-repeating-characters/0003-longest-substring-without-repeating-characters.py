"""
1. Learnt sliding window technique for this approach.
2. we have i = 0 kept at starting of the string and we have j iterating from 0 to end of string.
3. if j is a unique element (we have choosen set to store seen or not, as sets dont allow duplicates).
4. if j is seen in set then the pattern is broken, start shrinking the window, by increasing i until it removes the seen element from set.
5. if not then add it to the list and compute max len of the list and return the highest max len recorded.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        char_set = set()
        max_len = 0

        for j in range(len(s)):
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1
            
            char_set.add(s[j])
            max_len = max(max_len, j-i+1)
        
        return max_len
        
                