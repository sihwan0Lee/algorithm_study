def solution(A, B):
    C = []
    smallest_p = max(A)
    # min을 계속 갱신시켜야함.
    for i in range(len(A)):
        if A[i] > B[i]:
            C.append(A[i])
            smallest_p = min(B[i], smallest_p)
        elif A[i] < B[i]:
            C.append(B[i])
            smallest_p = min(A[i], smallest_p)
        elif A[i] == B[i]:
            C.append(A[i])
    print(C)
    # [1,3] [1,3] 이나 [2,3],[2,3] 인 경우 2와 1이 나와줘야됌.
    if C == A and C == B:
        print(1)
        smallest_in_c = 1
        for j in range(len(A)):
            if smallest_in_c == A[j]:
                smallest_in_c += 1
                if smallest_in_c == A[len(A)-1]:
                    return smallest_in_c + 1

            else:
                return smallest_in_c
    else:
        return smallest_p


#print(solution([1, 2, 4, 3], [1, 3, 2, 3]))
print(solution([1, 2], [1, 2]))
