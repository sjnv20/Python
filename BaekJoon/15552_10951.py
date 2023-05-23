#Q_15552 : A + B
# Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다.
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
# 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력
import sys
t = int(input())
for i in range(t) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# Q_11022 : A+B - 8
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력
t = int(input())
for i in range(1, t+1) :
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d = %d" %(i,a,b, a+b) )

# Q_ 2439 : 별 찍기 -2
# 오른쪽을 기준으로 정렬한 별(예제 참고)을 출력
'''
         *
       **
     ***
   ****
*****
'''
n = int(input())
for i in range( 1,n+1) :
    print(" "*(n-i) + "*" * i)

# Q_10951 : A + B - 4
# 입력이 끝날 때까지 A + B를 출력하는 문제로 EOF에 대해 알아보는 문제
while True :
    try:
        a, b= map(int, sys.stdin.readline().split())
        print(a+b)
    except :
        break