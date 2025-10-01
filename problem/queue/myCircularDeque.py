# 원형 큐 디자인
# 원형 큐를 디자인하라
# FIFO 구조를 지닌다는 점에서 기존의 큐와 동일하다. 그러나 마지막 위치가 시작 위치와 연결되는 원형 구조를 띈다.
# 기존 큐는 공간이 꽉 차게 되면 더이상 요소를 추가할 수 없다. 심지어 앞쪽에 요소들이 deQueue()로 모두 빠져서 충분한 공간이 남게 돼도 그쪽으로는 추가할 방법이 없다.
# 그래서 앞쪽에 공간이 남아있다면 동그랗게 연결해 앞쪽으로 추가할 수 있도록 재활용 가능한 구조가 원형 큐다.
# 동작 원리는 투 포인터와 비슷하다. enQueue()를 하게 되면 rear포인터가 앞으로 이동, deQueue()를 하면 front 포인터가 앞으로 이동.
# 만약 rear 포인터와 front 포인터가 같은 위치에서 서로 만나게 된다면(= 만나는 위치까지 이동했다면) 그때는 정말로 여유 공간이 하나도 없다는 얘기가 되므로 공간 부족 에러를 발생시킨다.

# [ 풀이 1 ] 배열을 이용한 풀이
# 이 풀이에서 사용한 Rear()연산은 리트코트 문제 풀이에는 없다. 큐는 맨 앞에 있는 요소를 가져오는 front(), peek()라는 이름으로 정의된 연산만 있기때문이다.
# 그러나 원형 큐를 구현하기 위해서는 2개의 포인터를 사용하는 만큼 Rear()연산을 구현하는 일이 어려운게 아니라서 구현했다고 함.
class MyCircularQueue:

    # k : 큐의 크기를 입력값으로 받는다. 최대 길이인 maxlen이 된다.
    def __init__(self, k : int ):
        self.q = [None] * k
        self.maxlen = k
        self.p1 = 0 # front 포인터 값, 가장 오래된 요소를 가리키는 역할을 한다.
        self.p2 = 0 # rear 포인터 값

    # enQueue() : 요소를 삽입하는 연산, rear 포인터 이동
    # 큐에 정수형 값(value)을 추가하고, 성공 여부를 불리언(True/False)으로 반환
    def enQueue(self, value : int ) -> bool:

        # elf.p2 : Rear 포인터 (새 요소가 들어갈 위치)
        # 이 위치의 배열 요소(self.q[self.p2])가 현재 비어 있는지 확인.
        if self.q[self.p2] is None:
            # 해당 위치(p2)에 값 넣어줌.
            self.q[self.p2] = value
            # p2(rear 포인터) 한칸 이동.
            # % self.maxlen: 배열의 인덱스가 배열의 최대 크기(self.maxlen)를 넘어서지 않도록 통제하는 역힐.
            # 나머지 연산 덕분에 포인터가 배열의 마지막 인덱스에 도달하더라도 다음 증가 시 자동으로 인덱스 0으로 되돌아갈 수 있게 된다. 나머지 값이 변수에 저장됨.
            # 나머지 연산을 쓰는 이유는 보통 (self.p2 + 1)이 maxlen보다 작거나 같은 두가지 경우가 생기는데
            # (self.p2 + 1)이 maxlen보다 작으면 나머지 연산의 값은 항상 (self.p2 + 1)이 되고
            # (self.p2 + 1))이 maxlen과 같으면 나머지 연산이 0이 되서 다시 앞으로 돌아가기 때문이다.
            # (self.p2 + 1)은 maxlen보다 클 수 없다. 왜냐면 self.p2은 배열의 길이-1(인덱스)의 크기가 가장 큰 값이기때문이다.
            # +1 하는이유는 다음 요소가 들어갈 빈 공간을 가리키기 때문이다.
            self.p2 = (self.p2 + 1) % self.maxlen
            return True
        # rear 포인터 위치의 값이 None이 아니라면 다른 요소가 이미 존재하는 공간 혹은 비정상적인 경우임.
        else:
            return False

    # deQueue() : 요소를 삭제하는 연산, front 포인터 이동
    # 큐에 정수형 값(value)을 삭제하고, 성공 여부를 불리언(True/False)으로 반환
    def deQueue(self) -> bool:

        # 값이 없다면 삭제 불가능
        if self.q[self.p1] is None:
            return False

        else:
            # 삭제
            self.q[self.p1] = None
            # 다음 위치로 이동. + 1 해서 뒤(오른쪽)으로 이동. 가장 앞에 요소가 나갔음으로 다음 삭제할 요소로 이동시키는 것.
            self.p1 = (self.p1 + 1) % self.maxlen
            return True

    # 가장 앞에 있는(=가장 오래된) 위치에 있는 값을 반환
    def Front(self) -> int:
        # p1 포인터의 값이 없다면(None)(=공간이 비어있다면) -1 를 반환,
        # p1에 값이 있다면(=큐에 요소가 있다면) 실제값을 반환
        return -1 if self.q[self.p1] is None else self.q[self.p1]

    #  가장 최근에 추가된 요소를 확인하는 기능
    def Rear(self) -> int:
        # p2 : rear 포인터로서 다음 요소가 삽입될 빈 공간 가리키기때문에 가장 최근에 삽입된 요소를 구하려면 p2-1을 하는 것.
        # p2 - 1에 값이 있다면(=가장 최근에 들어온 요소) 실제값을 반환
        return -1 if self.q[self.p2 - 1] is None else self.q[self.p2 - 1]

    def isEmpty(self) -> bool:
        # 두 포인터가 같은 위치에 있고 p1의 값이 없다면 비어있다고 판단
        return self.p1 == self.p2 and self.q[self.p1] is None

    def isFull(self) -> bool:
        # 두 포인터가 같은 위치에 있는데, p1의 값이 있다면 모든 공간이 꽉 찼다고 판단
        return self.p1 == self.p1 and self.q[self.p1] is not None