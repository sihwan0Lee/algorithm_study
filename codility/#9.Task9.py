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
