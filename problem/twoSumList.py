from typing import List
from problem.isPalindrome import ListNode
# 두 수의 덧셈
# 역순으로 저장된 연결 리스트의 숫자를 더하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 자료형 변환
def addTwoNumbers_sol1(l1: ListNode, l2: ListNode) -> ListNode:
    class Solution:
        def reverseList(self, head: ListNode) -> ListNode:
            node, prev = head, None

            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node

            return prev

        def toList(self, node: ListNode) -> list:
            lst = []
            while node:
                lst.append(node.val)
                node = node.next
            return lst

        def toReversedLinkedList(self, result: str) -> ListNode:
            prev = None
            for r in result:
                node = ListNode(int(r))
                node.next = prev
                prev = node
            return prev

        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
            a = self.toList(self.reverseList(l1))
            b = self.toList(self.reverseList(l2))

            result_str = str(int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b)))

            return self.toReversedLinkedList(result_str)

    return Solution().addTwoNumbers(l1, l2)

# [ 풀이 2 ] 전가산기 구현
def addTwoNumbers_sol2(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while l1 or l2 or carry:
        sum_val = 0
        if l1:
            sum_val += l1.val
            l1 = l1.next

        if l2:
            sum_val += l2.val
            l2 = l2.next

        carry, val = divmod(sum_val + carry, 10)
        head.next = ListNode(val)
        head = head.next
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

    print("--- Solution 1 ---")
    result1 = addTwoNumbers_sol1(l1, l2)
    print_linked_list(result1)  # Expected: 7->0->8

    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    print("\n--- Solution 2 ---")
    result2 = addTwoNumbers_sol2(l1, l2)
    print_linked_list(result2)  # Expected: 7->0->8