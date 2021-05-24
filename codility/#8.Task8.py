# 내가 이해 한거론
# 리스트가 주어진다
# N은 리스트의 밸류들을 세는 것임
# 근데 N이 5라면 5까지 밖에 셀수가 없어서
# 만약 리스트의 밸류중에 N보다 큰값이 있다면 모든 카운터의 요소가 +1 된다.

# 그런게 아니라 N보다 큰값이 있으면 현재의 카운터스에서 맥시멈 값으로 전부 set되야한다.

# 44%
def solution(N, A):
    counters = [0] * (N + 1)
    print(counters)
    for i in range(len(A)):
        print(i, A[i])
        # A[i] , A의 밸류가 N 보다 크다면 카운터스 전체 +1, 아니면 그 요소만.
        if A[i] > N:
            # 리스트 전체에 +1을 해주고싶은데 시간복잡도 N^2 되는게 거슬린다. 일단 진행함
            for i in range(N + 1):
                counters[i] = max(counters)
        else:
            counters[A[i]] += 1
        print(counters[1:])


#print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
# Correctness 100%
# performance  0%


# 일단 아까 거슬렸던 전체 set에서 또 for 돌려버린게 문제인게 분명함
def solution2(N, A):
    counters = [0] * (N + 1)
    print(counters)
    for i in range(len(A)):
        print(i, A[i])
        # A[i] , A의 밸류가 N 보다 크다면 카운터스 전체 +1, 아니면 그 요소만.
        if A[i] > N:
            counters = [max(counters)] * (N + 1)
        else:
            counters[A[i]] += 1
        print(counters[1:])


print(solution2(5, [3, 4, 4, 6, 1, 4, 4]))
