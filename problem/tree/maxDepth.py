import collections
# 42) 이진 트리의 최대 깊이
# 이진 트리의 최대 깊이를 구하라.
# [3,9,20,None,None,15,7]가 주어졌을때 깊이는 3이다.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# [ 풀이 1 ] 반복 구조로 BFS 풀이
# BFS 레벨 순회는 각 레벨을 한 번에 처리하므로 레벨의 개수 = 트리 깊이가 된다.

def maxDepth(root: TreeNode) -> int:
    # 예외 처리
    if root is None:
        return 0

    # BFS를 구현할 떄 필요한 큐 선언.
    # 초깃값으로 root 노드를 넣어서 root 노드부터 깊이를 재기 시작한다.
    # deque를 쓰는 이유는 이중 연결 리스트로 구성되어있어 큐와 스택 연산 모두 가능하며 양방향 모두 O(1)에 추출 가능해서 성능이 좋다.
    queue = collections.deque([root])
    depth = 0 # 깊이 값 변수

    # while queue 루프가 한 번 돌 때마다 한 레벨를 처리하고 depth를 1 증가시키므로, 끝까지 돌면 전체 깊이가 된다.
    while queue:
        depth += 1 # 깊이를 하나 올리고 시작. 이 반복에 진입했다는 것은 "한 레벨가 존재한다"는 뜻임으로.

        # 현재 큐에 들어있는 원소 수(= 현재 레벨의 노드 개수)만큼 반복한다.
        for _ in range(len(queue)):
            #  queue.popleft() : 큐에서 가장 왼쪽(앞)의 원소를 꺼낸다. BFS(너비 우선 탐색)은 먼저 들어온 노드부터 처리하기때문.
            # cur_root : 현재 노드는 큐의 가장 앞쪽에 있는 원소다.
            cur_root = queue.popleft()

            # 밑의 코드에서 append된 자식 노드들은 현재 for의 반복 범위를 벗어난다.(처음에 len(queue)을 계산 할때는 현재 노드들은 없었음으로 계산 값에 포함되지않음)
            # 그러므로 다음 while 반복 시에 처리된다. 즉, 다음 레벨에서 처리된다.
            # ex) root만 큐에 있을때 len(queue)은 1이다. 그러므로 1번만 반복된다.
            if cur_root.left: # 현재 노드에 왼쪽 자식 노드가 존재한다면
                # 이 노드를 큐에 넣어 다음 반복문에 꺼낸다.
                queue.append(cur_root.left)
            if cur_root.right: # 큐에 오른쪽 자식 노드가 존재한다면.
                # 큐에 넣어 다음 반복문에 꺼낼 준비를 한다.
                queue.append(cur_root.right)

    # 모든 큐가 다 빌때까지 while문이 돌아가면 모든 레벨을 다 처리한 것임으로 누적된 depth 값을 반환합
    return depth


def build_tree(values):
    # values 값이 없을때 예외 처리
    if not values or values[0] is None:
        return None

    # 제일 첫번쨰 값으로 root 노드 생성
    root = TreeNode(values[0])
    # BFS(레벨 순서) 방식으로 자식들을 연결하기 위해 큐를 사용한다.
    # 초기시에는 루트 노드만 큐에 넣는다.
    queue = collections.deque([root])
    # 현재 리스트에서 처리할 인덱스, 가장 첫번째는 루트 노드로 이미 생성했음으로 인덱스 1부터 시작한다.
    i = 1

    #  while queue : 큐에 부모로 처리할 노드가 남아있고
    # i < len(values) : 아직 처리해야할 값이 리스트에 남아있을떄
    while queue and i < len(values):
        # 큐에서 다음 부모 노드를 꺼낸다. 왼쪽부터 순서대로 꺼냄.
        node = queue.popleft()

        # node에 대해 values[i]를 왼쪽 자식으로, values[i+1]을 오른쪽 자식으로 할당한다.
        # 단 값이 존재하고 None이 아닐 시에

        # i < len(values) : 리스트에 i 인덱스가 존재하는지 확인
        # values[i] is not None : 그 위치의 값이 None이 아니면 실제 노드를 생성해야함.
        if i < len(values) and values[i] is not None:
            # values[i]로 왼쪽 자식 노드를 생성해서 node.left에 연결
            node.left = TreeNode(values[i])
            # 방금 만든 왼쪽 자식을 큐에 추가한다. 나중에 그 노드를 부모로 꺼내어 그 자식들의 자식들을 연결하게 된다.
            queue.append(node.left)

        # 왼쪽 자식값 처리를 마쳤으므로 인덱스 i를 다음 위치(오른쪽 자식 후보)로 옮긴다.
        # 여기서 values[i]가 None이어서 자식을 만들지 않았더라도 항상 i는 증가한다. 리스트의 자리를 소비했기 때문이다.
        i += 1

        # 오른쪽 자식 노드에 대해 똑같이 리스트에 i 인덱스가 존재하는지 확인.
        # 그 위치의 값이 None이 아니라면 실제 노드를 생성.
        if i < len(values) and values[i] is not None:
            # 오른쪽 자식 노드를 생성하여 node.right에 연결
            node.right = TreeNode(values[i])
            # 만든 오른쪽 자식 노드도 큐에 넣는다. 해당 노드의 자식 노드를 연결 하기 위함.
            queue.append(node.right)

        # 오른쪽 자식 자리까지 처리했음으로 인덱스를 한 칸 더 올린다.
        # 이제 다음 반복문에서 큐의 다음 부모와 values[i] 값으로 계속한다.
        i += 1
    # 모든 처리가 끝나면 루트 노드를 반환한다. 이 루트 노드에서부터 연결된 전체 트리를 사용할 수 있다.
    return root


if __name__ == "__main__":
    # 입력: [3,9,20,None,None,15,7]
    tree_values = [3, 9, 20, None, None, 15, 7]
    root = build_tree(tree_values)

    print("입력값:", tree_values)
    print("출력값:", maxDepth(root) , " | 기대값 : 3" )  # 기대값: 3
