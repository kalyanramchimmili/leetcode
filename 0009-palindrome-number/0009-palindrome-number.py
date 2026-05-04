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