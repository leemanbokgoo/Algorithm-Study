import itertools
from typing import List
# 35 ) 조합
# 전체 수 n을 입력받아 k개의 조합을 리턴하라.

# [ 풀이 1 ] DFS로 k개 조합 생성
# 조합의 경우 자기 자신 뿐만 아니라 앞의 모든 요소를 배제하고 next_elements를 구성한다.
def combine(n : int, k : int ) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        # elements : 현재 조합을 구성 중인 리스트
        # start : 숫자를 선택하기 시작할 지점, 1부터 시작함.
        # k : 남은 조합의 길이, 즉 몇개의 숫자를 더 골라야하는 지를 나타낸다.

        # 종료 조건
        if k == 0: # 현재 조합()에서 더이상 채워야 할 숫자가 없다. 즉, k개의 숫자를 전부 골라 조합을 완성했다는 뜻.
            results.append(elements) # 완성한 조합을 결과에 추가
            return # 재귀 호출 종료

        # 재귀 탐색 시작.
        for i in range(start, n + 1): # 숫자 i를 start부터 n까지 순차적으로 반복문 돌림.
            elements.append(i) # 현재 조합에 해당 숫자를 추가
            # 다음 숫자는 i+1부터 시작해야 하고, 남은 숫자는 이제 k−1
            # i+1 부터 시작한다는 건 depth를 한 단계 더 들어간다는 뜻. (깊이 탐색)
            # k-1하는 이유는 현재 위에서 elements(조합)에 elements.append(i)하면서 하나의 숫자를 넣었기때문에 -1 하는 것.
            dfs(elements, i + 1, k - 1)
            # 백트래킹 단계
            # 재귀 호출이 끝나고 여기로 돌아오면 방금 추가했던 i를 pop하는 것.
            elements.pop()

    # 함수 호출
    # [], 1, k : 첫 함수 호출 시 초기화 값. 1로 시작하는 이유는 숫자가 1로 시작하니까. 인덱스가 아니기때문.
    dfs([], 1 , k )
    # 결과 반환
    return results

# [ 풀이 2 ] itertools 모듈 사용
# itertools는 C언어로 구현되어 있어, 일반적인 파이썬 재귀 함수보다 훨씬 빠르고 메모리 효율적이다.
# 직접 재귀를 구현할 때 발생할 수 있는 스택 오버플로우(Stack Overflow)와 같은 오류의 위험이 없다.
def combine2(n: int , k : int) -> List[List[int]]:
    # itertools.combinations(iterable, r) : itertools 모듈에서 제공하는 함수로, 주어진 iterable (여기서는 1부터 n까지의 숫자)에서 r (여기서는 k)개의 요소를 선택하는 모든 조합(Combination)을 생성.
    # 각 조합은 튜플(tuple) 형태로 반환 된다.
    # [list(t) for t in ...] : 리스트 컴프리헨션으로, itertools.combinations가 생성한 반복자(t)를 순회하면서 작업을 수행.
    # 각 조합(t)은 튜플 형태이므로, 이를 list(t)를 사용하여 일반적인 리스트([1, 2]) 형태로 변환
    # 변환된 리스트들을 모아 최종 List[List[int]] 형태의 결과를 만든다.
    return [list(t) for t in itertools.combinations(range(1, n + 1), k)]


if __name__ == "__main__":
    # 입력값
    n = 4
    k = 2
    # 입력 : n = 4, k = 2
    # 출력 [ [2,4], [3,4], [2,3], [1,2], [1.3], [1,4], ]

    # combine 함수 (DFS)
    result_dfs = combine(n, k)
    print(f"# 입력: n = {n}, k = {k}")
    print(f"# combine(DFS) 출력")
    print(f"출력: {result_dfs}")
    print("\n")

    # combine2 함수 (itertools + 리스트 변환) 호출
    result_itertools_list = combine2(n, k)
    print(f"# 입력: n = {n}, k = {k}")
    print(f"# 출력 (combine2 함수)")
    print(f"출력: {result_itertools_list}")