from typing import List
# 61) 가장 큰 수
# 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라

# [ 풀이 1 ] 삽입 정렬
# 각 요소 단위로 크기 순으로 정렬하면 되지만. 맨 앞에서부터 자릿수 단위로 비교해서 크기순으로 비교한다.
# 즉, 9는 30보다 맨 앞자리수가 더 크므로 9가 더 앞에 와야한다. a + b 와 b + a를 비교하는 형태다.
class Solution:
    @staticmethod
    def to_swap(n1 : int, n2 : int) -> bool:
        return str(n1) + str(n2) < str(n2) + str(n1)

    def largestNumber(self, nums: List[int]) -> str:

        # 삽입 정렬은 리스트를 정렬된 부분과 정렬되지 않은 부분으로 나누어 작업한다.
        # 인덱스 0의 원소 (nums[0])는 그 자체로 하나의 원소만 있는 정렬된 부분으로 간주하기때문에 두번쨰 원소인 index 1부터 시작한다.
        i = 1

        while i < len(nums):
            # j를 삽입 대상 위치(i)로 초기화
            j = i

            # 새로운 삽입 대상(j)을 왼쪽으로 이동시키며 비교한다.
            # j > 0 : 현재 위치가 리스트의 시작(인덱스 0)이 아닌지 확인
            # to_swap(nums[j - 1], nums[j]) : 현재 원소(nums[j])와 바로 앞 원소(nums[j-1])를 비교하여 true가 반환된다면
            while j > 0 and self.to_swap(nums[j - 1], nums[j]):
                # 서로의 위치를 맞바꾼다.
                nums[j] , nums[j-1] = nums[j-1], nums[j]

                # j -= 1을 하면, 다음 루프가 실행될 때 j는 새로운 위치(j-1)를 가리키게 된다.
                # 이로써 새로운 위치에 있는 이 원소와 그 앞의 원소(nums[j-2], 즉 nums[j-1]로 바뀐 값)를 다시 비교하게 된다.
                # 이 과정은 원소가 최종적으로 정렬된 위치를 찾을 때까지 (즉, self.to_swap이 거짓이 되거나 j가 0이 될 때까지) 반복된다.
                j -= 1

            # 현재 nums[i]에 대한 삽입 과정이 완료되었으므로, i를 1 증가시켜 다음 정렬 대상 원소로 이동
            i += 1

        # 입력값이 ["0", "0"] 인 경우도 있기때문에 그냥 문자로 처리하면 리턴값이 00이 된다.
        # 따라서 join의 결과를 int로 바꿔서 0이 되도록 만들어준 후 str로 변경해야한다.
        return str(int(''.join(map(str, nums))))

if __name__ == "__main__":
    # 입력값 : [10,2]           출력값 : 210
    # 입력값2 : [3,30,36,5,9]  출력값 : 9534440

    nums = [10,2]
    nums2 = [3,30,36,5,9]
    so = Solution()
    print(so.largestNumber(nums) , "     기대 값 : 210" )
    print(so.largestNumber(nums2) , "     기대 값 : 9534440" )


