## 이진 탐색 트리 (Binary Search Tree)
- 이진 트리의 일정으로 특정 노드 값에 대해 왼쪽 서브 트리 노드들의 값은 부모 노드의 값보다 항상 작고 오른쪽 서브 트리 노드들의 값은 부모 노드의 값보다 항상 크게 배치 된 트리이다.
- 즉, 어떤 값을 찾을 때, 탐색하는 노드 대상으로 대소 비교를 한 뒤, 크면 오른쪽만, 작으면 왼쪽만 탐색하면 된다. 따라서 탐색 과정의 시간 복잡도는 일반적인 경우 O(log n)이다.

### 이진 탐색 트리 특징
- 이진 탐색 트리의 최소값은 트리의 가장 왼쪽에 있다.
- 이진 탐색 트리의 최대값은 트리의 가장 오른쪽에 있다.
- 각 노드의 왼쪽 서브트리에는 해당 노드의 값보다 작은 값을 지닌 노드들로 이루어져 있다.
- 각 노드의 오른쪽 서브트리에는 해당 노드의 값보다 큰 값을 지닌 노드들로 이루어져 있다.
- 중복된 노드가 없어야 한다.
- 왼쪽 서브트리, 오른쪽 서브트리 또한 이진탐색트리이다.


#### 운이 나쁜 경우 
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501602428-2738bd39-416c-4420-bc80-31177d1a7588.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T160432Z&X-Amz-Expires=300&X-Amz-Signature=962805cb1c796dd66332158b7408ec5201c53b340d71bf398bcd2fcd19f63200&X-Amz-SignedHeaders=host)
- 이진 탐색 트리에 1 ~ 100을 차례대로 넣으면 사향 이진트리를 만들면서 탐색 시 최대 O(n)의 시간이 소요될 수 있다.

#### 일반적인 경우 
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501602776-58e7e0a5-5229-4b4e-8e7e-49af6f3fab75.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T160559Z&X-Amz-Expires=300&X-Amz-Signature=0e5ffbf5cdc222de25086eb2b0c4cb427586181cbe9f0e3e49760d868c63323c&X-Amz-SignedHeaders=host)
- 이진트리의 균형이 적절하다면 이분 탐색과 다를 바가 없으므로 시간복잡도는 O(log n)이다.

### 이진 탐색 트리의 장점
- 삽입/삭제가 유연하다. ⇒ 레퍼런스만 재조정하면 된다.
- 값의 크기에 따라서 좌우로 서브트리가 나눠지기 때문에 삽입/삭제/검색이 일반적으로 빠르다.
    - 여기서 일반적이라는 말은 변질 이진 트리처럼 너무 치우치지 않는 경우를 말한다.
- 값을 순서대로 순회할 수 있다.

### 이진 탐색 트리의 단점
- 트리가 구조적으로 한쪽으로 편향되면 모든 동작의 수행 시간이 악화된다.
    - 이진 탐색 트리가 변질 이진 트리에 가까운 모양으로 (한쪽으로 치우쳐) 생긴 경우에, 삽입/삭제/탐색에 O(n)의 시간 복잡도를 가진다. ⇒ 오래 걸린다.
-  트리가 편향된 경우에 발생하는 문제를 해결하기 위해서, 스스로 균형을 잡는 이진 탐색 트리가 사용된다.
    - 높이 균형을 맞춰주는 자가 균형 이진 탐색 트리의 대표적인 예 : AVL 트리, Red-Black 트리 (worst case에도 삽입/삭제/탐색의 시간복잡도가 O(logN)다.)
    - 특히 레드-블랙 트리는 높은 효율적인 저장 구조를 위해 해시 테이블의 개별 체이닝 시 연결 리스트와 함께 레드-블랙 트리를 병행해 저장하는 구조로 구현 되어 있다. 


## 이진 탐색 트리의 순회 방법
- 이진 탐색 트리에서의 순회방법은 다양하다. 그 중 자주 사용되는 3가지 대표적인 순회 방법이 존재한다.

### 중위 순회

![alt text](image-1.png)

- 왼쪽 서브트리-노드-오른쪽 서브트리 순으로 순회. 이진 탐색 트리 내 있는 모든 값들을 정렬된 순서대로 읽을 수 있다. 
- ex ) 1,3,5,7,8,10


