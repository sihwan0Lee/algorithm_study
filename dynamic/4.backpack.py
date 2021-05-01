#  배낭 문제
# 피보나치에 이어 다이나믹 프로그래밍의 대표 적인 문제

def backpack(cargo):
    capacity = 15
    pack = []

    for i in range(len(cargo) + 1):
        pack.append([])
        print(pack)
        for c in range(capacity + 1):
            if i == 0 or c == 0:
                pack[i].append(0)
            elif cargo[i - 1][1] <= c:
                pack[i].append(max(cargo[i - 1][0] + pack[i - 1]
                                   [c - cargo[i - 1][1]], pack[i - 1][c]))
            else:
                pack[i].append(pack[i - 1][c])
    return pack[-1][-1]


print(backpack([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)]))
#(가격, 무게)


# cargo = [(4, 12), (2, 1), (10, 4), (1, 1), (2, 2)] ,     len(cargo) = 5
# for 0 ~ 5
#
