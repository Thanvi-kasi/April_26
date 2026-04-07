class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')
        dist = [INF] * n
        dist[src] = 0

        # Relax edges k+1 times
        for _ in range(k + 1):
            temp = dist.copy()
            for u, v, price in flights:
                if dist[u] == INF:
                    continue
                if dist[u] + price < temp[v]:
                    temp[v] = dist[u] + price
            dist = temp

        return -1 if dist[dst] == INF else dist[dst]
