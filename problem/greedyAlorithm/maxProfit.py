from typing import List
# 78 ) 주식을 사고 팔기 가장 좋은 시점 2
# 여러 번의 거래로 낼 수 있는 최대의 이익을 산출하라

# [ 풀이 1 ] 그리디 알고리즘
# 내리기 전에 팔고, 오르기전에 사면 된다. 다음 번 값이 현재보다 오르는 경우에 항상 이익을 취하는 형태로 코드를 구현한다.
def maxProfit( prices: List[int]) -> int:
    result = 0

    # 값이 오르는 경우 매번 그리디 계산
    # 가격 만큼 반복
    for i in range(len(prices) - 1):
        # 만약 다음 가격(prices[i + 1])이 현재 가격(prices[i]) 보다 크다면
        if prices[i + 1] > prices[i]:
            # 반환할 결과 값에 다음 가격(prices[i + 1]) - 현재 가격(prices[i])을 더한다.
            # prices[i + 1] - prices[i]은 얻은 시세 차익이다.
            result += prices[i + 1] - prices[i]

    return result

# [ 풀이 2 ] 파이썬 다운 방식
def maxProfit2(prices: List[int]) -> int:
    # for i in range(len(prices) - 1 : 반복문 순회
    # prices[i + 1] - prices[i] : 가격 차이 계산
    # max(,0) : 계산된 가격과 0 중에서 더 큰 값을 선택. 만약 가격이 상승했다면 (양수), 그 차이만큼 이익으로 더 한다. 가격이 하락했거나 같다면 (음수 또는 0), 이익은 0이 되므로 손해를 보지 않고 그냥 넘어간다.
    # sum() : 위에서 구한 결과 값을 합산하여 최대 이익을 반환.
    return sum(
        max(prices[i + 1] - prices[i], 0)
        for i in range(len(prices) - 1)
    )

if __name__ == "__main__":
    nums = [7,1,5,3,6,4]

    # 1일때 사서 5일때 팔아 4의 이익을 얻고 3일때 사서 6일떄 팔아 3의 이익을 얻는다. 4 + 3 = 7
    print("[ 풀이 1 ] 그리디 알고리즘 : ", maxProfit(nums), " | 기대 출력값 7 " )
    print("[ 풀이 2 ] 파이썬다운 방식 : ", maxProfit2(nums), " | 기대 출력값 7 " )
