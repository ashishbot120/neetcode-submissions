class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        for _ in range(k+1):
            temp_price = prices.copy()
            for start,end,price in flights:
                if prices[start] == float("inf"):
                    continue
                new_price = prices[start] + price
                temp_price[end]= min(
                    new_price,
                    temp_price[end]
                )
            prices = temp_price
        if prices[dst] == float("inf"):
            return -1
        return prices[dst]
