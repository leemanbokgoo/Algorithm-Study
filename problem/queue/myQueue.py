# 스택을 이용한 큐 구현
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라
# push(x) : 요소 x를 큐 마지막에 삽입한다.
# pop() : 큐 처음에 있는 요소를 삭제한다.
# peek() : 큐 처음에 있는 요소를 조회한다.
# empty() : 큐가 비어있는 지 여부를 리턴한다.

class MyQueue:
    def __init__(self):
        # 파이썬에서 스택 자료형이 따로 없기때문에 []를 사용. 논리적으로 스택 2개를 사용한다고 생각하면 됨.
        # 2개의 스택을 쓰는 이유는 스택의 LIFO 구조를 구현하기위해 두개의 스택을 쓰는게 효율적이기때문.
        # 후입선출 구조로 구현하기위해서는 input에 들어있는 요소들을 매번 뒤집어야하는데 그러면 비효율적이다.
        # 그래서 pop하거나 push할때는 input에 있는 요소들을 역순으로 뒤집어서 output에 넣는다.
        # 만약 output에 요소가 있는 상태에서 input에 요소가 push()되고 그다음에 다시 output에 pop이나 push가 되더라도, 즉 두개의 스택에 각각 요소가 있는 상황이더라도
        # output에 있는 요소를 다 pop이나 push 된 후에야 input에 있는 요소들을 다시 역순으로 정렬하여 output으로 보내기 때문에 상관이 없다.(선입선출이니까)
        self.input = [] #  큐에 새로운 요소를 받을 때 사용. LIFO를 깨지않고 효율적으로 요소를 삽입하는 역활을 함.
        self.output = [] # 큐에서 가장 오래된 요소를 꺼낼때 pop이나 peek를 사용한다.

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek() # output 스택이 채워져 있고, 순서가 뒤집혀 있는지 확인(가장 오래된 요소가 맨 위에 있도록)
        return self.output.pop() # output 스택의 맨 위 요소(가장 오래된 요소)를 꺼낸다.

    def peek(self):
        if not self.output: # 출력 스택이 비어있다면
            while self.input: # 입력 스택에 요소가 있느 ㄴ동안.
                self.output.append(self.input.pop()) # 모두 출력 스택으로 옮겨 순서를 뒤집는다.
        return self.output[-1] # 출력 스택의 맨 위 요소를 반환한다.

    def empty(self):
        return self.input == [] and self.output == []