# 프로그래머스
# 약수의 개수와 덧셈

# divmod(a,b)
# divmod(10, 3)
# (3, 1) || type tuple


# 약수의 개수가 짝수면 더하고, 약수의 개수가 홀수면 빼도록 한다.

def divisor(n):
    divisors = []
    if n == 1:
        divisors.append(1)
    for i in range(1, (n//2)+1):
        if n % i == 0:
            divisors.append(i)
            divisors.append(n // i)
    divisors = set(divisors)

    return len(divisors)


def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        # 홀수라면 뺴기
        if divisor(i) % 2 != 0:
            result += (-i)

        # 짝수라면 더하기
        if divisor(i) % 2 == 0:
            result += i
    return result


print(solution(24, 27))
