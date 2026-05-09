"""
1. this one was pretty hard to understand, but it was simple after that via recurrsion
2. capture the orignal value, if the value is already same as colour, nothing to change, return the image
3. we have fill fun within, which checks the boundary for rows and columns, if the new index is equal to orignal value or not, if not or out of index return simply.
4. if not then change it to colour, do the same thing for up down, right left 
5. start the fun by first calling the given index and return the image after it

time comp:- O(m*n)
space comp:- O(m*n)
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        orginal_value = image[sr][sc]

        if orginal_value == color:
            return image

        def fill(r, c):
            if r < 0 or c < 0 or r >= len(image) or c >= len(image[0]) or (image[r][c] != orginal_value):
                return

            image[r][c] = color

            fill(r-1, c)
            fill(r+1, c)
            fill(r, c-1)
            fill(r, c+1)
        
        fill(sr,sc)
        return image

        




        
        