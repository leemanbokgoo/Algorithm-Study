from typing import List

# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 요소를 출력하라.

# [ 풀이 1 ] 브루트 포스로 계산
# 3중 반복문을 사용하고 있어 시간 복잡도가 O(n의 3제곱)이라 너무 오래 걸림.
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    # 3중 반복문을 돌리면서 i + j + k = 0을 찾아낸다.
    # -2 하는 이유는 i는 첫번쨰 숫자의 인덱스 , j : 두번쨰 숫자의 인덱스( 항상 i + 1이상), k : 세번쨰 숫자의 인덱스 ( 항상 j + 1이상)
    #  리스트에 숫자가 3개만 있는 경우를 생각해보면 됨. i = 0 , j = 1, k = 2 일 수 있도록 -2 하는 것.
    for i in range(len(nums) - 2):

        # 중복된 값이 있을 수 있음으로 이 경우 다음과 같이 continue로 건너뛰도록 처리한다.
        # i > 0: 이 조건은 i가 첫 번째 인덱스(0)가 아닐 때만 비교를 수행. (i는 인덱스 임으로 0 일때는 비교할 숫자가 없음)
        # nums[ i -1 ] : 바로 이전의 숫자와 현재 숫자가 중복 숫자인지 확인, 현재 nums.sort()했기때문에 이전 숫자와 현재 숫자가 같다면 둘은 중복이다 ex) [-1, -1, 0 , 1 ]
        if i > 0 and nums[i] == nums[ i -1 ]:
            continue

        # 두 번째 숫자를 선택하는 반복문 첫 번째 숫자(i) 바로 다음부터 시작. len(nums) -1하는 이유는 위에 설명했다 싶이 k인덱스의 값을 남겨둬야하기때문.
        for j in range( i + 1, len(nums) -1 ):
            # j > i + 1 : i + 1이 j의 첫번째 시작 값임으로 그 이상의 값일때만 비교 가능 ( i + 1 이전의 숫자는 비교할 숫자가 없음)
            #  nums[ j - 1 ] : 바로 이전의 숫자와 현재 숫자가 중복 숫자인지 확인, 현재 nums.sort()했기때문에 이전 숫자와 현재 숫자가 같다면 둘은 중복이다.
            if j > i + 1 and nums[j] == nums[ j - 1 ]:
                continue
            # 세 번째 숫자를 선택하는 반복문 , 두번째 숫자 (j)의 바로 다음부터 시작.
            for k in range(j + 1, len(nums) ):
                # 위와 같음
                if k > j + 1 and nums[k] == nums[ k -1]:
                    continue
                # 세번째 값까지 정해졌는데 첫번째 + 두번째 + 세번째 의 합이 0 이라면 그 값을 return
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([ nums[i], nums[j], nums[k] ])
    return result

# [ 풀이 2 ] 투 포인터로 계산
# 풀이 1에 비해 시간 복잡도를 O(n^2)로 개선
def threeSum2(nums: List[int]) -> List[List[int]]:
    result = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 투 포인터 위치 셋팅
        left, right = i + 1, len(nums) - 1

        # 두 포인터 들이 만나기 전까지.
        while left < right:

            # 현재 투 포인터가 가르키는 숫자들의 합.
            sum = nums[i] + nums[left] + nums[right]

            # sum이  0 보다 작다면 값을 더 키워야함으로 left를 우축(뒤)으로 이동함.
            if sum < 0:
                left += 1

            # sum이 0보 보다 크다면 값을 줄여야함으로 right를 좌측(앞)으로 이동
            elif sum > 0:
                right -= 1

            # sum = 0 이라면
            else:
                # 결과를 저장
                result.append([ nums[i], nums[left], nums[right] ])

                # 결과를 저장하고 난 후에는 '모든 유효한 조합'을 찾아야하기때문에 다음 조합을 찾기위해 게속 탐색을 진행해야함.
                # left < right : 아직 투 포인터가 만나지 못한 상황 = 한바뀌 안 돌았다는 뜻.
                # 지금 왼쪽 포인터의 값과 다음 왼쪽 포인터의 값이 같다면, 중복 숫자라는 뜻임으로 왼쪽 포인터를 두칸 뒤로 옮겨야함.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # 위의 상황과 같음. 지금 오른쪽 포인터의 값 == 다음 오른쪽 포인터의 값이 같다면? 오른쪽 포인터를 다시 두칸 앞으로 옮겨야함.
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 중복 처리가 끝난 후, 다음 조합을 찾기 위해 left와 right 포인터를 각각 한 칸씩 이동
                left += 1
                right -= 1

    return result

if __name__ == "__main__":

    nums = [ -1, 0, 1, 2, -1, -4]
    # 출력 [ [-1, 0, 1], [-1, -1, 2] ]
    print(f"threeSum : {threeSum2(nums)}")
    print(f"threeSum2 : {threeSum2(nums)}")
