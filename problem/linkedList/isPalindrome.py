import collections
from typing import List

from typing_extensions import Deque

# 팰린드롬 연결 리스트
# 연결리스트가 펠린드롬 구조인지 판별하라.

class ListNode:

    # self : 자기자신(객체)를 참조하기위한 약속, 자기자신(객체)를 가르키는 매개변수.
    # 파이썬의 클래스에서 메서드(함수)를 정의할 때, 첫 번째 매개변수(parameter)는 항상 해당 메서드가 호출되는 객체 자신을 가리킨다.
    # 이 매개변수를 통해 객체의 속성(attributes)에 접근하거나, 객체의 다른 메서드를 호출할 수 있다. (자바는 이걸 알아서 해주지면 파이썬은 명시적으로 선언해야함.)
    def __init__(self, val=0, next=None): # 생성자. 새로운 ListNode 객체를 만들 때 자동으로 호출됨.
        self.val = val
        self.next = next

def stringToListNode(input_string: str) -> ListNode:
    # '1->2->3' 형태의 문자열을 연결 리스트로 변환합니다.
    if not input_string:
        return None

    # '->'를 기준으로 문자열을 분리하여 값 목록을 생성
    # 예: "1->2->2->1" -> ['1', '2', '2', '1']
    values = input_string.split('->')

    # 첫 번째 값을 사용하여 head 노드를 생성
    head = ListNode(int(values[0]))
    current = head

    # 나머지 값들을 순회하며 노드를 만들고 연결
    for val_str in values[1:]:
        # 새로운 노드를 만들고 이전 노드의 next에 연결
        current.next = ListNode(int(val_str))
        current = current.next

    return head

# [ 풀이 1 ] 리스트 변환
# 펠린드롬 여부를 판별하기 위해서는 앞뒤로 모두 추출할 수 있는 자료구조가 필요함으로 연결리스트를 리스트로 변환
def isPalindrome(head: ListNode) -> bool:
    q: List = []

    # 비어있는 리스트는 팰린드롬으로 간주하고 True를 반환
    if not head:
        return True

    # 연결 리스트에서 head는 가장 첫 번째 노드를 가리키는 변수. 리스트의 시작점이다.
    # 연결 리스트의 탐색을 시작하기 위해 변수를 초기화하는 과정
    # head 변수 자체를 사용해서 반복문을 돌면 head = head.next 하게 되어 원래의 Head 위치를 잃어버리게 된다.
    # 이렇게되면 다음번에 다시 리스트를 탐색해야 할 때 시작점으로 돌아갈 수 없게 된다.
    # 원래의 head 포인터를 보존하면서 리스트를 순회하기 위한 임시 포인터를 만들기 위함.
    node = head

    # 연결 리스트를 파이썬의 리스트로 변환하는 부분.
    # 연결 리스트의 첫 번째 노드인 head부터 시작해서, 리스트의 끝(None)에 도달할 때까지 반복
    while node is not None:
        # 노드의 값을 리스트로 저장.
        q.append(node.val)
        # 다음 노드로 이동
        node = node.next

    # q의 길이가 1보다 클때까지 반복
    while len(q) > 1:
        # q.pop(0) : 맨 앞의 값 추출
        # q.pop() : 인덱스를 지정하지 않으면 리스트의 맨 뒤 요소 추출
        # 가장 앞의 값과 가장 뒤의 값이 일치하지않는다면 팰린드롬이 아님.
        if q.pop(0) != q.pop():
            return False

    return True

# [ 풀이 2 ] 데크를 이용한 최적화
# 풀이 1 에서 q.pop(0)를 사용하면 첫번쨰 아이템을 추출할때 속도 문제가 생긴다. 동적 배열로 구성된 리스트는 맨 앞 아이템을 가져오기에 적합한 자료형이 아님.
# 첫번째 값을 꺼내오면 모든 값이 한칸씩 시프팅되며 시간복잡도 O(n)이 발생한다.
# 맨 앞 데이터를 가져올때  O(n)이내에 처리할 수 있는 자료형이 필요하다. 파이썬의 데크(Deque)는 이중 연결 리스트 구조로 양쪽 방향을 모두 추출하는데 O(1)이 걸림.
# 리스트로 처리했을때 타임아웃이 발생한다면 데크를 적용해볼 수 있다.
def isPalindrome2(head: ListNode) -> bool:

    # : Deque : 은 타입 힌트
    q : Deque = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) > 1:
        # q.popleft() : 가장 왼쪽(맨 앞)에 있는 요소를 제거하고 그 값을 반환, pop(0)과 같은 역할을 한다.
        if q.popleft() != q.pop():
            return False

    return True

