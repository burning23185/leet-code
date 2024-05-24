from collections import defaultdict, deque

class Solution:
    def __init__(self):
        self.graph = {}
        self.visited = set()
    
    def dfs(self, now):
        if now in self.visited:
            return False
        
        if self.graph[now] == []:
            return True
        
        self.visited.add(now)

        for next in self.graph[now]:
                if not self.dfs(next):
                    return False
        self.visited.remove(now)
        self.graph[now] = []
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        self.graph = defaultdict(list)

        for x, y in prerequisites:
            self.graph[y].append(x)

        for key in list(self.graph):
            if not self.dfs(key):
                return False

        return True
