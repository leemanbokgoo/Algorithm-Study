## Heap 자료구조

![image](https://github.com/user-attachments/assets/79f9fb5b-cdc1-43bf-a5ec-f73ae7c8c9a7)

![image](https://github.com/user-attachments/assets/ca9f7b8d-b085-44c4-846f-c2601db33d17)

- 트리 기반 자료구조로 완전 이진 트리(Complete Binary Tree)으로 구현되어있으며, 우선 큐(Priority Queue)와 같은 최대값 또는 최소값을 빠르게 찾기 위한 자료구조.
- Heap의 핵심 개념은 각 노드가 부모-자식 간의 우선순위 규칙을 만족한다는 것. 우선 순위의 개념을 큐에 도입한 자료구조다.
- 주로 최소 힙(Min Heap)과 최대 힙(Max Heap)으로 나뉘어 사용된다.
    - 최대 힙(max heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
    - 최소 힙(min heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
- 최솟값이나 최댓값을 찾기 위해 배열을 사용하면 Ο(n)만큼 시간이 걸린다. 하지만 힙을 사용하면 O(logn)만큼 소요되므로, 배열을 사용할 때보다 빠르게 최솟값과 최댓값을 구할 수 있다. 우선순위 큐와 같이 최댓값 또는 최솟값을 빠르게 찾아야하는 알고리즘 등에 활용된다.
- 힙은 다음 조건을 만족하는 자료구조이다.
    - 힙은 최대힙(Max heap)과 최소힙(Min heap)으로 나뉘어진다. 최대힙은 자식 노드보다 부모 노드의 값이 크고, 최소힙은 자식 노드보다 부모 노드의 값이 작다.
    - 노드가 왼쪽부터 채워지는 완전 이진 트리 형태를 가진다.
    - 중복을 허용한다.
- 우선 순위 큐를 사용할때 매번 활용했던 heapq모듈이 힙으로 구현되어있으며 그중에서도 파이썬에는 최소 힙만 구현되어있다.
- 완전 트리 형태인 이진 힙은 배열에 빈틈없이 배치가 가능하며, 대개 트리의 배열 표현의 경우 계산을 편하게 하기 위해 **인덱스는 1부터 사용**한다. (특히 이진 힙에서는 항상 1번 인덱스부터 사용한다.)

## Heap 특징

### 완전 이진트리(Complete Binary Tree)
- 힙은 완전 이진 트리의 구조를 가지며, 마지막 레벨을 제외한 모든 레벨이 꽉 차 있고, 마지막 레벨은 왼쪽에서부터 차례대로 채워진다.

### 우선순위 규칙
- 힙에서는 부모 노드가 자식 노드보다 우선순위가 높다.여기서 우선순위는 대표적으로 두 가지 규칙으로 나뉜다. 
    - 최소 힙(Min Heap): 부모 노드의 값이 자식 노드보다 작거나 같다. 따라서 루트 노드는 항상 최소값을 가진다. (PriorityQueue가 기본적으로 최소 힙으로 동작한다)
    - 최대 힙(Max Heap): 부모 노드의 값이 자식 노드보다 크거나 같다. 따라서 루트 노드는 항상 최대값을 가진다.
- 여기서 오해하기 쉬운 특징 중 하나는 **힙은 정렬된 구조가 아니다.** 최소 힙의 경우 부모 노드가 항상 작다는 조건만 만족할 뿐. 서로 정렬되어있지않다. 예를 들어 오른쪽 자식 노드가 레벨차이에도 불구하고 왼쪽 노드보다 더 작은 경우도 이씅ㄹ 수 있다. 부모,자식 간의 관계만 정의할뿐 좌우에 대한 관계는 정의하지않기때문이다.

### 배열로 구현 가능
- 힙은 완전 이진 트리(Complete Binary Tree)이기 때문에 배열을 이용하여 쉽게 구현할 수 있다. 부모와 자식 노드 간의 관계는 배열의 인덱스를 통해 계산된다.)
    - 부모 인덱스 : i
    - 왼쪽 자식: 2 * i + 1
    - 오른쪽 자식: 2 * i + 2

![image](https://github.com/user-attachments/assets/66cc22f2-1e3a-45a8-9958-b5fc52f4605c)

#### Java에서의 Heap과 메모리 영역
- 특히 Java에서는 Heap 자료구조와 Heap 메모리 영역은 **완전히 다른 개념**
H- eap 메모리는 프로그램 실행 중 동적으로 할당되는 메모리 영역을 의미하고, Heap 자료구조는 우선순위 규칙을 만족하는 완전 이진 트리를 의미.
- Heap은 무언가를 쌓다, 무더기, 더미라는 뜻을 가지는 영어 단어로 Heap 자료구조와 Heap 메모리 영역 모두 어떤 의미에선 위 영어 단어의 뜻을 반영하는 개념이기 때문에 같은 이름이 지어진 것으로 보임

## Heap 용도 
- 힙  자료구조는 **우선순위 처리, 정렬, 그래프 탐색, 스케줄링** 등 다양한 분야에서 필수적인 자료구조로 활용된다.

### 우선순위 큐(Priority Queue)
- 힙은 우선순위 큐의 가장 기본적인 자료구조로 사용된다.
- 우선순위 큐는 데이터들에 우선순위를 부여하고, 우선순위가 높은 데이터를 먼저 처리하는 큐(Queue). 최소 힙을 사용하면 우선순위가 가장 낮은 값을 먼저 처리하고, 최대 힙을 사용하면 우선순위가 가장 높은 값을 먼저 처리한다.
- Java와 Python의 PriorityQueue는 기본적으로 최소 힙을 기반으로 구현되어 있으며, Java에선 필요에 따라 Comparator 등을 사용해 최대 힙처럼 동작하게 할 수 있다. (다만, Python은 음수로 변환하는 별도의 과정이 필요하다.)
- 우선 순위 큐를 활용한 다익스트라 알고리즘에도 활용된다.

### 힙 정렬(Heap Sort)
- 힙을 이용하여 정렬 알고리즘을 구현할 수도 있다. 
- 힙 정렬은 최대 힙을 사용하여 배열을 내림차순으로, 최소 힙을 사용하여 배열을 오름차순으로 정렬할 수 있다. 
- 힙 정렬은 최악의 경우에도 O(n log n)의 시간 복잡도를 보장하며, 안정적인 정렬 알고리즘으로 알려져 있다.

### 최소 신장 트리(Minimum Spanning Tree)
- Prim's Algorithm과 같은 최소 신장 트리 알고리즘에서는 우선순위 큐로 힙을 사용하여 가장 적은 비용으로 그래프의 모든 노드를 연결할 수 있다.

### 최단 경로 알고리즘(Shortest Path Algorithm)
- 다익스트라(Dijkstra) 알고리즘은 힙을 사용하여 최소 비용 경로를 빠르게 계산한다.
- 우선순위 큐를 이용해 현재까지 계산된 최단 경로에서 가장 짧은 경로를 선택하고, 다른 노드들과의 경로를 갱신해 나가는 방식.

### 실시간 작업 스케줄링
- 운영체제(OS)에서는 힙을 사용하여 작업 스케줄링을 관리합니다.
- 각 작업의 우선순위에 따라 작업을 처리해야 할 때 우선순위 큐로 구현된 힙이 효율적으로 스케줄링을 할 수 있다.

### 이벤트 시뮬레이션
- 이벤트가 발생하는 순서대로 처리해야 하는 시뮬레이션 프로그램에서, 힙을 사용해 시간 우선순위에 따른 이벤트 처리를 할 수 있다.


## 우선순위 큐 (Priority Queue) 개념

![image](https://github.com/user-attachments/assets/b1356efa-aaa7-41e0-9cec-0d2f4023481c)


- Priority Queue(우선순위 큐)는 큐(Queue)의 일종이지만, 일반적인 큐와는 다르게 우선순위에 따라 요소가 처리되는 자료구조.
- 일반적인 큐는 FIFO(First In, First Out) 구조로, 먼저 들어온 데이터가 먼저 처리되지만 우선순위 큐는 우선순위가 높은 데이터가 먼저 처리된다.
- 즉, 먼저 들어온 데이터가 아니라, 가장 중요한 데이터가 먼저 처리되는 구조

### 우선순위 큐(Priority Queue) 주요 특징
- 우선순위 기준: 각 요소가 우선순위(priority)를 가지고 있으며, 큐는 이를 기준으로 요소를 정렬.
    - 최소 우선순위 큐(Min Priority Queue): 우선순위가 가장 낮은 요소가 먼저 처리. (기본적으로 Min Heap 기반)
    - 최대 우선순위 큐(Max Priority Queue): 우선순위가 가장 높은 요소가 먼저 처리. (기본적으로 Max Heap 기반)
- 힙 기반 구현: Priority Queue는 일반적으로 힙(Heap)을 기반으로 구현된다.
    - Min Heap 또는 Max Heap 구조를 사용하여 삽입과 삭제 연산을 O(log n)의 시간 복잡도로 처리할 수 있다.

### 우선순위 큐(Priority Queue) 동작 방식
- 삽입(Insertion): 새로운 요소는 우선순위에 따라 힙의 규칙을 유지하면서 삽입된다. 예를 들어, Min Heap 기반 우선순위 큐라면, 새로운 요소는 부모보다 작으면 부모와 자리를 바꾸는 방식으로 적절한 위치에 삽입된다.
- 삭제(Deletion): 가장 우선순위가 높은 (또는 낮은) 요소가 제거된다. 이는 힙의 루트에 해당하는 요소가 제거되고, 마지막 요소가 루트로 올라가면서 힙 규칙에 따라 다시 정렬됨.
- 최댓값/최솟값 반환: Priority Queue는 언제나 우선순위가 가장 높은 (혹은 낮은) 요소를 빠르게 찾을 수 있다. 루트 노드가 항상 우선순위가 가장 높은 요소를 가지기 때문에, 바로 O(1) 시간에 최댓값 또는 최솟값을 반환할 수 있다.

### 우선순위 큐(Priority Queue) 구현 방식
- 우선순위 큐는 여러 가지 방식으로 구현할 수 있으며, 각 방식은 삽입과 삭제의 효율성에 차이가 있다. 
- 배열을 이용한 구현: 배열을 정렬된 상태로 유지하며, 우선순위에 따라 삽입 및 삭제를 진행한다.
    - 단점: 삽입 시 배열을 재정렬해야 하므로 O(n)의 시간 복잡도가 발생할 수 있다.
- 연결 리스트를 이용한 구현: 우선순위 순서대로 정렬된 연결 리스트를 유지한다.
    - 단점: 삽입이나 삭제 시 정렬된 리스트를 유지하기 위해 O(n)의 시간이 필요할 수 있다.
- Heap(힙)을 이용한 구현: 가장 일반적인 방식으로, Min Heap 또는 Max Heap을 사용하여 삽입과 삭제를 O(log n) 시간에 처리한다.
    - 장점: 삽입, 삭제, 탐색이 모두 효율적으로 수행된다.


## Heap연산
- 힙에서 요소 삽입 시 동작 방식은 다음과 같다.
    - 1. 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 삽입한다. 가장 하위 레벨의 최대한 왼쪽으로 삽입한다고도 말할 수 있다. 
    - 2. 새로운 노드를 부모 노드들과 비교해 값이 더 작은 경우 위치를 변경한다.
    - 3. 계속 해서 부모 값과 비교해 위치를 변경한다. (가장 작은 값일 경우 루트까지 올라감)
- 이진 힙에서는 항상 1번 인덱스부터 사용한다.

![image](https://github.com/user-attachments/assets/15b31ae9-8c0a-4d92-a9ae-9a1e7e203df0)

```
// 최대 힙 삽입
void insert_max_heap(int x) {
    
    maxHeap[++heapSize] = x; // 힙 크기를 하나 증가하고, 마지막 노드에 x를 넣음
    
    for( int i = heapSize; i > 1; i /= 2) {
        
        // 마지막 노드가 자신의 부모 노드보다 크면 swap
        if(maxHeap[i/2] < maxHeap[i]) {
            swap(i/2, i);
        } else {
            break;
        }
        
    }
}
```
- 부모 노드는 자신의 인덱스 /2이므로, 비교하고 자신이 더 크면 swap하는 방식이다.

### Heap에서 요소 삭제 시 동작 방식
1. 최대 힙에서 최대값은 루트 노드이므로 루트 노드가 삭제된다. (최대 힙에서 삭제 연산은 최대값 요소를 삭제하는 것)
2. 삭제된 루트 노드에는 힙의 마지막 노드를 가져옴
3. 힙을 재구성

![image](https://github.com/user-attachments/assets/d5ff3a37-5682-420f-b1e1-632f5d2e9d53)

```
// 최대 힙 삭제
int delete_max_heap() {
    
    if(heapSize == 0) // 배열이 비어있으면 리턴
        return 0;
    
    int item = maxHeap[1]; 		// 루트 노드의 값을 저장
    maxHeap[1] = maxHeap[heapSize]; 	// 마지막 노드 값을 루트로 이동
    maxHeap[heapSize--] = 0; 		// 힙 크기를 하나 줄이고 마지막 노드 0 초기화
    
    for(int i = 1; i*2 <= heapSize;) {
        
        // 마지막 노드가 왼쪽 노드와 오른쪽 노드보다 크면 끝
        if(maxHeap[i] > maxHeap[i*2] && maxHeap[i] > maxHeap[i*2+1]) {
            break;
        }
        // 왼쪽 노드가 더 큰 경우, swap
        else if (maxHeap[i*2] > maxHeap[i*2+1]) {
            swap(i, i*2);
            i = i*2;
        }
        // 오른쪽 노드가 더 큰 경우, swap
        else {
            swap(i, i*2+1);
            i = i*2+1;
        }
    }
    
    return item;
    
}
```



## Java와 Python에서의 우선순위 큐(Priority Queue) 구현

### Java 
- Java에서 제공하는 PriorityQueue는 최소 힙을 기본으로 구현되어 있다. 
    - 최대 힙을 구현하려면 Comparator를 사용하여 우선순위를 반대로 설정해줘야함.
    - 메서드는 Queue 인터페이스의 메서드들을 활용하면 된다.

![image](https://github.com/user-attachments/assets/7ed38a1d-8cfe-4230-9534-13f8b4e11584)


#### 최소 힙 구현
```
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // 기본적으로 최소 힙으로 작동
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        minHeap.add(40);
        minHeap.add(10);
        minHeap.add(30);
        minHeap.add(7);

        System.out.println("Min Heap Priority Queue:");
        while (!minHeap.isEmpty()) {
            System.out.print(minHeap.poll() + " ");  // 출력: 7 10 30 40
        }
    }
}
```
- PriorityQueue는 기본적으로 최소 힙으로 작동하며, 값이 작은 것이 우선순위를 가진다.

#### 최대 힙 구현
- 최대 힙을 구현하기 위해서는 Comparator를 사용하여 우선순위를 역순으로 설정할 수 있다.
```
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        // 최대 힙으로 작동하도록 Comparator 설정
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

        maxHeap.add(40);
        maxHeap.add(10);
        maxHeap.add(30);
        maxHeap.add(7);

        System.out.println("Max Heap Priority Queue:");
        while (!maxHeap.isEmpty()) {
            System.out.print(maxHeap.poll() + " ");  // 출력: 40 30 10 7
        }
    }
}
```
- Collections.reverseOrder()를 사용하여 최대 힙을 구현할 수 있다. 이렇게 하면 값이 큰 것이 우선순위를 가지게 된다.
    - Comparator.reverseOrder()를 사용해도 된다. (어차피 같은 객체를 반환하기때문)


### Python : heapq와 PriorityQueue를 이용한 구현
- Python에서는 heapq 모듈과 PriorityQueue 클래스를 사용하여 우선순위 큐를 구현할 수 있다. 기본적으로 최소 힙으로 작동하며, 최대 힙을 구현하려면 약간의 트릭이 필요하다.

#### 최소 힙 구현 (heapq 모듈)
```
import heapq

# 기본적으로 최소 힙으로 작동
min_heap = []
heapq.heappush(min_heap, 40)
heapq.heappush(min_heap, 10)
heapq.heappush(min_heap, 30)
heapq.heappush(min_heap, 7)

print("Min Heap Priority Queue:")
while min_heap:
    print(heapq.heappop(min_heap), end=' ')  # 출력: 7 10 30 40
```
- heapq.heappush()와 heapq.heappop()을 사용하여 최소 힙 우선순위 큐를 구현할 수 있습니다.

#### 최대 힙 구현 (heapq 모듈)
- Python에서 최대 힙을 구현하려면 값을 음수로 변환한 후 heapq를 사용하고, 값을 추출할 때 다시 양수로 변환함.

```
import heapq

# 최대 힙을 구현하기 위해 음수로 값을 변환
max_heap = []
heapq.heappush(max_heap, -40)
heapq.heappush(max_heap, -10)
heapq.heappush(max_heap, -30)
heapq.heappush(max_heap, -7)

print("Max Heap Priority Queue:")
while max_heap:
    print(-heapq.heappop(max_heap), end=' ')  # 출력: 40 30 10 7

```
- 음수를 사용하여 우선순위를 반대로 설정하고, 값을 추출할 때 다시 양수로 변환한다.

#### PriorityQueue 클래스 사용
- queue.PriorityQueue 클래스는 스레드 안전한 방식으로 동작하지만, 기본적으로 최소 힙으로 작동한다.

```
from queue import PriorityQueue

pq = PriorityQueue()
pq.put(40)
pq.put(10)
pq.put(30)
pq.put(7)

print("Min Priority Queue (with PriorityQueue):")
while not pq.empty():
    print(pq.get(), end=' ')  # 출력: 7 10 30 40
```
- PriorityQueue는 기본적으로 최소 힙으로 작동하며, get() 메서드를 통해 가장 작은 값을 추출한다. 
- 최대 힙을 구현할 때는 마찬가지로 값을 음수로 변환한 후, 값을 추출할 때 다시 양수로 변환

### 이진 힙 VS 이진 탐색 트리(BST)

#### 힙은 상/하 , 이진 탐색 트리는 좌/우 관계
- 힙은 상/하 관계를 보장하며 최소 힙에서는 부모가 항상 자식보다 작다.
- 이진 탐색 트리는 좌/우 관계를 보장한다. BST에서 부모는 왼쪽 자식보다 크며 오른쪽 자식보다 작거나 같아.
- 이 같은 특징으로 인해 BST는 탐색과 삽입 모두 O(log n)에 가능하며, 모든 값이 정렬되어야할 떄 사용한다. 
- 반면 큰 값을 조회하거나(최대 힙) 가장 작은 값을 조회하려면(최소 힙) 이진 힙을 사용해야한다. 이진 힙은 이 작업이 O(1)에 가능하다. 우선 순위와 연관되어 있으며 따라서 이진 힙은 우선순위 큐에 활용된다. 



#### 참고 링크 
https://velog.io/@dankj1991/Tree-Heap-PriorityQueue

https://velog.io/@yanghl98/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Heap%ED%9E%99-%EA%B0%9C%EB%85%90-%EC%A2%85%EB%A5%98-%ED%99%9C%EC%9A%A9-%EC%98%88%EC%8B%9C-%EA%B5%AC%ED%98%84

https://velog.io/@gnwjd309/data-structure-heap