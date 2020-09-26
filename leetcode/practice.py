import sys
n = int(input())
a = [[0] * 2 for _ in range(n + 1)]
for i in range(1, n + 1):
    a[i][0], a[i][1] = map(int, input().split())
#求符合的序列
b = [0] * (n + 1)
b[1] = 1; b[2] = a[1][0]
t1 = b[1]; t2 = b[2]
for i in range(3, n + 1):
    if t1 == a[t2][0]:
        b[i] = a[t2][1]
    elif t1 == a[t2][1]:
        b[i] = a[t2][0]
    else:
        print(-1)
        sys.exit()
    t1 = t2; t2 = b[i]
if b[n] != a[1][1]:
    print(-1)
    sys.exit()
#看有多少位置相同，每个数字找能够将他顺时针或逆时针放到原位的位置
pos = [[0] * 2 for _ in range(n + 1)]
for i in range(1, n + 1):
    pos[(i - b[i] + 1 + n) % n][0] += 1 #顺时针
    pos[(i + b[i] - 1) % n][1] += 1

ans = 0
for i in range(n):
    ans = max(ans, pos[i][0], pos[i][1])
    
print(n - ans)