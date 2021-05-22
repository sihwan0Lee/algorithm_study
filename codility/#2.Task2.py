# 효율성 87%
def solution(A, K):
    for i in range(1, K+1):
        last_list = []
        last = A.pop()
        last_list.append(last)
        A = last_list + A
        last_list = []
    return A


#print(solution([3, 8, 9, 7, 6], 3))
#print(solution([0, 0, 0], 1))


# 효율성 100%
def solution2(A, K):
    if len(A) == 0 or K == 0:
        return A
    for i in range(1, K + 1):
        print([A[-1]], A[0:len(A) - 1])
        A = [A[-1]] + A[0:len(A) - 1]
        print(A)


print(solution2([3, 8, 9, 7, 6], 3))
