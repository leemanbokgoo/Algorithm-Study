import collections
from typing import List
# 카카오 공채) 캐시
# 문제 설명 :  https://tech.kakao.com/posts/344

# LRU 캐시 교체 알고리즘을 구현하는 문제이다.
# LRU는 캐시 교체 전략 중 하나로 가장 오래전에 사용된 아이템을 버리는 방식이다.
# 다만 주의해야할 점은 입력값에 0 이 포함되어있다는 점이다. 이 경우 예외 처리를 하지않고 LRU 알고리즘을 구현한다면 입출력이 달라져 주의가 필요하다.
# 즉, 캐시 메모리가 0이라는 소리이임으로 캐시가 없음으로 어떤 도시를 요청하든 절대로 캐시에서 찾을 수 없다. 캐시 메모리 자체가 존재하지않기때문이다.
# 따라서 캐시 miss가 됨으로 총 실행시간은 len(cities) * 5가 되어야한다.
# 문제에서 캐시 hit는 데이터를 요청했을 때, 요청한 데이터가 이미 가까이에 있는 임시 저장 공간인 캐시(Cache) 메모리에 존재하는 경우를 말하고
# 캐시 miss는 요청한 데이터를 캐시에서 찾지 못했을때를 의미한다.
def solution(cacheSize : int, cities : List[str]) -> int:

    # elapsed: 총 실행 시간을 저장하는 변수로, 0으로 초기화한다.
    elapsed : int = 0

    # maxlen=cacheSize를 설정함으로써 이 큐는 최대 cacheSize만큼의 요소만 저장할 수 있게 된다.
    # 새로운 요소가 추가될 때 (캐시 미스 시), maxlen을 초과하면 가장 오래된 요소(가장 왼쪽 요소)가 자동으로 제거된다. 이것이 LRU의 핵심 구현이다.
    # LRU를 바닥부터 구현할 수 있지만 길이가 제한된 자료형을 통해 손쉽게 구현할 수 있다. 파이썬에서는 Deque 자료형이 이에 해당된다.
    cache = collections.deque(maxlen=cacheSize)

    for c in cities:
        # 도시 이름을 소문자로 변환.
        # 캐시 정책은 대소문자를 구별하지않는다.
        c = c.lower()

        if c in cache:
            # 현재 케시에서 지우고
            cache.remove(c)
            # 다시 새롭게 넣어준다. 이는 이미 해당 도시가 캐시에 존재하더라도 순서에 따라 가장 최근에 사용한 것을 표시하기 위함이다.
            cache.append(c)
            # 캐시 hit임으로 실행시간을 + 1한다.
            elapsed += 1

        else :
            # 캐시에 추가하면 자동으로 가장 오래된 데이터는 삭제된다.
            cache.append(c)
            # 캐시 miss임으로 실행 시간을 + 5 한다.
            elapsed += 5

    return elapsed

