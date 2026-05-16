"""
1. I thought Binary tree level order was bfs, but no, although it acts like one, today I learnt BFS via queue
2. start with level 0, one matrix called distance, amrked with -1 rep not visited
3. intialize a queue with left and right pointers
4. iterate the orginal matrix, to find all 0s, if 0 mark the dis as 0 in dis matrix and append the r,c values to queue.
5. now if left < right in queue, pop the left element, from there we shld traverse all 4 direction.
6. calculate netrow and netcol value nr,nc. Checking boundaries for matrix, if the matrix element is unvisited which is -1 i.e the orginal value was 1, then 1 was found in 1 level from the orignal 0, so replace its values in dis matrix as level+1 and append it to stack.
7. further, it keeps iterating on level to updated the dis matrix, and return the distance matrix

Time comp:- O(m*n), where m and n are rows and col's.
space comp:- O(m*n) 
"""
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        lr = len(mat)
        lc = len(mat[0])
        level = 0
        dis = [[-1]*lc for _ in range(lr)]
        q = []
        left = 0
        right = 0

        for r in range(lr):
            for c in range(lc):
                if mat[r][c] == 0:
                    dis[r][c] = 0
                    q.append((r,c,level))
                    right += 1

        while left < right:
            r,c,level = q[left]
            left += 1
            distance =[[0,1],[0,-1],[1,0],[-1,0]]
            for dr,dc in distance:
                nr  = r+dr
                nc = c+dc
                if 0 <= nr < lr and 0 <= nc < lc and dis[nr][nc] == -1:
                    dis[nr][nc] = level + 1
                    q.append((nr,nc,level+1))
                    right += 1

        
        return dis