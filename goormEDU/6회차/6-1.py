# 거스름돈

# 구름 나라에는 총 5종류의 동전이 있다
# 1원, 5원, 10원, 20원, 40원
# 구름이는 각 동전을 무한히 많이 가지고있다.
# 구름이는 어느 날 손님에게  N원의 거스름돈을 주려고 한다, N원을 거슬러주기 위해 필요한 동전의 최소 개수는 몇개일까

# 입력
# 첫째줄에 정수 N이 주어진다

# 출력
# 구름이가 손님에게 거슬러줘야 하는 동전의 최소 개수를 출력하시오.

'''
55
----
3

39
----
7
'''
#<그리디 알고리즘>

coin = [40, 20, 10, 5, 1]
N = int(input())
count = 0
for i in coin:
    count += N // i
    N %= i
print(count)