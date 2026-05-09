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

        




        
        