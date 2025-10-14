import collections
import heapq
from typing import List
# 41) K 경유지 내 가장 저렴한 항공권
# 시적점에서 도착점까지의 가장 저렴한 가격을 계산하되, K개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지않을 경우 -1을 리턴한다.
# n = 3, edges = [ [0,1,100], [1,2,100], [0,2,500] ]
# src = 0, dst = 2, K = 0
# 시작점 src 노드 0 에서 도착점 dst 노드 2까지 최저가는 0->1->2 경로인 200이지만, 여기서는 입력값이 k=0임으로 경유지가 하나도 없어야한다.
# 이 조건을 만족하는 최저가는 0-2인 500이다.

# [ 풀이 1 ] 다익스트라 알고리즘 응용
# 가격을 시간으로 가정한다면 최단 시간을 계산하는 경로는 앞서 다익스트라 알고리즘으로 동일하게 구현할 수 있다.
# 다만 여기에는 한가지 제약 사항이 추가되었는데 K개의 경유지 이내에 도착해야한다는 점이다.
# 따라서 다익스트라 알고리즘 구현을 위해 우선순위 큐에 추가할때 K이내 일때만 경로를 추가하여 K를 넘어서는 경로는 더이상 탐색되지않게 한다.
def findCheapestPrice(n:int, flights:List[List[int]], src:int, dst:int, K:int)-> int:
    graph = collections.defaultdict(list)

    # u : 출발 노드
    # v : 도착 노드
    # w : 가격
    for u,v,w in flights:
        graph[u].append((v,w))

    # 우선 순위 큐 변수 : [ (가격, 정점, 남은 경유 가능 횟수) ]
    Q = [(0, src, K)]

    while Q:
        # 가격, 현재 노드, 남은 경유 가능 횟수
        # 해당 우선순위 큐 Q는 가격(price) 순으로 정렬된다.
        price, node, k = heapq.heappop(Q)

        # 현재 노드가 도착 지점이라면
        if node == dst:
            # 도착 지점에 도달했다는 뜻임으로 현재 까지의 가격을 리턴
            # 이 price는 K 횟수 제한을 만족하는 경로 중 가장 저렴한 가격임이 보장된다.
            # 그 이유는 다익스트라 알고리즘을 사용함으로 if node == dst: 에 도달하는 순간 반환하는 price는 해당 경유 횟수 제한 내에서 가장 저렴한 가격이 된다.
            return price

        # 현재 노드까지 k 번 이내에 도달한 경우에만 우선순위 큐에 넣는다.
        if k >= 0:
            # 현재 노드의 근처 노드를 뽑아온다.
            # v : 이웃 노드
            # w : 가격
            for v,w in graph[node]:
                # 출발지에서 이웃 노드 v까지의 총 가격 : 도착지점에서 현재 노드까지의 가격 price + 현재 노드에서 이웃노드 까지가는데 걸리는 가격 w
                alt = price + w
                # alt: 위에서 저장한 도착지점에서 이웃 노드까지 걸리는 가격,
                # v : 이웃 노드
                # k-1 : k번 이내에 도착해야함으로 남은 경유 가능 횟수를 -1 해서 깍아준다
                heapq.heappush(Q, (alt, v, k-1))
    return -1

if __name__ == "__main__":
    # 입력값
    n = 3
    edges = [ [0,1,100], [1,2,100], [0,2,500] ]
    src, dst, K = 0, 2, 0

    # 출력값
    expected_result = 500

    result = findCheapestPrice(n, edges, src, dst, K)
    print(str(result))
    print('True' if result == expected_result else 'False')
