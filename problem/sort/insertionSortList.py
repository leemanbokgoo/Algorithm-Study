# 60 ) 삽입 정렬 리스트
# 연결 리스트를 삽입 정렬로 정렬하라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 삽입 정렬
def insertionSortList(head: ListNode) -> ListNode:

    # 삽입 정렬은 정렬 해야 할 대상과 정렬을 끝낸 대상, 두 그룹으로 나눠진행한다.
    # head : 정렬해야할 대상
    # cur : 정렬을 끝낸 대상. 정렬을 끝낸 연결 리스트를 추가해줄 것.
    # parent : 계속 그 위치에 두어 사실상 루트를 가리키게 한다.
    cur = parent = ListNode(None)

    while head:

        # cur.next의 값이 head.val 보다 작다면
        # 정렬을 끝낸 cur은 이미 정렬된 상태이므로 정렬해야할 대상 head와 비교하면서 더 작다면 계속 cur.next를 이용해 이동한다.
        while cur.next and cur.next.val < head.val :
            # cur = cur.next : 포인터를 옆의 노드로 이동하면서 cur이 head의 값과 작거나 같아질때까지 계속 이동한다.
            cur = cur.next

        # 정렬이 필요한 위치. 즉 cur에 삽입될 위치를 찾았다면 cur 연결 리스트에 추가한다.
        # head.next에는  cur.next를 연결 해 연결 리스트가 끊기지않고 이어지도록 한다.
        # head는 다음 값을 가리키며 다음 값으로 이동한다.
        cur.next, head.next, head = head, cur.next, head.next
        # cur는 다시 처음으로 돌아가면서 차례대로 다시 비교하게 된다.
        cur = parent

    # head가 None이 되면 비교가 끝난다.

    return cur.next

# [ 풀이 2 ] 삽입 정렬의 비교 조건 개선
# [ 풀이 1 ] 은 제대로 된 삽입 정렬 풀이가 아니다. 삽입 정렬은 정답 셋과 정답이 아닌 셋을 비교할때, 정답 셋의 가장 큰 값부터 왼쪽 방향으로 내려가며 스왑되는 위치를 찾는다.
# 그러나 이 문제의 경우 연결 리스트이고, 이중 연결 리슽도 아니기때문에 큰 값에서부터 작은 값까지 거꾸로 거슬려 내려가는게 사실상 불가능하다.
# 그러다 보니 매번 가장 작읍 값부터 차례대로 크기를 비교하는 매우 비효율적인 연산이 수행된다.
# 그럼으로 개선이 필요하다.
def insertionSortList2(head: ListNode) -> ListNode:
    cur = parent = ListNode(None)

    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        # 풀이 1 에서 cur = parent은 다음번 head를 비교할때 정렬된 노드인 cur도 다시 맨처음으로 돌아가라는 명령이다.
        # 만약 다음번 head도 cur보다 큰 상태라면 굳이 되돌아가지않아도 된다. 그렇게 되면 비교 횟수를 줄일 수 있다.
        # 필요할때만 되돌아가는 것이다. cur가 head보다 클때만 돌아가면 된다.
        # head가 None일 수 있기때문에 존재 여부 체크도 반드시 필요하다.
        if head and cur.val > head.val:
            cur = parent
    return parent.next


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
    sorted_li = insertionSortList(li)

    # 정렬된 연결 리스트를 문자열로 출력
    output_string = list_to_string(sorted_li)
    print(f"정렬된 연결 리스트: {output_string}")



