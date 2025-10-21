# 69 ) 2D 행렬 검색
# m*n 행렬에서 값을 찾아내는 효율적인 알고리즘을 구현하라. 행렬은 왼쪽에서 오른쪽, 위에서 아래 오름차순으로 정렬 되어있다.

# [ 풀이 1 ] 첫 행의 맨 뒤에서 탐색.
# 열(col)을 기준으로 이진 검색을 수행한 다음, 찾아낸 값을 기준으로 해당 위치의 각 행을 기준으로 다시 이진검색을 수행해서 해결한다.
# 첫 행의 맨 뒤 요소를 택한 다음, 타겟이 이보다 작으면 왼쪽, 크면 아래로 이동하게 하는 방법이다.
# 행렬은 왼쪽에서 오른쪽, 위에서 아래로 오름차순 정렬 되어있기때문에 작으면 왼쪽, 크면 아래로 이동하도록 구현한다.
def searchMatrix(matrix , target):

    # 예외 처리
    if not matrix:
        return False

    row = 0 # 행(가로 줄)
    # 맨 뒤쪽 부터 시작해야하기때문에  len(matrix[0]) - 1하면 맨 끝의 index를 알 수 있다.
    col = len(matrix[0]) - 1 # 열 (세로 줄 )

    # row는 0에서부터 시작함으로  len(matrix) - 1 보다 작거나 같아질때까지
    # col은 맨 뒤에서부터 시작함으로 0보다 크거나 작을때까지 반복
    while row <= len(matrix) - 1 and col >= 0 :

        # target을 찾으면 true 리턴
        if target == matrix[row][col]:
            return True

        # 타겟이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1

        # 타겟이 크면 아래로 이동.
        elif target > matrix[row][col]:
            row +=1

    return False

# [ 풀이 2 ] 파이썬다운 방식
# [ 풀이1 ] 은 한칸씩 왼쪽, 아래쪽으로 움직이며 탐색했지만 [ 풀이 2 ]는 파이썬이 내부적으로 행렬에 값이 존재하는 지 여부를 위에서부터 차례대로 한줄씩 탐색한다.
def searchMatrix2(matrix , target):
    return any(target in row for row in matrix)

if __name__ == "__main__":
    matrix = [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ]
    target = 5
    target2 = 20
    # target값이 5일 경우 5가 존재함으로 true 반환. target값이 20일경우 값이 존재하지않음으로 false반환.

    print("[ 풀이1 ] 첫 행의 맨 뒤에서 탐색 : 기대 출력값 True  " , searchMatrix(matrix, target))
    print("[ 풀이1 ] 첫 행의 맨 뒤에서 탐색 : 기대 출력값 False " , searchMatrix(matrix, target2))
    print("[ 풀이2 ] 파이썬다운 풀이       : 기대 출력값 True  " , searchMatrix2(matrix, target))
    print("[ 풀이2 ] 파이썬다운 풀이       : 기대 출력값 False " , searchMatrix2(matrix, target2))

