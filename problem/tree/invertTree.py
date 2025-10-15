import collections
# 45 ) 이진 트리 반전
# 중앙을 기준으로 이진 트리를 반전시키는 문제다.
# 입력값 :  4-> 2,7 | 2-> 1,3 | 7 -> 6,9
# 출력값 : 4->7,2 | 7-> 6,9 | 2 -> 1,3

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# [ 풀이 1 ] 파이썬 다운 방식
# 재귀 함수로 해당 문제를 풀이 할 수 있다.
def invertTree(root: TreeNode) -> TreeNode:
    if root:
        # 루트 노드 부터 시작 하되 오른쪽 자식 노드부터 재귀 탐색을 진행
        # 노드 9게에서 첫번쨰 스왑이 일어나고(실제로는 그 자식인 None까지 탐색하다가 None을 리턴받은 이후에)
        # 두번쨰는 노드 6에서 스왑이 일어난다.
        root.left, root.right = invertTree(root.right), invertTree(root.left)
        return root
    return None

# 반복 구조로 BFS
def invertTree2(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # root 노드를 초기값으로 셋팅.
    queue = collections.deque([root])

    # 큐에 값이 존재할 동안
    while queue:
        # 큐에서 가장 앞에 있는 노드를 꺼내옴
        node = queue.popleft()

        # 노드가 존재한다면
        if node:
            # 노드의 left, right의 값을 스왑해줌.
            node.left, node.right = node.right, node.left

            # 큐에 현재 노드의 자식 노드들을 넣어서 다음 반복문에 자식 노드들을 처리할 수 있도록 해줌.
            queue.append(node.left)
            queue.append(node.right)
    return root

# [ 풀이 3 ] 반복 구조로 DFS
# 전위 순회 형태로 처리
def invertTree3(root: TreeNode) -> TreeNode:
    if not root:
        return None

    # DFS를 구현하기위해 stack으로 사용.
    stack = collections.deque([root])

    while stack:
        # 가장 마지막 노드를 pop
        node = stack.pop()

        if node:
            # 현재 노드의 왼쪽과 오른쪽 자식을 스왑
            node.left, node.right = node.right, node.left

            # 바뀐 자식들을 스택에 추가합니다. (순서: left, right)
            # stack.pop()은 right 자식부터 처리하게 된다.
            stack.append(node.left)
            stack.append(node.right)

    return root

# [ 풀이 4 ] 반복 구조로 DFS 후위 순회
# 풀이 3은 전위 순회 형태로 처리했지만 다음과 같이 후위 순회로 변경해도 문제가 없다. 그저 탐색 순서만 달라진다.
def invertTree4(root: TreeNode) -> TreeNode:
    if not root:
        return None

    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            # 풀이 3과 스왑 위치만 다를 뿐이다.
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left

    return root


# 1. 트리 복제 함수 (원본 트리를 보존하고 테스트용 복사본을 만들기 위함)
def cloneTree(root: TreeNode) -> TreeNode:
    if not root:
        return None

    new_root = TreeNode(root.val)
    new_root.left = cloneTree(root.left)
    new_root.right = cloneTree(root.right)
    return new_root


# 2. 레벨 오더 순회 출력 함수 (결과 트리를 확인하기 위함)
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
    # 원본 트리 구성 (예시: [4, 2, 7, 1, 3, 6, 9])
    original_root = TreeNode(4)
    original_root.left = TreeNode(2)
    original_root.right = TreeNode(7)
    original_root.left.left = TreeNode(1)
    original_root.left.right = TreeNode(3)
    original_root.right.left = TreeNode(6)
    original_root.right.right = TreeNode(9)

    # 예상 결과 (뒤집힌 트리): [4, 7, 2, 9, 6, 3, 1]

    print("--- 원본 트리 ---")
    printTreeLevelOrder(original_root)

    # 각 함수가 독립적으로 작동하도록 트리를 복제

    # 1. 재귀 (DFS) 방식 테스트
    root1 = cloneTree(original_root)
    result1 = invertTree(root1)
    print("\n--- invertTree (재귀) 결과 ---")
    printTreeLevelOrder(result1)

    # 2. BFS (반복) 방식 테스트
    root2 = cloneTree(original_root)
    result2 = invertTree2(root2)
    print("\n--- invertTree2 (BFS) 결과 ---")
    printTreeLevelOrder(result2)

    # 3. DFS (반복-Stack) 방식 테스트 1
    root3 = cloneTree(original_root)
    result3 = invertTree3(root3)
    print("\n--- invertTree3 (DFS Stack 1) 결과 ---")
    printTreeLevelOrder(result3)

    # 4. DFS (반복-Stack) 방식 테스트 2
    root4 = cloneTree(original_root)
    result34 = invertTree4(root4)
    print("\n--- invertTree4 (DFS Stack 2) 결과 ---")
    printTreeLevelOrder(result34)