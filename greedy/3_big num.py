# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
# 배열의 특정 인덱스에 해당하는 수는 연속해서 K 번을 초과할 순 없다.
# N : 배열 크기,  M : 더해지는 횟수, K : 초과할수 없는 횟수

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째로 큰 수

result = 0

while True:
    for i in range(k):   # k 번 이상 초과 안되므로
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)
