class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float('inf')

        dist = [INF] * n
        dist[src] = 0
        
        # At most k stops => at most k + 1 edges
        for _ in range(k + 1):
            # copy to prevent using updates from this same round
            next_dist = dist[:]
            
            for u, v, price in flights:
                if dist[u] != INF:
                    next_dist[v] = min(next_dist[v], dist[u] + price)
            
            dist = next_dist
        
        return -1 if dist[dst] == INF else dist[dst]
        