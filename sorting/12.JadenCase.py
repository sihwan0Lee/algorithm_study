# 프로그래머스 JadenCase 문자열 만들기


def solution(s):
    s = s.split(" ")
    for i in range(len(s)):
        print(s[i])
        s[i] = s[i][:1].upper() + s[i][1:].lower()
        print(s[i])
    # return ' '.join(s)


print(solution("3people unFollowed me"))
