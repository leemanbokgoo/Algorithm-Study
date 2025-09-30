import collections
# 큐를 이용한 스택 구현
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라
# push(x) : 요소 x를 스택에 삽입한다.
# pop() : 스택의 첫번쨰 요소를 삭제한다.
# top() : 스택의 첫번째 요소를 가져온다.
# empty() : 스택이 비어있는 지 여부를 리턴한다.

class MyStack:
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        # 새로 들어온 요소(x)를 제외한 모든 기존 요소들을 순서대로 꺼내 큐의 맨 뒤로 보내는 부분.
        # -1 : 새로 넣은 x 요소 1개를 전체 길이에서 빼서 재정렬에서 제외 
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0
