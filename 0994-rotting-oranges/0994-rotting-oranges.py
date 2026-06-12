"""
1. Similar to 01 matrix problem, it was distance here is time, both afre bfs, but this is mulit-soruce bfs pattern, the other one normal bfs.
2. Intialize a queue, if the orange is rotten append it to queue with intial level as 0 serving as time here.
3. if the ornage is fresh just count the fresh oranges, if no fresh oranges return 0 else continue.
4. Look through queue, first for all the first identified rotten oranges, all 4 dir of it, if exists then rotten it to, append it back with level+1 indicating +1 min, continue, also dec the fresh oranges count.
5. once the fun is completed, we record the highest level, if the fresh oranges count is 0 return level else -1, cause not all were reachable.

Time comp:- O(m*n), where m and n are rows and col's.
space comp:- O(m*n)
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        lr = len(grid)
        lc = len(grid[0])
        distance = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = []
        left = 0
        right = 0
        fresh_ora = 0
        level = 0
        for i in range(lr):
            for j in range(lc):
                if grid[i][j] == 2:
                    q.append((i, j, level))
                    right += 1
                elif grid[i][j] == 1:
                    fresh_ora += 1

        if not fresh_ora:
            return 0

        while left < right and fresh_ora:
            r, c, l = q[left]
            left += 1

            for dr, dc in distance:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < lr and 0 <= nc < lc and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, l + 1))
                    fresh_ora -= 1
                    right += 1
                    level = max(level, l + 1)

        if fresh_ora > 0:
            return -1
        else:
            return level
