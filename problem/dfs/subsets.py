from typing import List
# 37) 부분 집합
# 모든 부분 집합을 리턴하라.


# [ 풀이 1 ] 트리의 모든 DFS 결과
# 트리를 구성하고 트리를 DFS하는 문제로 풀이할 수 있다.
def subsets(nums:List[int]) -> List[List[int]]:
    result = [] # 결과 저장


    def dfs(index, path):

        # 재귀 함수를 돌떄마다 결과 저장
        result.append(path)

        # index와 nums의 길이만큼 반복문 추가
        # index가 끝까지 가면 반복문이 동작하지않아 재귀 함수가 다시 호출되지않아. 재귀가 끝남.
        # ex) len(nums)가 2이라면 index가 2일때, 반복문이 돌아가지않는다.
        for i in range(index, len(nums)):
            # 재귀 함수 시작,  이렇게 넘어가면 다음 depth의 탐색이 시작된다.
            # i + 1 : 다음 depth에서 nums[i]의 값을 탐색하지않아서 중복이 없도록 다음 숫자부터 넘김.
            # path + [nums[i]] : path와 현재 노드의 값을 더해서 새로운 배열을 만듬. 처음에 path는 []으로 초기화 되어있지만 재귀 함수가 반복될수록 그 전 재귀 함수의 값을 가지고 있음.
            # ex) [] -> [1] -> [1,2] -> [1,2,3] 이런식
            dfs( i + 1, path + [nums[i]] )

    dfs(0, [])
    return result

if __name__ == "__main__":
    # 입력값 : [1,2,3]
    # 출력 [ [3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], [] ]

    nums = [1,2,3]
    result = subsets(nums)
    result.reverse()

    print(f" 출력      : {result}")
    print("기대 출력값 : [[3], [1], [2], [1,2,3], [1,3], [2,3], [1,2], []]")

