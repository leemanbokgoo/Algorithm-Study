from typing import List
# 70 ) 싱글넘버
# 딱 하나를 제외하고 모든 엘리먼트는 2개씩 있다 1개인 엘리먼트를 찾아라

# [ 풀이 1 ] XOR 풀이
# 단 1개의 엘리멘트를 찾는데 XOR 연산자를 쓰면 적당하다.
# XOR은 입력값이 서로 다르면 True, 서로 동일한 경우 False가 되는 논리 게이트 연산자다.
# XOR은 같은 숫자끼리 XOR하면 0이 되지만 어떤 숫자와 0을 XOR하면 그 숫자가 그대로 나온다. 5 ^ 0 = 5다.
def singleNumber( nums : List[int]) -> int:
    result = 0
    for num in nums:

        # result ^= num : result = result ^ num
        # 모든 숫자에 대해서 XOR연산을 반복하는 부분.
        # 두번씩 짝을 이루는 숫자들은 서로 상쇄되어 0이 되고 최종적으로는 1번만 나타는 숫자만 result에 남게 된다.
        # 여기서 이게 가능한 이유는 XOR 연산은 덧셈과 근본적으로 다르기때문이다. 숫자를 더하는 것이 아니라, 비트(bit) 단위로 '기록'하는 개념에 가깝다.
        # result ^= num이 반복문에서 돌아갈 때, result는 이전 값들의 XOR 합을 유지하고 있다.
        # 결과값은 십진수로 변환되어 나오지만 실제 계산은 이진수(비트)로 계산로 계산하고 있기때문이다. 숫자를 덧셈하는게 아니라 각 자리의 비트 패턴을 기록한다.
        result ^= num

    return result

if __name__ == "__main__":
    nums = [2,2,1]
    nums2 = [4,1,2,1,2]

    print( singleNumber(nums), "         |    기대 출력값 : 1 ")
    print( singleNumber(nums2), "         |    기대 출력값 : 4 ")

