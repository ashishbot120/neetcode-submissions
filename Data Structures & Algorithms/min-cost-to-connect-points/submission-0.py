class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mindist = [float('inf')] * n
        mindist[0] = 0
        visited = [False] * n
        totalCost = 0
        for _ in range(n):
            minCost = float('inf')
            curr = -1
            for i in range(n):
                if not visited[i] and mindist[i] < minCost:
                    minCost = mindist[i]
                    curr = i
            visited[curr] = True
            totalCost += minCost
            x1,y1 = points[curr]
            for j in range(n):
                if not visited[j]:
                    x2,y2 = points[j]
                    dist = abs(x1-x2)+abs(y1-y2)
                    mindist[j] = min(mindist[j],dist)
        return totalCost