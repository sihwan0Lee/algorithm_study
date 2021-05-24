# 비어있지 않은 배열 A 는 N의 정수로 이루어져 있다.
# 어떤 정수 P, (0 < P < N)


def solution(A):
    N = len(A)
    result = []
    for P in range(1, N):
        part_1 = []
        part_2 = []
        for i in range(P):
            part_1.append(A[i])
        for j in range(P, N):
            part_2.append(A[j])

        result.append(abs(sum(part_1) - sum(part_2)))
        print(result)
    return min(result)


#print(solution([3, 1, 2, 4, 3]))


# 0 < P < N 범위의 아무 숫자 P를 통해 배열을 두개로 나눌수있다는 것인듯..?

# A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ....., A[N - 1]


# 이 두파트의 합의 절댓값들을 뺀것을 difference로 한다.
# 그 중 최솟값을 리턴하시오


# 53 %
def solution2(A):
    N = len(A)
    result = []
    for P in range(1, N):
        result.append(abs(sum(A[0:P]) - sum(A[P:N])))
    return min(result)


#print(solution2([3, 1, 2, 4, 3]))

# for loop 마다 sum을 해주는게 시간 초과의 문제 인듯.


def solution3(A):
    N = len(A)
    left_sum = 0
    right_sum = sum(A)
    result = []
    for i in range(N - 1):  # 01234
        left_sum += A[i]
        right_sum -= A[i]

        diff = abs(left_sum - right_sum)
        result.append(diff)
    print(result)


print(solution3([3, 1, 2, 4, 3]))

# 0, 13
# i = 0 , 3, 10  7
# i = 1 , 4, 9   5
# i = 2 , 6, 7   1
# i = 3 , 10, 3  7
# i = 4 , 13, 0  13
