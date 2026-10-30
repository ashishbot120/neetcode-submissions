from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for src,dst in tickets:
            graph[src].append(dst)
        for src in graph:
            graph[src].sort(reverse = True)
        result = []
        def dfs(airport):
            while graph[airport]:
                newairport = graph[airport].pop()
                dfs(newairport)
            result.append(airport)
        dfs("JFK")
        return result[::-1]