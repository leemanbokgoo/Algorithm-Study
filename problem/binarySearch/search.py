import bisect
from typing import List
# 65 ) 이진 검색
# 정렬된 nums를 입력받아 이진 검색으로 target에 해당되는 인덱스를 찾아라.

# [ 풀이 1 ] 재귀 풀이
def search(nums : List[int], target : int) -> int:

    def binary_search(left, right):

        # left가 right보다 작거나 같을떄까지 탐색
        if left <= right:

            ## 중앙 값 구하기
            mid = (left + right) // 2

            # 만약 nums[mid]가 target보다 크다면 왼쪽 포인터가 mid + 1 위치로 한칸 움직인다.
            if nums[mid] < target:
                return binary_search(mid + 1, right)

            # nums[mid]가 target보다 크다면 right 포인터를 mid - 1 위치로 움직인다.
            elif nums[mid] > target:
                return binary_search( left , mid - 1)

            # 둘다 아니라면 nums[mid] = target임으로 mid를 리턴한다.
            else :
                return mid

        # left의 포인터가 right보다 크면 말은 두 포인터가 만났다는 뜻임으로 탐색을 전부 완료했다는 것이다.
        else :
            return -1

    return binary_search(0, len(nums) - 1 )

# [ 풀이 2 ] 반복 풀이
# 대부분의 재귀 풀이는 반복 풀이로 변경 할 수 있다. 대게는 재귀 풀이가 더 우아하지만 반복 풀이는 좀 더 직관적이라 이해가 쉽다.
def search2(nums : List[int], target : int) -> int:
    left, right = 0 , len(nums) - 1

    while left <= right:
        ## 중앙 값 구하기
        mid = ( left + right ) // 2

        if nums[mid] < target:
            # left 포인터를 mid + 1로 옮긴다.
            left = mid + 1

        elif nums[mid] > target:
            # right를 mid - 1로 옮긴다.
            right = mid - 1

        else :
            return mid

    return -1

# [ 풀이 3 ] 이진 검색 모듈
# 파이썬에서는 이진 검색을 직접 구현할 필요가 없다. 이진 검색 알고리즘을 지원하는 bisect 모듈을 기본으로 제공한다.
# 실제로 코딩 테스트 시에는 가급적 재귀나 반복으로 이진 검색을 풀이하는 편이 나중에 코드 리뷰를 받을 때 저 돞은 평가를 받을 수 있다.
def search3(nums : List[int], target : int) -> int:

    # bisect.bisect_left(nums, target) : 정렬된 리스트 nums에서 target을 삽입할 수 있는 가장 왼쪽 인덱스를 찾는다.
    index = bisect.bisect_left(nums, target)

    # index < len(nums) : index가 리스트의 유효한 인덱스 범위 내에 있는지 확인
    # nums[index] == target: 유효한 인덱스라면, 실제로 해당 인덱스의 값이 우리가 찾고자 하는 target과 같은지 확인
    if index < len(nums) and nums[index] == target:
        return index

    else :
        return -1

# [ 풀이 4 ] 이진 검색을 사용하지않는 index vnfdl
def search4(nums : List[int], target : int) -> int:
    try:
        return nums.index(target) # target의 index값을 찾아내는 함수
    except ValueError:
        return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12]
    target = 9

    print(search(nums, target) , "         |    기대 출력값 : 4 ")
    print(search2(nums, target) , "         |    기대 출력값 : 4 ")
    print(search3(nums, target) , "         |    기대 출력값 : 4 ")
    print(search4(nums, target) , "         |    기대 출력값 : 4 ")

