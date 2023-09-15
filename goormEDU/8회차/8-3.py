# Q. 모래섬

# 바닷가에 놀러간 구름이는 모래사장에서 모래를 쌓아 모래섬을 만들었다.
# 구름이는 자신이 만든 모래섬 사이에 다리르 세우고 싶어한다. 다리를 그냥 만들 수 있지만, 구름이는 서로 떨어진 섬과 섬을 이어줄 때 다리가 의미있다고 생각했다,
# 그래서 구름이는 모래사장에 물을 부어 모래섬을 여러개의 섬으로 나누고자 한다.
# 모래사장은 세로의 길이가 N , 가로의 길이가 M인 직사각형 모양의 땅이다.
# 모래사장을 1 X 1 크기로 나누었을 때, 가장 왼쪽 위부터 i번째 줄의 j번째 칸의 상태를 Si,j라고 표현할 수 있다.
# 각 칸의 상태는 0 또는 1 중 하나이다.
# - Si.j의 값이 0이라면, 그 칸은 물에 가라앉은 칸임을 의미한다.
# -Si, j의 값이 1이라면, 그 칸은 모래가 쌓여있는 칸임을 의미한다.
# 매 분마다 모래가 쌓여있는 칸 중, 다음 조건에 해당하는 칸이 동시에 물에 가라앉게 된다,
# 이때 하나의 모래섬은 다음 내용을 만족한다. 모래가 쌓여있는 칸 중 , 상하좌우로 인접해있는 칸끼리는 이동할 수 있다,
# 단, 물에 가라앉은 칸이나 모래사장의 바깥으로 이동할 수 없다,
# 그리고 어떤 칸에서 다른 칸으로 이동할 수 있는 경로가 존재한다면, 두 칸은 같은 모래섬에 속해있다
# 구름이는 모래섬의 개수가 두 개 이상이 될 때, 다리를 건설하려한다. 구름이가 물을 부은 뒤 최소 몇분후에 다리를 건설할 수 있는지 출력하시오
# 단, 두개이상의 모래섬으로 나누어지지 않는 경우 -1을 출력하시오

# 예제 설명
#첫 번째 예제의 모래사장의 상태는 아래 그림과 같이 변하게 된다.
# [그림]
# 2일 후에 처음으로 두개 이상의 모래섬으로 나눠지므로, 2를 출력해야한다
# 두 번째 예제의 모래사장의 상태는 아래 그림과 같이 변하게 된다.
# [그림]
# 3일 후에 모래사장이 모두 물에 잠길 때까지 모래섬이 두 개이상으로 나누어지지 않으므로 -1 출력해야한다

# 입력
# 첫째줄에 모래사장의 크기를 의미하는 N, M이 공백을 두고 주어진다
# 다음 N개의 줄에는 모래사장의 상태가 주어진다. i번째 줄에는 Si1, ... , Si,m 이 공백을 두고 주어진다
# 물에 가라앉은 칸이 최소 한칸은 존재한다. 따라서 충분한 시간이 지났을 때 모래사장의 모든 칸이 물에 잠기게 된다.
# 처음에 모래섬의 개수는 하나이다. 따라서 0분이 지났을 때 다리를 건설할 수 있는 경우는 주어지지 않는다
# 입력에서 주어지는 모든 수는 정수이다

#출력
# 구름이가 물을 부은 뒤 최소 몇분 후에 다리를 건설할 수 있는지 출력하시오. 단, 두개이상의 모래섬으로 나누어지지 않는 경우 -1출력

'''
6 5
1 1 1 1 1
1 1 1 1 1
1 1 0 1 1
1 1 0 1 1
1 1 1 1 1
1 1 0 1 1
----------
2

5 5
0 0 1 0 0
0 1 1 1 0
1 1 1 1 1
0 1 1 1 0
0 0 1 0 0
----------
-1
'''

# <시뮬레이션, 그래프탐색>
import sys

sys.setrecursionlimit(12345)
input = sys.stdin.readline

N, M = map(int, input().split())
sand = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    info = list(map(int, input().split()))
    for j in range(M):
        sand[i][j] = info[j]

checked = [[0 for _ in range(M)] for _ in range(N)]
update = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def DFS(cur):
    cy, cx = cur
    for k in range(4):
        ny, nx = cy + dy[k], cx + dx[k]
        if ny < 0 or nx < 0 or ny >= N or nx >= M:
            continue
        if checked[ny][nx] or not sand[ny][nx]:
            continue
        checked[ny][nx] = 1
        DFS([ny, nx])


day = 0
while 1:
    island = 0
    for i in range(N):
        for j in range(M):
            if checked[i][j] or not sand[i][j]:
                continue
            checked[i][j] = 1
            island += 1
            DFS([i, j])

    if island > 1:
        print(day)
        exit(0)

    if island == 0:
        print(-1)
        exit(0)

    for i in range(N):
        for j in range(M):
            for k in range(4):
                ny, nx = i + dy[k], j + dx[k]
                if ny < 0 or nx < 0 or ny >= N or nx >= M:
                    continue
                if not sand[ny][nx]:
                    update[i][j] = 1

    for i in range(N):
        for j in range(M):
            if update[i][j]:
                sand[i][j] = 0

    for i in range(N):
        for j in range(M):
            update[i][j] = checked[i][j] = 0
    day += 1
