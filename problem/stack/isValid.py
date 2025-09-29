# 유효한 괄호
# 괄호로 입력값이 올바른지 판별하라

def isValid( s: str)-> bool:
    stack = []
    table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for char in s:
        # if char not in table : in 연산자는 딕셔너리(table)의 키(Key)에 해당 값이 존재하는지 확인하는 데 사용
        # 즉, '현재 문자 char가 딕셔너리 table의 키 목록에 포함되어 있지 않다면' 이라는 뜻
        if char not in table:
            stack.append(char)

        # 스택이 비었거나 아니면 table의 키값이 stack.pop()한 것 과 짝이 맞는 상황인가.
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0

if __name__ == "__main__":

    s = "()[]{}"
    print("출력값 : " + str(isValid(s)))