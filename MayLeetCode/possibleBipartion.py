class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        visit = [0] * N
        graph = [[] for _ in range(N)]
        for edge in dislikes:
            u = edge[0] - 1
            v = edge[1] - 1
            graph[u].append(v)
            graph[v].append(u)

        
        q = Queue()
        for i in range(0, N):
            if visit[i] != 0:
                continue
            visit[i] = 1
            q.put(i)

            while not q.empty():
                s = q.size()
                for j in range(0, s):
                    u = q.get()
                    for k in range(0, len(graph[u])):
                        v = graph[u][k]
                        if visit[v] == 0:
                            visit[v] = 2 if visit[v] == 1 else 1
                            q.put(v)
                        
                        if visit[v] == visit[u]:
                            return False
        return True