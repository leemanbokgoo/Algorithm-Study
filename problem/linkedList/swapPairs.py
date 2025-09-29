# 페어의 노드 스왑
# 연결 리스트를 입력받아 페어 단위로 스왑하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 값만 교환
# 연결리스트의 노드를 변경하는 게 아닌 노드 구조는 그대로 유지하되 값만 변경하는 방법.
# 해당 방법은 사실상 꼼수에 가깝기때문에 코드리뷰에서 안좋은 피드백을 받을 수 있음. 빨리 풀기 위해 시도할만한 방법이나 추천하지않음.
def swapPairs(head: ListNode) -> ListNode:

    cur = head

    while cur and cur.next:
        # 노드의 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        # 다음 페어로 이동
        cur = cur.next.next

    return head

# [ 풀이 2 ] 반복구조로 스왑
# 노드의 값만 바꾸는 게 아니라 노드 자체의 포인터를 변경하여 리스트 구조를 재배열한다.
def swapPairs2(head: ListNode) -> ListNode:
    # 더미 노드(Dummy Node)를 사용하여 head 처리 단순화
    # 노드 1은 리스트의 헤드이므로, 그 앞에는 노드가 없다. 따라서 1과 2를 교환하는 코드는 3과 4를 교환하는 코드와는 다르게 작성해야 하는 특별한 처리가 필요하다.
    # 그렇기때문에 더미 노드인 None을 헤드로 둬서 처리를 단순화 하는 것임.
    # 즉 더미 노드를 사용하면, 코드를 작성할 때 지금 교체하려는 노드가 헤드인지 고민할 필요가 없어진다.
    # prev: 교환될 두 노드(a, b)의 바로 앞 노드를 가리키는 포인터로 초기에는 root와 같은 더미 노드를 지정.
    root = prev = ListNode(None)
    # 더미노드의 다음 노드를 원래 리스트의 헤드로 설정.
    prev.next = head

    while head and head.next:
        # 반복문 안에서 교환할 두 노드를 다음과 같이 정의.
        # a = head, b = head.next
        b = head.next

        # 1. a의 next를 b의 next로 연결 (1 -> 3)
        # 이를 통해 a 노드(1)은 잠시 고립되고 원래 가리키던 b 노드(2)와 a(1)의 연결리 끊어진다.
        head.next = b.next

        # 2. b의 next를 a로 연결 (2 -> 1)
        # b의 next포인터를 a 노드(1)로 설정.
        # b->a 연결이 완성 되어 교환된 페어가 만들어짐.
        b.next = head

        # 3. prev의 next를 b로 연결 (None -> 2)
        # 이전 노드(prev)의 다음을 b로 연결하여 교환된 페어를 전체 연결 리스트에 삽입
        prev.next = b

        # 다음 페어로 포인터 이동 (head는 3, prev는 1)
        head = head.next
        # 교환된 페어를 건너뛰고 새로운 페어의 바로 앞을 가리켜야한다.
        # 0(가짜 더미 )->2->1->3->4 상태임으로 1을 가리켜야하는 것.
        prev = prev.next.next

    # 처음에 설정했던 더미 노드 root의 다음 노드, 즉 실제 리스트의 새로운 헤드를 반환
    return root.next


# [ 풀이 3 ] 재귀 구조로 스왑
def swapPairs3(head: ListNode) -> ListNode:

    if head and head.next:
        p = head.next  # p는 두 번째 노드 (2)

        # 재귀 시작
        # head(1)의 next를 다음 페어의 스왑 결과로 연결 (1 -> swap(3->4) -> 4->3)
        head.next = swapPairs3(p.next)
        # p(2)의 next를 head(1)로 연결 (2 -> 1)
        p.next = head
        # 스왑된 새 시작 노드 p(2)를 반환
        return p

    return head


# 연결 리스트를 만드는 유틸리티 함수
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 연결 리스트를 출력하는 유틸리티 함수
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(str(current.val))
        current = current.next
    return " -> ".join(vals)


if __name__ == "__main__":
    # [1] 풀이 1 (값만 교환) 테스트
    input_list1 = create_linked_list([1, 2, 3, 4])
    result1 = swapPairs(input_list1)
    print(f"[풀이 1] 입력: 1->2->3->4 | 결과: {print_linked_list(result1)}")

    # [2] 풀이 2 (반복구조로 스왑) 테스트
    input_list2 = create_linked_list([1, 2, 3, 4])
    result2 = swapPairs2(input_list2)
    print(f"[풀이 2] 입력: 1->2->3->4 | 결과: {print_linked_list(result2)}")

    # [3] 풀이 3 (재귀 구조로 스왑) 테스트
    input_list3 = create_linked_list([1, 2, 3, 4])
    result3 = swapPairs3(input_list3)
    print(f"[풀이 3] 입력: 1->2->3->4 | 결과: {print_linked_list(result3)}")