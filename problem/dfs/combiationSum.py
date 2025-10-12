from typing import List
# 36) 조합의 합
# 숫자 집합 candidates를 조합하여 합이 target이 되는 원소를 나열하라. 각 원소는 중복으로 나열 가능하다.
# 조합을 응용한 문제. 합 target을 만들 수 있는 모든 번호 조합을 찾는 문제이다. 순열 문제와 유사하게 DFS와 백트래킹으로 풀이할 수 있다.
# 모든 중복 조합에서 찾아야하기때문에 이 그림과 같이 항상 부모의 값부터 시작하는 그래프로 구성할 수 있다.
# 조합이 아니라 순열을 찾는 문제라면 자식노드는 항상 처음부터 시작해야해서 훨씬 더 많은 계산이 필요하다.
# 부모 값부터 시작해야하는 이유는 DFS 탐색 시, for 루프의 시작점을 현재 선택한 값의 인덱스(index)로 설정하면, 다음 숫자를 현재 숫자와 같거나 인덱스가 큰 숫자 중에서만 고르도록 강제된다.
# 그러면 조합을 항상 오름차순의 인덱스 순서로만 만들게 된다. 그렇게 되면 [2, 3]은 생성되지만, 3을 선택한 후 2 (인덱스 0)를 선택하는 것은 불가능해져서 [3, 2]의 생성을 원천적으로 막아 중복을 피한다.
# 중복 선택이 가능해야 하므로 index 대신 i를 다음 DFS 호출에 전달하여 현재 선택한 숫자를 다시 선택할 기회를 유지한다. (예: [2,2,3])
# 그러나 조합은 각각의 노드가 자기 자신부터 하위 원소까지의 나열로만 정리할 수 있다.

# 입력 : candidates = [2,3,6,7], target = 7
# 출력 : [ [7], [2,2,3] ]
# 입력2 : candidates = [2,3,5], target = 8
# 출력 : [ [2,2,2,2], [2,3,3,], [3,5] ]

# [ 풀이 1 ] DFS로 중복 조합 그래프 탐색
# 현재 문제에는 테스트 케이스에 0이 포함되어있지않아 문제가 발생하지않지만 0이 입력값에 존재하면 무한 루프가 발생한다.
# 목표값(target)은 줄어들지 않는데, 0을 무한정 선택하여 [2, 0, 0, 0, 0, ...]와 같은 무한히 긴 조합이 생성되며 프로그램이 멈춘다.
# 그러므로 0이 있으면 해당 값을 제외해야한다. 어차피 문제에서는 target의 값이 나오도록 숫자를 더해야하는데 0은 아무리 더해봤자 값이 올라가지않음으로 계산에서 처음부터 제외해도 문제가 없다.
# 고로 dfs탐색전에 입력값에 0이 존재하는지 확인하고 해당 값을 지워야할 필요가 있음.
def combinationSum(candidates : List[int], target : int) -> List[List[int]]:
    result = [] # 결과 저장 배열

    def dfs(csum, index, path):

        # 종료 조건

        # 가지치기
        # csum이 0보다 작으면, 해당 조합은 target의 값이 될 수 없다고 판단. 이미 target의 값보다 더 빠져서 음수가 됬음으로 해당 조합은 탐색 중단.
        if csum < 0:
            # 재귀 함수 종료
            return

        # 성공조건
        # csum이 0과 같으면
        if csum == 0 :
            # 결과에 해당 path를 저장한다.
            result.append(path)
            return

        # 현재 인덱스와 candidates의 길이만큼 반복문을 반복.
        for i in range(index, len(candidates)):
            # csum - candidates[i] : csum에서 현재 인덱스에 해당하는 값을 뺀다.
            # 처음 초기화 csum값은 target값이기떄문에 csum에서 점점  candidates[i]값을 뺴간다.
            # 그렇게 재귀를 돌면서 계속 값을 빼는데 딱 0이 되면 위의 if문을 통해 result에 값을 저장하는데, 딱 0이 되는 해당 조합은 다 더했을때 target값이 된다.
            # i : 현재 인덱스를 넘긴다 -> 이를 통해 다음 깊이로 넘어가며 현재 부모의 값부터 다시 재귀 함수를 돌리는 것.
            #  path + [candidates[i]] : path + [...] 연산은 새로운 리스트를 생성하여 전달한다. path 배열에 현재 candidates[i]의 값을 넘긴다.
            # 위에서 새로운 리스트를 생성하여 전달하기때문에 백트래킹 과정이 없다. 다만 이런식으로 하면 메모리 효율이 떨어진다 . 계속 객체를 만들어내야하니까
            dfs(csum - candidates[i], i , path + [candidates[i]])

    # 인덱스니까 0부터 시작
    # path에다가 중간 정답을 저장하는 것.
    # path 변수는 현재 DFS(깊이 우선 탐색)를 통해 구성하고 있는 부분적인 조합(combination)을 의미한다. 현재재 탐색 중인 상태 또는 단계라는 의미로 경로(path)라고 이름 짓는 것.
    dfs(target, 0 , [])
    return result



if __name__ == "__main__":

    # 테스트 케이스 1
    candidates1 = [2, 3, 6, 7]
    target1 = 7
    expected1 = [[7], [2, 2, 3]]
    result1 = combinationSum(candidates1, target1)

    print(f"입력 : candidates = {candidates1}, target = {target1}")
    # 조합의 순서는 중요하지 않으므로 정렬 후 비교를 위해 sort를 적용 (실제 테스트는 set을 사용하거나 정렬 후 비교해야 정확함)
    # 여기서는 간단하게 출력만 확인합니다.
    print(f"출력 : {result1}")
    print(f"예상 : {expected1}\n")

    # 테스트 케이스 2
    candidates2 = [2, 3, 5]
    target2 = 8
    expected2 = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    result2 = combinationSum(candidates2, target2)

    print(f"입력 : candidates = {candidates2}, target = {target2}")
    print(f"출력 : {result2}")
    print(f"예상 : {expected2}")