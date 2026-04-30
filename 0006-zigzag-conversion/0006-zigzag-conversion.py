class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_bucket = ["" for _ in range(numRows)]

        current_row = 0
        goingDown = True
        n = len(s)

        for i in range(n):
            row_bucket[current_row] += s[i]
            if goingDown:
                if current_row == numRows-1:
                    current_row -= 1
                    goingDown = False
                else:
                    current_row += 1
            else:
                if current_row > 0:
                    current_row -= 1
                else:
                    goingDown = True
                    current_row += 1

        return "".join(row_bucket)

                

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        if numRows == 1 or numRows > n:
            return s

        ans = [["" for _ in range(n)] for _ in range(numRows)]

        goingDown = True
        r = c = 0

        for char in s:
            ans[r][c] = char

            if goingDown:
                if r < numRows - 1:
                    r += 1
                else:
                    goingDown = False
                    r -= 1
                    c += 1
            else:
                if r > 0:
                    r -= 1
                    c += 1
                else:
                    goingDown = True
                    r += 1

        ans_str = ""

        for i in range(numRows):
            for j in range(n):
                if ans[i][j] != "":
                    ans_str += ans[i][j]

        return ans_str
"""