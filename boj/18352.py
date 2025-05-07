import sys
from heapq import heappush, heappop
from collections import deque


readline = sys.stdin.readline
    

n, m, k, x = map(int, readline().split())


graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, readline().split())
    if s == e:
        graph[s].append((0, e))
    else:
        graph[s].append((1,e))

dists = [1e9] * (n+1)
dists[x] = 0
pq = [(0, x)]

while pq:
    dist, now = heappop(pq)

    for next_dist, next_city in graph[now]:
        new_dist = dist + next_dist

        if new_dist >= dists[next_city]:
            continue

        dists[next_city] = new_dist
        heappush(pq, (new_dist, next_city))

ans = 0
if k not in dists:
    print(-1)
else:
    for i in range(len(dists)):
        if dists[i] == k:
            print(i)

