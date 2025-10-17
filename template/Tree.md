
# DFS 사용하여 Tree 관련 문제 풀이 

### 트리를 DFS로 탐색하는 코드 : Stack
- 트리 전체를 빠짐없이 탐색하는 가장 기본적인 DFS 순회 로직

```
from collections import deque
from typing import Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root: Optional[TreeNode]):
    # 예외 처리
    if not root:
        return 

    # 1. 스택 초기화 (DFS는 LIFO를 사용합니다.)
    # collections.deque를 사용하여 list.pop()보다 효율적으로 구현할 수 있습니다.
    stack = deque([root])
    
    while stack:
        # 2. 노드 꺼내기 (pop) - 가장 최근에 넣은 노드를 꺼낸다.
        node = stack.pop() 
        
        # 3. 현재 노드에서 수행할 작업
        # 여기서 노드의 값을 처리하거나, 조건을 검사하는 등 필요한 로직을 수행합니다.
        print(f"노드 {node.val} 처리") 
        
        # 4. 자식 노드를 스택에 추가 (다음 탐색 후보)
        # DFS이므로 다음 깊이로 내려갈 노드들을 먼저 넣는다..
        # 순서: 일반적으로 Left -> Right 순으로 처리하고 싶다면, 스택에는 Right -> Left 순으로 넣는다.
        # 오른쪽 자식이 있다면 스택에 추가
        if node.right:
            stack.append(node.right)
            
        # 왼쪽 자식이 있다면 스택에 추가 (가장 마지막에 넣어 다음 pop()에서 먼저 처리)
        if node.left:
            stack.append(node.left)

# --- 사용 예시 ---
# # 트리 구성: (1 -> 2, 3)
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# print("--- 반복문 DFS 탐색 순서 ---")
# iterative_dfs_tree_template(root)
# # 예상 순서: 1 -> 2 -> 3 (전위 순회와 유사)
```


### DFS를 이용한 트리의 지름(Diameter) 및 최대 깊이 동시 탐색
- 최대 깊이 (Max Depth) : 현재 노드를 루트로 하는 서브 트리에서 리프 노드까지의 가장 긴 단방향 경로의 간선 수. 이 값은 재귀 함수의 반환 값으로 사용된다.
    - return max(left_val, right_val) + 1
- 트리의 지름 (Diameter) : 트리 전체에서 두 노드 간의 가장 긴 경로의 간선 수. 이 값은 외부 변수(self.max_result)에 누적하여 갱신된다.

```
from typing import Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class SolutionTemplate:
    def __init__(self):
        # 1. 외부 상태 저장 변수: 탐색 중 발견한 '최댓값' (지름, 최대 경로 합 등)을 저장
        self.max_result = 0 

    def solve_tree_problem(self, root: TreeNode) -> Any:
        
        # 트리 DFS를 시작하고 최종 결과를 반환하는 메인 메서드
        def dfs(node: TreeNode) -> int:
            
            # 1. 종료 조건 (Base Case)
            if not node:
                # 문제에 따라 기본값(0, -1, None 등)을 반환하여 계산의 기준점을 설정
                # 예: 지름 문제에서는 깊이 계산을 위해 -1 반환
                return -1 

            # 2. 재귀 호출: 왼쪽 및 오른쪽 서브트리의 단방향 값 획득
            left_val = dfs(node.left)
            right_val = dfs(node.right)

            # 3. 외부 상태 갱신 (양방향 정보 계산 및 저장)
            # 현재 노드를 '중심'으로 왼쪽 정보와 오른쪽 정보를 결합하여 최댓값을 계산/갱신
            # 예: 지름 = left_val + right_val + 2
            current_combined_value = left_val + right_val + 2 
            
            # self를 통해 외부 상태 갱신 (가장 큰 값 유지)
            self.max_result = max(self.max_result, current_combined_value)

            # 4. 단방향 값 반환
            # 현재 노드를 포함하여, 위로 전달할 단방향의 최대 값 (깊이, 최대 경로 합 등)
            # 예: 깊이 = max(left_val, right_val) + 1
            return max(left_val, right_val) + 1

        # DFS 탐색 시작
        dfs(root)

        # 최종적으로 외부 상태 변수에 저장된 결과를 반환
        return self.max_result
```


