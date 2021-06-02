# triplet (P, Q, R) 의 결과물은
# A[P] * A[Q] * A[R] (0 <= P < Q < R < N)
# 최대값 triplet 을 리턴해보자
# 나는 (2,4,5)를 리턴하는건줄알았는데 그냥 최대 값만 리턴시키면됌.
def solution(A):
    A.sort()
    answer = max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
    return answer


print(solution([-5, 5, -5, 4]))

# 마이너스들이 들어간 거도 생각해야지
