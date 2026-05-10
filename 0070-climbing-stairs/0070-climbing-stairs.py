"""
1. Listing out till 5 
1 2 3 4 5
1 2 3 5 8
-> it is Fibonacci series starting from 1 and 2
2. Doing the recursive apporach, it gives TLE for n >= 44
3. Doing iterative apporach, n == 1 and 2 return n else for 3 to n, compute Fibonacci series and return the last sum.

time comp:- O(N)
space comp:- O(1)
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n==2:
            return n
        a = 1
        b = 2
        for i in range(3,n+1):
            a, b = b, a+b
        
        return b

        """return self.climbStairs(n-1)+self.climbStairs(n-2)"""