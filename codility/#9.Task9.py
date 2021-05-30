# 55%

def solution(A):
    N = len(A)
    A.sort()
    check = [0] * N
    # A에는 포함되지 않은 가장 작은 양의 정수를 리턴하시오
    # 경우의수
    # 리스트안에 있는경우, 리스트 밖인경우, 리스트가 전부 음수인 경우
    start = 1
    for i in range(len(A)):
        if start in A:
            start += 1
            check[i] = 1
    return check.count(1) + 1


print(solution([1, 3, 6, 4, 1, 2]))
print(solution([-1, -3]))
print(solution([1, 2, 3]))

# 길이 N 만큼의 체크 리스트를 만든다음
# 바로 밸류 값으로해서 양의 정수 시작인 1부터해서 밸류 가 있을떄 마다 1씩늘려감
# 애초에 2부터 시작했으면 1에서 걸려서 1리턴될거고
# 전부 마이너스면 애초에 1이 없을거고
# 중간에 값이 하나 부족하다면 반복문도 거기서 멈출거고
# 결국 카운팅된 1에서 +1 씩만해주면 되는거 아닌가.

def solution(A):
    A.sort()
    min = 1
    for i in A:
        if i == min:
            min += 1
    return min