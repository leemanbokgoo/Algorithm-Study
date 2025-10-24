import collections
from typing import List
# 76 ) 부분 문자열이 포함된 최소 윈도우
# 문자열 S와 T를 입력받아 O(n)에 T의 모든 문자가 포함된 S의 최소 윈도우를 찾아라.

# [ 풀이 1 ] 브루트 포스로 탐색
# 최소 윈도우라고 했음으로 T의 크기부터 시작해 점점 크기를 키워나가며 모든 윈도우 크기에 대해 탐색을 시도해볼 수 있다.
# 이 풀이의 경우 시간복잡도가 O(n^2)이기때문에 실제로는 이렇게 풀이해선 안된다.
def minWindow(s : str, t : str) -> str:

    def contains(s_substr_lst : List , t_lst : List) :
        # t의 문자를 하나씩 비교하며 슬라이딩 윈도우내에 속한 문자를 제거하는 방식으로 포함여부를 판단함
        # 문자 단위의 포함 여부를 판별하는 것은 반드시 일대일로 문자가 대응되어야한다는 점에서 전체를 한꺼번에 비교하기 어렵고 정렬해서 풀이하기도 어렵다.
        for t_elem in t_lst:
            if t_elem in s_substr_lst:
                s_substr_lst.remove(t_elem)
            else :
                return False
        return True

    # 예외 처리
    if not s or not t:
        return ''

    window_size = len(t)

    # 윈도우 사이즈를 계속 늘려가면서 contains()으로 탐색
    for size in range(window_size, len(s) + 1):

        # left가 윈도우의 시작 위치, i 이다.
        for left in range(len(s) - size + 1):
            # left에서 left + size까지 배열을 자르면 현재 윈도우 안에 있는 배열이다.
            s_substr = s[left : left + size]
            if contains(list(s_substr), list(t)):
                return s_substr
    return ''

# [ 풀이 2 ] 투 포인터, 슬라이딩 윈도우로 최적화
# 투 포인터를 사용하면 O(n^2)에서 O(n)으로 줄일 수 있다.
# 계속 우측으로 이동하는 슬라이딩 윈도우면서 적절한 위치를 찾았을때 좌우 포인터의 크기를 좁혀 나가는 투포인터로 풀이한다.
def minWindow2(s: str, t: str) -> str:
    # 기본 변수 정의
    need = collections.Counter(t) # 문자열 t에 필요한 각 문자의 개수를 딕셔너리 형태로 저장
    missing = len(t) # 아직 윈도우 내에서 찾지 못한 t에 있는 문자의 총 개수를 저장

    # left : 슬라이딩 윈도우의 왼쪽 포인터
    # start, end: 최소 윈도우의 시작과 끝 인덱스를 저장할 변수
    left = start = end = 0

    # 오른쪽 포인터인 right의 값을 점점 늘리면서 반복문을 실행
    # 슬라이딩 윈도우의 크기가 점점 더 커진다.
    # enumerate(s, 1) : 1부터 시작한다는 의미. 1부터 시작하는 이유는 left, right가 각각 앞이랑 끝을 가리키는데 left가 0부터 시작함으로 right는 최소 1이여야한다.
    for right , char in enumerate(s, 1):

        # missing = missing - ( need[char] > 0)
        # need[char]이 1이상이라면 현재 문자(char)가 t에 필요한 문자라는 소리임으로 missing 개수를 1 줄인다.
        missing -= need[char] > 0
        # char 문자를 하나 사용했으므로 need 딕셔너리에서 해당 문자의 필요 개수를 1 줄인다.
        need[char] -= 1

        # missing == 0 : 필요한 모든 문자를 윈도우 안에 넣었다는 뜻이다.
        # 이렇게 되면 왼쪽 포인터를 줄 일 수 있는 지 살핀다.
        if missing == 0 :
            # left < right : left포인터가 right 포인터와 만나기 전까지
            # need[s[left]] < 0 : s[left]는 left가 현재 가리키고 있는 문자열이다. 이 문자열을 need에서 찾았는데 만약 해당 값이 0보다 작다.
            # 즉,음수라면 현재 윈도우에 t에서 필요한 문자보다 해당 문자가 더 많이(초과해서) 들어있음을 의미한다.
            # 음수에서 벗어날때까지(=필요없는 s[left]문자를 제거할때까지) 반복하며 left 포인터를 오른쪽으로 이동해 포인터를 축소시킨다.
            while left < right and need[s[left]] < 0:
                # need[s[left]] += 1 : 왼쪽 끝 문자 (s[left])를 윈도우에서 제거할 것임으로, need를 1 증가시킨다.
                need[s[left]] += 1
                # 왼쪽 포인터를 오른쪽으로 한 칸 이동시켜 윈도우를 축소한다.
                left += 1

            # not end : end가 0일때 즉, 초기 상태라는 말.
            # right - left <= end - start : 현재 윈도우의 길이 (right - left) 가 기존의 최소 길이(end - start)보다 짧거나,
            #                               아직 최소 윈도우를 찾지 못했다면 최소 윈도우를 갱신한다.
            if not end or right - left <= end - start:
                # 현재의 최소 윈도우 경계를 기록
                start, end = left, right
                # 이제 다음 윈도우를 탐색하기 위해 left 포인터의 위치를 옮겨야한다. 그렇게 되면 현재 윈도우에서 s[left]는 제거 됨으로, 해당 값의 missing 카운트를 +1 한다.
                need[s[left]] += 1
                # missing이 1 늘어나면서 if missing == 0 조건이 거짓이 되어 현재 유효 윈도우는 깨진다.
                missing += 1
                # 왼쪽 포인터를 다시 이동시켜 새로운 윈도우 탐색을 시작한다.
                left += 1

    # 최종적으로 찾은 포인터만큼 잘라서 배열을 반환한다.
    return s[start : end]

