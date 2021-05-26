# 프로그래머스 예상 대진표
# N명이 참가하는 대회
# 각각 N - 1 번과 N 번이 게임을 진행
# 다음 라운드에 진출할 참가자의 번호는 다시 1번부터 N/2번을 차례대로 배정받는다
# 1 vs 2 에서 2가 이겼다면 다음 라운드에서 2/2 라서 1번을 부여받게되고
# 3 vs 4에서 3이 이겼다면 다음 라운드에서 2를 배정받는다 (홀수는 그냥 올려치기하는듯)
# 한명이 남을때 까지한다
# 이때, 처음 라운드에서 A 번을 가진 참가자는 경쟁자로 생각하는 B를 몇번쨰 라운드에서 만날지 궁금해한다
# 게임 참가자수 N, 그리고 참가자 A, B
# 처음 라운드에서 A번을 가진 참가자는 B번 참가자와 몇 번쨰 라운드에서 만나는가
# 이떄 둘은 무조건 이긴다.


# 처음 작성한 game2 와 solution2  런타임 에러가 뜸.
def game2(x):
    count = 0
    result = []
    while x > 1:
        if x % 2 == 0:
            x //= 2
            count += 1
            result.append([x, count])
        else:
            x //= 2
            x += 1
            count += 1
            result.append([x, count])
    return result


def solution2(n, a, b):
    info_a, info_b = game2(a), game2(b)
    for i in range((max(a, b)//2) + 1):
        a0 = info_a[i][0]
        b0 = info_b[i][0]
        a1 = info_a[i][1]
        b1 = info_b[i][1]
        if abs(a0 - b0) == 1 and a1 == b1:
            return(a1 + 1)


#print(solution2(8, 4, 7))


# 수정해본 game1과 solution2
# 재귀를 이용했고, 쓸데없는 코드도 많이 줄였다고 생각함.
# 런타임 에러는 모두 극복했으나, 테스트케이스 28/34
def game(x):
    if x % 2 == 0:  # 짝수
        x //= 2
        return x
    else:
        x //= 2
        x += 1
        return x


def solution(n, a, b):
    info_a, info_b = game(a), game(b)
    count = 0
    for i in range(max(a, b) // 2 + 1):
        a = game(a)
        b = game(b)
        count += 1
        if abs(a - b) == 1:
            return count + 1


#print(solution(8, 4, 7))


# 풀이 3

def solution3(n, a, b):
    cnt = 0
    for i in range(max(a, b) // 2 + 1):
        a = a//2 + a % 2
        b = b//2 + b % 2
        cnt += 1
        print(a, b)
        if abs(a-b) == 1:
            return cnt + 1


print(solution3(8, 4, 7))
