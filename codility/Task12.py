# DNA 배열은 A,C,G,T 로 이루어진 문자열로 표현될수 있다.
# 충격요소들은 정수로 된걸로 각각 가진다.
# A 1, C 2 , G 3, T 4
# 주어진 디엔에이 배열에서 특정 부분이 포함되어있는 유전자 최소의 충격요소

# S = dna sequence
# P , Q 는 M개의 요소로 이뤄져있음 (0 <= K <= M)



# 62% 
def solution(S, P, Q):
    A, C, G, T = 1, 2, 3, 4
    result = []
    nucle = []
    for i in S:
        if i == 'A':
            nucle.append(1)
        elif i == 'C':
            nucle.append(2)
        elif i == 'G':
            nucle.append(3)
        elif i == 'T':
            nucle.append(4)
    print(nucle)

    for idx in range(len(P)):
        print(P[idx], Q[idx])
        value = nucle[P[idx]:Q[idx] + 1]
        result.append(min(value))

    print(result)


print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))
