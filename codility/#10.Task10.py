# 아무튼 90분에 3문제였으니까.. 최소한 25분정도까진 한문제에 끝까지 예외 생각 계속 해줘야할듯
# 비어있지않은 배열 A가 (원소 N개)가 주어진다.
# 순열은 숫자 1~N가 한번씩 들어간
# 목표는 A가 순열인지 확인할것.
# 순열이 맞다면 1을 아니라면 0을 리턴시킬것.

# 88%
def solution(A):
    # 이게 만약 확실히 등차가 1 짜리고, 1부터시작이니까.
    
    N = len(A)
    if N == max(A):
        return 1 
    else:
        return 0
        

print(solution([4, 1, 3]))

def solution(A):
    if max(A) != len(A) or len(set(A)) != len(A):
        return 0
    return 1

