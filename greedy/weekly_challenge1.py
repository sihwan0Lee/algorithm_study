def solution(price, money, count):
    answer = abs(money - (price * (count * (count+1)//2)))
    if answer == 0:
        return 0
    else:
        return answer


print(solution(3, 20, 4))
