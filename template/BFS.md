### BFS 탐색 기본 템플릿 : Queue 사용
1. 최단 경로 문제 : 가중치(비용)가 없는 그래프(간선의 길이가 모두 1이거나 동일한 그래프)에서 시작점에서 특정 노드까지의 **가장 빠른 경로(최소 간선 수)**를 찾을 때 가장 효율적이다.
    - 미로 찾기: 미로의 한 지점에서 출구까지 가는 최소 칸 수.
    - 두 지점 간 최단 거리: 그래프에서 노드 A에서 노드 B까지 거쳐야 하는 최소 노드 수. (예: 아는 사람 건너서 아는 사람 찾기)
2. 모든 가능한 상태 탐색 (State Space Search) : 어떤 상태에서 다른 상태로 이동할 수 있는 경우, 모든 가능한 상태 변화를 탐색해야 할 때 사용
    - 퍼즐 게임 (예: 15-퍼즐): 초기 상태에서 목표 상태까지 도달하는 최소 이동 횟수. (각 이동을 큐에 넣어 순차적으로 탐색)
    - 물통 문제: 물통의 물을 옮겨 목표 양을 만드는 최소 조작 횟수.
3. 그래프의 레벨별 탐색 (Level Order Traversal) : 트리나 그래프의 모든 노드를 시작점에서부터의 거리가 가까운 순서대로 탐색해야 할 때 사용된다.
    - 컴퓨터 네트워크 브로드캐스트: 한 서버에서 네트워크 전체로 데이터를 전파할 때, 레벨별로 퍼져나가는 과정을 시뮬레이션.
    - 그룹화 및 연결 요소 찾기: 연결된 노드들을 그룹(연결 요소)으로 묶을 때. (DFS도 가능하지만 BFS가 레벨별로 확인하기에 적합할 수 있음)
4. 이분 그래프 판별 (Bipartite Graph Check) : 그래프의 노드들을 두 그룹으로 나눌 수 있는지 확인하는 문제에서, BFS를 통해 레벨이 홀수인 노드와 짝수인 노드를 나누어 판별할 수 있다.

```
# 그래프 정의: {노드: [인접 노드들]}
example_graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E', 'G'],
    'G': []
}

bfs_template(example_graph, 'A')
# 예상 탐색 순서: A -> B -> C -> D -> E -> F -> G
```

```
from collections import deque
from typing import Dict, List, Any

# 그래프 생성
graph = collections.defaultdict(list)

# 그래프 값을 배열로 다시 생성.
# 노드 : [연결된 노드 배열] 이런 식의 데이터 형태가 됨.
for x, y in  prerequisites:
graph[x].append(y)

def bfs_template(graph: Dict[Any, List[Any]], start_node: Any):
    # 그래프 (딕셔너리로 구현된 인접 리스트 형태)
    # 탐색을 시작할 노드
    
    # 1. 방문 여부를 저장할 집합(set) 초기화
    visited = set()
    
    # 2. 탐색할 노드를 저장할 큐(Queue) 초기화
    queue = deque([start_node])
    
    # 시작 노드를 방문 처리
    visited.add(start_node)
    
    # 큐가 빌 때까지 반복 (탐색할 노드가 남아있는 동안)
    while queue:
        
        # 3. 큐에서 가장 먼저 들어온 노드를 꺼냄 (Dequeue)
        node = queue.popleft()
        
        # 현재 노드를 방문했을 때 수행할 작업
        print(f"방문 노드: {node}")
        
        # 4. 현재 노드와 연결된 모든 인접 노드 순회
        # graph.get(node, [])는 노드가 그래프에 없을 경우 빈 리스트를 반환하여 KeyError 방지
        # 노드가 그래프에 있다면 그냥 graph[node] 하면 된다. 
        for neighbor in graph.get(node, []):
            
            # 5. 방문하지 않은 노드라면
            if neighbor not in visited:
                # 방문 처리
                visited.add(neighbor)
                
                # 큐에 추가 (Enqueue)
                # 이 노드는 현재 노드와 같은 레벨의 노드들을 모두 처리한 후에 탐색된다.
                queue.append(neighbor)

```
