class Solution:

    def longestPalindrome(self, s: str) -> str:

        l1 = len(s)
        max_str = ""

        for i in range(l1):
            for left, right in [(i,i), (i,i+1)]:
                while left >= 0 and right < l1 and s[left]==s[right]:
                    if (right-left+1) > len(max_str):
                        max_str = s[left : right+1]
                    
                    left -= 1
                    right += 1
        return max_str



"""
class Solution:
    def __init__(self):
        self.max_len = 0
        self.longest_str = ""

    def longestPalindrome(self, s: str) -> str:
        ls = len(s)

        for i in range(0,ls):
            char_list = []
            for j in range (i,ls):
                char_list.append(s[j])
                if char_list == char_list[::-1]:
                    if len(char_list) > self.max_len:
                        self.max_len = len(char_list)
                        self.longest_str = "".join(char_list)

        return self.longest_str

"""