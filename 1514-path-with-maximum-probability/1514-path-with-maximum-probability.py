class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dst = edges[i]
            prob = succProb[i]
            adj[src].append((dst, prob))
            adj[dst].append((src, prob))
        
        maxprob = [0] * n
        pq = [(-1, start_node)]
        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob *= -1

            if node == end_node:
                return curr_prob
            
            if curr_prob < maxprob[node]:
                continue
            
            for nei, nei_prob in adj[node]:
                new_prob = curr_prob * nei_prob
                if new_prob > maxprob[nei]:
                    heapq.heappush(pq, (-new_prob, nei))
                    maxprob[nei] = new_prob
        return 0