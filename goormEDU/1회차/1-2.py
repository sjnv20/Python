# Q2. 단어 필터
#
# 메시지 E에 특정 단어 S가 포함되어 있으면, 이를 가장 앞에서 등장하는 단어S부터 순서대로 제거한 후 완전한 메시지를 구름이에게 전달
# 단어 필터는 대소문자 모두 동일해야 지워야 할 단어라고 판단, 메시지 E에 더 이상 단어 S가 존재하지 않을 때 까지 반복해서 필터링 적용

s, e = map(int, input().split())
w_s = input()
w_e = input()

while w_s in w_e:
    w_e = w_e.replace(w_s, "")

if w_e:
    print(w_e)
else:
    print("EMPTY")