## BFS 이용한 풀이 

### 트리를 BFS로 탐색하는 코드 : Queue
- 트리 전체를 빠짐없이 탐색하는 가장 기본적인 DFS 순회 로직

```
from collections import deque
from typing import Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def iterative_bfs_tree_template(root: Optional[TreeNode]):
    
    # 예외 처리
    if not root:
        return 

    # 1. 큐 초기화
    queue = deque([root])

    while queue:
        # 2. 노드 꺼내기 (popleft) - 큐의 가장 앞에 있는 노드를 꺼낸다.
        node = queue.popleft() 
        
        # None 체크는 큐에 None이 들어갔을 경우를 대비함.
        if node:
            
            # 3. 현재 노드에서 수행할 작업 
            # 여기서 노드를 방문했을 때 해야 할 모든 로직을 수행한다.
            print(f"노드 {node.val} 방문 및 처리") 
            
            # 4. 자식 노드를 큐에 추가 (다음 레벨 탐색 후보)
            # 순서: 왼쪽 자식을 먼저 넣고 오른쪽 자식을 넣으면, 다음 레벨에서 왼쪽->오른쪽 순서로 처리된다.
            # 왼쪽 자식이 있다면 큐에 추가
            if node.left:
                queue.append(node.left)
                
            # 오른쪽 자식이 있다면 큐에 추가
            if node.right:
                queue.append(node.right)

# --- 사용 예시 ---
# 트리 구성: (1 -> 2, 3), 2는 (4, 5)를 가짐
# root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# print("--- 반복문 BFS 탐색 순서 ---")
# iterative_bfs_tree_template(root) 
# # 예상 순서: 1 -> 2 -> 3 -> 4 -> 5
```

### 범용적인 BFS 레벨 탐색 템플릿
- 트리나 그래프에서 레벨별로 작업을 수행하거나 최단 거리를 계산할 때 사용

```
from collections import deque
from typing import Optional, List, Any

class TreeNode:
    """트리 노드 구조를 위한 기본 정의"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# BFS를 사용하여 이진 트리를 레벨(층) 단위로 탐색하는 범용 템플릿.
# (예시로 레벨별 노드 값을 리스트로 반환하도록 구성)
def bfs_level_traversal_template(root: Optional[TreeNode]) -> List[List[Any]]:

    if not root:
        return []

    queue = deque([root])
    results = [] # 결과를 레벨별로 저장할 리스트

    while queue:
        # 1. 현재 레벨의 모든 노드를 처리하기 위해 큐의 현재 크기를 저장
        level_size = len(queue)
        current_level_nodes = [] # 현재 레벨의 노드들을 저장할 임시 리스트
        
        # 2. 현재 레벨의 노드 개수만큼 반복
        for _ in range(level_size):
            
            # 3. 노드 Dequeue (현재 레벨의 노드를 꺼냄)
            node = queue.popleft()
            
            # 4. 현재 노드에서 수행할 작업 (PLACEHOLDER)
            # 예: 노드의 값을 저장하거나, 깊이(depth) 변수를 증가시키거나, 특정 조건 검사
            current_level_nodes.append(node.val)
            
            # 5. 자식 노드 Enqueue (다음 레벨의 탐색 후보)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # 6. 레벨 처리 완료: 현재 레벨의 결과를 최종 리스트에 추가
        results.append(current_level_nodes)

    return results

# # --- 사용 예시 ---
# # 트리 구성: (1 -> 2, 3)
# root = TreeNode(1, TreeNode(2), TreeNode(3))
# print("--- BFS 레벨 순회 결과 ---")
# # 결과: [[1], [2, 3]]
# print(bfs_level_traversal_template(root))
```

## BST 트리 순회 

