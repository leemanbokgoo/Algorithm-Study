import itertools
from typing import List
# 34 ) 순열
# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라.

# [ 풀이 1 ] DFS를 활용한 순열 생성
def permute(nums : List[int]) -> List[List[int]]:
    results = [] # 최종적으로 모든 순열을 저장할 빈 리스트
    prev_elements = [] # 현재까지 선택된 요소들을 임시로 저장하는 리스트, 리스트는 가변적이기 때문에 따로 리스트를 생성해서 값을 백업해두는게 좋다.

    # elements : 아직 선택되지 않은 남은 요소를 담고 있는 리스트
    def dfs(elements):
        if len(elements) == 0: # 모든 요소를 다 선택했다는 의미 , 하나의 순열이 완성되었다는 뜻
            # 완성된 순열인 prev_elements를 results에 추가한다.
            # 이때 슬라이싱 [:]을 사용하여 리스트의 복사본을 저장해야 한다.
            # 그렇지 않으면 나중에 prev_elements가 변경될 때 results 안의 순열도 함께 바뀌어 버린다. 리스트는 가변적이기때문.
            results.append(prev_elements[:])

        # 매개변수로 받아온 elements 배열의 요소드를 하나씩 꺼낸다.
        # 예를 들어 nums가 들어왔다면 elements는 [1,2,3]이고 첫번째 e는 1이다
        for e in elements:
            # elements[:] : [:]하면 해당 리스트를 복사하여 새로운 리스트를 만든다.
            # 예를 들어 e가 1이면 elements[:]는 [1,2,3]
            next_elements = elements[:]
            # 복사된 리스트에서 현재 선택된 요소인 e를 제거한다.
            # 이렇게 제거하고 난 리스트가 다음 재귀 호출에 사용될 새롭게 남은 요소들이 된다.
            # 예를 들어 e가 1이면 elements[:]는 [2,3]
            next_elements.remove(e)

            # 선택한 요소 e를 현재 순열을 구성 중인 prev_elements에 추가한다.
            # 예를 들어 e가 1이면 prev_elements = [1]
            prev_elements.append(e)
            # 새로운 남은 요소 리스트로 dfs를 재귀 호출하여 다음 단계를 탐색한다.
            # 예를 들어 e가 1이면 dfs([2,3])
            dfs(next_elements)
            # 백트래킹 (Backtracking)
            # 재귀 호출이 끝난 후, prev_elements에 추가했던 요소 e를 제거.
            # 다른 경우의 수(순열)를 시도하기 위해 상태를 이전으로 되돌리는(Backtrack) 과정이다.
            # 예를 들어 e가 1이었다면  dfs([2,3]), dfs([3]) 이런 식으로 재귀 호출이 되면서 prev_elements에 넣었던 요소들을 재귀호출이 종료되면서 하나씩 삭제 해간다.
            # [1]->[1,2]-> [1,2,3] 이렇게 prev_elements에 요소를 추가하다가 dfs([])로 인해 재귀 함수가 종료되면 [1,2,3]-> [1,2]-> [1] 이런식으로 pop()해가는 것.
            prev_elements.pop()

    dfs(nums)
    return results

# [ 풀이 2 ] itertools 모듈 사용
# itertools 모듈 : 반복자 생성에 최적화된 효율적인 기능들을 제공한다. C 라이브러리라 속도도 빠른 편. 온라인 테스트 시 별다른 제약사향이 없으면 쓸만함.
# 다만, 주석으로 구현의 효율성, 성능을 위해 사용했다고 설명을 달아두는 것이 좋음.
def permute2(nums:List[int]) -> List[List[int]]:

    # itertools.permutations(nums) : 주어진 iterable(nums 리스트)의 모든 순열(Permutations)을 생성하는 이터레이터(iterator)를 반환한다.
    # map(list, ...) :  map() 함수는 permutations가 반환한 이터레이터의 각 요소(순열 튜플)에 첫 번째 인수로 전달된 함수(list)를 적용한다.
    # 튜플 형태의 순열을 리스트로 변환된다.
    # list() : 마지막으로, list() 생성자는 map 함수가 반환한 이터레이터를 순회하며 생성된 모든 리스트를 모아 최종적인 하나의 큰 리스트로 만든다.
    return list(map(list, itertools.permutations(nums)))


if __name__ == "__main__":
    # 1. 입력 및 예상 출력 정의
    input_nums = [1, 2, 3]
    expected_output = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1]
    ]

    # 2. DFS 방식 검증
    dfs_results = permute(input_nums)

    # 리스트 비교를 위해 정렬 (순열의 순서는 구현에 따라 다를 수 있으므로)
    dfs_results.sort()
    expected_output.sort()

    is_dfs_correct = (dfs_results == expected_output)
    print(f"DFS 방식 결과 검증: {is_dfs_correct}")

    # 3. itertools 방식 검증
    itertools_results = permute2(input_nums)
    itertools_results.sort()  # 비교를 위해 정렬

    is_itertools_correct = (itertools_results == expected_output)
    print(f"itertools 방식 결과 검증: {is_itertools_correct}")
