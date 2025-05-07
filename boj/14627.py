import sys
readline = sys.stdin.readline 
p, c = map(int, readline().split())
green_onions = []
max_green_onions = 0
ans = 0
for _ in range(p):
    green_onion = int(readline())
    green_onions.append(green_onion)
    max_green_onions = max(max_green_onions, green_onion)
print(green_onions)
'''
1부터 10억 끝 잡고
이진 탐색 후 
개수만큼 안나오면 -> 1부터 미드까지
개수보다 많이 나오면 -> 미드부터 끝까지ㅣ
'''
left = 1
right = max_green_onions
mid = 0
while left <= right:
    mid = (left + right) // 2
    print(mid)
    sum_chickens = 0
    for i in range(p):
        sum_chickens += green_onions[i] // mid
    # 1. 치킨보다 작은 경우
    if sum_chickens < c:
        right = mid
    # 2. 치킨보다 큰 경우
    elif sum_chickens > c:
        left = mid
    else:
        ans = max(ans, mid)
        left = mid