# [ 풀이 3 ] Counter로 좀 더 편리한 풀이
# [ 풀이 2 ]와 같은 방식으로 풀되 missing == 0 대신 Counter()의 AND 연산으로 비교한다.
def minWindow3(s: str, t: str) -> str:
    t_count = collections.Counter(t) # 문자열 t에 있는 각 문자의 개수 저장
    # 빈 Counter 객체생성. 여기에 슬라이딩 윈도우(s[left:right]) 안에 포함된 문자들의 개수를 실시간으로 추적하여 기록한다.
    # {'문자': 개수} 형태로 { 'A': 5, 'B': 2} 이런식으로 저장된다.
    current_count = collections.Counter()

    start = float('-inf')
    end = float('inf')

    left = 0 # 왼쪽 포인터

    for right , char in enumerate(s, 1):
        # current_count[char] = current_count[char] + 1
        # Counter의 특징(current_count는 Counter 객체임): 만약 char가 처음 들어온 문자라면, Counter는 0을 반환하고 거기에 +1을 한다.
        # 즉, 현재 문자(char)의 갯수를 카운팅하는 것.
        current_count[char] += 1

        # current_count & t_count : & 연산은 두 Counter 객체에서 공통으로 존재하는 문자들의 교집합을 구한다. 즉, current_count와 t_count의 교집합을 구한 것이다.
        # current_count & t_count == t_count : current_count와 t_count의 교집합이 t_count와 같다면,
        #                                      current_count가 t_count의 모든 문자를 최소한 필요한 개수만큼 포함하고 있다는 것을 의미한다.
        # right 포인터를 확장해나가다가 밑의 조건을 충족하면 while문이 돌아간다.
        while current_count & t_count == t_count:
            # 현재 윈도우의 길이(right - left)가 이전의 최소 길이(end - start)보다 작은지 확인
            if right - left < end - start:
                # 작다면 갱신
                start, end = left, right

            # 왼쪽 끝 문자(s[left])를 윈도우에서 제거
            current_count[s[left]] -= 1
            # 왼쪽 포인터를 오른쪽으로 한칸 이동시켜 윈도우를 축소한다.
            left += 1
            # 이런 식으로 left 포인터를 줄여나가며 최소 윈도우를 찾다가 current_count & t_count == t_count 조건을 만족하지 못하게 됬을때
            # right를 확장하는 반복문이 실행된다.

    # if end - start <= len(s): end - start는 유효한 윈도우의 길이다. 이 길이가 전체 문자열의 길이(len(s))보다 작거나 같다는 것은 유효한 윈도우를 찾았다는 뜻.
    return s [start:end] if end - start <= len(s) else ''

if __name__ == "__main__":

    S = "ADOBECODEBANC"
    T = "ABC"

    print("[ 풀이 1 ] 브루트 포스로 탐색 : ", minWindow(S,T), " | 기대 출력값 BANC " )
    print("[ 풀이 2 ] 투 포인터, 슬라이딩 윈도우 : ",minWindow2(S,T), " | 기대 출력값 BANC " )
    print("[ 풀이 2 ] Counter : ",minWindow3(S,T), " | 기대 출력값 BANC " )

