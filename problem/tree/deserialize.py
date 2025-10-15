import collections

# 47 ) 이진 트리 직렬화 & 역직렬화
# 이진 트리를 배열로 직렬화 하고 반대로 역직렬화 하는 기능을 구현하라.
# 입력값 : 1 -> 2,3 | 3 -> 4,5
# 즉, 다음과 같은 트리는 [1,2,3,null,null,4,5] 형태로 직렬화 할 수 있을 것이다.

import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# [ 풀이 1 ] 직렬화 & 역직렬화 구현
# BFS , DFS 둘다 상관없지만 이진 트리를 BFS로 표현하면 순서대로 배치 되기때문에 DFS에 비해 매우 직관적으로 알아 볼수 있음으로 BFS 사용.
class Codec:

    # BFS를 사용한 레벨 순회(Level-Order Traversal) 직렬화
    # 트리를 문자열로 변환
    def serialize(self, root: TreeNode) -> str:
        # 비어있는 노드 일 경우 none 대신 #으로 표현함.
        if not root:
            return "#"

        # BFS로 풀이하기 위해 큐 사용.
        queue = collections.deque([root])
        result = [] # 결과를 저장할 변수

        while queue:

            # 가장 앞쪽의 노드를 추출
            node = queue.popleft()

            if node:
                # 문자열로 변환하여 result에 node의 값을 추가
                result.append(str(node.val))

                # 현재 node의 자식 노드를 큐에 추가하여 다음 반복문에 자식 노드를 꺼내서 작업하도록 한다.
                queue.append(node.left)
                queue.append(node.right)

            else:
                # 노드가 존재하지않을 경우 '#'로 표시
                result.append('#')

        return ' '.join(result)

    # BFS를 사용한 역직렬화
    # 문자열을 트리 형태로 변환
    def deserialize(self, data: str) -> TreeNode:

        # 빈 노드일 경우 None을 반환
        if data == '#':
            return None

        # 문자열을 잘라서 배열로 생성
        nodes = data.split()

        # 첫 번째 노드 (루트) 생성
        # nodes[0]은 항상 루트 노드 값이어야한다.
        root = TreeNode(int(nodes[0]))

        # BFS를 하기 위해 큐를 생성
        queue = collections.deque([root])
        index = 1  # 루트 노드를 위에서 생성했음으로 그 다음 노드(루트 노드의 left 자식 노드)의 인덱스 부터 시작.

        # 큐에 노드가 존재하는 동안 and 인덱스가 nodes 배열 길이 보다 작을 떄까지 즉, nodes에 값이 존재할떄까지
        while queue and index < len(nodes):
            # 현재 큐의 가장 앞에 있는 노드 추출
            node = queue.popleft()

            # 1. 왼쪽 자식 처리
            if nodes[index] != '#':
                # 현재 노드의 왼쪽 자식 노드에 nodes에서 꺼낸 왼쪽 자식 노드의 값을 treeNode로 만들어 넣어준다.
                node.left = TreeNode(int(nodes[index]))
                # 생성한 자식 노드를 큐에 넣어 다음 반복문에 자식 노드가 현재 노드가 되어 위의 코드 동작을 타도록 만든다.
                queue.append(node.left)

            # 왼쪽 자식 노드를 처리했으니 +1 하여 오른쪽 자식 노드를 처리하도록 한다.
            index += 1

            # 2. 오른쪽 자식 처리
            # 위의 왼쪽 자식 노드는 index < len(nodes):로 인덱스 범위가 체크 되었지만 오른쪽 노드는 안되었음으로 인덱스 범위를 넘어서지않았는지 체크한다.
            if index < len(nodes):
                # 현재 오른쪽 자식 노드의 값이 있ㄷ면
                if nodes[index] != '#':
                    # 오른쪽 자식 노드를 만들어서 현재 node에게 할당한다.
                    node.right = TreeNode(int(nodes[index]))
                    # 큐에 넣어 똑같이 오른쪽 자식 노드도 다다음 반복문에서 현재 node가 되어 위의 코드 동작을 타도록 만든다.
                    queue.append(node.right)

                # index를 다음 칸으로 옮겨서 다음 현재 node의 왼쪽 자식을 가리키도록 바꾼다.
                # nodes에 [ 루트노드,왼쪽 자식노드, 오른쪽 자식노드, 왼쪽 자식 노드 , 오른쪽 자식노드 ] 이런 식으로 노드 트리가 저장되어있기떄문에 가능함.
                index += 1

        return root


if __name__ == "__main__":
    # 원본 트리 구성 (1 -> 2,3 | 3 -> 4,5)
    # 시각화:
    #     1
    #    / \
    #   2   3
    #      / \
    #     4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()

    # 1. 직렬화
    serialized_data = codec.serialize(root)

    # 2. 역직렬화
    deserialized_root = codec.deserialize(serialized_data)

    # 3. 역직렬화된 트리를 다시 직렬화하여 원본과 비교
    #    (트리 구조가 복원되었는지 확인하는 가장 쉬운 방법)
    reserialized_data = codec.serialize(deserialized_root)

    print("----- 이진 트리 직렬화 & 역직렬화 결과 -----")
    print(f"원본 트리: [1, 2, 3, null, null, 4, 5]")
    print("-" * 40)
    print(f"1. 직렬화 (Serialize) 결과:")
    print(f"   {serialized_data}")
    print("-" * 40)
    print(f"2. 역직렬화 후 재직렬화 결과 (복원 확인):")
    print(f"   {reserialized_data}")
    print("-" * 40)

# 출력 결과 (예상)
# ----- 이진 트리 직렬화 & 역직렬화 결과 -----
# 원본 트리: [1, 2, 3, null, null, 4, 5]
# ----------------------------------------
# 1. 직렬화 (Serialize) 결과:
#    1 2 3 # # 4 5 # # # #
# ----------------------------------------
# 2. 역직렬화 후 재직렬화 결과 (복원 확인):
#    1 2 3 # # 4 5 # # # #
# ----------------------------------------