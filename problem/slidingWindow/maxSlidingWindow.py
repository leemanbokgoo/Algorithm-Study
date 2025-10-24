import collections
from typing import List
# 75 ) 최대 슬라이딩 윈도우
# 배열 nums가 주어졌을때 k 크기의 슬라이딩 윈도우를 오른쪽 끝까지 이동하면서 최대 슬라이딩 윈도우를 구하라.

# [ 풀이 1 ] 브루트 포스로 계산
# 슬라이딩 윈도우를 우측으로 움직여 가며 max()로 최대값을 추출한다.
# 매번 윈도우의 최댓값을 계산하기때문에 시간 복잡도가 O(k*n)이다.
def maxSlidingWindow( nums: List[int], k : int) -> List[int]:

    # 예외처리
    if not nums:
        return nums

    r = []

    # k개의 윈도우를 움직여야함으로 마지막 윈도우는 k개 앞이여야한다. 그럼으로 nums에서 -k해야함.
    # 0부터 nums - k까지 반복문이 돌아야하는데 range(사이즈) 할시에 사이즈 값은 포함되지않음으로 +1 해야함.
    for i in range(len(nums) - k + 1):
        # 현재 위치[i]에서 슬라이딩 윈도우 범위 i+k 만큼 자른다.
        # 자른 배열의 max값을 구해서 배열에 추가.
        r.append(max(nums[i : i+k]))

    return r

# [ 풀이 2 ] 큐를 이용한 최적화
# max()를 계산하는 부분에서 최적화를 할 수 있다. 최댓값 계산을 최소화하기 위해 이전의 최댓값을 저장해뒀다가 한칸씩 이동할 때 새값에 대해서만 더 큰 값인지 확인하고,
# 최댓값이 윈도우에서 빠지게 되는 경우에만 다시 전체를 계산하는 형태로 개선한다.
def maxSlidingWindow2( nums: List[int], k : int) -> List[int]:

    results = []

    window = collections.deque() # 큐를 사용하기 위한 데크 선언.
    current_max = float('-inf') # 현재 윈도우의 최대값을 저장할 변수를 음의 무한대로 초기화

    for i , v in enumerate(nums):

        # 큐에 현재 값을 넣는다.
        window.append(v)

        # 현재 인덱스가 윈도우 크기 k에 도달하기 전(윈도우가 아직 가득 차지 않음)인지 확인한다.
        # 즉 첫번째 반복문에는 아직 윈도우가 가득 차지않음으로 첫번째 윈도우가 꽉 찰때까지 반복문을 돌리는 것.
        if i < k - 1:
            # if 조건이 참이면, 현재 반복을 건너뛰고 다음 반복문으로 건너뛴다..
            continue

        # 직전 윈도우에서 최대값에 해당되는 숫자를 제거하여 현재 배열 안에 직전의 최대값이 존재하지않는 상태인지 확인한다.
        if current_max == float('-inf'):
            # 그런 경우에는 윈도우 전체의 최댓값을 계산한다.
            current_max = max(window)

        # 만약 현재 값(윈도우가 한칸 이동하면서 새로 추가된 값)이 current_max보다 크다면
        elif v > current_max:
            # current_max 값을 갱신
            current_max = v

        # 최댓값을 구했다면 결과 배열에 넣어준다.
        results.append(current_max)

        # 한번 반복문이 돌았다면 슬라이딩 윈도우가 다음 칸으로 이동해야한다는 의미임으로 윈도우의 가장 왼쪽(가장 오래된) 요소를 제거한다.
        # 이때, 제거된 값이 이전 윈도우의 최대값과 같은지 확인한다.
        if current_max == window.popleft():
            # 제거된 값이 최대값과 같다면, 이제 최대값이 윈도우(큐)안에 존재하지않음으로 current_max를 초기화한다.
            # 초기화 시켜놓고 다음 반복문에 새롭게 만들어진 윈도우 배열 안에서 최댓값을 구하는 것이다.
            # 예를 들어 3이 최댓값인데, 다음 반복문에 윈도우가 한칸 이동하면, 윈도우에서 3이 없어진다고 가정한다. 이런 경우에는 v > current_max:을 통해 윈도우의 최댓값을 구할 수 없다.
            # 왜냐면 current_max가 직전 윈도우의 최댓값을 들고 있기때문이다. 고로 배열 안의 숫자를 전부 확인해서 다시 최댓값을 구해야한다.
            # 그럼으로 current_max = float('-inf')을 초기화하여 max()를 통해 새롭게 current_max를 구할 수 있도록 해준다.
            current_max = float('-inf')

    return results


if __name__ == "__main__":

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    print("[ 풀이 1 ] 브루트 포스로 계산 : ",maxSlidingWindow(nums,k), " | 기대 출력값 [ 3,3,5,5,6,7] " )
    print("[ 풀이 2 ] 큐를 이용한 최적화 : ",maxSlidingWindow2(nums,k), " | 기대 출력값 [ 3,3,5,5,6,7] " )
