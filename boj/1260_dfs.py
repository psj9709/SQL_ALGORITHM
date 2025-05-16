import sys
from collections import deque

readline = sys.stdin.readline

def dfs(start):
    if visited[start]:
        return
    visited[start] = 1
    res_dfs.append(start)
    for next_node in graph[start]:
        if visited[next_node]:
            continue
        dfs(next_node)

def bfs(x):
    dq = deque([x])
    while dq:
        x = dq.popleft()
        if visited2[x]:
            continue
        visited2[x] = 1
        res_bfs.append(x)
        for next_node in graph[x]:
            if visited2[next_node]:
                continue
            dq.append(next_node)

n, m, v = map(int, readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, readline().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(n+1):
    graph[i].sort()
visited = [0] * (n+1)
visited2 = [0] * (n+1)
res_dfs = []
res_bfs = []
dfs(v)
bfs(v)
print(*res_dfs)
print(*res_bfs)