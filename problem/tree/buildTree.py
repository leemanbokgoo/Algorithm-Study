import collections
from typing import List
# 54 ) 전위, 중위 순회 결과로 이진 트리 구축
# 트리의 전위,중위 순회 결과를 입력값으로 받아 이진 트리를 구축하라.
# 전위 순회 결과 : [ 3, 9, 20, 15, 7 ]
# 중위 순회 결과 : [ 9, 3, 15, 20, 7 ]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 전위 순회 결과로 중위 순회 분할 정복
# 전위, 중위, 후위 순회가 있으며 이 셋 중 2가지만 있어도 이진 트리를 복원할 수 있다.
# 전위의 첫번 째 값은 부모 노드다. 즉, 전위 순회의 첫 번쨰 결과는 정확히 정위 순회 결과를 왼쪽과 오른쪽으로 분할 시키는 역할을 한다.
def buildTree(preorder : List[int], inorder : List[int]) -> TreeNode:

    # 처리할 중위 순회 리스트가 비어있지 않는지 확인.
    # 전위 순회리스트가 비어있으면 해당 서브트리가 존재하지않는 다는 뜻
    if inorder:
        # 전위 순회의 첫번쨰 결과를 가져와 중위 순회를 분할하는 인덱스로 쓴다.
        # 전위의 첫번 째 값은 부모 노드 이기 떄문에 정위 순회의 결과를 왼쪽 서브트리와 오른쪽 서브트리로 정확하게 분할 수 있다.
        # 정위 순회 결과는 왼쪽,루트 노드, 오른쪽 이기때문.
        # 여기서 전위 순회 결과는 pop(0)으로 가장 첫번쨰 값을 가져온다. 즉, 큐 연산이다.
        index = inorder.index(preorder.pop(0))

        # 현재 서브트리의 루트 노드 생성. 중위 순회 리스트에서 찾은 인덱스 위치의 값(즉, 루트 노드 값)으로 새로운 TreeNode 객체를 생성한다.
        node = TreeNode(inorder[index])
        # 왼쪽 자식 노드 재귀적 생성.
        # preorder.pop(0)로 루트 노드 값을 이미 제거했기 때문에, 남은 preorder 리스트는 왼쪽 서브트리와 오른쪽 서브트리의 노드들로만 구성되어 있다.
        # inorder[0:index] : root 노드 인덱스(index) 앞 부분을 잘라낸다. 이 부분이 왼쪽 서브트리의 모든 노드이다.
        node.left = buildTree(preorder, inorder[0:index])
        # 오른쪽 자식 노드 재귀적 생성.
        # 왼쪽 서브트리 노드들을 재귀 호출에서 소비하고 남은 preorder 리스트가 전달된다.
        # 리스트의 첫 번째 노드가 오른쪽 서브트리의 루트 노드가 된다.
        #  [index + 1:] : 중위 순회 리스트에서 루트 노드 인덱스(index) 뒷 부분을 잘라낸다. 이 부분이 오른쪽 서브트리의 모든 노드이다.
        node.right = buildTree(preorder, inorder[index + 1:])
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

    # 전위 순회 결과 : [ 3, 9, 20, 15, 7 ]
    # 중위 순회 결과 : [ 9, 3, 15, 20, 7 ]
    # 결과 값 : [3, 9, 20, None, None, 15, 7 ]

    preorder = [ 3, 9, 20, 15, 7 ]
    inorder = [ 9, 3, 15, 20, 7 ]
    expected_result = [3, 9, 20, None, None, 15, 7 ]

    result = buildTree(preorder, inorder)
    print("              결과값                ")
    printTreeLevelOrder(result)
    print("           기대 결과값                ")
    print("[3, 9, 20, None, None, 15, 7 ]")
