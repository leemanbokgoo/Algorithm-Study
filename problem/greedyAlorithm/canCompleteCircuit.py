from typing import List
# 81 ) 주유소
# 원형으로 경로가 연결된 주유소 목록이 있다. 각 주유소는 gas[i]만큼의 기름을 갖고있으며 다음 주유소로 이동하는데 cost[i]가 필요하다.
# 기름이 부족하면 이동 할 수 없다고 할때 모든 주유소를 방분할 수 있는 출발점의 인덱스를 출력하라
# 출발점이 존재하지않을 경우 -1 을 리턴하며 출발점은 유일하다.

# [ 풀이 1 ] 모두 방문
# 한칸씩 출발점으로 지정하고 나머지 모든 주유소를 방문하는 방법으로 풀이한다.
# 참고로 주유소의 경로는 원형으로 연결 되어있다.
def canCompleteCircuit( gas : List[int] , cost : List[int]) -> int:

    for start in range(len(gas)):
        fuel = 0 # 기름값을 저장할 변수

        # start 지점부터 gas의 길이만큼 반복한다.
        for i in range(start, len(gas) + start) :
            # start 지점부터 시작해야하기때문에 i를 그대로 쓸 수 없으므로 나머지 연산을 통해 현재 이동할 주유소의 인덱스를 계산한다.
            # (예: 주유소가 4개일 때, 인덱스 3 다음은 4 % 4 = 0번 주유소
            index = i % len(gas)

            can_travel = True # 이동이 가능한지 여부 플래그 값

            # 현재 주유소(gas[index])에서 연료를 채웠을떄 총 연료(gas[index] + fuel)가 다음 주유소로 이동하는데 필요한 비용(cost[index])보다 적은지 확인.
            if gas[index] + fuel < cost[index]:
                # 적다면 이동 불가임으로 break로 이번 start의 반복문을 빠져나간다.
                can_travel = False
                break
            else:
                # 이동 가능하다면
                # 남은 연료 값을 계산한다.
                fuel += gas[index] - cost[index]

        # 반복문을 다 돌고도 can_travel true라면 모든 주유소를 무사히 방문한 것이다.
        # 이 문제는 출발점이 유일하다는 제약이 있다. 즉, 정답이 한군데라는 소리임으로 바로 해당 출발점을 반환한다.
        if can_travel:
            return start

    return -1

# [ 풀이 2 ] 한 번 방문.
# 전체 기름의 양이 전체 비용보다 클 경우 반드시 전체를 방문 할 수 있는 출발점이 존재한다.
# 이 문제는 출발점이 유일하다는 제약이 있으므로 여기서는 반드시 한군데만 존재하게 된다.
# i번 주유소까지 오는 여정 중 어느 지점에서 출발했든, i번 주유소에서 이동이 불가능하다면, i번 이전의 어떤 지점도 완벽한 출발점이 될 수 없다.
def canCompleteCircuit2(gas: List[int], cost: List[int]) -> int:

    # 총 공급되는 연료(sum(gas))가 총 소모되는 연료(sum(cost))보다 적다면, 완주는 불가능함으로 바로 -1를 반환.
    if sum(gas) < sum(cost):
        return -1

    start, fuel = 0, 0

    # 전체 인덱스를 한번씩 방문한다.
    # [ 풀이 1 ] 의 경우 start지점에서 end 지점까지의 전체 경로를 전부 돌면서 해당 start지점이 실패인지 성공인지를 확인했다. 즉, 전체 경로를 확인했지만
    # [ 풀이 2 ] 의 경우 부분 경로가 실패하면 어차피 전체 경로는 실패하기때문에 부분 경로들만 살펴보는 것이다.
    # 만약 i에서 i + 1로 가는 것이 실패한다면 i까지 도달하는 모든 start 지점은 실패한다. (이는 start 지점이 오름차순으로 존재하기때문에 가능함.)
    # 예를들어 3에서 실패했다면 어차피 1,2 start는 실패한다 왜냐? 1 -> 2-> 3 이런식으로 움직일 것이기때문이다. 3과 1,2의 경로가 겹쳐지기떄문.
    # 그래서 겹치지않는 새로운 경로 i + 1로 start 지점을 건너 뛰는 것이다.
    # 이런식으로 실패하는 부분 경로들을 없애고 나면 남아있는 유일한 후보 start가 정답이 되는 것이다.
    for i in range(len(gas)):
        # gas[i] + fuel(현재 연료량)이 cost[i](다음 주유소로 갈 때 필요한 연료량)보다 작다면
        # 현재의 start 지점은 실패했다는 것을 의미
        if gas[i] + fuel < cost[i]:
            # 새로운 출발 지점을 설정하고
            start = i + 1
            # 연료를 다시 0으로 리셋한다.
            fuel = 0
        else:
            # i번 주유소에서 다음으로 이동있다면
            # i번 주유소에서 얻은 연료와 소모한 비용의 차이만큼 갱신하여 누적한다.
            fuel += gas[i] - cost[i]

    return start

if __name__ == "__main__":
    gas =  [1,2,3,4,5]
    cost = [3,4,5,1,2]

    # 3번 인덱스(기름을 4만큼 충전할 수 있는)에서 출발할 경우는 다음과 같다.
    # 3번->4번 +4 -1 fuel 3
    # 4번->0번 +5 -2 fuel 6
    # 0번->1번 +1 -3 fuel 4
    # 1번->2번 +2 -4 fuel 2
    # 2번->3번 +3 -5 fuel 0
    print("[ 풀이 1 ] 모두 방문 : ", canCompleteCircuit(gas, cost), " | 기대 출력값 3 " )
    print("[ 풀이 2 ] 우선순위 큐 : ", canCompleteCircuit2(gas, cost), " | 기대 출력값 3 " )
