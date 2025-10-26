import collections
from typing import List
# 83 ) 과반수 엘리먼트
# 과반수를 차지하는(절반을 초과하는) 엘리먼트를 출력하라

# [ 풀이 1 ] 브루트 포스로 과반수 비교
# 타임 아웃이 발생하는 풀이
def majorityElement(nums : List[int]) -> int:
    for num in nums:
        # len(nums) // 2 -> 길이를 반으로 나눈 값
        if nums.count(num) > len(nums) // 2:
            return num

# [ 풀이 2 ] 다이나믹 프로그래밍
# 메모이제이션을 이용한 아주 간단한 다이나믹 프로그래밍 풀이
def majorityElement2(nums : List[int]) -> int:
    counts = collections.defaultdict(int)

    # nums.count()로 한번 카운트를 계산한 값은 저장해서 재활용
    # 계산 되지않았던 값이 들어온다면 항상 0 이고, 그때만 카운트를 계산함.
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            return num

# [ 풀이 3 ] 분할 정복
# 병합 정렬과 매우 유시한 방식으로 풀이할 수 있다.
# 쪼갠 다음 정렬해서 각각의 엘리먼트를 전부 리턴하는 병합 정렬과 달리 여기서는 과반수 후보군에 해당하는 엘리먼트만 리턴하면서
# 계속 위로 올려주면(즉, 백트래킹하면) 최종적으로 정답이 남게 된다.
# 재귀 풀이의 특성상 다이나믹 프로그래밍이나 다른 방식에 비해서는 속도가 다소 느린 편이다.
def majorityElement3(nums : List[int]) -> int:

    #  재귀 함수 종료 조건
    # 배열에 값이 없으면 과반수 요소가 없음으로 None 반환
    if not nums:
        return None

    # 배열의 길이가 1이면, 그 요소 자체가 과반수 요소이므로 그 값을 반환
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2 # 배열의 절반 인덱스를 계산

    # 분할 시도
    # 배열 nums를 두 개의 절반(왼쪽: nums[:half], 오른쪽: nums[half:])으로 나눈다.
    # a와 b는 재귀 호출을 통해 왼쪽 절반과 오른쪽 절반에서 각각 찾은 과반수 요소 후보이다.
    a = majorityElement3(nums[:half])
    b = majorityElement3(nums[half:])

    # 백 트래킹 될때 처리하는 부분, 즉 정복에 해당하는 부분
    # 분할 정복의 논리에 따라, 전체 배열의 과반수 요소는 반드시 왼쪽 절반의 과반수 요소(a)이거나 오른쪽 절반의 과반수 요소(b) 둘 중 하나이다.
    # 어떤 요소가 전체 배열의 절반을 초과하여 나타난다면, 이 요소는 왼쪽 절반 또는 오른쪽 절반 중 적어도 한쪽에서는 그 절반의 과반수 요소(또는 가장 많이 나타난 요소)여야 하기 때문

    # nums.count(a): 전체 배열 nums에서 왼쪽에서 찾은 후보 a가 몇 번 나타나는지 카운ㄴ팅
    # nums.count(a) > half: $a$의 개수가 전체 배열 길이의 절반(half)을 초과하는지 확인
    # 조건이 참일 경우 1을 리턴함으로 [b,a]배열의 인덱스 1의 값인 a를 리턴, 반대일 경우 b를 리턴.
    # 다만 이 조건이 경우 재귀함수를 통해 쪼개진 배열이 [1,2]인 상황에서는 실제로는 과반수 요소가 없다. 하지만 코드는 둘중 하나를 강제로 선택하도록 구현되어있음으로 둘 중 하나를 반드시 반환한다.
    # 이 틀린 후보가 상위 단계의 배열에서는 다시 count()함수로 검증되면서 올바른 최정 결과를 찾는데 기여하게 된다. 부분 배열에서 틀린 답을 반환하더라도, 최종단계에서 전체 배열을 대상으로 하는 count()검증을 통해 걸러지게 된다.
    # 이것이 가능한 이유는 부분 배열에서 올라온 '틀린' 후보는 전체 배열의 nums.count()를 통과할 만큼 충분한 개수를 가지고 있지 않기때문이다.
    # 따라서 최종 단계 또는 진짜 과반수 요소가 있는 상위 단계에서 nums.count() 검증을 통과하지 못하고 걸러지게 된다.
    # 분할 정복 알고리즘은 유력한 후보를 추려내는 필터의 역할을 하고, 마지막에 전체 배열을 대상으로 하는 최종 검증(nums.count() > half)을 통해 정답을 확정하는 것이다.
    return [b,a][nums.count(a) > half]

# [ 풀이 4 ] 파이썬다운 방식
# 숫자를 정렬하여 가운데를 지정하면 반드시 과반수 이상인 엘리먼트일 것이다.
def majorityElement4(nums : List[int]) -> int:
    return sorted(nums)[len(nums) // 2 ]

if __name__ == "__main__":
    nums = [3,2,3]
    nums2 = [2,2,1,1,1,2,2]

    print("[ 풀이 1 ] 브루트 포스로 과반수 비교 : ", majorityElement(nums), " | 기대 출력값 3 " )
    print("[ 풀이 1 ] 브루트 포스로 과반수 비교 : ", majorityElement(nums2), " | 기대 출력값 2 " )

    print("============================================================================")
    print("[ 풀이 2 ] 다이나믹 프로그래밍 : ", majorityElement2(nums), " | 기대 출력값 3 " )
    print("[ 풀이 2 ] 다이나믹 프로그래밍 : ", majorityElement2(nums2), " | 기대 출력값 2 " )

    print("============================================================================")
    print("[ 풀이 3 ] 분할 정복 : ", majorityElement3(nums), " | 기대 출력값 3 " )
    print("[ 풀이 3 ] 분할 정복 : ", majorityElement3(nums2), " | 기대 출력값 2 " )

    print("============================================================================")
    print("[ 풀이 4 ] 파이썬다운 방식 : ", majorityElement4(nums), " | 기대 출력값 3 " )
    print("[ 풀이 4 ] 파이썬다운 방식 : ", majorityElement4(nums2), " | 기대 출력값 2 " )
