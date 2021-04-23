# 자연수 n이 주어진다. n의 다음 큰숫자를 정의한다
# n 보단 커야함
# 2진수로 바꿧을때 1의 갯수가 같다.
# 위의 조건 두개를 만족하는애중에 가장 작은 수.
def solution(n):
    count = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == count:
            return i


print(solution(78))

# bin() 함수를 통해 10진수를 2진수로 바꿀수가 있다.
