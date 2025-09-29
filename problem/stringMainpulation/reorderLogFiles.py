# 로그를 재정렬 해야하는 문제
# 1. 로그의 가장 앞부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.
# 입력 : logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# 출력 : [ "let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6" ]
from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit(): # isdigit() : 숫자 여부인지를 판별해 구분
            digits.append(log) # 숫자로 변환 가능한 로그는 digits
        else:
            letters.append(log) # 그렇지않은 경우에는 문자로그에 출력

    # 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하며 동일한 경우 후순위로 식별자[0]을 지정해 정렬되도록 한 람다표현식.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero"
    ]

    # let1 -> 식별자  art, can -> 로그 | 로그가 문자라면 식별자가 아닌 로그에 해당되는 부분을 기준으로 정렬함.
    # dig1 -> 식별자 8, 1, 5, 1 ->  | 로그가 숫자라면 입력 된 순서대로 정렬( 즉, 8이 더 커도 8이 먼저 들어왔기때문에 우선 정렬)
    print(reorderLogFiles(logs))