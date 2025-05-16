import sys
readline = sys.stdin.readline

n = int(readline())
soldiers = list(map(int, readline().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if soldiers[i] < soldiers[j]: # 배치에서 빼야하는 놈인 경우
            dp[i] = max(dp[i], dp[j]+1)
# print(n-max(dp))
print(dp)