#Q2. 8진수 계산기

#N개의 10진수 정수가 주어지면, 주어진 정수를 모두 더한 값을 8진수로 표시한다.
#N개의 10진수 정수가 주어졌을 때, 8진수 계산기의 계산 결과를 출력하시오.

n = int(input())
s = list(map(int, input().split()))
print(format(sum(s),'o'))