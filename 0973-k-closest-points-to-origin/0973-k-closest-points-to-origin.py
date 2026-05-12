"""
1. distance fun to return the distance, a ans list
2. for point in points, find the distance and append the distance and point in the list 
3. sort based on distance, sorts based of first element by default
4. result list, where we append k points from the ans list and return the result

time comp:- O(nlogn) :- to sort, building list is only n
space comp:- O(n)
"""
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        ans = []

        def distance(x,y):
            return math.sqrt((x)**2+(y)**2)

        for point in points:
            dis = distance(point[0], point[1])
            ans.append((dis, point)) #python automatically sorts based on first element

        ans.sort()
        # or ans.sort(key=lamda x: x[1]) -> sort based on 2nd element
        result = []
        for _ in range(k):
            result.append(ans[_][1])
        
        return result