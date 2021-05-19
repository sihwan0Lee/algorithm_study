# 주식을 사고팔기 가장 좋은 시점

def solution(prices):
    result = 0

    for i in range(len(prices) - 1):
        if prices[i + 1] > prices[i]:
            result += prices[i + 1] - prices[i]
    return result


print(solution([7, 1, 5, 3, 6, 4]))


#1 > 7
# 5 > 1 -> result += 4
# 3 > 5 ->
# 6 > 3 -> result += 3
