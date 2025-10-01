from typing import List, Optional
import heapq
# k개 정렬 리스트 병합
# k개의 정렬된 리스트를 1개의 정렬된 리스트로 병합하라.
# [1->4->5, 1->3->4, 2->6]가 입력값이라면 여기서 k는 3이다.

# 연결 리스트의 노드 정의 (ListNode 클래스)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# [ 풀이 1 ] 우선순위 큐를 이용한 리스트 병합
# 대부분의 우선 순위 큐 풀이에 거의 항상 heapq 모듈을 사용하므로 잘 파악해두는게 좋다.
# 왜 PriorityQueue를 사용하지않는 이유는 PriorityQueue는 내부적으로 heapq 모듈을 사용한다.
# 다만, 둘의 차이는 PriorityQueue는 스레드 세이프 클래스라는 점이다. heapq는 스레드 세이프를 보장하지않는다.
# 파이썬은 GIL의 특성상 멀티 스레딩이 거의 의미가 없기때문에 대부분 멀티 프로세싱으로 활용한다는 점을 생각해보면 PriorityQueue의 멀티 스레딩 지원은 사실 큰 의미가 없다.
# 또한 스레드 세이프를 보장한다 = 내부적으로 락킹을 제공한다는 의미 = 락킹 오버헤드가 발생해 성능에 영향을 끼친다.
# 따라서 굳이 멀티 스레드로 구현할 게 아니라면 PriorityQueue 모듈은 사용할 필요가 없다.
def mergeKLists(lists: List[ListNode]) -> ListNode:

    # root : 더미 헤드를 가리키며, 최종 결과 (root.next)를 반환하는 데 사용
    # result : 현재 병합된 리스트의 마지막 노드를 가리키는 포인터로, 새로운 노드가 추가될 때마다 이동하며 리스트를 확장함.
    root = result = ListNode(None)
    # heap : 파이썬의 heapq 모듈로 관리될 최소 힙. 값, 리스트_인덱스, 노드_객체) 순서로 저장
    heap = []

    # lists에 들어있는 k개의 연결 리스트를 순회한다.
    # 힙 초기화 : 모든 리스트의 첫 번째 노드를 힙에 추가한다. 각 리스트의 첫 번째 노드만 힙에 넣는다.
    for i, node in enumerate(lists):
        if node:
            # ListNode 객체는 비교할 수 없으므로, 값이 같을 때 비교할 인덱스(i)를 중간에 넣는다.
            # node.val : 힙의 정렬 기준이 됨. 항상 튜플의 첫번째 요소가 최소 힙의 기준이다.
            # i : 같은 값을 가진 두 노드가 힙에 들어갈 경우, 파이썬의 heapq는 두 번째 요소(i)를 비교, 이 인덱스가 없으면 ListNode 객체 자체를 비교하려다가 오류가 발생함
            # node : 이 노드를 결과 리스트에 실제로 연결해야 하므로 저장해둔다.
            #  (node.val, i, node) : 이런 식으로  쉼표로 구분된 값들을 괄호 () 안에 넣으면 튜플(tuple)이 된다.
            heapq.heappush(heap, (node.val, i, node))

    # while heap : 루프는 힙이 완전히 빌 때까지, 즉 모든 리스트의 모든 노드가 처리될 때까지 반복
    while heap:
        # heapq.heappop(heap) : 현재 힙에 있는 모든 노드 중 "가장 작은 값"을 가진 노드 튜플을 꺼낸다. 이 값이 병합된 리스트의 다음 노드가 된다.
        # val, idx, node는 아까 위에서 넣은 heap, (node.val, i, node) 이 값들임.
        val, idx, node = heapq.heappop(heap)

        # 추출한 노드를 결과 리스트에 연결
        result.next = node
        # result 포인터를 방금 추가된 노드로 이동, 다음 노드를 받을 준비를 함.
        result = result.next

        # 추출한 노드의 다음 노드를 확인
        next_node = node.next

        #  다음 노드가 존재하면, 힙에 추가하여 다음 최소값을 찾을 준비를 한다.
        # 그러니까 즉, 위의 for문에서 넣어준 첫번째 노드 다음의 노드를 넣어주는 것이다. Lists 1의 노드 1 의 다음인 노드 4가 heap에 들어간다.
        # while문을 반복하면서 가장 작은 값이 꺼내지고, 다시 그 작은 값이 존재한 배열의 next 노드 값이 heap에 들어가고를 반복하다보면 정렬이 된다.
        if next_node:
            heapq.heappush(heap, (next_node.val, idx, next_node))

    # 더미 헤드(root) 다음 노드가 실제 병합된 리스트의 시작입니다.
    return root.next

# 배열을 연결 리스트로 변환
def create_list(arr: List[int]) -> Optional[ListNode]:
    if not arr: return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# 연결 리스트를 문자열로 출력
def print_list(node: Optional[ListNode]):
    vals = []
    while node:
        vals.append(str(node.val))
        node = node.next
    return " -> ".join(vals)



if __name__ == "__main__":

    # 입력 리스트 생성
    list1 = create_list([1, 4, 5])
    list2 = create_list([1, 3, 4])
    list3 = create_list([2, 6])

    lists_to_merge = [list1, list2, list3]
    merged_list = mergeKLists(lists_to_merge)

    # 출력값 확인: 1->1->2->3->4->4->5->6
    print("입력값 [1->4->5, 1->3->4, 2->6]")
    print(f"출력값 (병합된 리스트):")
    print(print_list(merged_list))