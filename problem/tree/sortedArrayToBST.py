import collections
from typing import List

# 50) 정렬된 배열의 이진 탐색 트리 변환
# 오름 차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
# 이 문제에서 높이 균형이란 모든 노드의 두 서브 트리 간 깊이 차이가 1 이하인 것을 말한다.
# 정렬된 배열 [-10,-3,0,5,9]이 주어졌을 때 가능한 답변은 [0,-3,9,-10,null,5]이다. 이와 같은 높이 균형 BST(이진 탐색 트리)로 나타낼 수 있다.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 이진 검색 결과로 트리 구성
# 정렬된 배열이 입력값으로 주어질때 균형 이진 탐색 트리로 변환하는 가장 일반적이고 효율적인 방법은 배열의 중앙 요소를 root 노드로 선택하는 것이다.
def sortedArrayToBST( nums: List[int] ) -> TreeNode:
    if not nums:
        return None

    # 중앙 값을 구한다.
    # 중앙 값에 해당되는 요소가 root 노드의 인덱스다. 예를 들어 len(nums)가 3이라면 2를 나눠 나온 결과인 1.5에서 내림하여 1이 된다.
    mid = len(nums) // 2

    # 위에서 구한 중앙 값을 루트 노드로 생성
    node = TreeNode(nums[mid])

    # 재귀를 통해 현재 노드의 왼쪽, 오른쪽 자식 노드를 구한다.
    # nums[:mid] : 시작(인덱스 0)부터 mid 직전까지의 요소들을 포함하는 새로운 배열을 생성. 중앙 값보다 작은 값들의 집합으로 왼쪽 서브 트리를 만드는데 사용.
    # 이렇게 되면 다음 재귀 에선 nums[:mid]의 중앙 값을 구하게 된다.
    # 왼쪽 서브 트리 노드에서 중앙값을 구하는 과정은 바로 그 서브 트리의 다음 루트 노드(즉, 현재 루트의 자식 노드)를 결정하는 과정인 것이다. 그래프를 보면 이해하기 쉽다.
    node.left = sortedArrayToBST(nums[:mid])
    # nums[mid + 1:] : mid+1부터 끝까지의 요소들을 포함하는 새로운 배열 생성. (mid+1하는 이유는 이미 mid는 root 노드로 생성되었음으로.)
    # 중앙 값보다 큰 값들의 집합으로 오른쪽 서브트리를 만드는데 사용한다.
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node

# 레벨 오더 순회 출력 함수 (결과 트리를 확인하기 위함)
def printTreeLevelOrder(root: TreeNode):
    if not root:
        print("[]")
        return

    output = []
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            output.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            # None (빈 노드)도 출력하여 구조를 시각적으로 확인
            output.append(None)

            # 맨 끝의 의미 없는 None 값들을 제거
    while output and output[-1] is None:
        output.pop()

    print(output)

if __name__ == "__main__":
    # 입력: [0,-3,9,-10,None,5,None]
    input = [ -10, -3, 0, 5 , 9]
    root = sortedArrayToBST(input)
    printTreeLevelOrder(root)
