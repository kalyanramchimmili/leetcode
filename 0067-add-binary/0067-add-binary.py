"""
1. if sum is 2 or 3 carry is 1, else carry is 0
2. traverse from last, i or j >= 0 or if carry is at last, count the sum, if sum is even, append 0 else append 1
3. carry would be floor operator for 0

time comp:- O(n), n being max(i+1, j+1)
space comp:- O(n)
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a)-1
        j = len(b)-1
        ans = []
        carry = 0

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1
            
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            ans.append(str(total%2))
            carry = total//2
        
        return "".join(ans[::-1])
