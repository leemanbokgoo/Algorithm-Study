import collections
from typing import List
# 39) 코스 스케줄
# 0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다. 코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.
# 문제에서 [a,b] 쌍은 "코스 a를 들으려면, 코스 b를 먼저 들어야 한다"는 의미이다.
# 즉, 입력값으로 만든 그래프가 순환 구조인지 판별해야한다.

# [ 풀이 1 ] DFS로 순환 구조 판별
def canFinish( numCourses: int, prerequisites: List[List[int]]) -> bool:

    # 입력값을 넣어줄 그래프 list를 생성
    graph = collections.defaultdict(list)

    # 페어들의 목록인 입력값을 받아서 그래프로 표현한다.
    # 그러면 x : [y1, y2]의 구조가 되는데 여기서 x는 코스를 의미하고 y는 x가 의존하는 코스들의 리스트다. 즉, x를 듣기위해 먼저 수강해야하는 코스가 y다.
    for x, y in  prerequisites:
        graph[x].append(y)

    # 이미 방문했던 노드를 저장하는 변수
    # 이미 방문했던 노드를 중복 방문하면 순환 구조로 간주 할 수 있고 이 경우 False를 리턴하여 종료.
    # traced는 중복값을 갖지않음으로 set으로 생성.
    traced = set()

    def dfs(i):

        # i에서 깊이 탐색을 진행하면서 현재 탐색 경로에 i가 다시 나타나는지 확인하여 순환을 탐지.
        # i가 이미 방문한 노드라면 순환구조임으로 종료
        if i in traced:
            return False

        # 현재 노드를 방문한 노드 배열에 추가
        traced.add(i)

        # graph[i]의 값은 위에서 만들어준 y값이다. y값은 graph[i]를 수강하기 위해 먼저 수강해야하는 코스다.
        # 즉,깊이 탐색을 한단계 더 들어가기 위해 graph[i]에 연결된 노드 y를 찾아서 하나씩 깊이 탐색을 들어가는 것.
        for y in graph[i]:
            # 재귀 시작
            # dfs 재귀 호출의 반환값이 false라면 위의 if i in traced: 에서 false를 반환했다는 뜻이다.
            # 재귀가 계속 호출되면서 마지막 값이 False라면 가장 처음 호출된 재귀 호출에게 False값이 반환된다.
            # y 를 매개 변수로 넘겨서 depth를 한단계 더 들어간다.
            if not dfs(y):
                return False
        # i에서 시작된 모든 선수 과목 경로 탐색(재귀 호출)에서 순환이 발견되지않았다면,
        # 즉,해당 노드(i)를 모든 이용한 탐색이 끝나면 방문했던 내역을 반드시 삭제 해야함.
        # 그렇지않으면 형제 노드가 방문한 노드까지 남게 되어 순환이 아닌데 순환이라고 잘못 판단할 수 있음.
        traced.remove(i)

        # 만약 재귀호출이 전부 끝나도 false가 반횐되지않았다면 순환구조가 없다는 뜻이다.
        return True

    # list(graph) : 모든 key를 추출한다. 여기서 key로 쓰이는 값들은 최소한 한 번이라도 선수 과목으로 지정된 (즉, 의존 관계가 있는) 모든 코스들이다.
    for x in list(graph):
        # 각 코스를 호출하여 순환이 있는지 확인, dsf(x)의 반환값이 false라면 순환이 존재함으로 false 반환.
        if not dfs(x):
            return False

    return True

# [ 풀이 2 ] 가지치기를 이용한 최적화
# 앞어 풀이는 순환이 발견될떄까지 모든 자식 노드를 탐색하는 구조로 되어있다.
# 그렇기에 만약 순환이 아니더라도 복잡하게 서로를 호출하는 구조로 그래프가 구성되어있다면 불필요하게 동일한 그래프를 여러번 탐색하게 될 수 있다.
# 따라서 한 번 방문했던 그래프는 두번 이상 방문하지않도록 무조건 True로 리턴하는 구조로 개선한다면 속도를 줄일 수 있다.
# 예를들어 A경로는 A→B→C→D 이런 식으로 깊이 탐색하였고 순환구조가 발견되지않았다. 여기서 D경로를 탐색한다면 D->C->B->A가 된다.
# 즉 A-> D로 가는 경로를 역순으로 돌리면 D->A로 가는 경로가 되는 것이다. 고로 A->D에서 순환 구조 발견되지않으면 D->A도 발견되지않는다.
# 그리고 DFS는 원래 이런식으로 가지 치기 하도록 구현하는게 올바른 구현방법이다. 풀이 1은 너무 곧이곧대로 구현한 풀이라고 볼 수 있음.
def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = collections.defaultdict(list)

    for x, y in prerequisites:
        graph[x].append(y)

    traced = set() # 이미 방문한 노드를 저장하기 위한 변수로 탐색 중에 방문한 노드를 저장한다.
    # 한번 방문했던 노드들을 저장하기 위한 변수로 모든 탐색이 끝난 후에 다른 root 노드로 깊이 탐색을 진행할때 노드를 추가한다.
    # 탐색 도중 순환 구조가 발견된다면 false를 리턴하면서 visited는 추가 하지 않고 모든 함수를 빠져나가며 종료하게 된다.
    # 즉, 한 번 방문한 노드는 (현재의 깊이 탐색이 아니라 이전 깊이 탐색에서 방문했던 노드라도) 더이상 탐색하지않는다.
    # 순환 없이 성공적으로 깊이 탐색한 끝난 노드를 저장하는 것이다.
    visited = set()

    def dfs(i):

        # 해당 노드 i가 이미 방문한 노드라면
        if i in traced:
            return False

        # 이미 해당 노드 i가 방문한 노드라면
        if i in visited:
            return True

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        # 모든 깊이 탐색이 끝난 후에 방문했던 노드 i를 visited에 저장한다.
        visited.add(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True

# 입력 : 2, [[1,0]]
# 출력 : true
# 2개의 코스가 있으며 1을 완료하기위해 0을 끝내면 된다. 따라서 가능.
# 입력 : 2 [ [1,0],[0,1] ]
# 출력 : false
# 2개의 코스가 있으며, 1을 완료하기 위해서는 0을 끝내야하고 0을 완료하기 위해서는 1을 끝내야한다. 따라서 불가능하다.
if __name__ == "__main__":
    result1_1 = canFinish( 2, [[1,0]])
    result1_2 = canFinish( 2, [ [1,0],[0,1] ])

    print("============ canFinish ============")
    print("결과 : " + str(result1_1))
    print("결과2 : " + str(result1_2))

    result2_1 = canFinish2( 2, [[1,0]])
    result2_2 = canFinish2( 2, [ [1,0],[0,1] ])

    print("============ canFinish2 ============")
    print("결과 : " + str(result2_1))
    print("결과2 : " + str(result2_2))
