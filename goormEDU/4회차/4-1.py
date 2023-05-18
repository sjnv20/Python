#Q1. 제곱암호

# 제곱암호 특징
# 암호문의 길이가 N이라면 N/2개의 숫자와 N/2개의 알파벳 소문자로 이루어져있다.
# 암호문의 길이는 항상 짝수이다
# 암호문의 첫 글자는 항상 알파벳 소문자이며, 이후에는 항상 숫자와 알파벳 소문자가 번갈아가며 등장한다.

# 복호화 방법
# 원문은 처음 비어있는 상태에서 암호문의 첫 번째 문자부터 복호화 과정을 거친다
# i가 홀수일 때, 암호문의 i번째 문자를 알파벳의 사전 기준 다음문자로 바꾸는 작업을 암호의 i번째 숫자의 제곱번 시행한다,
# 작업이 끝난 뒤 변환된 알파벳을 원문의 맨 오른쪽에 추가한다 (i번째 숫자는 암호문의 i+1번째 문자에 해당함)
# z에서 사전 기준 다음 문자로 바꿔야 하는 경우에는 a로 바뀌게 된다.
# 복호화가 끝난 뒤의 원문은 N/2의 길이의 알파벳 소문자로만 이루어진 문자열이다.

from string import ascii_lowercase
alphabet = list(ascii_lowercase)

n = int(input())
pwd = list(input())
result = ""

for j in range(0, n, 2):
    a = int(pwd[j + 1]) ** 2
    b = alphabet.index(pwd[j])
    hap = (a + b) % 26
    result += alphabet[hap]

print(result)