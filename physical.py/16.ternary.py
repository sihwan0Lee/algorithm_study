# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.

def make_ternary(n):
    ternary = []
    while n >= 1:
        if n > 0:
            ternary.append(str(n % 3))
            n = (n//3)
        else:
            ternary.append(str(n))
            break
    return ''.join(ternary)


def solution(n):
    answer = 0
    ternary = (make_ternary(n))
    l = len(ternary)
    for i in ternary:
        answer += (int(i) * (3 ** (l-1)))
        l = l - 1
    return answer


# print(solution(45))


# 초기 코드가 6번쨰 줄이 if n > 3: 이었는데 , 이러면 만약 n이 3이 들어와버리면 3진법은 0 1 2 밖에 못쓰는데
# 삼진법으로 변환한게 3이 되버리는 오류가 생김.
# 상당히 피곤하고 집중이 안되서 기능만되는 정말 pythonic 하지 못한 코드라고 생각함.

def solution(n):
    while n:
        n -= 1
        print(n)


print(solution(15))
# while n:
