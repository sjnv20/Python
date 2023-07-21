# Q1. 대소문자 바꾸기
# 길이가 N인 영어로 이루어진 문자열 S가 주어진다.
# 이 문자열 S가 철자가 대문자라면 소문자로, 소문자라면 대문자로 바꿔서 출력하시오.

# 입력
# 첫째 줄에 문자열 길이 N
# 둘째줄에 길이가 N인 문자열 S가 주어진다
# 모든 문자열은 알파벳으로 이루어져있다,

# 출력
# 바뀐 문자열 출력

'''
10
goormLevel
----------------
GOORMlEVEL
'''

n = int(input())
s = list(input())

for i in range(n):
    if s[i].isupper() == True:
        print(s[i].lower(), end="")
    else:
        print(s[i].upper(), end="")