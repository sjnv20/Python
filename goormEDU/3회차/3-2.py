#Q2.4자리 규칙 숫자 야구
# 정답과 입력을 바탕으로 strike, ball, fail을 판단한다
# strike = 입력의 i번째 값이 정답에 포함되고, 위치도 같은 경우
# ball = 입력의 i번째 값이 정답에 포함되지만, 위치는 같지 않은 경우
# fail = 입력의 i번째 값이 정답에 포함되어 있지 않는 경우
# strike가 4개면 승리한다

# 게임 진행 순서
# 1. 정답과 입력 비교해서 strike, ball, fail 중 어떤 상태인지 판단
#       - 정답과 입력값이 일치하면 게임에서 승리 , 이후 과정은 생략
# 2. 현재 입력의 가장 왼쪽 자리부터 순서대로 아래 과정 반복
#       - 현재 자리 값이 strike면 아무것도 하지 않는다.
#       - 현재 자리 값이 fail이면 현재 자리 값에 1을 더한 뒤 10으로 나눈다
#           만약 계산값이 현재 입력의 다른자리에 존재한다면, 존재하지 않을 때 까지 반복
# 3. 2번 과정에서 ball인 자리가 있으면 판단 결과 중 strike에 해당하는 자리를 제외하고 나머지 자리를 모두 오른쪽으로 한칸씩 옮긴다.
#       오른쪽으로 옮길 자리가 없는 경우 strike가 아닌 가장 왼쪽자리로 이동

# 구름이가 게임을 진행했을 때 승리하기 위해 위 과정을 몇번 수행해야하는지 구하시오.

answer =list(map(int,input()))
inp = list(map(int,input()))
score = 0

def fail() :
    for i in range(4) :
        if result[i]  != 2 :
            continue
        while True:
            temp = (inp[i] + 1) % 10
            out = temp not in inp
            inp[i] = temp
            if out :
                break
def ball() :
        if 1 not in  result  :
            return
        pos = []
        value = []
        for i in range(4) :
            if result[i] != 0 :
                pos.append(i)                    # strike에 해당하는 자리를 제외
                value.append(inp[i])
        for i in range(len(pos)) :
            if i == 0:
                inp[pos[i]] = value [-1]    #  오른쪽으로 옮길 자리가 없는 경우
            else :
                inp[pos[i]] = value[i - 1]  # 나머지 자리를 모두 오른쪽으로 한칸씩 옮기기

while True :
    score += 1
    result = [2,2,2,2]
    if inp == answer :
        print(score)
        break;

    for i in range(4) :
        if inp[i] in answer :
            if inp[i] == answer[i] :
                result[i] = 0                 #strike
            else :
                result[i] = 1                  # ball

    fail()
    ball()
