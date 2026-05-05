"""
1. common prefix, find the shortest string in the list
2. for loop of the shortest string len, we take the intial string to create a char_to_match
3. run other for loop of num of strings in the list, if all chars are same add it to ans, if it breaks return the current ans
4. by defaults its "", would like to solve the common substring, that would be more challenging.

time comp:- o(n x l) each string is visited as number of elements in the short string
space comp:- o(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        if not strs:
            return ans
        l = min([len(s) for s in strs])
        n = len(strs)

        for i in range(l):
            char_to_match = strs[0][i]
            for j in range(1,n):
                if strs[j][i] != char_to_match:
                    return ans
            
            ans += char_to_match
        return ans