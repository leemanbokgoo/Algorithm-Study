import bisect
from typing import List
# 82 ) 쿠기 부여
# 아이들에게 1개씩 쿠키를 나눠줘야한다. 각 아이(child_i)마다 그리드 팩터를 갖고 있으며 이는 아이가 만족하는 최소 쿠키의 크기를 말한다.
# 각 쿠키()는 크기 s를 가지고 있으며 s_j > = g_i이어야 아이가 만족하며 쿠키를 받는다.
# 최대 몇명의 아이들에게 쿠키를 줄 수 있는 지 출력하라.
# 참고) s_j > = g_i는 if s[j] >= g[i]: 과 같으며 쿠키 사이즈가 아이들이 원하는 크키 사이즈보다 크거나 같야아한다.는 뜻임.

# [ 풀이 1 ] 그리디 알고리즘
def findContentChildren( g : List[int], s : List[int]) -> int:
    # 정렬을 해줘야 그리디 알고리즘으로 풀 수 있음.
    g.sort()
    s.sort()

    # 아이 index와 쿠키 index
    child_i = cookie_j = 0

    # child_i가 아이의 숫자보다 작을 동안, cookie_j가 쿠키 숫자보다 작을 동안.
    while child_i < len(g) and cookie_j < len(s):
        # 만약 현재 쿠키(s[cookie_j])의 크기가 아이가 원하는 쿠키의 크기(g[child_i])보다 크거나 같다면
        if s[cookie_j] >= g[child_i]:
            # 다음 아이로 넘어간다.
            child_i += 1

        # 리스트는 정렬 되어있으므로 현재 쿠키가 현재 아이를 만족시키지못하면 이 쿠키는 다음 아이도 만족하지못한다.
        # 왜냐면 다음 아이는 반드시 현재 쿠키보다 더 큰 쿠키를 원하기 때문이다.
        # 그럼으로 아이가 쿠키를 받든, 안받든 간에 쿠키는 다음 쿠키로 넘어가야한다.
        cookie_j += 1

    return child_i


if __name__ == "__main__":
    # 두번째 아이부터는 크기 2 이상의 쿠키가 필요하지만 갖고 있는 최대 크기는 1이기때문에 1명의 아이에게만 줄수 있다.
    child = [1,2,3]
    cookie = [1,1]

    # 충분한 쿠키를 갖고있고 2명 모두에게 쿠키를 줄 수 있다.
    child2 = [1,2]
    cookie2 = [1,2,3]

    print("[ 풀이 1 ] 그리디 알고리즘 : ", findContentChildren(child, cookie), " | 기대 출력값 1 " )
    print("[ 풀이 1 ] 그리디 알고리즘 : ", findContentChildren(child2, cookie2), " | 기대 출력값 2" )