### 전위 순회 : 재귀 함수 
```
result_list = [] 

class RecursiveTraversal:

    def preorder_template(self, node: Optional[TreeNode]):
        # 전위 순회 (Pre-order): 현재 -> 왼쪽 -> 오른쪽
        if not node:
            return

        # 1. 현재 노드 처리 (ROOT) 
        # 예: result_list.append(node.val)
        print(f"[전위] 노드 {node.val} 처리")

        # 2. 왼쪽 자식 재귀 호출
        self.preorder_template(node.left)

        # 3. 오른쪽 자식 재귀 호출
        self.preorder_template(node.right)
```

### 전위 순회 : DFS를 이용한 반복구조 
```
from collections import deque
from typing import Optional

def iterative_preorder_template(root: Optional[TreeNode]):
    # 반복문 전위 순회: stack을 사용하며, 오른쪽 -> 왼쪽 순으로 stack에 넣음
    if not root:
        return

    stack = deque([root])
    
    while stack:
        node = stack.pop()
        
        # 1. 현재 노드 처리 (ROOT)
        # 예: print(node.val)
        print(f"[반복-전위] 노드 {node.val} 처리")

        # 2. 오른쪽 자식을 먼저 stack에 넣는다. (LIFO 원칙에 의해 나중에 처리)
        if node.right:
            stack.append(node.right)
            
        # 3. 왼쪽 자식을 나중에 stack에 넣는다. (LIFO 원칙에 의해 가장 먼저 처리)
        if node.left:
            stack.append(node.left)
```


### 중위 순회 : 재귀 함수를 이용한 BST 중위 순회 템플릿(오름 차순)
```
from typing import Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTInorderTemplate:
    def __init__(self):
        # 1. 이전 노드 상태를 저장할 변수 (문제에 따라 초기값 설정)
        # 예: 최소 차이 문제에서는 -무한대, 정렬된 리스트 생성에서는 None 등
        self.prev_state = None 
        
        # 2. 최종 결과 또는 누적된 결과를 저장할 변수
        # 예: 최소 차이 문제에서는 sys.maxsize, 결과 리스트에서는 [] 등
        self.result_container = [] 

    def inorder_traversal_dfs(self, node: Optional[TreeNode]) -> Any:
        # 현재 방문 중인 TreeNode

        if not node:
            return

        # 1. 왼쪽 자식 탐색 (가장 작은 노드부터)
        # 재귀 호출이 먼저 발생하여 가장 깊은 왼쪽 노드까지 탐색
        self.inorder_traversal_dfs(node.left)

        # 2. 현재 노드 처리 (PLACEHOLDER)
        # 노드를 오름차순 순서로 방문했을 때 수행할 핵심 로직
        # 이 코드에서는 임의 적으로 이전 노드와의 관계를 활용하여 상태 갱신하는 코드를 작성했음.
        if self.prev_state is not None:
            # 예: 이전 값과의 차이를 계산하여 최솟값 갱신
            self.result_container = min(self.result_container, node.val - self.prev_state)
            # 예: 정렬된 리스트에 값 추가
            self.result_container.append(node.val)

        # 현재 노드를 '이전 노드'로 업데이트
        self.prev_state = node.val
        
        # 3. 오른쪽 자식 탐색 (다음으로 큰 노드로 이동)
        self.inorder_traversal_dfs(node.right)
        
        # DFS 함수 자체는 명시적인 반환값이 필요 없을 수 있다.
        # 최종 결과는 self.result_container에서 얻는다.
        return self.result_container # (필요에 따라 반환)
```


### 중위 순회 : 반복문 기반 DFS를 사용하여 BST를 중위 순회(오름차순 방문)

