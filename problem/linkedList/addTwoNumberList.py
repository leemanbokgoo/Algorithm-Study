from typing import List
# 두 수의 덧셈
# 이 문제에서 각 연결 리스트의 노드는 숫자의 한자리수를 나타내며 숫자는 역순으로 저장되어있다.
# 2->3->1 라면 실제 값은 132.
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 자료형 변환
#  연결 리스트를 문자열로 변환하고, 두 숫자를 더한 다음, 그 결과를 다시 역순의 연결 리스트로 변환하여 반환하는 방식
def addTwoNumbersList1(l1: ListNode, l2: ListNode) -> ListNode:
    class Solution:

        # 입력받은 연결 리스트를 역순으로 뒤집는다.
        def reverseList(self, head: ListNode) -> ListNode:
            node, prev = head, None

            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node

            return prev

        # 연결 리스트를 파이썬 리스트로 변환.
        def toList(self, node: ListNode) -> list:
            lst = []
            while node:
                lst.append(node.val)
                # 한칸 이동
                node = node.next
            return lst

        # 덧셈 결과 문자열을 역순의 연결리스트로 변환한다.
        def toReversedLinkedList(self, result: str) -> ListNode:
            prev = None # 이전 노드를 가리키는 포인터 역할

            # 문자열을 for in 하면 각 자리수의 문자를 반환 ex) result가 문자열이라면 r은 r,e,s,u,l,t가 반복문으로 돈다.
            for r in result:
                # int(r) : 문자열을 정수형으로 반환.
                # ListNode() : 새로운 노드 생성
                node = ListNode(int(r))
                # 새로만든 노드의 next가 이전 단계에 만들어진 노드 prev를 가리키도록 설정
                node.next = prev
                # 현재 노드값을 prev에 넣어서 다음 반복문에 위의 코드가 정상적으로 작동할 수 있도록 함.
                prev = node
            return prev

        def addTwoNumbersList(self, l1: ListNode, l2: ListNode) -> ListNode:
            # 연결 리스트인 l1,l2를 역순으로 뒤집고 그 결과를 파이쎤 리스트로 변환.
            a = self.toList(self.reverseList(l1))
            b = self.toList(self.reverseList(l2))

            # 리스트 a와 b를 문자열로 합치고(''.join(...)), 이를 정수형으로 변환하여(int(...)) 원래 숫자를 얻는다.
            # 예를 들어 a = [3, 4, 2] → 문자열 '342' → 정수 342
            result_str = str(int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b)))

            # 덧셈 결과 문자열을 역순의 연결 리스트로 변환하여 반환
            # 덧셈 결과 문자열이 (ex '807')라면 결과는 7->0->8 인것.
            return self.toReversedLinkedList(result_str)

    return Solution().addTwoNumbersList(l1, l2)

# [ 풀이 2 ] 전가산기 구현
#  마치 사람이 손으로 덧셈을 하듯이 자릿수별로 더하고 올림(carry)을 처리하는 방식
# 연결 리스트의 길이와 상관없이 작동하며 숫자가 매우 클때 발생할 수 있는 오버 플로우 문제를 피할 수 있음
def addTwoNumbersList2(l1: ListNode, l2: ListNode) -> ListNode:

    # 변수 초기화
    # root (더미 헤드): 결과를 담을 새로운 연결 리스트의 시작을 가리키는 더미 노드.
    # 최종적으로는 root.next를 반환하여 실제 결과 리스트의 헤드를 반환하게 된다. 더미 노드를 사용하면 리스트의 첫 번째 노드를 특별히 처리할 필요가 없어 코드가 간결해짐.
    # head : 현재 위치 포인터. 결과 리스트(root가 가리키는 리스트)를 만들어 나갈 때, 새로운 노드를 연결할 현재 위치를 가리킨다. 초기에는 root를 가리킴.
    # carry : 이전 자릿수에서 발생한 올림 값(carry)을 저장하는 변수. 초기에는 올림이 없음으로 0
    root = head = ListNode(0)
    carry = 0

    # carry : 이전 덧셈에서 발생한 최종 올림이 1로 남아있는 경우
    while l1 or l2 or carry:

        # 현재 자릿수(ex 십의 자리,백의 자리 등)의 합을 계산하기 위해 sum_val을 0으로 초기화
        sum_val = 0

        # l1과 l2에 노드가 남아 있다면, 그 노드의 값(val)을 sum_val에 더하고, 포인터(l1, l2)를 다음 노드로 이동
        # 만약 한쪽 리스트가 먼저 끝나면, 해당 리스트의 값은 자연스럽게 0이 더해지는 효과가 난다.
        # 즉, 이 코드는 123+ 456할때 3+6 이런식으로 같은 순서에 있는 숫자들 끼리 더하고 있는 상황인 것.
        if l1:
            sum_val += l1.val
            l1 = l1.next

        if l2:
            sum_val += l2.val
            l2 = l2.next

        # sum_val + carry: 현재 자릿수의 값(두 리스트 노드 값의 합)에 이전 단계의 올림(carry)을 더 한다.
        # divmod(x, 10): 파이썬의 내장 함수로, x를 10으로 나눈 몫(carry)과 나머지(val)를 한 번에 반환.
        # 17+28 일때 두번째 자리인 7+8을 더하고 나면 값이 15인데 여기서 1은 십의 자리 계산 결과에 더해지고 나머지인 5가 일의 자리의 숫자다.
        carry, val = divmod(sum_val + carry, 10)

        # val 값을 가진 새로운 노드를 생성하고, 현재 결과 리스트의 끝에 연결한다.
        head.next = ListNode(val)
        # head 포인터를 새로 생성된 노드로 이동시켜, 다음 반복에서는 새로운 노드가 이 위치에 연결되도록 준비
        head = head.next

    # root는 처음에 만든 더미 노드이므로 0을 가리키고있다. 고로 더미값인 0 다음의 실제 덧셈 결과의 첫 노드인 root.next를 반환한다.
    # head와 root가 처음에 같은 연결 리스트 객체를 가리키고 있기 때문에 root와 head라는 두 개의 변수(포인터) 모두 동일한 객체를 가리키고있다.
    # 즉, head = [], root = [] 이런 식으로 각자의 값을 가지고 있는 것이 아니라 head,root = []이렇게 둘다 똑같은 메모리상의 연결 리스트를 가리키고있는 것.
    # 그렇기 떄문에 head에 값을 더하면 root에도 값이 더해진다.(같은 메모리상 주소를 가리키고있으니까)
    # 다만 while문이 끝나면 head 포인터는 해당 연결리스트의 끝을 가리키고 있고 root는 해당 연결리스트의 앞을 가리키고 있음으로 root.next를 반환하는 것.
    return root.next


def create_linked_list(nums: list) -> ListNode:
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head


def print_linked_list(head: ListNode):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print("->".join(result))


if __name__ == "__main__":
    # 입력값: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # 출력값 7->0->8
    # 설명: 342 + 465 = 807
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    print("--- [ 풀이 1 ] 자료형 변환 ---")
    result1 = addTwoNumbersList1(l1, l2)
    print_linked_list(result1)  # Expected: 7->0->8

    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    print("\n--- [ 풀이 2 ] 전가산기 구현 ---")
    result2 = addTwoNumbersList2(l1, l2)
    print_linked_list(result2)  # Expected: 7->0->8