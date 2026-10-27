class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(1,len(edges)+1)}
        def dfs(node,target,visited):
            if node == target:
                return True
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    if dfs(i,target,visited):
                        return True
            return False
        for a,b in edges:
            visited = set()
            if dfs(a,b,visited):
                return [a,b]
            graph[a].append(b)
            graph[b].append(a)
        return []