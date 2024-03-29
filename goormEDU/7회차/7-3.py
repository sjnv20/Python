# Q.거리두기

# 구름이는 구름카페를 운영하는 사장님이다. 구름카페에는 테이블 N X 3 격자 형태로 배열되어 있다
# 한 줄에는 3개의 테이블이 있고, 이러한 줄이 총 N 줄 있다.
# 기존에는 모든 테이블에 동시에 사람들이 앉을 수 있었다. 하지만 사람들 사이에서 소음으로 자주 다툼이 발생하자,
# 구름이는 테이블 간 거리두기를 시행해서 일부 테이블에서만 앉아서 커피를 마시거나 작업을 할 수 있도로 하려한다.
# 테이블간 거리두기를 시행하게 되면 어떤 사람이 앉아있는 자리에서 앞뒤와 양옆으로 인접한 테이블에는 동시에 사람들이 앉을 수 없게된다
# 구름이는 거리두기 방식에 따라 사람들이 앉을 수 있는 테이블에 스티커를 붙이기로 했다.
# 구름이는 충분히 많은 스티커를 가지고 있기 때문에 붙일 수 있는 스티거의 개수에는 제한이 없으며, 스티커를 하나도 붙이지 않을 수도 있다.
# 구름 카페에 있는 테이블의 줄 수 N이 주어졌을 때, 구름이가 테이블에서 스티커를 붙일 수 있는 경우의 수를 구해보자
# 단, 수가 너무 커질 수 있으므로 경우의 수를 100 000 007로 나눈 나머지를 출력한다,

# 예제 설명
# 구름 카페의 한 줄에 나올 수 있는 스티커 배치의 경우의 수는 아래의 5가지이다. 스티커를 하나도 붙이지 않는 경우도 포함해야 함을 유의하라.
#[ 그림]
# 아래는 구름 카페에 두 줄의 테이블이 있을 때 스티커를 붙일 수 있는 경우의 수 중 일부이다
# [그림]

# 입력
# 첫째 줄 테이블의 줄 수를 의미하는 N이 주어진다

# 출력
# 경우의 수를 100 000 007로 나눈 나머지를 출력

#<다이나믹 프로그래밍, Bottom-Up DP>
'''
1
-
5

2
-
17

3
-
63
'''
N = int(input())
dp = [[0 for _ in range(5)] for _ in range(N + 1)]
dp[0][0] = 1
MOD = 100000007

for i in range(1, N + 1):
    dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3] + dp[i - 1][4]) % MOD
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2] + dp[i - 1][3]) % MOD
    dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
    dp[i][3] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][4] = (dp[i - 1][0] + dp[i - 1][2]) % MOD

print(sum(dp[N]) % MOD)
#====================================================================

import sys

sys.setrecursionlimit(150000)

# 이 정해 코드를 그냥 실행하면 스택 메모리 제한으로 인해 일부 테스트 케이스를 통과하지 못합니다.
# 아래 주석 처리된 코드와 같이 실행하면, 스택 메모리 제한을 임시적으로 조금 늘려서 문제를 해결할 수 있습니다.
# 시스템에 직접 접근하는 코드이므로, 일반적으로 코딩 테스트를 응시할 때는 사용하면 안되는 코드입니다!!

import resource

resource.setrlimit(resource.RLIMIT_STACK, (64 * 1024 * 1024, -1))

MOD = 10 ** 8 + 7
N = int(input())
dp = dict()
for n in range(5):
    dp[(0, n)] = 1 if n == 0 else 0


def get(i, n):
    if (i, n) in dp:
        return dp[(i, n)]
    ret = 0
    if n == 0:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 2) + get(i - 1, 3) + get(i - 1, 4)
    elif n == 1:
        ret += get(i - 1, 0) + get(i - 1, 2) + get(i - 1, 3)
    elif n == 2:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 3) + get(i - 1, 4)
    elif n == 3:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 2)
    else:
        ret += get(i - 1, 0) + get(i - 1, 2)
    ret %= MOD
    dp[(i, n)] = ret
    return ret


ans = 0
for n in range(5):
    ans += get(N, n)
print(ans % MOD)