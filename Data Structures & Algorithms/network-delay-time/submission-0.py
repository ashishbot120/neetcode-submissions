import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for u,v,t in times:
            graph[u].append((v,t))
        dist = [float("inf")]*(n+1)
        dist[k] = 0
        heap = [(0,k)]
        while heap:
            time_travel,node = heapq.heappop(heap)
            if time_travel > dist[node]:
                continue
            for neighbour,new_travel in graph[node]:
                new_time = time_travel + new_travel
                if new_time < dist[neighbour]:
                    dist[neighbour] = new_time
                    heapq.heappush(heap,(new_time,neighbour))
        answer = max(dist[1:])

        return answer if answer != float("inf") else -1