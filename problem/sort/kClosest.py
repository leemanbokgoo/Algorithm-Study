import heapq
from typing import List
# 64 ) 원점에 K번째로 가까운 점
# 평면상에 points 목록이 있을때, 원점(0,0)에서 K번 가까운 점 목록을 순서대로 출력하라. 평면상 두 점의 거리는 유클리드 거리로 한다.

# [ 풀이 1 ] 유클리드 거리의 우선 순위 큐 순서
# 유클리드 거리 : 유클리드 공간에서 두 점 사이의 거리를 계산하는 가장 일반적인 방법 중 하나.
# 유클리드 거리를 계산하고 이 값을 우선순위 큐로 K번 출력하면 쉽게 문제를 풀이할 수 있다.
def kClosest(points : List[List[int]], K : int) -> List[List[int]] :

    # math 모듈을 사용해 유클리드 거리 수식을 구현해 계산해고 heap에 삽입하는 코드
    heap = []

    for (x,y) in points:
        dist = x ** 2 + y ** 2
        heapq.heappush(heap, (dist, x, y))

    # 결과를 저장할 result
    result = []

    for _ in range(K):
        (dist, x, y) = heapq.heappop(heap)
        result.append((x,y))

    return result

if __name__ == "__main__":
    points = [[1, 3], [-2, 2]]
    K = 1
    # (1, 3)과 가까운 거리는 루트 10이고 (-2, 2)와의 거리는 루트 8이다. 두 번째가 더 가까우며, K=1로 가장 가까운 거리 K개는 [[-2,2]]이다.
    print(kClosest(points, K), f"       : 기대 출력값 [ [-2, 2] ]")

    point2 = [[3, 3], [5, -1], [-2, 4]]
    # 가장 가까운 거리 k=2개는 [ [3,3], [-2,4] ]이다.
    K2 = 2

    print(kClosest(point2, K2), f"       : 기대 출력값 [ [3,3], [-2,4] ]")





