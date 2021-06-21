# 다이나믹 프로그래밍
# 키워드 : 중복되는 연산을 줄이자

# 피보나치 수열
# 피보나치 수열은 다음 항의 값이 이전의 두개 의 항의 값의 합으로 이루어진 수열이다.

# 0, 1, 1, 2, (1+2=3), (2+3=5), (3+5=8)....

# 기본적으로 피보나치를 프로그래밍해보자


def fibo1(n):
    if n == 1 or n == 2:
        return 1
    return fibo1(n-1) + fibo1(n-2)


# print(fibo1(10))

# 프로그래머스에도 피보나치문제가 있어서 이를통해 채점을 해보면
# 절반의 테스트에서 런타임 에러와 시간 초과가 발생한다.

# 그 이유는 f(n) 함수에서 n이 커질수록 수행 시간이 기하급수적으로 늘어나기 떄문이다.
# 시간복잡도는 O(2^N)이다. N이 30 이라면 약 10억가량의 연산을 수행해야한다.
# 구조를 살펴보면
# f(6)의 값을 알려면
# f(6) = f(5) + f(4)
# ( f(5) = f(3) + f(4) ) + ( f(4) = f(2) + f(3) )
# (f(4) = f(2) + f(3)) + ( f(3) = f(1) + f(2) ) + ( f(3) = f(1) + f(2) ) + ( f(2)  )
# ( f(3) = f(1) + f(2) ) + f(2)

# 동일한 함수가 반복적으로 호출이되고있다. 숫자가 커질수록 반복되는 함수가 엄청나게 많아진다.
# 재귀함수가 매번 좋은 것 만이 아니라는것을 알수있게되었다.

# 다이나믹 프로그래밍을 통해 이제 풀어보기전에 다이나믹 프로그래밍에는 조건이 필요하다
# 1. 큰 문제를 작은 문제로 나눌 수 있어야 한다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# 메모제이션을 이용한 풀이
# 메모제이션 (한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 호출하면 메모한 결과를 그대로 가져오는 기법 . 캐싱이라고도 한다. )
# (단순히 한 번 구한 정보를 리스트에 저장하면 쉽게 구현할 수 있다.)

d = [0] * 100


def fibo2(n):
    #d = [0] * 100
    if n == 1 or n == 2:
        return 1
    if d[n] != 0:
        return d[n]
    d[n] = fibo2(n - 1) + fibo2(n - 2)
    print(d)
    return d[n]


# print(fibo2(50))

# d가 함수 안에 있으면 만약에 d[5] = d[4] + d[3] 매번 [0]*100의 리스트로 재 초기화 되어버린다.
# 해당 코드의 시간복잡도는 O(N) 이다
# 위와 같이 재귀 함수를 이용하여 큰 문제를 해결하기위해 작은 문제를 호출 한다고하여
# 탑다운방식이라고 한다.

# 아래의 코드는 단순히 반복문을 이용하여 소스코드를 작성하여 작은 문제부터 차근차근 답을 도출하는 것을
# 보텀업 방식이라고 한다.
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
   # print(d)


# 탑다운(메모이제이션)방식은 하향식이라고도 하며, 보텀업은 상향식이라고도한다.
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업이다.
# 메모이제이션은 탑다운 방식에서 국한되어 사용되는 표현이다.

# 일반적인 프로그래밍 언어는 CPU에서 제공하는 최소 읽기 단위를 기준으로 변수의 범위를 지정한다
# 일반적인 int자료형은 -2,147,483,648 ~ 2,147,483,647 까지 만을 표현 할수 있다.
# 하지만 파이썬은 자료형의 구분 없이 큰 수를 저장할수있다.

def solution(n):
    d = [0] * (n + 1)
    d[1] = 1
    d[2] = 1
    for i in range(3, n + 1):
        d[i] = (d[i-1] + d[i-2]) % 1234567
    return d[i]


print(solution(100))