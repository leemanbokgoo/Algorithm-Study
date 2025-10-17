### DFS 구현의 아주 기본적인 틀 : 재귀 방식
```
def test(input : List[List[int]]):
    # 그래프 생성
    graph = collections.defaultdict(list)

    # 그래프 값을 배열로 다시 생성.
    # 노드 : [연결된 노드 배열] 이런 식의 데이터 형태가 됨.
    for x, y in  prerequisites:
    graph[x].append(y)

    visited = set() 

    def dfs(start_node):
        # 현재 노드를 방문 처리
        visited.add(start_node)
        print(start_node, end=' ') # 방문 순서 출력 (예시)

        # 현재 노드와 연결된 모든 인접 노드에 대해
        for neighbor in graph[start_node]:
            # 아직 방문하지 않았다면 재귀적으로 방문
            if neighbor not in visited:
                dfs(neighbor)

    # 첫번째 노드 부터 탐색한다고 가정.
    start_node = 0
    dfs(start_node)

```

### DFS 구현의 아주 기본적인 틀 : stack 

```
def iterative_dfs(graph, start_node):

    # 1. 방문 여부를 저장할 집합(set) 초기화
    visited = set()
    # 2. 탐색할 노드를 저장할 스택(Stack) 초기화 (리스트로 구현)
    stack = [start_node]
    
    while stack:
        # 스택의 가장 위에 있는 노드(가장 최근에 추가된 노드)를 꺼냄 (pop)
        node = stack.pop()
        
        # 방문하지 않은 노드라면
        if node not in visited:
            # 3. 방문 처리
            visited.add(node)
            print(f"방문 노드: {node}") # 노드를 방문할 때 수행할 작업
            
            # 4. 인접 노드를 스택에 추가
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
```

### DFS 백트래킹의 기본적인 재귀 함수 템플릿
- 이 템플릿은 다음과 과정을 통해 해답을 찾는다. 
    - 선택 (Append): 현재 가능한 선택지 중 하나를 선택하고 경로에 추가한다.
    - 탐색 (DFS): 다음 선택을 위해 더 깊은 단계로 탐색을 진행한다.
    - 취소 (Pop/Backtrack): 깊은 탐색이 끝난 후, 방금 했던 선택을 취소하고 상태를 이전으로 되돌려 (백트래킹), 다음 선택지를 시도한다.

- 주로 다음과 같은 문제에서 사용함.
- 조합, 순열, 부분 집합 문제 (Combination, Permutation, Subset)
    - 조합 (Combination): n개 중 k개를 순서에 상관없이 뽑는 모든 경우를 찾을 때 (예: "숫자 1부터 5까지 중 3개를 고르는 모든 조합을 구하라")
    - 순열 (Permutation): n개 중 k개를 순서를 고려하여 나열하는 모든 경우를 찾을 때
    - 부분 집합 (Subset): 주어진 집합의 모든 부분 집합을 찾을 때 (각 요소를 '선택'하거나 '선택하지 않거나'의 문제로 치환)
- 제약 충족 문제 
    - N-Queen 문제
    - 스토쿠
- 경로 찾기 및 최적화
    - 미로 찾기: 시작 지점에서 도착 지점까지의 모든 경로 또는 가장 짧은 경로를 찾을 때.
    - 여행자 문제 (TSP의 일부 변형): 모든 지점을 한 번씩 방문하는 경로를 찾을 때.
    - 동전 거스름돈 문제 (조합 버전): 특정 금액을 만들 수 있는 모든 동전 조합을 찾을 때.

