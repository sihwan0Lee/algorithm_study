# 길이 N인 문자열 S를 전달 받는다.
# which encodes a non-negative numver V in a binary form.
# 음수가 아닌 숫자 V를 이진 형식으로 인코딩합니다.

# 만약 V가 홀수면, 그것으로부터 1을 빼줍니다
# V가 짝수이면 2로 나눕니다.
# 이거를 V가 0이 될때까지 합니다
# S = 011100 이면  V 는 28 입니다.
# b = bin(value)
# 이진수를 10진수로 일단 바꿔야합니다.

def solution(S):
    # change bin to decimal
    V = int(S, 2)
    # 이 수가 짝수라면 2로 나누고 , 홀수라면 1을 뺸다 0이 될때 까지
    while V > 0:
        if V % 2 == 0:
            V = (V//2)
        else:
            V = (V - 1)
        print(V)


# print(solution('1111010101111'))


def solution2(S):
    count = 0
    V = int(S, 2)
    print(V)
    while V != 0:
        if V % 2 == 0:
            V = (V // 2)
        else:
            V -= 1
        count += 1
    return count


print(solution2('1'))
