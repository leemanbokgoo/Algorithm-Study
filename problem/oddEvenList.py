# 역순 연결 리스트
# 연결 리스트를 홀수번째 노드 다음에 짝수번째 노드가 오도록 재구성하라. 공간복잡도 O(1), 시간복잡도 O(n)에 풀이하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 ] 반복 구조로 홀짝 노드 처리
# 연결 리스트의 노드를 홀수 번째와 짝수 번째 인덱스에 따라 분리한 후, 홀수 리스트 뒤에 짝수 리스트를 연결하여 재구성
def oddEvenList(head: ListNode) -> ListNode:

    # 예외처리
    if head is None:
        return None

    odd = head # 홀수 리스트
    even = head.next # 짝수 리스트
    # 짝수 리스트 전체를 나중에 홀수 리스트 뒤에 붙이기 위해, 짝수 리스트의 시작(2)을 저장
    # even이 while문을 거치고 나면 짝수 리스트의 끝부분을 가리킬 수 있으니까 head부분을 따로 저장
    even_head = head.next

    #  짝수 리스트에 최소한 두 개의 노드가 존재할때까지 실행
    while even and even.next :
        # odd.next에 odd.next.next를 넣는다. odd(홀수), odd.next(짝수), odd.next.next(홀수)
        # even(짝수) even.next(홀수) even.next.next(짝수)
        odd.next, even.next = odd.next.next, even.next.next
        # 포인터의 다음 위치로 이동, 한칸 씩 이동하는 것.
        odd, even = odd.next, even.next

    # while문이 끝나고 odd는 홀수 리스트의 끝.
    # 홀수 리스트 끝에 짝수 리스트의 첫부분을 붙여주는 것.
    odd.next = even_head
    return head

# 연결 리스트 생성
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

# 연결 리스트 출력
def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print("->".join(vals))


if __name__ == "__main__":
    # 입력값 1: 1->2->3->4->5->NULL
    head1 = build_linked_list([1, 2, 3, 4, 5])
    res1 = oddEvenList(head1)
    print_linked_list(res1)  # 기대: 1->3->5->2->4

    # 입력값 2: 2->1->3->5->6->4->7->NULL
    head2 = build_linked_list([2, 1, 3, 5, 6, 4, 7])
    res2 = oddEvenList(head2)
    print_linked_list(res2)  # 기대: 2->3->6->7->1->5->4