import math

N, R = input().split()
N, R = int(N), float(R)
Pai = 3.1415926535
ans = 2 * Pai * R
p1_x, p1_y = map(float, input().split())
f_x, f_y = p1_x, p1_y
for i in range(N - 1):
    p2_x, p2_y = map(float, input().split())
    ans += math.sqrt((p1_x - p2_x) * (p1_x - p2_x) + (p1_y - p2_y) * (p1_y - p2_y))
    p1_x, p1_y = p2_x, p2_y
ans += math.sqrt((p1_x - f_x) * (p1_x - f_x) + (p1_y - f_y) * (p1_y - f_y))
print('%.2f' % ans)