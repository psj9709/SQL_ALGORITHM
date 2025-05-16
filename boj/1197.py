import sys
from heapq import heappush, heappop

readline = sys.stdin.readline

def prim(start):
    global cnt
    hq = []
    visited = [0] * (v+1)
    sum_w = 0
    heappush(hq, (0, start))

    while cnt < v:
        w, a = heappop(hq)

        if visited[a]:
            continue
            
        visited[a] = 1
        sum_w += w
        cnt += 1
        for i in graph[a]:
            heappush(hq, i)
    return sum_w

v, e = map(int, readline().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

cnt = 0
ans = prim(1)
print(ans)
