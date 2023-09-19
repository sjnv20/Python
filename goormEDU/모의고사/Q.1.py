# 구름이는 구름 사이트의 UXUI 디자이너로 일하게 되었다. 구름이의 첫 업무는 구름 사이 트에서 사용자들이 자주 실행하는 이벤트를 정리하는 일이다.
# 이때 이벤트란 사용자가 웹 사이트에서 실행하거나, 클릭한 것을 의미한다. 구름이는 이를 위해서 사용자들이 취할 수 있는 이벤트를 N개로 규정하고, 각각의 이벤트에 1번부터 N번까지 번호를 붙였다.
# 구름이는 이어서 M 명의 사용자가 구름 사이트에서 이벤트를 실행한 내역을 추출하였다.
# 추출한 정보를 바탕으로 구름이는 사용자들이 가장 자주 실행하는 이벤트들을 알아내고자 한다. 한 사람이 같은 이벤트를 여러 번 실행한 경우에도 중복으로 세어준다.
# 구름이를 도와 M명의 사용자들이 가장 자주 실행했던 이벤트들을 찾아 출력하시오.

# 입력
# 첫째 줄에 이벤트의 개수 N과 사용자의 수 M이 공백을 두고 주어진다,
# 다음 M개의 줄에는 매 줄마다 i번 사용자가 실행한 이벤트의 개수 k가 주어지고,
# 이어서 실행한 이벤트의 번호 e1, ... , ek가 공백을 두고 주어진다,

# 출력
# 추출한 정보를 바탕으로 사용자들이 구름 사이트에서 가장 많이 실행한 이벤트를 출력하시오,
# 단, 가장많이 실행한 이벤트가 여러 개라면 각 이벤트를 공백으로 구분하여, 이벤트 번호가 큰 순서에서 작은 순서로 출력하시오.

'''
4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
---------
4 3 2 1

4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 3
-----------
3
'''

#<defaultdict, 정렬>



from collections import defaultdict
import sys
input = sys.stdin.readline

# 요즘 문제가 입력하는 테스트 케이스가 너무 커짐 - 런타임에러 방지 / 필수는 아님

# K는 필요없는 데이터 - 다른 언어에서는 필요할 수 있음
N, M = map(int, input().split())
cnt = defaultdict(int)  # 자료형 미리 선언가능

'''
4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 6
'''
for _ in range(M) :
    events = list(map(int, input().split()))
    for e in events[1:]:
        cnt[e] += 1
# print(cnt.items())  # list 로 형 변환
# print(cnt)

# 반환값은 리스트 형태로 준다
res = sorted(cnt.items(), key = lambda x : (x[1],x[0]), reverse=True)     # x의 1번째 값이 크면 우선순위를 가지고
                                                                                                                    # 만약 같다면 x의 0번째 값이 큰순서대로 우선순위를 가져
                                                                                                                    # 정렬은 항상 오름차순 - 낮은친구부터 높은친구 => reverse=True 하면 내림차순으로 변경
# print(res)
# filter은 list로 반환 꼭 해주어야가능함
res = list(filter(lambda x : x[1] == res[0][1], res))
print("filter: ",res)
for i in res  :
    print(i[0], end=" ")

 # ==================

from collections import defaultdict
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
cnt = defaultdict(int)
for _ in range(M):
    events = list(map(int, input().split()))
    for e in events[1:]:
        cnt[e] += 1

ans = []
res = sorted(cnt.items(), key=lambda x: (x[1], x[0]), reverse=True)
ans.append(res[0][0])

for i in range(1, len(res)):
    if res[i - 1][1] != res[i][1]:
        break
    ans.append(res[i][0])

print(*ans)