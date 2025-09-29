## Stack(후입선출, LIFO, Last In First Out)

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495043477-fd252f33-8c77-40c5-9ab6-afc508ef4a0f.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250929T073155Z&X-Amz-Expires=300&X-Amz-Signature=628a7831efc251b72465f377e00391537c1cb8e0915bd7c3243fe501facdce23&X-Amz-SignedHeaders=host)


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

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495043222-b2d4f96c-0075-44b8-a0ee-796ee69ff772.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250929%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250929T073113Z&X-Amz-Expires=300&X-Amz-Signature=7f9b4f6b396db0d09093391f0656102977ffea333c9d83b4a302e56b7feaea6d&X-Amz-SignedHeaders=host)


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
