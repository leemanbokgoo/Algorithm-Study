# 역순 연결 리스트 2
# 인덱스 m에서 n까지를 역수능로 만들어라. 인덱스 m은 1부터 시작한다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 반복 구조로 노드 뒤집기
# 연결 리스트의 특정 구간을 반복 구조를 사용하여 O(n) 시간에 역순으로 뒤집는 완벽하게 구현된 코드
def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 예외처리
    if not head or m == n:
        return head

    # root: 더미 노드 (Dummy Node)를 생성하여 head 노드 처리를 단순화
    # start: 뒤집기를 시작할 '앞' 노드 (m-1번째 노드), 고정된 기준점이 된다.
    root = start = ListNode(None)
    root.next = head

    # 이 코드에서 사용된 _ (밑줄)은 반복문 내에서 변수 값이 필요하지 않을 때 사용하는 관례적인 변수 이름
    # m-1번이ㅡ 반복 횟수 생성.
    # start를 m-1번째 노드까지 이동 m이 3이라면 2번째 노드까지 이동.
    for _ in range(m - 1):
        start = start.next

    # end: m번째 노드. 즉, 뒤집을 구간의 시작 노드.
    # 시작할때는 역순 구간의 첫번째 노드이지만 역순을 진행하면서 end는 역순 구간의 가장 끝부분이 된다.
    end = start.next

    # n-m : 뒤집는 횟수, 한 번의 반복마다 한 개의 노드에 대해 수행되므로, 총 n−m번 반복
    for _ in range(n - m):
        # tmp : start.next가 다른 노드로 바뀌기 때문에 원래 연결을 잃지 않으려면 미리 저장. 새로운 노드가 삽입되기 전의 start 뒤 노드로 현재까지 뒤집은 리스트의 맨 앞 노드임.
        # start.next = end.next : 최초의 end값이 가장 뒤로 가야함. 즉, end.next 값들이 순서대로 앞으로 가서 새로운 맨 앞 노드가 되어한다.
        # 1->2->3 일때 end가 2라면 end.next는 3이고 start.next = end.next하면 1->3->2 가 되는 것.
        # end.next = end.next.next : 방금 start 앞으로 end.next를 노드를 이동시켰기때문에 end.next.next를 end 다음 노드에 연결하여 리스트를 다시 연결함.
        tmp, start.next, end.next = start.next, end.next, end.next.next # ex) 1->4 3->2->5 대략 이런 상태
        # start.next는 방금 앞으로 당겨온 새로운 노드이다. 새로운 노드의 다음 노드를 tmp(이전에 맨 앞이던 노드)로 연결하여 현재의 역순 리스트 연결(새 노드→이전 노드)을 완성한다.
        start.next.next = tmp

    # 더미 노드의 다음, 즉 새로운 head를 반환
    return root.next


# 연결 리스트 생성 유틸리티 함수
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


# 연결 리스트 출력 유틸리티 함수
def print_linked_list(head):
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    return "->".join(vals)


if __name__ == "__main__":
    # 입력값 : 1->2->3->4->5->NULL, m=2, n=4
    # 뒤집을 구간: 2, 3, 4 (2->3->4 가 4->3->2 로 바뀐다)
    # 출력값 예상 : 1->4->3->2->5->NULL

    m_val = 2
    n_val = 4

    # 리스트 빌드
    input_values = [1, 2, 3, 4, 5]
    head = build_linked_list(input_values)

    print(f"입력: {print_linked_list(head)} (m={m_val}, n={n_val})")

    # 함수 실행
    reversed_head = reverseBetween(head, m_val, n_val)

    # 결과 출력
    print(f"출력: {print_linked_list(reversed_head)}")