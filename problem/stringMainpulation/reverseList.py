# 역순 연결 리스트
# 연결 리스트를 뒤집어라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# [ 풀이 1 ] 재귀 구조로 뒤집기.
def reverseList(head: ListNode) -> ListNode:
    # 함수 안에 함수를 정의하는 이유
    # reverseList 안에 reverse를 넣는 것은 단순히 코드를 정리하는 것을 넘어, 함수의 사용성과 안정성을 높이는 디자인 패턴.
    # 사용자가 알아야 할 가장 핵심적인 정보만 받도록 reverseList라는 간단한 인터페이스를 만들고, 복잡한 내부 로직은 reverse라는 내부 함수에 숨기는 것
    # reverse 함수는 reverseList 함수 내에서만 사용되는 일회성 로직이므로, 외부에 노출시키지 않아 코드를 더 깔끔하고 관리하기 쉽게 만든다.
    # 캡슐화 라고 생각하면 됨.
    def reverse(node: ListNode, prev: ListNode = None):
        # node가 None이 되면 = 리스트의 끝에 도달하면 prev를 반환.
        # prev는 마지막까지 연결이 완료된, 뒤집힌 리스트의 새로운 head
        if not node:
            return prev

        # 현재 노드의 다음 노드를 next_node 변수에 임시로 저장
        # 현재 노드의 연결을 끊기전에 다음 노드의 위치를 잃어버리지 않기 위함.
        next_node = node.next

        # 현재 노드의 next 포인터를 이전 노드(prev)를 가리키도록 변경합
        # node가 prev와 연결되어 리스트가 뒤집힘.
        node.next = prev
        # 재귀호출
        # reverse 함수를 다시 호출하면서 다음 노드였던 next_node를 새로운 현재 노드로 , 현재 노드였던 node를 새로운 이전 노드로 전달.
        return reverse(next_node, node)

    return reverse(head)

# [ 풀이 2 ] 반복 구조로 뒤집기
def reverseList2(head: ListNode) -> ListNode:
    # node : 현재 처리할 노드를 가리킴.
    node, prev = head, None

    # node가 None이 아닌 동안, 리스트의 끝에 도달할때까지
    while node:
        # next 에 node.next값을 넣어주고, prev에 node.next값을 저장.prev는 처음에 None임으로 처음에는 prev = None이 됨.
        next, node.next = node.next, prev
        # 다음 순회를 위해 포인터를 이동시킴.
        # prev는 현재 처리한 노드를 가르킴. node는 위에서 저장한 next값을 가르킴.
        prev, node = node, next
    return prev


# 연결 리스트를 순회하며 값을 출력하는 헬퍼 함수
def printList(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    # 첫 번째 함수 호출을 위한 리스트 생성
    l1_orig = ListNode(1)
    l1_orig.next = ListNode(2)
    l1_orig.next.next = ListNode(3)
    l1_orig.next.next.next = ListNode(4)
    l1_orig.next.next.next.next = ListNode(5)

    print("입력값 (original):", end=" ")
    printList(l1_orig)

    # reverseList 함수 호출 (l1_orig 사용)
    reversed_list = reverseList(l1_orig)
    print("reverseList 결과:", end=" ")
    printList(reversed_list)

    # 두 번째 함수 호출을 위한 새로운 리스트 생성
    l2_orig = ListNode(1)
    l2_orig.next = ListNode(2)
    l2_orig.next.next = ListNode(3)
    l2_orig.next.next.next = ListNode(4)
    l2_orig.next.next.next.next = ListNode(5)

    # reverseList2 함수 호출 (새로운 l2_orig 사용)
    reversed_list2 = reverseList2(l2_orig)
    print("reverseList2 결과:", end=" ")
    printList(reversed_list2)