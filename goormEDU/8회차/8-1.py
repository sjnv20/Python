# Q.구름이의 여행
# 구름이가 사는 구름나라는 N개의 섬으로 이루어져있다. 각 섬에는 1부터 N까지의 번호가 붙어있고, 구름 나라는 사람들이 섬과 섬 사이를 편하게 이동할 수 있도록 다리를 M개 설치했다.
# 설치된 다리들은 모두 아래 특징들을 만족한다.
# - 모든 다리는 양방향으로 이동할 수 있다,
# - 서로 다른 두 섬을 잇는 다리는 최대 하나이다
# - 다리가 잇는 두 섬은 항상 다른섬이다.
# 구름이는 1번 섬에서 출발해서 N번 섬으로 가려하는데, 통과하는 다리의 개수가 K개이하가 되길 원한다.
# 구름이를 도와 1번섬에서 N번 섬까지 K개 이하의 다리를 이용해 도착할 수 있는지 판별해보자

# 예제 설명
# 첫 번째 예제의 경우 1번 섬에서 2번 섬으로 이동한 뒤, 2 번 섬에서 6번 섬으로 이동하면 두 개의 다리만 이용해 도달할 수 있다.
# 따라서 YES를 출력해야 한다,

# 입력
# 첫째줄에 섬의 개수 N과 다리의 개수 M 그리고 구름이가 건널 다리의 최대 개수 K가 공백을 두고 주어진다,
# 다음 M개의 줄에는 다리가 잇는 두 섬의 번호를 의미하는 ui, Ui가 공백을 두고 주어진다,

# 출력
# 구름이가 1번 섬에서 N번 섬까지 K 개 이하의 다리를 사용해서 갈 수 있다면, YES, 갈 수 없다면 NO를 출력한다.

'''
6 6 2
1 4
4 2
2 6
4 3
1 2
3 1
-------
YES

6 6 2
1 2
2 3
3 4
3 5
5 6
5 2
-------
NO

3 1 1
1 2
------
NO
'''

# < 그래프 , BFS >
from collections import deque
import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

D = [9 ** 9 for _ in range(N + 1)]
D[1] = 0

Q = deque()
Q.append(1)
while Q:
    cur = Q.popleft()
    for next in G[cur]:
        if D[next] <= D[cur] + 1:
            continue
        D[next] = D[cur] + 1
        Q.append(next)

if D[N] <= K:
    print("YES")
else:
    print("NO")
