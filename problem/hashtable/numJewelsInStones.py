import collections
# 보석과 돌
# J는 보석이며 S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

# [ 풀이 1 ] 해시 테이블을 이용한 풀이
def numJewelsInStones(J: str, S: str) -> int:
    # 딕셔너리 초기화. 이 딕셔너리는 돌(S) 문자열에 나타나는 각 돌의 종류별 개수(빈도)를 저장하는 데 사용
    # Frequency를 줄인 말이 freqs로 빈도 라는 뜻.
    freqs = {} # 예: {'a': 2, 'B': 1}
    count = 0 # 최종적으로 찾은 보석의 총 개수를 저장하는 변수

    # 돌의 빈도 계산
    for char in S:
        # 해당 문자가 ferqs에 없으면
        if char not in freqs:
            # 해당 문자를 키로 한 딕셔너리 값 생성
            freqs[char] = 1
        # 해당 문자가 ferqs에 있으면
        else:
            # 기존에 있던 값을 +1
            freqs[char] += 1

    # 보석(J)의 빈도 수 합산
    for char in J:
        if char in freqs:
            # 만약 존재한다면, 그 보석의 개수(freqs[char])를 최종 count에 더한다.
            count += freqs[char]
    return count

# [ 풀이 2 ] defaultdict를 이용한 비교 생략
def numJewelsInStones2(J: str, S: str) -> int:
    # defaultdict: 키가 존재하지 않을 때 자동으로 기본값을 생성하여 초기화 해준다.
    freqs = collections.defaultdict(int)
    count = 0

    # defaultdict를 쓰기때문에 [ 풀이 1 ] 처럼 if문으로 if char not in freqs: 체크할 필요가 없음.
    for char in S:
        freqs[char] += 1

    # defaultdict를 쓰기때문에 [ 풀이 1 ]처럼 if char in freqs: 체크할 필요가 없음
    for char in J:
        count += freqs[char]

    return count

# [ 풀이 3 ]
def numJewelsInStones3(J: str, S: str) -> int:
    # 반복 가능한 객체(Iterable) (예: 문자열, 리스트, 튜플)를 인수로 받아 그 안에 있는 각 요소의 개수(빈도)를 세서 딕셔너리 형태로 저장해분다.
    freqs = collections.Counter(S)
    count = 0

    for char in J:
        count += freqs[char]

    return count

# [ 풀이 4 ] 파이썬 다운 방식
# 해시 테이블과는 관련이 없지만 이 문제는 파이썬 다운 방식으로 단 한줄로 계산 할 수 있다.
def numJewelsInStones4(J: str, S: str) -> int:
    # s in J for s in S : 제너레이터 표현식 (Generator Expression)
    # for s in S : 반복문
    # s in J : s 가 J 문자열안에 포함되어있는 지 확인.
    # 그러면 결과가 [True, True, True, False, False, False, False] 이런 식으로 나온다.
    # 여기서 sum 함수를 통해 true인 애들의 숫자를 계산하여 출력
    return sum( s in J for s in S )

if __name__ == "__main__":
    # 입력값 설정
    J = "aA"
    S = "aAAbbbb"
    expected_output = 3 # 출력값

    # 함수별 결과 출력
    print(f"입력: J='{J}', S='{S}', 예상 출력: {expected_output}\n")

    result1 = numJewelsInStones(J, S)
    print(f"numJewelsInStones 결과: {result1}, {'성공' if result1 == expected_output else '실패'}")

    result2 = numJewelsInStones2(J, S)
    print(f"numJewelsInStones2 결과: {result2}, {'성공' if result2 == expected_output else '실패'}")

    result3 = numJewelsInStones3(J, S)
    print(f"numJewelsInStones3 결과: {result3}, {'성공' if result3 == expected_output else '실패'}")

    result4 = numJewelsInStones4(J, S)
    print(f"numJewelsInStones4 결과: {result4}, {'성공' if result4 == expected_output else '실패'}")
