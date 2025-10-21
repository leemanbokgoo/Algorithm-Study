import bisect
from typing import List, Set
# 67 ) 두 배열의 교집합
# 두 배열의 교집합을 구하라

# [ 풀이 1 ] 브루트 포스로 계산.
def intersection( nums1 : List[int], nums2 : List[int]) ->  List[int]:
    result : Set = set()

    for n1 in nums1:
        for n2 in nums2:
            if n1 == n2:
                result.add(n1)

    return result

# [ 풀이 2 ] 이진 검색으로 일치 여부 판별
def intersection2( nums1 : List[int], nums2 : List[int]) ->  List[int]:
    result : Set = set()
    nums2.sort()

    for n1 in nums1:

        # bisect_left(nums2, n1) : n1이 배열에 없다면 n1보다 크거나 작은 첫번째 요소의 인덱스를 반환한다.
        #                          만약 n1이 존재한다면 이미 존재하는 중복값들 중 가장 먼저 나오는 중복값의 인덱스를 반환한다.
        i2 = bisect.bisect_left(nums2, n1)

        # n1이 nums2에 실제로 존재하는 지를 검증한다.
        #  len(nums2) > 0 : nums2 배열의 값이 실제로 존재하는지 확인.
        # len(nums2) > i2 : 위에서 이진 검색 모듈(bisect)이 반환한 i2가 nums2에 유효한 인덱스인지 확인
        # n1 == nums2[i2] : n1이 nums2[i2]와 같다면
        if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
            result.add(n1)

    return result

def intersection3( nums1 : List[int], nums2 : List[int]) ->  List[int]:
    result : Set = set()
    nums1.sort()
    nums2.sort()

    # 각 배열의 포인터 초기화
    i = j = 0

    # i 와 j가 nums1, nums2의 길이만큼 반복하도록.
    # 둘중 하나라도 먼저 해당 배열의 길이만큼 반복했다면 while문 종료
    while i < len(nums1) and j < len(nums2):

        # nums1[i] > nums2[j] :  nums1[i]가  nums2[j] 보다 크다면 j(nums2의 포인터)를 다음칸(끝쪽으로) 이동
        if nums1[i] > nums2[j]:
            j += 1

        # nums1[i] < nums2[j] :  nums2[j]가 nums1[i]보다 크다면 i(nums1의 포인터)를 다음칸(끝쪽으로) 이동
        elif nums1[i] < nums2[j]:
            i += 1

        # 둘의 값이 같다면 저장하고 두 포인터를 다음 칸으로 이동 시킨다.
        else:
            result.add(nums1[i])
            i += 1
            j += 1

    return result


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]

    nums1_1 = [4,9,5]
    nums2_2 = [9,4,9,8,4]
    print("[ 풀이1 ] 부르트 포스 : 기대 출력값 2 " , intersection(nums1,nums2))
    print("[ 풀이1 ] 부르트 포스 : 기대 출력값 9,4", intersection(nums1_1,nums2_2))

    print("[ 풀이2 ]이진검색 : 기대 출력값 2 " , intersection2(nums1,nums2))
    print("[ 풀이2 ]이진검색 : 기대 출력값 2 " , intersection2(nums1_1,nums2_2))

    print("[ 풀이3 ]투 포인터 : 기대 출력값 2 " , intersection2(nums1,nums2))
    print("[ 풀이3 ]투 포인터 : 기대 출력값 2 " , intersection2(nums1_1,nums2_2))


