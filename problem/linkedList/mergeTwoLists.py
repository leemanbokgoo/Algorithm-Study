# 두 정렬 리스트의 병합
# 장렬 되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [ 풀이 1 ] 재귀 구조로 연결
# 정렬된 리스트라는 점이 중요하다. 병합 정렬에서 마지막 조합 시 첫번쨰 값부터 차례대로 비ㅛㄱ
def mergeTwoLists( l1: ListNode, l2 : ListNode ) -> ListNode:

    # not l1: 만약 l1 리스트가 비어 있다면(끝에 도달했다면)
    # l2 and l1.val > l2.val : 만약 l2가 존재하고 l2의 현재 값이 l1의 현재 값보다 작다면
    if(not l1) or (l2 and l1.val > l2.val) :
        # 연결 리스트 전체가 변경됨. 시작 노드만 변경되는 것이 아님.
        # 정확하게는 l1 변수는 l1 연결리스트의 포인터를 값으로 가지고 있는데 12 시작 노드의 포인터로 값이 변경되면서 되면서 l2 연결리스트의 값을 가지게 되는 것.
        # l1 = 1->2->3 , l2 = 5-> 6 라면 l1은 5를 가르키게 됨. 이제 l1은 5 -> 6 리스트를 의미하고 l2는 1을 가르키게 됨. 이제 l2는 1 -> 2 -> 3 리스트를 의미함.
        l1, l2 = l2, l1

    # if l1: l1이 비어있지 않은 경우에만 다음 로직을 실행함. (재귀 호출의 끝에 도달하면 l1이 None이 된다.)
    if l1 :
        # l1은 전체 배열(또는 연결 리스트)을 통째로 가리키는 것이 아니라, 리스트의 시작점인 첫 번째 ListNode 객체의 메모리 주소를 담고 있는 변수입니다.
        # 현재 l1 노드의 next 값과 l2 연결리스트를 넘긴다 ex) mergeTwoLists(2->4, 1->3->4) 이런 형태로,
        # 이렇게 두 개의 리스트 중 하나라도 끝에 도달하면 재귀 호출이 종료된다.
        # 재귀 호출이 종료되면 이제 마지막 재귀 호출부터 차례대로 값을 반환하여 l1.next 에 값을 넣어준다.
        # 참고로 재귀호출이 5번 호출되었다고 가정하면 5번째부터 값을 반환하기 시작한다. 5 -> 4 -> 3 이런식으로 역순으로 값을 반환함.
        # 고로 5번쨰 호출의 값이 4라면 4-> None이 4->4 가 된다.( 4는 원래 l1이 가지고 있던 값)
        # 4번쨰 호출값이 반환되면 현재 l1의 값인 3에 4 -> 4 가 붙어 3->4->4 가 된다. l1 : 3 , l1.next :  4 -> 4 => l1 = 3-> 4 -> 4
        # [[ 참고 ]] l1.next를 하게 되면 l1의 첫번째 노드의 next 값을 의미한다. 즉 l1.next = mergeTwoLists(l1.next , l2) 할때
        # 만약 l1의 값이 1->2고, mergeTwoLists(l1.next , l2)의 값이 3->4 라면 1->3->4 가 된다.
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