```
from typing import List

def backtrack_template(n, target_value):
    # n: 탐색 대상의 최대 범위 (예: 1부터 n까지의 숫자)
    # target_value: 목표 조건 (예: 조합의 길이 k, 목표 합계 등)
    
    results = []  # 최종 결과를 저장할 리스트

    def dfs(current_path: List, start_index: int, remaining_target):
        # 재귀적으로 탐색하는 내부 함수 (DFS)
        # current_path: 현재까지 선택된 요소들의 경로 (조합, 순열 등)
        # start_index: 다음 요소를 선택하기 시작할 인덱스 (조합 문제에서 중복 방지용)
        # remaining_target: 종료 조건 확인에 사용되는 값 (예: 남은 요소 수, 남은 합계)

        # 1. 종료 조건 (Base Case)
        # 현재 경로가 문제의 목표 조건을 만족할 때 (리프 노드 도달)
        if remaining_target == 0:
            # Note: 리스트는 가변적이므로, 현재 경로의 '복사본'을 저장해야 합니다.
            # 백트래킹 후 pop()으로 요소가 제거되어 원본이 바뀌는 것을 방지하기 위함.
            results.append(list(current_path))
            return # 재귀 호출 종료

        # 2. 재귀 탐색 (Recursive Step)
        # 현재 위치(start_index)부터 가능한 모든 선택지를 순회
        # 조합 문제의 경우: i를 start_index부터 시작하여 중복을 방지합니다.
        for i in range(start_index, n + 1): # n+1은 n까지 포함하기 위함
            
            # 유효성 검사 (선택 가능 여부 확인)
            # 가지치기(Pruning): 현재 선택이 목표 달성에 불가능하다면 건너뛴다.

            # 현재 선택을 경로에 포함
            # 경로에 포함한다는 말은 결과 값이 [2,3,4]일때 2->3->4 경로가 된다. 
            # 그러므로 i를 계속 더하며 [2,3,4] 경로를 만들어 나가는 것.
            current_path.append(i)

            # 깊이 탐색 (DFS) - 다음 단계로 재귀 호출
            # 조합 문제의 경우: 다음 시작점은 i + 1, 남은 목표는 remaining_target - 1
            dfs(current_path, i + 1, remaining_target - 1)

            # 백트래킹 (Backtrack) - 상태를 이전으로 되돌림
            # 재귀 호출이 끝난 후, 방금 추가했던 요소를 제거하여 다른 선택지를 탐색
            current_path.pop()

    # 초기 호출 (보통 빈 경로, 시작 인덱스, 목표값으로 시작)
    dfs([], 1, target_value)
    
    return results

```
- 위의 예시 코드의 경우 순열 문제를 기반으로 만들어져 있어서 dfs()함수의 인자가 current_path: List, start_index: int, remaining_target이지만 어떤 문제를 푸냐에 따라 매개 변수는 달라질 수 있다. 
    - dfs([], start_node, current_path) : 경로를 기록할때는 current_path , current_sum을 넘기기도 함. 현재까지 선택된 요소들을 담은 리스트나 문자열, 경로를 따라 누적된 합계나 점수. 
    - dfs([], start_node, max_val) : 혹은 visited, max_val 등 제약 조건을 넘기기도 한다. 이는 가지치기할때 사용된다.


```
def permute(nums : List[int]) -> List[List[int]]:
    results = [] 
    prev_elements = [] 

    def dfs(elements):
        if len(elements) == 0: 
            results.append(prev_elements[:])

        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
    dfs(nums)
    return results
```

- 위의 코드처럼 그냥 nums만 넘길 수도 있다. 어떻게 풀이하냐에 따라 인자는 매번 달라진다.
    - 해당 풀이는 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라는 문제임.

### 백트래킹 문제 예시 코드 
- N개의 숫자 중 M개를 고르는 순열 문제
- 주어진 N개의 서로 다른 원소 중에서 M개의 원소를 뽑아 순서대로 나열하는 모든 경우의 수(순열)를 찾는 것.
  - 만약 N개의 숫자 [1,2,3] 중 M = 2개를 고른다면 [1,2], [1,3] 이런 식으로 순열을 선택하여 6가지 경우를 만들 수 있다. 

```

N, M = 3, 2 # 예: [1, 2, 3] 중 2개를 고르는 순열
nums = [1, 2, 3]
result = []

def backtrack_permutation(path):
    # 1. 종료 조건: M개의 숫자를 모두 골랐을 때
    if len(path) == M:
        result.append(list(path))
        return

    # 2. 가능한 '선택' 목록 순회 (모든 nums의 원소)
    for i in range(len(nums)):
        choice = nums[i]
        
        # 3. 가지치기: 이미 path에 포함된 숫자는 중복 선택 불가 (순열)
        if choice in path:
            continue
            
        # 4. 선택 및 5. 탐색
        path.append(choice) 
        backtrack_permutation(path)
        
        # 6. 선택 취소
        path.pop()

# backtrack_permutation([])
# print(result) # [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
```