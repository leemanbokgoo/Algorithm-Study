from typing import List
# n 개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
# 주어진 리스트의 숫자들을 두 개씩 짝지어서(페어), 각 짝의 두 숫자 중 더 작은 값을 선택한 뒤, 이 작은 값들을 모두 더했을 때 합이 가장 크게 만드는 문제.
# 만약 [1,2,3,4] 라면 (1,2), (3,4) 조합, (1,3),(2,4) 조합 , (1,4)(2,3) 조합이 가능하다.
# 이 문제를 해결하는 가장 간단한 방법은 리스트를 오름차순으로 정렬한 다음, 두 개씩 묶어 각 페어의 첫 번째 숫자만 더하는 것.
# 왜냐하면 페어의 첫 번째 숫자가 항상 작은 값이 된다. 이렇게 하면 항상 가장 작은 값을 고르게 되어 손실을 최소화하고, 결과적으로 합을 최대로 만들 수 있다.

# [ 풀이 1 ] 오름차순 풀이
def arrayPariSum(nums : List[int]) -> int :
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        # pair 배열에 숫자가 2개가 되면 한 페어가 완성된 것.
        if len(pair) == 2:
            # 완성된 pair에서 더 작은 값을 찾아 sum 변수에 더함.
            # num가 정렬되어있으므로 pair에 들어가는 숫자는 항상 nums[i] 와 nums[i+1]이 되고 min(pair)는 항상 nums[i]가 된다.
            sum += min(pair)
            # 페어를 처리한 후 , 다음 페어를 만들기위해 pair 리스트를 비움.
            pair = []
    return sum

# [ 풀이 2 ] 짝수 번째 값 계산
# 정렬 된 상태에서는 짝수번쨰에 항상 작은 값이 위치한다.
def arrayPariSum2(nums : List[int]) -> int :
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝 수 번째 값의 합 계산
        if i % 2 == 0:
            sum += n
    return sum

# [ 풀이 3 ] 파이썬 다운 방식
# 슬라이싱을 활용하면 한줄로도 풀이가 가능
def arrayPariSum3(nums : List[int]) -> int :
    #[::2]는 2칸씩 건너뛰므로 짝수번째를 계산하는 것과 동일하다.
    return sum(sorted(nums)[::2])

if __name__ == "__main__":

    nums = [ 1,4,3,2]
    # 출력 4
    # n은 2가 되며 최대합은 4이다.
    # min(1,2) + min(3,4) = 4
    print(f"arrayPariSum : {arrayPariSum(nums)}")
    print(f"arrayPariSum2 : {arrayPariSum2(nums)}")
    print(f"arrayPariSum3 : {arrayPariSum3(nums)}")