```
from typing import Optional, Any

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_iterative_inorder_template(root: Optional[TreeNode]) -> Any:

    if not root:
        # 문제에 따라 None, 0, 또는 적절한 초기값을 반환
        return None 

    # 1. 상태 초기화 (문제에 따라 필요한 변수들을 정의.)
    # 예: 최소 차이 계산을 위한 초기값
    prev_state = None  # 직전 노드 값을 저장 (처음에는 None 또는 -sys.maxsize)
    result_container = [] # 최종 결과(혹은 누적된 값)를 저장
    
    stack = [] # 아직 방문하지 않은 부모 노드들을 저장하는 스택
    node = root
    
    while stack or node:
        
        # 2. 왼쪽 탐색 (Go Left): 가장 깊은 왼쪽 노드까지 부모들을 스택에 저장
        while node:
            stack.append(node)
            node = node.left

        # 3. 현재 노드 처리 (Process Node)
        # 스택에서 노드를 꺼냄 (이때 꺼내지는 노드가 현재 서브트리에서 가장 작은 값)
        node = stack.pop()

        # 핵심 처리 로직 (PLACEHOLDER)
        # 노드를 오름차순으로 방문했을 때 수행할 모든 작업을 여기에 삽입합니다.
        
        # 이 코드에서는 예시 코드로  최소 차이 계산 문제에 적용하는 로직을 적었음.
        if prev_state is not None:
            # result_container를 최솟값으로 갱신하는 로직
            result_container = min(result_container, node.val - prev_state)
            
            # (예시로 노드 값만 출력)
            print(f"현재 노드: {node.val}, 직전 노드: {prev_state}")
            
        # 직전 노드 상태 업데이트 (다음 반복을 위해)
        prev_state = node.val
        
        # 4. 오른쪽 탐색 (Go Right)
        # 오른쪽 서브트리로 이동. 다음 루프에서 해당 서브트리의 가장 왼쪽 노드부터 다시 탐색 시작
        node = node.right

    # 최종 결과 반환 (문제에 따라 result_container의 최종 값 또는 누적된 리스트 반환)
    # return result_container 
    return None # 템플릿이므로 None 반환
```

### 후위 순회 : 재귀 함수

```
from typing import Optional, List, Any

# 결과를 담을 외부 리스트를 가정
result_list = [] 
def postorder_template(self, node: Optional[TreeNode]):
    # 후위 순회 (Post-order): 왼쪽 -> 오른쪽 -> 현재
    if not node:
        return

    # 1. 왼쪽 자식 재귀 호출
    self.postorder_template(node.left)

    # 2. 오른쪽 자식 재귀 호출
    self.postorder_template(node.right)

    # 3. 현재 노드 처리 (ROOT)
    # 예: result_list.append(node.val)
    print(f"[후위] 노드 {node.val} 처리")
```

### 후위 순회 : DFS 반복구조 
```
from collections import deque
from typing import Optional, List

def iterative_postorder_template(root: Optional[TreeNode]) -> List[Any]:
    # 반복문 후위 순회: 임시 스택(혹은 리스트)을 사용하여 전위 순회의 역순으로 결과를 저장한 후, 최종적으로 결과를 뒤집어 반환.
    if not root:
        return []

    stack = deque([root])
    # 결과를 임시로 저장할 스택/리스트
    temp_result = [] 
    
    while stack:
        node = stack.pop()
        
        # 1. 임시 결과에 현재 노드 저장
        # '현재 -> 오른쪽 -> 왼쪽' 순
        temp_result.append(node.val)

        # 2. 왼쪽 자식을 먼저 stack에 넣는다. (LIFO 원칙에 의해 나중에 처리)
        if node.left:
            stack.append(node.left)
            
        # 3. 오른쪽 자식을 나중에 stack에 넣는다. (LIFO 원칙에 의해 먼저 처리)
        if node.right:
            stack.append(node.right)

    # 4. 임시 결과를 뒤집어 후위 순회 순서로 만든다.
    # (현재 -> 오른쪽 -> 왼쪽)의 역순은 (왼쪽 -> 오른쪽 -> 현재)이다.
    # 
    return temp_result[::-1]
```

### 이진 검색 결과로 트리 구성
```
def sortedArrayToBST( nums: List[int] ) -> TreeNode:
    if not nums:
        return None

    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node
```

## Utils
### 배열 입력받아서 트리 생성
```
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
```

### 트리 배열로 출력
```
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
```