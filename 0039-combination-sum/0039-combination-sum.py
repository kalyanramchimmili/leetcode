class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        res = []

        def solve(start, remaining, path):
            if remaining == 0:
                res.append(list(path))
                return

            if remaining < 0:
                return

            for i in range(start, l):
                path.append(candidates[i])
                solve(i, remaining - candidates[i], path)
                path.pop()

        solve(0, target, [])
        return res
