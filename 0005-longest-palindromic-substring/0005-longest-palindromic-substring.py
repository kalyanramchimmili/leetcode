"""
Old approach:-
1. Tried the brute force, starting from first char, add each char, check is that is a palindrome, if yes record the max len and the same for 2nd char and so on - the time comp was not the best O(n3), it gave me a time limit exceeded error

new approach:-
1. all palindromes have centre, one for loop starting from 0, we have left and right var intially set to 0, so def palindrome len is 1 ofc, then left -- and right ++. if it is a first element, left is out of bounds, so right will icrease by 1, hence i and i+1 in the range.
2. if left and right are equal, it is palindrome, check if it is greater than max len if yes, replace max str with the current palindrome s[left:right+1]
3. once done retuen the max_str

Time comp:- o(n2) - forloop is n and the expansion in worstcase is n steps.
Space comp:- o(1)
"""
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