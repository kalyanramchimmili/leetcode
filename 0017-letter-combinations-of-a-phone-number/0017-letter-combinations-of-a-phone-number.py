"""
1. map out the numbers to letters, similar to int to roman problem
2. make a list of all the group of numbers based on lists i.e., ans_list
3. using something called itertools.product which multiples each list element with other list element to return all possible values -> combinations
4. the prob here is combinations spits out ("a" , "d"), to convert into "ad", use "".join for all combination groups inside combinations and return the value

itertools.product is a new thing for me in python, haven't used it before

time comp:- O(3^6 * 4^2 * n), n being size of string -> O(4^n * n)
Space comp:- O(4^n * n) as we are building ans_list
"""
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        conv_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        ans_list = []
        for d in digits:
            ans_list.append(conv_map[d])
        
        combinations = itertools.product(*ans_list)
        return ["".join(comb) for comb in combinations]