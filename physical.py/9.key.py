# 카카오 2020

# 이럼 구현문제를 잘해야 하는데..

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a)  # 행 길이
    m = len(a[0])  # 열 길이
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


print(rotate_a_matrix_by_90_degree([[0, 0, 0], [1, 0, 0], [0, 1, 1]]))


# i = 0, 1, 2
# j = 0, 1, 2

# i = 0
# result[0][3 - 0 - 1] = a[0][0] => result[0][2] = a[0][0]
# result[1][3 - 0 - 1] = a[0][1] => result[1][2] = a[0][1]
# result[2][3 - 0 - 1] = a[0][2] => result[2][2] = a[0][2]

# i = 1
# result[0][3 - 1 - 1] = a[1][0] => result[0][1] = a[1][0]
# result[1][3 - 1 - 1] = a[1][1] => result[1][1] = a[1][1]
# result[2][3 - 1 - 1] = a[1][2] => result[2][1] = a[1][2]

# i = 2
# result[0][3 - 2 - 1] = a[2][0] => result[0][0] = a[2][0]
# result[1][3 - 2 - 1] = a[2][1] => result[1][0] = a[2][1]
# result[2][3 - 2 - 1] = a[2][2] => result[2][0] = a[2][2]

# 원래 행렬에서 행은 그대로이고 열의 값만 바뀌는게
# 90도 회전하면 이번엔 열은 그대로이고 행의 값만 바뀐다는 걸 이용

# 1행은 90도 회전하면 n열로 가게된다.


# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 자물쇠 크기를 기존 3배로 변환 (완전 탐색을 수월하게 하기위해)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4가지 방향에 대해 확인
    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)  # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                # 자물쇠에 열쇠 끼워넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
                if check(new_lock) == True:
                    return True
                # 자물쇠에서 다시 열쇠를 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],
               [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
