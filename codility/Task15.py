# N개의 정수들로 이루어진 비어있지 않은 배열 A이 주어진다
# 정수들의 짝 (P, Q) 0 <= P < Q < N
# 저 짝들을 배열 A의 슬라이스라고 부른다(스라이스에는 최소 두개의 요소는 들어가 있어야한다.)
# 슬라이스(P, Q)의 평균은
# A[P] + A[P + 1] + ..... + A[Q] 의 합을 슬라이스의 길이로 나눈 것이다.
# 정확하게 되기 위해, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1)
# 목표는 평균의 최소의 짝의 시작점을 구하는 것이다.
# 예시였으면 (2 + 2) / 2 가 최소 평균 2였으므로 그때의 시작점 P의 인덱스는 1 이다. 1이 리턴되면 된다.
# If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# Task Score : 50%
# Correctness : 100%
# Detected time complexity : O(N ** 3)
def solution(A):
    # pair을 구하자
    pairs = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            sum = 0
            avg = 0
            for k in range(i, j+1):
                sum += A[k]
            avg = sum / (j-i+1)
            pairs.append([i, j, avg])
    # print(pairs)
    avgs = []
    for pair in pairs:
        avgs.append(pair[2])
    # print(avgs)
    # print(avgs.index(min(avgs)))
    return pairs[avgs.index(min(avgs))][0]

#print(solution([4, 2, 2, 5, 1, 5, 8]))


# 정확도는 다 맞았는데 for을 3번이나 돌린게 문제였다.
def solution2(A):
    # pair을 구하자
    pairs = []
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            pairs.append([i, j])
    print(pairs)

    avgs = []
    for m in range(len(pairs)):
        avg = 0
        sum = 0
        for l in range(pairs[m][0], pairs[m][1] + 1):
            sum += A[l]

        avg = sum / (pairs[m][1]-pairs[m][0]+1)
        avgs.append(avg)
    print(avgs)
    return pairs[avgs.index(min(avgs))][0]


print(solution2([4, 2, 2, 5, 1, 5, 8]))
