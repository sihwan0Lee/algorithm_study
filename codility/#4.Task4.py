# 개구리가 건너편 길로 가려고 한다.
# 현재 개구리는 포지션 X에 있고, Y와 같거나 더 큰 위치로 이동하려고한다.
# 개구리는 항상 D만큼 움직인다

# 개구리가 타겟까지 가는데 뛰는 최소횟수를 구하자

# x = 10, y = 85, d =30
# 첫 점프, 10 + 30 = 40
# 두번째 점프, (10 + 30) + 30 = 70
# 세번쨰 점프, (10 + 30 + 30) + 30 = 100

def solution(X, Y, D):
    count = 0
    for i in range(1, Y + 1):
        X += D
        count += 1
        if int(X) > int(Y) or int(X) == int(Y):
            break
    return count


print(solution(10, 85, 30))
