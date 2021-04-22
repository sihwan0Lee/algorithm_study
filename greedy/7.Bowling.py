# 무게 마다 볼링공이 몇 개 있는지를 계산해야 한다.
# ex:
# 1kg : 1개, 2kg : 2개, 3kg : 2개
# 1kg짜릴 고르면 나머지 경우의 수는 4가지. (1 * 4)
# 2kg를 골랐을땐  4가지  (2 * 2)
# 3kg를 골랐을땐 앞서 소모다했으므로 0
# 총 8
n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1 부터 m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i]  # 무게가 i인 볼링공의 개수(A가 선택하는 개수) 제외
    result += array[i] * n   # B가 선택하는 경우와 곱하기

print(result)

# 5 3
# 1 3 2 3 2
# 8
