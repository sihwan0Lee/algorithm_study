# until 1
# 숫자 N이 1이 될때까지,
# N에서 1을 빼거나, K로 나눠(단, K로 나눠 떨어질때만)
# 1이 될때가지 수행해야하는 최수 횟수를 구해보자.

n, k = map(int, input().split())
result = 0
while n >= k:
    while n % k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1
while n > 1:
    n -= 1
    result += 1

print(result)
