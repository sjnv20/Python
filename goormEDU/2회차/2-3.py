#Q3. 소수찾기

#수열의 앞에서 소수 번째에 위치한 값들을 모두 더한 값 구하기
#첫번째 줄에 수열 A의 길이 N이 주어지고 두번째에 수열의 값들이 입력되어진다.

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