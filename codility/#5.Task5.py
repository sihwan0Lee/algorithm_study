# 배열 A  N개의 다른 정수로 이루어진.
# 범위는 1~N+1
# 정확히 한 원소가 빠져있다

# 없어진 원소를 찾는 것이 목표이다

# 50%
def solution(A):
    li = [0] * (len(A) + 1)
    print(li)
    for i in A:
        li[i-1] = 1
        print(li)
    return li.index(0) + 1


print(solution([2, 3, 1, 5]))


# 요소가 N 개의 정수로 이루어진 배열
# 배열은 range[1.....(N+1)]

# 100%
def solution(A):
    li = []
    for i in range(len(A) + 2):
        li.append(i)

    return abs(sum(A) - sum(li))


# 문제 이해 좀 잘하자
# 쉽게 풀 수 있는데도,..
