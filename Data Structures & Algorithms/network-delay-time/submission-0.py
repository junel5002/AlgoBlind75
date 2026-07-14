class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))

        minHeap = [(0, k)]
        visited = {}

        while minHeap:
            curTime, node = heapq.heappop(minHeap)

            if node in visited:
                continue

            visited[node] = curTime

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (curTime + weight, nei))

        if len(visited) != n:
            return -1

        return max(visited.values())



#NB: This is how you remember; normally when they give you the linked list,
# you have to rewrite it to look like a row column something
# eg. times = [[1, 2, 1], [2, 3, 1]]

# will be times = [[1, 2, 1],
#                  [2, 3, 1]]

# so this is how it works [from_node, to_node, cost_involved] : meaning
# that for the times linked list above, you move from node 1 to node 2 with
# a cost/time/weight of 1. similarly from node 2 to node 3, a cost of 1
