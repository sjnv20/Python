# Q.수 이어 붙이기

# 구름이는 10이상 99 이하의 서로 다른 수 Ai가 적힌 카드를 N개 가지고 있다.
# 구름이는 카드의 순서를 임의로 정한 다음, 카드에 적힌 수들을 순서대로 이어붙여서 하나의 큰 수를 만드는 놀이를 하고자 한다,
# 예를 들어 12가 적힌 카드와 34가 적힌 카드를 순서대로 이어 붙이면 1234를 만들 수 있다.
# 구름이는 앞에 있는 카드의 이르이 자리 숫자와 뒤에 있는 카드의 십의 자리 숫자가 같다면 숫자 하나를 겹쳐서 이어 붙일 수 있다는 규칙을 추가했다.
# 예를 들어 38이 적힌 카드와 84가 적힌 카드를 이어붙일 때, 38의 일의 자리 숫자와 84의 십의 자리 숫자가 동일하므로 두 수를 384와 같이 겹쳐서 이어 붙일 수 있다.
# 물론 3884와 같이 겹쳐서 이어 붙이지 않는 것도 가능하다
# 구름이가 놀이에서 만들 수 있는 수 중, 가장 작은 수를 찾아 출력하시오,(단, 놀이할 때 모든 카드는 다 사용해야한다.)

# 입력
# 첫째줄에는 구름이가 가지고 있는 카드의 개수 N이 주어진다.
# 둘째줄에는 각 카드에 적혀있는 A1 ~ An이 공백을 두고 주어진다

# 출력
# 구름이가 놀이에서 만들 수 있는 가장 작은 수

#< 완전탐색, 순열, permutations() >

'''
4
42 31 16 19
------------
1631942

2
87 88
-------
887
'''

from itertools import permutations

N = int(input())
A = list(map(int, input().split()))
A.sort()

ans = 1e18
for order in permutations(A, N):
    cur = order[0]
    for i in range(1, N):
        if cur % 10 == order[i] // 10:
            cur = cur * 10 + order[i] % 10
        else:
            cur = cur * 100 + order[i]
    ans = min(ans, cur)

print(ans)