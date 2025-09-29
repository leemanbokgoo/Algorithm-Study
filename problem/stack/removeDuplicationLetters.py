# 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라.
# 사전식 순서 : 사전에서 단어를 찾는 방식과 같다.
# 다만 순서를 나열할때 ebcabc라면 결과값은 eabc다. 즉, 문자열의 위치를 마음대로 변경해서는 안된다. 중복을 제거하는 방식으로만 사전식 순서로 나열해야한다.
import collections


# [ 풀이 1 ] 재귀를 이용한 분리
# 결과 문자열의 첫번째 문자를 찾고 그 문자를 기준으로 나머지 문자열을 다시 재귀적으로 처리하는 방식으로 작동.
def removeDuplicationLetters( s: str )-> str:

    # sorted(set(s)) : 중복 문자열 제거 및 알파벳 순서대로 정렬
    # for char in sorted(set(s)) : 사전적으로 가장 작은 문자부터 순서대로 결과 문자열의 첫번째 후보로 검사.
    for char in sorted(set(s)):

        # s.index(char) : 현재 후보 문자 char가 원본 문자열 s에서 처음 등장하는 위치(인덱스)를 찾는다.
        # suffix = s[s.index(char)] : s.index(char)인덱스부터 문자열의 끝까지를 자른 부분 문자열. 이걸 suffix(접미사)라고 지칭.
        suffix = s[s.index(char):]

        # 둘다 중복을 제거 했을떄 위에서 자른 문자열과 s가 동일하다면
        #
        if set(s) == set(suffix):
            # if문을 통과한 char은 가장 사전적으로 작은 문자.
            # suffix.replace(char, '') : 남은 문자열(suffix)에서 방금 선택한 char를 모두 제거한다. ( char은 이미 사용했으므로 중복 제거)
            # char가 제거된 남은 문자열에 대해 재귀적으로 함수를 호출하여, 나머지 문자열에서 다시 사전적으로 가장 작은 다음 문자를 찾는다.
            # return '' 하고 있기때문에 removeDuplicationLetters(suffix.replace(char, '')의 마지막 재귀 값은 ''이 반환되고 실질적으로 재귀 호출 시 반환값은
            # 예를 들어 5번째 재귀 호출 최종 반환값은 '' , 4번쨰 재귀호출값은 b + '' , 3번째 재귀 호출값은 d + b + '' 이런식이 되서 결과값이 'acdb'가 된다.
            return char + removeDuplicationLetters(suffix.replace(char, ''))

    # 빈 문자열('')을 반환하며 재귀를 종료
    return ''

# [ 풀이 2 ] 스택을 이용한 문자 제거
def removeDuplicationLetters2( s: str )-> str:
    # collections.Counter(s) : Python의 collections 모듈에 있는 함수(정확히는 클래스)로,
    # 주어진 문자열 s와 같은 반복 가능한(iterable) 객체 내부의 요소들이 각각 몇 번 나타나는지를 자동으로 세어준다.
    # counter : 문자열 s에 포함된 각 문자의 남은 빈도수를 저장하는 딕셔너리
    # seen : 현재 스택에 이미 포함된 숫자들을 따로 기록해주는 집합, 스택(stack, 리스트로 구현됨)에서 특정 요소의 존재 여부를 검색하는 연산 속도가 느리기때문에 사용.
    counter, seen, stack = collections.Counter(s), set() , []

    for char in s:
        # counter[char] -= 1 : 현재 문자를 처리했으므로, 이 문자의 남은 빈도수를 1 감소
        # ex )  s="bcac" 이면 {'b': 1, 'c': 2, 'a': 1}
        counter[char] -= 1
        # 현재 처리 중인 문자 char가 이미 스택에 포함되어 있다면 이 문자를 추가할 필요가 없으므로 건너뜀.
        if char in seen:
            continue

        # stack[-1]은 스택(List)의 가장 마지막에 추가된 요소
        # char < stack[-1]: 현재 처리 중인 문자(char)가 스택의 최상단 문자보다 사전적으로 더 작다는 의미.
        # counter[stack[-1]] > 0 : 현재 스택의 최상단 문자(stack[-1])가 처리 중인 문자(char) 이후에도 문자열에 또다시 남아있다는 의미
        # 지금 더 작은 문자(char)가 들어왔고, 스택에 있는 더 큰 문자(stack[-1])는 뒤에 다시 나타날 예정이니, 나중에 다시 주워 담을 수 있도록 지금 제거하는 것임.
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            # 스택의 최상단 문자(stack.pop())를 제거하고, seen 집합에서도 제거
            seen.remove(stack.pop())
        # while 루프가 끝난 후 현재 문자 char은 스택에 추가.
        stack.append(char)
        # 이 문자가 스택에 들어갔음을 seen 집합에 기록.
        seen.add(char)

    return ''.join(stack)

if __name__ == "__main__":

    s1 = "bcabc"
    s2 = "cbacdcbc"

    print("=========== 재귀를 이용한 분리 ===========")
    print("출력값 : " + str(removeDuplicationLetters(s1)))
    print("출력값 : " + str(removeDuplicationLetters(s2)))

    print("=========== 스택을 이용한 문자 제거 ===========")
    print("출력값 : " + str(removeDuplicationLetters2(s1)))
    print("출력값 : " + str(removeDuplicationLetters2(s2)))