## 이진 탐색 트리의 연산

#### BST 선언 
```
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
 
class BinarySearchTree:
    def __init__(self, val):
        self.root = TreeNode(val)

```

### 탐색
- 탐색은 아래의 과정에서 탐색에 성공할 때까지 계속해서 반복한다.
    - 탐색하려는 값이 루트 노드의 키 값과 같으면 탐색에 성공한다.
    - 탐색하려는 값이 루트 노드의 키 값보다 작으면 왼쪽 서브트리를 탐색한다.
    - 탐색하려는 값이 루트 노드의 키 값보다 크면 오른쪽 서브트리를 탐색한다.
    - 이 과정에서 데이터를 발견하지 못하면 탐색에 실패한다.
- 최악의 경우 시간 복잡도는 O(h) 인데, 여기서 h는 트리의 높이를 말한다. 여기서 최악의 경우는, 이진 탐색 트리가 변질 이진 트리에 가까운 모양을 한 경우이다.
- 트리의 모양이 균형 이진 트리 쪽에 가까울 수록 트리가 균형잡혔다고 하는데, 이 경우 h가 log(n) (n은 노드의 개수)에 가까워진다.
    - 트리가 균형 잡힌 경우 ⇒ 탐색 시간 복잡도는 O(log n)
    - 트리가 한쪽으로 치우쳐져 있을 경우 ⇒ 최악의 경우에 탐색 시간 복잡도는 O(n)

(![alt text](image.png))

- 위의 BST에서 7을 찾는다고 가정한다. 5 < 7 이므로 왼쪽 서브 트리는 탐색 할 필요가 없다. 다음 단계에서 7 < 8 이므로 우측 서브 트리를 탐색할 필요가 없다. 6 < 7 이므로 우측 탐색을 진행하면 원하는 값을 찾을 수 있다. 
- 위의 트리 처럼 전체 크기가 8인 트리에서 총 3번 만에 값을 찾을 수 있음으로 log 시간 내로 결과를 찾을 수 있다. 
- 즉, 최악의 경우라도 마지막 리프 노드까지 탐색하기 때문에 트리의 높이가 h
라 하면 탐색의 시간복잡도는 O(h) 이라 표현할 수도 있다. 만약 마지막 리프 노드까지 진행했음에도 찾을 수 없으면 False를 반환하고 종료하면 된다.

```

   def find(self, val):
        if self.find_node(self.root, val):
            return True # 노드를 반환 받으면 True
        else:
            return False # 없으면 False
 
    def _find_node(self, cur, val):
        if not cur:
            return False # 마지막 리프노드까지 탐색해도 없으니 False
        if cur.val == val:
            return cur # 값을 발견하면 노드 반환
        if cur.val > val: # 커서의 값이 더 크면 좌측 탐색
            return self.find_node(cur.left, val)
        if cur.val < val: # 커서의 값이 더 작으면 우측 탐색
            return self._find_node(cur.right, val)
```

### BST 삽입
- 먼저 삽입하려는 데이터를 탐색해야 한다. 데이터가 이미 존재한다면 삽입할 수 없기 때문에, 탐색을 하다가 실패해 NULL을 반환받은 그 위치에 데이터를 삽입한다.
- 오래 걸리는 작업은 데이터를 탐색이기 하기 때문에, 탐색과 동일한 시간 복잡도를 가진다.
- 이진 탐색 트리에서 데이터를 삽입할때 중복은 허용하지않으며 새 키는 항상 리프 노드에 삽입된다. 삽입 과정은 다음과 같다. 
    - 1. root에서 탐색 시작.
    - 2. 삽입 값을 루트와 비교. 루트보다 작으면 왼쪽으로 재귀, 크다면 오른쪽으로 재귀 
    - 3. 리프 노드에 도달한 후 리프 노드보다 크다면 오른쪽에 작다면 왼쪽에 삽입한다. 

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501610993-3306aa38-3cfb-49c1-80ea-ec09833f7c34.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T162440Z&X-Amz-Expires=300&X-Amz-Signature=747e81058ac5a44d360691b57b844060e0bb4a8925629d82eaa21295cf8a45b3&X-Amz-SignedHeaders=host)

