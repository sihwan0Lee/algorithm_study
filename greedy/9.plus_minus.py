def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        for j in range(len(signs)):
            if i == j:
                if signs[j] == True:
                    result += absolutes[i]
                else:
                    result -= absolutes[i]
    return result


print(solution([4, 7, 12], [True, False, True]))
