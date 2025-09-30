## Heap 자료구조

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495776831-af8cbf14-bd47-44f5-9e2d-26d3770191ea.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T154030Z&X-Amz-Expires=300&X-Amz-Signature=b4c3fdb0b42990a3b4e625f9404224460e1463366b7b2bb9659fe9e91a4f3016&X-Amz-SignedHeaders=host)

- 완전 이진 트리(Complete Binary Tree)으로 구현되어있으며, 우선 큐(Priority Queue)와 같은 최대값 또는 최소값을 빠르게 찾기 위한 자료구조.
- Heap의 핵심 개념은 각 노드가 부모-자식 간의 우선순위 규칙을 만족한다는 것. 우선 순위의 개념을 큐에 도입한 자료구조다.
- 주로 최소 힙(Min Heap)과 최대 힙(Max Heap)으로 나뉘어 사용된다.
    - 최대 힙(max heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
    - 최소 힙(min heap) : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
- 최솟값이나 최댓값을 찾기 위해 배열을 사용하면 Ο(n)만큼 시간이 걸린다. 하지만 힙을 사용하면 O(logn)만큼 소요되므로, 배열을 사용할 때보다 빠르게 최솟값과 최댓값을 구할 수 있다. 우선순위 큐와 같이 최댓값 또는 최솟값을 빠르게 찾아야하는 알고리즘 등에 활용된다.
- 힙은 다음 조건을 만족하는 자료구조이다.
    - 힙은 최대힙(Max heap)과 최소힙(Min heap)으로 나뉘어진다. 최대힙은 자식 노드보다 부모 노드의 값이 크고, 최소힙은 자식 노드보다 부모 노드의 값이 작다.
    - 노드가 왼쪽부터 채워지는 완전 이진 트리 형태를 가진다.
    - 중복을 허용한다.


## Heap 특징

### 완전 이진트리(Complete Binary Tree)
- 힙은 완전 이진 트리의 구조를 가지며, 마지막 레벨을 제외한 모든 레벨이 꽉 차 있고, 마지막 레벨은 왼쪽에서부터 차례대로 채워진다.

### 우선순위 규칙
- 힙에서는 부모 노드가 자식 노드보다 우선순위가 높다.여기서 우선순위는 대표적으로 두 가지 규칙으로 나뉜다. 
    - 최소 힙(Min Heap): 부모 노드의 값이 자식 노드보다 작거나 같다. 따라서 루트 노드는 항상 최소값을 가진다. (PriorityQueue가 기본적으로 최소 힙으로 동작한다)
    - 최대 힙(Max Heap): 부모 노드의 값이 자식 노드보다 크거나 같다. 따라서 루트 노드는 항상 최대값을 가진다.

### 배열로 구현 가능
- 힙은 완전 이진 트리(Complete Binary Tree)이기 때문에 배열을 이용하여 쉽게 구현할 수 있다. 부모와 자식 노드 간의 관계는 배열의 인덱스를 통해 계산된다.)
    - 부모 인덱스 : i
    - 왼쪽 자식: 2 * i + 1
    - 오른쪽 자식: 2 * i + 2

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495782377-c9ef87aa-8196-434e-b42d-a47989de6c58.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T155256Z&X-Amz-Expires=300&X-Amz-Signature=27072b1e1cf7dfae8dc15e72983fcef3ec9c3195cd054dbdc6924398cc722874&X-Amz-SignedHeaders=host)

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


## Heap에서 요소 삽입 시 동작 방식.
1. 힙에 새로운 요소가 들어오면, 일단 새로운 노드를 힙의 마지막 노드에 삽입한다.
2. 새로운 노드를 부모 노드들과 교환한다.

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495791047-ba22df23-53bd-405a-8471-326934556c00.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T161459Z&X-Amz-Expires=300&X-Amz-Signature=43b4686e0521eda2e65c311ba7fea02d88a17ba2de32ac34a1a79a1d07e28a46&X-Amz-SignedHeaders=host)
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

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495791847-e654557b-19bc-4baa-bd2e-bc551ab6e3c6.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T161639Z&X-Amz-Expires=300&X-Amz-Signature=3c83ff127599eb6855bd40fc37f3434c7384783ceed9b2d50831da71962229ab&X-Amz-SignedHeaders=host)

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
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/495787666-cc97af98-40c8-40bd-b955-dd4aca5b9b66.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T160603Z&X-Amz-Expires=300&X-Amz-Signature=cc872828be0dedd33e344a24c5db75de7447a87802c7dd1ffe22159fb17fee2e&X-Amz-SignedHeaders=host)


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

#### 참고 링크 
https://velog.io/@dankj1991/Tree-Heap-PriorityQueue

https://velog.io/@yanghl98/%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Heap%ED%9E%99-%EA%B0%9C%EB%85%90-%EC%A2%85%EB%A5%98-%ED%99%9C%EC%9A%A9-%EC%98%88%EC%8B%9C-%EA%B5%AC%ED%98%84

https://velog.io/@gnwjd309/data-structure-heap