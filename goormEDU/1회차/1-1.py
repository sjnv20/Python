# Q1. 대소문자 바꾸기
#
# 길이가 N인 영어로 이루어진 문자열 S가 주어진다.
# 이 문자열 S가 철자가 대문자라면 소문자로, 소문자라면 대문자로 바꿔서 출력하시오.
n = int(input())
s = list(input())

for i in range(n):
    if s[i].isupper() == True:
        print(s[i].lower(), end="")
    else:
        print(s[i].upper(), end="")