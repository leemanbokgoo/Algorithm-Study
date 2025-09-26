# 페어의 노드 스왑
# 연결 리스트를 입력받아 페어 단위로 스왑하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 값만 교환
def swapPairs(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # 노드의 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        # 다음 페어로 이동
        cur = cur.next.next

    return head


# [ 풀이 2 ] 반복구조로 스왑
def swapPairs2(head: ListNode) -> ListNode:
    # 더미 노드(Dummy Node)를 사용하여 head 처리 단순화
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # a=head, b=head.next
        b = head.next

        # 1. a의 next를 b의 next로 연결 (1 -> 3)
        head.next = b.next
        # 2. b의 next를 a로 연결 (2 -> 1)
        b.next = head

        # 3. prev의 next를 b로 연결 (None -> 2)
        prev.next = b

        # 다음 페어로 포인터 이동 (head는 3, prev는 1)
        head = head.next
        prev = prev.next.next

    return root.next


# [ 풀이 3 ] 재귀 구조로 스왑
def swapPairs3(head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next  # p는 두 번째 노드 (2)

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