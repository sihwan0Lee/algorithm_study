def solution(arr1, arr2):
    # 구현 하고 싶은 것은 우선 answer은 처음에 arr1 그자체로 두고,
    # arr2의 위치에 맞는 값을 그대로 arr1에 더해버린다.
    answer = []
    # 이제 arr2의 요소를 해당 위치에 맞게 arr1에 더한다.
    print(answer)
    # ARR2 요소체크
    for i in range(len(arr2)):
        for j in range(len(arr2[i])):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    print(arr1)


print(solution([[1, 2], [2, 3]], [[3, 4], [5, 6]]))

# 개선 완료.
