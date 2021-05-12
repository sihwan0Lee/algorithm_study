# def solution(A, B):
#    result = 0
#    A.sort()
#    B.sort(reverse=True)
#    for i in range(len(A)):
#        for j in range(len(B)):
#            if i == j:
#               result += (A[i] * B[j])
#    return result

# 효율성 테스트에서 시간 초과가 나버렸다.

def solution(A, B):
    result = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        result += (A[i] * B[i])
    return result


print(solution([1, 4, 2], [5, 4, 4]))
