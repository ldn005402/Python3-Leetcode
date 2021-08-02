import collections
import heapq
# Minimum Spanning Tree

# Prim
class Solution:
    def minCostToSupplyWater(self, n: int, wells, pipes) -> int:
        # build graph
        graph = collections.defaultdict(list)
        for u, v, w in pipes:
            graph[u].append([w, u, v])
            graph[v].append([w, v, u])
        for i in range(n):
            # No need to point back to 0
            graph[0].append([wells[i], 0, i+1])
            # graph[i+1].append([wells[i], i+1, 0])
        visited = {0}
        edges = graph[0]
        heapq.heapify(edges)
        res = 0
        while len(visited) < n+1 and edges:
            w, u, v = heapq.heappop(edges)
            if v not in visited:
                res += w
                visited.add(v)
                for edge in graph[v]:
                    if edge[2] not in visited:
                        heapq.heappush(edges, edge)
        return res
