# 체크카드

# 구름이가 쓰는 체크카드는 deposit, pay, reservation의 세가지 기능을 가지고 있다.
# deposit :주어진 금액만큼 계좌에 돈이 들어온다
# pay: 주어진 금액만큼 계좌에서 돈이 결제된다 단, 계좌의 현재 잔액이 주어진 금액보다 적다면 결제되지 않는다.
# reservation : 주어진 금액만큼 계좌에서 돈이 결제된다.
# 단, 계좌의 현재 잔액이 주어진 금액보다 적거나, 대기목록에 다른 거래가 있다면 결제되지 않고 대기 목록의 맨 뒤에 추가된다.
# 대기 목록에 있는 거래들은 대기 목록에 들어간 순서대로 결제가 가능해지는 즉시 해당 거래의 금액만큼 계좌에서 금액이 차감된 뒤 대기목록에서 삭제된다.

# 구름이의 계좌에 들어있던 금액과 지난달 구름이의 거래 내역이 주어졌을 때, 주어진 모든 거래가 진행된 뒤에
# 구름이의 계좌에 남아있는 금액을 출력하시오
# 거래가 완료되지 않고 대기 목록에 남아있는 경우도 거래가 진행된것으로 본다.

# 입력
# 첫째줄에는 처음에 구름이의 계좌에 들어 있던 잔액 N과 지난달 구름이의 거래 횟수 M이 공백을 두고 주어진다.
# 다음 M개의 줄에는 구름이의 거래 내역이 시간 순서대로 주어진다. 거래 내역은 유형과 금액이 공백을 두고 주어진다.

# 출력
# 주어진 모든 거래가 진행된 뒤에 구름이의 계좌에 남아있는 금액을 출력한다.

'''
0 6
deposit 10
reservation 20
pay 5
deposit 10
deposit 10
reservation 6
---------------
5

0 6
deposit 10
pay 5
reservation 5
reservation 5
pay 5
deposit 10
----------------
5
'''
# < 시뮬레이션, 큐>

from collections import deque

N, M = map(int, input().split())
Q = deque()

for i in range(M):
    op, cost = input().split()
    cost = int(cost)

    if op == "deposit":
        N = N + cost
        # 잔액이 늘어난 뒤에, 현재 대기 목록에 있는 거래가 결제될 수 있는지를 판단합니다.
        # 큐가 비어있는데 큐의 맨 앞 원소에 접근을 하면 IndexError가 뜨므로,
        # 항상 큐의 원소가 들어있는지를 확인하는 과정이 필요합니다.
        while Q and Q[0] <= N:
            # 거래가 가능한 경우에는 거래를 하고, 다시 위의 과정을 반복합니다.
            N = N - Q[0]
            Q.popleft()

    elif op == "pay":
        if N >= cost:
            N = N - cost

    elif op == "reservation":
        if not Q and N >= cost:
            N = N - cost
        else:
            # reservation에서 거래가 실패할 경우에는, 큐에 거래 내역을 추가합니다.
            Q.append(cost)

print(N)