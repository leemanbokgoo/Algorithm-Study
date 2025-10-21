from typing import List
# 66 ) 회전 정렬된 배열 검색
# 특정 피벗을 기준으로 회전하여 정렬된 배열에서 target 값의 인덱스를 출력하라

# [ 풀이 1 ] 피벗을 기준으로 한 이진 검색
# 입력값을 보면 가장 작은 값을 찾는 다면 해당 위치의 인덱스가 피벗이 될 수 있다.
def search( nums : List[int] , target : int) -> int :

    if not nums:
        return -1

    # pivot 찾기. 여기서 pivot은 최솟값의 index다.
    left, right = 0 , len(nums) -1

    while left < right:
        # 자료형을 초과하지 않는 중앙 위치 계산
        mid = left + (right - left) // 2

        # mid가 오른쪽 끝보다 크다는 것은, mid가 높은 값들이 밀집해 있는 영역에 있다는 뜻
        # ex: [4, 5, 6, 7, 0, 1, 2]에서 mid=3(값 7), right=6(값 2)
        if nums[mid] > nums[right]:
            # 최솟값은 mid 오른쪽에 있다.
            left = mid + 1

        # mid가 오른쪽 끝보다 작거나 같다는 것은, mid가 이미 작은 값 영역에 있거나
        # 아직 회전 전의 순수 정렬 영역에 있다는 뜻.
        # ex: [4, 5, 6, 7, 0, 1, 2]에서 mid=5(값 1), right=6(값 2)
        else :
            # 최솟값은 mid이거나 mid 왼쪽에 있다.
            # 최솟값을 포함하는 쪽에 대해서는 경계를 좁힐때 mid를 포함해야함으로 -1이나 +1을 하지않는다.
            right = mid

    # pivot : 회전 지점
    pivot = left

    # # 2단계: Pivot을 사용한 이진 탐색
    left, right = 0 , len(nums) -1

    while left <= right :

        # mid : 논리적인 정렬 상태에서의 인덱스
        mid = left + (right - left) // 2
        # mid_pivot = 논리적인 인덱스(mid)에  회전 지점 pivot을 더하고, 리스트의 길이 len(nums)로 나머지 연산을 하면 실제 회전된 배열의 인덱스로 변한된다.
        # 논리적 인덱스에 잘린 지점(pivot)을 더해, 논리적인 배열의 시작(0)이 실제 배열의 시작(4)으로 밀려난 효과를 만든다.
        # ex )  [4, 5, 6, 7, 0, 1, 2]은 len=7, pivot=4이다. 논리적 중간 mid =3 은 논리적 배열에서 값 4를 가리킨다.
        #       mid_pivot = ( 3 + 4 ) & 7 = 0 로 4의 인덱스가 마치 0 (배열의 첫번째 요소)인 것처럼 계산 할 수 있다. 
        mid_pivot = (mid + pivot) % len(nums)

        if nums[mid_pivot] < target:
            left = mid + 1

        elif nums[mid_pivot] > target:
            right = mid - 1

        else :
            return mid_pivot

    return -1


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 1

    print(search(nums, target) , "         |    기대 출력값 : 4 ")

