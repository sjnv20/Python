# Q3. 폭탄 구현하기

# n x n 크기의 정사각형 모양의 땅의 (y, x) 좌표에 폭탄을 떨어트리면
# 폭탄이 떨어진 땅과, 그 땅의 상화좌우에 인접한 칸의 폭탄 값이 1증가하게 된다.
# n x n 의 영역에 벗어난 땅은 아무런 영향을 받지 않고 폭탄의 초기값이 0일 경우,
# 폭탄을 모두 떨어트렸을 때 n x n 땅들의 폭탄 값의 합을 구하시오.

# n = 땅크기   , k = 폭탄 횟수
n, k = map(int, input().split())
ground = [[0 for _ in range(n + 1)] for _ in range(n + 1)]      # 폭탄 땅

# 폭탄 떨어진 땅의 상하좌우 좌표
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]

for i in range(k):
    y, x = map(int, input().split())
    ground[y][x] += 1   # 폭탄 떨어진 땅
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if ny < 1 or nx < 1 or ny > n or nx > n:
            continue
        ground[ny][nx] += 1  # 폭탄 떨어진 땅의 인접한 땅

hap2 = 0
for i in range(n + 1):
    hap = sum(ground[i])
    hap2 += hap
print(hap2)