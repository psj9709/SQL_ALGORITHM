import sys
from heapq import heappush, heappop

readline = sys.stdin.readline

def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def unionfind(x, y):
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:
        return
    if root_x > root_y:
        parents[root_x] = root_y
    else:
        parents[root_y] = root_x 

v, e = map(int, readline().split())
graph = []
for _ in range(e):
    a, b, c = map(int, readline().split())
    graph.append((a, b, c))
graph.sort(key = lambda x: x[2])
parents = [i for i in range(v+1)]

cnt = 0
ans = 0
for a, b, c in graph:
    if find(a) != find(b):
        cnt += 1
        unionfind(a, b)
        ans += c
    if cnt == v-1:
        break
print(ans)
