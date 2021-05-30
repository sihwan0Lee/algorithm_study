# 개구리가 또 강을 건너려고한다
# 강한편의 위치 0 에서 위치한 개구리
# 위치 X+1로 가려고한다.
# 낙옆이 강의 표면으로 떨어집니다
# N개의 정수로 이루어진 배열 A를 전달 받을것이다. 이것은 낙옆들을 의미한다.
# A[k] 는 시간 k일때 나뭇잎이 떨어질 위치이다.
# 목표는, 개구리가 강의 다른편에 도착할수있는 최소시간을 구하는 것이다
# x가 5라면 5만큼 다채워져야함 이건 체크리스트 만들어야함


# 54%
def solution(X, A):
    river = [0] * (X)

    # value가 river의 인덱스가 되줘야함.
    for i in range(len(A)):
        leaf = A[i]
        if river[leaf - 1] == 0:
            river[leaf - 1] = 1
        if river.count(1) == X:
            return i
    else:
        return -1


#print(solution(2, [2, 2, 2, 2, 2]))
#print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))

# 100%
def solution2(X, A):
    river = [0] * X
    l = 0
    for i in range(len(A)):
        if river[A[i] - 1] == 0:
            river[A[i] - 1] = 1
            l += 1

            print(A[i], river)
            if l == X:
                return i
    return -1


print(solution2(5, [1, 3, 1, 4, 2, 3, 5, 4]))


# 소감
# 문제이해를 100% 잘하는것이 중요하다/
