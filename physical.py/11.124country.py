# 프로그래머스
# 124 나라의 숫자

# 124 나라에는 자연수만 존재합니다.
# 124 나라에는 모든 수를 표현할 때 1, 2, 4만 사용합니다.

# 10진법    124나라     10진법수를 3으로 나눴을 때
#   1       1           몫 0 나머지 1
#   2       2           몫 0 나머지 2
#   3       4           몫 1 나머지 0
#   4       11          몫 1 나머지 1
#   5       12          몫 1 나머지 2
#   6       14          몫 2 나머지 0
#   7       21          몫 2 나머지 1
#   8       22          몫 2 나머지 2
#   9       24          몫 3 나머지 0
#   10      41          몫 3 나머지 1
#   11      42          몫 3 나머지 2
#   12      44          몫 4 나머지 0

# 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록 solution 함수를 완성해 주세요.

# 나머지가 1, 2 일땐 몫에 따라  124 를 인덱스에 맞게 넣어주고, 나머지가 4일땐 몫에서 -1 한 것의 인덱스로 .
def solution(n):
    # 인덱스 다루기 편하게 앞에 0 넣어서 나머지 1 2 4 가 인덱스 상으로 1 2 3 으로 되게함
    coun124 = [4, 1, 2]
    share = n // 3
    remainder = n % 3
    if n <= 3:
        return str(coun124[remainder])
    elif n > 3:
        if remainder == 0:
            result = str(coun124[share - 1]) + str(coun124[remainder])

            return result
        elif remainder == 1 or 2:
            result = str(coun124[share]) + str(coun124[remainder])

            return result


print(solution(6))


def solution(n):
    if n <= 3:
        return '124'[n - 1]
    else:
        share, remainder = divmod(n - 1, 3)
        return solution(share) + '124'[remainder]


# 풀이 1은 런타임 에러가 뜨고 그 뒤에 divmod() 함수를 알게 되었다
# divmod(n, a)는 n을 a로 나눈 몫과 나머지를 튜플로 제공 해준다.
# n - 1 인 이유는 인덱스 때문이다.
