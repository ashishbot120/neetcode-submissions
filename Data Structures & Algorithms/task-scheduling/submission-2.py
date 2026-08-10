class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        heap = [-freq for freq in count.values()]
        heapq.heapify(heap)

        time = 0
        q = deque()

        while heap or q:

            time += 1

            if heap:
                freq = heapq.heappop(heap)
                freq += 1

                if freq != 0:
                    q.append((freq, time + n ))

            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])

        return time