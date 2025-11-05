from typing import List
# ) 카카오 공채 비밀 지도
# 문제 설명 :  https://tech.kakao.com/posts/344

def solution(n : int, arr1 : List[int], arr2 :  List[int] ) ->  List[int]:
    maps = []

    for i in range(n):
        maps.append(
            bin(arr1[i] | arr2[i])[2:]
            .zfill(n)
            .replace('1', "#")
            .replace('0', ' ')
        )

    return maps

