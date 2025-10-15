import collections

# 48 ) 균형 이진 트리
# 이진 트리 높이가 균형인지 판단하라
# 높이 균형은 모든 노드의 서브 트리간의 높이 차이가 1 이하 인것을 말한다.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 재귀 구조로 높이 차이 계산
def isBalanced(root : TreeNode) -> bool:

    def check(root):
        # 맨 마지막 노드에 도달하면 0을 리턴한다.
        if not root:
            return 0

        # 재귀 호출로 리프 노드까지 내려간다.
        left = check(root.left)
        right = check(root.right)

        # left, right 둘중 하나라도 -1의 값이라면(즉, 재귀 함수의 반환값에서 -1를 반환 받았다면) 불균형 상태다.(높이 차이가 1이상이다.)
        # abs(left - right) : left에서 right를 뺀 결과의 절댓값을 반환. 음수일 경우 양수로 반환 즉, left와 right 값 가이의 순수한 차이를 나타낸다.
        # abs(left - right) > 1 : 현재 노드의 왼쪽 서브트리 높이(left)와 오른쪽 서브트리 높이(right)의 차이가 2 이상라는 의미이다.
        # 서브 트리간의 높이 차이가 1 이하라는 조건을 위반한 것.
        # 즉 양쪽 노드 중 어느하나가 -1 이 되는 경우 계속해서 -1을 리턴하게 된다.
        # 각 서브 트리 높이 차이가 한번이라도 1을 초과하는 경우 -1이 할당되며 계속해서 재귀 함수 반환값으로 -1를 리턴한다.
        if left == -1 or right == -1 or abs(left - right) > 1:
            # 불균형 트리(= 서브 트리 간의 높이 차이가 1 이상)임으로 -1 반환.
            return -1

        # 예를 들어 left와 right가 모두 0이라면, 차이가 1보다 크지않으므로 max(0, 0) + 1로 1을 리턴하게 된다.
        # 이런 식으로 재귀 함수가 한번씩 종료될때마다(리프 노드에 도달해서 위로 올라갈때마다) + 1하면서 해당 노드의 높이를 나타내게 된다. 1->2->3....
        return max(left, right) + 1

    #  check(root)의 반환 값이 -1와 같다면 false, 아닐 시 true
    return check(root) != -1


# 배열을 TreeNode 구조로 변환하는 헬퍼 함수
def list_to_tree(arr):
    if not arr or arr[0] is None:
        return None

    # 루트 노드 생성
    root = TreeNode(arr[0])
    queue = collections.deque([root])
    i = 1

    while queue and i < len(arr):
        parent = queue.popleft()

        # 1. 왼쪽 자식 처리
        if i < len(arr) and arr[i] is not None:
            parent.left = TreeNode(arr[i])
            queue.append(parent.left)
        i += 1

        # 2. 오른쪽 자식 처리
        if i < len(arr) and arr[i] is not None:
            parent.right = TreeNode(arr[i])
            queue.append(parent.right)
        i += 1

    return root

if __name__ == "__main__":

    # 서브 트리간 높이 차이가 1 이하이므로 높이 균형이다. 따라서 true
    arr1 = [3, 9, 20, None, None, 15, 7]
    # 1의 왼쪽 서브트리 2와 오른쪽 2는 높이차이가 2다. 따라서 false
    arr2 = [1, 2, 2, 3, 3, None, None, 4, 4]

    # 헬퍼 함수를 사용하여 트리 객체 생성
    root1 = list_to_tree(arr1)
    root2 = list_to_tree(arr2)

    print("root1 결과 : ", isBalanced(root1), "  |   기대값 : True")
    print("root2 결과 : ", isBalanced(root2), "  |   기대값 : False")

