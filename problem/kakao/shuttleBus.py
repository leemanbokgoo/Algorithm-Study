from typing import List
# 카카오 공채) 셔틀 버스
# 문제 설명 :  https://tech.kakao.com/posts/344

# 문자형으로 들어오는 timetable의 입력값을 쉽게 계산 할 수 있는 형태로 변경하는 작업이 필요하다.
# 에포크 타임으로 변경하면 좋을 것 같은데 여기서는 시/분만 있는 형태이기떄문에 갇난히 분 단위로 변경하는 게 가장 쉬울 것 같다.
# 다른 언어라면 이 작업만 해도 적지않은 코드가 필요한데 파이썬은 다음과 같이 리스트 컴프리헨셔능로 간단하게 처리할 수 있다.

def solution( n : int, t : int, m : int, timetable : List[str]) -> str:

    # 입력으로 받은 크루들의 도착 시간(timetable)을 "HH:MM" 문자열 형식에서 분(minute) 단위의 정수로 변환
    # 예를들어 "09:00" -> 9 X  60 + 0 = 540 으로 변경하여 시간 비교 계산을 훨씬 간편하게 변경
    timetable = [
        int(time[:2]) * 60 + int(time[3:])
        for time in timetable
    ]
    # 변경한 값을 오름차순으로 정렬.
    # 순서대로 처리해야하기 때문에 분 단위로 변경 후에 바려 정렬하여 이후 처리가 편리하도록 준비하는 것.
    timetable.sort()

    # 셔틀버스는 09:00에 운행을 시작하며, 이를 분 단위로 변환하면 9 * 60 = 540분이다.
    # 변수 current는 현재 셔틀버스의 도착 시각(분 단위)을 저장하는 변수이다.
    current = 540

    #  총 n회의 셔틀 운행을 시뮬레이션하는 이중 for 루프
    for _ in range(n):
        # 사람의 수만큼 다시 for문 반복. 해당 시간에 도착한 버스에 크루를 탑승시킨다.
        for _ in range(m):

            # if timetable : 아직 탑승할 크루가 남아 있고
            # timetable[0] <= current : 가장 일찍 도착한 크루의 도착 시간이 현재 버스 도착 시간(current)보다 이르거나 같으면
            if timetable and timetable[0] <= current:
                # 해당 크루는 버스에 탑승한다.
                # 탑승하는 크루를 timetable에서 제거
                # 이 크루가 도착한 시간보다 1분 일찍 도착하는 시간을 candidate로 저장한다.
                # 1분 일찍 도착하는 시간을 저장하는 이유는 이 크루보다 1분만 일찍 도착하면 이 크루 대신 콘이 마지막 자리에 탈 수 있기때문이다.
                candidate = timetable.pop(0) - 1

            # 만약 정원 m명 이전에 if 조건이 거짓이 되었다면, 현재 버스 도착 시간(current)보다 늦게 도착하는 크루만 남았거나 (즉, 크루가 부족하거나) 이미 정원 m명이 꽉 찬 경우이다.
            else :
                # 버스에 아직 자리가 남았다는 뜻임으로 콘은 버스 도착 시간(current)에 맞춰 도착하면 안전하게 탑승할수 있다.
                # 이떄 candidate를 현재 버스 시간인 current로 설정한다.
                candidate = current

        # 현재 버스에 탑승할 크루들을 다 처리하고 나면 다음 버스에 들어갈 크루들을 처리해야한다.
        # 다음 버스는 t분 간격으로 오므로 current에 t를 더하여 다음 버스의 도착 시간을 갱신한다.
        current += t

    # candidate 변수에는 최종적으로 결정된 콘이 도착해야하는 가장 늦은 시간이 분단위로 저장되어있다.
    # 그러므로 분단위를 HH:MM 형태로 변경해야한다. candidate를 60으로 나누어 시간 h (몫)과 분 m (나머지)을 구한다.
    h , m = divmod(candidate, 60)
    # 시간과 분을 두 자리 문자열로 만들고 (zfill(2)) 콜론으로 연결하여 "HH:MM" 형식의 최종 결과를 반환
    return str(h).zfill(2) + ":" + str(m).zfill(2)
