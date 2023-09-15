# Q.뭉친 K

# N X N 크기의 2차원 배열 M이 있다, M의 i번째 줄 j 번째 칸을 Mi,j라고 하며
# 한 칸의 크기는 1이다. 배열의 각 칸에는 0부터 9사이의 숫자가 하나씩 적혀 있다.
# 이 숫자를 해당 칸의 값이라고 한다.
# 배열 M에는 뭉친 그룹이 있다. 뭉친 그룹이란 상하좌우로 인접한 칸으로 연결되어 있으면서,
# 모든 칸들이 같은 값을 가지는 칸들의 집합을 의미한다. 뭉친 그룹의 크기는 그 그룹에 속한 칸의 개수와 같다,
# Mx,y 칸의 값이 K일 때, 값이 K인 칸으로 이루어진 뭉친 그룹 중 가장 큰 뭉친 그룹의 크기를 출력하시오.

# 입력
# 첫째줄에 M의 크기 N이 주어진다.
# 둘째줄에 x, y가 공백을 두고 주어진다,
# 다음 N개의 줄에는 M의 상태가 주어진다. i번째 줄에는 Mi,1, ... , Mi,n 이 공백을 두고 주어진다,

# 출력
# 값이 K인 칸으로 이루어진 뭉친 그룹 중 가장 큰 뭉친 그룹의 크기를 출력하시오

'''
4
1 2
0 0 1 1
0 1 1 0
0 0 0 1
1 1 1 1
--------
6

4
1 2
0 0 1 2
2 1 1 2
2 0 0 2
1 1 1 2
----------
2
'''

# < 격자형태의 그래프, 그래프 탐색 >
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
Y, X = map(int, input().split())

M = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
V = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(1, N + 1):
    M[i] = [0] + list(map(int, input().split()))

K = M[Y][X]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if V[i][j] or M[i][j] != K:
            continue
        Q = deque()
        V[i][j] = 1
        cnt = 0
        Q.append([i, j])
        while Q:
            cy, cx = Q.popleft()
            cnt += 1
            for k in range(4):
                ny, nx = cy + dy[k], cx + dx[k]
                if ny < 1 or nx < 1 or ny > N or nx > N:
                    continue
                if V[ny][nx] or M[ny][nx] != M[cy][cx]:
                    continue
                V[ny][nx] = 1
                Q.append([ny, nx])
        ans = max(ans, cnt)

print(ans)