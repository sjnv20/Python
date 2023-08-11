class Stack:
    def __init__(self, max_size = 4) :
        self.stack = []     # list 생성
        self.top = -1         # top 변수 설정
        self.max = max_size - 1

    def isEmpty(self) : #pop()연산 전 실행
        if self.top == -1 :
            return True
        else :
            return False

    def isFull(self) :  # push() 연산 전 실행
     if self.top == self.max :
        return True
     else :
         return False

    def push(self, item) :
        if self.isFull() == True :  # stack이 가득 찬 경우
            print("Stack is Full, don't push()")    # don't push()
        else :
            self.stack.append(item) # stack에 item 집어넣기
            self.top += 1                         # top = top +1

    def pop(self) :
        if self.isEmpty() == True  :                         # 스택이 비어있는 경우
            print("Stack is Empty.  don't pop()")   # don't pop()
        else :
            pop_item = self.stack[self.top]     # 제거할 맨 위 요소를 pop_item에 저장
            del self.stack[self.top]                       # 맨 위 요소 삭제
            self.top -= 1                                               # top = top - 1
            return pop_item

    def peek(self) :
        if self.isEmpty() == True :
            print("Stack is Empty.  don't peek()")
        else:
            return self.stack[self.top]
