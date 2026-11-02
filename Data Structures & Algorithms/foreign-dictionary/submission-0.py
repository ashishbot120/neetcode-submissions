        
from collections import defaultdict, deque
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Create graph and indegree
        graph = defaultdict(set)
        indegree = {}

        # Include every character in the graph
        for word in words:
            for ch in word:
                indegree[ch] = 0

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # Invalid prefix case
            if len(w1) > len(w2) and w1[:minLen] == w2:
                return ""

            # Find first different character
            for j in range(minLen):
                if w1[j] != w2[j]:

                    # Add edge only if it doesn't already exist
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1

                    # Only the first difference matters
                    break

        # Step 3: Add all zero-indegree characters to queue
        queue = deque()

        for ch in indegree:
            if indegree[ch] == 0:
                queue.append(ch)

        # Step 4: Perform topological sort
        result = []

        while queue:
            ch = queue.popleft()
            result.append(ch)

            for neighbor in graph[ch]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 5: Check for a cycle
        if len(result) != len(indegree):
            return ""

        return "".join(result)
