from typing import List, Optional
import collections
# 해시맵 디자인
# 다음의 기능을 제공하는 해시맵을 디자인하라.
# put(key, value) : 키, 값을 해시맵에 삽입한다. 만약 이미 존재하는 키라면 업데이트 한다.
# get(key) : 키에 해당하는 값을 조회한다. 만약 키가 존재하지않는다면 -1을 리턴한다.
# remove(key) : 키에 해당하는 키, 값을 해시맵에서 삭제한다.

# [ 풀이 1 ] 개별 체이닝 방식을 이용한 해시 테이블 구현
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None # 다음 노드를 가리키는 포인터. 연결 리스트의 기본 구조를 형성

class MyHashMap:
    def __init__(self):
        self.size = 1000 # 해쉬 테이블의 크기, 즉 버킷의 개수를 1000으로 고정. 해시 함수로 나눈 나머지를 취할때 사용된다.
        # 해시 테이블 자체로, 크기가 1000인 배열 또는 리스트 역할을 함. defaultdict를 사용하여 각 버킷에 접근할 때 자동으로 ListNode 객체를 초기값으로 설정함.
        self.table = collections.defaultdict(ListNode)

    def _hash(self, key: int) -> int:
        # 입력된 key를 해시 테이블 크기(여기선 1000)로 나눈 나머지를 반환. 이 값이 해당 키-값 쌍이 저장될 버킷의 인덱스가 됨.
        # 장 간단하고 효율적인 해시 함수 중 하나인 나누셈법이다. 나머지 연산(Modulus  Operation)은 입력 값을 원하는 범위 안에 가두는 가장 확실한 방법.
        # 해시 테이블의 유효한 인덱스 범위(현재 해시테이블의 범위가 100임으로 유효한 인덱스 범위는 0 ~ 999)를 절대 벗어나지 않게 보장한다.
        return key % self.size

    def put(self, key: int, value: int) -> None:
        # 키에 해당하는 버킷 인덱스를 계산.
        index = self._hash(key)
        # 해당 버킷의 첫번쨰 노드가 실제 값을 가지고 있는지 확인
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value) # 값이 없다면 새로운 노드를 생성하고 값을 저장한 뒤 종료
            return

        # 체이닝 순회 시작, 해시 충돌 처리
        # 해당 버킷의 더미 노드부터 순회를 시작.
        p = self.table[index]
        while p:
            if p.key == key: # 이미 같은 key를 가진 노드 발견시
                p.value = value # 해당 노드의 value를 새로운 값으로 갱신하고 종료.
                return
            # if p.next is None : 연결 리스트의 끝까지 도달했다면.
            # 그런데도 key를 발견하지못했다면 일단 while문 종료.
            if p.next is None:
                break
            # 다음 노드로 한칸 이동
            # p를 p.next값으로 계속 갱신하기때문에 while문을 반복할때마다 p 변수가 새로운 노드를 가리킬 수 있다.
            p = p.next
        # 마지막 노드의 next에 새로운 ListNode를 연결하여 추가한다.
        p.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = self._hash(key)
        # 해당 테이블에 노드가 존재하지않으면 -1 반환
        if self.table[index].value is None:
            return -1

        # 체이닝 순회
        p = self.table[index]
        while p :
            if p.key == key: # 지금 key와 노드의 key가 같으면
                return p.value # 값을 찾았다면 반환
            # 포인터를 한칸 옆의 노드로 이동.
            p = p.next

        return -1  # 찾지 못하면 -1 반환

    def remove(self, key: int) -> None:
        index = self._hash(key)
        # 해당 값이 없다면, 삭제 할 수 없음
        if self.table[index].value is None:
            return # 종료

        # 체이닝 순회
        p = self.table[index]

        # 첫번째 노드 자체가 삭제 대상인지 확인
        if p.key == key:
            # if p.next is None : 연결 리스트에 노드가 하나뿐이라면, 해당 버킷을 빈 ListNode()로 초기화 (리스트 비움)
            # else p.next : 다음 ㅗㄴ드가 있다면 버킷의 시작(self.table[index])을 다음 노드(p.next)로 변경. (삭제된 p 노드는 가비지 컬렉터가 처리함.)
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # prev : p의 바로 앞에 있는 노드를 항상 가리키는 변수. p의 이전 노드.
        prev = p # p로 일단 초기화

        while p:
            if p.key == key:
                # 이전 노드의 포인터를 현재 노드(p)를 건너뛰고 다음 노드로 직접 연결. p는 리스트에서 분리되어 삭제됨.
                # prev와 p는 연결리스트의 값을 저장하는 게 아니라, 포인터를 저장하고 있기때문에 둘다 같은 연결 리스트를 가리키는 포인터 값을 가지고 있고,
                # 그렇기 때문에 prev.next 값을 바꾸면 p가 가르키고 있는 연결 리스트 값이 바뀌는것.
                # 즉 prev.p는 연결리스트 자체가 아니라 연결 리스트안에 속하는 노드 객체 하나하나를 가리키고 있는 것이다.
                prev.next = p.next
                return
            # 키를 찾지 못했다면 두 포인터를 한칸씩 앞으로 이동.
            prev, p = p, p.next