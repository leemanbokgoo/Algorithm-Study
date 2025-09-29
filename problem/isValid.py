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
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False

    return len(stack) == 0


if __name__ == "__main__":

    s = "()[]{}"
    print("출력값 : " + str(isValid(s)))