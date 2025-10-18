import heapq
from typing import List

# 55 ) 배열의 K번쨰 큰 요소
# 정렬되지않은 배열에서 k번쨰 큰 요소를 추출하라.

# [ 풀이 1 ] heapq 모듈 이용
# 상위 K 빈도 요소와 비슷한 문제다. 다른 점이라면 가정 큰 값이냐, 가장 빈번한 값이냐의 차이 정도임.
def findKthLargest(nums: List[int], k : int) -> int:

    heap = list()

    # 입력값을 힙에 넣어준다.
    # heapq는 최소 힙을 지원하므로, 가장 큰 값을 찾기 위해 입력 요소들을 음수로 변환하여 저장한다.
    for n in nums:
        heapq.heappush(heap, -n)

    # 가장 낮은 수 부터 추출해 부호를 변환하면 최대 힙처럼 동작하도록 할 수 있다.
    # 1번째부터 (k-1)번째로 큰 요소들을 제거한다. (음수 기준으로는 '가장 작은' k-1개)
    for _ in range(1,k):
        heapq.heappop(heap)

    # 힙의 루트에 남은 k번째 큰 요소를 꺼내고, 다시 양수로 변환하여 반환한다.
    return -heapq.heappop(heap)

# [ 풀이 2 ] heapq 모듈의 heapify 이용
def findKthLargest2(nums: List[int], k : int) -> int:

    # 모든 값을 꺼내서 push 하지 않고도 한번에 heapify()하여 처리할 수 있다.
    # heapify() : 주어진 자료구조가 힙 특성을 만족하도록 바꿔주는 연산. 일반적인 리스트는 힙 특성을 만족하는 리스트로 값의 위치가 변경된다.
    # 하나라도 값을 추가하면 다시 힙 특성이 꺠지지만 추가가 계속 일어나는 형태가 아니기때문에 heapify()는 한번만 해도 충분하다.
    heapq.heapify(nums)
    for _ in range(len(nums) - k ):
        heapq.heappop(nums)
    return heapq.heappop(nums)

# [ 풀이 3 ] heapq 모듈의 nlargest 이용
def findKthLargest3(nums: List[int], k: int) -> int:
    # heapq.nlargest() : 가장 큰 값부터 시작하여 총 k개의 요소를 찾아서 리스트 형태로 반환한다. 즉 가장 큰 값부터 k번째 까지의 배열을 리턴한다. 여기서 마지막 인덱스 -1이 [k]번째 값이 된다.
    # 힙이 아니라도 내부적으로 heapify()함수도 호출해 처리해주기떄문에 별도로 힙처리를 할 필요가 없어 편리하다.
    # nsmallest()를 사용하면 동일한 방식으로 n번째 작은 값도 추출이 가능하다.
    return heapq.nlargest(k, nums)[-1]

# [ 풀이 4 ] 정렬을 이용한 풀이
# 정렬부터 한다음 k번쨰 값을 추출하는 방식으로 풀이한다. 추가, 삭제가 빈번할때는 heapq을 이요한 힙 정렬이 유용하지만 이처럼 입력값이 고정되어있을떄는 한번 정렬하는 걸로 충분하다.
def findKthLargest4(nums: List[int], k: int) -> int:
    return sorted(nums, reverse=True)[ k - 1 ]

if __name__ == "__main__":

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4

    print("findKthLargest   기대 출력값 : 4  |   실제 출력값    : " , findKthLargest(nums[:],k))
    print("findKthLargest2  기대 출력값 : 4  |   실제 출력값    : " , findKthLargest2(nums[:],k))
    print("findKthLargest3  기대 출력값 : 4  |   실제 출력값    : " , findKthLargest3(nums[:],k))
    print("findKthLargest4  기대 출력값 : 4  |   실제 출력값    : " , findKthLargest4(nums[:],k))