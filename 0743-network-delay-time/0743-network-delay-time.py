class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        start = k
        edges = [[] for _ in range(n+1)]

        for i in range(len(times)):
            u, v, weight = times[i]
            edges[u].append((v, weight))
        
        #나올 수 없는 최대 거리 = (간선 수 + 1) * 최대 가중치
        max_weight = 100 * len(times)

        dist_arr = [max_weight] * (n + 1)
        dist_arr[start] = 0

        queue = []
        heapq.heappush(queue, (0, start))

        while queue:
            dist_cur, cur = heapq.heappop(queue)

            # 현재까지 도달 했을 때, 그 값이 이전에 온 경로 보다 긴 경우
            if dist_arr[cur] < dist_cur:
                continue

            # 연결된 간선에 거리에 대한 정보를 업데이트
            for adj, weight in edges[cur]:
                # 인접한 노드에 갈 수 있는 더 짧은 거리를 찾았다면 이에 대한 정보를 갱신하고 큐에 추가
                if dist_arr[adj] > dist_arr[cur] + weight:
                    dist_arr[adj] = dist_arr[cur] + weight
                    heapq.heappush(queue, (dist_arr[adj], adj))
        # 최소 거리 값
        res = 0

        for i in range(1, n + 1):
            if dist_arr[i] == max_weight:
                return -1
            
            #가장 큰 값이 끝까지 도달한 경우
            res = max(res, dist_arr[i])
        return res