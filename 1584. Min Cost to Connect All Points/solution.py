# Code from vanAmsen on leetcode
# For educational purposes
# Prim's Algorithm implementation with minHeap
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan_distance(p1: List[int], p2: List[int]) -> int:
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        n = len(points)
        visited = [False] * n
        heap_dict = {0: 0}  
        min_heap = [(0, 0)]
        
        mst_weight = 0
        
        while min_heap:
            w, u = heappop(min_heap)
            
            if visited[u] or heap_dict.get(u, float('inf')) < w:
               pass
            else: 
            
                visited[u] = True
                mst_weight += w
                
                for v in range(n):
                    if not visited[v]:
                        new_distance = manhattan_distance(points[u], points[v])
        
                        if new_distance < heap_dict.get(v, float('inf')):
                            heap_dict[v] = new_distance
                            heappush(min_heap, (new_distance, v))
        
        return mst_weight
