# 비어 있지 않은 배열 A는 N개의 정수로 구성되어 있다.
# 배열이 홀수를 가지고 있고, 배열의 각 요소는 같은 값을 가진 배열과 짝지어질수있다
# 아 value로 짝 없는 인덱스 찾는거구나


# 시간복잡도가 O(N^2) 라서 효율도 55% 실패
def solution(A):
    board = [0] * len(A)
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            if A[i] == A[j] and board[i] == 0 and board[j] == 0:
                board[i] = 1
                board[j] = 1
    for i in range(len(board)):
        if board[i] == 0:
            return A[i]


#print(solution([9, 3, 9, 3, 9, 7, 9]))


# 엥 이거도 55%..?
def solution2(A):
    for i in A:
        if A.count(i) == 1:
            return i


#print(solution2([9, 3, 9, 3, 9, 7, 9]))


def solution3(A):
    A.sort()
    print(A)
    for i in range(0, len(A), 2):
        print(i)
        if A[i] == A[i + 1]:
            pass
        else:
            return A[i]


#print(solution3([9, 3, 9, 3, 9, 7, 9]))

def solution4(A):
    A.sort()
    count = 1
    for idx in range(0, len(A) - 1):
        if A[idx] == A[idx + 1]:
            count += 1
        else:
            if count % 2 != 0:
                return A[idx]
                count = 1
            return A[len(A) - 1]


#print(solution4([9, 3, 9, 3, 9, 7, 9]))

def solution5(A):
    if len(A) == 1:
        return A[0]

    A.sort()
    for i in range(0, len(A), 2):
        if i+1 == len(A):
            return A[i]
        if A[i] != A[i+1]:
            return A[i]


print(solution5([9, 3, 9, 3, 9, 7, 9]))

# 
