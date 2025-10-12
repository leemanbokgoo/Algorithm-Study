import collections
from typing import List
# 38) 일정 재구성
# [from, to] 로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순으로 방문한다.

# [ 풀이 1 ] DFS로 일정 그래프 구성
# 여행 일정을 그래프로 구성하면 DFS로 문제를 풀이할 수 있다. 한ㄴ가지 주의할 점은 중복된 일정인 경우 어휘 순으로 방문한다.

def findItinerary(tickets : List[List[int]]) -> List[str]:
    # Python의 collections 모듈에 포함된 클래스로 이는 표준 딕셔너리(dict)를 확장한 형태로,
    # 존재하지 않는 키(key)에 접근하려고 할 때 자동으로 기본값(default value)을 생성해주는 특별한 딕셔너리
    # collections.defaultdict(list)를 사용하여 인접 리스트 형태의 그래프를 만든다.
    # graph[a].append(b)시에  graph에 a라는 키값이 존재하지않으면 에러를 발생시키는게 아니라 a라는 키를 만들어 b 값을 추가해준다.
    # key는 출발 항공, value는 도착 항공
    graph = collections.defaultdict(list)

    # 어휘 순으로 방문해야 하기떄문에 tickets를 정렬한다.
    # 안에 들어있는 값이 [출발 항공, 도착 항공] 임으로 출발 항공이 1차 기준이고 2차기준은 도착항공이다.
    for a,b in sorted(tickets):
        # 정렬한 값을 꺼내 graph에 넣어준다.
        # 입력값을 정렬하여 graph를 셋팅, 인접 리스트(Adjacency List) 방식으로 그래프를 구축하는 부분이다.
        # ex) {'JFK': ['ATL', 'SFO']}
        #
        graph[a].append(b)

    route = [] # 최종 경로의 공항들을 역순으로 저장할 리스트

    def dfs(a):
        while graph[a]: # 현재 공항 a에서 출발하는 남아있는 항공편이 있는 동안 계속 된다.
            # 재귀 호출
            # pop(0)은 리스트에서 첫번쨰 요소를 꺼낸다. 요소를 꺼내며 동시에 이 요소를 리스트에서 제거한다.
            # graph[a].pop(0) : a에서 출발하는 항공편 중 어휘순으로 가장 빠른 다음 도착 공항을 가져온다.
            # pop으로 처리했음으로 graph에서 해당 노드는 사라지게 되어 재방문하지않음.
            # 어휘순으로 방문해야하기때문에 어휘순으로 그래프를 생성했음. 때문에 pop(0)으로 첫번쨰 값을 읽어야한다.

            # graph[a].pop(0)의 값은 a의 다음 공항이다. 그 다음 공항에서부터 다시 경로를 탐색한다.
            dfs(graph[a].pop(0))

        # while 루프가 종료되면 더 이상 현재 공항 a에서 출발하는 미사용 항공편이 없다는 뜻임으로
        # 이 시점에서 현재 공항 a를 route에 추가한다.
        # 이렇게 되면 재귀가 끝까지 갔다가 거기서부터 차례대로 route.append(a)하며 재귀 호출이 종료되기때문에 가장 마지막에 방문한 공항부터 경로에 추가되며 역순으로 경로가 쌓인다.
        route.append(a)

    dfs('JFK')

    # 다시 뒤집어서 어휘순으로 맨 처음 읽어들였던 값이 처음이 되게 한다.
    return route[::-1]

# [ 풀이 2 ] 스택 연산으로 큐 연산 최적화 시도.
# 마지막 값을 꺼내는 pop()은 O(1)이지만 첫번째 값을 꺼내는 pop(0)은 O(n)이다. 따라서 효율적인 구현을 위해서 pop()으로 꺼내도 문제가 없도록 개선이 필요하다.
def findItinerary2(tickets : List[List[int]]) -> List[str]:
    graph = collections.defaultdict(list)

    # reverse=True : 역순으로 정렬하는 역할이다.
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    route = []

    def dfs(a):
        while graph[a]:
            # graph[a].pop() : 리스트의 맨 끝 요소를 꺼내고 제거한다.
            dfs(graph[a].pop())
        route.append(a)

    dfs('JFK')

    # pop()으로 꺼냄에도 재귀 호출의 특성상 가장 깊게 탐색한 이후부터 다시 돌아와  route.append(a)를 시도함으로 결과 값은 여전히 역순 경로이기떄문에 뒤집어 줘야한다.
    return route[::-1]

