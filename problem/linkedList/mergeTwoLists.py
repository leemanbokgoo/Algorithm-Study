# 두 정렬 리스트의 병합
# 장렬 되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [ 풀이 1 ] 재귀 구조로 연결
# 정렬된 리스트라는 점이 중요하다. 병합 정렬에서 마지막 조합 시 첫번쨰 값부터 차례대로 비교
def mergeTwoLists( l1: ListNode, l2 : ListNode ) -> ListNode:

    # not l1: 만약 l1 리스트가 비어 있다면(끝에 도달했다면)
    # l2 and l1.val > l2.val : 만약 l2가 존재하고 l2의 현재 값이 l1의 현재 값보다 작다면
    # 이 블록이 끝나면 l1이 두 노드 중 더 작거나 같은 값을 가진 노드를 가리키게 된다. 이 노드 l1이 현재 재귀호출이 반환할 노드, 즉 병합 리스트의 다음 요소가 된다.
    if(not l1) or (l2 and l1.val > l2.val) :
        # l2과 l1의 값을 교환한다.
        l1, l2 = l2, l1

    # if l1: l1이 비어있지 않은 경우에만 다음 로직을 실행함. (재귀 호출의 끝에 도달하면 l1이 None이 된다.)
    # 현재 이 l1은 위의 if문에서 선택한 가장 작은 노드이다. 이 노드의 다음(l1.next)를 결정해야한다.
    if l1 :
        # 현재 노드 l1을 제외한 나머지 l1 => l1.next 와 l2를 재귀 호출하여 다음에 올 노드를 선정한다.


        l1.next = mergeTwoLists(l1.next , l2)

    return l1

# 연결 리스트를 순회하며 값을 출력하는 헬퍼 함수
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    # 입력값 : 1->2->4, 1->3->4
    # 출력값 : 1->1->2->3->4->4

    # 입력값 생성
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    merged_list = mergeTwoLists(l1, l2)

    print("병합된 리스트:")
    printList(merged_list)