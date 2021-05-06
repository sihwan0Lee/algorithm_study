# 2019 카카오 인턴 튜플

def solution(s):
    answer = []
    s = s[2:-2]
    print(s)
    s = s.split("},{")
    print(s)
    s.sort(key=len)
    print(s)
    for i in s:
        x = i.split(',')
        for j in x:
            if int(j) not in answer:
                answer.append(int(j))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
