import collections
import copy
from typing import List
# 52 ) 이진 탐색 트리 (BTS) 합의 범위
# 이진 탐색 트리(BST)가 주어졌을 떄 L이상 R이하의 값을 지닌 노드의 합을 구하라.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 재귀 구조 DFS로 부루트 포스 탐색
# DFS로 전체를 탐색한 다음 노드의 값이 L과 R 사이 일때만 값을 부여하고, 아닐 경우에는 0을 취해 계속 더해 나간다.
def rangeSumBST(root : TreeNode, L : int, R : int) -> int:
    if not root:
        return 0

    # (root.val if L <= root.val <= R else 0) : 현재 root의 값이 L이상 R 이하인지 확인한다. 조건을 만족하면 roo.val을 반환함.
    # (rangeSumBST(root.left, L,R)) : 현재 root 노드의 왼쪽 자식 값을 재귀 함수로 돌린다.
    # (rangeSumBST(root.right, L, R)) : 현재 root 노드의 오른쪽 자식 값을 재귀 함수로 돌린다.
    # 이런 식으로 가장 끝의 왼쪽, 가장 오른쪽 자식노드부터 root.val을 더해서 반환하기 시작한다.
    # 고로 최초의 재귀 함수에서는 왼쪽 서브 트리 중 L이상 R 이하 노드의 합, 오른쪽 서브 트리 중 L이상 R 이하 노드의 합이 반환된다.
    # 현재 노드 root.val + 왼쪽 서브 트리 중 L이상 R 이하 노드의 합 + 오른쪽 서브 트리 중 L이상 R 이하 노드의 합 이 되는 겻.
    return (root.val if L <= root.val <= R else 0) + (rangeSumBST(root.left, L,R)) + (rangeSumBST(root.right, L, R))

# [ 풀이 2 ] DFS 가지 치기로 필요한 노드 탐색
# DFS로 불필요한 노드는 가지치기를 통해 최적화를 진행 해보자. DFS로 탐색 하되 L,R의 조건에 해당하지않는 가지는 쳐내는 형태로 탐색에서 배제하도록 다음과 같이 구현한다.
def rangeSumBST2(root : TreeNode, L : int, R : int) -> int:

    def dfs(node : TreeNode):
        if not node:
            return 0

        # 이진 탐색 트리는 왼쪽이 항상 작고, 오른쪽이 항상 크다.
        # 즉, 현재 노드 root가 L보다 작을 경우, 더이상 왼쪽 가지는 탐색할 필요가 없다.
        # 고로 오른쪽만 탐색하도록 재귀 호출을 리턴한다.
        if node.val < L:
            return dfs(node.right)

        # R보다 클 경우, 오른쪽은 더이상 탐색할 필요가 없음으로 왼쪽만 탐색하도록 재귀 호출을 리턴한다.
        elif node.val > R:
            return dfs(node.left)

        # 만약 현재 노드 root의 값이 [L,R] 안에 있다면 이 노드는 합산해야 하므로
        # node.val을 포함하여 더 하고 양쪽 자식 노드를 모두 탐색해야한다.
        return node.val + dfs(node.left) + dfs(node.right)

    return dfs(root)

# [ 풀이 3 ] 반복 구조 DFS로 필요한 노드 검색
# 대부분의 재귀 풀이는 반복으로 변경할 수 있다. 이 문제 또한 반복으로 풀이 가능.
def rangeSumBST3(root: TreeNode, L: int, R: int) -> int:
    # 유효한 노드만 스택에 계속 집어넣으며 L과 R 사이의 값인 경우 값을 더해나간다.
    # 유효한 노드만 삽입하기때문에 앞서 풀이인 가지치기와 탐색 범위가 유사하며, 스택이므로 DFS로 동일한 탐색 구조를 띤다.

    # stack에는 root노드를 초기화 값을 넣는다.
    # 가지치기를 하더라도 일단 시작은 루트 노드에서 시작해야함.
    stack, sum = [root], 0

    while stack :
        node = stack.pop()

        if node:
            # 위의 풀이처럼 유효한 노드만 스택에 넣는다.
            # 이진 탐색 트리는 왼쪽이 항상 작고, 오른쪽이 항상 크다.
            # 즉, 현재 노드 root가 L보다 작을 경우, 더이상 왼쪽 가지는 탐색할 필요가 없다.
            # 고로 오른쪽만 stack에 넣어 탐색한다.
            if node.val > L :
                stack.append(node.left)

            if node.val < R :
                stack.append(node.right)

            # L과 R사이의 값일 경우 sum에 값을 누적한다.
            if L <= node.val <= R :
                sum += node.val

    return sum

# [ 풀이 4 ] 반복 구조 BFS로 필요한 노드 검색
# 스택을 단순히 큐 형태로 바꾸기만 하면 BFS를 구현할 수 있다. 원래는 파이썬의 데크를 사용해야 성능을 높일 수 있지만
# 편의상 간단히 리스트를 pop(0)(가장 앞의 요소부터 꺼내도록) 처리하는 정도로 다음과 같이 BFS를 구현할 수 있다.
def rangeSumBST4(root: TreeNode, L: int, R: int) -> int:
    stack, sum = [root], 0

    while stack:
        node = stack.pop(0) # 위의 풀이와 다른 부분. 가장 앞이 요소를 꺼냄으로서 큐 자료구조와 동일한 동작이 된다.
        if node:
            if node.val > L:
                stack.append(node.left)

            if node.val < R:
                stack.append(node.right)

            if L <= node.val <= R:
                sum += node.val

    return sum

def array_to_treenode( nums: List[int]) -> TreeNode:

    if not nums:
        return None

    # 1. 루트 노드 생성
    root = TreeNode(nums[0])

    # 2. BFS를 위한 큐 초기화
    queue = collections.deque([root])

    # 3. 배열 인덱스 초기화
    i = 1
    n = len(nums)

    # 4. BFS 순회 및 노드 연결
    while i < n and queue:
        parent = queue.popleft()

        # 왼쪽 자식 처리
        if i < n and nums[i] is not None:
            parent.left = TreeNode(nums[i])
            queue.append(parent.left)
        i += 1

        # 오른쪽 자식 처리
        if i < n and nums[i] is not None:
            parent.right = TreeNode(nums[i])
            queue.append(parent.right)
        i += 1

    return root

if __name__ == "__main__":
    # 입력값
    root = [10,5,15,3,7,None,18]
    L,R = 7,15
    # 출력값 : 32
    # 7이상 15이하인 다른 노드는 10이 있으며 따라서 결과는 7 + 10 + 15 = 32 가 된다.

    input1 = array_to_treenode(root)

    print("rangeSumBST 출력 값 : ", rangeSumBST(copy.deepcopy(input1), L, R), " |   기대 출력값 : 32")
    print("rangeSumBST2 출력 값 : ", rangeSumBST2(copy.deepcopy(input1), L, R), " |   기대 출력값 : 32")
    print("rangeSumBST3 출력 값 : ", rangeSumBST3(copy.deepcopy(input1), L, R), " |   기대 출력값 : 32")
    print("rangeSumBST4 출력 값 : ", rangeSumBST4(copy.deepcopy(input1), L, R), " |   기대 출력값 : 32")

