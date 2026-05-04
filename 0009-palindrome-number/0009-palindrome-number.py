"""
It was similar to reverse.
1. As per problem description, negative numbers with sign are not palindromes as the sign comes post the int after reversing it
2. 0-9 are all palindromes
3. was to rev a int with tmp variable and check if its a palindrome

time comp:- O(log10(x)) // number of digits in x
space comp:- o(1) //just 2 constants
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif 0 <= x <= 9:
            return True
        else:
            rev = 0
            tmp_x = x
            while x != 0:
                tmp = x % 10
                rev = rev * 10 + tmp
                x = int(x / 10)

            if rev == tmp_x:
                return True

        return False