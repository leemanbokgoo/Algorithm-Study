# 72 ) 두 정수의 합
# 두 정수 a와 b의 합을 구하라. + 또는 - 연산자는 사용할 수 없다.

# [ 풀이 1 ] 전가산기 구현
#  덧셈이나 뺄셈을 사용할 수 없기때문에 비트 연산만으로 풀어야하는 문제다.
def getSum(a : int, b : int) -> int:
    # 전처리
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFFF

    a_bin = bin( a & MASK)[2:].zfill(32)
    b_bin = bin( b & MASK)[2:].zfill(32)

    result = []

    carry = 0
    sum = 0

    # 32비트로 가정햇으므로 다음과 같이 32번 반복
    for i in range(32):
        A = int(a_bin[31 - i])
        B = int(b_bin[31 - i])

        # 전기산기를 통해 합 sum을 구하는 로직
        Q1 = A & B
        Q2 = A ^ B
        Q3 = Q2 & carry
        sum = carry ^ Q2
        carry = Q1 | Q3

        result.append(str(sum))

    if carry == 1:
        result.append('1')

    # 초과 자릿수 처리
    result = int(''.join(result[::-1]), 2) & MASK
    # 음수처리
    if result > INT_MAX:
        result = ~(result ^ MASK)

    return result

# [ 풀이 2 ] 좀 더 간소한 구현
# [ 풀이 1 ] 에서 구현한 전가산기를 핵심만 살려서 간단하게 동작 가능하게 풀이한다.
def getSum2(a : int, b : int) -> int:

    # MASK = 0xFFFFFFFF(16진수) : 이 마스크를 사용하여 연산 결과를 32비트 정수 범위로 강제하고, 특히 비트 연산 시 음수(2의 보수)를 올바르게 처리하기 위해 사용한다.
    # INT_MAX = 0x7FFFFFFF (16진수) : 32비트 부호 있는 정수의 최댓값 (2^31 - 1)이다.
    #                               최종 결과 a가 이 값보다 크면, 해당 숫자는 32비트 환경에서 음수로 간주하고 음수 처리 로직을 적용하기 위해 사용된다.
    MASK = 0xFFFFFFFF
    INT_MAX = 0x7FFFFFFFF

    # 합, 자릿수 처리
    # while b != 0 : b가 0이 될 때까지 (즉, 더 이상 자리 올림이 없을 때까지) 합과 자리 올림을 계산
    while b != 0:
        # (a ^ b) & MASK : a ^ b는 두 수의 비트 중 다른 비트만 1로 만든다. 자리 올림을 고려하지않는 두수위 합을 계산한다. MASK는 32비트 범위 유지를 위함이다.
        # ((a & b) << 1) & MASK : a ^ b는 두 수의 비트 중 다른 비트만 1로 만든다. 이 비트는 다음 자리로 올림되어야함으로 << 1(왼쪽으로 1칸 시프트)를 통해 자리 왼쪽으로 이동시킨다.
        #                          이 것이 다음 반복에서 더해져야할 carry값이 된다. 즉, carry값은 올림 값이다.
        a,b = (a ^ b) & MASK, ((a & b) << 1) & MASK

    # 음수 처리
    # 반복문이 끝나면 a는 두 수의 XOR 합이 된다. 이제 이 값이 음수인지 확인하고 필요하다면 변환
    if a > INT_MAX:

        # a = ~(a ^ MASK) : 2의 보수 변환을 수행하여 파이썬의 무한대 정수에서 32비트 부호 있는 음수 값으로 변환
        # a ^ MASK: 32비트 범위 내에서 a의 모든 비트를 반전($\sim$)시킨 것과 같다.
        # ~(...): 다시 모든 비트를 반전시킨 후, 1을 더하는 효과가 발생하여 (파이썬의 비트 반전 ~x는 -(x+1)이므로) 최종적으로 올바른 2의 보수 음수 값을 얻는다.
        a = ~(a ^ MASK)

    return a

if __name__ == "__main__":

    a1 = 1
    b1 = 2

    a2 = -2
    b2 = 3

    print("==================[ 풀이 1 ]==================")
    print( getSum(a1,b1), "         |    기대 출력값 : 3 ")
    print( getSum(a2,b2), "         |    기대 출력값 : 1 ")

    print("==================[ 풀이 2 ]==================")
    print( getSum2(a1,b1), "         |    기대 출력값 : 3 ")
    print( getSum2(a2,b2), "         |    기대 출력값 : 1 ")

