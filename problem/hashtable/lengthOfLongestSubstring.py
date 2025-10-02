# 중복 문자 없는 가장 긴 부분 문자열
# 중복 문자가 없는 가장 긴 부분 문자열(subString)의 길이를 리턴하라.

# [ 풀이 1 ] 슬라이딩 윈도우와 투 포인터로 사이즈 조절
# 슬라이딩 윈도우로 한칸씩 우측으로 이동하면서 윈도우내 모든 문자가 중복이 없도록 투 포인터로 윈도우 사이즈를 조절하면서 풀이.
def lengthOfLongestSubstring(s: str) -> int:

    used = {} # 문자(key)와 그 문자가 마지막으로 나타난 인덱스(value)를 저장
    max_length = 0
    # start : 왼쪽 포인터, 윈도우의 시작 인덱스
    start = 0
    # index : 오른쪽 포인터, 윈도우의 끝 인덱스
    for index, char in enumerate(s):
        # if char in used : 현재 문자 char가 이전에 등장했었는지 확인, 이미 char이 이전에 등장했다면
        # start <= used[char] : 이전에 등장한 인덱스(used[char])가 현재 윈도우 범위 내에 있는 지 검사. 윈도우 바깥에 있는 문자는 예전에 등장한 적이 있더라도 해당 계산에서는 무시해야함.
        # 밑의 if문을 통과하면 현재 윈도우 s[start : index] 안에 char와 같은 문자가 이미 있다는 뜻.
        if char in used and start <= used[char]:
            # 중복을 해결하고 새로운 중복 없는 윈도우를 시작하기위해, 윈도우의 시작점(start)를 중복된 문자가 마지막으로 등장한 위치(used[char]) 다음으로 옮긴다.(+1)
            start = used[char] + 1
        # 중복이 없거나 윈도우 밖에 있는 경우
        # 현재 윈도우(s[start:index+1])에 중복된 문자가 없다는 뜻.
        else:
            # 윈도우의 길이를 계산하고(index - start + 1) 기존의 max_length와 비교하여 더 큰 값으로 갱신
            max_length = max(max_length, index - start + 1)

        # 해당 문자열의 index 값을 저장
        # 이로 인해 해당 문자가 문자열에서 가장 마지막에 등장한 위치(인덱스)를 계속 갱신한다.
        used[char] = index

    return max_length

if __name__ == "__main__":
    # 입력값
    s1 = "abcabcbb" # 정답은 abc 출력값 3
    s2 = "bbbbb" # 정답은 b, 출력값 1
    s3 = "pwwkew" # 정답은 wke, 출력값 3  pwke는 서브 시퀀스로 연속적이지않은 문자열이다. 정답은 반드시 부분 문자열이다.

    print(f" 출력값: {lengthOfLongestSubstring(s1)}")
    print(f" 출력값: {lengthOfLongestSubstring(s2)}")
    print(f" 출력값: {lengthOfLongestSubstring(s3)}")
