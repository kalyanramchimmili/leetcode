"""
1. sort the 2 strings using sorted which would split the string into list and sort them based on ascii
2. use join to form string
3. sort both s and t compare them and return the output

time comp:- o(2nlogn) assuming n is len of t and n
space comp:- o(2n)
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
            
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        return (sorted_s == sorted_t)