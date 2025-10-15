import collections
# 46 ) 두 이진 트리 병합
# 두 지인 트리를 병합하라. 중복되는 노드는 값을 합산한다.
# 트리 1 : 1-> 3,2 | 3-> 5
# 트리 2 : 2-> 1,3 | 1-> 4 | 3 -> 7

# 출력값 : 3-> 4,5 | 4-> 5,4 | 5->7
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 재귀 탐색
# 다양한 방식으로 풀이가 가능하지만 이번에는 간단한 재귀 풀이만 살펴본다.
# 탐색 순서를 본다면 후위 순회 임을 알수 있다.
def mergeTrees( t1 : TreeNode, t2 : TreeNode ) -> TreeNode:

    # 각각 이진 트리의 루트부터 시작해 합쳐나가면서 좌,우 자식 노드 또한 병합될 수 있도록 각 트리의 자식 노드를 재귀 호출한다.
    if t1 and t2:
        # t1의 값과 t2의 값을 더해서 새로운 노드를 만든다.
        node = TreeNode(t1.val + t2.val)
        # 재귀 호출을 통해 좌,우 노드들 매개 변수로 던저 자식 노드들도 병합한다.
        node.left = mergeTrees(t1.left, t2.left)
        node.right = mergeTrees(t1.right, t2.right)
        # node를 return 한다.
        # node를 return 하면 되는 이유는 재귀 호출이 진행되면서 가장 끝 리프 노드에 도달하면 그때부터 재귀 함수는 값을 return 하기 시작한다.
        # 최초로 호출한 재귀 함수 까지 값이 return 되면 이제 새로운 Tree가 완성 된 상태이다.(재귀 함수가 실행되면서 tree들을 연결한다.)
        # 최초로 호출한 재귀 함수의 node가 root 노드임으로 해당 노드가 최종적으로 return 되면 트리가 전부 return 되는 것이다.
        return node

    # 만약 둘중 어느 한쪽에 노드가 존재하지않는 다면
    else:
        # 존재하는 노드만 리턴하고 더이상 재귀 호출을 진행하지않는다.
        return t1 or t2

# 트리 출력
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
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    result = mergeTrees(t1, t2)
    print("기대 출력값 : [3, 4, 5, 5, 4, None, 7]")
    printTreeLevelOrder(result)


