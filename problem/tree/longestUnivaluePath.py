
# 44 ) 가장 긴 동일 값 경로
# 동일한 값을 지닌 가장 긴 경로를 찾아라.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 상태값 거리 계산 DFS
# 트리의 말단, 리프 노드까지 DFS로 탐색해 내려간 다음, 값이 일치할 경우 거리를 차곡차곡 쌓아 올려가며 백트래킹하는 형태로 풀이 할 수 있다.
class Solution:
    result : int = 0

    def longestUnivaluePath(self, root : TreeNode) -> int:
        def dfs(node : TreeNode):

            # 더이상 존재하지않는 노드까지 내려가면 다음과 같은 형태로 값을 리턴한다.
            # 여기까지 도달하면 리프 노드의 자식노드에 도달했다는 뜻인데 리프 노드는 자식 노드가 없음으로 0을 return 한다.
            if node is None:
                return 0

            # 이렇게 재귀 호출로 내려가면서 left, right가 각각 리프 노드에 도달하면, 그떄부터 값을 리턴받게 된다.
            # 재귀 호출로 왼쪽, 오른쪽 서브트리의 동일 값 경로 길이를 각각 계산한다.
            left = dfs(node.left)
            right = dfs(node.right)

            # 왼쪽 자식 노드가 존재하고, 왼쪽 자식 노드의 값이 현재 노드와 같으면 동일한 값을 지닌 경로라는 뜻이다.
            if node.left and node.left.val == node.val:
                # 거리를 + 1 증가한다.
                left +=1
            # 만약 왼쪽 자식 노드의 값이 노드와 다르다면, left를 0으로 초기화한다.
            else :
                left = 0

            # 오른쪽 노드가 존재하고 오른쪽 노드의 값이 현재 노드의 값과 동일하다면, 동일한 값을 지닌 경로다.
            if node.right and node.right.val == node.val:
                # 그러므로 거리를 +1 증가한다.
                right += 1

            # 하지만 아니라면 right를 0으로 초기화한다.
            else :
                right = 0

            # 결과(result) : 왼쪽 자식 노드와 오른쪽 자식 노드간 거리의 합
            # left + right : 현재 노드를 기준으로 왼쪽과 오른쪽으로 이어지는 동일 값 경로의 총 간선 수이다.
            # 기존의 결과 보다 크다면 현재 결과 값을 덮는다.
            # # 참고로 43번 문제는 양쪽 끝까지 연결 할 수 있어서 +2 하는데 현재 경로는 경로는 단방향으로만 내려갈 수 있는 동일 값 경로임으로 부모 노드 방향으로는 한쪽만 선택가능하다.
            # 고로  left + right + 2할 필요가 없이  left + right하면 된다.
            # 43번 문제 처럼 +2 하지않는 이유는 이미 위의 if문으로 left +=1 , right += 1 하고 있기떄문이다.
            # 이 문제는 동일한 값인 경우에만 간선의 갯수를 카운팅해야하기떄문이다.
            self.result = max(self.result, left + right)

            # 다음번 백트래킹 시 계산을 위해 앞서 문제와 유사하게 상태값(부모 함수의 반환값)을 셋팅해서 부모 노드로 올려준다.
            # 부모노드를 위해 현재까지의 거리를 리턴한다.
            # 자식 노드 값을 둘다 반환해야할 것 같지만 오른쪽, 왼쪽 자식 노드 중 큰 값을 리턴해야한다.
            # 그 이유는 현재 노드의 부모 노드에서는 현재 노드의 자식 노드를 양쪽 다 동시에 연결 할 수 없다.
            # 단방향임으로 양쪽 자식 노드 중 한쪽 자식만을 선택할 수 있다. 이는 트리의 특징이다. 따라서 둘중 큰 값을 상태값으로 리턴해준다.
            # 즉, return max(left, right)는 부모 방향으로 이어질 수 있는 한쪽 경로의 최대 거리를 의미한다.
            # 43번과 달리 +1 할 필요 없는 이유는 위의 if문에서 이미 간선을 더하고 있기때문이다.
            # 43번과 44번 둘다 반복문이 한번 돌때마다 +1을 하거나 +2하는 건 같지만 그 동작을 표현하는 코딩 방식이 다른 것 뿐이다.
            # 43번의 경우 한번 돌아가면 무조건 +1 해서 해당 노드와 부모 노드간의 간선을 이어주지만 44번은 조건이 있기때문에 이게 불가능해서 굳이 if문을 쓰는 것.
            return max(left,right)

        dfs(root)

        return self.result


if __name__ == "__main__":

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(5)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)

    root.right.right = TreeNode(5)

    sol = Solution()
    result = sol.longestUnivaluePath(root)

    # root에서 오른쪽 노드 끝까지 5->5->5로 가장 긴 이동거리가 2이다.
    print("입력 트리 구조: [5, 4, 5, 1, 1, 5]")
    print("출력값:", result, " | 기대값 : 2")  # 기대값: 2

    root2 = TreeNode(1)
    root2.left = TreeNode(4)
    root2.right = TreeNode(5)

    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(4)

    root2.right.right = TreeNode(5)

    result2 = sol.longestUnivaluePath(root2)

    # 왼쪽 리프 노드 4에서 형제 노드 4까지 4->4->4로 가장 긴 이동거리가 2이다.
    print("입력 트리 구조: [5, 4, 5, 4, 4, 5]")
    print("출력값:", result, " | 기대값 : 2")  # 기대값: 2

