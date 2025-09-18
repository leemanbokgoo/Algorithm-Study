from typing import List
# 덧셈하여 타겟을 만들 수 있는 배열의 두숫자 인덱스를 리턴한다.

# [ 풀이 1 ] 브루토 포스로 계산
# 브루토 포스 방식 : 배열을 2번 반복하면서 모든 조합을 더해서 일일히 확인해보는 무차별 대입 방식
def twoSum(nums:List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i +1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]
    return None

# [ 풀이 2 ] int을 이용한 탐색
# 모든 조합을 비교하지않고 정답, 즉 타겟에서 첫번쨰 값을 뺀 값 target -n이 존재하는 지 탐색하는 문제로 변경한다.
# in의 시간복잡도는 O(n)이고 따라서 전체 시간 복잡도는 이전과 동일한 O(n의 제곱)이지만 같은 시간 복잡도라도 in 연산 쪽이 훨씬 가볍고 빠르다.
def twoSum2(nums: List[int], target: int) -> List[int]:

    # enumerate() : 반복(iteration)할 때, 요소의 인덱스(순번)와 값을 함께 꺼내주는 내장 함수, i = index , n = vluae
    for i, n in enumerate(nums):
        # 현재 n( value에 해당하는 값)을 target에서 빼고 나면 어떤 값이 필요한지 확인 ex) 9-2=7 일떄 complement는 7
        complement = target - n

        #  nums의 현재 인덱스 i 다음 위치부터 끝까지의 슬라이스한 배열(nums[i+1:])에 위에서 계산한 complement가 포함되어 있는지 확인.
        #  이렇게 i+1부터 탐색하는 이유는 한 요소를 두 번 사용하는 것을 방지하기 위함.
        if complement in nums[i + 1:]:
            # complement가 리스트에 있다면, 조건을 만족하는 두 수를 찾았으므로 두 수의 인덱스를 담은 리스트를 반환하고 함수를 종료
            # nums.index(n): 현재 요소 n의 인덱스
            # nums[i + 1:].index(complement): nums[i+1:] 슬라이스한 배열내에서 complement의 인덱스 값.
            # (i+1)을 더하는 이유는 위에서 찾은 슬라이스한 배열 내 인덱스는 원래 nums 리스트에서의 인덱스가 아니므로 원래 위치인 i+1을 더 해줘야함.
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
    return None

# [ 풀이 3 ] 첫번째 수를 뺀 결과 키조회
# target = 첫번째 값 + 두번째 값 이기때문에 targe - 첫번쨰 값 = 두번째 값이다.
# 두번쨰 수를 키로 하고 기존의 인덱스는 값으로 바꿔서 딕셔너리로 저장해두면 두번쨰 수를 키로 조회해서 정답을 즉시 찾아낼 수 있다.
# 타겟에서 첫번째수를 뺸 결과를 key로 조회해보면 두번째 인덱스를 즉시 조회할 수 있다.
# 이경우 최악의 경우는 O(n)이겠지만 보통의 경우 O(1)의 시간 복잡도를 가진다.
def twoSum3(nums: List[int], target: int) -> list[int] | None:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫번째 수를 뺸 결과를 키로 조회
    for i, num in enumerate(nums):
        # target - num in nums_map : traget - num = 나머지 값이 nums_map에 존재하는지.
        # i != nums_map[target -num] : 동일한 인덱스 [0,0]이런 결과를 출력하지않도록 두번째 값의 인덱스가 i와 같지않아야한다.
        # target- num은 두번째 값이고, 두번째 값이 7이라고 할때 nums_map[7] = 1 이 된다.
        # 이때 두번째 값의 인덱스와 i의 인덱스가 같으면 둘은 같은 값이기때문에 index값이 출력되서는 안된다.
        # ex) [1,2,3,4]인 배열에서 3+3이 되어 [2,2]가 출력되는 사태를 막기 위함.
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target-num]]

# [ 풀이 4 ] 조회 구조 개선
# 전체를 모두 저장할 필요없이 정답을 찾게 되면 함수를 바로 빠져나올 수 있다.
# 그러나 두번째 값을 찾기위해 어차피 매번 비교해야하기 때문에 [ 풀이 3 ]에 비해서 성능상 큰 이점은 없다.
def twoSum4(nums: List[int], target: int) -> List[int]:
    nums_map ={}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target-num] , i]

        # [ 풀이 3 ]처럼 미리 nums_map에 값을 채워놓는게 아니라 한번 for문이 돌고 if문을 통과한 값만 저장한다.
        # 그렇기 때문에 nums_map에는 두번째 값이 없다. 고로 첫번째 값은 if문을 지나치고 그대로 nums_map에 저장이 되게 된다.
        # 그 다음 for문이 계속 돌면서 두번째 값이 돌아갈 차례가 됬을 때, if target - num in nums_map:이 동작하게 되면서 [nums_map[target-num] , i]을 리턴한다.
        nums_map[num] = i

# @@@ 이 방법은 배열의 index를 출력하는 문제에선 쓸 수 없고(배열을 정렬해야하기때문) 값을 출력하는 경우에는 가능 @@@
# [ 풀이 5 ] 투 포인터 이용
def twoSum_not_index(nums: List[int], target: int) -> List[int]:
    # left는 가장 앞의 인덱스[0] 이고 right는 가장 끝 인덱스 값
    left, right = 0 , len(nums) - 1

    # 오른쪽으로 가면 값이 더 커지도록 배열을 정렬
    nums.sort()
    # 두 포인터가 만날때까지 반복.
    while not left == right:
        # 합이 target보다 작으면 왼쪽 포인터를 늘리기
        # -> 배열이 정렬되있어서 오른쪽으로 갈수록 숫자가 커진다. 합이 작으면 큰 수가 필요함으로 왼쪽 포인터를 오른쪽으로 옮김.
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 target보다 크면 오른쪽 포인터를 줄이기
        # -> 배열이 정렬되있어서 오른쪽으로 갈수록 숫자가 커지기 때문, 합이 크니까 더 작은 수가 필요함으로 오른쪽 포인터를 앞쪽으로 옮기는 것.
        elif nums[left] + nums[right] > target:
            right -=1
        else:
            return [left, right]
    return None


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    # nums[0] + nums[1] = 2 +7 =9 임으로 0,1을 출력해야함.
    print(f"twoSum : {twoSum(nums, target)}")
    print(f"twoSum2 : {twoSum2(nums, target)}")
    print(f"twoSum3 : {twoSum3(nums, target)}")
    print(f"twoSum4 : {twoSum4(nums, target)}")
