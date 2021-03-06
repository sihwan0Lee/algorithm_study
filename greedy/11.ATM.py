# 백준 11399번 ATM 문제

# 1대 있는 ATM기계에 "N"명이 줄을 서있다.
# 예를들어 5명이 있고, p1 = 3, p2 = 1, p3 = 4, p4 = 3, p5 = 2
# 1,2,3,4,5 순서로 줄을 선다면, 1번 사람은 3분만에 돈을 뽑는다는 소리다.
# 그럼 3번 사람까지 돈을 뽑았을때는 8분이 소요된다.
# 5번사람은 돈을 뽑는데 까지 13분이 걸린 것이다.
# 그래서 각자
# 3, 4, 8, 11, 13 분씩 걸려서 총 39분이 걸렸다고 본다.
# 줄을 2 5 1 4 3 순으로 서면
# 1, (1+2=3), (3+3=6), (6+3=9), (9+4=13) = 32분 이다.이것이 최소다.


# 필요한 시간이 최소가 되게하는 프로그램을 작성하시오
# 사람수는 1<= N <= 1000


# 예제 입력
# 5
# 3 1 4 3 2

# 32


# N,과 pi를 입력 받는다
n = int(input())
times = list(map(int, input().split()))

# 시간의 합의 최솟값만 있으면 되서 그냥 sort
times.sort()
answer = 0
sigma = 0
for i in times:
    sigma += i
    answer += sigma
    # print(answer)  # 계산 과정 확인용

print(answer)
