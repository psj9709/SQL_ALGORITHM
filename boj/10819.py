import sys
readline = sys.stdin.readline
n = int(readline())
arr = list(map(int, readline().split()))
# print(arr)
'''
순열을 뽑아야 할거 같네요
'''
ans = 0
visited = [0] * n
def backtracking(cnt):
    global ans, n
    if cnt == n:
        ans = max(ans, cal(sub))
        return
    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        sub.append(arr[i])
        backtracking(cnt+1)
        sub.pop()
        visited[i] = 0

def cal(arr):
    total = 0
    for i in range(len(arr)-1):
        total += abs(arr[i] - arr[i+1])
    
    return total

sub = []
backtracking(0)
print(ans)