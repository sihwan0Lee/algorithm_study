# 정수 A, B, K 가 주어진다.
# 범위 A B 안에서 K로 나눠 떨어지는애들 찾아오셈
# 참고로 A는 0부터 범위가 시작함. K는 1부터.
# 문제는 0을 어떻게 하냐인듯.
# mod == % 나머지

# 정확성 100% 퍼포먼스 50% 
def solution(A, B, K):
    div = 1
    count = 0
    for i in range(A, B+1, div):
        print(i)
        if i % K == 0:
            count += 1
            div = K
            print(i, count, div)
    return count


print(solution(6, 11, 2))
