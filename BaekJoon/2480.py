# Q_2480 : 주사위 세개
#1.  같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다.
# 2. 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다.
# 3. 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.
# 3개 주사위의 나온 눈이 주어질 때, 상금을 계산하는 프로그램을 작성 하시오.

a, b, c = map(int,input().split())

if a == b == c :
    reward = 10000 + a * 1000
    print(reward)
elif a == b or a ==c :
    reward = 1000 + a * 100
    print(reward)
elif b == c :
    reward = 1000 + c * 100
    print(reward)
else :
    if a > b and a > c :
        reward = a * 100
    elif b > a and b > c :
        reward = b*100
    else :
        reward = c*100
    print(reward)