- 아래의 트리에서 3을 삽입하고자 가정해보면 2, 5 사이에 3을 삽입해도 해당 노드끼리는 BST의 성질에 위배되지 않을 수 있겠지만 밑의 서브트리에 대해서는 BST의 속성을 만족하지 못할 수 있다. 
- 따라서, BST에서의 삽입은 리프 노드에서 이루어져야 한다. 그러므로 BST의 가장 왼쪽의 리프노드는 트리 내 값들 중 최소값이고 오른쪽의 리프 노드는 트리 내 값들 중 최대값이다. 결국 리프 노드 끝까지 **탐색**해야 하므로 시간복잡도는 탐색과 동일하게 트리의 높이가 h라 할 때 O(h)가 된다.


### BST 삭제 
- 리프 노드 끝에서만 변경이 발생하는 삽입과 달리 삭제는 고려할 점이 더 있다. 특정 값을 삭제하면 다른 노드들과의 대소관계를 유지해야 하는데 단순히 삭제해버리면 곤란한 경우가 있다.

#### 리프 노드를 삭제 할 경우 
![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501618600-e7633d8c-b04f-4c07-bfa2-9520361a90a3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T164348Z&X-Amz-Expires=300&X-Amz-Signature=770efcf1c7eb597b67eb621cc5343f58c43180882d2e8b6ed15e0536608e7edc&X-Amz-SignedHeaders=host)

- 3이나 7을 삭제한다고 하면 단순히 삭제해도 전체 트리에 영향을 미치지 않는다.

#### 자식 노드가 1개인 경우 

![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501618417-3dbc4c6a-5dfa-4b22-ab02-66e5722d0d49.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T164321Z&X-Amz-Expires=300&X-Amz-Signature=71d57f06f1efd5a909bb1bdfcf3c031ff7a965830d2521b43c903a512bc64360&X-Amz-SignedHeaders=host)

- 4나 6을 삭제한다고 하자. 아래에 자식 노드로 각각 3, 7을 갖고 있는데 각각에 대해 삭제하고자 하는 노드의 부모 노드에 대해 대소 관계가 유지된다. 
- 따라서, 노드를 삭제하고 삭제된 노드의 부모노드와 삭제된 노드의 자식 노드를 연결해도 BST의 속성이 유지된다.
- 삭제될 노드를 가리키던 레퍼런스를 삭제될 노드의 자녀 노드를 가리키도록 변경한다.

#### 자식 노드가 2개인 경우
- 삭제될 노드의 오른쪽 서브 트리에서 제일 값이 작은 노드가 삭제될 노드를 대체한다. (왼쪽 서브트리에서 제일 값이 큰 값이여도 된다.) 
- 삭제를 하고 나서도, 여전히 이진 탐색 트리의 특징이 유지될 수 있도록 레퍼런스를 조정하는 과정이 필요하다.
- 삭제 작업 역시 데이터 탐색을 동반하기 때문에 탐색과 동일한 시간 복잡도를 가진다


