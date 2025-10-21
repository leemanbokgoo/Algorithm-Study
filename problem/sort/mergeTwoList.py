# 58) 리스트 정렬
# 연결 리스트를 O(n log n)에 정렬하라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 병합 정렬
# 코딩 테스트 시 직접 정렬을 구현할 일은 거의 없지만 이 문제는 연결 리스트를 입력값으로 주기떄문에 직접 정렬을 구현해야한다.
# 현재 문제는 시간 복잡도가  O(n log n)이라는 제약사항이 있음으로 버블 정렬 같은 알고리즘은 사용할 수 없다.
# 연결 리스트 입력에 대해서는 파이썬에서 정렬할 수 있는 별도의 함수를 제공하지않기때문에 직접 정렬 알고리즘을 구현해야한다.
# 그렇기에 병합 정렬과 퀵 정렬을 구현해볼 수 있는데 연결 리스트는 특성상 피벗을 고정된 위치로 지정할 수 밖에 없고 퀵 정렬은 입력값에 따라 성능의 편차가 심하므로 벙합 정렬로 구현해본다.
def mergeTwoList(l1 : ListNode, l2 :ListNode) -> ListNode:
    # 재귀 호출을 통해 l1의 포인터를 이동하면서 정렬해 리턴한다.
    # return l1 or l2는 l1값이 있다면 항상 l1을 리턴하고 l1이 None인 경우 l2를 리턴한다. 즉, l1이 우선이다.
    # 크기 비교를 통해 정렬하면서 이어 붙인다.
    if l1 and l2:
        # l1의 현재 노드 값이 l2의 현재 노드 값보다 큰 경우
        if l1.val > l2.val:
            # 더 작은 값을 가진 노드가 항상 l1이 되도록 두 변수를 교체.
            # 이렇게 하면 병합된 리스트의 시작 노드는 항상 l1이 된다.
            l1, l2 = l2, l1

        # 재귀 호출을 통해 뒤의 리스트들을 정렬
        # 4 , 3->4, 2->3->4 , 1->2->3->4 이렇게 반환된다.
        l1.next = mergeTwoList(l1.next, l2)

    # 둘 중 하나의 리스트가 비어있다면, 비어있지않은 리스트를 반환.
    return l1 or l2

def sortList(head: ListNode) -> ListNode:
    if not (head and head.next):
        return head

    # 런너 기법을 활용하는 부분
    # slows는 한칸씩, fast는 두칸씩 앞으로 이동한다. 이렇게 하면 fast가 맨 끝에 도달했을 때 slow는 중앙에 도착해있을 것.
    # half는 slow의 바로 이전 값으로 한다.
    # 반복문이 끝나면 half는 리스트 전반부의 마지막 노드가 된다.
    half, slow, fast = None, head, head
    while fast and fast.next:
        half, slow, fast = slow, slow.next, fast.next.next
    # half 위치를 기준으로 연결 리스트 관계를 끊어버린다.
    # 즉, head로 시작하는 전반부와 slow로 시작하는 후반부로 완전히 두개의 연결 리스트로 분할됨.
    half.next = None

    # 재귀 호출을 통해서 재귀적으로 정렬한다.
    # sortList(head) : 전반부 리스트를 다시 중앙으로 쪼개기 위해 새로운 sortList 호출을 시작한다. 이 과정은 리스트의 크기가 1이 될 때까지 반복된다.
    # 모든 리스트가 노드 1개짜리로 쪼개지면, 이 노드 1개짜리 리스트는 정렬된 상태로 간주되어 반환된다.
    l1 = sortList(head)
    l2 = sortList(slow)

    # 위 단계에서 반환된 정렬된 두 개의 작은 리스트(l1과 l2)를 mergeTwoList 함수가 병합한다.
    # # mergeTwoList는 두 리스트의 노드를 비교하여 더 작은 값부터 연결하면서 하나의 정렬된 리스트를 만든다.
    #  병합된 새로운 정렬 리스트가 상위 호출 단계로 반환되고, 이 과정이 반복적으로 이루어지면서 최종적으로 전체 리스트가 정렬됨.
    # mergeTwoList(4, 2), mergeTwoList(2->4, 1->3) => 1->2->3->4 이런 식으로 재귀호출하며 결과를 완성
    return mergeTwoList(l1, l2)

# [ 풀이 2 ] 내장 함수를 이용하는 실용적인 방법
# 대부분의 프로그래밍 언어들은 표준 라이브러리에서 이미 성능 좋은 정렬 알고리즘을 제공하고 있다.
def sortList(head:ListNode) -> ListNode:

    p = head
    # 연결 리스트를 파이썬의 리스트로 만든다.
    lst : list = []
    while p:
        lst.append(p.val)
        p = p.next

    # 내장 정렬 함수 사용
    lst.sort()

    # 정렬한 리스트를 다시 연결 리스트로 변환
    p = head
    for i in range(len(lst)):
        p.val = lst[i]
        p = p.next

    return head

# 연결 리스트를 문자열로 변환하는 헬퍼 함수
def list_to_string(head: ListNode) -> str:
    s = ""
    current = head
    while current:
        s += str(current.val)
        if current.next:
            s += "->"
        current = current.next
    return s

if __name__ == "__main__":
    # 요청하신 입력값: 4->2->1->3
    li = ListNode(4)
    li.next = ListNode(2)
    li.next.next = ListNode(1)
    li.next.next.next = ListNode(3)

    print(f"원본 연결 리스트: {list_to_string(li)}")

    # 풀이 1 (Merge Sort)을 사용하여 정렬
    sorted_li = sortList(li)

    # 정렬된 연결 리스트를 문자열로 출력
    output_string = list_to_string(sorted_li)
    print(f"정렬된 연결 리스트: {output_string}")



