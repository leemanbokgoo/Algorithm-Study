from typing import List
# 33 ) 전화번호 문자 조합
# 2에서 9까지 숫자가 주어졌을 때 전화 번호로 조합 가능한 모든 문자를 출력하라.
# 예를 들어 입력값이 23이라면 첫번쨰 숫자는 2에서 문자를 고르고, 두번쨰 숫자는 3에서 문자를 골라야한다는 것.
# 즉, 2번 문자 + 3번 문자로 만들수 있는 모든 2글자 조합을 말한다.


# [ 풀이 1 ] 모든 조합 탐색
# 해당 문제는 항상 전체를 탐색해야 하고 가지치기 등으로 최적화 할 수 있는 문제는 아니기 떄문에 어떻게 풀이하든 결과는 비슷하다.
# 모두 조합하는 형태로 전체를 탐색한 후 백트래킹하면서 결과를 조합할 수 있다.
# digits : 입력값. 각 자릿수에 해당하느 키판 배열을 DFS로 탐색하면 결과가 완성된다.
def letterCombinations(digits : str ) -> List[str]:
    # dfs() 함수는 자릿수가 동일할 때까지 재귀 호출을 반복하다 끝까지 탐색하면 결과를 추가하고 리턴한다.
    # 이렇게 모든 경우의 수를 DFS로 탐색하고 백트래킹으로 결괄르 조합하면서 리턴하게 된다.
    # digits : 전화번호 숫자로 이루어진 문자열을 입력받아. 가능한 모든 문자 조합을 담은 문자열 리스트 반환

    # index : 현재 digits 문자열에서 처리해야할 숫자의 인덱스
    # path : 현재까지 만들어진 문자 조합을 저장하는 문자열
    def dfs(index, path):
        # 입력된 숫자의 만큼 문자열을 조합해야함으로
        # 현재까지 만들어진 조합(path)의 길이가 입력된 숫자(digits)의 길이와 같아지면 탐색을 종료.
        # 즉 path 가 ab라면 길이가 len(digits)과 같으니 문자열을 결과에 넣어준다음 해당 재귀를 종료한다.
        if len(path) == len(digits):
            # 완성된 조합(pah)를 최종 결과 리스트(result)에 추가한다.
            result.append(path)
            # 해당 경로의 재귀 호출을 종료하고 이전 단계로 되돌아간다.( 백트래킹 )
            return

        # DFS 탐색 및 재귀 호출 부분
        # 여기서 for문은 입력값 자릿수 단위를 반복하기 위해서 사용된다.
        # 예를 들어 23이 입력값이면 최초의 dfs() 함수 호출 값이 dfs(0,"")이기때문에 index는 0이고 digits[i]의 값은 2다.
        # 그럼 이중 반복문인 j의 값은 2의 value인 abc가 되고, j는 abc값이 번갈아가며 순서대로 호출되는 것.
        # i가 0 일때 재귀호출이 전부 끝나고 첫 함수 호출 시 반복문이 돌아 i = 1이 되면 반복문은 돌아가지만 아무런 값도 return 할 수 없다.
        # i가 1이면 dic[3]이 되어 def가 j의 반복문을 돌며 j는 def값이 번갈아되며 순서대로 호출한다.
        # 이때 재귀 호출이 발생하며 dfs(i+1, path+j)가 되는데 이떄 i는 1임으로 i+1은 2다.
        # 그럼 다음 재귀 호출에서 for i in range(index, len(digits))의 값이 for i in range(2,2)가 되는데 그럼 해당 반복문은 실행 될 수 없다.
        # 그래서 3이 키값인 dic의 value를 다 돌며 재귀 호출을 때려도 실제로 result.append(path) 되는 값은 없다고 할 수 있다.
        # 즉,dfs(2, "d") 호출 내부에서는 더 이상 다음 깊이로의 탐색이 일어나지 않는다. 다음 깊이로 탐색이 일어나려면 for문 안의 재귀 호출을 통해 i + 1 하여 다음 깊이로 넘어가야하는데
        # for i in range(2,2)가 되버려 for문이 동작하지않기때문!
        for i in range(index, len(digits)): # 현재 깊이에서 처리할 '시작' 숫자를 결정하는 루프라고 할 수 있다.
            # digits[i] : 현재 처리중인 숫자 (ex 2)
            # dic[digits[i]] : 해당 숫자에 매핑된 문자열 ( ex digits[i]가 2라면 dic[digits[i]]는 a,b,c 다.
            # ex) i가 2라면 j는 a,b,c가 된다.
            for j in dic[digits[i]]:
                # i + 1 : 다음 깊이의 노드를 탐색하기 위해 인덱스를 1 증가시킨다.(이러면 깊이가 +1 되는 것) 깊이를 더하면, 다시 재귀 호출을 해야함.
                # path + j : 현재까지의 조합 path에 현재 선택한 문자 j(즉, 현재 depth 노드) 를 추가하여 다음 재귀 호출로 넘긴다.
                # 예를 들어 a의 노드의 재귀 호출이 끝나면 다음은 b의 재귀 호출이 시작된다. 여기서 j는 a,b,c 가 되고
                # 다음 깊이의 노드에서 j는 d,e,f가 되는 것이다. 그렇게 깊이가 한단계씩 깊어지는 이유는 i + 1를 해서 depth를 + 1씩 해주기 때문이다.
                dfs(i + 1, path + j)

    if not digits:
        return []

    # 문제에서 주어지는 키판 배열
    dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz" }
    result = []
    dfs(0,"")

    return result


if __name__ == "__main__":
    # 입력  23
    # 출력 ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    input_digits_1 = "23"
    result_1 = letterCombinations(input_digits_1)
    expected_output_1 = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    is_correct = result_1 == expected_output_1

    print(f"입력: {input_digits_1}")
    print(f"출력   : {result_1}")
    print(f"결과가 기대값과 일치하는가? {is_correct}")
