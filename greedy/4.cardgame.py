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


# until 1
# 숫자 N이 1이 될때까지,
# N에서 1을 빼거나, K로 나눠(단, K로 나눠 떨어질때만)
# 1이 될때가지 수행해야하는 최수 횟수를 구해보자.

n, k = map(int, input().split())
result = 0
while N >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
while n > 1:
    n -= 1
    result += 1

print(result)
