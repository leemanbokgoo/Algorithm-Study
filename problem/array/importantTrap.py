# 높이를 입력받아 비 온후 얼마나 많은 물이 쌓일 수 있는 지 계산하라
from typing import List

from sympy.physics.units import volume


# [ 풀이 1 ] 투 포인터를 최대로 이동
def trap(height : List[int]) -> int :
    if not height :
        return 0

    volume = 0 # 총 물의 양
    left_index, right_index = 0, len(height) -1
    # 각각 포인터 시작점의 막대의 길이 ,즉 height 배열의 가장 첫번째 값(왼쪽 포인터)과 가장 마지막 값(오른쪽 포인터)
    left_max , right_max = height[left_index] , height[right_index]

    # 투 포인터가 만나기전까지 반복,
    # 양쪽에서 안쪽으로 한 칸씩 좁혀 들어가기 떄문에 왼쪽 포인터가 오른쪽으로 오른쪽 포인터가 왼쪽으로 가다보면 만나는 지점이 생김. 그 지점 전까지 반복.
    while left_index < right_index :

        # 현재 위치(left, right)의  left_max와 right_max를 갱신(이전 최대와 현재 높이 중 큰 값).
        left_max , right_max = max(height[left_index], left_max),max(height[right_index],right_max)

        # max값이 더 작은 쪽이 기준이 됨. 왜냐하면 [3, 0, 2] 길의 막대가 두개 있다고 하면 2만큼의 물의 양을 넣을 수 있기때문에.
        if left_max <= right_max:
            # 가장 높은 왼쪽 위치(left_max)에서 현재 왼쪽 높이(height[left])를 뺀 값이 물을 넣을 수 있는 공간의 값
            # @@@ 여기서 주의할 점은 왼쪽이라는 건 왼쪽 막대를 의미하는 게 아니라 배열의 방향을 의미하는 것. 즉,어느쪽 포인터를 기준으로 물높이를 계산할지 정하기 위한 용어다.
            # 지금 만약 height배열의 [3] 위치라면 막대의 길이는 1이다. 그 뒤의 값은 다 2보다 작다(=낮다) [8]의 값은 3이다.
            # 그러니 3-2 만큼 물을 채울 수 있다.
            # 바로 2칸뒤 막대 길이가 아니라 최대 길이(max)를 재는 이유는 2칸 뒤 막대 < 현재 막대 이더라도 max값 > 현재 막대 라면, 물을 담을 수 있기 때문이다.
            # 만약 현재  height[left_index] = 2 이고 left_max 가 0이라면 해당 막대는 2의 위치에 있으니까 물을 담을 수 없다.
            # 하지만 한번 더 반복문이 돌아서  left_max = 2로 갱신되고 height[left_index] = 0이면 2만큼의 물을 담을 수 있다.
            # 즉, 물은 막대가 낮을 떄 담긴다. 그러니까 최대 값이 갱신되기전까지는 물이 안 담기는 게 맞다.
            # 이건 왼쪽 포인터 기준이기 때문에 왼쪽 막대를 기준으로 최대 높이를 계속 갱신해가며 왼쪽 막대와 현재 위치를 비교하는 것임.
            # 왼쪽 막대 최대 길이 > 현재 위치면 물이 담긴다.
            volume += left_max - height[left_index]
            left_index += 1
        else:
            volume += right_max - height[right_index]
            right_index -= 1
    return volume

# [ 풀이 2 ] 스택 쌓기
# 스택에 쌓아나가면서 현재 높이가 이전 높이보다 높을 때,그 격차만큼 물 높이를 채운다.
def trap2(hegiht : List[int]) -> int :
    stack = []
    volume = 0

    ## 참고로 stack에는 막대의 길이 값이 아니라 index가 들어감.
    for i in range(len(hegiht)):

        # 스택이 비어있지않고 현재 막대의 값이 stack의 top보다 높으면 물이 고일 수 있는 구간이 발생.
        # stack[-1] : 스택에서 가장 마지막에 넣은 값, 즉 가장 위에 있는 값
        # 이 조건 때문에 반복문이 계속 돌아감. 유의할 것.
        # hegiht[i] > hegiht[stack[-1]] : 물이 고일 수 있는 구간이 생겼다는 뜻.
        while stack and hegiht[i] > hegiht[stack[-1]]:
            #스택에서 꺼낸다
            # stack.pop()하면 가장 마지막에 넣은 값을 꺼낼 수 있다.
            # @@@ 여기서 주의해야할 점 pop하면 값이 사라지지만 stack[-1]은 값을 확인하는 거라서 값이 남아있다.
            top = stack.pop()
            # 꺼낸 후 스택이 비어있다면
            if not len(stack):
                # 좌측 막대가 없다는 뜻임으로 물을 못 담는다
                break

            # i : 현재 막대 인덱스 (오른쪽 막대)
            # stack[-1] : 왼쪽 막대
            # 왼쪽 막대와 오른쪽 막대 사이 폭(가로 길이) 계산
            # 즉, 2, 0 , 0 , 3 이렇게 막대의 길이가 되어있다면 2칸 만큼의 가로 길이 * 높이를 계산해야하기때문
            # i - stack[-1]을 계산하면 왼쪽 막대를 포함하지않은 왼쪽 막대 바로 다음 칸부터 오른쪽 막대까지 포함한 칸 수 이다. 이러면 오른쪽 막대까지 포함이 되버린다.
            # 우리가 구해야하는 값은 왼쪽 막대과 오른쪽 막대의 사이의 공간이다. 고로 오른쪽 막대 값인 -1 을 해줘야한다.
            distance = i - stack[-1] - 1 # index임을 유의해서 볼 것.
            # min(hegiht[i], hegiht[stack[-1]]) : 두개의 막대 중 낮은 쪽을 기준으로 해야함으로 min을 사용
            # 가로 * 세로 = 현재 막대에서 채울 수 있는 물의 양이다.
            # 주의해야할 점은 물을 세로로 채운다고 생각하면 안된다. 가로로 채운다고 생각해야 이해가 쉽다.
            # [5, 2,0,0,3,6]의 경우 while문이 돌면서 0,4,3,8 이렇게 채우게 되는데 그림을 그려보면 이해가 쉽다.
            # 3에서 while문이 돌기 시작하고  2, 0, 0 , 3 에서 4만큼 채우고 5, 2, 0, 0, 3 에서 3 만큼 채우고 5, 2, 0, 0, 3, 6에서 8만큼 채운다.
            # 이렇게 되면 계산식이 2(낮은 쪽) * 4 , 3 * 1 , 5 * 2 이런식으로 된다.
            # 이렇게 되는 이유는 2 높이에서 3까지의 거리 2 만큼 채운다. 이렇게 되면 2, 0, 0 , 3은 빗물이 다 차있다.
            # 그러니까 3(낮은 쪽이 기준이다) - 2를 하면 높이는 1이다. 여기서 5와 3까지의 거리만큼 곱한다 3 * 1
            # 이제 3 높이 까지는 다 찼다 그럼 이제 5의 높이까지 채워야한다.  5 - 3 = 2 , 5와 6까지의 거리는 4다. 2 * 4
            volume += distance * waters

            # 담을 수 있는 물의 양은 가로길이 * 막대의 길이다.
            volume += distance * waters

        stack.append(i)
    return volume




if __name__ == "__main__":
    nums = [0,1,0,2,1,0,1,3,2,1,2,1]
    nums = [5,2,0,0,3,6]
    # 출력 6
    print("two pointer : " + str(trap(nums)))
    print("stack : " + str(trap2(nums)))
