import collections
import sys
from typing import List
# 53 ) 이진 탐색 트리(BST) 노드 간 최소 거리
# 두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.
# 입력값 : root = [4,2,6,1,3,None,None]  출력값 : 1
# 노드 3과 노드 4의 값의 차이는 1이다.
# 입력값2 : root2 = [10,4,15,1,8,None,None]   출력값 : 2
# 이 경우 노드 간 값의 차이가 가장 작은 노드는 8과 10이다. 1과 4는 거리 차이가 3이고 4와 8은 차이가 4지만 8과 10의 차이는 2로 최솟값이다.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 재귀 구조로 중위 순회(왼쪽 → 부모 → 오른쪽).
# 값의 차이가 가장 작은 노드를 찾으려면 어디와 어디를 비교해야하는지 생각해봐야한다. BST는 왼쪽 자식은 항상 부모 보다 작고 오른쪽 자식은 항상 부모보다 크다.
#              D (Root)
#             / \
#            C   G
#           / \
#          B   E
#         / \ / \
#        A  F H  I
# 이렇게 생긴 BST가 있다고 할때 루트 D와 가장 차이가 작을 수 있는 노드는 딱 2개만 가능한데 I와 G이다
# 이외에는 항상 I와 G보다 값의 차이가 클 것이다. D->B의 차이는 D->C보다는 무조건 크다. 왼쪽으로 갈 수록 값이 작아지기때문이다.
# D->A, D->F도 D->C 보다 작아질 수 없다. 따라서 D->B부터는 제외한다.
# D->E 하위 노드들의 경우, D->H는 D->E보다 무조건 크기때문에 마찬가지로 최소값이 커진다.
# 오른쪽 값은 더 큰 값을 가지기때문에 왼쪽 서브 트리에선 D->I가 가장 작은 값이 될 수 있다.
# 그리고 의외로 D->G가 가장 작은 값이 될 수 도 있는데 여기서는 D->I와 D->G 중 작은 값을 택하면 정답이 된다.
class Solution:
    def __init__(self):
        # 인스턴스 변수로 정의하여 각 인스턴스마다 독립적인 값을 가짐

        # -sys.maxsize: 이는 파이썬에서 사용할 수 있는 가장 작은 정수 값으로 초기값 설정
        # self.prev는 중위 순회 시 바로 직전에 방문한 노드의 값을 저장하는 역할을 합니다. BST의 노드 값은 음수가 될 수도 있고, 0 또는 양수가 될 수도 있기때문에 0으로 초기화 하면 안됨.
        self.prev = -sys.maxsize # 중위 순회(Inorder Traversal) 과정에서 바로 직전에 방문했던 노드의 값

        # min(self.result, root.val - self.prev)으로 값을 비교해야해서 result를 0으로 초기화하면 result가 계속 선택되어버려서 안됨.
        # sys.maxsize: 이는 파이썬에서 사용할 수 있는 가장 큰 정수 값으로 초기값 설정
        self.result = sys.maxsize # 지금까지 발견된 노드 값들 간의 최소 차이를 저장.

    def minDiffInBST(self, root : TreeNode ) -> int:

        # 왼쪽 중위 순회.
        # 왼쪽노드 값이 있으면
        if root.left:
            # 재귀 호출을 호출하여 이대로 타고 리프 노드까지 탐색
            self.minDiffInBST(root.left)

        # 2. 부모 처리 (차이 계산 및 prev 업데이트)
        # 현재 노드 root의 값에 바로 중위순회로 바로 직전에 방문했던 노드의 값을 뺸다.
        # 여기서 바로 직전에 방문했던 노드이 값을 빼는 이유는 중위 순회를 했기때문이다.
        # BST의 노드 값들을 오름차순으로 정렬된 상태로 얻는 유일한 방법은 중위 순회를 하는 것이다.(왼쪽 → 부모 → 오른쪽).
        # 고로 1,2,3,4 이런 식으로 오름 차순으로 방문이 가능하다.
        self.result = min(self.result, root.val - self.prev)
        # 현재 노드 root를 다음 재귀 회귀에서 prev로 쓰기위해 값을 재할당
        self.prev = root.val

        # 3. 오른쪽 탐색
        if root.right:
            self.minDiffInBST(root.right)

        return self.result

# [ 풀이 2 ] 반복 구조로 중위 순회(왼쪽 → 부모 → 오른쪽)
# 반복은 재귀보다 직관적이여서 이해하기 쉽다. [ 풀이 1 ]과 비교 순서는 동일하다.
# 재귀 일때는 prev와 result를 클래스 멤버 변수로 선언했지만 반복 구조에서는 한 함수내에서 처리할 수 있어 함수 내 변수로 선언이 가능하다.
def minDiffInBST2( root : TreeNode) -> int:
    prev = -sys.maxsize
    result = sys.maxsize

    stack = [] # 아직 방문하지않은 부모 노드들을 임시로 저장하는 스택
    node = root

    while stack or node :

        while node:
            stack.append(node)
            # 현재 노드를 왼쪽 자식 노드로 이동.
            # 이를 통해 가장 왼쪽 리프 노드까지 탐색 경로의 모든 노드가 스택에 쌓이게 된다.
            node = node.left

        # 스택에 가장 마지막에 들어간 노드, 즉 아직 처리하지안흔 가장 작은 값을 가진 노드를 꺼낸다.
        node = stack.pop()

        # 현재 노드의 값(node.val) -  직전 노드의 값(prev)
        result = min(result, node.val - prev)
        # 현재 노드의 값을 다음 순서를 위해 prev에 저장한다.
        prev = node.val

        # 현재 처리한 노드의 오른쪽 자식으로 이동.
        # 만약 오른쪽 자식이 있다면 (node가 None이 아니라면), 메인 루프의 다음 반복에서 while node: 반복문으로 들어가 해당 서브트리의 가장 왼쪽 노드까지 다시 탐색하고 스택을 채우게 된다.
        # 오른쪽 자식이 없다면 (node가 None이라면), 메인 루프의 다음 반복에서 while node: 루프는 건너뛰고, 스택에서 다음 부모 노드를 꺼내 처리한다.
        # 그래서 첫 while stack or node :반복 시에는 왼쪽 서브 트리의 노드가 stack에 들어가게 된다. 리프 노드에 도달하면 node = node.right이 None임으로
        # while node: 가 동작하지않아 바로 node = stack.pop()이 동작하는데 이때, root 노드가 pop()되며 그 뒤부턴 오른쪽 서브 트리를 탐색하게 된다.
        node = node.right

    return result

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
    root = [4,2,6,1,3,None,None]
    root2 = [10,4,15,1,8,None,None]
    root_tree = array_to_treenode(root)
    root_tree2 = array_to_treenode(root2)

    sol = Solution()
    result1_1 = sol.minDiffInBST(root_tree)
    result1_2 = minDiffInBST2(root_tree)

    sol2 = Solution()
    result2_1 = sol2.minDiffInBST(root_tree2)
    result2_2 = minDiffInBST2(root_tree2)

    print("재귀 구조 : ", result1_1, "   : 기대 출력값 : 1 " )
    print("재귀 구조 : ", result1_2, "   : 기대 출력값 : 1 " )
    print("============================================")
    print("재귀 구조 : ", result2_1, "   : 기대 출력값 : 2 " )
    print("반복 구조 : ", result2_2, "   : 기대 출력값 : 2 " )
