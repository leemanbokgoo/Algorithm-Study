# 원형 데크 디자인
# 다음 연산을 제공하는 원형 데크를 디자인하라.

class ListNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # 이전 노드를 가리키는 포인터
        self.right = right  # 다음 노드를 가리키는 포인터

# [ 풀이 1 ] 이중 연결 리스트를 이용한 데크 구현
# 데크란 양쪽 끝을 모두 추출 할 수 있는 큐
# 데크 구현체이기도 한 이중 연결 리스트로 구현해본다.
# 이중 연결 리스트로 구현이 가능하다는 것을 보여주기 위한 구현일뿐 실제로 원형의 이점을 살리기위해서라면 연결 리스트가 아닌 배열로 풀이해야함.
class MyCircularDeque:
    def __init__(self, k : int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node:ListNode, new :ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node:ListNode ):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value : int ) -> bool:
        if self.len == self.k:
            return False

        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value:int ) -> bool:
        if self.len == self.ke:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0 :
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k