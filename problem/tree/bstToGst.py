import collections
from typing import List, Optional
# 51 ) 이진 탐색 트리 (BTS)를 더 큰 수 합계 트리로
# BTS의 각 노드를 현재 값보다 더 큰 값을 가진 모든 노드의 합으로 만들어라.
# 입력값 : [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# 출력값 : [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 자신보다 더 큰 값을 가진 모든 노드의 합이 출력된다. 6의 경우 더 큰 값을 지닌 노드는 7,8이며 6+7+8 = 21 이 출력 노드가 된다.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 중위 순회로 노드 값 누적
# 자신보다 같거나 큰 값을 구하려면 자기 자신을 포함한 우측 자식 노드의 합을 구하면된다.
# BST의 우측 자식 노드는 항상 부모 노드보다 큰 값이기 때문이다.

    # 트리 출력
    def printTreeLevelOrder(self, root: TreeNode):
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

    def array_to_treenode( self, nums: List[int]) -> TreeNode:

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

    # 입력값 : [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
    # 출력값 : [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

    nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    sol = Solution()
    root = sol.array_to_treenode(nums)
    result = sol.bstToGst(root)

    print("기대 출력값 : [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]")
    sol.printTreeLevelOrder(result)