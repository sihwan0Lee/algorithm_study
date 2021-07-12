def solution(arr):
    arr.sort()
    answer = 1
    for i in range(arr[-1], 0, -1):
        count = 0
        new = []
        for j in range(len(arr)):
            if arr[j] % i == 0:
                count += 1
                new.append(arr[j] // i)
        if count == len(arr):
            print(i)
            answer *= i
            arr = new
        else:
            new = arr

    for h in new:
        answer *= h
    return answer


print(solution([3, 6, 9, 2, 4, 8]))
print(solution([6, 3, 2, 7]))
print(solution([2, 6, 8, 14]))
print(solution([4, 8, 12, 16]))
print(solution([3, 6, 9, 12]))
print(solution([4, 6, 8, 10]))


# 테스트 케이스 4개는 성공하지만 예외에서 탈락

