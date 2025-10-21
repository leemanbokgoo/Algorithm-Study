import bisect
from typing import List
# 68 ) 두수의 합
# 정렬된 배열을 받아 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
# 주의 이 문제에서 배열은 0이 아닌 1부터 시작하는 것으로 한다.

# [ 풀이 1 ] 투 포인터
# O(n)에 풀이할 수 있다.
def twoSum( numbers : List[int], target : int )-> List[int]:
    left, right = 0 , len(numbers) - 1

    # 두 포인터가 만나기 전까지 while문
    while not left == right:

        if numbers[left] + numbers[right] < target:
            # 두 포인터가 가리키는 위치의 값을 합한 값이 target보다 작다면 더 큰 값이 필요함으로
            # 왼쪽 포인터를 끝쪽(오른쪽)으로 이동
            left += 1

        elif numbers[left] + numbers[right] > target:
            # 두 포인터가 가리키는 위치의 값을 합한 값이 target보다 크다면 더 작은 값이 필요함으로
            # 오른쪽 포인터를 앞쪽(왼쪽)으로 이동
            right -= 1
        else:
            # 배열이 0이 아닌 1부터 시작한다고 했음으로 각 포인터에 +1을 한다.
            return left + 1, right + 1

# [ 풀이 2 ] 이진 검색
# 이 풀이의 시간 복잡도는 O(n log n)으로 [ 풀이 1 ] 투포인터가 O(n)으로 좀 더 빠르다.
def twoSum2( numbers : List[int], target : int )-> List[int]:
    # k : numbers 인덱스
    # v : numbers 값
    for k, v in enumerate(numbers):
        # left 포인터를 현재 인덱스 k 의 바로 뒤에 위치 시킨다.
        left, right = k + 1, len(numbers) - 1
        # target값에서 현재 값을 뺴면 나머지 필요로 하는 값(expected)이 나온다.
        expected = target - v

        # 두 포인터가 만날때까지
        while left <= right:
            # 중앙값
            mid = left + (right - left) // 2

            # 중앙값이 기대값보다 작으면 더 큰 값이 필요함으로
            if numbers[mid] < expected:
                # left를 mid + 1 의 위치로 이동
                left = mid + 1

            # 중앙값이 기대값보다 크면 더 작은 값이 필요함으로
            elif numbers[mid] > expected:
                # right를 mid - 1 위치로 이동
                right = mid - 1

            else:
                return k + 1, mid + 1

# [ 풀이 3 ] bisect 모듈 + 슬라이싱
# [ 풀이 2 ] 이진 검색 보다 20배 이상 느리다.
def twoSum3( numbers : List[int], target : int )-> List[int]:
    for k, v in enumerate(numbers):
        expected = target - v
        # numbers[ k + 1:] : 인덱스 k의 다음부터 리스트의 끝까지
        i = bisect.bisect_left(numbers[ k + 1:], expected)

        #  numbers[i + k + 1] : i + k + 1이 실제 numbers 배열에서의 i값의 인덱스다.
        if i < len(numbers[ k + 1:]) and numbers[i + k + 1] == expected:
            # + 2 하는 이유는 배열은 0이 아닌 1부터 시작하는 것으로 했음으로 +1을 해야한다.
            # 그래서 i + k + 1 에서 +1 을 해야하기때문에 + 2
            return k + 1 , i + k + 2

# [ 풀이 4 ] bisect 모듈 + 슬라이싱 최소화
def twoSum4(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        expected = target - v
        # [ 풀이 3 ]을 개선하여 슬라이싱을 한번만 하도록 변수에 담아 사용
        nums = numbers[ k + 1:]
        i = bisect.bisect_left(nums, expected)
        if i < len(nums) and numbers[i + k + 1] == expected:
            return k + 1, i + k + 2

# [ 풀이 5 ] bisect 모듈 + 슬라이싱 제거
# 이 풀이는 [ 풀이 1 ]투 포인터와 속도가 같아졌다.
def twoSum5(numbers: List[int], target: int) -> List[int]:
    for k, v in enumerate(numbers):
        expected = target - v
        # k + 1 : 왼쪽 범위를 제한하는 파라미터. 이렇게 하면 슬라이싱을 사용할 필요가 없어진다.
        i = bisect.bisect_left(numbers, expected, k + 1 )
        if i < len(numbers) and numbers[i] == expected:
            return k + 1, i + 1

if __name__ == "__main__":
    numbers = [2,7,11,15]
    target = 9

    print("[ 풀이1 ] 투 포인터 : 기대 출력값 1,2 " , twoSum(numbers, target))
    print("[ 풀이2 ] 이진 검색 : 기대 출력값 1,2", twoSum2(numbers, target))
    print("[ 풀이2 ] bisect 모듈 + 슬라이싱 : 기대 출력값 1,2", twoSum3(numbers, target))
    print("[ 풀이2 ] bisect 모듈 + 슬라이싱 최소화 : 기대 출력값 1,2", twoSum4(numbers, target))
    print("[ 풀이2 ] bisect 모듈 + 슬라이싱 제거 : 기대 출력값 1,2", twoSum5(numbers, target))


