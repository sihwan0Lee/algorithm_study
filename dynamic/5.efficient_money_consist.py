# N가지 종류의 화폐가 있다. 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 이 때 각 화폐는 몇 개라도 사용가능하다. 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 취급한다.
# 첫째줄에 N,M이 주어지고 N개의 줄에는 각 화폐의 가치가 주어지고 , M은 가치의 합이 되도록 하는 수이다.

# 적은 금액부터 큰 금액까지 확인하며 차례대로 만들수있는 최소한의 화폐 개수를 찾아보자

# 몇개를 쓰든 개수를 최소한으로 해서 M원을 만들어보자.

# 정수 n, m을 입력받음 n이 화폐 종류 갯수고, m이 만들어야 될 숫자
n, m = map(int, input().split())
# n개의 화폐단위 정보 입력받기
array = []
for i in range(n):
    array.append(int(input()))

# 한번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])


