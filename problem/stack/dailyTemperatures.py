from typing import List
# 일일 온도
# 매일 화씨온도 리스트 T를 입력받아서 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야하는 지를 출력하라.
# 예를들어 첫째 날 - 화씨 73, 둘째날 - 화씨 74라면 따뜻한 나을 위해서는 하루만 더 기다리면 된다.

# [ 풀이 1 ] 스택 값 비교
def dailyTemperatures( T:List[int] )-> List[int]:
    answer = [0] * len(T)
    stack = []

    #  i: 현재 날짜의 인덱스, cur: 현재 날짜의 온도 (T[i])
    for i, cur in enumerate(T):
        # 현재 온도(cur)가 스택의 최상단 인덱스에 해당하는 온도보다 높다면 계속 반복
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            # i : 더 높은 온도가 나타난 날짜의 인덱스
            # last : 기다리고 있던 날짜의 인덱스
            answer[last] = i - last

        # 스택이 비었거나, cur가 T[stack[-1]]보다 작거나 같을 때), 현재 날짜의 인덱스(i)를 스택.
        # 현재 온도가 더 높은 온도를 만났을 때, 그보다 낮았던 과거 온도의 정답이 결정되는 방식이기때문에 미리 stack에 값을 넣어놓지않는다.
        # 위에 반복문에서도 cur > T[stack[-1]] 라고 하고 있다. 여기서 핵심은 현재 온도가 T[stack[-1]]보다 크면 현재 인덱스 - stack의 인덱스 해서 stack의 인덱스에 value를 새로 넣어주는 것.
        stack.append(i)

    return answer


if __name__ == "__main__":

    T = [73, 74, 75, 71, 69, 72, 76, 73]
    # 출력값 : [1, 1, 4, 2, 1, 1, 0, 0 ]

    print("=========== 스택 값 비교 ===========")
    print("출력값 : " + str(dailyTemperatures(T)))
