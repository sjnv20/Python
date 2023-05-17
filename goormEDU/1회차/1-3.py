#Q3. 큰 수식 찾기

# 각 수식을 연산자 우선순위에 따라 계산했을 때, 두 수식의 계산 결과 중 더 큰 값을 출력하시오.
#두 수식의 계산 결과는 항상 다름이 보장됨

a, b = input().split()

if eval(a) > eval(b) :
	print(eval(a))
else :
	print(eval(b))