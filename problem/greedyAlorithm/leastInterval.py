import collections
from typing import List
# 80 ) 테스크 스케줄러
# A에서 Z로 표현된 태스크가 있다. 각 간격마다 CPU는 한번의 테스크만 실행할 수 있고 n번의 간격 내에는 동일한 태스크를 실행할 수 없다.
# 더이상 태스크를 실행할 수 없는 경우 아이들(idle) 상태가 된다. 모든 태스크를 실행하기 위한 최소 간격을 출력하라

# [ 풀이 1 ] 우선순위 큐 이용
# 우선순위를 통해 그리디하게 풀 수 있는 문제로 아이템을 추출한 이후에는 매번 아이템 개수를 업데이트해야줘야한다.
# 이를 heapq만으로 구현하기에는 상당히 번거롭기때문에 Counter 모듈을 사용해서 코드를 구현한다.
def leastInterval( tasks : List[str] , n : int) -> int :

    # 입력된 작업 목록(tasks)에서 각 작업의 갯수를 카운팅.
    counter = collections.Counter(tasks)
    result = 0 # 작업할때 걸리는 간격

    # 우선 순위큐를 사용해 가장 개수가 많은 아이템부터 하나씩 추출해야하는데, 문제는 전체를 추출하는 게 아니라 하나만 추출하고 빠진 개수를 업데이트 할 수 있는 구조가 필요하다.
    while True:
        sub_count = 0 # 현재 라운드에서 실행된 작업의 개수를 기록하는 변수

        # counter.most_common : 가장 개수가 많은 아이템부터 출력하는 함수. 사실상 최대 힙과 같은 역할을 한다.
        # 남은 개수가 가장 많은 순서대로 최대 n + 1개의 서로 다른 작업을 선택하여 task에 넣어준다.
        # n + 1 하는 이유는 n개만 출력할 경우에는 예를 들어 n이 2라고 치면 A -> B 만 출력된다. 만약 A가 아직 남아있다면 다음 반복문에서 A가 나와
        # A->B->idle -> A 이런 식으로 나올 수 있다. 이러면 중간에 불필요한 idle이 들어가야한다.
        # 그러나 n+1을 하면 A-> B-> C ->A이런식으로 나오기때문에 idle을 최소화할 수 있다.
        # 즉,동일한 작업을 다시 실행하기전에 필요한 최소 슬롯이 n + 1이기 때문에 이 라운드에서 n + 1개의 서로 다른 작업을 배치하려고 시도하면 idle이 없이 가장 효율적으로 배치 가능하다.
        for task, _ in counter.most_common(n + 1):
            sub_count += 1 # 실행된 작업 갯수 증가
            result += 1 # 간격 증가

            # subtract(task) : 1개씩 개수를 줄여나간다.
            counter.subtract(task)
            # collections.Counter의 덧셈 연산자는 값이 0보다 큰 항목만 결과로 만 남긴다.
            # 고로 빈 collections.Counter()를 더해서 0 이하인 아이템을 목록에서 제거한다.
            counter += collections.Counter()

        # counter가 비어있다는 것 = 모든 작업이 완료되었음을 의미
        if not counter:
            break

        # 채워야할 idle 슬롯의 수를 구하는 부분. 현재 라운드가 끝난 후 다음 라운드가 시작될떄까지의 idle를 추가 한다.
        # n + 1 : 동일한 종류의 작업이 idle(n) 제약 조건을 만족하면서 연속적으로 실행될 때 필요한 최소 시간 간격
        #         1(작업) + n(idle) = n + 1이 하나의 작업의 주기가 된다.
        # 참가로 위에  for task, _ in counter.most_common(n + 1):에서 n+1만큼의 작업 갯수만 가져오기때문에 아래의 계산 값이 -음수가 나올 일은 없다.
        # 작업 주기 - 현재 라운드 작업 갯수를 뺴면 특정 작업을 위해 쉬어야할 idle의 간격이 나온다.
        result += (n + 1) - sub_count

    return result


if __name__ == "__main__":
    task = [ "A", "A", "A", "B", "B", "B"]
    n = 2

    # A -> B -> idle -> A -> B -> idle -> A -> B
    print("[ 풀이 1 ] 우선순위 큐 : ", leastInterval(task, n), " | 기대 출력값 8 " )
