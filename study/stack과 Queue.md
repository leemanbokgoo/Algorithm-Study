## Stack(후입선출, LIFO, Last In First Out)

![image](https://github.com/user-attachments/assets/deed7331-1852-47da-98de-c433ac79c75c)


- stakc은 데이터를 쌓아 올리듯이 저장하는 자료구조.
- stack은 마지막에 저장한 데이터를 가장 먼저 꺼낸다. 이런 특징을 후입선출(LIFO)라고 한다. Last In, First Out
- 예를 들어 가장 마지막에 들어간 총알이 가장 먼저 발사되는 것과 같은 이치이다.
- stack에서는 push() 연산을 통해 새로운 데이터를 top위치에 삽입하고 pop()연산을 통해 가장 늦게 들어온 데이터(가장 위에 있는 데이터)를 제거 할 수 있다. 
- 데이터는 top을 통해섬나 접근 가능하며 중간에 있는 데이터를 직접 수정하거나 삭제할 수 없다. 

### stack의 사용사례
- 웹브라우저 방문기록(뒤로가기)
- 실행 취소
- 역순 문자열 만들기
- 후위 표기법 계산 

## Queue(선입선출, FIFO, First In First Out)

![image](https://github.com/user-attachments/assets/82838815-ef07-4a0e-a6f6-cbd54e75388a)

- 먼저 들어온 데이터가 먼저 나가는 선입선출 방식의 선형 자료구조.
- 은행에 가면 먼저 기다린 손님이 먼저 온 순서대로 서비스를 받는 것을 생각하면 됨.
- 큐는 front에서 데이터를 삭제(dequeue)하고 rear에서 데이터를 삽입(enqueue)한다. 즉, 한쪽 끝에서 데이터를 추가하고 반대쪽 끝에서만 삭제 할 수 있다. 

### Queue 사용사례
- 은행 업무
- 대기열 순서와 같은 우선순위의 작업 예약등
- 서비스 센터의 대기시간
- 프로세스 관리 

## stack VS Queue 비교
- 구조 : 후입선출(LIFO) VS 선입선출(FIFO)
- 삽입 방식 : push(top에서 삽입) VS enqueue(rear에서 삽입)
- 삭제 방식 : pop(top에서 삭제) VS dequeue(front에서 삭제)
- 접근 방식 : top을 이용해서만 가능 VS front에서만 삭제, rear에서 삽입
- 사용 사례 : 실행취소(undo),역순 문자열 VS 은행 업무,프로세스 관리


#### 참고자료 
https://jud00.tistory.com/entry/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-%EC%8A%A4%ED%83%9DStack%EA%B3%BC-%ED%81%90Queue%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
