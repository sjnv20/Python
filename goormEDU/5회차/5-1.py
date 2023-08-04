# Q.Stack

# 크기가 K인 Stack 자료구조를 구현하려고 한다.
# - 주어지는 명령은 push와 pop 두 가지이다,
# - push는 스택에 크기가 1인 정수를 추가하는 명령이다.
# - 만약 이미 스택이 가득 차 있을 때 push명령이 주어진다면, 대신 overflow를 출력한다
# - pop은 스택에 가장 최근에 추가된 정수를 제거하고, 제거된 정수를 출력하는 명령이다.
# - 만약에 이미 스택이 비어있을 대 pop 명령이 주어진다면, 대신 underflow를 출력한다.
# N개의 명령이 주어질 때, 위 지시 사항에 따라 값을 출력하시오.

# 입력
# 첫째줄에 주어지는 명령의 개수 N과 스택의 크기 K가 공백을 두고 주어진다
# 다음 N개의 줄에는 명령이 주어진다
# - push <value> : 스택에 값이 <value>인 정수 데이터를 추가한다
# - pop : 스택에서 가장 최근에 추가된 정수를 제거한다
# 명령은 항상 위 두가지 형식 중 하나로 주어진다

# 출력
# 지문의 지시사항에 따라 명령 수행 결과를 한 줄에 하나씩 출력한다

# <stack>
'''
10 3
push 1
push 6
push 5
pop
pop
pop
push 4
push 4
push 3
pop
---------
5
6
1
3
'''

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
S = []

for _ in range(N):
    op = input().rstrip().split()
    if op[0] == "push":
        if len(S) < K:
            S.append(int(op[1]))
        else:
            print("Overflow")
    else:
        if S:
            print(S.pop())
        else:
            print("Underflow")

# deque를 이용한 구현
import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
S = deque()

for _ in range(N):
    op = input().rstrip().split()
    if op[0] == "push":
       if len(S) < K:
           S.append(int(op[1]))
       else:
           print("Overflow")
    else:
        if S:
            print(S.pop())
        else:
            print("Underflow")