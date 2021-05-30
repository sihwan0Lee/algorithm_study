# 프로그래머스 lv2 다음 큰 숫자
# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

# 10진수 각 진수로 변환
# bin(number) : 2진수 변환 함수
# oct(number) : 8진수 변환 함수
# hex(number) : 16진수 변환 함수

# 10진수로 변환
# int("", 해당진법)
# ex
# print(int("1001110", 2))  -> 78
# print(bin(78)) -> 0b1001110

def solution(n):
    for i in range(n + 1, 1000001):
        if bin(n).count('1') == bin(i).count('1'):
            break
    return i


print(solution(15))