# [ 풀이 4 ] 런너를 이용한 우아한 풀이
# 팰린드롬 연결 리스트 문제의 제대로 된 풀이법은 런너 기법을 활용하는 것이다.
# 런너 기법(Runner Technique) : 연결 리스트(Linked List)를 순회할 때, 두 개 이상의 포인터를 서로 다른 속도로 이동시키는 알고리즘 기법
# fast는 두 칸씩, slow는 한 칸씩 이동합니다. fast가 리스트의 끝에 도달하면 slow는 정확히 중간 지점에 위치하게 된다.
def isPalindrome3(head: ListNode) -> bool:
    #  rev는 뒤집힌(역방향) 연결 리스트를 저장할 포인터
    rev = None
    # slow와 fast 포인터를 리스트의 시작점(head)으로 초기화
    slow = fast = head

    # fast 포인터가 리스트의 끝에 도달할 때까지 계속 반복
    # 이 루프가 끝나면 slow는 리스트의 중간 노드에 rev는 앞쪽 절반이 뒤집한(역방향) 상태가 됨.
    while fast and fast.next:
        # fast 포인터를 두칸씩 이동함.
        fast = fast.next.next
        # rev = slow : rev를 slow의 현재 위치로 이동.
        # rev.next = rev : rev.next가 이전 rev를 가리키게 하여 노드를 뒤집는다.
        # rev.next를 해서 값을 덮어쓰는 이유는 연결 리스트를 역순으로 만들어야 하기 때문이다.
        # 만약 덮어쓰지 않으면 새로운 노드를 기존 리스트에 연결할 수 없다. rev는 매번 새로운 노드를 리스트의 맨 앞에 추가하는 역할을 하는데, 이를 위해 rev의 next를 이전 rev 노드로 지정한다.
        # 즉 연결리스트는 연결 리스트는 배열과 달리, 노드들이 메모리의 연속된 공간에 저장되지 않기 때문에 next 포인터를 명시적으로 지정해서 노드 간의 연결을 직접 만들어줘야한다.
        # 연결리스트의 노드들은 메모리에 흩어져있을 수 있기때문에 각 노드는 자신의 데이터 외에  다음 노드의 주소(위치)를 담고 있는 next 포인터를 가져야 한다. 그래야 연결 가능!
        # slow = slow.next : slow를 한 칸씩 이동.
        # @@@ 밑의 코드의 경우 반드시  [[ 다중 할당 ]] 을 해야만 함. 파이썬에서 변수는  객체 자체를 저장하는 것이 아니라, 객체의 메모리 주소를 가리키는 참조(reference)를 저장한다.
        # 연결 리스트의 경우 각 노드가 next 포인터를 통해 다음 노드의 참조를 갖고 있다. 그러나 다중할당이 아니라 각각 할당해버리면
        # 각 줄이 실행될 때마다 변수의 참조가 즉시 바뀌면서, 다음 줄에서 필요한 이전 값에 대한 참조를 잃어버려 값이 제대로 할당되지않는다.
        # 하지만 다중할당을 하면 파이썬은 오른쪽의 값들을 모두 먼저 계산한 후 한 번에 할당한다.
        # 이 방식은 rev가 slow의 값으로 업데이트되기 전에 rev.next에 필요한 이전 rev의 값(1)을 안전하게 가져올 수 있게 해준다.
        rev, rev.next , slow = slow, rev, slow.next

    # if fast : 만약 리스트의 노드 개수가 홀수라면, fast는 None이 아닌 마지막 노드에 멈춘다.
    if fast:
        # 이 경우, slow는 정중앙의 노드를 가리키므로, 팰린드롬 비교를 위해 slow를 한 칸 더 이동시켜 중앙 노드를 건너 뛰어야함.
        slow = slow.next

    # 이제 rev 포인터(뒤집힌 앞쪽 절반)와 slow 포인터(원래 리스트의 뒷쪽 절반)를 동시에 한 칸씩 이동하며 각 노드의 *값(val)을 비교.
    # 두 노드의 값이 다르면 루프가 멈춘다.
    while rev and rev.val == slow.val:
        # slow 포인터와 rev 포인터를 한칸씩 이동함.
        slow, rev = slow.next, rev.next
    # 모든 노드가 일치하여 rev가 None이 되면 not rev는 True를 반환.
    # 주악ㄴ에 값이 달라 루프가 멈췄다면 rev는 None이 아니므로 False를 반환.
    return not rev

if __name__ == "__main__":
    # 팰린드롬 문자열 입력
    input_str_palindrome = "1->2->2->1"
    input_str_not_palindrome = "1->2"

    input1 = stringToListNode(input_str_palindrome)
    input2 = stringToListNode(input_str_not_palindrome)

    print(f"isPalindrome1 {isPalindrome(input1)}")
    print(f"isPalindrome1 {isPalindrome(input2)}")

    print(f"isPalindrome2 {isPalindrome2(input1)}")
    print(f"isPalindrome2 {isPalindrome2(input2)}")

