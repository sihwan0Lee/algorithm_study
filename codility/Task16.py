

# 50%
def solution(A):
    pairs = []
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] == 0:
                if A[j] == 1:
                    pairs.append((i, j))
    if len(pairs) < 1000000000:
        return len(pairs)
    else:
        return -1
#print(solution([0, 1, 0, 1, 1]))


# 0이 나왔을때 그 뒤에 1의 누적되는 1의 갯수
# 이거도 50%
# O(N ** 2)
def solution2(A):
    count = 0
    for i in range(len(A)):
        if A[i] == 0:
            count += A[i+1:].count(1)
    if count < 1000000000:
        return count
    else:
        return -1


print(solution2([0, 1, 0, 1, 1]))

# 아래의 것과 차이가 무엇이길래 위의 것은 n^2 일지 생각해보자


def solution(A):
    result = 0
    count_zero = 0
    for i in A:
        if i == 1 and count_zero == 0:
            continue
        elif i == 0:
            count_zero += 1
        elif i == 1:
            result += count_zero

    if result > 1000000000:
        return -1
    return result
