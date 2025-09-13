# 주어진 문자열이 펠린드롬인지 확인해라.
# 펠린드롬 : 문자열을 뒤집어도 똑같은 말이 되는 문자열
# 입력 : A man, a plan , a canal : Panama  출력: true
# 일벽 : race a car 출력 : false
import collections
import re

from typing_extensions import Deque


# 풀이 1 : 리스트로 변환

def isPalindrome(slef, s: str) -> bool:
    strs = []
    for char in s:
        # 영문, 숫자 여부를 판별하는 함수로 이를 이용해 해당하는 문자만 추가한다.
        if char.isalnum():
            strs.append(char.lower()) # 모두 소문자로 변환

    # 펠린드롬 여부 판별
    while len(strs) > 1 : # 만약 strs의 길이가 1보다 크다면
        # .pop() 함수는 리스트의 마지막 요소를 꺼내고 반환하는 메서드.
        if strs.pop(0) != strs.pop(): # 가장 앞에 있는 문자열과 가장 뒤에 있는 문자열을 비교
            return False # 둘이 일치하지않으면 false 반환

    return True;

# 풀이 2 데크 자료형을 이용한 최적화
def isPalindrome(slef, s : str ) -> bool:
    # 자료형 테크로 선언
    # 리스트의 pop(0)은 O(n)인데 반해 데크의 popleft() 는 O(1)으로 성능차이가 크다.
    strs : Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1 :
        if strs.popleft() != strs.pop():
            return False

    return True

# 풀이 3 슬라이싱 사용
# 문자열을 조작할때는 항상 슬라이싱을 우선으로 사용하는 편이 속도 개선에 유리하다. 대부분의 문자열 작업은 슬라이싱으로 처히나느 편이 가장 빠르다.
def isPalindrome(slef, s : str ) -> bool:
    s = s.lower()
    #정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    # [::-1]를 사용하면 문자열을 뒤집을 수 있다.
    return s == s[::-1] # 슬라이딩

# 실행 테스트
if __name__ == "__main__":
    print(isPalindrome(None, "A man, a plan, a canal: Panama"))  # True
    print(isPalindrome(None, "race a car"))  # False