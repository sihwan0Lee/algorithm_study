# 배낭 문제
# 조합 최적화분야의 유명한 문제이다.
# 배낭에 담을 수 있는 무게의 최댓값이 정해져 있고, 각각 짐의 가치와 무게가 있는 짐들을 배낭에 넣을 때 가치의 합이 최대가 되도록
# 가치(돈)이 최대가 될수 있게 담는 방법을 구하는 것이다.
# 짐 쪼개기가 가능한 문제다.

def solution(cargo):
    capacity = 15
    pack = []

    # 단가 계산 역순 정렬
    for c in cargo:
        pack.append((c[0] / c[1], c[0], c[1]))   # 단가, 가격, 무게
    pack.sort(reverse=True)
    print(pack)
    # 단가 순 그리디 계산
    total_value: float = 0
    # total_value = 0
    for p in pack:
        if capacity - p[2] >= 0:
            capacity -= p[2]
            total_value += p[1]
            print(capacity, total_value)
        else:
            fraction = capacity / p[2]
            total_value += p[1] * fraction
            break
    # return total_value
# 이렇게 되면 마지막 7/12 만큼만 else 에서 채워진다.


print(solution([(4, 12), (2, 1), (10, 4), (1, 1), (2, 2), ]))


# 위에서
# total_value: float = 0
# total_value = 0

# 둘의 결과자체는 같다.
