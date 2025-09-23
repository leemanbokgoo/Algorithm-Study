import sys
from typing import List

# 주식을 사고 팔기 가장 좋은 시점
# 한번의 거래로 낼 수 있는 최대 이익을 산출하라.

# [ 풀이 1 ] 부르트 포스로 계산
def maxProfit(prices: List[int]) -> int:
    max_price = 0
    for i , price in enumerate(prices):
        # 해당 prices[i]의 값에 price를 빼서 가장 큰 값이 나오는 경우로 max_price를 변경
        for j in range(i, len(prices)):
            max_price = max(prices[i] - price, max_price )
    return max_price

# [ 풀이 2 ] 저점과 현재 값과의 차이 계산
def maxProfit2(prices: List[int]) -> int:
    profit = 0
    #  Python에서 정수(integer)가 가질 수 있는 가장 큰 값
    min_price = sys.maxsize

    # 입력된 가격 리스트 prices를 처음부터 끝까지 하나씩 순회.
    for price in prices:
        # price와 min_price중 더 낮은 가격을 min_price로 넣음.
        # 배열 중 가장 작은 값이 아니라 배열의 순서가 계산에 영향을 미치기때문에 prices배열중에 작은 값을 찾는 게 아니라
        # 반복문이 반복될때 가장 작은 값을 찾는 것.
        # 예를들어, price가 7일떄 min_price는 7이 됨. 7이 가장 첫번째 가격이기 떄문임.
        # 1이 더 작은 값이지만 주식을 사고 팔기 좋은 시점<이기떄문에 이후 주식의 값이 더 작다고 해서 현재 계산에서 min_price로 쓸수 없음.
        min_price = min(min_price, price)
        # 현재 가격(price)에서 가장 낮은 가격을 빼서 현재 이익을 계산
        # 현재 이익이 profit 크다면 profit 값을 덮어씌운다.
        profit = max(profit, price - min_price)

    return profit

if __name__ == "__main__":

    # 참고로 배열은 시간 순으로 주식의 값을 나타내는 것. 그렇기떄문에 1에 사서 7에 팔수 없. 1->7 순이니까.
    nums = [7,1,5,3,6,4]
    # 출력 5 | 1일때 사서 6일때 팔면 5의 이익을 얻는다.
    print("maxProfit" + str(maxProfit(nums)))
    print("maxProfit2" + str(maxProfit2(nums)))