# [ 풀이 3 ] 일정 그래프 반복
# 재귀가 아닌 동일한 구조를 반복으로 풀이해본다. 대부분의 재귀 문제는 반복으로 치환할 수 있으며 스택으로 풀이가 가능하다.
def findItinerary3(tickets : List[List[int]]) -> List[str]:
    graph = collections.defaultdict(list)

    for a, b in sorted(tickets):
        graph[a].append(b)

    # stack은 DFS에 사용되는 스택으로 시작공항인 JFK를 넣어 탐색을 시작한다.
    route, stack = [], ['JFK']

    # stack에 공항이 남아있는 동안 = 방문할 공항이 남아있는 동안 반복한다.
    while stack :
        # stack[-1]: 스택의 가장 위에 있는, 즉 가장 마지막에 들어온 현재 탐색 중인 공항이다.
        # graph[stack[-1]]: 현재 공항에서 출발하는 미사용 항공편 리스트가 존재하는 동안 while문이 돌아간다.
        while graph[stack[-1]]:
            # graph[stack[-1]].pop(0) : 현재 공항에서 출발하는 미사용 항공편 리스트의 가장 첫번째 값을 pop. pop하는 이유는 해당 항공편을 사용했기떄문에 해당 경로를 없애기 위함이다.
            # 그렇게 꺼낸 항공편(=어휘순으로 가장 빠른 도착지)를 stack에 추가한다. 이는 깊이 탐색을 계속 진행하라는 의미다.
            # 이러면 graph에 있는 도착 항공지들은 점점 pop되어 사라지고 stack에는 pop된 도착 항공들이 쌓이기 시작한다.
            # stack에 현재 탐색중인 경로를 임시로 저장하며 깊이 탐색의 경로를 나타내고 graph에는 아직 사용되지않은 잔여 항공편의 목록이 남아있다.
            stack.append(graph[stack[-1]].pop(0))

        # 안쪽 while 루프가 종료되면, 현재 stack[-1] 공항에서 출발하는 미사용 항공편이 더 이상 없다는 뜻으로 깊이 탐색 경로가 끝에 도달했다는 뜻이다.
        # 스택에서 현재 공항을 꺼내서 route에 추가한다.
        # 이런 식으로  while stack : 동안 stack.pop()을 하면 stack에 값이 존재하는 동안 계속 while문이 돌아가면서 stack에 존재하는 모든 값을 route에 append한다.
        route.append(stack.pop())

    # route는 경로가 역순으로 기록되어있음으로 [::-1] 해줘서 다시 뒤집어야한다.
    return route[::-1]


if __name__ == "__main__":

    # 예제 1: 단순 경로
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    expected1 = ["JFK", "MUC", "LHR", "SFO", "SJC"]

    # 예제 2: 순환 경로 및 사전순 우선순위 필요
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    # 사전순: JFK->ATL, JFK->SFO. 먼저 ATL로 가야 함 (JFK-ATL-JFK-SFO-ATL-SFO)
    expected2 = ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    print("--- findItinerary (DFS 재귀) ---")

    result1 = findItinerary(tickets1)
    print(f"입력 1: {tickets1}")
    print(f"출력: {result1}")
    print(f"예상: {expected1}")
    print(f"결과 일치: {result1 == expected1}\n")

    result2 = findItinerary(tickets2)
    print(f"입력 2: {tickets2}")
    print(f"출력: {result2}")
    print(f"예상: {expected2}")
    print(f"결과 일치: {result2 == expected2}\n")

    print("--- findItinerary2 (DFS 반복문/Stack) ---")

    result2_1 = findItinerary2(tickets1)
    print(f"입력 1: {tickets1}")
    print(f"출력: {result2_1}")
    print(f"예상: {expected1}")
    print(f"결과 일치: {result2_1 == expected1}\n")

    result2_2 = findItinerary2(tickets2)
    print(f"입력 2: {tickets2}")
    print(f"출력: {result2_2}")
    print(f"예상: {expected2}")
    print(f"결과 일치: {result2_2 == expected2}\n")

    print("--- findItinerary3 (DFS 반복문/Stack) ---")

    result3_1 = findItinerary3(tickets1)
    print(f"입력 1: {tickets1}")
    print(f"출력: {result3_1}")
    print(f"예상: {expected1}")
    print(f"결과 일치: {result3_1 == expected1}\n")

    result3_2 = findItinerary3(tickets2)
    print(f"입력 2: {tickets2}")
    print(f"출력: {result3_2}")
    print(f"예상: {expected2}")
    print(f"결과 일치: {result3_2 == expected2}\n")
