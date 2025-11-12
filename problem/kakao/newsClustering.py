import collections
import re
# 카카오 공채) 뉴스 클러스터링
# 문제 설명 :  https://tech.kakao.com/posts/344

# 자카드 유사도를 구현하는 문제로 다중 집합을 다뤄야한다. multiest 자료형이 필요하다 하지만 파이썬은 지원하지않는다.
# Counter()를 이용해 요소의 개수를 각각 계산하고 이 값의 sum()으로 교집합과 합집합을 구하는 형태로 구현한다.
def solution(str1 : str, str2 : str) -> int:

    # 입력 문자열을 두글자씩 끊어서 원소로 만든다.
    # 리스트 컴프리헨션 문법을 사용함.
    str1s = [
        # for문을 돌면서 if문 조건을 통과하면 밑의 코드가 동작하여 str1s배열에 들어갈 원소 들을 생성
        # 문자열을 두 글자씩 자르고 모두 소문자로 변환
        str1[i : i + 2].lower()
        for i in range(len(str1) - 1 )
        # re.findall은 파이썬의 정규 표현식(Regular Expression) 모듈인 re에서 제공하는 함수로, 입력 문자열 전체에서 주어진 패턴과 일치하는 모든 부분을 찾아서 리스트로 반환한다.
        # 헤딩 if문에서 re.findall()하는 건, re.findall()했을때 배열이 존재하면 True, 배열이 존재하지않으면 False로 if문 조건을 알려준다.
        if re.findall('[a-z]{2}', str1[i : i + 2].lower())
    ]

    str2s = [
        str2[i : i + 2].lower()
        for i in range(len(str2) - 1)
        if re.findall('[a-z]{2}', str2[i: i + 2].lower())
    ]

    # collections.Counter() : 리스트의 각 원소의 개수를 세어 다중집합으로 만든다. (예: Counter(['a', 'a', 'b']) -> {'a': 2, 'b': 1})
    # Counter(str1s) & Counter(str2s)는 두 다중집합의 교집합을 구한다. 다중집합의 교집합은 두 집합 중 더 적게 나타난 원소의 개수를 따른다.
    # .values() : 교집합 Counter에서 원소의 개수(값)만 추출한다.
    # sum(...)을 통해 교집합 다중집합에 포함된 총 원소의 개수를 구한다. 이것이 교집합의 크기이다.
    intersection = sum( (collections.Counter(str1s) & collections.Counter(str2s)).values())

    # Counter(str1s) | Counter(str2s)는 두 다중집합의 합집합을 구한다. 다중집합의 합집합은 두 집합 중 더 많이 나타난 원소의 개수를 따른다.
    union = sum( (collections.Counter(str1s) | collections.Counter(str2s)).values())

    # 1 if union == 0 : 만약 합집합의 크기(union)가 0이라면, 이는 두 문자열 모두에서 유효한 두 글자 쌍이 하나도 추출되지 않았다는 뜻임으로 이 경우 자카드 유사도는 1로 정의된다.
    # else intersection / union : 그렇지 않은 경우, 교집합 크기 / 합집합 크기를 통해 자카드 유사도 jaccard_sim을 계산
    jaccard_sim = 1 if union == 0 else intersection / union
    # 문제에서 요구하는 대로 유사도 값에 65536을 곱한 후 정수 부분만 반환
    return int(jaccard_sim * 65536)