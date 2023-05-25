#Q3. 소수찾기

#수열의 앞에서 소수 번째에 위치한 값들을 모두 더한 값 구하기
#첫번째 줄에 수열 A의 길이 N이 주어지고 두번째에 수열의 값들이 입력되어진다.

# 풀이 1
def result(n):
    b = [1 for _ in range(n + 1)]
    c = []
    for i in range(2, n + 1):
        if not b[i]:
            continue
        c.append(i)
        for j in range(2 * i, n + 1, i):
            b[j] = 0
    return c


n = int(input())
a = [0] + list(map(int, input().split()))
hap = 0

cs = result(n)
for c in cs:
    hap += a[c]
print(hap)

# 풀이 2
import sys
input = sys.stdin.readline
n = int(input())
a = [0] + list(map(int, input().split()))
b = [1 for _ in range (len(a))]
c = []
result = 0

for i in range(2,n+1) :
    if  b[i] :   # b[i]가 1이 아니면
        c.append(i)
    for j in range(2*i, n+1,i ) :   # 자기 자신의 배수 제거
        b[j] = 0    # 소수가 아닌 자리들 0으로 변경

for i in range(len(c)) :
    result += a[c[i]]
print(result)