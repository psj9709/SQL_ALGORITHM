sugars = int(input())

ans = 10e9
num = (sugars // 5) + 1

for i in range(num):
    sugar_3 = -1
    sugar_residual = sugars - 5 * i
    if sugar_residual % 3 == 0:
        sugar_3 = sugar_residual // 3
    else:
        continue
    ans = min(ans, sugar_3 + i)
if ans == 10e9:
    print(-1)
else:
    print(ans)
