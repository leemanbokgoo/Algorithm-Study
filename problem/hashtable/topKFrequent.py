import collections
import heapq
from typing import List

# 상위 K 빈도 요소
# 상위 k번 이상 등장하는 요소를 추출하라

# [ 풀이 1 ] Counter를 이용한 음수 순 추출
#  요소의 값을 키로 하는 해시 테이블을 만들고 여기에 빈도 수를 저장한 다음, 우선순위 큐를 이용해 상위 k번만큼 추출하면 k번 이상 등장하는 요소를 손쉽게 추출할 수 있다.
# 파이썬에서 우선 순위 큐는 힙을 활용하는 heapq 모듈을 사용한다.
def topKFrequent(nums : List[int], k : int) -> List[int]:
    # 매개변수로 들어온 배열의 요소들이 몇번이 중복되는지 카운팅해줌.
    freqs = collections.Counter(nums)
    freqs_heap = [] # 요소를 빈도 순으로 정렬하기 위해 사용할 힙리스트.

    # 힙에 freps(빈도수 배열) 넣어줌.
    for f in freqs:
        # 빈도 수를 키로, freqs의 키를 값으로 키/값을 바꿔서 힙에 추가.
        # 이유는 힙은 키 순서대로 정렬되기 때문에 이를 위해 빈도수를 키로 한 것이다.
        # 값을 음수로 정한 이유는 파이썬 heapq 모듈은 최소 힙만 지원하기때문에 최소 힙을 그대로 지원하되 음수로 변환해 가장 빈도수가 높은 값이 가장 큰 음수가 되게 한것.
        # 이렇게 최소 힙으로도 빈도 수가 가장 높았던 값 추출 가능.
        # 모듈차원에서 최대힙도 지원하지만 메소드가 프로텍티드 멤버로 선언되어있고 함수명이 밑줄(_)로 선언되어있어 직접 호출은 권장되지않음.
        #  (-freqs[f], f) : 튜플. -freqs[f]는 빈도수의 음수 값, f는 값(value)이다.
        # 튜플은 딕셔너리처럼 key, value로 구성된 자료구성은 아니지만 heapq 모듈의 특성을 이용하기 위해 튜플의 첫 번째 요소를 인위적인 Key로, 두 번째 요소를 실제 Value로 사용하는 방식이다.
        # 파이썬은 튜플을 정렬할때 첫번쨰 요소를 보고 첫번쨰 요소가 겹치면 두번쨰 항목을 비교하는 방식이라 최소 힙으로 정렬이 가능하다.
        heapq.heappush(freqs_heap, (-freqs[f], f)) # heapq.heappush(데이터 저장소, 삽입할 요소)

    topk = list() # 빈 리스트 생성 topk = []와 같음.
    # k 만큼 반복
    for _ in range(k):
        # heappop 을 사용하여 가장 음수인 값을 꺼낸다.
        # [1]은 꺼낸 튜플에서 value에 해당되는 부분이 index [1]에 저장되어있기때문에.
        topk.append(heapq.heappop(freqs_heap)[1])

    return topk

# [ 풀이 2 ] 파이썬다운 방식
def topKFrequent2(nums : List[int], k : int) -> List[int]:
    # Counter.most_common() : 빈도 수가 높은 순서대로 아이템을 추출  ex) [(요소, 빈도수)] [ (1,3), (2,2)]
    # * : 언패킹 연산자, [(1, 3), (2, 2)]와 같은 리스트 앞에 붙으면, 리스트를 풀어헤쳐 개별 인자(튜플)로 만든다. 즉, zip 함수에 (1, 3)과 (2, 2)가 개별 인자로 전달
    # zip() : 여러 이터러블(iterable)을 인자로 받아, 같은 인덱스에 위치한 요소들을 묶어 새로운 튜플로 만든다. ex) ((1,3), (2,2)) -> ((1,2),(3,2))
    # list(...): zip()의 결과((1, 2), (3, 2))를 리스트로 변환하면 [ (1, 2), (3, 2) ]가 된다.
    # [0] :  인덱스 [0]에 위치한 튜플을 추출.
    return list(zip(*collections.Counter(nums).most_common(k)))[0]

if __name__ == "__main__":
    # 입력값 설정
    nums = [1,1,1,2,2,3]
    k = 2

    print(f" [ 풀이 1 ] Counter를 이용한 음수 순 추출 : {topKFrequent(nums)}")
    print(f" [ 풀이 2 ] 파이썬다운 방식 : {topKFrequent2(nums)}")