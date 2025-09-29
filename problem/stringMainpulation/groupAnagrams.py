# 문자열 배열을 받아 에너그램 단위로 그룹핑 하라

import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    # 딕셔너리는 존재하지않는 키에 접근하면 에러가 남.
    # 그래서 defaultdict(list)를 사용하면 존재하지않는 키가 접근했을 때 자동으로 빈 리스트([])를 생성해서 넣어준다.
    # anagrams[].append() 할때 anagrams['존재하지않는 키'].append('값')을 했을때 원래라면 존재하지않는 키에 접근해야함으로 에러가 나야하지만
    # defaultdict(list)를 사용했기떄문에 빈 리스트([])를 만들어서 생성해준다.
    # 여기서 collections.defaultdict(list)의 list는 파이썬 내장 자료형(클래스)로 key: value형태의 딕셔너리(dict)를 생성할때 value에 list[]를 넣는다는 뜻임.
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        # 애너그램은 문자 순서를 바꿔도 같은 글자 조합이므로, 정렬하면 같은 문자열이 됨. "eat" → "aet" | "tea" → "aet" | "ate" → "aet" 전부 ate라는 키에 들어간다.
        # 파이썬에서 문자열을 sorted() 하면, 정렬된 문자 리스트가 나오기때문에 문자열이 아니라 key로 쓸수 없어 join()을 사용하여 리스트의 원소들을 하나의 문자열로 합쳐줌.
        anagrams[' '.join(sorted(word))].append(word)

    # 딕셔너리의 값들만 모아 리스트로 변환. 리스트들의 리스트 -> [[],[],[]]
    # list() 생성자에 iterable(반복할 수 있는 객체, for문에 넣을 수 있는 것들, ex) 문자열, 리스트, 튜플, 딕셔너리, 집합 등등)을 넣으면 리스트로 변환해줌.
    return list(anagrams.values())



if __name__ == "__main__":
    anagrams = [ "eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(anagrams))