# 여러 개의 숫자 카드중에서 가장 높은 숫자가 쓰인 카드 한장을 뽑는게임
# N x M 형태로 카드가 주어진다. N이 행 M이 열이다.
# 가장 작은 수들 중에서 가장 큰 수 찾기이다 .

n, m = map(int, input().split())

result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

