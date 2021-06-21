
def solution(land):
    point_table = []
    for i in range(1, len(land)):
        for j in range(len(land[i])):
            print(land[i][j])
            print(land[i - 1][:j] + land[i - 1][j + 1:])
            land[i][j] = max(land[i - 1][:j] + land[i - 1]
                             [j + 1:]) + land[i][j]

    return max(land[-1])


print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
