from typing import List
# 84 ) 괄호를 삽입하는 여러가지 방법
# 숫자와 연산자를 입력받아 가능한 모든 조합의 결과를 출력하라

# [ 풀이 1 ] 분할 정복을 이용한 다양한 조합
# 모든 조합을 계산해야하는데 분할정복으로 가능하다.
# *,-,+ 연산자가 등장할때 좌/우 분할을 하고 각각 계산 결과를 리턴한다.
# 즉, 연산자를 기준으로 재귀적으로 left,right를 계속 분할하고 분할한 값을 합친다.
def diffWaysToCompute( input : str ) -> List[int]:

    # 재귀적으로 분할한 left, right를 합치는 함수
    # op : 현재 연산자
    def compute(left, right, op):
        # 결과가 복수일수도 있기때문에 배열로 선언
        results = []

        # 중첩 루프를 사용하여 left의 모든 값과 right의 모든 값을 조합한다.
        for l in left:
            for r in right:
                # eval() : 문자열 형태의 수식 ("2" + "+" + "3")을 실제 계산(2 + 3)으로 실행하고 결과를 리스트에 추가
                results.append(eval(str(l) + op + str(r) ))
        return results

    # 재귀의 종료 조건
    # 입력 문자열이 연산자없이 숫자만 남아있다면 더이상 분할할수 없다.
    # 이 경우 이 숫자를 정수형으로 변환하여 리스트 형태로 반환하고 재귀를 종료한다.
    # isdigit() : 문자열(string)을 구성하는 모든 문자가 0부터 9 사이의 숫자(digit)인지를 검사한다.
    if input.isdigit():
        return [int(input)]

    results = []

    # 문자열을 순회하며 연산자를 찾는다.
    for index, value in enumerate(input):
        if value in "-+*":
            # 연산자가 존재할 경우 분할에 들어간다.
            left = diffWaysToCompute(input[:index])
            right = diffWaysToCompute(input[index + 1:])

            # 재귀 호출을 통해 얻어낸 결과는 각 부분에서 나올 수 있는 모든 가능한 계산 결과 리스트를 받아와 현재 연산자(value)로 모두 조합해 계산한다. 이 부분이 '결합'하는 부분이다.
            # 중요한 건 결과값이 배열 일수도있다는 점이다. 예를 들어 3-4*는 -17, -15의 복수 개의 계산 결과를 가질 수 있다.
            # 그러므로 results에 더할때 append가 아니라 extend를 쓴다. extend는 리스트에 또다른 리스트를 삽입할때 리스트를 풀어서 리스트 안의 각각 엘리면트를 삽입한다.
            results.extend(compute(left, right, value))

    return results

if __name__ == "__main__":
    # ( (2-1) - 1 ) = 0
    # ( 2 - (1-1) ) = 2
    input1 = "2-1-1"

    # ( 2* ( 3 - (4*5) ) ) = -34
    # ( (2*3) - (4*5) ) = - 14
    # ( (2 * (3-4)) * 5 ) = -10
    # ( 2 * ( (3-4) * 5 ) ) = -10
    # ( ((2*3) -4) * 5 ) = 10
    input2 = "2*3-4*5"


    print(diffWaysToCompute(input1))
    print("[ 0 , 2 ]")
    print(diffWaysToCompute(input2) )
    print(" [ -34, - 14, -10, -10, 10 ] ")

