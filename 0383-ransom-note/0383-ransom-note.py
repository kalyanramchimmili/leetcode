"""
1. intialize count var and count all char in magazine
2. check in ransomNote if there is any char not in count or if its frew has got to 0, but the char exists in ransomNote, return false
3. dec the count of the ch in count other wise 
4. if loop completes, ransomNote can be made form magazine, return true

time comp:- O(N), n = len(ransomNote)
space comp:- O(N)
"""
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        count = {}
        
        for char in magazine:
            count[char] = count.get(char,0)+1
        
        for ch in ransomNote:
            if ch not in count or count[ch] == 0:
                return False
            
            count[ch] -= 1
        
        return True
        