![image](https://github-production-user-asset-6210df.s3.amazonaws.com/123913164/501616649-4bdf84a9-af77-481d-b9d7-b4c121782613.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20251015%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20251015T163828Z&X-Amz-Expires=300&X-Amz-Signature=0ee30e1f2c40a9034e05a7b5d247dfe74608b8658234ecb25658835af70f0196&X-Amz-SignedHeaders=host)


- 위 트리에서 16을 삭제해야 한다고 가정한다. 그런데 기존처럼 16을 무작정 지우게 되면 13의 위치가 애매해진다. 계산복잡성을 줄이기 위해서는 트리의 요소값들을 크게 바꾸지 않고 원하는 값(16)만 삭제할 수록 좋기때문에 최대한 변경 없는 방법을 고려해야한다. 
- 16을 삭제 하기 전 위의 트리의 각 요소를 중위 순회 방식(왼쪽 서브트리 - 노드 - 오른쪽 서브티리 순으로 순회)으로 읽으면 다음과 같다.
    - 4, 10, 13, 16, 20, 22, 25, 28, 30, 42

- 위의 배열은 이진 탐색 트리 속성을 만족하고 있다. 16의 왼쪽 서브 트리에 속한 값은 16보다 작고, 오른쪽 서브 트리에 속한 모든 값은 16보다 크다. 
    - 특히 13을 predecessor(삭제 대상 노드의 왼쪽 서브트리 가운데 최대값)
    - 20을 successor(삭제 대상 노드의 오른쪽 서브트리 가운데 최소값)라고 한다.

- 따라서 아래와 같이 삭제할 노드인 16 위치에 20을 복사해 놓고, 기존 20 위치에 있던 노드를 삭제하게 되면 정렬된 순서를 유지(=이진탐색트리 속성을 만족)하면서도 원하는 결과를 얻을 수 있게 된다. (16 위치에 predecessor인 13을 놓고, 기존 13 위치에 있던 노드를 삭제해도 원하는 결과를 얻을 수 있다.)
    - 4, 10, 13, ~~16~~~  20,  ~~20~~, 22, 25, 28, 30, 42

- 이진 탐색 트리 구조상 successor(삭제 대상 노드의 오른쪽 서브트리 가운데 최소값)는 자식 노드가 하나이거나, 하나도 존재하지않는다. 각각 살펴보면 다음과 같다. 
    - successor의 자식노드가 하나인 케이스 : 위 예시 그림과 같다. 삭제 대상 노드의 오른쪽 서브트리가 30을 루트노드로 하는 트리일 때, 이 트리의 맨 왼쪽 노드인 20은 하나의 자식노드(25)를 갖는다.
    - successor의 자식노드가 존재하지 않는 케이스 : 삭제 대상 노드의 오른쪽 서브트리가 오른쪽 자식 노드가 없는 경우에는 successor는 왼쪽 자식노드를 가지지 않는다. successor는 오른쪽 서브 트리에서 가장 작은 값임으로 만약 successor이 왼쪽 자식을 가진다면 왼쪽 자식의 값은 successor의 보다 작아야한다. 하지만 successor은 이미 오른쪽 서브 트리에서 가장 작은 노드였으므로 successor 보다 작은 왼쪽 자식 노드가 존재할 수 없다. successor가 가장 작다는 정의에 모순되기때문이다. 고로 successor은 왼쪽 자식 노드를 가질 수 없다. 

- 마찬가지로 왼쪽 서브트리의 맨 오른쪽 노드인 predecessor 또한 자식노드가 하나이거나, 하나도 존재하지 않는다. 따라서 자식노드가 두 개인 경우(case 3)에는 다음과 같이 삽입 연산을 수행하면 된다.(successor 기준).
    - 1. 삭제 대상 노드의 오른쪽 서브트리를 찾는다.
    - 2. successor(1에서 찾은 서브트리의 최소값) 노드를 찾는다.
    - 3. 2에서 찾은 successor의 값을 삭제 대상 노드에 복사한다.
    - 4. successor 노드를 삭제한다.
- 4번 successor 노드를 삭제하는 과정은 case 1나 case2에 해당한다. successor는 자식노드가 하나이거나, 하나도 존재하지 않기 때문이다.

- Big-O notation으로는 최악의 케이스를 고려해야 하므로 가장 연산량이 많은 case 3(삭제 대상 노드의 자식노드가 두 개인 경우)이 계산 복잡성의 분석 대상이 된다.
    - 트리의 높이가 ℎ이고 삭제대상 노드의 레벨이 𝑑
라고 가정할때, 1번 과정에서는 𝑑
번의 비교 연산이 필요하다. 2번 successor 노드를 찾기 위해서는 삭제 대상 노드의 서브트리 높이(ℎ−𝑑
)에 해당하는 비교 연산을 수행해야 한다. 3번 4번은 복사하고 삭제하는 과정으로 상수시간이 걸려 무시할 만 하다. 종합적으로 따지면 𝑂(𝑑+ℎ−𝑑), 즉 𝑂(ℎ)가 된다.



#### 참고 링크 

https://ratsgo.github.io/data%20structure&algorithm/2017/10/22/bst/

https://8iggy.tistory.com/110

https://engineerinsight.tistory.com/321#google_vignette

https://yoongrammer.tistory.com/71